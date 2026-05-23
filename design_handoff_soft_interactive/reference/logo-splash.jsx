// Logo variations + hero splash designs for SideHustleGuard
// Direction E palette: indigo #2d3068, apricot #e89464, cream #f0ece1, paper #fbf8ee
// Fraunces (serif, italic for accents) + Inter (sans for UI)

const INDIGO = "#2d3068";
const APRICOT = "#e89464";
const CREAM = "#f0ece1";
const PAPER = "#fbf8ee";

// ════════════════════════════════════════════════════════════
// LOGOS — four variations to choose from
// ════════════════════════════════════════════════════════════

// Logo 1: Refined shield (evolution of the existing one)
function LogoShield({ size = 1, dark = false }) {
  const stroke = dark ? PAPER : INDIGO;
  const accent = APRICOT;
  return (
    <svg width={48 * size} height={48 * size} viewBox="0 0 48 48" fill="none">
      <path
        d="M24 3 L41 9 V22 C41 33 33 41.5 24 45 C15 41.5 7 33 7 22 V9 L24 3 Z"
        stroke={stroke}
        strokeWidth="2"
        fill="none"
        strokeLinejoin="round"
      />
      {/* Inner soft arc instead of literal checkmark */}
      <path
        d="M14 24 Q24 34 34 18"
        stroke={accent}
        strokeWidth="2.8"
        strokeLinecap="round"
        fill="none"
      />
    </svg>
  );
}

// Logo 2: Italic G monogram in a soft circle
function LogoMonogram({ size = 1, dark = false }) {
  const fill = dark ? INDIGO : INDIGO;
  return (
    <svg width={48 * size} height={48 * size} viewBox="0 0 48 48">
      <circle cx="24" cy="24" r="22" fill={fill} />
      <text
        x="24"
        y="34"
        textAnchor="middle"
        fontFamily="Fraunces, serif"
        fontSize="30"
        fontStyle="italic"
        fontWeight="500"
        fill={APRICOT}
        style={{ fontVariationSettings: "'opsz' 144, 'SOFT' 50" }}
      >
        G
      </text>
    </svg>
  );
}

// Logo 3: Abstract — a sheltering arc over a dot (no shield literalism)
function LogoArc({ size = 1, dark = false }) {
  const stroke = dark ? PAPER : INDIGO;
  return (
    <svg width={48 * size} height={48 * size} viewBox="0 0 48 48" fill="none">
      {/* Outer arc */}
      <path
        d="M6 30 Q24 4 42 30"
        stroke={stroke}
        strokeWidth="2.4"
        strokeLinecap="round"
        fill="none"
      />
      {/* Inner arc */}
      <path
        d="M14 32 Q24 18 34 32"
        stroke={APRICOT}
        strokeWidth="2.4"
        strokeLinecap="round"
        fill="none"
      />
      {/* Dot — "the protected thing" */}
      <circle cx="24" cy="36" r="2.4" fill={stroke} />
    </svg>
  );
}

// Logo 4: Crest — small italic g inside a soft squircle
function LogoCrest({ size = 1, dark = false }) {
  const bg = dark ? PAPER : INDIGO;
  const fg = dark ? INDIGO : PAPER;
  return (
    <svg width={48 * size} height={48 * size} viewBox="0 0 48 48">
      <rect x="4" y="4" width="40" height="40" rx="14" fill={bg} />
      <rect x="4" y="4" width="40" height="40" rx="14" fill="none" stroke={APRICOT} strokeWidth="1.5" />
      <text
        x="24"
        y="33"
        textAnchor="middle"
        fontFamily="Fraunces, serif"
        fontSize="26"
        fontStyle="italic"
        fontWeight="500"
        fill={fg}
        style={{ fontVariationSettings: "'opsz' 144, 'SOFT' 30" }}
      >
        g
      </text>
      <circle cx="36" cy="14" r="2.5" fill={APRICOT} />
    </svg>
  );
}

// ────────────────────────────────────────────────────────────
// Wordmark lockup
// ────────────────────────────────────────────────────────────
function Wordmark({ size = 1, dark = false }) {
  const c1 = dark ? PAPER : INDIGO;
  return (
    <div style={{
      display: "inline-flex", alignItems: "baseline", gap: 0,
      fontFamily: "Inter, sans-serif", fontWeight: 600,
      fontSize: 22 * size, color: c1, letterSpacing: "-0.015em",
      lineHeight: 1,
    }}>
      <span>SideHustle</span>
      <span style={{
        color: APRICOT,
        fontFamily: "Fraunces, serif",
        fontStyle: "italic",
        fontWeight: 500,
        fontVariationSettings: "'opsz' 144, 'SOFT' 30",
        marginLeft: 2,
      }}>guard</span>
    </div>
  );
}

// ════════════════════════════════════════════════════════════
// LOGO LINEUP — show all 4 side by side on light + dark
// ════════════════════════════════════════════════════════════
function LogoLineup() {
  const logos = [
    { name: "01 · Shield (evolved)", C: LogoShield, note: "Keeps the protective metaphor but softer — arc replaces literal checkmark" },
    { name: "02 · Monogram", C: LogoMonogram, note: "Italic Fraunces G in a filled circle — closest to the Direction E voice" },
    { name: "03 · Arc & dot", C: LogoArc, note: "Abstract shelter — no shield literalism, very calm" },
    { name: "04 · Crest", C: LogoCrest, note: "Squircle badge with lowercase italic g + apricot pin — most distinctive" },
  ];
  const sectionStyles = {
    root: {
      width: "100%", height: "100%", background: CREAM,
      fontFamily: "Inter, sans-serif", color: INDIGO,
      padding: "56px 64px", boxSizing: "border-box",
      display: "flex", flexDirection: "column", gap: 40,
    },
    head: { display: "flex", justifyContent: "space-between", alignItems: "baseline" },
    kicker: {
      fontFamily: "Inter, sans-serif", fontSize: 12,
      letterSpacing: "0.14em", textTransform: "uppercase",
      color: APRICOT, fontWeight: 600, marginBottom: 12,
    },
    h2: {
      fontFamily: "Fraunces, serif", fontSize: 44, fontWeight: 400,
      lineHeight: 1, letterSpacing: "-0.022em",
      fontVariationSettings: "'opsz' 144, 'SOFT' 30",
    },
    h2it: { fontStyle: "italic", color: APRICOT },
    grid: { display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 16 },
    card: {
      background: PAPER, borderRadius: 18,
      border: `1px solid rgba(45,48,104,0.08)`,
      padding: 24, display: "flex", flexDirection: "column", gap: 16,
    },
    cardDark: {
      background: INDIGO, borderRadius: 18,
      padding: 24, display: "flex", flexDirection: "column", gap: 16,
    },
    label: {
      fontFamily: "Inter, sans-serif", fontSize: 11,
      letterSpacing: "0.1em", textTransform: "uppercase",
      color: "rgba(45,48,104,0.55)", fontWeight: 600,
    },
    labelDark: {
      fontFamily: "Inter, sans-serif", fontSize: 11,
      letterSpacing: "0.1em", textTransform: "uppercase",
      color: "rgba(251,248,238,0.5)", fontWeight: 600,
    },
    mark: {
      display: "flex", justifyContent: "center", alignItems: "center",
      padding: "16px 0", minHeight: 72,
    },
    name: {
      fontFamily: "Fraunces, serif", fontSize: 18, fontWeight: 500,
      letterSpacing: "-0.01em",
    },
    note: { fontSize: 12.5, color: "rgba(45,48,104,0.65)", lineHeight: 1.5 },
    lockup: {
      display: "flex", alignItems: "center", gap: 10,
      paddingTop: 16, borderTop: "1px solid rgba(45,48,104,0.08)",
    },
    lockupDark: {
      display: "flex", alignItems: "center", gap: 10,
      paddingTop: 16, borderTop: "1px solid rgba(251,248,238,0.12)",
    },
  };
  return (
    <div style={sectionStyles.root}>
      <div style={sectionStyles.head}>
        <div>
          <div style={sectionStyles.kicker}>Logo lineup · 4 options</div>
          <h2 style={sectionStyles.h2}>
            Marks that <span style={sectionStyles.h2it}>belong</span> here
          </h2>
        </div>
        <div style={{ fontSize: 13, color: "rgba(45,48,104,0.6)", maxWidth: 280, textAlign: "right", lineHeight: 1.5 }}>
          Each shown solo, then locked up with the wordmark. Light and dark surfaces.
        </div>
      </div>
      {/* Light row */}
      <div style={sectionStyles.grid}>
        {logos.map(({ name, C, note }) => (
          <div key={name} style={sectionStyles.card}>
            <div style={sectionStyles.label}>{name}</div>
            <div style={sectionStyles.mark}><C size={1.4} /></div>
            <div style={sectionStyles.name}>{name.split("· ")[1]}</div>
            <div style={sectionStyles.note}>{note}</div>
            <div style={sectionStyles.lockup}>
              <C size={0.7} />
              <Wordmark size={0.75} />
            </div>
          </div>
        ))}
      </div>
      {/* Dark row */}
      <div style={sectionStyles.grid}>
        {logos.map(({ name, C }) => (
          <div key={name + "d"} style={sectionStyles.cardDark}>
            <div style={sectionStyles.labelDark}>on indigo</div>
            <div style={sectionStyles.mark}><C size={1.4} dark /></div>
            <div style={sectionStyles.lockupDark}>
              <C size={0.7} dark />
              <Wordmark size={0.75} dark />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

// ════════════════════════════════════════════════════════════
// HERO SPLASH — three different backdrop treatments
// ════════════════════════════════════════════════════════════

// Shared hustle list for the picker side
const HUSTLES = [
  { n: "01", label: "Digital products", meta: "Etsy, Gumroad" },
  { n: "02", label: "Physical products", meta: "Shopify, Amazon" },
  { n: "03", label: "Freelance & services", meta: "Upwork, Fiverr" },
  { n: "04", label: "Content creation", meta: "YouTube, Twitch" },
  { n: "05", label: "Reselling / flipping", meta: "eBay, Poshmark" },
  { n: "06", label: "Rideshare & delivery", meta: "Uber, DoorDash" },
];

// ────────────────────────────────────────────────────────────
// SPLASH A — Concentric arcs / shelter (echoes Logo 03)
// ────────────────────────────────────────────────────────────
function SplashA() {
  const [active, setActive] = React.useState(0);
  const c = HUSTLES[active];
  return (
    <div style={{
      width: "100%", height: "100%", background: CREAM, color: INDIGO,
      fontFamily: "Inter, sans-serif",
      padding: "44px 64px 56px", boxSizing: "border-box",
      position: "relative", overflow: "hidden",
    }}>
      {/* Backdrop — concentric arcs anchored bottom-right */}
      <svg
        viewBox="0 0 1200 700"
        preserveAspectRatio="xMaxYMax slice"
        style={{ position: "absolute", inset: 0, width: "100%", height: "100%", pointerEvents: "none" }}
      >
        <defs>
          <radialGradient id="aGlow" cx="80%" cy="100%" r="60%">
            <stop offset="0%" stopColor={APRICOT} stopOpacity="0.22" />
            <stop offset="60%" stopColor={APRICOT} stopOpacity="0.04" />
            <stop offset="100%" stopColor={APRICOT} stopOpacity="0" />
          </radialGradient>
        </defs>
        <rect width="1200" height="700" fill="url(#aGlow)" />
        {/* concentric protective arcs */}
        {[180, 280, 380, 480, 580, 680, 780].map((r, i) => (
          <circle key={r} cx="980" cy="720" r={r}
            fill="none"
            stroke={i % 2 === 0 ? INDIGO : APRICOT}
            strokeOpacity={0.08 + (i % 2) * 0.04}
            strokeWidth={i === 3 ? 1.5 : 1}
          />
        ))}
        {/* hairline grid */}
        <g stroke={INDIGO} strokeOpacity="0.05" strokeWidth="1">
          {[100, 200, 300, 400, 500, 600].map((y) => <line key={y} x1="0" y1={y} x2="1200" y2={y} />)}
        </g>
      </svg>

      {/* Nav */}
      <div style={{
        display: "flex", justifyContent: "space-between", alignItems: "center",
        position: "relative", zIndex: 2, marginBottom: 80,
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <LogoArc size={0.8} />
          <Wordmark size={0.8} />
        </div>
        <div style={{ display: "flex", gap: 28, alignItems: "center", fontSize: 13, color: "rgba(45,48,104,0.6)" }}>
          <span>How it works</span>
          <span>Pricing</span>
          <span>Guides</span>
          <span style={{
            background: INDIGO, color: PAPER, padding: "9px 18px",
            borderRadius: 100, fontWeight: 600, fontSize: 13,
          }}>Free check →</span>
        </div>
      </div>

      {/* Hero content */}
      <div style={{
        display: "grid", gridTemplateColumns: "0.95fr 1fr", gap: 56,
        position: "relative", zIndex: 1, alignItems: "center",
      }}>
        <div>
          <div style={{
            display: "inline-flex", alignItems: "center", gap: 8,
            padding: "5px 12px", background: PAPER,
            border: `1px solid rgba(45,48,104,0.1)`,
            borderRadius: 100, fontSize: 11, fontWeight: 600,
            letterSpacing: "0.14em", textTransform: "uppercase",
            color: APRICOT, marginBottom: 22,
          }}>
            <span style={{ width: 6, height: 6, borderRadius: "50%", background: APRICOT }}></span>
            Free legal check
          </div>
          <h1 style={{
            fontFamily: "Fraunces, serif", fontSize: 76, fontWeight: 400,
            lineHeight: 0.98, letterSpacing: "-0.025em", marginBottom: 22,
            color: INDIGO,
            fontVariationSettings: "'opsz' 144, 'SOFT' 30",
          }}>
            Is your hustle<br />
            <span style={{ fontStyle: "italic", color: APRICOT }}>legally</span> protected?
          </h1>
          <p style={{
            fontSize: 17, lineHeight: 1.65, color: "rgba(45,48,104,0.7)",
            maxWidth: 440, marginBottom: 32,
          }}>
            Plain-English answers on your taxes, licenses, and structure. 60 seconds, no lawyer, no jargon.
          </p>
          {/* Indigo preview card */}
          <div style={{
            background: INDIGO, color: PAPER, borderRadius: 18,
            padding: "22px 26px", maxWidth: 440,
          }} key={active}>
            <div style={{
              fontSize: 11, fontWeight: 600, letterSpacing: "0.14em",
              textTransform: "uppercase", color: APRICOT, marginBottom: 10,
            }}>
              We'd check {c.label.toLowerCase()} for —
            </div>
            <div style={{
              display: "flex", flexWrap: "wrap", gap: 8,
            }}>
              {["SE tax", "Quarterly dates", "1099-K threshold", "State license", "Sales tax nexus"].map(t => (
                <span key={t} style={{
                  fontSize: 12, padding: "5px 10px",
                  background: "rgba(251,248,238,0.08)", borderRadius: 100,
                  color: "rgba(251,248,238,0.85)",
                }}>{t}</span>
              ))}
            </div>
          </div>
        </div>

        {/* Picker side */}
        <div style={{
          background: PAPER, borderRadius: 22,
          border: `1px solid rgba(45,48,104,0.08)`,
          padding: 10, position: "relative",
        }}>
          <div style={{
            position: "absolute", left: 10, right: 10,
            top: 10 + active * 64, height: 64, background: CREAM,
            border: `1px solid ${APRICOT}`, borderRadius: 14,
            transition: "top .35s cubic-bezier(0.4, 0, 0.2, 1)",
          }}></div>
          {HUSTLES.map((h, i) => (
            <div key={h.n}
              onMouseEnter={() => setActive(i)}
              style={{
                position: "relative", zIndex: 1, display: "grid",
                gridTemplateColumns: "40px 1fr auto", alignItems: "center",
                gap: 14, height: 64, padding: "0 18px", cursor: "pointer",
              }}>
              <div style={{
                fontFamily: "Fraunces, serif", fontStyle: "italic",
                fontSize: 22, fontWeight: 500,
                color: active === i ? APRICOT : "rgba(45,48,104,0.35)",
                transition: "color .25s",
              }}>{h.n}</div>
              <div>
                <div style={{ fontSize: 15, fontWeight: 600, color: INDIGO }}>{h.label}</div>
                <div style={{ fontSize: 12, color: "rgba(45,48,104,0.55)" }}>{h.meta}</div>
              </div>
              <div style={{
                fontSize: 14, color: active === i ? APRICOT : "rgba(45,48,104,0.3)",
                transition: "color .25s",
              }}>→</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

// ────────────────────────────────────────────────────────────
// SPLASH B — Topographic contour lines (calm, papery)
// ────────────────────────────────────────────────────────────
function SplashB() {
  return (
    <div style={{
      width: "100%", height: "100%", background: CREAM, color: INDIGO,
      fontFamily: "Inter, sans-serif",
      padding: "44px 64px 56px", boxSizing: "border-box",
      position: "relative", overflow: "hidden",
    }}>
      {/* Backdrop — topographic contour map */}
      <svg
        viewBox="0 0 1200 700"
        preserveAspectRatio="xMidYMid slice"
        style={{ position: "absolute", inset: 0, width: "100%", height: "100%", pointerEvents: "none" }}
      >
        <defs>
          <radialGradient id="bGlow" cx="20%" cy="80%" r="55%">
            <stop offset="0%" stopColor={APRICOT} stopOpacity="0.20" />
            <stop offset="100%" stopColor={APRICOT} stopOpacity="0" />
          </radialGradient>
        </defs>
        <rect width="1200" height="700" fill="url(#bGlow)" />
        {/* topo contours — nested blobby ovals */}
        <g fill="none" stroke={INDIGO} strokeOpacity="0.07" strokeWidth="1">
          {[0, 1, 2, 3, 4, 5, 6, 7, 8].map(i => (
            <ellipse key={i}
              cx={300 - i * 6} cy={520 - i * 14}
              rx={460 - i * 35} ry={220 - i * 18}
              transform={`rotate(${-12 + i * 1.5} 300 520)`}
            />
          ))}
        </g>
        {/* Second group on the right */}
        <g fill="none" stroke={APRICOT} strokeOpacity="0.18" strokeWidth="1">
          {[0, 1, 2, 3, 4, 5].map(i => (
            <ellipse key={i}
              cx={1050 + i * 4} cy={180 - i * 8}
              rx={300 - i * 30} ry={140 - i * 14}
              transform={`rotate(${18 - i * 2} 1050 180)`}
            />
          ))}
        </g>
      </svg>

      {/* Nav */}
      <div style={{
        display: "flex", justifyContent: "space-between", alignItems: "center",
        position: "relative", zIndex: 2, marginBottom: 100,
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <LogoMonogram size={0.8} />
          <Wordmark size={0.8} />
        </div>
        <div style={{ display: "flex", gap: 28, alignItems: "center", fontSize: 13, color: "rgba(45,48,104,0.6)" }}>
          <span>How it works</span>
          <span>Pricing</span>
          <span>Guides</span>
          <span style={{
            background: INDIGO, color: PAPER, padding: "9px 18px",
            borderRadius: 100, fontWeight: 600, fontSize: 13,
          }}>Free check →</span>
        </div>
      </div>

      {/* Centered hero — gives the topo room to breathe */}
      <div style={{
        position: "relative", zIndex: 1, maxWidth: 760,
        margin: "0 auto", textAlign: "center",
      }}>
        <div style={{
          display: "inline-flex", alignItems: "center", gap: 8,
          padding: "5px 12px", background: PAPER,
          border: `1px solid rgba(45,48,104,0.1)`,
          borderRadius: 100, fontSize: 11, fontWeight: 600,
          letterSpacing: "0.14em", textTransform: "uppercase",
          color: APRICOT, marginBottom: 24,
        }}>
          <span style={{ width: 6, height: 6, borderRadius: "50%", background: APRICOT }}></span>
          Free legal check · 60 seconds
        </div>
        <h1 style={{
          fontFamily: "Fraunces, serif", fontSize: 96, fontWeight: 400,
          lineHeight: 0.96, letterSpacing: "-0.028em", marginBottom: 24,
          color: INDIGO,
          fontVariationSettings: "'opsz' 144, 'SOFT' 30",
        }}>
          Know <span style={{ fontStyle: "italic", color: APRICOT }}>exactly</span><br />
          where you stand.
        </h1>
        <p style={{
          fontSize: 18, lineHeight: 1.65, color: "rgba(45,48,104,0.7)",
          maxWidth: 540, margin: "0 auto 40px",
        }}>
          Taxes, licenses, structure — every legal obligation a US side hustler faces, checked in plain English. Free score. $5 full report.
        </p>
        <div style={{ display: "inline-flex", gap: 12, alignItems: "center" }}>
          <a style={{
            background: INDIGO, color: PAPER, padding: "15px 32px",
            borderRadius: 100, fontWeight: 600, fontSize: 15,
            textDecoration: "none",
          }}>Start free check →</a>
          <a style={{
            color: INDIGO, padding: "15px 24px",
            fontWeight: 500, fontSize: 15, textDecoration: "none",
          }}>See sample report</a>
        </div>
        <div style={{
          marginTop: 56, display: "inline-flex", gap: 40,
          fontFamily: "Fraunces, serif", fontStyle: "italic",
        }}>
          {[
            ["50", "states covered"],
            ["60s", "median check"],
            ["0", "data stored"],
          ].map(([n, l]) => (
            <div key={l} style={{ textAlign: "center" }}>
              <div style={{
                fontSize: 36, fontWeight: 500, color: APRICOT, lineHeight: 1,
              }}>{n}</div>
              <div style={{
                fontFamily: "Inter, sans-serif", fontStyle: "normal",
                fontSize: 11, fontWeight: 600, letterSpacing: "0.1em",
                textTransform: "uppercase", color: "rgba(45,48,104,0.55)",
                marginTop: 6,
              }}>{l}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

// ────────────────────────────────────────────────────────────
// SPLASH C — Giant italic backdrop word + receipt motifs
// ────────────────────────────────────────────────────────────
function SplashC() {
  return (
    <div style={{
      width: "100%", height: "100%", background: CREAM, color: INDIGO,
      fontFamily: "Inter, sans-serif",
      padding: "44px 64px 56px", boxSizing: "border-box",
      position: "relative", overflow: "hidden",
    }}>
      {/* Giant backdrop word */}
      <div style={{
        position: "absolute",
        bottom: -60, left: -30, right: 0,
        fontFamily: "Fraunces, serif", fontStyle: "italic",
        fontSize: 480, fontWeight: 500, lineHeight: 1,
        color: "rgba(45,48,104,0.06)",
        pointerEvents: "none", letterSpacing: "-0.04em",
        fontVariationSettings: "'opsz' 144, 'SOFT' 50",
        userSelect: "none",
      }}>protected</div>

      {/* Floating "receipt" cards */}
      <div style={{
        position: "absolute", top: 110, right: 80,
        width: 200, background: PAPER, borderRadius: 14,
        padding: "14px 16px", boxShadow: "0 12px 32px rgba(45,48,104,0.08)",
        transform: "rotate(6deg)",
      }}>
        <div style={{
          fontFamily: "Inter, sans-serif", fontSize: 10, letterSpacing: "0.14em",
          textTransform: "uppercase", color: APRICOT, fontWeight: 600, marginBottom: 8,
        }}>Q3 Estimated</div>
        <div style={{
          fontFamily: "Fraunces, serif", fontSize: 32, fontStyle: "italic",
          fontWeight: 500, color: INDIGO, lineHeight: 1, marginBottom: 4,
        }}>$1,847</div>
        <div style={{ fontSize: 11, color: "rgba(45,48,104,0.55)" }}>Due Sep 15</div>
        <div style={{
          marginTop: 10, paddingTop: 10,
          borderTop: "1px dashed rgba(45,48,104,0.15)",
          fontSize: 10, color: "rgba(45,48,104,0.5)",
        }}>SE tax 15.3% · QBI deduction applied</div>
      </div>

      <div style={{
        position: "absolute", top: 320, right: 220,
        width: 170, background: INDIGO, borderRadius: 14,
        padding: "14px 16px", color: PAPER,
        transform: "rotate(-4deg)", boxShadow: "0 12px 32px rgba(45,48,104,0.12)",
      }}>
        <div style={{
          fontFamily: "Inter, sans-serif", fontSize: 10, letterSpacing: "0.14em",
          textTransform: "uppercase", color: APRICOT, fontWeight: 600, marginBottom: 8,
        }}>Compliance score</div>
        <div style={{ display: "flex", alignItems: "baseline", gap: 8 }}>
          <div style={{
            fontFamily: "Fraunces, serif", fontSize: 48, fontStyle: "italic",
            fontWeight: 500, color: APRICOT, lineHeight: 1,
          }}>84</div>
          <div style={{ fontSize: 11, color: "rgba(251,248,238,0.5)" }}>/100</div>
        </div>
        <div style={{ fontSize: 11, color: "rgba(251,248,238,0.55)", marginTop: 4 }}>3 issues to fix</div>
      </div>

      {/* Nav */}
      <div style={{
        display: "flex", justifyContent: "space-between", alignItems: "center",
        position: "relative", zIndex: 2, marginBottom: 90,
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <LogoCrest size={0.8} />
          <Wordmark size={0.8} />
        </div>
        <div style={{ display: "flex", gap: 28, alignItems: "center", fontSize: 13, color: "rgba(45,48,104,0.6)" }}>
          <span>How it works</span>
          <span>Pricing</span>
          <span>Guides</span>
          <span style={{
            background: INDIGO, color: PAPER, padding: "9px 18px",
            borderRadius: 100, fontWeight: 600, fontSize: 13,
          }}>Free check →</span>
        </div>
      </div>

      {/* Content */}
      <div style={{ position: "relative", zIndex: 1, maxWidth: 580 }}>
        <div style={{
          display: "inline-flex", alignItems: "center", gap: 8,
          padding: "5px 12px", background: PAPER,
          border: `1px solid rgba(45,48,104,0.1)`,
          borderRadius: 100, fontSize: 11, fontWeight: 600,
          letterSpacing: "0.14em", textTransform: "uppercase",
          color: APRICOT, marginBottom: 22,
        }}>
          <span style={{ width: 6, height: 6, borderRadius: "50%", background: APRICOT }}></span>
          Free legal check
        </div>
        <h1 style={{
          fontFamily: "Fraunces, serif", fontSize: 80, fontWeight: 400,
          lineHeight: 0.98, letterSpacing: "-0.025em", marginBottom: 22,
          color: INDIGO,
          fontVariationSettings: "'opsz' 144, 'SOFT' 30",
        }}>
          The tax season<br />
          you won't <span style={{ fontStyle: "italic", color: APRICOT }}>dread.</span>
        </h1>
        <p style={{
          fontSize: 17, lineHeight: 1.65, color: "rgba(45,48,104,0.7)",
          maxWidth: 460, marginBottom: 32,
        }}>
          Quarterly dates, deductions, license rules — every obligation a US side hustler faces, in plain English. 60 seconds.
        </p>
        <div style={{ display: "inline-flex", gap: 12, alignItems: "center" }}>
          <a style={{
            background: INDIGO, color: PAPER, padding: "15px 32px",
            borderRadius: 100, fontWeight: 600, fontSize: 15,
            textDecoration: "none",
          }}>Start free check →</a>
          <a style={{
            color: INDIGO, padding: "15px 8px",
            fontWeight: 500, fontSize: 15, textDecoration: "none",
            borderBottom: `1px solid ${APRICOT}`,
          }}>Sample report</a>
        </div>
      </div>
    </div>
  );
}

Object.assign(window, {
  LogoShield, LogoMonogram, LogoArc, LogoCrest, Wordmark,
  LogoLineup, SplashA, SplashB, SplashC,
});
