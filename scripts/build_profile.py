"""Build the borderless liquid gallery. Python standard library only."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets/profile'
OUT.mkdir(parents=True, exist_ok=True)
BG = '#0d1117'
DEFS = '''<defs>
<linearGradient id="cyan-purple" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#22d3ee"/><stop offset=".48" stop-color="#818cf8"/><stop offset="1" stop-color="#a855f7"/></linearGradient>
<linearGradient id="gold-green" x2="1" y2="1"><stop stop-color="#fbbf24"/><stop offset=".45" stop-color="#f59e0b"/><stop offset="1" stop-color="#10b981"/></linearGradient>
<linearGradient id="coral" x2="1" y2="1"><stop stop-color="#fb7185"/><stop offset="1" stop-color="#f97316"/></linearGradient>
<linearGradient id="pearl" x2=".7" y2="1"><stop stop-color="#f8fafc"/><stop offset=".48" stop-color="#d9f2ff"/><stop offset="1" stop-color="#7dd3fc"/></linearGradient>
<linearGradient id="glass" x2=".8" y2="1"><stop stop-color="#1d2c3e"/><stop offset="1" stop-color="#101821"/></linearGradient>
<linearGradient id="waterline"><stop stop-color="#22d3ee" stop-opacity="0"/><stop offset=".45" stop-color="#22d3ee" stop-opacity=".6"/><stop offset=".6" stop-color="#818cf8" stop-opacity=".5"/><stop offset="1" stop-color="#818cf8" stop-opacity="0"/></linearGradient>
<radialGradient id="aura"><stop stop-color="#22d3ee" stop-opacity=".2"/><stop offset=".5" stop-color="#818cf8" stop-opacity=".06"/><stop offset="1" stop-color="#0d1117" stop-opacity="0"/></radialGradient>
<filter id="shadow" x="-.4" y="-.4" width="1.8" height="1.9"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-opacity=".5"/></filter>
<filter id="glow" x="-.5" y="-.5" width="2" height="2"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="soft-glow" x="-.5" y="-.5" width="2" height="2"><feGaussianBlur stdDeviation="3"/></filter>
</defs>
<style>
text {font-family:Arial,Helvetica,sans-serif;fill:#f8fafc}
.label {fill:#8b949e;font-size:12px;letter-spacing:2.16px}
.float {animation:float 6s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.breathe {animation:breathe 3s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.ripple {animation:ripple 4.5s linear infinite;transform-box:fill-box;transform-origin:center;opacity:0}
.ripple-two {animation-delay:1.5s}
.ripple-three {animation-delay:3s}
.bubble {animation:bubble 5s ease-in-out infinite;opacity:0}
.bubble-two {animation-delay:2.5s}
.sheen {animation:sheen 7s ease-in-out infinite;opacity:0}
.status {animation:status 3s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes float {0%,100% {transform:translateY(0) rotate(-2deg)}50% {transform:translateY(-9px) rotate(3deg)}}
@keyframes breathe {0%,100% {transform:scale(.93);opacity:.8}50% {transform:scale(1.07);opacity:1}}
@keyframes ripple {0% {transform:scale(.55);opacity:0}15% {opacity:.5}100% {transform:scale(2.1);opacity:0}}
@keyframes bubble {0% {transform:translateY(15px);opacity:0}20% {opacity:.6}85% {opacity:.35}100% {transform:translateY(-45px);opacity:0}}
@keyframes sheen {0%,58% {transform:translateX(-180px);opacity:0}63% {opacity:.48}87% {transform:translateX(940px);opacity:0}100% {transform:translateX(940px);opacity:0}}
@keyframes status {0%,100% {transform:scale(.85);opacity:.5}50% {transform:scale(1.2);opacity:1}}
@media (prefers-reduced-motion:reduce) {* {animation:none!important}.sheen {display:none}.ripple {opacity:.16}.ripple-two {transform:scale(1.4)}.ripple-three {transform:scale(1.8)}.bubble {opacity:.4}}
</style>'''


def svg(name, width, height, title, body, desc=''):
    (OUT / name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc or title)}</desc>
{DEFS}<rect width="{width}" height="{height}" fill="{BG}"/>
{body}</svg>
''', encoding='utf-8')


svg('hero.svg', 840, 450, 'MINGRUI AI — liquid light', '''
<defs>
<clipPath id="wordmark"><text x="420" y="120" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="94" font-weight="500" letter-spacing="-5">MINGRUI AI</text></clipPath>
<linearGradient id="shine"><stop stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<radialGradient id="core" cx=".28" cy=".25" r=".85"><stop stop-color="#d5fcff"/><stop offset=".2" stop-color="#22d3ee"/><stop offset=".65" stop-color="#818cf8"/><stop offset="1" stop-color="#5b21b6"/></radialGradient>
<linearGradient id="orbit" gradientUnits="userSpaceOnUse" x1="-110" y1="-47" x2="110" y2="47"><stop stop-color="#a5f3fc"/><stop offset=".2" stop-color="#22d3ee"/><stop offset=".46" stop-color="#1d446c"/><stop offset=".67" stop-color="#818cf8"/><stop offset=".86" stop-color="#b3b8ff"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
<linearGradient id="orbit-two" gradientUnits="userSpaceOnUse" x1="-94" y1="-42" x2="94" y2="42"><stop stop-color="#22d3ee"/><stop offset=".48" stop-color="#818cf8"/><stop offset="1" stop-color="#a855f7"/></linearGradient>
<g id="tracks" fill="none">
<ellipse rx="110" ry="47" transform="rotate(-32)" stroke="url(#orbit)" stroke-width="15" stroke-opacity=".8"/>
<ellipse rx="94" ry="42" transform="rotate(55)" stroke="url(#orbit-two)" stroke-width="12" stroke-opacity=".65"/>
<ellipse rx="110" ry="47" transform="rotate(-32)" stroke="#cffafe" stroke-width="1.2" stroke-opacity=".6"/>
<ellipse rx="94" ry="42" transform="rotate(55)" stroke="#c4b5fd" stroke-width="1" stroke-opacity=".5"/>
</g>
</defs>
<text x="420" y="120" text-anchor="middle" font-size="94" font-weight="500" letter-spacing="-5" style="fill:#cdd5df">MINGRUI AI</text>
<g clip-path="url(#wordmark)"><path class="sheen" d="M0 36H100L170 138H70Z" fill="url(#shine)"/></g>
<text x="420" y="158" text-anchor="middle" font-size="17" style="fill:#8b949e">Computer science &amp; AI</text>
<ellipse cx="420" cy="295" rx="240" ry="120" fill="url(#aura)"/>
<g transform="translate(420 281)"><g class="float">
<use href="#tracks" filter="url(#glow)" opacity=".35"/>
<use href="#tracks"/>
<g class="breathe"><circle r="43" fill="url(#core)" filter="url(#glow)" opacity=".58"/><circle r="31" fill="url(#core)"/><ellipse cx="-9" cy="-11" rx="13" ry="7" fill="#ecfeff" opacity=".24" transform="rotate(-30)"/></g>
<g transform="rotate(-32)" fill="none"><path d="M-110 0A110 47 0 0 0 110 0" stroke="url(#orbit)" stroke-width="15"/><path d="M-110 0A110 47 0 0 0 110 0" stroke="#cffafe" stroke-width="1.2" stroke-opacity=".6"/></g>
<g transform="rotate(55)" fill="none"><path d="M-94 0A94 42 0 0 1 94 0" stroke="url(#orbit-two)" stroke-width="12" stroke-opacity=".85"/><path d="M-94 0A94 42 0 0 1 94 0" stroke="#c4b5fd" stroke-width="1" stroke-opacity=".5"/></g>
</g></g>
<g transform="translate(420 394) scale(1 -.2)" opacity=".12"><use href="#tracks"/></g>
<g fill="none" stroke="url(#waterline)" stroke-width="1.1"><ellipse class="ripple" cx="420" cy="389" rx="125" ry="15"/><ellipse class="ripple ripple-two" cx="420" cy="389" rx="125" ry="15"/><ellipse class="ripple ripple-three" cx="420" cy="389" rx="125" ry="15"/></g>
''', 'A floating translucent gyroscope surrounds a cyan-indigo breathing core. Three ripples expand over the water; a restrained diagonal light crosses the name every seven seconds. All motion respects reduced-motion preferences.')

svg('projects.svg', 840, 94, 'Selected work', '<text x="20" y="65" font-size="38" letter-spacing="-1.5">Selected work</text>')
svg('activity.svg', 840, 86, 'Activity', '<text x="20" y="62" font-size="36" letter-spacing="-1.3">Activity</text>')


def row(name, title, label, number, art, desc, reverse=False):
    # Illustrations and type deliberately alternate. Each text field has only
    # a displaced number, a title with an arrow, and one short uppercase label.
    tx, ax = (52, 490) if reverse else (470, 42)
    nx = tx + 244 if reverse else tx - 24
    svg(name, 840, 240, title, f'''
<g transform="translate({ax} 12)">{art}</g>
<text x="{nx}" y="85" font-size="54" font-weight="600" style="fill:#21262d">{number}</text>
<text x="{tx}" y="133" font-size="28" font-weight="600" letter-spacing="-.8">{escape(title)} <tspan font-size="22" font-weight="400">↗</tspan></text>
<text x="{tx}" y="166" class="label">{escape(label)}</text>
''', desc)


row('echosoul.svg', 'EchoSoul', 'DESKTOP AI · JAVAFX', '01', '''
<ellipse cx="165" cy="113" rx="160" ry="95" fill="url(#aura)"/>
<g transform="translate(20 35) rotate(-7 140 80)" filter="url(#shadow)">
<rect width="285" height="164" rx="15" fill="url(#glass)" stroke="#22d3ee" stroke-opacity=".35"/>
<path d="M0 27H285M65 27V164" stroke="#36455a"/>
<g fill="#63738a"><circle cx="15" cy="14" r="2.5"/><circle cx="25" cy="14" r="2.5"/><circle cx="35" cy="14" r="2.5"/></g>
<rect x="12" y="45" width="41" height="31" rx="9" fill="#22d3ee" fill-opacity=".16"/>
<circle cx="32" cy="60" r="8" fill="#22d3ee"/>
<path d="M20 95H45M20 112H38M20 129H42" stroke="#52657e" stroke-width="3" stroke-linecap="round"/>
<rect x="137" y="43" width="128" height="36" rx="11" fill="#22d3ee" fill-opacity=".85"/>
<path d="M153 56H245M153 66H213" stroke="#cffafe" stroke-width="3" stroke-linecap="round"/>
<rect x="83" y="91" width="139" height="43" rx="12" fill="#a855f7" fill-opacity=".7"/>
<path d="M99 111H108L113 100L120 124L127 101L133 118L139 107L144 111H203" stroke="#e9d5ff" stroke-width="2" fill="none" stroke-linejoin="round"/>
<path d="M87 150H253" stroke="#4c5570" stroke-width="4" stroke-linecap="round"/>
</g><path d="M75 190Q176 217 295 177" fill="none" stroke="url(#cyan-purple)" stroke-width="2" opacity=".45"/>
''', 'EchoSoul: JavaFX desktop AI conversations with personas, multiple model providers and local history. Original conceptual illustration.')

row('job-search.svg', 'AI Job Search CN', 'CAREER AGENTS · PYTHON', '02', '''
<g transform="translate(65 23) rotate(-8 92 90)" filter="url(#shadow)">
<rect x="14" y="-8" width="172" height="178" rx="10" fill="#264337" stroke="#10b981" stroke-opacity=".5"/>
<rect width="172" height="178" rx="10" fill="#26231d" stroke="#f59e0b" stroke-opacity=".6"/>
<circle cx="30" cy="34" r="12" fill="#f59e0b"/>
<path d="M53 28H139M53 39H111" stroke="#fcd34d" stroke-width="4" stroke-linecap="round"/>
<path d="M24 72H148M24 92H124M24 112H140M24 132H99" stroke="#8b7549" stroke-width="4" stroke-linecap="round"/>
<rect x="23" y="152" width="67" height="9" rx="4.5" fill="#f59e0b"/>
</g>
<path d="M220 73H277V134H246M45 143H27V67H65" fill="none" stroke="#10b981" stroke-opacity=".6" stroke-width="1.5"/>
<g fill="#f59e0b"><circle cx="27" cy="67" r="5"/><circle cx="45" cy="143" r="4"/></g><circle cx="277" cy="73" r="5" fill="#10b981"/>
<g transform="translate(216 121) rotate(10 36 37)" filter="url(#shadow)"><rect width="73" height="76" rx="17" fill="#103c31" stroke="#10b981"/><circle cx="36" cy="37" r="23" fill="#10b981"/><path d="M23 37L33 47L50 27" fill="none" stroke="#ecfdf5" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></g>
''', 'AI Job Search CN: an in-development Chinese-market adaptation of ai-job-search, with JD parsing and explainable matching. Python.', reverse=True)

row('lil-seal.svg', 'lil-seal', 'INTERACTIVE WEB', '03', '''
<ellipse cx="170" cy="188" rx="136" ry="16" fill="none" stroke="#7dd3fc" stroke-opacity=".18"/>
<g transform="translate(-16 -12) scale(.65)" filter="url(#shadow)">
<path d="M372 251Q431 217 461 245Q450 281 389 278Z" fill="url(#pearl)"/>
<path d="M174 258Q130 215 157 162Q174 109 230 107Q286 102 316 160Q333 188 376 204Q413 220 408 254Q398 283 300 280Q210 282 174 258Z" fill="url(#pearl)"/>
<path d="M247 230Q286 224 314 265Q265 286 241 248Z" fill="#9edafa"/>
<ellipse cx="186" cy="180" rx="5.5" ry="7" fill="#253644"/><ellipse cx="239" cy="178" rx="5.5" ry="7" fill="#253644"/>
<ellipse cx="211" cy="200" rx="8" ry="6" fill="#486374"/>
<path d="M211 205Q204 217 197 210M211 205Q218 217 225 210M182 199L158 194M182 205L155 207M239 197L264 191M239 204L267 206" fill="none" stroke="#68899d" stroke-width="2"/>
</g><g fill="none" stroke="#7dd3fc" stroke-width="1.3"><circle class="bubble" cx="57" cy="119" r="8"/><circle class="bubble bubble-two" cx="287" cy="97" r="5"/></g>
''', 'lil-seal: a playful JavaScript web experiment. A pearl-white seal and two slowly rising ice-blue bubbles.')

row('linuxdo.svg', 'LinuxDo Android', 'KOTLIN · ANDROID · FORK', '04', '''
<g transform="translate(116 4) rotate(13 56 105)" filter="url(#shadow)">
<rect width="112" height="208" rx="21" fill="#281e26" stroke="url(#coral)" stroke-width="2"/>
<rect x="6" y="7" width="100" height="194" rx="16" fill="#201b25"/>
<rect x="40" y="11" width="32" height="7" rx="3.5" fill="#0d1117"/>
<circle cx="24" cy="40" r="10" fill="#f97316"/>
<path d="M43 36H87M43 45H74" stroke="#fdba74" stroke-width="3" stroke-linecap="round"/>
<rect x="13" y="65" width="86" height="32" rx="7" fill="#fb7185" fill-opacity=".9"/>
<rect x="13" y="108" width="86" height="32" rx="7" fill="#f97316" fill-opacity=".85"/>
<rect x="13" y="151" width="86" height="32" rx="7" fill="#fb7185" fill-opacity=".6"/>
<g fill="#fff1f2"><circle cx="25" cy="77" r="4"/><circle cx="25" cy="120" r="4"/><circle cx="25" cy="163" r="4"/></g>
<path d="M37 75H88M37 85H73M37 118H88M37 128H78M37 161H88M37 171H68" stroke="#fff1f2" stroke-width="2" stroke-linecap="round" opacity=".8"/>
</g><path d="M77 173C39 112 62 45 114 28M239 52C283 105 263 170 221 192" stroke="url(#coral)" stroke-width="1.2" fill="none" opacity=".3"/>
''', "Mingrui Ai's fork of xuemk/linuxdo-android, a Kotlin Android community client. Original conceptual illustration.", reverse=True)

svg('contact.svg', 840, 178, "Let's build something — mingrui.ai@outlook.com", '''
<text x="20" y="83" font-size="44" letter-spacing="-1.7">Let's build something.</text>
<circle class="status" cx="26" cy="122" r="5" fill="#2dd4bf"/>
<text x="44" y="128" font-size="18" style="fill:#8b949e">mingrui.ai@outlook.com</text>
<path d="M758 49H790V81M790 49L755 84" stroke="#cbd5e1" stroke-width="1.8" fill="none"/>
''', 'Contact Mingrui Ai at mingrui.ai@outlook.com. A decorative teal dot breathes gently; it is not a live availability indicator.')
print('Built 8 liquid gallery SVGs.')
