"""A daily, factual public-data dashboard and fallback for Metrics outages.

Only public GitHub REST endpoints are queried. The short-lived Actions token is
read from the environment and never written to artifacts or logs.
"""
from collections import Counter
from datetime import datetime, timedelta, timezone
from html import escape
import json
import os
from pathlib import Path
import urllib.request

OUT = Path(__file__).resolve().parents[1] / 'assets/generated'
OUT.mkdir(parents=True, exist_ok=True)
USER = os.environ.get('PROFILE_USER', 'Mingrui-Ai')
TOKEN = os.environ.get('GH_TOKEN', '')


def api(path):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'deepwater-profile'}
    if TOKEN:
        headers['Authorization'] = f'Bearer {TOKEN}'
    request = urllib.request.Request(f'https://api.github.com/{path}', headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


account = api(f'users/{USER}')
repos = []
page = 1
while True:
    batch = api(f'users/{USER}/repos?type=owner&per_page=100&page={page}')
    repos.extend(r for r in batch if not r['private'])
    if len(batch) < 100:
        break
    page += 1
originals = [r for r in repos if not r['fork']]
languages = Counter()
for repo in originals:
    languages.update(api(f"repos/{USER}/{repo['name']}/languages"))
events = api(f'users/{USER}/events/public?per_page=100')
types = Counter(e['type'] for e in events)
now = datetime.now(timezone(timedelta(hours=8)))
cards = [
    ('Public repositories', len(repos)),
    ('Stars received', sum(r['stargazers_count'] for r in originals)),
    ('Followers', account['followers']),
]
parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="590" viewBox="0 0 1200 590" role="img" aria-labelledby="title desc">
<title id="title">{escape(USER)} — public GitHub pulse</title>
<desc id="desc">Daily public GitHub data. Languages are bytes of code in public non-fork repositories. Activity is sampled from the latest {len(events)} public events returned by GitHub, not lifetime totals.</desc>
<style>text{{font-family:Arial,Helvetica,sans-serif;fill:#e0e6eb}}.dim{{fill:#97a6b3}}</style>
<rect width="1200" height="590" fill="#0d1117"/>
<text x="24" y="60" font-size="42">GitHub activity</text>''']
for i, (label, value) in enumerate(cards):
    x = 24 + i * 400
    parts.append(f'<text x="{x}" y="159" font-size="60">{value:,}</text><text x="{x}" y="198" font-size="24" class="dim">{label}</text>')
parts.append('<path d="M24 235H1176" stroke="#28313c"/><text x="24" y="287" font-size="27">Languages</text>')
total = sum(languages.values()) or 1
palette = ['#b4d2e3', '#8aaec5', '#638ca8', '#46677f']
for i, (language, size) in enumerate(languages.most_common(4)):
    y = 338 + i * 44
    percent = size / total * 100
    parts.append(f'<text x="24" y="{y}" font-size="23">{escape(language)}</text><rect x="185" y="{y-14}" width="{max(1,percent*2.7):.1f}" height="11" rx="5.5" fill="{palette[i]}"/><text x="555" y="{y}" text-anchor="end" font-size="23" class="dim">{percent:.1f}%</text>')
parts.append(f'<text x="650" y="287" font-size="27">Latest {len(events)} public events</text>')
labels = [('PushEvent', 'Pushes'), ('PullRequestEvent', 'Pull request events'), ('IssuesEvent', 'Issue events'), ('IssueCommentEvent', 'Issue comments')]
for i, (kind, label) in enumerate(labels):
    y = 338 + i * 44
    parts.append(f'<text x="650" y="{y}" font-size="23" class="dim">{escape(label)}</text><text x="1176" y="{y}" text-anchor="end" font-size="25">{types[kind]}</text>')
parts.append(f'<path d="M24 517H1176" stroke="#28313c"/><text x="24" y="559" class="dim" font-size="20">Languages by public source bytes</text><text x="1176" y="559" text-anchor="end" class="dim" font-size="20">{now:%Y-%m-%d %H:%M} UTC+08</text></svg>')
(OUT / 'public-pulse.svg').write_text(''.join(parts), encoding='utf-8')
summary = {
    'public_repositories': len(repos),
    'top_languages_by_bytes': [name for name, _ in languages.most_common(3)],
    'updated_at': now.isoformat(),
}
(OUT / 'public-summary.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
print(f'Generated factual public dashboard for {USER}; {len(repos)} public repositories.')
