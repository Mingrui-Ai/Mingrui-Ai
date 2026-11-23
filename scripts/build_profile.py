"""Build self-contained profile SVGs; Python 3 standard library only."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'profile'
OUT.mkdir(parents=True, exist_ok=True)
DEFS = '''<defs>
<radialGradient id="paper"><stop stop-color="#fff"/><stop offset=".66" stop-color="#eeefec"/><stop offset="1" stop-color="#c5c9c8"/></radialGradient>
<linearGradient id="chrome" x1="0" y1="0" x2="1" y2=".8"><stop stop-color="#969d9d"/><stop offset=".16" stop-color="#f9ffff"/><stop offset=".28" stop-color="#bfcacb"/><stop offset=".38" stop-color="#fff"/><stop offset=".47" stop-color="#e1d8cb"/><stop offset=".5" stop-color="#8db9c7"/><stop offset=".53" stop-color="#d2d3f5"/><stop offset=".57" stop-color="#fff"/><stop offset=".72" stop-color="#9aa7a9"/><stop offset=".86" stop-color="#eef7f5"/><stop offset="1" stop-color="#b4b9b7"/></linearGradient>
<linearGradient id="edge" x2="1" y2="1"><stop stop-color="#fafbff"/><stop offset=".32" stop-color="#96d9ec"/><stop offset=".5" stop-color="#f8ccae"/><stop offset=".65" stop-color="#d0baf1"/><stop offset="1" stop-color="#fff"/></linearGradient>
<linearGradient id="mint" x2="1" y2="1"><stop stop-color="#173c39"/><stop offset=".55" stop-color="#2d7971"/><stop offset="1" stop-color="#a6d2bc"/></linearGradient>
<linearGradient id="violet" x2="1" y2="1"><stop stop-color="#29213f"/><stop offset=".5" stop-color="#77629d"/><stop offset="1" stop-color="#d1b7d4"/></linearGradient>
<linearGradient id="ice" x2="1" y2="1"><stop stop-color="#153e52"/><stop offset=".6" stop-color="#56a4ba"/><stop offset="1" stop-color="#b9e7dc"/></linearGradient>
<linearGradient id="orange" x2="1" y2="1"><stop stop-color="#642c19"/><stop offset=".55" stop-color="#bc643c"/><stop offset="1" stop-color="#f3c495"/></linearGradient>
<radialGradient id="glow"><stop stop-color="#fff" stop-opacity=".45"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
<linearGradient id="seal" x2=".6" y2="1"><stop stop-color="#fff"/><stop offset=".7" stop-color="#e7f4ed"/><stop offset="1" stop-color="#abcac7"/></linearGradient>
<filter id="shadow" x="-.4" y="-.4" width="1.8" height="2"><feDropShadow dx="0" dy="14" stdDeviation="13" flood-color="#0b1920" flood-opacity=".24"/></filter>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".63" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="linear" slope=".1"/></feComponentTransfer><feBlend in="SourceGraphic" mode="soft-light"/></filter>
</defs>
<style>
text {font-family:Arial,Helvetica,sans-serif;fill:#202322}
.mono {font-family:'Courier New',monospace;letter-spacing:1.5px}
.white {fill:#f5f5ef}
.float {animation:drift 10s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.float-slow {animation:drift 14s ease-in-out -4s infinite;transform-box:fill-box;transform-origin:center}
@keyframes drift {0%,100% {transform:translateY(0) rotate(-2deg)}50% {transform:translateY(-14px) rotate(3deg)}}
@media (prefers-reduced-motion:reduce) {.float,.float-slow {animation:none}}
</style>'''


def svg(name, width, height, title, body, desc=''):
    (OUT / name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc or title)}</desc>
{DEFS}\n{body}\n</svg>\n''', encoding='utf-8')


def shards():
    parts = []
    for i in range(15):
        x, y = 74 + (i * 173) % 1070, 96 + (i * 91) % 380
        if 270 < x < 950 and 190 < y < 370:
            y = 115 if i % 2 else 430
        parts.append(f'''<g transform="translate({x} {y}) rotate({i * 43 % 160}) scale({.5 + i % 4 * .19})" opacity=".68"><g class="float-slow"><path d="M0 0Q12 -24 37 -21Q25 -5 15 15Z" fill="url(#chrome)" stroke="url(#edge)" stroke-width="1.6"/><path d="M0 0L37 -21L15 15Z" fill="#fff" opacity=".24"/></g></g>''')
    return ''.join(parts)


svg('hero.svg', 1200, 570, 'Mingrui Ai — Computer Science & Artificial Intelligence', f'''
<rect width="1200" height="570" fill="url(#paper)"/>
<g opacity=".45" filter="url(#grain)"><rect width="1200" height="570" fill="transparent"/></g>
<text x="36" y="55" font-size="28" letter-spacing="-1.6">mingrui<tspan font-family="Georgia,serif" font-style="italic" letter-spacing="-1"> ai</tspan><tspan font-size="11" dy="-13"> / </tspan></text>
<text x="1164" y="48" text-anchor="end" font-size="12" class="mono">CODE · EXPERIMENT · BUILD</text>
<g transform="translate(130 302) rotate(-30)" opacity=".64"><g class="float"><ellipse rx="89" ry="193" fill="none" stroke="url(#chrome)" stroke-width="37"/><ellipse rx="108" ry="211" fill="none" stroke="url(#edge)" stroke-width="2"/><ellipse rx="71" ry="175" fill="none" stroke="#fff" stroke-opacity=".65" stroke-width="2"/></g></g>
<g transform="translate(1091 302) rotate(25)" opacity=".57"><g class="float-slow"><ellipse rx="74" ry="176" fill="none" stroke="url(#chrome)" stroke-width="44"/><ellipse rx="96" ry="198" fill="none" stroke="url(#edge)" stroke-width="2"/></g></g>
{shards()}
<text x="600" y="170" text-anchor="middle" class="mono" font-size="14">COMPUTER SCIENCE / ARTIFICIAL INTELLIGENCE</text>
<text x="600" y="305" text-anchor="middle" font-size="120" letter-spacing="-8">Mingrui Ai</text>
<text x="600" y="355" text-anchor="middle" font-size="25" letter-spacing="-.6">Ideas into experiences.</text>
<rect x="440" y="395" width="320" height="35" rx="18" fill="#fff" fill-opacity=".65" stroke="#fff"/>
<circle cx="461" cy="413" r="4" fill="#4b7669"/><text x="480" y="418" font-size="12" class="mono">LLM · AGENTS · FULL STACK</text>
<path d="M36 506H1164" stroke="#9fa7a4" stroke-width=".8"/>
<text x="36" y="539" font-size="12" class="mono">SOUTH CHINA AGRICULTURAL UNIVERSITY</text>
<text x="1164" y="539" text-anchor="end" font-size="12" class="mono">SELECTED WORK ↓</text>
''', 'A silver gallery with animated glass rings and floating prismatic fragments. Mingrui Ai explores computer science, LLMs, AI agents and full-stack development.')

svg('projects.svg', 1200, 210, 'Selected Projects — four public repositories', '''
<rect width="1200" height="210" fill="url(#paper)"/>
<text x="600" y="89" text-anchor="middle" font-size="64" letter-spacing="-3.5">Selected Projects</text>
<rect x="329" y="119" width="542" height="43" rx="22" fill="#fff" fill-opacity=".8"/>
<rect x="336" y="125" width="83" height="31" rx="16" fill="#242625"/>
<text x="377" y="146" text-anchor="middle" font-size="13" class="white">All 04</text>
<text x="481" y="146" text-anchor="middle" font-size="13">AI / Agents 02</text>
<path d="M551 130V151M725 130V151" stroke="#dedfdb"/>
<text x="639" y="146" text-anchor="middle" font-size="13">Experiment 01</text>
<text x="795" y="146" text-anchor="middle" font-size="13">Open Source 01</text>
<text x="600" y="192" text-anchor="middle" class="mono" font-size="11">A FEW THINGS I AM BUILDING &amp; EXPLORING</text>
''', 'Four public repositories. Click the project cards below. Category labels are a visual index, not filtering controls.')


def card(name, title, category, number, bg, art, description):
    svg(name, 580, 444, title, f'''
<rect width="580" height="444" fill="#eeefec"/>
<defs><clipPath id="art"><rect x="14" y="14" width="552" height="322"/></clipPath></defs>
<g clip-path="url(#art)"><rect x="14" y="14" width="552" height="322" fill="url(#{bg})"/>{art}
<text x="32" y="43" font-size="10" class="white mono">{number} / SELECTED WORK</text></g>
<text x="16" y="377" font-size="30" letter-spacing="-1.2">{escape(title)}</text>
<text x="16" y="405" font-size="18">{escape(category)}</text>
<path d="M535 385L552 402M535 402H552V385" fill="none" stroke="#242625" stroke-width="2"/>
<path d="M16 426H564" stroke="#525b57" stroke-width="1"/>
''', description)


card('echosoul.svg', 'EchoSoul', 'Persona-driven AI / JavaFX', '01', 'mint', '''
<ellipse cx="400" cy="80" rx="280" ry="240" fill="url(#glow)"/>
<g transform="translate(91 75) rotate(-7 202 120)"><g class="float" filter="url(#shadow)">
<rect width="405" height="227" rx="10" fill="#0f2423" stroke="#9cb4a6" stroke-width="1.5"/>
<path d="M0 28H405M112 28V227" stroke="#4f6b61" stroke-opacity=".6"/>
<circle cx="14" cy="14" r="3" fill="#f0b4a0"/><circle cx="25" cy="14" r="3" fill="#e0cf93"/><circle cx="36" cy="14" r="3" fill="#abd0b2"/>
<text x="202" y="18" text-anchor="middle" class="white" font-size="10">EchoSoul</text>
<text x="16" y="54" class="white" font-size="11">Your personas</text>
<rect x="9" y="67" width="94" height="31" rx="5" fill="#355c51"/>
<circle cx="26" cy="82" r="9" fill="#b6d6c8"/><text x="43" y="86" class="white" font-size="9">Conversation</text>
<path d="M17 119H86M17 138H70M17 157H80" stroke="#72968b" stroke-width="5" stroke-linecap="round" opacity=".6"/>
<text x="132" y="55" class="white" font-size="13">A little more human.</text>
<rect x="179" y="77" width="205" height="33" rx="8" fill="#d3e6d9"/>
<text x="192" y="98" font-size="10">Where should we begin?</text>
<rect x="130" y="123" width="218" height="49" rx="8" fill="#29483f"/>
<text x="142" y="143" class="white" font-size="10">With an idea. And a conversation.</text>
<path d="M143 155H284" stroke="#749588" stroke-width="3" stroke-linecap="round"/>
<rect x="130" y="188" width="256" height="24" rx="12" fill="#1b3730" stroke="#4c6e60"/>
<text x="143" y="204" class="white" font-size="9">Say something...</text>
<path d="M367 196L373 200L367 204" fill="none" stroke="#bdd9c9" stroke-width="1.5"/>
</g></g><text x="39" y="315" font-size="10" class="white mono">LOCAL FIRST · MULTIPLE AI PROVIDERS</text>
''', 'EchoSoul: a JavaFX desktop chat app with persona-driven conversations, pluggable LLM providers, local history and optional speech. Conceptual interface illustration.')

card('job-search.svg', 'AI Job Search CN', 'Local-first agent workflow / Python', '02', 'violet', '''
<ellipse cx="430" cy="265" rx="320" ry="280" fill="url(#glow)"/>
<g transform="translate(89 65) rotate(-8 150 120)"><g class="float-slow" filter="url(#shadow)">
<rect x="27" width="282" height="224" rx="3" fill="#c6bfd5"/><rect x="13" y="9" width="282" height="224" rx="3" fill="#e0d9e8"/>
<rect y="20" width="282" height="224" rx="3" fill="#f8f4f0"/>
<text x="22" y="51" font-size="10" class="mono">OPPORTUNITY / 001</text>
<text x="22" y="87" font-size="26" letter-spacing="-.8">Find your next.</text>
<path d="M22 106H257" stroke="#bbb2bc"/><text x="22" y="128" font-size="10">CHINESE JD → STRUCTURED EVIDENCE</text>
<path d="M22 146H175M22 159H228M22 172H201" stroke="#c2b8c5" stroke-width="4"/>
<rect x="22" y="191" width="119" height="29" rx="15" fill="#5d4a72"/>
<text x="81" y="210" class="white" font-size="10" text-anchor="middle">Explainable matching</text>
</g></g>
<g transform="translate(360 117) rotate(15)"><g class="float" filter="url(#shadow)">
<rect width="126" height="142" rx="8" fill="#27213b" stroke="#baafce"/>
<circle cx="63" cy="50" r="25" fill="none" stroke="#c6e6cf" stroke-width="2"/>
<path d="M50 50L59 60L77 39" fill="none" stroke="#c6e6cf" stroke-width="3"/>
<text x="63" y="102" class="white" font-size="11" text-anchor="middle">EVIDENCE</text>
<text x="63" y="120" class="white" font-size="9" text-anchor="middle">BEFORE GUESSWORK</text>
</g></g><text x="39" y="315" font-size="10" class="white mono">CN ADAPTATION · IN DEVELOPMENT</text>
''', 'An in-development Chinese-market adaptation of ai-job-search: Chinese JD parsing, evidence validation and explainable matching. Python, Codex and Claude Code.')

card('lil-seal.svg', 'lil-seal', 'A small web experiment / JavaScript', '03', 'ice', '''
<ellipse cx="340" cy="80" rx="300" ry="280" fill="url(#glow)"/>
<ellipse cx="305" cy="285" rx="155" ry="18" fill="#244c57" opacity=".2"/>
<ellipse cx="300" cy="283" rx="220" ry="39" fill="none" stroke="#cbf2ed" stroke-opacity=".4"/><ellipse cx="300" cy="283" rx="265" ry="59" fill="none" stroke="#cbf2ed" stroke-opacity=".2"/>
<g class="float" filter="url(#shadow)">
<path d="M372 251Q431 217 461 245Q450 281 389 278Z" fill="url(#seal)"/>
<path d="M174 258Q130 215 157 162Q174 109 230 107Q286 102 316 160Q333 188 376 204Q413 220 408 254Q398 283 300 280Q210 282 174 258Z" fill="url(#seal)"/>
<path d="M247 230Q286 224 314 265Q265 286 241 248Z" fill="#d1e4df"/>
<ellipse cx="186" cy="180" rx="5.5" ry="7" fill="#233d42"/><ellipse cx="239" cy="178" rx="5.5" ry="7" fill="#233d42"/>
<ellipse cx="211" cy="200" rx="8" ry="6" fill="#4a666c"/>
<path d="M211 205Q204 217 197 210M211 205Q218 217 225 210" fill="none" stroke="#536f74" stroke-width="2"/>
<path d="M182 199L158 194M182 205L155 207M239 197L264 191M239 204L267 206" stroke="#759394" stroke-width="1.5"/>
<ellipse cx="179" cy="199" rx="10" ry="5" fill="#e7b8b7" opacity=".5"/><ellipse cx="242" cy="196" rx="10" ry="5" fill="#e7b8b7" opacity=".5"/>
</g><g fill="none" stroke="#d0f7f0" opacity=".6"><circle cx="105" cy="100" r="12"/><circle cx="454" cy="95" r="7"/><circle cx="425" cy="64" r="4"/></g>
<text x="39" y="315" font-size="10" class="white mono">A LITTLE CURIOSITY, ON THE WEB.</text>
''', 'lil-seal: a small JavaScript web experiment featuring a cute seal. Original vector cover illustration.')

card('linuxdo.svg', 'LinuxDo Android', 'Community client / Kotlin · Fork', '04', 'orange', '''
<ellipse cx="330" cy="100" rx="300" ry="260" fill="url(#glow)"/>
<g transform="translate(212 46) rotate(14 82 140)"><g class="float-slow" filter="url(#shadow)">
<rect width="168" height="304" rx="23" fill="#192120" stroke="url(#chrome)" stroke-width="4"/><rect x="8" y="8" width="152" height="288" rx="16" fill="#f1eee7"/>
<rect x="61" y="12" width="46" height="10" rx="5" fill="#192120"/>
<circle cx="32" cy="56" r="13" fill="#e5b266"/><text x="54" y="62" font-size="16" letter-spacing="-.5">LINUX DO</text>
<path d="M20 82H148" stroke="#b2b5ad"/><text x="20" y="105" font-size="11">Community, connected.</text>
<rect x="18" y="120" width="132" height="44" rx="5" fill="#fff"/><circle cx="34" cy="137" r="7" fill="#c2d8d3"/><path d="M49 135H132M49 145H113" stroke="#b1bdb5" stroke-width="4"/>
<rect x="18" y="174" width="132" height="44" rx="5" fill="#fff"/><circle cx="34" cy="191" r="7" fill="#d7c2b2"/><path d="M49 189H132M49 199H104" stroke="#b1bdb5" stroke-width="4"/>
<rect x="18" y="228" width="132" height="44" rx="5" fill="#fff"/><circle cx="34" cy="245" r="7" fill="#c6c4de"/><path d="M49 243H132M49 253H118" stroke="#b1bdb5" stroke-width="4"/>
</g></g><text x="52" y="173" font-size="58" class="white" opacity=".18" letter-spacing="-3">{ }</text>
<text x="434" y="240" font-size="54" class="white" opacity=".25">↗</text>
<text x="39" y="315" font-size="10" class="white mono">EXPLORING OPEN SOURCE · ANDROID</text>
''', "Mingrui Ai's fork of xuemk/linuxdo-android, a Kotlin Android client for LinuxDo. Conceptual interface illustration, not a product screenshot.")

svg('contact.svg', 1200, 235, "Let's build something — mingrui.ai@outlook.com", '''
<rect width="1200" height="235" fill="url(#paper)"/>
<text x="42" y="50" font-size="12" class="mono">HAVE AN IDEA?</text>
<text x="40" y="129" font-size="66" letter-spacing="-3">Let's build something.</text>
<path d="M1087 68L1149 130M1087 130H1149V68" fill="none" stroke="#252a27" stroke-width="3"/>
<path d="M42 164H1158" stroke="#9fa7a4"/>
<text x="42" y="201" font-size="17">mingrui.ai@outlook.com</text>
<text x="1158" y="201" text-anchor="end" font-size="12" class="mono">MINGRUI AI / ALWAYS EXPLORING</text>
''')
print(f"Built {len(list(OUT.glob('*.svg')))} SVG assets in {OUT}")
