"""Prepare quiet, consistently framed artwork from the daily generators."""
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import re
import shutil
from html import escape
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/generated'
OUT.mkdir(parents=True, exist_ok=True)
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)

# Keep the contribution blocks and their original animation, without the
# duplicate radar, language chart, counters and captions. A shallow projection
# lets the city flow across the page while keeping the buildings vertical.
city = ET.parse(ROOT / 'profile-3d-contrib/deepwater-city.svg').getroot()
# The pinned generator exposes contributionCalendar.totalContributions in the
# summary next to the literal "contributions" label. Reuse the same dataset;
# do not mislabel this aggregate (commits, issues, PRs...) as a commit count.
totals = [g for g in city.findall(f'{{{NS}}}g') if any(
    e.tag == f'{{{NS}}}text' and e.text == 'contributions' for e in g)]
assert len(totals) == 1, 'Missing upstream contribution summary'
counts = [e.text for e in totals[0] if e.get('class') == 'fill-strong']
assert len(counts) == 1 and counts[0].isdigit(), 'Invalid contribution total'
contributions = int(counts[0])
groups = [g for g in city.findall(f'{{{NS}}}g') if any(
    e.get('class', '').startswith('cont-top-') for e in g.iter())]
assert len(groups) == 1, 'Unexpected upstream city structure'
blocks = groups[0]
shear = -0.36
bounds = []
for block in blocks:
    transform = re.fullmatch(r'translate\(([-\d.]+) ([-\d.]+)\)', block.get('transform', ''))
    assert transform is not None, 'Unexpected contribution block transform'
    x, y = map(float, transform.groups())
    heights = [float(e.get('height', 0)) for e in block.findall(f'{{{NS}}}rect')]
    assert heights, 'Empty contribution block'
    # Conservative bounds include all three faces and the growth animation.
    bounds.extend((y + shear * x - 30, y + shear * x + max(heights) * 1.15 + 30))
top, bottom = math.floor(min(bounds) - 20), math.ceil(max(bounds) + 20)
height = bottom - top
result = ET.Element(f'{{{NS}}}svg', {
    'width': '1280', 'height': str(height), 'viewBox': f'0 {top} 1280 {height}',
    'role': 'img', 'aria-labelledby': 'title desc',
})
ET.SubElement(result, f'{{{NS}}}title', {'id': 'title'}).text = 'A year of contributions'
ET.SubElement(result, f'{{{NS}}}desc', {'id': 'desc'}).text = (
    'Real GitHub contributions, updated daily. Building heights and colors come '
    'from github-profile-3d-contrib; the surrounding statistics are available in the dashboard.')
result.append(city.find(f'{{{NS}}}style'))
ET.SubElement(result, f'{{{NS}}}rect', {
    'x': '0', 'y': str(top), 'width': '1280', 'height': str(height), 'fill': '#0d1117',
})
frame = ET.SubElement(result, f'{{{NS}}}g', {'transform': f'matrix(1 {shear} 0 1 0 0)'})
frame.append(blocks)
ET.ElementTree(result).write(OUT / 'city.svg', encoding='utf-8')

snake = OUT / 'deepwater-snake.svg'
snake_root = ET.parse(snake).getroot()
# Cover the entire viewBox, including its negative origin. Re-running this
# preparation replaces the existing background instead of stacking rectangles.
for child in list(snake_root):
    if child.tag == f'{{{NS}}}rect' and not child.get('class') and child.get('fill'):
        snake_root.remove(child)
    elif child.tag == f'{{{NS}}}rect' and 'u' in child.get('class', '').split():
        snake_root.remove(child)  # No second animated tally bar under the snake.
    elif child.get('id') == 'gallery-snake-defs':
        snake_root.remove(child)
snake_root.set('viewBox', '-16 -32 880 160')
snake_root.set('height', '160')
styles = snake_root.find(f'{{{NS}}}style')
assert styles is not None and styles.text, 'Snake animation stylesheet is missing'
colors = {'--cb': '#0d1117', '--cs': '#22d3ee', '--ce': '#161b22',
          '--c0': '#161b22', '--c1': '#202c38', '--c2': '#304255',
          '--c3': '#485978', '--c4': '#66709b'}
for key, color in colors.items():
    styles.text = re.sub(re.escape(key) + r':[^;}]+', key + ':' + color, styles.text)
defs = ET.SubElement(snake_root, f'{{{NS}}}defs', {'id': 'gallery-snake-defs'})
segments = [e for e in snake_root if 's' in e.get('class', '').split()]
assert len(segments) > 1, 'Expected an animated snake with multiple segments'
def shade(t):
    start, end = (34, 211, 238), (168, 85, 247)
    return '#' + ''.join(f'{round(a + (b-a)*t):02x}' for a, b in zip(start, end))
for i, segment in enumerate(segments):
    gradient = ET.SubElement(defs, f'{{{NS}}}linearGradient', {
        'id': f'snake-{i}', 'x1': '0', 'y1': '0', 'x2': '1', 'y2': '1',
    })
    for offset, t in [('0', i / len(segments)), ('1', (i+1) / len(segments))]:
        ET.SubElement(gradient, f'{{{NS}}}stop', {'offset': offset, 'stop-color': shade(t)})
    segment.set('style', f'fill:url(#snake-{i})')
if 'prefers-reduced-motion' not in styles.text:
    styles.text += '\n@media(prefers-reduced-motion:reduce){.c,.s{animation:none!important}}'
x, y, width, height = snake_root.get('viewBox').split()
snake_root.insert(0, ET.Element(f'{{{NS}}}rect', {
    'x': x, 'y': y, 'width': width, 'height': height, 'fill': '#0d1117',
}))
ET.ElementTree(snake_root).write(snake, encoding='utf-8')

summary = json.loads((OUT / 'public-summary.json').read_text(encoding='utf-8'))
abbreviations = {'TypeScript': 'TS', 'JavaScript': 'JS', 'Jupyter Notebook': 'JUPYTER'}
languages = ' · '.join(abbreviations.get(s, s.upper()) for s in summary['top_languages_by_bytes'])
labels = [f'{contributions:,} CONTRIBUTIONS · 1Y',
          f"{summary['public_repositories']:,} PUBLIC REPOS", languages or 'EXPLORING']
strip = f'''<svg xmlns="{NS}" width="840" height="60" viewBox="0 0 840 60" role="img" aria-labelledby="title desc">
<title id="title">GitHub activity at a glance</title>
<desc id="desc">{contributions:,} public contributions in the last year, including commits, issues and pull requests; {summary['public_repositories']} public repositories. Top languages by source bytes in public original repositories: {escape(', '.join(summary['top_languages_by_bytes']))}. Updated {escape(summary['updated_at'])}.</desc>
<rect width="840" height="60" fill="#0d1117"/>
<style>text{{font-family:Arial,Helvetica,sans-serif;font-size:12px;letter-spacing:1.5px;fill:#8b949e}}</style>
<text x="20" y="36">{escape(labels[0])}</text><text x="423" y="36" text-anchor="middle">{escape(labels[1])}</text><text x="820" y="36" text-anchor="end">{escape(labels[2])}</text>
<path d="M305 24L300 38M551 24L546 38" stroke="#30363d"/>
</svg>'''
(OUT / 'activity-strip.svg').write_text(strip, encoding='utf-8')
metrics = Path('/metrics_renders/deepwater-metrics.svg')
if os.environ.get('METRICS_OUTCOME') == 'success' and metrics.is_file():
    shutil.copyfile(metrics, OUT / 'metrics.svg')
    source = 'lowlighter/metrics'
else:
    # Never replace a dashboard with an error card or leave a broken image.
    shutil.copyfile(OUT / 'public-pulse.svg', OUT / 'metrics.svg')
    source = 'public GitHub REST fallback'
    print('Published the daily public-data dashboard. A scope-less classic METRICS_TOKEN enables the full Metrics dashboard.')
for name in ('city.svg', 'deepwater-snake.svg', 'metrics.svg', 'public-pulse.svg', 'activity-strip.svg'):
    path = OUT / name
    root = ET.parse(path).getroot()
    assert root.tag.endswith('svg') and path.stat().st_size > 500, name
    assert not any(e.tag.endswith('script') for e in root.iter()), name
status = {'updated_at': datetime.now(timezone.utc).isoformat(), 'metrics_source': source}
(OUT / 'status.json').write_text(json.dumps(status, indent=2) + '\n', encoding='utf-8')
print('Validated city, snake and metrics SVGs. Metrics source:', source)
