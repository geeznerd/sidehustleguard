#!/usr/bin/env python3
"""
Phase 14.5 — Author the remaining 19 expense-swiper illustrations.

Each entry maps a live ITEMS[i].q value to an inline SVG illustration in
the Direction A style:
  - 280×200 viewBox
  - 2.2px indigo (#2d3068) line work, rounded caps + joins
  - Single apricot (#e89464) accent (or one coordinated concept)
  - One of the 6 ambient animation primitives where the metaphor allows

The script finds each item by its q field, anchored by hint + cat lines
above the art:'' placeholder, then replaces the placeholder with a
template-literal-quoted SVG string.
"""
import re
from pathlib import Path

PATH = Path('/Users/dork/Desktop/sidehustleguard/expense-swiper.html')


# Each value is the inner SVG content, including the <svg> wrapper.
ILLUS = {

    # 01 — speedometer needle pulse
    'Mileage between deliveries': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <circle cx="140" cy="108" r="56"/>
        <circle cx="140" cy="108" r="46" stroke-opacity="0.25"/>
        <line x1="100" y1="78" x2="106" y2="84" stroke-width="2.5"/>
        <line x1="118" y1="64" x2="121" y2="68" stroke-width="2.5"/>
        <line x1="140" y1="58" x2="140" y2="62" stroke-width="2.5"/>
        <line x1="162" y1="64" x2="159" y2="68" stroke-width="2.5"/>
        <line x1="180" y1="78" x2="174" y2="84" stroke-width="2.5"/>
        <line x1="108" y1="71" x2="110" y2="74" stroke-opacity="0.4"/>
        <line x1="126" y1="62" x2="128" y2="65" stroke-opacity="0.4"/>
        <line x1="152" y1="62" x2="154" y2="65" stroke-opacity="0.4"/>
        <line x1="170" y1="71" x2="172" y2="74" stroke-opacity="0.4"/>
        <g class="anim-rock" style="transform-origin: 140px 108px;">
          <line x1="140" y1="108" x2="118" y2="80" stroke="#e89464" stroke-width="3"/>
        </g>
        <circle cx="140" cy="108" r="5" fill="#fbf8ee" stroke="#2d3068"/>
        <text x="140" y="146" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" font-weight="600" letter-spacing="0.16em" fill="#2d3068" fill-opacity="0.5">MILES</text>
      </svg>''',

    # 04 — phone with signal bars + animated % badge
    'Phone bill': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <rect x="100" y="32" width="80" height="138" rx="10"/>
        <rect x="110" y="48" width="60" height="106" rx="3" fill="#fbf8ee" stroke="#2d3068" stroke-opacity="0.4"/>
        <line x1="132" y1="40" x2="148" y2="40"/>
        <rect x="118" y="58" width="6" height="10" rx="1"/>
        <rect x="128" y="54" width="6" height="14" rx="1"/>
        <rect x="138" y="50" width="6" height="18" rx="1"/>
        <rect x="148" y="46" width="6" height="22" rx="1"/>
        <rect x="158" y="42" width="6" height="26" rx="1" fill="#e89464" stroke="none"/>
        <circle class="anim-pin" cx="140" cy="110" r="18"/>
        <text x="140" y="118" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-style="italic" font-size="22" font-weight="500" fill="#2d3068">%</text>
        <line x1="118" y1="138" x2="162" y2="138" stroke-opacity="0.35"/>
        <line x1="118" y1="146" x2="148" y2="146" stroke-opacity="0.35"/>
      </svg>''',

    # 05 — torn ticket with stamp, gentle rock
    'Speeding ticket received on the job': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <g class="anim-rock">
          <g transform="rotate(-4 140 104)">
            <path d="M76 50 L204 50 L204 158 L76 158 Z" fill="#fbf8ee" stroke="#2d3068"/>
            <line x1="76" y1="76" x2="204" y2="76"/>
            <text x="140" y="70" text-anchor="middle" font-family="Inter, sans-serif" font-size="13" font-weight="700" letter-spacing="0.22em" fill="#e89464">SPEEDING</text>
            <line x1="88" y1="92" x2="192" y2="92" stroke-opacity="0.4"/>
            <line x1="88" y1="104" x2="180" y2="104" stroke-opacity="0.4"/>
            <line x1="88" y1="116" x2="192" y2="116" stroke-opacity="0.4"/>
            <line x1="88" y1="128" x2="160" y2="128" stroke-opacity="0.4"/>
            <rect x="118" y="138" width="68" height="14" rx="2" stroke-opacity="0.4"/>
            <text x="152" y="148" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-style="italic" font-size="11" font-weight="600" fill="#2d3068">$235</text>
          </g>
        </g>
      </svg>''',

    # 09 — sandwich with cheese + steam
    'Your own lunch during a 6-hour shift': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path class="anim-steam-1" d="M120 36 Q124 28 120 22" stroke="#e89464"/>
        <path class="anim-steam-2" d="M140 36 Q144 28 140 22" stroke="#e89464"/>
        <path class="anim-steam-3" d="M160 36 Q164 28 160 22" stroke="#e89464"/>
        <path d="M80 86 Q140 50 200 86"/>
        <path d="M80 86 L80 100 Q80 116 100 116 L180 116 Q200 116 200 100 L200 86"/>
        <ellipse cx="115" cy="72" rx="2" ry="1.2" fill="#2d3068" stroke="none"/>
        <ellipse cx="140" cy="64" rx="2" ry="1.2" fill="#2d3068" stroke="none"/>
        <ellipse cx="165" cy="72" rx="2" ry="1.2" fill="#2d3068" stroke="none"/>
        <ellipse cx="128" cy="78" rx="2" ry="1.2" fill="#2d3068" stroke="none"/>
        <ellipse cx="152" cy="78" rx="2" ry="1.2" fill="#2d3068" stroke="none"/>
        <path d="M82 94 Q92 90 102 94 Q112 98 122 94 Q132 90 142 94 Q152 98 162 94 Q172 90 182 94 Q192 98 198 94"/>
        <path d="M86 100 L194 100 L188 110 L92 110 Z" fill="#e89464" stroke="#2d3068"/>
        <ellipse cx="140" cy="138" rx="100" ry="6" stroke-opacity="0.25"/>
      </svg>''',

    # 10 — car silhouette with bubble cluster, ping on largest bubble
    'Car wash during a delivery shift': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="30" y1="172" x2="250" y2="172" stroke-width="2.6"/>
        <path d="M70 152 L82 110 Q86 100 96 100 L184 100 Q194 100 200 110 L212 152 Z"/>
        <path d="M96 100 L106 118 L174 118 L184 100" stroke-opacity="0.5"/>
        <line x1="138" y1="100" x2="138" y2="118" stroke-opacity="0.4"/>
        <circle cx="100" cy="152" r="14"/>
        <circle cx="100" cy="152" r="6"/>
        <circle cx="182" cy="152" r="14"/>
        <circle cx="182" cy="152" r="6"/>
        <circle cx="104" cy="72" r="5"/>
        <circle cx="126" cy="58" r="4"/>
        <circle cx="140" cy="46" r="10" stroke="#e89464" stroke-width="2.4"/>
        <circle class="anim-ping-1" cx="140" cy="46" r="10" style="transform-origin: 140px 46px; transform-box: view-box;" fill="none" stroke="#e89464" stroke-width="1.6" opacity="0"/>
        <circle class="anim-ping-2" cx="140" cy="46" r="10" style="transform-origin: 140px 46px; transform-box: view-box;" fill="none" stroke="#e89464" stroke-width="1.6" opacity="0"/>
        <circle cx="158" cy="58" r="4"/>
        <circle cx="178" cy="72" r="5"/>
      </svg>''',

    # 11 — hi-vis safety vest (apricot reflective bands)
    'Reflective vest for late-night deliveries': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M86 60 L120 50 L120 38 Q140 32 160 38 L160 50 L194 60 L194 170 L86 170 Z"/>
        <path d="M120 50 Q140 64 160 50"/>
        <line x1="140" y1="64" x2="140" y2="170" stroke-opacity="0.6"/>
        <rect x="92" y="94" width="100" height="10" fill="#e89464" stroke="#2d3068"/>
        <rect x="92" y="134" width="100" height="10" fill="#e89464" stroke="#2d3068"/>
        <line x1="92" y1="84" x2="138" y2="74" stroke-opacity="0.4"/>
        <line x1="142" y1="74" x2="192" y2="84" stroke-opacity="0.4"/>
      </svg>''',

    # 12 — car with hanging $ payment tag
    'Personal car payment': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="30" y1="170" x2="250" y2="170" stroke-width="2.6"/>
        <path d="M60 152 L74 112 Q78 102 88 102 L192 102 Q202 102 208 112 L222 152 Z"/>
        <path d="M88 102 L100 120 L184 120 L192 102" stroke-opacity="0.5"/>
        <line x1="140" y1="102" x2="140" y2="120" stroke-opacity="0.4"/>
        <circle cx="90" cy="152" r="13"/>
        <circle cx="90" cy="152" r="6"/>
        <circle cx="190" cy="152" r="13"/>
        <circle cx="190" cy="152" r="6"/>
        <g class="anim-rock" style="transform-origin: 140px 40px;">
          <line x1="140" y1="40" x2="140" y2="62" stroke-opacity="0.5"/>
          <path d="M122 62 L158 62 L158 86 L140 96 L122 86 Z" fill="#e89464" stroke="#2d3068"/>
          <text x="140" y="82" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-style="italic" font-size="16" font-weight="600" fill="#fbf8ee">$</text>
        </g>
      </svg>''',

    # 13 — pump bottle with falling apricot drop
    'Hand sanitizer + disinfecting wipes for your car': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="50" y1="172" x2="230" y2="172" stroke-opacity="0.2"/>
        <rect x="124" y="38" width="32" height="14" rx="2"/>
        <line x1="140" y1="52" x2="140" y2="64"/>
        <path d="M156 42 L184 42 L184 54 L156 54"/>
        <rect x="118" y="64" width="44" height="10" rx="2"/>
        <rect x="100" y="74" width="80" height="92" rx="6"/>
        <rect x="110" y="98" width="60" height="42" rx="2" stroke-opacity="0.5"/>
        <line x1="120" y1="112" x2="160" y2="112" stroke-opacity="0.4"/>
        <line x1="120" y1="122" x2="156" y2="122" stroke-opacity="0.4"/>
        <line x1="120" y1="132" x2="160" y2="132" stroke-opacity="0.4"/>
        <path class="anim-drop" d="M184 56 Q182 64 184 70 Q186 64 184 56 Z" fill="#e89464" stroke="none"/>
      </svg>''',

    # 14 — phone with hanging apricot $$ price tag
    'New phone (full retail price)': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <rect x="92" y="38" width="68" height="138" rx="10"/>
        <rect x="100" y="52" width="52" height="108" rx="3" fill="#fbf8ee" stroke="#2d3068" stroke-opacity="0.4"/>
        <line x1="118" y1="46" x2="134" y2="46"/>
        <rect x="108" y="62" width="12" height="12" rx="2" stroke-opacity="0.4"/>
        <rect x="132" y="62" width="12" height="12" rx="2" stroke-opacity="0.4"/>
        <rect x="108" y="80" width="12" height="12" rx="2" stroke-opacity="0.4"/>
        <rect x="132" y="80" width="12" height="12" rx="2" stroke-opacity="0.4"/>
        <rect x="108" y="98" width="12" height="12" rx="2" stroke-opacity="0.4"/>
        <rect x="132" y="98" width="12" height="12" rx="2" stroke-opacity="0.4"/>
        <g class="anim-rock" style="transform-origin: 198px 56px;">
          <line x1="164" y1="56" x2="198" y2="78" stroke-opacity="0.4"/>
          <path d="M198 78 L242 78 L242 106 L222 116 L198 106 Z" fill="#e89464" stroke="#2d3068"/>
          <text x="220" y="102" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-style="italic" font-size="13" font-weight="600" fill="#fbf8ee">$1.2k</text>
        </g>
      </svg>''',

    # 16 — dashcam with apricot REC LED, pulses
    'Dashcam for your delivery vehicle': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="20" y1="170" x2="260" y2="170" stroke-width="2.6"/>
        <line x1="140" y1="38" x2="140" y2="56" stroke-width="2.4"/>
        <rect x="132" y="34" width="16" height="6" rx="1"/>
        <rect x="92" y="56" width="96" height="78" rx="8"/>
        <circle cx="140" cy="98" r="22"/>
        <circle cx="140" cy="98" r="14" stroke-opacity="0.5"/>
        <circle cx="140" cy="98" r="7" fill="#2d3068" stroke="none"/>
        <circle cx="137" cy="95" r="2" fill="#fbf8ee" stroke="none"/>
        <circle class="anim-pin" cx="170" cy="68" r="4" fill="#e89464" stroke="none" style="transform-origin: 170px 68px;"/>
        <text x="106" y="128" font-family="Inter, sans-serif" font-size="9" font-weight="700" letter-spacing="0.16em" fill="#2d3068" fill-opacity="0.55">REC</text>
        <rect x="148" y="124" width="32" height="6" rx="1" stroke-opacity="0.4"/>
      </svg>''',

    # 17 — phone with apricot wrench glyph, rocks gently
    'AAA / roadside assistance subscription': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <rect x="100" y="32" width="80" height="138" rx="10"/>
        <rect x="110" y="48" width="60" height="106" rx="3" fill="#fbf8ee" stroke="#2d3068" stroke-opacity="0.4"/>
        <line x1="132" y1="40" x2="148" y2="40"/>
        <g class="anim-rock" style="transform-origin: 140px 100px;">
          <g transform="rotate(-30 140 100)">
            <rect x="136" y="72" width="8" height="56" rx="1" fill="#e89464" stroke="#2d3068"/>
            <rect x="126" y="56" width="28" height="22" rx="3" fill="#e89464" stroke="#2d3068"/>
            <rect x="132" y="61" width="16" height="12" rx="2" fill="#fbf8ee" stroke="#2d3068"/>
            <rect x="126" y="124" width="28" height="22" rx="3" fill="#e89464" stroke="#2d3068"/>
            <rect x="132" y="129" width="16" height="12" rx="2" fill="#fbf8ee" stroke="#2d3068"/>
          </g>
        </g>
      </svg>''',

    # 18 — ticket under windshield wiper, rocks
    'Parking ticket during a delivery': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M40 162 L60 88 Q62 80 70 80 L210 80 Q218 80 220 88 L240 162"/>
        <line x1="40" y1="162" x2="240" y2="162" stroke-width="2.6"/>
        <line x1="160" y1="158" x2="120" y2="100"/>
        <line x1="160" y1="158" x2="166" y2="160"/>
        <g class="anim-rock" style="transform-origin: 140px 130px;">
          <g transform="rotate(8 140 130)">
            <path d="M96 100 L184 100 L184 158 L96 158 Z" fill="#fbf8ee" stroke="#2d3068"/>
            <line x1="96" y1="116" x2="184" y2="116" stroke-opacity="0.4"/>
            <text x="140" y="113" text-anchor="middle" font-family="Inter, sans-serif" font-size="10" font-weight="700" letter-spacing="0.18em" fill="#e89464">TICKET</text>
            <line x1="104" y1="126" x2="176" y2="126" stroke-opacity="0.35"/>
            <line x1="104" y1="134" x2="170" y2="134" stroke-opacity="0.35"/>
            <line x1="104" y1="142" x2="176" y2="142" stroke-opacity="0.35"/>
            <rect x="126" y="146" width="42" height="10" rx="2" stroke-opacity="0.4"/>
          </g>
        </g>
      </svg>''',

    # 19 — two layered tote bags (front one apricot)
    'Reusable grocery totes for Instacart deliveries': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M76 76 L162 76 L166 168 L72 168 Z"/>
        <path d="M76 76 L86 50 Q102 42 118 50 L128 76"/>
        <path d="M108 84 L208 84 L212 174 L104 174 Z" fill="#e89464" stroke="#2d3068"/>
        <path d="M108 84 L120 56 Q140 46 160 56 L172 84"/>
        <rect x="142" y="116" width="36" height="22" rx="2" fill="#fbf8ee" stroke="#2d3068"/>
        <path d="M150 128 L156 134 L172 120" stroke="#2d3068" stroke-width="2.4"/>
      </svg>''',

    # 20 — two phones, second one apricot-tinted (the business line)
    'A second cell phone line just for the apps': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <rect x="76" y="38" width="60" height="130" rx="8"/>
        <rect x="84" y="50" width="44" height="100" rx="3" fill="#fbf8ee" stroke="#2d3068" stroke-opacity="0.4"/>
        <line x1="98" y1="44" x2="114" y2="44"/>
        <rect x="144" y="46" width="60" height="130" rx="8" fill="#fbf8ee" stroke="#2d3068"/>
        <rect x="152" y="58" width="44" height="100" rx="3" fill="#e89464" fill-opacity="0.22" stroke="#2d3068" stroke-opacity="0.4"/>
        <line x1="166" y1="52" x2="182" y2="52"/>
        <text x="174" y="92" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-style="italic" font-size="14" font-weight="500" fill="#e89464">biz</text>
        <circle class="anim-pin" cx="174" cy="124" r="5" fill="#e89464" stroke="none" style="transform-origin: 174px 124px;"/>
      </svg>''',

    # 21 — aviator sunglasses (paired apricot lenses)
    'Sunglasses for daytime driving': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M62 86 Q56 132 100 132 Q132 132 132 92 L132 84 Q132 76 124 76 L70 76 Q62 76 62 86 Z" fill="#e89464" stroke="#2d3068"/>
        <path d="M218 86 Q224 132 180 132 Q148 132 148 92 L148 84 Q148 76 156 76 L210 76 Q218 76 218 86 Z" fill="#e89464" stroke="#2d3068"/>
        <path d="M132 88 Q140 82 148 88"/>
        <path d="M74 92 Q74 104 84 114" stroke="#fbf8ee" stroke-width="2"/>
        <path d="M214 92 Q214 104 204 114" stroke="#fbf8ee" stroke-width="2"/>
        <line x1="62" y1="86" x2="46" y2="80"/>
        <line x1="218" y1="86" x2="234" y2="80"/>
      </svg>''',

    # 22 — laptop with apricot play button (pulses)
    'Online course: "How to maximize your DoorDash earnings"': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M50 156 L230 156 L242 172 L38 172 Z"/>
        <line x1="124" y1="164" x2="156" y2="164" stroke-opacity="0.4"/>
        <rect x="68" y="40" width="144" height="116" rx="4"/>
        <rect x="74" y="50" width="132" height="100" rx="2" fill="#fbf8ee" stroke="#2d3068" stroke-opacity="0.4"/>
        <line x1="84" y1="62" x2="142" y2="62" stroke-opacity="0.4"/>
        <line x1="84" y1="70" x2="124" y2="70" stroke-opacity="0.4"/>
        <g class="anim-pin">
          <circle cx="140" cy="110" r="22" fill="#e89464" stroke="#2d3068"/>
          <path d="M134 100 L134 120 L154 110 Z" fill="#fbf8ee" stroke="none"/>
        </g>
        <text x="184" y="146" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" font-weight="600" letter-spacing="0.1em" fill="#2d3068" fill-opacity="0.5">12:30</text>
      </svg>''',

    # 23 — phone showing mileage gauge with apricot progress bar
    'Mileage-tracking app subscription (Stride, MileIQ, etc.)': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <rect x="100" y="30" width="80" height="140" rx="10"/>
        <rect x="110" y="46" width="60" height="108" rx="3" fill="#fbf8ee" stroke="#2d3068" stroke-opacity="0.4"/>
        <line x1="132" y1="38" x2="148" y2="38"/>
        <text x="140" y="84" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-style="italic" font-size="22" font-weight="500" fill="#2d3068">847</text>
        <text x="140" y="100" text-anchor="middle" font-family="Inter, sans-serif" font-size="8" font-weight="600" letter-spacing="0.16em" fill="#2d3068" fill-opacity="0.55">MILES</text>
        <rect x="118" y="114" width="44" height="6" rx="3" stroke-opacity="0.3"/>
        <rect class="anim-pin" x="118" y="114" width="32" height="6" rx="3" fill="#e89464" stroke="none" style="transform-origin: 134px 117px;"/>
        <line x1="118" y1="132" x2="162" y2="132" stroke-opacity="0.35"/>
        <circle cx="125" cy="142" r="3" stroke-opacity="0.5"/>
        <circle cx="140" cy="142" r="3" stroke-opacity="0.5"/>
        <circle cx="155" cy="142" r="3" stroke-opacity="0.5"/>
      </svg>''',

    # 24 — umbrella over apricot car
    'Car insurance premium': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M60 76 Q140 26 220 76" stroke-width="2.6"/>
        <path d="M60 76 Q80 84 100 76 Q120 84 140 76 Q160 84 180 76 Q200 84 220 76" stroke-opacity="0.5"/>
        <line x1="80" y1="80" x2="100" y2="50"/>
        <line x1="120" y1="80" x2="128" y2="40"/>
        <line x1="160" y1="80" x2="152" y2="40"/>
        <line x1="200" y1="80" x2="180" y2="50"/>
        <line x1="140" y1="76" x2="140" y2="120"/>
        <line x1="30" y1="180" x2="250" y2="180" stroke-opacity="0.25"/>
        <g class="anim-rock" style="transform-origin: 140px 160px;">
          <path d="M88 156 L98 126 Q100 118 108 118 L172 118 Q180 118 182 126 L192 156 Z" fill="#e89464" stroke="#2d3068"/>
          <path d="M108 118 L116 134 L164 134 L172 118" stroke-opacity="0.5"/>
          <circle cx="104" cy="156" r="9" fill="#fbf8ee" stroke="#2d3068"/>
          <circle cx="176" cy="156" r="9" fill="#fbf8ee" stroke="#2d3068"/>
        </g>
      </svg>''',

    # 25 — hooded coat with apricot inner lining (static)
    'A new winter coat': '''<svg viewBox="0 0 280 200" fill="none" stroke="#2d3068" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M104 50 Q140 34 176 50 L176 70 Q140 60 104 70 Z"/>
        <path d="M114 56 Q140 50 166 56 L166 64 Q140 58 114 64 Z" fill="#e89464" stroke="none"/>
        <path d="M104 70 L72 102 L82 162 L104 154 L104 170 L176 170 L176 154 L198 162 L208 102 L176 70"/>
        <line x1="140" y1="70" x2="140" y2="170" stroke-opacity="0.5"/>
        <line x1="138" y1="90" x2="142" y2="90" stroke-opacity="0.4"/>
        <line x1="138" y1="100" x2="142" y2="100" stroke-opacity="0.4"/>
        <line x1="138" y1="110" x2="142" y2="110" stroke-opacity="0.4"/>
        <line x1="138" y1="120" x2="142" y2="120" stroke-opacity="0.4"/>
        <line x1="138" y1="130" x2="142" y2="130" stroke-opacity="0.4"/>
        <line x1="138" y1="140" x2="142" y2="140" stroke-opacity="0.4"/>
        <line x1="138" y1="150" x2="142" y2="150" stroke-opacity="0.4"/>
        <path d="M108 118 L92 134 L88 158 L108 162" stroke-opacity="0.4"/>
        <path d="M172 118 L188 134 L192 158 L172 162" stroke-opacity="0.4"/>
      </svg>''',
}


def main() -> int:
    text = PATH.read_text(encoding='utf-8')
    total = 0
    failed = []

    for q, svg in ILLUS.items():
        # Pattern: match the q line, then hint + cat lines, then the empty
        # art: '' placeholder. Replace ONLY the art line.
        pattern = re.compile(
            r"(q: '" + re.escape(q) + r"',\n"
            r"      hint: [^\n]*\n"
            r"      cat: [^\n]*\n"
            r"      )art: ''",
        )
        def repl(m):
            return m.group(1) + 'art: `' + svg + '`'
        new_text, n = pattern.subn(repl, text, count=1)
        if n == 0:
            failed.append(q)
            continue
        text = new_text
        total += 1

    PATH.write_text(text, encoding='utf-8')
    print(f'replaced={total} failed={len(failed)}')
    for q in failed:
        print(f'  [NO MATCH] {q}')
    return 0 if not failed else 1


if __name__ == '__main__':
    raise SystemExit(main())
