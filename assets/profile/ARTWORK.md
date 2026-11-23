# Deepwater / v2

Original artwork inspired by Unseen Studio's immersive presentation, adapted to
GitHub README constraints: near-black panels, refracted typography, a luminous
blue cube above water, glass project covers, fine rules and diagonal arrows.
No reference-site photographs, fonts, logo or source code are included. Interface
illustrations are conceptual covers, not screenshots. LinuxDo is labeled as a fork.

## Artwork

Run `python scripts/build_profile.py` with Python 3 (standard library only).
The SVGs are self-contained, with system fonts and no scripts or external assets.
The hero uses `feTurbulence` + `feDisplacementMap`, with SMIL animating noise
frequency and displacement strength. CSS supplies slow object movement.
`prefers-reduced-motion` replaces the animated hero group with an unfiltered
static wordmark and disables CSS movement. There is no WebGL or cursor tracking.

## Daily generation

`.github/workflows/deepwater.yml` runs at **04:23 Asia/Shanghai** (20:23 UTC)
daily, on workflow/configuration changes, or via **Run workflow**. Scheduled
Actions can run late; GitHub may disable schedules after 60 days of repository
inactivity. A single job commits generated assets together, only when changed.

- **City:** `yoshi389111/github-profile-3d-contrib`, pinned v0.9.3, customized
  using `.github/profile/city.json`.
- **Snake:** `Platane/snk/svg-only`, pinned v3, customized blue palette and an
  opaque background for light and dark GitHub themes.
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
a disclosure. Alt text describes every meaningful image. Navigation and project
links are native GitHub links. Category pills are visual labels, not filters.
GitHub still controls the surrounding page, margins and profile sidebar; the
dark panels cannot recolor that surrounding interface. Generated graphics may
remain cached briefly after a successful update.
