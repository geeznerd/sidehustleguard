/*!
 * SideHustleGuard — Expense Swiper shared dataset
 *
 * Single source of truth for the /expense-swiper engine + all niche
 * variants. Each HTML page loads this file once, then reads its dataset
 * by matching `window.location.pathname` against EXPENSE_SWIPER_PATHS.
 *
 * Adding a new niche:
 *   1. Add a new key to EXPENSE_SWIPER_DATA with 20-25 items.
 *   2. Add the same key to EXPENSE_SWIPER_LABELS (used in FAQ schema).
 *   3. Add a new `'/your-slug': 'yourkey'` entry to EXPENSE_SWIPER_PATHS.
 *   4. Copy expense-swiper.html → your-slug.html, swap the per-page meta.
 *
 * Item shape:
 *   {
 *     q:       'Expense name shown on the card',
 *     hint?:   'Optional sub-text (not rendered on card; for context)',
 *     cat:     'Category chip text — Gear / Personal / Vehicle / etc.',
 *     img?:    '/assets/images/expense-cards/file.jpeg' (optional),
 *     art?:    '<svg>...</svg>' inline (optional, legacy from Phase 14),
 *     verdict: 'yes' | 'no' | 'cond',
 *     explain: 'HTML-safe explanation shown on the results page',
 *     cite:    'IRS citation source — Pub 535 / IRC § 162 / etc.'
 *   }
 */
(function () {
  'use strict';

  window.EXPENSE_SWIPER_PATHS = {
    '/expense-swiper':            'delivery',
    '/etsy-deduction-swiper':     'etsy',
    '/airbnb-deduction-swiper':   'airbnb',
    '/onlyfans-deduction-swiper': 'onlyfans',
    '/tutor-deduction-swiper':    'tutor'
  };

  // Used in the dynamic FAQPage schema Qs: "Can I deduct X as a {label}?"
  window.EXPENSE_SWIPER_LABELS = {
    delivery: 'delivery driver',
    etsy:     'Etsy seller',
    airbnb:   'Airbnb host',
    onlyfans: 'content creator',
    tutor:    'online tutor'
  };

  window.EXPENSE_SWIPER_DATA = {

    // ──────────────────────────────────────────────────────────────
    // DELIVERY — 25 items. Curated set with images from Gemini.
    // ──────────────────────────────────────────────────────────────
    delivery: [
      { q:'Mileage between deliveries', cat:'Vehicle', img:'/assets/images/expense-cards/mileage.jpeg', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Mileage is the single biggest deduction for delivery drivers. Standard mileage is 70¢/mile in 2026 — track every business mile.', cite:'IRS Pub 463' },
      { q:'Insulated delivery bag or pizza warmer', cat:'Gear', img:'/assets/images/expense-cards/insulated-bag.jpeg', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Equipment specifically required for the job is "ordinary and necessary." 100% deductible in the year purchased.', cite:'IRS Pub 535' },
      { q:'Spotify Premium subscription', cat:'Personal', img:'/assets/images/expense-cards/spotify.jpeg', verdict:'no',
        explain:'<strong>Not deductible.</strong> Music streaming is personal entertainment, even if you only listen while driving for work.', cite:'IRS Pub 535' },
      { q:'Phone bill', cat:'Phone', img:'/assets/images/expense-cards/phone-bill.jpg', verdict:'cond',
        explain:'<strong>Partial — depends on use.</strong> Deduct the business-use portion. If you spend ~60% of phone time on delivery apps, deduct 60% of the bill.', cite:'IRS Pub 535' },
      { q:'Speeding ticket received on the job', cat:'Penalty', img:'/assets/images/expense-cards/speeding-ticket.jpg', verdict:'no',
        explain:'<strong>Never deductible.</strong> Fines and penalties paid to a government for any law violation are explicitly non-deductible — even when incurred during work.', cite:'IRC § 162(f)' },
      { q:'Tolls paid during a delivery', cat:'Vehicle', img:'/assets/images/expense-cards/tolls.jpg', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Tolls and parking fees paid during business driving are deductible <em>in addition to</em> standard mileage.', cite:'IRS Pub 463' },
      { q:'Gym membership', cat:'Personal', img:'/assets/images/expense-cards/gym.jpg', verdict:'no',
        explain:'<strong>Not deductible.</strong> Personal fitness expenses are not "ordinary and necessary" for delivery work — even if you genuinely use them for stamina.', cite:'IRS Pub 535' },
      { q:'Phone mount for your car dashboard', cat:'Gear', img:'/assets/images/expense-cards/phone-mount.jpg', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Equipment used directly for the work — especially when required by law (hands-free phone use). 100% deductible if exclusively for business.', cite:'IRS Pub 535' },
      { q:'Your own lunch during a 6-hour shift', cat:'Personal', img:'/assets/images/expense-cards/lunch.jpg', verdict:'no',
        explain:'<strong>Not deductible.</strong> Your own meals during a normal workday are personal. Only meals with clients or business contacts qualify (at 50%).', cite:'IRC § 274(n)' },
      { q:'Car wash during a delivery shift', cat:'Vehicle', img:'/assets/images/expense-cards/car-wash.jpg', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Reasonable car care directly tied to active business use of the vehicle. Track the receipts.', cite:'IRS Pub 463' },
      { q:'Reflective vest for late-night deliveries', cat:'Gear', img:'/assets/images/expense-cards/reflective-vest.jpeg', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Safety gear directly required for the work. 100% deductible.', cite:'IRS Pub 535' },
      { q:'Personal car payment', cat:'Vehicle', img:'/assets/images/expense-cards/car-payment.jpeg', verdict:'no',
        explain:'<strong>Not deductible (as such).</strong> Under standard mileage, depreciation is baked in. You <em>can</em> deduct the business-use portion of <strong>interest</strong> on the loan separately — but not the principal.', cite:'IRS Pub 463' },
      { q:'Hand sanitizer + disinfecting wipes for your car', cat:'Supplies', img:'/assets/images/expense-cards/hand-sanitizer.jpg', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Reasonable, ordinary supplies for the safe conduct of customer-facing delivery work.', cite:'IRS Pub 535' },
      { q:'New phone (full retail price)', cat:'Phone', img:'/assets/images/expense-cards/new-phone.jpeg', verdict:'cond',
        explain:'<strong>Partial — only the business-use percentage.</strong> If you use the phone 50% for delivery, deduct 50% of the cost (likely via Section 179 in year 1).', cite:'IRS Pub 535' },
      { q:'Coffee you bought for yourself mid-shift', cat:'Personal', img:'/assets/images/expense-cards/coffee.jpeg', verdict:'no',
        explain:'<strong>Not deductible.</strong> Your own food and drinks are personal, regardless of when you consume them.', cite:'IRC § 262' },
      { q:'Dashcam for your delivery vehicle', cat:'Gear', img:'/assets/images/expense-cards/dashcam.jpg', verdict:'cond',
        explain:'<strong>Partial — depends on use.</strong> If used only when delivering, deduct fully. If also recording during personal driving, prorate by business-use %.', cite:'IRS Pub 535' },
      { q:'AAA / roadside assistance subscription', cat:'Vehicle', img:'/assets/images/expense-cards/roadside-assistance.jpg', verdict:'cond',
        explain:'<strong>Method-dependent.</strong> Deductible via <strong>actual expense method</strong>. Under <strong>standard mileage</strong>, roadside assistance is baked in — don\'t double-deduct.', cite:'IRS Pub 463' },
      { q:'Parking ticket during a delivery', cat:'Penalty', img:'/assets/images/expense-cards/parking-ticket.jpg', verdict:'no',
        explain:'<strong>Never deductible.</strong> Same rule as a speeding ticket — government fines are non-deductible by statute.', cite:'IRC § 162(f)' },
      { q:'Reusable grocery totes for Instacart deliveries', cat:'Gear', img:'/assets/images/expense-cards/tote-bag.jpeg', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Job-specific equipment, 100% deductible. Buy in bulk and keep the receipts.', cite:'IRS Pub 535' },
      { q:'A second cell phone line just for the apps', cat:'Phone', img:'/assets/images/expense-cards/second-phone.jpeg', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> A dedicated business line with no personal use is 100% deductible.', cite:'IRS Pub 535' },
      { q:'Sunglasses for daytime driving', cat:'Personal', img:'/assets/images/expense-cards/sunglasses.jpg', verdict:'no',
        explain:'<strong>Not deductible.</strong> Sunglasses are personal even for full-time drivers — they have ordinary personal utility.', cite:'IRS Pub 535' },
      { q:'Online course: "How to maximize your DoorDash earnings"', cat:'Education', img:'/assets/images/expense-cards/online-course.jpeg', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Education that maintains or improves skills in your current trade is deductible.', cite:'IRS Pub 970' },
      { q:'Mileage-tracking app subscription (Stride, MileIQ)', cat:'Software', img:'/assets/images/expense-cards/mileage-app.jpeg', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Business software directly used for tax compliance and recordkeeping. 100% deductible.', cite:'IRS Pub 535' },
      { q:'Car insurance premium', cat:'Vehicle', img:'/assets/images/expense-cards/car-insurance.jpg', verdict:'cond',
        explain:'<strong>Method-dependent.</strong> Deductible via <strong>actual expense method</strong> (business-use %). Baked in under <strong>standard mileage</strong>.', cite:'IRS Pub 463' },
      { q:'A new winter coat', cat:'Personal', img:'/assets/images/expense-cards/winter-coat.jpeg', verdict:'no',
        explain:'<strong>Not deductible.</strong> Clothing that\'s also suitable for everyday wear is personal — even if you bought it specifically for the job.', cite:'IRS Pub 529' }
    ],

    // ──────────────────────────────────────────────────────────────
    // ETSY — 22 items. Shipping, supplies, studio, COGS.
    // ──────────────────────────────────────────────────────────────
    etsy: [
      { q:'Shipping labels (USPS, UPS, FedEx)', cat:'Supplies', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Postage and shipping costs are ordinary expenses for any seller. 100% deductible.', cite:'IRS Pub 535' },
      { q:'Bubble wrap and packing materials', cat:'Supplies', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Packing supplies directly tied to fulfilling orders. 100% deductible.', cite:'IRS Pub 535' },
      { q:'Photography backdrops + lightbox', cat:'Gear', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Equipment used for product photography that drives sales. Deduct via Section 179 in year 1 or depreciate.', cite:'IRS Pub 946' },
      { q:'Crafting tools (scissors, hot glue gun, pliers)', cat:'Gear', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Tools used to produce inventory. Small items can be expensed immediately under de minimis safe harbor.', cite:'IRS Pub 535' },
      { q:'Cricut blade replacements + materials', cat:'Supplies', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Consumable supplies for production. 100% deductible as ordinary expense.', cite:'IRS Pub 535' },
      { q:'Studio rent or coworking space', cat:'Workspace', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Dedicated business space rented outside the home is fully deductible — no business-use % calculation.', cite:'IRS Pub 535' },
      { q:'Etsy listing fees ($0.20 per listing)', cat:'Platform', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Platform fees of any kind are 100% deductible business expenses. Etsy provides annual reports.', cite:'IRS Pub 535' },
      { q:'Etsy transaction + payment processing fees', cat:'Platform', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> The 6.5% transaction fee and payment processing fees are deductible. Pull totals from Etsy\'s annual CSV export.', cite:'IRS Pub 535' },
      { q:'Raw materials (yarn, beads, fabric, wood)', cat:'COGS', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Cost of goods sold — materials that become part of your products. Tracked separately on Schedule C Part III.', cite:'IRS Pub 538' },
      { q:'Adobe Creative Cloud or Canva subscription', cat:'Software', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Business software used to design listings, marketing, and product graphics. 100% deductible if business-only.', cite:'IRS Pub 535' },
      { q:'Custom packaging (branded tissue, stickers, thank-you cards)', cat:'Supplies', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Branded packaging serves both fulfillment and marketing. Fully deductible.', cite:'IRS Pub 535' },
      { q:'Domain name + portfolio website hosting', cat:'Software', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Website costs that promote your shop are ordinary business expenses. Annual fees deductible in the year paid.', cite:'IRS Pub 535' },
      { q:'Coffee while crafting at home', cat:'Personal', verdict:'no',
        explain:'<strong>Not deductible.</strong> Your own food and drinks are personal, even when consumed while working.', cite:'IRC § 262' },
      { q:'Driving to the post office to ship orders', cat:'Vehicle', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Business mileage at 70¢/mile (2026 standard rate). Track every trip with a mileage app.', cite:'IRS Pub 463' },
      { q:'Storage unit for inventory', cat:'Workspace', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Storage exclusively used for business inventory is 100% deductible. Mixed-use storage requires proration.', cite:'IRS Pub 535' },
      { q:'Sales tax software (TaxJar, Avalara)', cat:'Software', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Business compliance software directly tied to the trade. Subscription fees fully deductible.', cite:'IRS Pub 535' },
      { q:'Etsy SEO course you bought', cat:'Education', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Education that improves skills in your current trade is deductible — but not courses to enter a new trade.', cite:'IRS Pub 970' },
      { q:'New iPhone for product photography', cat:'Phone', verdict:'cond',
        explain:'<strong>Partial — business-use percentage only.</strong> If you use the phone 50% for shop work (photos, customer messages), deduct 50%.', cite:'IRS Pub 535' },
      { q:'Home office (your craft room)', cat:'Home Office', verdict:'cond',
        explain:'<strong>Conditional — requires exclusive and regular use.</strong> The space must be used <em>only</em> for business, regularly. Simplified method: $5/sq ft up to 300 sq ft.', cite:'IRS Pub 587' },
      { q:'Costco membership for bulk supplies', cat:'Supplies', verdict:'cond',
        explain:'<strong>Partial — business-use percentage.</strong> If you use Costco 70% for inventory purchases and 30% personal, deduct 70% of the membership fee.', cite:'IRS Pub 535' },
      { q:'Gym membership "for creative inspiration"', cat:'Personal', verdict:'no',
        explain:'<strong>Not deductible.</strong> Personal fitness is personal regardless of rationalization. IRS has rejected this argument repeatedly.', cite:'IRS Pub 535' },
      { q:'Etsy gift cards you bought for yourself', cat:'Personal', verdict:'no',
        explain:'<strong>Not deductible.</strong> Personal purchases on your own platform aren\'t deductible business expenses.', cite:'IRC § 262' }
    ],

    // ──────────────────────────────────────────────────────────────
    // AIRBNB / STR — 22 items. Hospitality, property, cleaning.
    // ──────────────────────────────────────────────────────────────
    airbnb: [
      { q:'Welcome basket items (snacks, water bottles)', cat:'Hospitality', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Consumables provided to guests are ordinary hospitality expenses. 100% deductible.', cite:'IRS Pub 535' },
      { q:'Bulk coffee + condiment restock', cat:'Hospitality', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Supplies consumed by guests during their stay. Track via grocery receipts allocated to the rental.', cite:'IRS Pub 535' },
      { q:'Professional cleaning between guests', cat:'Cleaning', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Cleaning fees directly tied to rental turnovers. 100% deductible as ordinary operating expense.', cite:'IRS Pub 527' },
      { q:'Netflix/Hulu subscriptions for the guest TV', cat:'Hospitality', verdict:'cond',
        explain:'<strong>Conditional.</strong> Deductible only if the streaming account is dedicated to the rental property. Sharing with your personal account requires proration.', cite:'IRS Pub 535' },
      { q:'Patio furniture for the rental', cat:'Furniture', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Furniture for the rental is a depreciable asset (5-year property) or can be expensed under Section 179 in year 1.', cite:'IRS Pub 946' },
      { q:'New towels + linens for the property', cat:'Supplies', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Replacement linens are an ordinary operating expense — typically expensed immediately rather than depreciated.', cite:'IRS Pub 527' },
      { q:'Smart lock + keyless entry system', cat:'Equipment', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Equipment for guest access. Depreciate over 5 years or expense under Section 179.', cite:'IRS Pub 946' },
      { q:'Property management fees', cat:'Services', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Management fees are 100% deductible operating expenses. Common rate: 15-25% of rental income.', cite:'IRS Pub 527' },
      { q:'Mortgage interest on the rental property', cat:'Financing', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Mortgage interest on rental property is fully deductible on Schedule E. Form 1098 lists the amount.', cite:'IRS Pub 527' },
      { q:'Property insurance for the rental', cat:'Insurance', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Property/landlord insurance is 100% deductible. Personal homeowner\'s on your primary residence is not.', cite:'IRS Pub 527' },
      { q:'Utilities (electric, water, internet) during rentals', cat:'Operating', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Utilities for the rental property are fully deductible. Track via separate accounts when possible.', cite:'IRS Pub 527' },
      { q:'HOA fees on the rental', cat:'Operating', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Homeowner\'s association fees on a rental are fully deductible operating expenses.', cite:'IRS Pub 527' },
      { q:'Your personal vacation "to check on the property"', cat:'Personal', verdict:'cond',
        explain:'<strong>Conditional — primary purpose test.</strong> Only deductible if the trip\'s <em>primary purpose</em> is documented business activity. Casual check-ins don\'t qualify.', cite:'IRS Pub 463' },
      { q:'Furniture for your own bedroom in the same house', cat:'Personal', verdict:'no',
        explain:'<strong>Not deductible.</strong> Furniture in your personal space — even in a house that also has a rental — is personal property.', cite:'IRS Pub 527' },
      { q:'Property repairs (plumbing, broken AC)', cat:'Repairs', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Repairs that maintain the property are immediately deductible. Improvements (capital additions) must be depreciated.', cite:'IRS Pub 527' },
      { q:'Professional listing photos + virtual tour', cat:'Marketing', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Marketing costs that drive bookings are 100% deductible. Photography fees, virtual tours, copywriting all qualify.', cite:'IRS Pub 535' },
      { q:'Airbnb host service fees (3%)', cat:'Platform', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Platform fees are fully deductible. Airbnb provides 1099-K showing gross + fees separately.', cite:'IRS Pub 535' },
      { q:'Snow removal + lawn care', cat:'Operating', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Property maintenance services are ordinary operating expenses. Fully deductible.', cite:'IRS Pub 527' },
      { q:'Welcome cards + stationery', cat:'Marketing', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Small marketing/hospitality touches that drive reviews. Fully deductible.', cite:'IRS Pub 535' },
      { q:'Disposable amenities (toilet paper, soap, shampoo)', cat:'Supplies', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Consumables provided to guests. 100% deductible as ordinary operating expenses.', cite:'IRS Pub 535' },
      { q:'Your personal Netflix (also accessed at the rental)', cat:'Personal', verdict:'cond',
        explain:'<strong>Partial — proration required.</strong> A shared subscription requires allocating between personal and business use. Dedicated rental subscription is cleaner.', cite:'IRS Pub 535' },
      { q:'Speeding ticket on the way to the rental', cat:'Penalty', verdict:'no',
        explain:'<strong>Never deductible.</strong> Government fines and penalties are non-deductible by statute — even when incurred during business travel.', cite:'IRC § 162(f)' }
    ],

    // ──────────────────────────────────────────────────────────────
    // ONLYFANS / CREATOR — 22 items. Studio, wardrobe, production.
    // ──────────────────────────────────────────────────────────────
    onlyfans: [
      { q:'Ring light + softbox kit', cat:'Equipment', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Lighting equipment used for content production. Depreciable asset or expense under Section 179 in year 1.', cite:'IRS Pub 946' },
      { q:'Editing software (Adobe Premiere, Final Cut Pro)', cat:'Software', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Business software directly used to produce content. Subscription fees fully deductible annually.', cite:'IRS Pub 535' },
      { q:'Professional microphone + boom arm', cat:'Equipment', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Audio gear used exclusively for content. 100% deductible if business-only.', cite:'IRS Pub 535' },
      { q:'4K webcam for streaming', cat:'Equipment', verdict:'cond',
        explain:'<strong>Conditional — business-use %.</strong> If also used for personal video calls, prorate. If dedicated to content production, 100% deductible.', cite:'IRS Pub 535' },
      { q:'Specialized wardrobe (costumes, lingerie)', cat:'Wardrobe', verdict:'cond',
        explain:'<strong>Conditional — strict test.</strong> Deductible only if NOT suitable for everyday wear and required for content. The IRS is aggressive on this — keep clear records.', cite:'IRS Pub 529' },
      { q:'Makeup + skincare specifically for filming', cat:'Wardrobe', verdict:'cond',
        explain:'<strong>Conditional and risky.</strong> The IRS generally treats cosmetics as personal even when used on-camera. Stage-only specialty makeup is more defensible.', cite:'IRS Pub 529' },
      { q:'Gym membership for "physique work"', cat:'Personal', verdict:'no',
        explain:'<strong>Not deductible.</strong> Fitness expenses are personal even for fitness creators (per multiple tax court rulings). The IRS rejects this argument consistently.', cite:'IRS Pub 535' },
      { q:'Set decor + props for backdrops', cat:'Equipment', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Production props used exclusively for content are 100% deductible.', cite:'IRS Pub 535' },
      { q:'Spotify Premium for background music', cat:'Software', verdict:'cond',
        explain:'<strong>Partial — business-use %.</strong> Music used in content may be partially deductible. But mind royalty/licensing rules — most streaming music isn\'t licensed for commercial use.', cite:'IRS Pub 535' },
      { q:'Internet upgrade for streaming bandwidth', cat:'Operating', verdict:'cond',
        explain:'<strong>Partial — business-use %.</strong> If you upgrade specifically for streaming, deduct the incremental cost above what you\'d pay for personal use.', cite:'IRS Pub 535' },
      { q:'Dedicated home studio space', cat:'Home Office', verdict:'cond',
        explain:'<strong>Conditional — exclusive and regular use.</strong> The space must be used <em>only</em> for content production. Simplified method: $5/sq ft up to 300 sq ft.', cite:'IRS Pub 587' },
      { q:'Travel for a content shoot', cat:'Travel', verdict:'cond',
        explain:'<strong>Conditional — primary-purpose test.</strong> Travel deductible if the trip\'s primary purpose is producing content. Document business activity per day.', cite:'IRS Pub 463' },
      { q:'Subscription to competitor\'s content (research)', cat:'Research', verdict:'cond',
        explain:'<strong>Conditional — defensible but scrutinized.</strong> Research subscriptions can be deductible if the business purpose is documented (e.g., market analysis log).', cite:'IRS Pub 535' },
      { q:'Tax + legal + accounting fees', cat:'Services', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Professional fees for business compliance are 100% deductible operating expenses.', cite:'IRS Pub 535' },
      { q:'Lighting kit (LED panels, etc.)', cat:'Equipment', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Production equipment for content creation. Section 179 immediate expense or depreciate over 5 years.', cite:'IRS Pub 946' },
      { q:'Green screen + backdrop stand', cat:'Equipment', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Production equipment used exclusively for content. 100% deductible.', cite:'IRS Pub 535' },
      { q:'Personal therapist appointments', cat:'Personal', verdict:'no',
        explain:'<strong>Not deductible.</strong> Mental health care is personal medical expense regardless of how content-stress related. May be deductible as medical, not business.', cite:'IRS Pub 502' },
      { q:'Vacation that\'s also a "content trip"', cat:'Travel', verdict:'cond',
        explain:'<strong>Conditional — strict documentation.</strong> Only the business-purpose days are deductible. The IRS requires day-by-day logs of business vs personal activity.', cite:'IRS Pub 463' },
      { q:'New phone for shooting + posting content', cat:'Phone', verdict:'cond',
        explain:'<strong>Partial — business-use percentage.</strong> Track content-creation time vs personal. If 60% business, deduct 60% via Section 179 or depreciation.', cite:'IRS Pub 535' },
      { q:'Cosmetic surgery (for content)', cat:'Personal', verdict:'no',
        explain:'<strong>Not deductible.</strong> Cosmetic procedures are generally personal medical expenses, not business deductions — even if performed for on-camera appearance.', cite:'IRS Pub 502' },
      { q:'Hairstylist appointments for shoots', cat:'Wardrobe', verdict:'cond',
        explain:'<strong>Conditional — production-only.</strong> Styling exclusively for content shoots may be deductible. Routine grooming you\'d do anyway is personal.', cite:'IRS Pub 529' },
      { q:'Speeding ticket while driving to a shoot', cat:'Penalty', verdict:'no',
        explain:'<strong>Never deductible.</strong> Government fines and penalties are non-deductible by statute. Same rule applies regardless of trade.', cite:'IRC § 162(f)' }
    ],

    // ──────────────────────────────────────────────────────────────
    // TUTOR — 22 items. Software, materials, mileage, education.
    // ──────────────────────────────────────────────────────────────
    tutor: [
      { q:'Zoom Pro subscription', cat:'Software', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Business software directly used for tutoring sessions. 100% deductible if used only for work.', cite:'IRS Pub 535' },
      { q:'Digital clip art + worksheet downloads', cat:'Materials', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Teaching materials purchased for student lessons. Fully deductible as ordinary expenses.', cite:'IRS Pub 535' },
      { q:'Laminator + laminating sheets', cat:'Equipment', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Equipment used to produce teaching materials. Small items are expensed immediately under de minimis safe harbor.', cite:'IRS Pub 535' },
      { q:'iPad + Apple Pencil for tutoring', cat:'Equipment', verdict:'cond',
        explain:'<strong>Partial — business-use percentage.</strong> If used 70% for tutoring (annotations, screen-share), deduct 70% of cost. Document usage.', cite:'IRS Pub 535' },
      { q:'Educational software (Khan Academy Plus, etc.)', cat:'Software', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Subscriptions to educational platforms used in your teaching practice. 100% deductible.', cite:'IRS Pub 535' },
      { q:'Whiteboard + dry-erase markers', cat:'Supplies', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Teaching supplies used in sessions. Immediate expense as ordinary supplies.', cite:'IRS Pub 535' },
      { q:'Online course on teaching methods', cat:'Education', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Education that maintains or improves skills in your current trade is deductible. Not for courses to enter a new field.', cite:'IRS Pub 970' },
      { q:'Coffee bought before a tutoring session', cat:'Personal', verdict:'no',
        explain:'<strong>Not deductible.</strong> Your own food and drinks are personal, regardless of whether consumed before or during work.', cite:'IRC § 262' },
      { q:'Printer + ink for worksheets', cat:'Equipment', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Equipment used to produce teaching materials. Section 179 expense in year 1 or depreciate.', cite:'IRS Pub 946' },
      { q:'Subject-matter textbooks for lesson prep', cat:'Materials', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Reference materials used in your teaching practice. Fully deductible as ordinary business expense.', cite:'IRS Pub 535' },
      { q:'Background sign / banner for video tutoring', cat:'Marketing', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Professional appearance materials for client-facing video calls. 100% deductible.', cite:'IRS Pub 535' },
      { q:'Mileage to in-person tutoring sessions', cat:'Vehicle', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Business mileage at 70¢/mile (2026 standard rate). Track every business trip with a mileage app.', cite:'IRS Pub 463' },
      { q:'Tutoring platform fees (Wyzant, Outschool, VIPKid)', cat:'Platform', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Platform commissions and fees are 100% deductible business expenses.', cite:'IRS Pub 535' },
      { q:'Promotional flyers + business cards', cat:'Marketing', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Marketing materials that promote your tutoring services. Fully deductible.', cite:'IRS Pub 535' },
      { q:'Professional liability insurance', cat:'Insurance', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Business insurance directly tied to your trade is 100% deductible.', cite:'IRS Pub 535' },
      { q:'Office chair for long tutoring sessions', cat:'Equipment', verdict:'cond',
        explain:'<strong>Conditional — business use.</strong> If the chair is used exclusively in your business workspace, 100% deductible. Shared use requires proration.', cite:'IRS Pub 535' },
      { q:'Personal lunch on a tutoring day', cat:'Personal', verdict:'no',
        explain:'<strong>Not deductible.</strong> Your own meals during a workday are personal — same rule as any other trade.', cite:'IRC § 274(n)' },
      { q:'Background music subscription for sessions', cat:'Software', verdict:'cond',
        explain:'<strong>Conditional.</strong> Deductible if used exclusively for tutoring background. Most consumer streaming licenses don\'t permit commercial use — check terms.', cite:'IRS Pub 535' },
      { q:'Streaming subscription for "educational content"', cat:'Personal', verdict:'cond',
        explain:'<strong>Conditional and weak.</strong> Generic streaming consumed as personal entertainment isn\'t deductible. A specific subject-matter platform used in lessons is.', cite:'IRS Pub 535' },
      { q:'Gym membership "to stay sharp"', cat:'Personal', verdict:'no',
        explain:'<strong>Not deductible.</strong> Personal fitness expenses are not deductible regardless of profession. The IRS rejects this argument consistently.', cite:'IRS Pub 535' },
      { q:'Continuing education credits (CEU)', cat:'Education', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Required or recommended continuing education in your current field. 100% deductible.', cite:'IRS Pub 970' },
      { q:'Small snack rewards for student progress', cat:'Materials', verdict:'yes',
        explain:'<strong>Likely deductible.</strong> Small motivational rewards used in lessons. Document the business purpose (improving engagement / outcomes).', cite:'IRS Pub 535' }
    ]
  };

})();
