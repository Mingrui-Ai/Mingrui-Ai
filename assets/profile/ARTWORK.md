# Profile artwork

The visual direction references [Unseen Studio's projects page](https://unseen.co/projects/): silver-white space, oversized sans-serif typography, refractive objects, a two-column project gallery, fine divider rules and diagonal arrows.

All illustrations here are original, code-generated SVGs. No Unseen Studio project photographs, fonts, logo, source code or client work are included. Interface illustrations are conceptual covers, not screenshots. The LinuxDo card explicitly identifies the repository as a fork.

Regenerate with `python scripts/build_profile.py` (Python 3 standard library only). The seven SVGs are self-contained: system font stacks, no scripts, no foreignObject and no external assets. CSS animations run inside the images and respect `prefers-reduced-motion`; every asset also has a complete static state.

GitHub supplies the README layout. Category pills are visual labels, not filtering controls. Project cards, navigation links, disclosures and contact links use GitHub-supported Markdown/HTML. WebGL distortion, cursor effects, audio and scroll-linked movement cannot run inside a GitHub README.

The original bilingual introduction and third-party stats are retained. Stats are folded away so their availability does not determine the gallery's appearance.
