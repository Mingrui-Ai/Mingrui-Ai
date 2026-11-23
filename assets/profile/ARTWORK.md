# Deepwater / liquid gallery

Original artwork inspired by Unseen Studio's immersive presentation, adapted to
GitHub README constraints: a neutral dark canvas, a liquid-light gyroscope,
saturated project illustrations and alternating full-width compositions.
No reference-site photographs, fonts, logo or source code are included. Interface
illustrations are conceptual covers, not screenshots. LinuxDo is labeled as a fork.

## Artwork

Run `python scripts/build_profile.py` with Python 3 (standard library only).
The SVGs are self-contained, with system fonts and no scripts or external assets.
The hero uses pure SVG gradients, layered translucent orbits and CSS animation:
opposing 10- and 16-second orbit rotations, 2.7-/2.9-second traveling highlights,
a 12px float over 3.8 seconds and a 2.5-second breathing core. Complete tracks
are reused for the clipped foreground halves, preserving their centered pivots
and synchronized motion. Three expanding water ripples remain staggered by
1.5 seconds, with a restrained seven-second wordmark highlight.

Project motion is local to each illustration, with one or two moving focal
points per row: staggered voice peaks in EchoSoul; traveling circuit light and
a three-second match halo for AI Job Search CN; two staggered rising bubbles
and a quick four-second blink for lil-seal; a 4.8-second orbiting light and
top-to-bottom card brightness wave for LinuxDo Android. The interfaces, text
and project compositions stay still. All local CSS rotation and scaling use
`transform-box: fill-box` and `transform-origin: center`.

A teal contact dot breathes decoratively; it is not a real-time presence
signal. `prefers-reduced-motion` disables all artwork animations and hides
transient light effects while keeping the complete static composition.
There is no WebGL or cursor tracking.

The canvas is `#0d1117`, matching GitHub's default dark theme. Four 840×240 rows
alternate illustration and text, with a low-contrast number, a 28px title and
one 12px uppercase label. Color is concentrated in the subjects: cyan/purple,
amber/emerald, pearl/ice blue and coral/orange. There are no card frames or tiny
interface captions. LinuxDo's label retains its fork attribution. The default
Activity view contains the snake and a 60px data strip; the city and dashboard
are in ARCHIVE, with the biography in a separate disclosure.

## Daily generation

`.github/workflows/deepwater.yml` runs at **04:23 Asia/Shanghai** (20:23 UTC)
daily, on workflow/configuration changes, or via **Run workflow**. Scheduled
Actions can run late; GitHub may disable schedules after 60 days of repository
inactivity. A single job commits generated assets together, only when changed.

- **City:** `yoshi389111/github-profile-3d-contrib`, pinned v0.9.3, customized
  using `.github/profile/city.json`. `prepare_generated.py` retains the original
  blocks and growth animation, removes the extra charts and counters, and uses
  a shallower projection with calculated vertical bounds for a compact composition.
- **Snake:** `Platane/snk/svg-only`, pinned v3. Preparation keeps the real route
  and calendar, removes the lower tally bar, uses `#161b22` empty cells, and
  applies a continuous cyan-to-purple color progression across the body
  segments. The background covers the complete viewBox, including its negative
  origin. Calendar and snake animation stop under reduced-motion preferences.
- **Data strip:** public repository count and top three languages by source
  bytes come from `public-summary.json`, refreshed by the public REST script.
  The annual count reuses `contributionCalendar.totalContributions` as rendered
  in the pinned city generator's summary. It is labeled contributions, not
  commits. The daily Actions token sees public contributions and repositories;
  these can differ from the owner's signed-in profile totals. No numbers are
  hard-coded from screenshots.
- **Metrics:** `lowlighter/metrics`, pinned v3.34, includes base statistics,
  languages, habits and compact achievements when `METRICS_TOKEN` is set.
- **Public dashboard:** `scripts/refresh_dashboard.py` always refreshes real
  public REST data. It becomes `metrics.svg` if the Metrics token is absent or
  the upstream generator fails. It shows public repository/star/follower counts,
  language byte proportions and explicitly bounded recent public-event counts.
  It does not pretend to supply lowlighter achievement badges.

The city and snake use GitHub's automatic repository token. The public dashboard
queries public endpoints only. `assets/generated/status.json` identifies which
dashboard was published and when; no credentials or private repository names
are written into any output.

## Enabling full lowlighter Metrics

Upstream v3.34 requires a **classic personal access token**, even for public data;
it rejects the automatic Actions token and fine-grained tokens. A classic token
with **no scopes selected** is sufficient for the configured public-data features.

1. Create that token in GitHub's developer settings.
2. Add it as a repository Actions secret called `METRICS_TOKEN` at
   `https://github.com/Mingrui-Ai/Mingrui-Ai/settings/secrets/actions`.
3. Run **Deepwater daily visuals** from the Actions tab. Check `status.json` for
   `"metrics_source": "lowlighter/metrics"` and inspect the rendered panel.

No local CLI credential is copied to Actions. Token creation and configuration
are separate from the already-operational city, snake and public dashboard.

## Editing and rendering

The original bilingual biography and project notes remain available as text in
a disclosure. Alt text describes every meaningful image. Project and contact
links are native GitHub links. GitHub controls the surrounding page, margins and
profile sidebar; other GitHub themes may expose the dark artwork's boundaries.
Generated graphics may remain cached briefly after a successful update.

Visual reference: https://unseen.co/projects/
Daily generators: https://github.com/yoshi389111/github-profile-3d-contrib,
https://github.com/Platane/snk and https://github.com/lowlighter/metrics.
