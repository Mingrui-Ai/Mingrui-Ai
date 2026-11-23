"""Build Deepwater v2: self-contained dark SVG artwork and water refraction."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'profile'
OUT.mkdir(parents=True, exist_ok=True)
DEFS = '''<defs>
<radialGradient id="paper"><stop stop-color="#0e2640"/><stop offset=".65" stop-color="#080f1c"/><stop offset="1" stop-color="#070d18"/></radialGradient>
<linearGradient id="chrome" x1="0" y1="0" x2="1" y2=".8"><stop stop-color="#969d9d"/><stop offset=".16" stop-color="#f9ffff"/><stop offset=".28" stop-color="#bfcacb"/><stop offset=".38" stop-color="#fff"/><stop offset=".47" stop-color="#e1d8cb"/><stop offset=".5" stop-color="#8db9c7"/><stop offset=".53" stop-color="#d2d3f5"/><stop offset=".57" stop-color="#fff"/><stop offset=".72" stop-color="#9aa7a9"/><stop offset=".86" stop-color="#eef7f5"/><stop offset="1" stop-color="#b4b9b7"/></linearGradient>
<linearGradient id="edge" x2="1" y2="1"><stop stop-color="#fafbff"/><stop offset=".32" stop-color="#96d9ec"/><stop offset=".5" stop-color="#f8ccae"/><stop offset=".65" stop-color="#d0baf1"/><stop offset="1" stop-color="#fff"/></linearGradient>
<linearGradient id="mint" x2="1" y2="1"><stop stop-color="#070f1c"/><stop offset=".55" stop-color="#10243c"/><stop offset="1" stop-color="#17374e"/></linearGradient>
<linearGradient id="violet" x2="1" y2="1"><stop stop-color="#0b1020"/><stop offset=".5" stop-color="#182444"/><stop offset="1" stop-color="#253a61"/></linearGradient>
<linearGradient id="ice" x2="1" y2="1"><stop stop-color="#061421"/><stop offset=".6" stop-color="#10324a"/><stop offset="1" stop-color="#1e5364"/></linearGradient>
<linearGradient id="orange" x2="1" y2="1"><stop stop-color="#07121c"/><stop offset=".55" stop-color="#142b45"/><stop offset="1" stop-color="#23435c"/></linearGradient>
<radialGradient id="glow"><stop stop-color="#399fff" stop-opacity=".28"/><stop offset="1" stop-color="#399fff" stop-opacity="0"/></radialGradient>
<linearGradient id="seal" x2=".6" y2="1"><stop stop-color="#c8f0ff" stop-opacity=".94"/><stop offset=".5" stop-color="#59a8cd" stop-opacity=".9"/><stop offset="1" stop-color="#183b65"/></linearGradient>
<filter id="shadow" x="-.4" y="-.4" width="1.8" height="2"><feDropShadow dx="0" dy="12" stdDeviation="14" flood-color="#000b1a" flood-opacity=".85"/><feDropShadow dx="0" dy="0" stdDeviation="3" flood-color="#249fff" flood-opacity=".35"/></filter>
<filter id="bloom" x="-.6" y="-.6" width="2.2" height="2.2"><feGaussianBlur stdDeviation="10"/></filter>
<filter id="water" x="-.15" y="-.35" width="1.3" height="1.7" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency=".009 .025" numOctaves="2" seed="12" result="waves"><animate attributeName="baseFrequency" dur="18s" values=".009 .025;.013 .035;.009 .025" repeatCount="indefinite"/></feTurbulence>
<feDisplacementMap in="SourceGraphic" in2="waves" scale="16" xChannelSelector="R" yChannelSelector="G"><animate attributeName="scale" dur="12s" values="12;23;12" repeatCount="indefinite"/></feDisplacementMap>
</filter>
<linearGradient id="beam"><stop stop-color="#3ca7ff" stop-opacity="0"/><stop offset=".5" stop-color="#a9efff" stop-opacity=".9"/><stop offset="1" stop-color="#3ca7ff" stop-opacity="0"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#fff" stop-opacity=".45"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".63" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="linear" slope=".1"/></feComponentTransfer><feBlend in="SourceGraphic" mode="soft-light"/></filter>
</defs>
<style>
text {font-family:Arial,Helvetica,sans-serif;fill:#d7eeff}
.mono {font-family:'Courier New',monospace;letter-spacing:1.5px}
.white {fill:#d7eeff}
.dim {fill:#718eac}
.accent {fill:#7edfff}
.water-still {display:none}
.float {animation:drift 10s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.float-slow {animation:drift 14s ease-in-out -4s infinite;transform-box:fill-box;transform-origin:center}
@keyframes drift {0%,100% {transform:translateY(0) rotate(-2deg)}50% {transform:translateY(-14px) rotate(3deg)}}
@media (prefers-reduced-motion:reduce) {.float,.float-slow {animation:none}.water-motion{display:none}.water-still{display:inline}}
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


svg('hero.svg', 1200, 680, 'MINGRUI AI / DEEPWATER', '''
<defs>
<g id="name"><text x="600" y="265" text-anchor="middle" font-size="116" font-weight="500" letter-spacing="-6">MINGRUI AI</text></g>
<g id="cube"><path d="M600 359L681 402L600 445L519 402Z" fill="#155b9a" fill-opacity=".85"/><path d="M519 402L600 445V524L519 481Z" fill="#0b2b57"/><path d="M600 445L681 402V481L600 524Z" fill="#124579"/><path d="M600 359L681 402V481L600 524L519 481V402ZM519 402L600 445L681 402M600 445V524" fill="none" stroke="#5ddaff" stroke-width="1.8"/><path d="M600 359L600 436M526 405L600 365L674 405" fill="none" stroke="#b3f4ff" stroke-opacity=".4"/></g>
</defs>
<rect width="1200" height="680" fill="#070d18"/>
<ellipse cx="600" cy="470" rx="500" ry="235" fill="url(#glow)" opacity=".75"/>
<text x="42" y="53" class="mono" font-size="16">mingrui / dev</text>
<text x="1158" y="53" class="mono dim" text-anchor="end" font-size="12">DEEPWATER — VOL.02</text>
<path d="M42 78H1158" stroke="#173047"/>
<text x="600" y="149" text-anchor="middle" font-size="13" class="mono dim">COMPUTER SCIENCE / ARTIFICIAL INTELLIGENCE</text>
<g class="water-motion" filter="url(#water)">
<use href="#name" transform="translate(-2 1)" opacity=".5" stroke="#00cfff" stroke-width="1.5"/>
<use href="#name" transform="translate(2 -1)" opacity=".35" stroke="#8765ff" stroke-width="1.2"/>
<use href="#name"/>
</g><g class="water-still"><use href="#name"/></g>
<text x="600" y="313" text-anchor="middle" font-size="22" letter-spacing=".3" class="dim">Ideas beneath the surface.</text>
<g class="float"><use href="#cube" filter="url(#bloom)" opacity=".6"/><use href="#cube"/></g>
<g opacity=".15" class="water-motion" filter="url(#water)"><use href="#cube" transform="translate(0 830) scale(1 -.55)"/></g>
<g fill="none" stroke="url(#beam)"><ellipse cx="600" cy="546" rx="252" ry="22" opacity=".8"/><ellipse cx="600" cy="546" rx="391" ry="45" opacity=".4"/><ellipse cx="600" cy="546" rx="535" ry="76" opacity=".15"/></g>
<path d="M130 546H1070" stroke="url(#beam)" stroke-width="2"/>
<g opacity=".22" class="water-motion" filter="url(#water)"><path d="M210 557Q450 545 700 560T1030 558M155 580Q500 567 720 583T1090 580M320 599Q600 586 878 602" fill="none" stroke="#3986b0" stroke-width="2"/></g>
<circle cx="376" cy="382" r="1.5" fill="#6fd6ff"/><circle cx="835" cy="430" r="2" fill="#6fd6ff" opacity=".5"/><circle cx="914" cy="333" r="1" fill="#6fd6ff"/>
<text x="42" y="651" class="mono dim" font-size="11">SCAU / LLM / AGENTS / FULL STACK</text>
<text x="1158" y="651" class="mono accent" text-anchor="end" font-size="11">DIVE INTO THE WORK ↓</text>
''', 'An ice-blue name refracts underwater using animated SVG turbulence and displacement. A luminous glass cube floats above blue water. Motion is replaced by a static name when reduced motion is preferred.')

svg('projects.svg', 1200, 210, 'Selected Projects — four public repositories', '''
<rect width="1200" height="210" fill="#070d18"/>
<text x="600" y="89" text-anchor="middle" font-size="64" letter-spacing="-3.5">Selected Projects</text>
<rect x="329" y="119" width="542" height="43" rx="22" fill="#0c192b" stroke="#1a3450"/>
<rect x="336" y="125" width="83" height="31" rx="16" fill="#175487"/>
<text x="377" y="146" text-anchor="middle" font-size="13" class="white">All 04</text>
<text x="481" y="146" text-anchor="middle" font-size="13">AI / Agents 02</text>
<path d="M551 130V151M725 130V151" stroke="#1a3450"/>
<text x="639" y="146" text-anchor="middle" font-size="13">Experiment 01</text>
<text x="795" y="146" text-anchor="middle" font-size="13">Open Source 01</text>
<text x="600" y="192" text-anchor="middle" class="mono" font-size="11">A FEW THINGS I AM BUILDING &amp; EXPLORING</text>
''', 'Four public repositories. Click the project cards below. Category labels are a visual index, not filtering controls.')


def card(name, title, category, number, bg, art, description):
    palette = {
        '#f8f4f0': '#10263f', '#c6bfd5': '#183955', '#e0d9e8': '#1d4262',
        '#f1eee7': '#101d31', '#fff': '#18334c', '#d3e6d9': '#194466',
        '#d1e4df': '#427f9f', '#0f2423': '#0a1525', '#9cb4a6': '#3a89bb',
        '#355c51': '#123958', '#29483f': '#152c46', '#1b3730': '#0c2035',
        '#4c6e60': '#254e72', '#749588': '#417898', '#72968b': '#417898',
        '#c2b8c5': '#3d6483', '#5d4a72': '#17476d', '#27213b': '#0b1930',
        '#baafce': '#387eaf', '#c6e6cf': '#80dfff', '#b1bdb5': '#3b6182',
        '#e5b266': '#67cfff', '#b6d6c8': '#64b6d6', '#b2b5ad': '#244966',
    }
    for original, replacement in palette.items():
        art = art.replace('"' + original + '"', '"' + replacement + '"')
    svg(name, 580, 444, title, f'''
<rect width="580" height="444" fill="#070d18"/>
<defs><clipPath id="art"><rect x="14" y="14" width="552" height="322"/></clipPath></defs>
<g clip-path="url(#art)"><rect x="14" y="14" width="552" height="322" fill="url(#{bg})"/>{art}
<text x="32" y="43" font-size="10" class="white mono">{number} / SELECTED WORK</text></g>
<rect x="14" y="14" width="552" height="322" fill="none" stroke="#247db2" stroke-opacity=".6"/>
<path d="M14 85V14H156M424 336H566V265" fill="none" stroke="#75d8ff" stroke-opacity=".7"/>
<text x="16" y="377" font-size="30" letter-spacing="-1.2">{escape(title)}</text>
<text x="16" y="405" font-size="18" class="dim">{escape(category)}</text>
<path d="M535 385L552 402M535 402H552V385" fill="none" stroke="#76c9f6" stroke-width="2"/>
<path d="M16 426H564" stroke="#19314d" stroke-width="1"/>
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
<rect width="1200" height="235" fill="#070d18"/>
<text x="42" y="50" font-size="12" class="mono">HAVE AN IDEA?</text>
<text x="40" y="129" font-size="66" letter-spacing="-3">Let's build something.</text>
<path d="M1087 68L1149 130M1087 130H1149V68" fill="none" stroke="#77d9ff" stroke-width="3"/>
<path d="M42 164H1158" stroke="#19314d"/>
<text x="42" y="201" font-size="17">mingrui.ai@outlook.com</text>
<text x="1158" y="201" text-anchor="end" font-size="12" class="mono">MINGRUI AI / ALWAYS EXPLORING</text>
''')
for filename, title, subtitle, index in [
    ('city-heading.svg', 'A city built one commit at a time.', '365 DAYS / CONTRIBUTION TOPOGRAPHY', '02'),
    ('snake-heading.svg', 'Follow the current.', 'CONTRIBUTIONS / IN MOTION', '03'),
    ('metrics-heading.svg', 'Signals from the deep.', 'LANGUAGES / ACTIVITY / MILESTONES', '04'),
]:
    svg(filename, 1200, 150, title, f'''<rect width="1200" height="150" fill="#070d18"/>
    <text x="42" y="41" class="mono accent" font-size="12">{index} / {subtitle}</text>
    <text x="40" y="110" font-size="46" letter-spacing="-1.5">{title}</text>''')

svg('about.svg', 1200, 315, 'Mingrui Ai — about & tools', '''
<rect width="1200" height="315" fill="#070d18"/><path d="M42 28H1158" stroke="#19314d"/>
<text x="42" y="72" class="mono accent" font-size="12">05 / THE PERSON BEHIND THE PROJECTS</text>
<text x="42" y="129" font-size="40" letter-spacing="-1">Curious by nature. Building by choice.</text>
<text x="42" y="172" font-size="20" class="dim">Mingrui Ai / Computer Science / South China Agricultural University</text>
<text x="42" y="223" class="mono" font-size="14">JAVA · PYTHON · C/C++ · SQL</text>
<text x="42" y="257" class="mono dim" font-size="14">VUE 3 · TYPESCRIPT · GIT · DOCKER</text>
<text x="1158" y="257" text-anchor="end" class="mono accent" font-size="12">LLM / AI AGENTS / FULL STACK</text>
''')
for slug, label, index in [('projects', 'PROJECTS', '01'), ('activity', 'ACTIVITY', '02'), ('about', 'ABOUT', '03'), ('contact', 'CONTACT', '04')]:
    svg(f'nav-{slug}.svg', 300, 64, label, f'''<rect width="300" height="64" fill="#070d18"/>
    <text x="150" y="38" text-anchor="middle" class="mono" font-size="14">{index} / {label}</text>
    <path d="M26 60H274" stroke="#19314d"/>''')
print(f"Built {len(list(OUT.glob('*.svg')))} Deepwater SVG assets in {OUT}")
