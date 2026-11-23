"""Build restrained Deepwater artwork with self-contained, accessible SVGs."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'profile'
OUT.mkdir(parents=True, exist_ok=True)
BG = '#0d1117'  # GitHub's default dark canvas.
DEFS = '''<defs>
<radialGradient id="atmosphere"><stop stop-color="#254158" stop-opacity=".62"/><stop offset="1" stop-color="#0d1117" stop-opacity="0"/></radialGradient>
<linearGradient id="glass" x2=".8" y2="1"><stop stop-color="#263744"/><stop offset="1" stop-color="#111b25"/></linearGradient>
<linearGradient id="edge" x2=".9" y2="1"><stop stop-color="#91afbf" stop-opacity=".7"/><stop offset=".5" stop-color="#486477" stop-opacity=".35"/><stop offset="1" stop-color="#263845" stop-opacity=".2"/></linearGradient>
<linearGradient id="silver" x2=".7" y2="1"><stop stop-color="#cedce2"/><stop offset=".4" stop-color="#a2bbc9"/><stop offset="1" stop-color="#496b82"/></linearGradient>
<linearGradient id="waterline"><stop stop-color="#6e9ab5" stop-opacity="0"/><stop offset=".5" stop-color="#90bbd4" stop-opacity=".6"/><stop offset="1" stop-color="#6e9ab5" stop-opacity="0"/></linearGradient>
<filter id="shadow" x="-.3" y="-.3" width="1.6" height="1.8"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#000" flood-opacity=".45"/></filter>
<filter id="bloom" x="-.5" y="-.5" width="2" height="2"><feGaussianBlur stdDeviation="12"/></filter>
<filter id="water" x="-.1" y="-.3" width="1.2" height="1.6" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency=".009 .025" numOctaves="2" seed="12" result="waves"><animate attributeName="baseFrequency" dur="20s" values=".009 .025;.012 .032;.009 .025" repeatCount="indefinite"/></feTurbulence>
<feDisplacementMap in="SourceGraphic" in2="waves" scale="10" xChannelSelector="R" yChannelSelector="G"><animate attributeName="scale" dur="14s" values="8;15;8" repeatCount="indefinite"/></feDisplacementMap>
</filter>
</defs>
<style>
text {font-family:Arial,Helvetica,sans-serif;fill:#e0e6eb}
.dim {fill:#97a6b3}
.still {display:none}
.float {animation:drift 12s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes drift {0%,100% {transform:translateY(0)}50% {transform:translateY(-8px)}}
@media (prefers-reduced-motion:reduce) {.float {animation:none}.motion {display:none}.still {display:inline}}
</style>'''
BUILT = []


def svg(name, width, height, title, body, desc=''):
    (OUT / name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc or title)}</desc>
{DEFS}
<rect width="{width}" height="{height}" fill="{BG}"/>
{body}
</svg>
''', encoding='utf-8')
    BUILT.append(name)


svg('hero.svg', 1200, 560, 'MINGRUI AI — Computer science & AI', '''
<defs>
<g id="name"><text x="600" y="189" text-anchor="middle" font-size="140" font-weight="500" letter-spacing="-7">MINGRUI AI</text></g>
<g id="cube"><path d="M600 294L675 334L600 374L525 334Z" fill="#345d78"/><path d="M525 334L600 374V448L525 408Z" fill="#172e42"/><path d="M600 374L675 334V408L600 448Z" fill="#254761"/><path d="M600 294L675 334V408L600 448L525 408V334ZM525 334L600 374L675 334M600 374V448" fill="none" stroke="#82b6d0" stroke-width="1.5"/><path d="M531 334L600 300L669 334" fill="none" stroke="#c3dce7" stroke-opacity=".35"/></g>
</defs>
<ellipse cx="600" cy="374" rx="490" ry="177" fill="url(#atmosphere)"/>
<g class="motion" filter="url(#water)"><use href="#name" transform="translate(-1 0)" stroke="#749db9" stroke-width="1.2"/><use href="#name"/></g>
<g class="still"><use href="#name"/></g>
<text x="600" y="243" text-anchor="middle" font-size="28" class="dim">Computer science &amp; AI</text>
<g class="float"><use href="#cube" filter="url(#bloom)" opacity=".3"/><use href="#cube"/></g>
<g opacity=".12" class="motion" filter="url(#water)"><use href="#cube" transform="translate(0 704) scale(1 -.5)"/></g>
<g fill="none" stroke="url(#waterline)"><ellipse cx="600" cy="470" rx="245" ry="18"/><ellipse cx="600" cy="470" rx="372" ry="37" opacity=".5"/><ellipse cx="600" cy="470" rx="500" ry="60" opacity=".22"/></g>
<path d="M150 470H1050" stroke="url(#waterline)"/>
''', 'A large silver-blue name gently refracts in water above a floating glass cube. Reduced-motion preferences replace the refraction with static typography.')


def heading(filename, title):
    svg(filename, 1200, 120, title,
        f'<text x="20" y="83" font-size="56" letter-spacing="-2">{escape(title)}</text>')


heading('projects.svg', 'Selected work')
heading('activity.svg', 'Activity')


def card(name, title, subtitle, art, description):
    svg(name, 580, 420, title, f'''
<defs><clipPath id="art"><rect width="580" height="306" rx="14"/></clipPath></defs>
<g clip-path="url(#art)"><ellipse cx="290" cy="169" rx="288" ry="145" fill="url(#atmosphere)"/>{art}</g>
<text x="10" y="355" font-size="42" letter-spacing="-1.5">{escape(title)}</text>
<text x="10" y="394" font-size="25" class="dim">{escape(subtitle)}</text>
<path d="M533 332H551V350M551 332L530 353" fill="none" stroke="#8fa9bc" stroke-width="2"/>
''', description)


card('echosoul.svg', 'EchoSoul', 'AI conversations', '''
<g transform="translate(85 48) rotate(-6 205 112)" filter="url(#shadow)">
<rect width="410" height="224" rx="14" fill="url(#glass)" stroke="url(#edge)" stroke-width="1.5"/>
<path d="M0 32H410M96 32V224" stroke="#496172" stroke-opacity=".35"/>
<g fill="#788e9e"><circle cx="18" cy="17" r="3"/><circle cx="30" cy="17" r="3"/><circle cx="42" cy="17" r="3"/></g>
<rect x="13" y="52" width="70" height="36" rx="8" fill="#324b5d"/>
<circle cx="31" cy="70" r="7" fill="#91b4c8"/>
<path d="M46 70H69M22 111H71M22 134H61M22 157H68" fill="none" stroke="#668496" stroke-width="4" stroke-linecap="round" opacity=".6"/>
<rect x="195" y="54" width="192" height="44" rx="12" fill="#496c84"/>
<path d="M213 72H356M213 83H318" stroke="#acc3d1" stroke-width="3" stroke-linecap="round" opacity=".65"/>
<rect x="120" y="115" width="223" height="59" rx="12" fill="#293d4d"/>
<path d="M139 134H317M139 146H285M139 158H238" stroke="#92aab9" stroke-width="3" stroke-linecap="round" opacity=".6"/>
<rect x="120" y="188" width="267" height="22" rx="11" fill="#16232e" stroke="#3c5262"/>
<path d="M367 195L373 199L367 203" fill="none" stroke="#a6c5d6" stroke-width="1.6"/>
</g>
''', 'EchoSoul: a JavaFX desktop AI chat app with persona-driven conversations, pluggable models and local history. Conceptual interface illustration.')

card('job-search.svg', 'AI Job Search CN', 'Career agents · In progress', '''
<g transform="translate(125 27) rotate(-8 140 120)" filter="url(#shadow)">
<rect x="24" y="0" width="250" height="228" rx="10" fill="#283d4e" stroke="url(#edge)"/>
<rect x="12" y="10" width="250" height="228" rx="10" fill="#344d60" stroke="url(#edge)"/>
<rect y="22" width="250" height="228" rx="10" fill="url(#glass)" stroke="url(#edge)"/>
<circle cx="41" cy="67" r="14" fill="#7699af"/>
<path d="M69 61H164M69 74H131" stroke="#8fa9b9" stroke-width="5" stroke-linecap="round"/>
<path d="M27 113H221M27 135H181M27 157H211M27 179H157" stroke="#668496" stroke-width="5" stroke-linecap="round" opacity=".6"/>
<rect x="27" y="207" width="99" height="17" rx="8.5" fill="#507791"/>
</g>
<g transform="translate(365 114) rotate(11 58 68)" filter="url(#shadow)">
<rect width="116" height="134" rx="17" fill="#172735" stroke="url(#edge)" stroke-width="1.5"/>
<circle cx="58" cy="60" r="29" fill="#2e4c61" stroke="#789fb7" stroke-width="1.5"/>
<path d="M44 60L54 70L74 48" fill="none" stroke="#c2d7e2" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M37 108H79" stroke="#6c8ca1" stroke-width="4" stroke-linecap="round"/>
</g>
''', 'AI Job Search CN: an in-development Chinese-market adaptation of ai-job-search, with Chinese JD parsing and explainable matching. Python.')

card('lil-seal.svg', 'lil-seal', 'A playful web experiment', '''
<ellipse cx="299" cy="268" rx="190" ry="23" fill="none" stroke="url(#waterline)" opacity=".6"/>
<ellipse cx="299" cy="268" rx="240" ry="39" fill="none" stroke="url(#waterline)" opacity=".25"/>
<g transform="translate(0 -15)" filter="url(#shadow)">
<path d="M372 251Q431 217 461 245Q450 281 389 278Z" fill="url(#silver)"/>
<path d="M174 258Q130 215 157 162Q174 109 230 107Q286 102 316 160Q333 188 376 204Q413 220 408 254Q398 283 300 280Q210 282 174 258Z" fill="url(#silver)"/>
<path d="M247 230Q286 224 314 265Q265 286 241 248Z" fill="#7996a8"/>
<ellipse cx="186" cy="180" rx="5.5" ry="7" fill="#253644"/><ellipse cx="239" cy="178" rx="5.5" ry="7" fill="#253644"/>
<ellipse cx="211" cy="200" rx="8" ry="6" fill="#486374"/>
<path d="M211 205Q204 217 197 210M211 205Q218 217 225 210M182 199L158 194M182 205L155 207M239 197L264 191M239 204L267 206" fill="none" stroke="#536f80" stroke-width="2"/>
</g>
<g fill="none" stroke="#8aafc4" opacity=".45"><circle cx="120" cy="103" r="10"/><circle cx="431" cy="92" r="6"/></g>
''', 'lil-seal: a small JavaScript web experiment. Original vector seal illustration.')

card('linuxdo.svg', 'LinuxDo Android', 'Community client · Fork', '''
<g transform="translate(211 10) rotate(12 84 140)" filter="url(#shadow)">
<rect width="168" height="282" rx="25" fill="#15212c" stroke="url(#edge)" stroke-width="3"/>
<rect x="8" y="8" width="152" height="266" rx="18" fill="url(#glass)"/>
<rect x="62" y="12" width="44" height="8" rx="4" fill="#101820"/>
<circle cx="34" cy="54" r="13" fill="#7d9fb4"/>
<path d="M57 50H130M57 59H109" stroke="#9ab3c3" stroke-width="4" stroke-linecap="round"/>
<path d="M20 79H148" stroke="#617c8f" stroke-opacity=".35"/>
<rect x="18" y="95" width="132" height="44" rx="8" fill="#2b4050"/>
<rect x="18" y="151" width="132" height="44" rx="8" fill="#2b4050"/>
<rect x="18" y="207" width="132" height="44" rx="8" fill="#2b4050"/>
<g fill="#728fa2"><circle cx="34" cy="112" r="7"/><circle cx="34" cy="168" r="7"/><circle cx="34" cy="224" r="7"/></g>
<path d="M51 109H132M51 120H107M51 165H132M51 176H116M51 221H132M51 232H101" stroke="#8aa3b4" stroke-width="3" stroke-linecap="round" opacity=".7"/>
</g>
''', "Mingrui Ai's fork of xuemk/linuxdo-android, a Kotlin Android community client. Conceptual interface illustration.")

svg('contact.svg', 1200, 215, "Let's build something — mingrui.ai@outlook.com", '''
<path d="M20 25H1180" stroke="#28313c"/>
<text x="20" y="113" font-size="64" letter-spacing="-2.5">Let's build something.</text>
<text x="22" y="163" font-size="28" class="dim">mingrui.ai@outlook.com</text>
<path d="M1114 73H1154V113M1154 73L1110 117" fill="none" stroke="#91acbf" stroke-width="2.5"/>
''')

print(f'Built {len(BUILT)} Deepwater SVG assets in {OUT}')
