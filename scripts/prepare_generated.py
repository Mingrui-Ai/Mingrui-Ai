"""Normalize the three generators into stable README asset paths."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/generated'
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(ROOT / 'profile-3d-contrib/deepwater-city.svg', OUT / 'city.svg')
snake = OUT / 'deepwater-snake.svg'
text = snake.read_text(encoding='utf-8')
# GitHub also renders this in light mode, so the SVG carries its own dark panel.
text = re.sub(r'(<svg\b[^>]*>)', r'\1<rect width="100%" height="100%" fill="#070d18"/>', text, count=1)
snake.write_text(text, encoding='utf-8')
metrics = Path('/metrics_renders/deepwater-metrics.svg')
if os.environ.get('METRICS_OUTCOME') == 'success' and metrics.is_file():
    shutil.copyfile(metrics, OUT / 'metrics.svg')
    source = 'lowlighter/metrics'
else:
    # Never replace a dashboard with an error card or leave a broken image.
    shutil.copyfile(OUT / 'public-pulse.svg', OUT / 'metrics.svg')
    source = 'public GitHub REST fallback'
    print('::warning::Metrics unavailable; published the daily public-data fallback. A scope-less METRICS_TOKEN can enable the full Metrics dashboard.')
for name in ('city.svg', 'deepwater-snake.svg', 'metrics.svg', 'public-pulse.svg'):
    path = OUT / name
    root = ET.parse(path).getroot()
    assert root.tag.endswith('svg') and path.stat().st_size > 500, name
    assert not any(e.tag.endswith('script') for e in root.iter()), name
status = {'updated_at': datetime.now(timezone.utc).isoformat(), 'metrics_source': source}
(OUT / 'status.json').write_text(json.dumps(status, indent=2) + '\n', encoding='utf-8')
print('Validated city, snake and metrics SVGs. Metrics source:', source)
