// SideHustleGuard /guides redesign — Direction E
// Desktop + Mobile variants share the same component tree; the `mobile` prop
// switches layout density, hero composition, and sticky-nav behavior.

const G_INDIGO = "#2d3068";
const G_APRICOT = "#e89464";
const G_CREAM = "#f0ece1";
const G_PAPER = "#fbf8ee";
const G_INK_70 = "rgba(45,48,104,0.7)";
const G_INK_55 = "rgba(45,48,104,0.55)";
const G_INK_35 = "rgba(45,48,104,0.35)";
const G_INK_08 = "rgba(45,48,104,0.08)";
const G_INK_12 = "rgba(45,48,104,0.12)";

// ─── Logo (Arc & Dot) — reused inline ─────────────────────────
function GLogo({ size = 28, dark = false }) {
  const c = dark ? G_PAPER : G_INDIGO;
  return (
    <svg width={size} height={size} viewBox="0 0 48 48" fill="none">
      <path d="M6 30 Q24 4 42 30" stroke={c} strokeWidth="2.4" strokeLinecap="round" fill="none"/>
      <path d="M14 32 Q24 18 34 32" stroke={G_APRICOT} strokeWidth="2.4" strokeLinecap="round" fill="none"/>
      <circle cx="24" cy="36" r="2.4" fill={c}/>
    </svg>
  );
}

function GWordmark({ size = 17, dark = false }) {
  return (
    <span style={{
      display: "inline-flex", alignItems: "baseline", lineHeight: 1,
      letterSpacing: "-0.015em",
    }}>
      <span style={{
        fontFamily: "Inter, sans-serif", fontWeight: 600,
        fontSize: size, color: dark ? G_PAPER : G_INDIGO,
      }}>SideHustle</span>
      <span style={{
        fontFamily: "Fraunces, serif", fontStyle: "italic", fontWeight: 500,
        fontSize: size, color: G_APRICOT, marginLeft: 2,
        fontVariationSettings: "'opsz' 144, 'SOFT' 30",
      }}>guard</span>
    </span>
  );
}

// ─── Content data ─────────────────────────────────────────────
const SECTIONS = [
  {
    id: "tools",
    name: "Tools",
    headline: "Interactive tools",
    count: "7 free tools",
    featured: {
      title: "Side Hustle Dashboard",
      titleItalic: "Dashboard",
      blurb: "Enter your income once — audit risk, tax set-aside, and S-Corp savings update live. Download a clean PDF report.",
      pills: ["Audit Shield", "Tax Guard", "S-Corp Sim"],
      href: "/dashboard",
    },
    items: [
      { letter: "A", title: "Audit Risk Estimator", desc: "Your IRS audit risk score with a safety checklist", href: "/audit-risk-estimator", tag: "New" },
      { letter: "T", title: "Tax Guard Calculator", desc: "How much to set aside from every client payment", href: "/tax-guard-calculator", tag: "New" },
      { letter: "S", title: "S-Corp vs Sole Prop Simulator", desc: "See exactly when an S-Corp saves more than it costs", href: "/scorp-savings-calculator", tag: "New" },
      { letter: "C", title: "Self-Employment Tax Calculator", desc: "Instant SE tax estimate — federal + state, 2025 rates", href: "/self-employment-tax-calculator" },
      { letter: "Q", title: "Quarterly Tax Calculator", desc: "How much to set aside and pay each quarter", href: "/quarterly-tax-calculator" },
      { letter: "D", title: "Tax Deduction Checklist", desc: "Every deduction by hustle type — free and printable", href: "/tax-checklist" },
    ],
  },
  {
    id: "gig",
    name: "Gig & Delivery",
    headline: "Gig work & delivery",
    count: "8 guides",
    items: [
      { letter: "U", title: "Uber & Lyft Taxes", desc: "What every rideshare driver actually owes", href: "/uber-lyft-taxes" },
      { letter: "D", title: "DoorDash Taxes", desc: "Mileage, 1099s, and quarterly payments", href: "/doordash-taxes" },
      { letter: "U", title: "Uber Eats Taxes", desc: "Food delivery taxes, 1099s, and mileage", href: "/uber-eats-taxes" },
      { letter: "G", title: "Grubhub Taxes", desc: "Mileage deduction guide for delivery drivers", href: "/grubhub-taxes" },
      { letter: "I", title: "Instacart Taxes", desc: "Tax rules for in-store and full-service shoppers", href: "/instacart-taxes" },
      { letter: "A", title: "Amazon Flex Taxes", desc: "Mileage, deductions, and the 1099-NEC explained", href: "/amazon-flex-taxes" },
      { letter: "T", title: "TaskRabbit Taxes", desc: "Service fees, tools, mileage, and quarterly payments", href: "/taskrabbit-taxes" },
      { letter: "R", title: "Rover Taxes", desc: "Pet sitting, dog walking, and home boarding deductions", href: "/rover-taxes" },
    ],
  },
  {
    id: "str",
    name: "Short-Term Rentals",
    headline: "Short-term rentals",
    count: "28 guides",
    subfilters: ["All", "Platforms", "Topics", "State rules"],
    featured: {
      title: "Complete STR tax guide",
      titleItalic: "STR tax guide",
      blurb: "Platforms, tax strategy, the 14-day rule, the STR loophole, and state rules — all in one place.",
      pills: ["14-day rule", "Loophole", "Cost seg"],
      href: "/short-term-rentals",
    },
    items: [
      { letter: "A", title: "Airbnb Host Taxes", desc: "Deductions, taxes owed, and the 14-day rule", href: "/airbnb-host-taxes" },
      { letter: "V", title: "Vrbo Host Taxes", desc: "Whole-home vacation rental taxes explained", href: "/vrbo-host-taxes", tag: "Soon" },
      { letter: "B", title: "Booking.com Host Taxes", desc: "Taxes for property hosts on Booking.com", href: "/booking-com-host-taxes", tag: "Soon" },
      { letter: "T", title: "Turo Host Taxes", desc: "Car rental income, Schedule C, and deductions", href: "/turo-host-taxes", tag: "Soon" },
      { letter: "H", title: "Hipcamp Host Taxes", desc: "Land and outdoor camping rental taxes", href: "/hipcamp-host-taxes", tag: "Soon" },
      { letter: "R", title: "RV Rental Host Taxes", desc: "RVshare & Outdoorsy income taxes", href: "/rv-rental-host-taxes", tag: "Soon" },
      { letter: "1", title: "The Airbnb 14-Day Rule", desc: "Rent up to 14 days tax-free — here's how", href: "/airbnb-14-day-rule" },
      { letter: "L", title: "The STR Tax Loophole", desc: "Use rental losses to offset W-2 income", href: "/short-term-rental-loophole" },
      { letter: "C", title: "Cost Segregation for STRs", desc: "Accelerate depreciation and cut your tax bill", href: "/cost-segregation-str" },
      { letter: "C", title: "California STR Rules", desc: "Permits, TOT, and state income tax rules", href: "/california-short-term-rental-rules" },
      { letter: "N", title: "New York STR Rules", desc: "NYC restrictions, state and city tax obligations", href: "/new-york-short-term-rental-rules" },
      { letter: "F", title: "Florida STR Taxes", desc: "Sales tax, tourist development tax, no income tax", href: "/florida-short-term-rental-taxes" },
    ],
    more: 16,
  },
  {
    id: "creator",
    name: "Creator",
    headline: "Creator economy",
    count: "8 guides",
    items: [
      { letter: "Y", title: "YouTube Taxes", desc: "AdSense, brand deals, memberships, merch", href: "/youtube-taxes" },
      { letter: "T", title: "Twitch Taxes", desc: "Subs, bits, donations — all of it is taxable", href: "/twitch-taxes" },
      { letter: "T", title: "TikTok Taxes", desc: "Creator Fund, TikTok Shop, and LIVE gifts", href: "/tiktok-taxes" },
      { letter: "O", title: "OnlyFans Taxes", desc: "What creators owe and how to pay less", href: "/onlyfans-taxes" },
      { letter: "F", title: "Fiverr Taxes", desc: "Tax on what you receive, not what clients pay", href: "/fiverr-taxes" },
      { letter: "P", title: "Patreon Taxes", desc: "Membership income, platform fees, and deductions", href: "/patreon-taxes" },
      { letter: "S", title: "Substack Taxes", desc: "Newsletter income, Substack's 10% fee, deductions", href: "/substack-taxes" },
      { letter: "P", title: "Pinterest Taxes", desc: "Affiliate commissions, sponsored pins, and 1099s", href: "/pinterest-taxes" },
    ],
  },
  {
    id: "ecom",
    name: "E-commerce",
    headline: "Etsy, e-commerce & resellers",
    count: "12 guides",
    items: [
      { letter: "E", title: "Etsy Taxes", desc: "The complete Etsy seller tax guide", href: "/etsy-taxes" },
      { letter: "E", title: "Etsy Taxes Under $600", desc: "You still owe tax even below the 1099 threshold", href: "/etsy-taxes-under-600" },
      { letter: "P", title: "PayPal & 1099-K on Etsy", desc: "New $600 threshold rules explained", href: "/paypal-1099k-etsy" },
      { letter: "H", title: "Etsy Home Office Deduction", desc: "How to claim your workspace correctly", href: "/etsy-home-office-deduction" },
      { letter: "S", title: "Etsy Schedule C", desc: "Complete filing guide for Etsy sellers", href: "/etsy-schedule-c" },
      { letter: "L", title: "LLC for Etsy Sellers", desc: "When it's actually worth the paperwork", href: "/llc-etsy-seller" },
      { letter: "R", title: "Reseller Taxes", desc: "General guide for all reselling platforms", href: "/reseller-taxes" },
      { letter: "E", title: "eBay Taxes", desc: "COGS, 1099-K thresholds, casual vs business seller", href: "/ebay-taxes" },
      { letter: "P", title: "Poshmark Taxes", desc: "Fees, COGS, and the personal property rule", href: "/poshmark-taxes" },
    ],
    more: 3,
  },
  {
    id: "freelance",
    name: "Freelancing",
    headline: "Freelancing & self-employment",
    count: "5 guides",
    items: [
      { letter: "S", title: "Side Hustle Taxes", desc: "The complete overview — start here", href: "/side-hustle-taxes" },
      { letter: "F", title: "Freelancer Taxes", desc: "1099s, deductions, and quarterly payments", href: "/freelancer-taxes" },
      { letter: "U", title: "Upwork Taxes", desc: "Service fees, 1099-K, and freelancer deductions", href: "/upwork-taxes" },
      { letter: "Q", title: "Quarterly Taxes", desc: "When to pay and how much each quarter", href: "/quarterly-taxes-self-employed" },
      { letter: "L", title: "LLC vs Sole Proprietor", desc: "Key differences and when it's worth the paperwork", href: "/llc-vs-sole-proprietor" },
    ],
  },
  {
    id: "state",
    name: "State guides",
    headline: "State-specific guides",
    count: "5 guides",
    items: [
      { letter: "C", title: "California Self-Employment Tax", desc: "CA income tax, quarterly schedule, LLC fees", href: "/california-self-employment-tax" },
      { letter: "C", title: "California Side Hustle Rules", desc: "Licenses, AB5 contractor rules, CA requirements", href: "/california-side-hustle" },
      { letter: "T", title: "Texas Self-Employment Tax", desc: "No income tax — here's what you still owe", href: "/texas-self-employment-tax" },
      { letter: "N", title: "New York Self-Employment Tax", desc: "NY state + NYC city tax + MCTMT explained", href: "/new-york-self-employment-tax" },
      { letter: "5", title: "2025 State Tax Rates", desc: "Complete rate table for all 50 states", href: "/state-tax-rates" },
    ],
  },
];

// ─── Topographic SVG backdrop ─────────────────────────────────
function TopoBackdrop() {
  return (
    <svg viewBox="0 0 1200 600" preserveAspectRatio="xMidYMid slice"
      style={{ position: "absolute", inset: 0, width: "100%", height: "100%", pointerEvents: "none" }}
      aria-hidden="true">
      <defs>
        <radialGradient id="gGlow" cx="20%" cy="80%" r="55%">
          <stop offset="0%" stopColor={G_APRICOT} stopOpacity="0.18"/>
          <stop offset="100%" stopColor={G_APRICOT} stopOpacity="0"/>
        </radialGradient>
      </defs>
      <rect width="1200" height="600" fill="url(#gGlow)"/>
      <g fill="none" stroke={G_INDIGO} strokeOpacity="0.07" strokeWidth="1">
        {[0,1,2,3,4,5,6,7,8].map(i => (
          <ellipse key={i}
            cx={300 - i * 6} cy={460 - i * 14}
            rx={460 - i * 35} ry={200 - i * 18}
            transform={`rotate(${-12 + i * 1.5} 300 460)`}/>
        ))}
      </g>
      <g fill="none" stroke={G_APRICOT} strokeOpacity="0.18" strokeWidth="1">
        {[0,1,2,3,4,5].map(i => (
          <ellipse key={i}
            cx={1050 + i * 4} cy={140 - i * 8}
            rx={300 - i * 30} ry={120 - i * 14}
            transform={`rotate(${18 - i * 2} 1050 140)`}/>
        ))}
      </g>
    </svg>
  );
}

// ─── Monogram avatar for guide cards ──────────────────────────
function Monogram({ letter, small }) {
  const s = small ? 28 : 34;
  return (
    <div style={{
      width: s, height: s, borderRadius: 10,
      background: "rgba(232,148,100,0.12)",
      display: "inline-flex", alignItems: "center", justifyContent: "center",
      flexShrink: 0,
    }}>
      <span style={{
        fontFamily: "Fraunces, serif", fontStyle: "italic", fontWeight: 500,
        fontSize: small ? 16 : 19, color: G_APRICOT, lineHeight: 1,
        fontVariationSettings: "'opsz' 144, 'SOFT' 30",
      }}>{letter}</span>
    </div>
  );
}

// ─── Tag pill (New / Soon) ────────────────────────────────────
function Tag({ children, variant }) {
  const colors = variant === "soon"
    ? { bg: G_INK_08, fg: G_INK_55 }
    : { bg: "rgba(232,148,100,0.15)", fg: G_APRICOT };
  return (
    <span style={{
      fontFamily: "Inter, sans-serif", fontSize: 10, fontWeight: 600,
      letterSpacing: "0.08em", textTransform: "uppercase",
      padding: "3px 8px", borderRadius: 100,
      background: colors.bg, color: colors.fg,
      whiteSpace: "nowrap",
    }}>{children}</span>
  );
}

// ─── Guide card ───────────────────────────────────────────────
function GuideCard({ item, mobile }) {
  const [hover, setHover] = React.useState(false);
  return (
    <a href={item.href}
      onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}
      style={{
        background: G_PAPER, borderRadius: 16,
        border: `1px solid ${hover ? G_APRICOT : G_INK_08}`,
        padding: mobile ? "16px 16px 14px" : "18px 20px 16px",
        textDecoration: "none", color: "inherit",
        display: "block", position: "relative",
        transition: "border-color .25s, transform .25s",
        transform: hover ? "translateY(-2px)" : "translateY(0)",
        cursor: "pointer",
      }}>
      <div style={{
        display: "flex", gap: 12, alignItems: "flex-start",
        marginBottom: 10,
      }}>
        <Monogram letter={item.letter} small />
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{
            display: "flex", alignItems: "baseline", gap: 8,
            flexWrap: "wrap",
          }}>
            <span style={{
              fontFamily: "Inter, sans-serif", fontSize: mobile ? 14.5 : 15,
              fontWeight: 600, color: G_INDIGO, letterSpacing: "-0.005em",
              lineHeight: 1.25,
            }}>{item.title}</span>
            {item.tag && <Tag variant={item.tag === "Soon" ? "soon" : "new"}>{item.tag}</Tag>}
          </div>
        </div>
      </div>
      <div style={{
        fontFamily: "Inter, sans-serif", fontSize: 13, lineHeight: 1.5,
        color: G_INK_70, paddingLeft: 0,
      }}>{item.desc}</div>
      <div style={{
        position: "absolute", right: 16, bottom: 12,
        fontSize: 14, color: hover ? G_APRICOT : G_INK_35,
        transition: "color .25s, transform .25s",
        transform: hover ? "translateX(3px)" : "translateX(0)",
      }}>→</div>
    </a>
  );
}

// ─── Featured (mega) card — used for Dashboard + STR overview ─
function FeaturedCard({ data, mobile }) {
  const [hover, setHover] = React.useState(false);
  return (
    <a href={data.href}
      onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}
      style={{
        background: G_INDIGO, color: G_PAPER,
        borderRadius: 18, padding: mobile ? "22px 22px 24px" : "26px 30px 28px",
        textDecoration: "none", display: "block", position: "relative",
        overflow: "hidden", transition: "transform .25s",
        transform: hover ? "translateY(-2px)" : "translateY(0)",
        cursor: "pointer",
        gridColumn: mobile ? "auto" : "1 / -1",
      }}>
      <div style={{
        position: "absolute", top: -80, right: -60,
        width: 240, height: 240, borderRadius: "50%",
        background: "radial-gradient(circle, rgba(232,148,100,0.22), transparent 65%)",
        pointerEvents: "none",
      }}/>
      <div style={{
        fontFamily: "Inter, sans-serif", fontSize: 11, fontWeight: 600,
        letterSpacing: "0.14em", textTransform: "uppercase",
        color: G_APRICOT, marginBottom: 12,
      }}>★ Featured</div>
      <div style={{
        fontFamily: "Fraunces, serif", fontWeight: 400,
        fontSize: mobile ? 28 : 36, lineHeight: 1.05,
        letterSpacing: "-0.015em", marginBottom: 10,
        fontVariationSettings: "'opsz' 144, 'SOFT' 30",
      }}>
        {data.title.replace(data.titleItalic, "")}
        <span style={{ fontStyle: "italic", color: G_APRICOT }}>{data.titleItalic}</span>
      </div>
      <div style={{
        fontFamily: "Inter, sans-serif", fontSize: mobile ? 14 : 14.5,
        lineHeight: 1.6, color: "rgba(251,248,238,0.72)",
        maxWidth: mobile ? "100%" : 540, marginBottom: 16,
      }}>{data.blurb}</div>
      <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: 18 }}>
        {data.pills.map(p => (
          <span key={p} style={{
            fontFamily: "Inter, sans-serif", fontSize: 12, fontWeight: 500,
            padding: "5px 11px", borderRadius: 100,
            background: "rgba(251,248,238,0.1)", color: "rgba(251,248,238,0.85)",
          }}>{p}</span>
        ))}
      </div>
      <div style={{
        display: "inline-flex", alignItems: "center", gap: 8,
        fontFamily: "Inter, sans-serif", fontSize: 13, fontWeight: 600,
        color: G_APRICOT, letterSpacing: "-0.005em",
      }}>
        Open
        <span style={{ transition: "transform .25s", transform: hover ? "translateX(4px)" : "translateX(0)" }}>→</span>
      </div>
    </a>
  );
}

// ─── Section header ───────────────────────────────────────────
function SectionHeader({ data, mobile }) {
  return (
    <div style={{
      display: "flex", justifyContent: "space-between",
      alignItems: mobile ? "flex-start" : "baseline",
      flexDirection: mobile ? "column" : "row",
      gap: mobile ? 6 : 16,
      marginBottom: mobile ? 18 : 24, paddingTop: 4,
    }}>
      <h2 style={{
        fontFamily: "Fraunces, serif", fontWeight: 400,
        fontSize: mobile ? 26 : 36, letterSpacing: "-0.018em",
        lineHeight: 1.1, color: G_INDIGO, margin: 0,
        fontVariationSettings: "'opsz' 144, 'SOFT' 30",
      }}>{data.headline}</h2>
      <div style={{
        fontFamily: "Inter, sans-serif", fontSize: 12, fontWeight: 600,
        letterSpacing: "0.1em", textTransform: "uppercase",
        color: G_INK_55,
      }}>{data.count}</div>
    </div>
  );
}

// ─── Sticky category tabs ─────────────────────────────────────
function CategoryTabs({ active, setActive, mobile }) {
  const tabs = [{ id: "all", name: "All" }, ...SECTIONS.map(s => ({ id: s.id, name: s.name }))];
  return (
    <div style={{
      position: "sticky", top: mobile ? 56 : 64,
      background: "rgba(240,236,225,0.92)",
      backdropFilter: "blur(12px)",
      WebkitBackdropFilter: "blur(12px)",
      borderBottom: `1px solid ${G_INK_08}`,
      zIndex: 10, marginInline: mobile ? -20 : -64,
      padding: mobile ? "0 20px" : "0 64px",
    }}>
      <div style={{
        display: "flex", gap: mobile ? 4 : 6,
        overflowX: "auto", padding: mobile ? "12px 0" : "14px 0",
        scrollbarWidth: "none", msOverflowStyle: "none",
      }}>
        {tabs.map(t => (
          <button key={t.id}
            onClick={() => setActive(t.id)}
            style={{
              fontFamily: "Inter, sans-serif", fontSize: mobile ? 12.5 : 13,
              fontWeight: 500, padding: mobile ? "7px 13px" : "8px 16px",
              borderRadius: 100, border: "none", cursor: "pointer",
              background: active === t.id ? G_INDIGO : "transparent",
              color: active === t.id ? G_PAPER : G_INK_70,
              whiteSpace: "nowrap", transition: "background .2s, color .2s",
              letterSpacing: "-0.005em",
            }}>{t.name}</button>
        ))}
      </div>
    </div>
  );
}

// ─── Main guides page ────────────────────────────────────────
function GuidesPage({ mobile }) {
  const [active, setActive] = React.useState("all");
  const [search, setSearch] = React.useState("");
  const [strFilter, setStrFilter] = React.useState("All");

  const visibleSections = active === "all" ? SECTIONS : SECTIONS.filter(s => s.id === active);

  // search filter
  const q = search.trim().toLowerCase();

  const renderSection = (s) => {
    let items = s.items;
    if (q) items = items.filter(i => i.title.toLowerCase().includes(q) || i.desc.toLowerCase().includes(q));
    if (items.length === 0 && !s.featured) return null;

    return (
      <section key={s.id} id={s.id} style={{ marginBottom: mobile ? 48 : 72 }}>
        <SectionHeader data={s} mobile={mobile} />

        {/* STR has subfilters */}
        {s.subfilters && !q && (
          <div style={{
            display: "flex", gap: 6, marginBottom: 18, flexWrap: "wrap",
          }}>
            {s.subfilters.map(sf => (
              <button key={sf} onClick={() => setStrFilter(sf)}
                style={{
                  fontFamily: "Inter, sans-serif", fontSize: 12,
                  fontWeight: 500, padding: "6px 13px", borderRadius: 100,
                  border: `1px solid ${strFilter === sf ? G_APRICOT : G_INK_08}`,
                  background: strFilter === sf ? "rgba(232,148,100,0.1)" : G_PAPER,
                  color: strFilter === sf ? G_APRICOT : G_INK_70,
                  cursor: "pointer", transition: "all .2s",
                }}>{sf}</button>
            ))}
          </div>
        )}

        <div style={{
          display: "grid",
          gridTemplateColumns: mobile ? "1fr" : "repeat(3, 1fr)",
          gap: mobile ? 10 : 14,
        }}>
          {s.featured && !q && <FeaturedCard data={s.featured} mobile={mobile} />}
          {items.map((item, i) => <GuideCard key={i} item={item} mobile={mobile} />)}
        </div>

        {s.more && !q && (
          <div style={{
            marginTop: 16, textAlign: mobile ? "left" : "center",
          }}>
            <a href={`#${s.id}-all`} style={{
              fontFamily: "Inter, sans-serif", fontSize: 13, fontWeight: 500,
              color: G_APRICOT, textDecoration: "none",
              display: "inline-flex", alignItems: "center", gap: 6,
              padding: "8px 16px", borderRadius: 100,
              border: `1px solid ${G_INK_08}`, background: G_PAPER,
            }}>Show {s.more} more →</a>
          </div>
        )}
      </section>
    );
  };

  return (
    <div style={{
      width: "100%", minHeight: "100%", background: G_CREAM,
      fontFamily: "Inter, sans-serif", color: G_INDIGO,
      paddingBottom: 0,
    }}>
      {/* NAV */}
      <nav style={{
        position: "sticky", top: 0, zIndex: 20,
        background: "rgba(240,236,225,0.96)",
        backdropFilter: "blur(16px)",
        WebkitBackdropFilter: "blur(16px)",
        borderBottom: `1px solid ${G_INK_08}`,
        padding: mobile ? "14px 20px" : "16px 64px",
        display: "flex", justifyContent: "space-between", alignItems: "center",
      }}>
        <a href="/" style={{
          display: "flex", alignItems: "center", gap: 10,
          textDecoration: "none",
        }}>
          <GLogo size={mobile ? 26 : 30} />
          <GWordmark size={mobile ? 15 : 17} />
        </a>
        {!mobile && (
          <div style={{ display: "flex", gap: 28, alignItems: "center" }}>
            <a href="/#how-it-works" style={{ fontSize: 13, color: G_INK_55, textDecoration: "none" }}>How it works</a>
            <a href="/#pricing" style={{ fontSize: 13, color: G_INK_55, textDecoration: "none" }}>Pricing</a>
            <a href="/guides" style={{ fontSize: 13, color: G_INDIGO, fontWeight: 500, textDecoration: "none" }}>Guides</a>
            <a href="/tool" style={{
              background: G_INDIGO, color: G_PAPER, padding: "9px 18px",
              borderRadius: 100, fontWeight: 600, fontSize: 13,
              textDecoration: "none",
            }}>Free check →</a>
          </div>
        )}
        {mobile && (
          <a href="/tool" style={{
            background: G_INDIGO, color: G_PAPER, padding: "7px 14px",
            borderRadius: 100, fontWeight: 600, fontSize: 12,
            textDecoration: "none",
          }}>Free check →</a>
        )}
      </nav>

      {/* HERO */}
      <section style={{
        position: "relative", overflow: "hidden",
        padding: mobile ? "40px 20px 32px" : "72px 64px 48px",
      }}>
        <TopoBackdrop />
        <div style={{
          position: "relative", zIndex: 1,
          maxWidth: mobile ? "100%" : 720,
          margin: mobile ? "0" : "0 auto", textAlign: mobile ? "left" : "center",
        }}>
          <div style={{
            display: "inline-flex", alignItems: "center", gap: 8,
            padding: "5px 12px", background: G_PAPER,
            border: `1px solid ${G_INK_08}`,
            borderRadius: 100, fontSize: 11, fontWeight: 600,
            letterSpacing: "0.14em", textTransform: "uppercase",
            color: G_APRICOT, marginBottom: 22,
          }}>
            <span style={{ width: 6, height: 6, borderRadius: "50%", background: G_APRICOT }}/>
            Free tax guides · 67 in total
          </div>
          <h1 style={{
            fontFamily: "Fraunces, serif", fontWeight: 400,
            fontSize: mobile ? 44 : 72, lineHeight: 0.98,
            letterSpacing: "-0.025em", color: G_INDIGO, margin: "0 0 22px",
            fontVariationSettings: "'opsz' 144, 'SOFT' 30",
          }}>
            Plain-English guides<br/>
            for <span style={{ fontStyle: "italic", color: G_APRICOT }}>every</span> side hustle.
          </h1>
          <p style={{
            fontFamily: "Inter, sans-serif", fontSize: mobile ? 15 : 17,
            lineHeight: 1.65, color: G_INK_70,
            maxWidth: mobile ? "100%" : 520,
            margin: mobile ? "0 0 28px" : "0 auto 32px",
          }}>
            7 interactive tools and 67 guides covering gig work, creator income, Etsy, e-commerce, freelancing, and state taxes. No jargon, no upsells.
          </p>

          {/* Search bar */}
          <div style={{
            position: "relative", maxWidth: mobile ? "100%" : 480,
            margin: mobile ? "0" : "0 auto",
          }}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none"
              style={{
                position: "absolute", left: 18, top: "50%",
                transform: "translateY(-50%)", pointerEvents: "none",
              }}>
              <circle cx="11" cy="11" r="7" stroke={G_INK_55} strokeWidth="2"/>
              <path d="M21 21l-4.3-4.3" stroke={G_INK_55} strokeWidth="2" strokeLinecap="round"/>
            </svg>
            <input
              type="text"
              placeholder="Search 74 guides & tools…"
              value={search}
              onChange={e => setSearch(e.target.value)}
              style={{
                width: "100%", padding: "14px 18px 14px 42px",
                fontFamily: "Inter, sans-serif", fontSize: 14.5,
                color: G_INDIGO, background: G_PAPER,
                border: `1px solid ${G_INK_12}`, borderRadius: 100,
                outline: "none", boxSizing: "border-box",
              }}
            />
            {search && (
              <button onClick={() => setSearch("")} style={{
                position: "absolute", right: 14, top: "50%",
                transform: "translateY(-50%)", background: "none",
                border: "none", color: G_INK_55, cursor: "pointer",
                fontSize: 18,
              }}>×</button>
            )}
          </div>
        </div>
      </section>

      {/* STICKY TABS */}
      <div style={{ padding: mobile ? "0 20px" : "0 64px" }}>
        <CategoryTabs active={active} setActive={setActive} mobile={mobile} />
      </div>

      {/* SECTIONS */}
      <div style={{
        padding: mobile ? "32px 20px 0" : "48px 64px 0",
      }}>
        {visibleSections.map(renderSection)}

        {/* CTA */}
        <section style={{
          background: G_INDIGO, color: G_PAPER,
          borderRadius: 22, padding: mobile ? "32px 24px" : "52px 56px",
          marginBottom: mobile ? 32 : 72, position: "relative", overflow: "hidden",
        }}>
          <div style={{
            position: "absolute", top: -100, right: -80,
            width: 320, height: 320, borderRadius: "50%",
            background: "radial-gradient(circle, rgba(232,148,100,0.2), transparent 65%)",
            pointerEvents: "none",
          }}/>
          <div style={{
            position: "relative", zIndex: 1,
            display: mobile ? "block" : "flex",
            justifyContent: "space-between", alignItems: "center", gap: 32,
          }}>
            <div style={{ maxWidth: mobile ? "100%" : 540 }}>
              <div style={{
                fontFamily: "Inter, sans-serif", fontSize: 11, fontWeight: 600,
                letterSpacing: "0.14em", textTransform: "uppercase",
                color: G_APRICOT, marginBottom: 10,
              }}>Not sure where to start?</div>
              <h2 style={{
                fontFamily: "Fraunces, serif", fontWeight: 400,
                fontSize: mobile ? 30 : 40, lineHeight: 1.05,
                letterSpacing: "-0.018em", margin: "0 0 12px",
                fontVariationSettings: "'opsz' 144, 'SOFT' 30",
              }}>
                Tell us your hustle.<br/>
                <span style={{ fontStyle: "italic", color: G_APRICOT }}>We'll figure out the rest.</span>
              </h2>
              <p style={{
                fontFamily: "Inter, sans-serif", fontSize: mobile ? 14 : 15,
                lineHeight: 1.6, color: "rgba(251,248,238,0.65)",
                margin: 0, marginBottom: mobile ? 22 : 0,
              }}>8 quick questions. Personalized breakdown — taxes, licenses, structure. Free, no account, 60 seconds.</p>
            </div>
            <a href="/tool" style={{
              background: G_APRICOT, color: G_INDIGO,
              padding: mobile ? "14px 26px" : "16px 32px",
              borderRadius: 100, fontWeight: 600, fontSize: 15,
              textDecoration: "none", whiteSpace: "nowrap",
              alignSelf: "center", flexShrink: 0,
              display: "inline-block",
            }}>Check my hustle →</a>
          </div>
        </section>
      </div>

      {/* FOOTER */}
      <footer style={{
        borderTop: `1px solid ${G_INK_08}`,
        padding: mobile ? "24px 20px 32px" : "32px 64px 40px",
        background: G_PAPER,
      }}>
        <div style={{
          display: "flex", justifyContent: "space-between",
          alignItems: mobile ? "flex-start" : "center",
          flexDirection: mobile ? "column" : "row", gap: 16,
        }}>
          <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
            <GLogo size={24} />
            <GWordmark size={14} />
          </div>
          <div style={{ fontSize: 11.5, color: G_INK_55, maxWidth: mobile ? "100%" : 420, lineHeight: 1.5 }}>
            General educational information only — not legal or tax advice. Consult a licensed CPA or attorney for your situation.
          </div>
          <div style={{ display: "flex", gap: 18 }}>
            <a href="/" style={{ fontSize: 12, color: G_INK_55, textDecoration: "none" }}>Home</a>
            <a href="/guides" style={{ fontSize: 12, color: G_INK_55, textDecoration: "none" }}>Guides</a>
            <a href="/tool" style={{ fontSize: 12, color: G_INK_55, textDecoration: "none" }}>Free check</a>
          </div>
        </div>
      </footer>
    </div>
  );
}

Object.assign(window, { GuidesPage });
