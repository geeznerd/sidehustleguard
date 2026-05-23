// Three "What we check" redesign directions
// Each renders inside a fixed-size design canvas artboard

const CHECKS = [
  {
    n: "01",
    title: "Tax obligations",
    short: "SE tax, quarterly payments, 1099 thresholds.",
    long: "15.3% self-employment tax kicks in above $400 net. Most platforms withhold nothing. We flag the exact obligations for your hustle and state.",
    glyph: "§",
    metric: "15.3%",
    metricLabel: "SE tax rate",
  },
  {
    n: "02",
    title: "Business structure",
    short: "Sole prop, LLC, or S-corp — for your numbers.",
    long: "An LLC adds protection. S-corp election only saves taxes above ~$40k net. We compare all three against your actual income.",
    glyph: "⌂",
    metric: "$40k",
    metricLabel: "S-corp breakpoint",
  },
  {
    n: "03",
    title: "Licenses & permits",
    short: "State, city, and home-occupation rules.",
    long: "Some states require licenses even for digital sellers. Operating without the right one can mean fines or forced closure.",
    glyph: "✦",
    metric: "50",
    metricLabel: "states checked",
  },
  {
    n: "04",
    title: "Sales tax",
    short: "Marketplace facilitator vs. direct sales.",
    long: "Etsy and Amazon collect for you in most states. Your own Shopify store, or crossing nexus thresholds, can still create an obligation.",
    glyph: "%",
    metric: "45+",
    metricLabel: "nexus rules",
  },
  {
    n: "05",
    title: "Missed deductions",
    short: "Home office, equipment, software, health.",
    long: "Self-employed health insurance, half of SE tax, and the §199A QBI deduction are the three most-missed — and they meaningfully cut your bill.",
    glyph: "−",
    metric: "20%",
    metricLabel: "QBI deduction",
  },
  {
    n: "06",
    title: "Deadlines",
    short: "Quarterly dates and annual filings.",
    long: "Estimated payments are due Apr 15, Jun 15, Sep 15, Jan 15. Miss one and you owe an underpayment penalty even if you pay in full at year-end.",
    glyph: "◐",
    metric: "4",
    metricLabel: "quarterly dates",
  },
];

// ────────────────────────────────────────────────────────────
// DIRECTION A — EDITORIAL MAGAZINE
// Cream paper, ink black, ochre accent, big italic serif,
// numbered like an article series, dense rules and marginalia
// ────────────────────────────────────────────────────────────
function DirectionEditorial() {
  const [hover, setHover] = React.useState(null);
  const styles = {
    root: {
      width: "100%",
      height: "100%",
      background: "#f3ede0",
      color: "#1a1715",
      fontFamily: "'Newsreader', Georgia, serif",
      padding: "56px 64px 64px",
      position: "relative",
      overflow: "hidden",
      boxSizing: "border-box",
    },
    grain: {
      position: "absolute", inset: 0, pointerEvents: "none",
      backgroundImage: "radial-gradient(rgba(26,23,21,0.06) 1px, transparent 1px)",
      backgroundSize: "3px 3px", opacity: 0.4, mixBlendMode: "multiply",
    },
    masthead: {
      display: "flex", justifyContent: "space-between", alignItems: "baseline",
      borderBottom: "1px solid #1a1715", paddingBottom: 14, marginBottom: 32,
      fontFamily: "'JetBrains Mono', monospace", fontSize: 11,
      letterSpacing: "0.16em", textTransform: "uppercase",
    },
    issue: { color: "#9c6a1f" },
    h2: {
      fontFamily: "'Newsreader', Georgia, serif",
      fontWeight: 400, fontStyle: "italic",
      fontSize: 88, lineHeight: 0.95, letterSpacing: "-0.02em",
      marginBottom: 8, color: "#1a1715",
    },
    h2Plain: { fontStyle: "normal", fontWeight: 500 },
    kicker: {
      fontFamily: "'JetBrains Mono', monospace", fontSize: 12,
      letterSpacing: "0.18em", textTransform: "uppercase",
      color: "#9c6a1f", marginBottom: 24,
    },
    standfirst: {
      fontSize: 18, lineHeight: 1.55, color: "#3a342f",
      maxWidth: 580, marginBottom: 44, fontStyle: "italic",
    },
    grid: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      borderTop: "1px solid #1a1715",
    },
    item: (i, isHover) => ({
      display: "grid",
      gridTemplateColumns: "60px 1fr",
      gap: 22,
      padding: "26px 0 28px",
      borderBottom: "1px solid rgba(26,23,21,0.18)",
      borderRight: i % 2 === 0 ? "1px solid rgba(26,23,21,0.18)" : "none",
      paddingRight: i % 2 === 0 ? 32 : 0,
      paddingLeft: i % 2 === 1 ? 32 : 0,
      cursor: "pointer",
      background: isHover ? "rgba(156,106,31,0.06)" : "transparent",
      transition: "background .25s ease",
    }),
    folio: {
      fontFamily: "'Newsreader', Georgia, serif",
      fontStyle: "italic", fontWeight: 400,
      fontSize: 44, lineHeight: 1, color: "#9c6a1f",
    },
    iTitle: {
      fontFamily: "'Newsreader', Georgia, serif",
      fontWeight: 500, fontSize: 26, lineHeight: 1.15,
      marginBottom: 6, letterSpacing: "-0.01em",
    },
    iShort: {
      fontFamily: "'JetBrains Mono', monospace", fontSize: 11,
      letterSpacing: "0.06em", color: "#6b5e51", marginBottom: 12,
      textTransform: "uppercase",
    },
    iLong: {
      fontSize: 14.5, lineHeight: 1.6, color: "#3a342f",
      maxWidth: 360,
    },
    iMetric: (isHover) => ({
      marginTop: 14, display: "inline-flex", alignItems: "baseline", gap: 8,
      fontFamily: "'Newsreader', serif", fontSize: 22, fontWeight: 500,
      color: "#1a1715",
      transform: isHover ? "translateX(4px)" : "translateX(0)",
      transition: "transform .25s",
    }),
    iMetricLabel: {
      fontFamily: "'JetBrains Mono', monospace", fontSize: 10,
      letterSpacing: "0.1em", textTransform: "uppercase", color: "#9c6a1f",
    },
  };
  return (
    <div style={styles.root}>
      <div style={styles.grain} />
      <div style={styles.masthead}>
        <span>SideHustleGuard <span style={styles.issue}>· Vol. I</span></span>
        <span>What we check / Six chapters</span>
        <span>50 states · est. 2024</span>
      </div>
      <div style={styles.kicker}>— A field guide</div>
      <h2 style={styles.h2}>
        Everything you actually<br />
        <span style={styles.h2Plain}>need to know.</span>
      </h2>
      <p style={styles.standfirst}>
        Six chapters covering every legal and tax obligation a US side hustler is likely to face. Plain English, with a footnote when one is owed.
      </p>
      <div style={styles.grid}>
        {CHECKS.map((c, i) => (
          <div
            key={c.n}
            style={styles.item(i, hover === i)}
            onMouseEnter={() => setHover(i)}
            onMouseLeave={() => setHover(null)}
          >
            <div style={styles.folio}>{c.n}.</div>
            <div>
              <div style={styles.iTitle}>{c.title}</div>
              <div style={styles.iShort}>{c.short}</div>
              <div style={styles.iLong}>{c.long}</div>
              <div style={styles.iMetric(hover === i)}>
                {c.metric}
                <span style={styles.iMetricLabel}>{c.metricLabel}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

// ────────────────────────────────────────────────────────────
// DIRECTION B — CALM UTILITY
// Off-white, single muted accent, mono tags, Linear/Stripe vibe
// Each row reveals a tidy detail panel on hover
// ────────────────────────────────────────────────────────────
function DirectionCalm() {
  const [active, setActive] = React.useState(0);
  const accent = "#0e6b5e"; // muted teal
  const styles = {
    root: {
      width: "100%", height: "100%",
      background: "#fafaf7", color: "#0c0d0e",
      fontFamily: "'Geist', 'Geist Sans', -apple-system, system-ui, sans-serif",
      padding: "64px 72px", boxSizing: "border-box",
      display: "grid",
      gridTemplateColumns: "minmax(0, 0.85fr) minmax(0, 1fr)",
      gap: 64, alignItems: "start",
    },
    leftKicker: {
      fontFamily: "'Geist Mono', ui-monospace, monospace",
      fontSize: 11, letterSpacing: "0.08em", textTransform: "uppercase",
      color: accent, marginBottom: 14,
      display: "inline-flex", alignItems: "center", gap: 8,
    },
    dot: { width: 6, height: 6, borderRadius: "50%", background: accent },
    h2: {
      fontFamily: "'Geist', sans-serif",
      fontSize: 56, fontWeight: 500, lineHeight: 1.02,
      letterSpacing: "-0.025em", color: "#0c0d0e", marginBottom: 22,
    },
    h2Sub: { color: "#7a7d80" },
    leftP: {
      fontSize: 15, lineHeight: 1.65, color: "#52555a",
      maxWidth: 380, marginBottom: 28, fontWeight: 400,
    },
    metricRow: {
      display: "grid", gridTemplateColumns: "1fr 1fr",
      gap: 16, marginTop: 32, paddingTop: 24,
      borderTop: "1px solid #e8e7e1",
    },
    metric: {},
    metricNum: {
      fontFamily: "'Geist', sans-serif",
      fontSize: 32, fontWeight: 500, letterSpacing: "-0.02em",
      color: "#0c0d0e", lineHeight: 1,
    },
    metricLabel: {
      fontSize: 12, color: "#7a7d80", marginTop: 6, fontWeight: 400,
    },
    list: {
      border: "1px solid #e8e7e1", borderRadius: 14,
      background: "#fff", overflow: "hidden",
    },
    row: (isActive) => ({
      display: "grid", gridTemplateColumns: "44px 1fr auto",
      alignItems: "center", gap: 16,
      padding: "18px 22px",
      borderBottom: "1px solid #f0efe9",
      cursor: "pointer",
      background: isActive ? "#f7f7f3" : "transparent",
      transition: "background .18s ease",
    }),
    rowTag: {
      fontFamily: "'Geist Mono', monospace", fontSize: 11,
      color: "#9a9da0", letterSpacing: "0.04em",
    },
    rowTitle: (isActive) => ({
      fontSize: 15, fontWeight: 500, color: "#0c0d0e",
      letterSpacing: "-0.005em",
    }),
    rowSub: { fontSize: 13, color: "#7a7d80", marginTop: 2, fontWeight: 400 },
    chev: (isActive) => ({
      color: isActive ? accent : "#bcbfc2",
      fontSize: 14, transition: "transform .2s, color .2s",
      transform: isActive ? "rotate(90deg)" : "rotate(0deg)",
    }),
    detail: {
      padding: "22px 22px 22px 82px",
      background: "#f7f7f3",
      borderBottom: "1px solid #f0efe9",
      animation: "calmExpand .22s ease",
    },
    detailText: {
      fontSize: 14, lineHeight: 1.6, color: "#3a3d40",
      maxWidth: 460, marginBottom: 14,
    },
    detailMeta: {
      display: "inline-flex", alignItems: "baseline", gap: 10,
      padding: "6px 12px", borderRadius: 8,
      background: "#fff", border: "1px solid #e8e7e1",
      fontFamily: "'Geist Mono', monospace",
    },
    detailMetric: { fontSize: 13, color: accent, fontWeight: 500 },
    detailLabel: { fontSize: 11, color: "#7a7d80", letterSpacing: "0.04em" },
  };
  return (
    <div style={styles.root}>
      <style>{`@keyframes calmExpand { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }`}</style>
      <div>
        <div style={styles.leftKicker}><span style={styles.dot}></span>What we check</div>
        <h2 style={styles.h2}>
          Six checks.<br />
          <span style={styles.h2Sub}>One quiet report.</span>
        </h2>
        <p style={styles.leftP}>
          Tax, structure, licenses — every obligation a US side hustler is likely to face, in plain English. No noise, no upsell calls.
        </p>
        <div style={styles.metricRow}>
          <div>
            <div style={styles.metricNum}>50</div>
            <div style={styles.metricLabel}>states · all rules</div>
          </div>
          <div>
            <div style={styles.metricNum}>60s</div>
            <div style={styles.metricLabel}>median check time</div>
          </div>
          <div>
            <div style={styles.metricNum}>$5</div>
            <div style={styles.metricLabel}>full report · no sub</div>
          </div>
          <div>
            <div style={styles.metricNum}>0</div>
            <div style={styles.metricLabel}>data stored</div>
          </div>
        </div>
      </div>
      <div style={styles.list}>
        {CHECKS.map((c, i) => (
          <React.Fragment key={c.n}>
            <div
              style={styles.row(active === i)}
              onMouseEnter={() => setActive(i)}
            >
              <div style={styles.rowTag}>{c.n}</div>
              <div>
                <div style={styles.rowTitle(active === i)}>{c.title}</div>
                <div style={styles.rowSub}>{c.short}</div>
              </div>
              <div style={styles.chev(active === i)}>→</div>
            </div>
            {active === i && (
              <div style={styles.detail}>
                <div style={styles.detailText}>{c.long}</div>
                <div style={styles.detailMeta}>
                  <span style={styles.detailMetric}>{c.metric}</span>
                  <span style={styles.detailLabel}>{c.metricLabel}</span>
                </div>
              </div>
            )}
          </React.Fragment>
        ))}
      </div>
    </div>
  );
}

// ────────────────────────────────────────────────────────────
// DIRECTION C — BOLD MAXIMALIST + INTERACTIVE
// Dark canvas, electric lime accent, chunky display type,
// auto-cycling spotlight tile + huge hover state
// ────────────────────────────────────────────────────────────
function DirectionMaximalist() {
  const [active, setActive] = React.useState(0);
  const [paused, setPaused] = React.useState(false);

  React.useEffect(() => {
    if (paused) return;
    const id = setInterval(() => setActive((a) => (a + 1) % CHECKS.length), 2400);
    return () => clearInterval(id);
  }, [paused]);

  const lime = "#d8ff3d";
  const ink = "#0a0a0a";
  const styles = {
    root: {
      width: "100%", height: "100%",
      background: ink, color: "#fff",
      fontFamily: "'Bricolage Grotesque', system-ui, sans-serif",
      padding: "48px 56px", boxSizing: "border-box",
      position: "relative", overflow: "hidden",
    },
    bgGrid: {
      position: "absolute", inset: 0, pointerEvents: "none",
      backgroundImage: "linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px)",
      backgroundSize: "48px 48px",
    },
    glow: {
      position: "absolute", top: -100, right: -80, width: 460, height: 460,
      borderRadius: "50%",
      background: "radial-gradient(circle, rgba(216,255,61,0.18), transparent 65%)",
      pointerEvents: "none",
    },
    head: {
      display: "flex", justifyContent: "space-between", alignItems: "flex-end",
      marginBottom: 32, position: "relative",
    },
    kicker: {
      fontFamily: "'Space Mono', ui-monospace, monospace",
      fontSize: 11, letterSpacing: "0.2em", textTransform: "uppercase",
      color: lime, marginBottom: 14,
    },
    h2: {
      fontFamily: "'Bricolage Grotesque', sans-serif",
      fontSize: 92, fontWeight: 800, lineHeight: 0.92,
      letterSpacing: "-0.04em", color: "#fff",
      fontVariationSettings: "'wdth' 90",
    },
    h2Out: {
      WebkitTextStroke: "2px #fff",
      color: "transparent",
    },
    headRight: {
      fontFamily: "'Space Mono', monospace", fontSize: 11,
      color: "rgba(255,255,255,0.5)", letterSpacing: "0.1em",
      textTransform: "uppercase", textAlign: "right", lineHeight: 1.7,
    },
    layout: {
      display: "grid", gridTemplateColumns: "1.15fr 1fr", gap: 24,
      position: "relative", height: "calc(100% - 200px)",
      minHeight: 380,
    },
    spotlight: {
      background: lime, color: ink,
      borderRadius: 24, padding: "36px 40px",
      position: "relative", overflow: "hidden",
      display: "flex", flexDirection: "column", justifyContent: "space-between",
    },
    spotN: {
      fontFamily: "'Space Mono', monospace", fontSize: 13,
      letterSpacing: "0.16em", marginBottom: 8,
    },
    spotGlyph: {
      position: "absolute", top: 24, right: 32,
      fontSize: 180, fontWeight: 600, lineHeight: 0.8,
      color: "rgba(10,10,10,0.08)",
      fontFamily: "'Bricolage Grotesque', sans-serif",
    },
    spotTitle: {
      fontFamily: "'Bricolage Grotesque', sans-serif",
      fontSize: 56, fontWeight: 700, lineHeight: 0.95,
      letterSpacing: "-0.03em", marginBottom: 14, marginTop: 12,
    },
    spotLong: {
      fontSize: 16, lineHeight: 1.55, color: "rgba(10,10,10,0.78)",
      maxWidth: 480, marginBottom: 22,
    },
    spotMetric: {
      display: "inline-flex", alignItems: "baseline", gap: 10,
      paddingTop: 18, borderTop: "1.5px solid rgba(10,10,10,0.18)",
    },
    spotMetricNum: {
      fontFamily: "'Bricolage Grotesque', sans-serif",
      fontSize: 56, fontWeight: 700, letterSpacing: "-0.03em",
      lineHeight: 1, color: ink,
    },
    spotMetricLabel: {
      fontFamily: "'Space Mono', monospace", fontSize: 11,
      letterSpacing: "0.12em", textTransform: "uppercase", color: ink,
    },
    grid: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: 10,
    },
    tile: (i, isActive) => ({
      background: isActive ? "rgba(216,255,61,0.08)" : "rgba(255,255,255,0.04)",
      border: `1px solid ${isActive ? lime : "rgba(255,255,255,0.1)"}`,
      borderRadius: 14, padding: "16px 18px",
      cursor: "pointer",
      transition: "background .25s, border-color .25s, transform .25s",
      transform: isActive ? "translateY(-2px)" : "translateY(0)",
      position: "relative", overflow: "hidden",
      display: "flex", flexDirection: "column", justifyContent: "space-between",
      minHeight: 110,
    }),
    tileN: {
      fontFamily: "'Space Mono', monospace", fontSize: 11,
      color: "rgba(255,255,255,0.4)", letterSpacing: "0.1em",
    },
    tileTitle: (isActive) => ({
      fontFamily: "'Bricolage Grotesque', sans-serif",
      fontSize: 18, fontWeight: 600, marginTop: 10,
      letterSpacing: "-0.01em",
      color: isActive ? lime : "#fff",
    }),
    tileGlyph: (isActive) => ({
      position: "absolute", right: 12, bottom: 0,
      fontSize: 60, lineHeight: 0.8, fontWeight: 600,
      color: isActive ? "rgba(216,255,61,0.18)" : "rgba(255,255,255,0.05)",
      fontFamily: "'Bricolage Grotesque', sans-serif",
      transition: "color .25s",
    }),
    progress: {
      position: "absolute", left: 0, bottom: 0, height: 2,
      background: lime,
      width: "100%",
      transformOrigin: "left",
      animation: paused ? "none" : "maxProg 2.4s linear infinite",
    },
  };
  const c = CHECKS[active];
  return (
    <div
      style={styles.root}
      onMouseEnter={() => setPaused(true)}
      onMouseLeave={() => setPaused(false)}
    >
      <style>{`
        @keyframes maxProg { from { transform: scaleX(0); } to { transform: scaleX(1); } }
        @keyframes maxFade { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
      `}</style>
      <div style={styles.bgGrid} />
      <div style={styles.glow} />
      <div style={styles.head}>
        <div>
          <div style={styles.kicker}>// What we check</div>
          <h2 style={styles.h2}>
            Six checks.<br />
            <span style={styles.h2Out}>Zero surprises.</span>
          </h2>
        </div>
        <div style={styles.headRight}>
          [auto-cycle]<br />
          hover to pause<br />
          click to pin
        </div>
      </div>
      <div style={styles.layout}>
        <div style={styles.spotlight} key={active}>
          <div style={styles.spotGlyph}>{c.glyph}</div>
          <div>
            <div style={styles.spotN}>// CHECK {c.n} / 06</div>
            <div style={styles.spotTitle}>{c.title}</div>
            <div style={styles.spotLong}>{c.long}</div>
          </div>
          <div style={styles.spotMetric}>
            <div style={styles.spotMetricNum}>{c.metric}</div>
            <div style={styles.spotMetricLabel}>{c.metricLabel}</div>
          </div>
          <div style={styles.progress} />
        </div>
        <div style={styles.grid}>
          {CHECKS.map((cc, i) => (
            <div
              key={cc.n}
              style={styles.tile(i, active === i)}
              onMouseEnter={() => setActive(i)}
            >
              <div style={styles.tileN}>{cc.n}</div>
              <div style={styles.tileTitle(active === i)}>{cc.title}</div>
              <div style={styles.tileGlyph(active === i)}>{cc.glyph}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

// ────────────────────────────────────────────────────────────
// DIRECTION D — WARM MODERN
// Clay/paprika on warm cream. Confident sans, soft motion,
// each card has a colored corner that animates on hover.
// Has personality without shouting.
// ────────────────────────────────────────────────────────────
function DirectionWarmModern() {
  const [hover, setHover] = React.useState(null);
  const clay = "#c2533a";
  const moss = "#5a6b3f";
  const ink = "#1c1a17";
  const cream = "#f5efe4";
  // pair a soft accent to each card
  const accents = [clay, moss, "#a87c2e", clay, moss, "#a87c2e"];

  const styles = {
    root: {
      width: "100%", height: "100%",
      background: cream, color: ink,
      fontFamily: "'Instrument Sans', 'Inter', system-ui, sans-serif",
      padding: "56px 64px", boxSizing: "border-box",
      position: "relative", overflow: "hidden",
    },
    head: {
      display: "grid", gridTemplateColumns: "1.2fr 1fr",
      gap: 64, alignItems: "end", marginBottom: 44,
    },
    kicker: {
      fontFamily: "'Instrument Sans', sans-serif",
      fontSize: 12, letterSpacing: "0.12em", textTransform: "uppercase",
      color: clay, marginBottom: 18, fontWeight: 500,
      display: "inline-flex", alignItems: "center", gap: 10,
    },
    kdash: { width: 28, height: 1.5, background: clay, display: "inline-block" },
    h2: {
      fontFamily: "'Instrument Serif', 'Newsreader', Georgia, serif",
      fontSize: 76, fontWeight: 400, lineHeight: 0.98,
      letterSpacing: "-0.025em", color: ink,
    },
    h2It: { fontStyle: "italic", color: clay },
    rightCol: {
      fontSize: 15.5, lineHeight: 1.65, color: "#4a463f",
      maxWidth: 380, paddingBottom: 8,
    },
    meta: {
      display: "flex", gap: 24, marginTop: 18,
      fontFamily: "'JetBrains Mono', ui-monospace, monospace",
      fontSize: 11, letterSpacing: "0.04em", color: "#6b6457",
      textTransform: "uppercase",
    },
    metaItem: { display: "inline-flex", alignItems: "center", gap: 6 },
    metaDot: (c) => ({ width: 6, height: 6, borderRadius: "50%", background: c }),
    grid: {
      display: "grid", gridTemplateColumns: "repeat(3, 1fr)",
      gap: 14,
    },
    card: (i, isHover) => ({
      background: "#fbf7ee",
      border: `1px solid ${isHover ? accents[i] : "rgba(28,26,23,0.1)"}`,
      borderRadius: 18, padding: "26px 24px 24px",
      cursor: "pointer", position: "relative", overflow: "hidden",
      transition: "border-color .25s, transform .25s",
      transform: isHover ? "translateY(-3px)" : "translateY(0)",
      minHeight: 250,
      display: "flex", flexDirection: "column", justifyContent: "space-between",
    }),
    // animated corner bar
    corner: (i, isHover) => ({
      position: "absolute", top: 0, left: 0,
      width: isHover ? "100%" : 56, height: 3,
      background: accents[i],
      transition: "width .35s cubic-bezier(0.4, 0, 0.2, 1)",
    }),
    cardN: {
      fontFamily: "'JetBrains Mono', monospace",
      fontSize: 11, letterSpacing: "0.1em", color: "#9a9081",
      marginBottom: 14, marginTop: 4,
    },
    cardTitle: {
      fontFamily: "'Instrument Serif', Georgia, serif",
      fontSize: 26, fontWeight: 400, lineHeight: 1.1,
      letterSpacing: "-0.015em", marginBottom: 8, color: ink,
    },
    cardLong: {
      fontSize: 13.5, lineHeight: 1.6, color: "#4a463f",
      marginBottom: 14,
    },
    cardFoot: {
      display: "flex", justifyContent: "space-between", alignItems: "baseline",
      paddingTop: 14, borderTop: "1px solid rgba(28,26,23,0.08)",
    },
    cardMetric: (i) => ({
      fontFamily: "'Instrument Serif', serif",
      fontStyle: "italic",
      fontSize: 22, fontWeight: 500, color: accents[i], lineHeight: 1,
    }),
    cardMetricLbl: {
      fontFamily: "'JetBrains Mono', monospace",
      fontSize: 10, letterSpacing: "0.08em", color: "#6b6457",
      textTransform: "uppercase",
    },
  };
  return (
    <div style={styles.root}>
      <div style={styles.head}>
        <div>
          <div style={styles.kicker}><span style={styles.kdash}></span>What we check</div>
          <h2 style={styles.h2}>
            Six checks for the<br />
            <span style={styles.h2It}>whole picture.</span>
          </h2>
        </div>
        <div>
          <p style={styles.rightCol}>
            Every legal and tax obligation a US side hustler is likely to face — tailored to your state, your hustle, and your numbers.
          </p>
          <div style={styles.meta}>
            <span style={styles.metaItem}><span style={styles.metaDot(clay)}></span>50 states</span>
            <span style={styles.metaItem}><span style={styles.metaDot(moss)}></span>60s check</span>
            <span style={styles.metaItem}><span style={styles.metaDot("#a87c2e")}></span>no signup</span>
          </div>
        </div>
      </div>
      <div style={styles.grid}>
        {CHECKS.map((c, i) => (
          <div
            key={c.n}
            style={styles.card(i, hover === i)}
            onMouseEnter={() => setHover(i)}
            onMouseLeave={() => setHover(null)}
          >
            <div style={styles.corner(i, hover === i)}></div>
            <div>
              <div style={styles.cardN}>— {c.n}</div>
              <div style={styles.cardTitle}>{c.title}</div>
              <div style={styles.cardLong}>{c.long}</div>
            </div>
            <div style={styles.cardFoot}>
              <span style={styles.cardMetric(i)}>{c.metric}</span>
              <span style={styles.cardMetricLbl}>{c.metricLabel}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

// ────────────────────────────────────────────────────────────
// DIRECTION E — SOFT INTERACTIVE
// Light periwinkle/cream with deep indigo + apricot accent.
// Animated indicator slides along a vertical list.
// Has motion + interaction without being "loud".
// ────────────────────────────────────────────────────────────
function DirectionSoftInteractive() {
  const [active, setActive] = React.useState(0);
  const indigo = "#2d3068";
  const apricot = "#e89464";
  const cream = "#f0ece1";
  const paper = "#fbf8ee";

  const styles = {
    root: {
      width: "100%", height: "100%",
      background: cream, color: indigo,
      fontFamily: "'Inter', system-ui, sans-serif",
      padding: "56px 60px", boxSizing: "border-box",
      display: "grid",
      gridTemplateColumns: "minmax(0, 0.9fr) minmax(0, 1.1fr)",
      gap: 48, alignItems: "stretch",
      position: "relative", overflow: "hidden",
    },
    // soft blob bg
    blob: {
      position: "absolute", bottom: -120, left: -100,
      width: 380, height: 380, borderRadius: "50%",
      background: "radial-gradient(circle, rgba(232,148,100,0.18), transparent 65%)",
      pointerEvents: "none",
    },
    left: { display: "flex", flexDirection: "column", justifyContent: "space-between" },
    kicker: {
      fontFamily: "'Inter', sans-serif",
      fontSize: 12, letterSpacing: "0.14em", textTransform: "uppercase",
      color: apricot, marginBottom: 18, fontWeight: 600,
    },
    h2: {
      fontFamily: "'Fraunces', 'Newsreader', Georgia, serif",
      fontVariationSettings: "'opsz' 144, 'SOFT' 30",
      fontSize: 64, fontWeight: 400, lineHeight: 1.0,
      letterSpacing: "-0.022em", color: indigo, marginBottom: 22,
    },
    h2It: { fontStyle: "italic", color: apricot },
    leftP: {
      fontSize: 15.5, lineHeight: 1.65, color: "rgba(45,48,104,0.7)",
      maxWidth: 380, marginBottom: 28, fontWeight: 400,
    },
    // big illustrative preview card on bottom-left
    preview: {
      background: indigo, color: paper, borderRadius: 22,
      padding: "26px 28px", position: "relative", overflow: "hidden",
      minHeight: 220,
    },
    pvN: {
      fontFamily: "'Inter', sans-serif", fontSize: 11,
      letterSpacing: "0.16em", color: apricot, textTransform: "uppercase",
      marginBottom: 14, fontWeight: 600,
    },
    pvTitle: {
      fontFamily: "'Fraunces', serif",
      fontSize: 32, fontWeight: 400, lineHeight: 1.1,
      letterSpacing: "-0.015em", marginBottom: 14,
    },
    pvLong: {
      fontSize: 13.5, lineHeight: 1.65, color: "rgba(251,248,238,0.7)",
      marginBottom: 20,
    },
    pvFoot: {
      display: "flex", alignItems: "baseline", gap: 12,
      paddingTop: 16, borderTop: "1px solid rgba(251,248,238,0.12)",
    },
    pvNum: {
      fontFamily: "'Fraunces', serif", fontSize: 38, fontWeight: 500,
      color: apricot, lineHeight: 1, fontStyle: "italic",
    },
    pvLbl: {
      fontFamily: "'Inter', sans-serif", fontSize: 11,
      color: "rgba(251,248,238,0.55)", letterSpacing: "0.08em",
      textTransform: "uppercase",
    },
    // right list
    listWrap: {
      background: paper, borderRadius: 22,
      padding: 10,
      border: "1px solid rgba(45,48,104,0.08)",
      position: "relative",
      display: "flex", flexDirection: "column",
    },
    // sliding indicator
    indicator: (i) => ({
      position: "absolute",
      left: 10, right: 10,
      top: 10 + i * 68,
      height: 68,
      background: cream,
      borderRadius: 14,
      transition: "top .35s cubic-bezier(0.4, 0, 0.2, 1)",
      border: `1px solid ${apricot}`,
    }),
    row: (isActive) => ({
      position: "relative", zIndex: 1,
      display: "grid", gridTemplateColumns: "44px 1fr auto",
      alignItems: "center", gap: 16, padding: "0 18px",
      height: 68, cursor: "pointer",
    }),
    rowN: (isActive) => ({
      fontFamily: "'Fraunces', serif", fontStyle: "italic",
      fontSize: 26, fontWeight: 500,
      color: isActive ? apricot : "rgba(45,48,104,0.35)",
      transition: "color .25s",
      lineHeight: 1,
    }),
    rowTitle: (isActive) => ({
      fontFamily: "'Inter', sans-serif", fontSize: 15.5,
      fontWeight: 600, color: indigo,
      letterSpacing: "-0.005em",
    }),
    rowShort: { fontSize: 12.5, color: "rgba(45,48,104,0.55)", marginTop: 2 },
    rowMetric: (isActive) => ({
      fontFamily: "'Fraunces', serif", fontStyle: "italic",
      fontSize: 18, fontWeight: 500,
      color: isActive ? apricot : "rgba(45,48,104,0.4)",
      transition: "color .25s",
    }),
  };
  const c = CHECKS[active];
  return (
    <div style={styles.root}>
      <div style={styles.blob}></div>
      <div style={styles.left}>
        <div>
          <div style={styles.kicker}>What we check ✦</div>
          <h2 style={styles.h2}>
            Quietly thorough.<br />
            <span style={styles.h2It}>Built for sleep.</span>
          </h2>
          <p style={styles.leftP}>
            We walk through six things — slowly, in plain English — so nothing surprises you in April.
          </p>
        </div>
        <div style={styles.preview} key={active}>
          <div style={styles.pvN}>Check {c.n} of 06</div>
          <div style={styles.pvTitle}>{c.title}</div>
          <div style={styles.pvLong}>{c.long}</div>
          <div style={styles.pvFoot}>
            <span style={styles.pvNum}>{c.metric}</span>
            <span style={styles.pvLbl}>{c.metricLabel}</span>
          </div>
        </div>
      </div>
      <div style={styles.listWrap}>
        <div style={styles.indicator(active)}></div>
        {CHECKS.map((cc, i) => (
          <div
            key={cc.n}
            style={styles.row(active === i)}
            onMouseEnter={() => setActive(i)}
          >
            <div style={styles.rowN(active === i)}>{cc.n}</div>
            <div>
              <div style={styles.rowTitle(active === i)}>{cc.title}</div>
              <div style={styles.rowShort}>{cc.short}</div>
            </div>
            <div style={styles.rowMetric(active === i)}>{cc.metric}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

Object.assign(window, { DirectionEditorial, DirectionCalm, DirectionMaximalist, DirectionWarmModern, DirectionSoftInteractive });
