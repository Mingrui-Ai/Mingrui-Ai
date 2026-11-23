"""Prepare quiet, consistently framed artwork from the daily generators."""
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import re
import shutil
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
x, y, width, height = snake_root.get('viewBox').split()
snake_root.insert(0, ET.Element(f'{{{NS}}}rect', {
    'x': x, 'y': y, 'width': width, 'height': height, 'fill': '#0d1117',
}))
ET.ElementTree(snake_root).write(snake, encoding='utf-8')
metrics = Path('/metrics_renders/deepwater-metrics.svg')
if os.environ.get('METRICS_OUTCOME') == 'success' and metrics.is_file():
    shutil.copyfile(metrics, OUT / 'metrics.svg')
    source = 'lowlighter/metrics'
else:
    # Never replace a dashboard with an error card or leave a broken image.
    shutil.copyfile(OUT / 'public-pulse.svg', OUT / 'metrics.svg')
    source = 'public GitHub REST fallback'
    print('Published the daily public-data dashboard. A scope-less classic METRICS_TOKEN enables the full Metrics dashboard.')
for name in ('city.svg', 'deepwater-snake.svg', 'metrics.svg', 'public-pulse.svg'):
    path = OUT / name
    root = ET.parse(path).getroot()
    assert root.tag.endswith('svg') and path.stat().st_size > 500, name
    assert not any(e.tag.endswith('script') for e in root.iter()), name
status = {'updated_at': datetime.now(timezone.utc).isoformat(), 'metrics_source': source}
(OUT / 'status.json').write_text(json.dumps(status, indent=2) + '\n', encoding='utf-8')
print('Validated city, snake and metrics SVGs. Metrics source:', source)
