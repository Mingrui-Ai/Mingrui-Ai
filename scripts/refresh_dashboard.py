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
    ('PUBLIC REPOSITORIES', len(repos)),
    ('STARS RECEIVED', sum(r['stargazers_count'] for r in originals)),
    ('FOLLOWERS', account['followers']),
    ('PUBLIC ORIGINALS', len(originals)),
]
parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="590" viewBox="0 0 1200 590" role="img" aria-labelledby="title desc">
<title id="title">{escape(USER)} — public GitHub pulse</title>
<desc id="desc">Daily public GitHub data. Languages are bytes of code in public non-fork repositories. Activity is sampled from the latest {len(events)} public events returned by GitHub, not lifetime totals.</desc>
<style>text{{font-family:Arial,Helvetica,sans-serif;fill:#d9f2ff}}.dim{{fill:#7896b2}}.mono{{font-family:monospace;letter-spacing:1px}}</style>
<rect width="1200" height="590" fill="#070d18"/>
<path d="M44 86H1156M44 228H1156" stroke="#19314d"/>
<text x="44" y="54" font-size="28">Open-source pulse</text>
<text x="1156" y="52" text-anchor="end" class="mono dim" font-size="12">PUBLIC GITHUB DATA / DAILY</text>''']
for i, (label, value) in enumerate(cards):
    x = 44 + i * 284
    parts.append(f'<text x="{x}" y="161" font-size="52">{value:,}</text><text x="{x}" y="196" font-size="11" class="mono dim">{label}</text>')
parts.append('<text x="44" y="274" font-size="18">Languages / public source bytes</text>')
total = sum(languages.values()) or 1
palette = ['#85ecff', '#299cff', '#6f8fff', '#997cdb', '#4eb3bc', '#456d99']
for i, (language, size) in enumerate(languages.most_common(6)):
    y = 311 + i * 31
    percent = size / total * 100
    parts.append(f'<text x="44" y="{y}" font-size="14">{escape(language)}</text><rect x="178" y="{y-11}" width="{max(1,percent*3.7):.1f}" height="10" rx="5" fill="{palette[i]}"/><text x="570" y="{y}" text-anchor="end" font-size="13" class="dim">{percent:.1f}%</text>')
parts.append(f'<text x="646" y="274" font-size="18">Recent public activity / {len(events)} events</text>')
labels = [('PushEvent', 'Push events'), ('PullRequestEvent', 'Pull request events'), ('IssuesEvent', 'Issue events'), ('IssueCommentEvent', 'Issue comments'), ('CreateEvent', 'Branches & repositories created')]
for i, (kind, label) in enumerate(labels):
    y = 312 + i * 34
    parts.append(f'<text x="646" y="{y}" font-size="14" class="dim">{label}</text><text x="1156" y="{y}" text-anchor="end" font-size="18">{types[kind]}</text>')
parts.append(f'<path d="M44 530H1156" stroke="#19314d"/><text x="44" y="564" class="mono dim" font-size="11">UPDATED {now:%Y-%m-%d %H:%M} UTC+08</text><text x="1156" y="564" text-anchor="end" class="mono dim" font-size="11">GITHUB REST API / NO ESTIMATED VALUES</text></svg>')
(OUT / 'public-pulse.svg').write_text(''.join(parts), encoding='utf-8')
print(f'Generated factual public dashboard for {USER}; {len(repos)} public repositories.')
