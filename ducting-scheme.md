# The duct scheme — primer and design thinking

Where the ducting design stands as of 2026-09-02, why it is shaped this way, and what is still open. Written to be readable cold — by a contractor, by a future session, or by the owner in six months.

Companion documents: `ducting-design.md` (the as-built seed), `ducting-plan.md` (the earlier forward spec, including the maintenance-wall chase), `chimney-measure-sheet.md` (the chimney's geometry), and `hvac/README.md` (the load calculations and where they disagree with the professional Manual J).

---

## The scheme in one paragraph

**One air handler, relocated to the basement behind the bar, feeding all three floors through a single stacked utility cabinet built alongside the chimney.** The main floor is served by basement runs — south through the under-stair space, north through the basement bathroom and then west along the girder. The second floor is served by one supply and one return riser up the cabinet, with the supply branching short and central and the return splitting in the knee-wall attic to reach the far corners of both rooms.

The alternative on the table — a second air handler in the second-floor knee-wall attic — has been proposed by two separate contractors. This document exists partly to argue against it on evidence rather than preference.

---

## The governing principle

Everything below follows from one rule, and it is worth stating first because it decides every routing question that comes up:

> **Supplies stay inside the thermal envelope. Returns may cross buffer spaces.**

The reason is asymmetric cost. Air leaving the coil at 55°F and arriving at a register at 62°F has lost delivered capacity *and* the room feels it. Air leaving a room at 75°F and reaching the unit at 80°F only makes the unit work a little harder — the register still delivers 55°F. Losses on the supply side cost comfort and capacity; losses on the return side cost efficiency alone.

So where a duct has to cross a crawlspace, an attic, or any unconditioned run, it should be the return. That single rule is what makes the knee-wall attic acceptable for returns, the crawlspace acceptable for the kitchen return, and neither acceptable for supply.

**One caveat that comes with it:** a return leak is worse than a supply leak. A leaking supply wastes conditioned air outward; a leaking *return* pulls attic or crawlspace air inward — hot, humid, dusty, and capable of depressurising the house. Returns crossing buffer space get sealed with mastic, not tape.

---

## What each floor needs

Design airflow from Eldr's per-room Manual J, on geometry that is deliberately conservative (see the caveat below):

| Level | CFM | Dominated by |
|---|---:|---|
| Basement | 155 | Future Media 73, Utility 70 |
| **Main** | **524** | Main Bed 156, Kitchen 153, Living room 114 |
| 2nd floor | 205 | Office 87, Play Room 72 |
| **Total** | **884** | |

**The main floor is the load** — two and a half times the second floor. Which reframes the whole argument: the second floor is not the hard part *volumetrically*, it is the hard part *geometrically*. That distinction is the crux of the disagreement with the contractors, who are pricing the geometry and concluding the load can't be served.

**These numbers understate the second floor and should be presented that way.** Our ceiling area on that level is 984 ft² against the professional Manual J's 1,547 — sloped roof and knee-wall surfaces nobody has modelled yet. It cuts both ways: it makes *"the south side needs real supply"* stronger than shown, and *"one unit can do it"* easier than reality. Quote them as a floor, not an estimate: *on geometry that understates our second-floor ceiling by a third, the office still needs 87 CFM.* A number biased against your own case is much harder to argue with.

---

## The three-level utility cabinet

The cabinet is the whole argument in physical form. The standard, correct objection to retrofit second-floor ducting is that ducts in an unconditioned knee-wall attic lose 20–30%. A stacked cabinet running basement → main → second floor is a **conditioned chase**: it keeps the ducts inside the thermal envelope, which dissolves the objection rather than arguing with it.

It carries **only the second floor** — 205 CFM up, 205 CFM back. Not the whole 884. The main floor is fed from basement runs and never enters the cabinet. That is why a chase this modest is sufficient.

| Duct | CFM | Equivalent round | Rectangular options |
|---|---:|---|---|
| Supply riser | 205 | ~8″ | 6×10, 8×8, 4×14 |
| Return riser | 205 | ~8–10″ | 6×10, 9×9 |

Round is unnecessary anywhere inside the cabinet or under the stairs — it is all concealed, so rectangular wins on fit. Round is worth reserving for anywhere the duct is seen.

### Basement — the binding case

Just over **40″ of wall × ~16″ deep**, between the staircase door and the chimney, with the ceiling cut by the stair diagonal at 45° (36″ of headroom at the north end falling to 3″ at the south).

Two 15″ stud bays, and both are constrained:

- **North bay** — tall, but the chimney sits ~1″ behind the wall face and blocks roughly half its width.
- **South bay** — full width, but a triangle. Only about 9–10″ of its length has 10″ or more of clearance, so it is somewhere to **cross**, not to run.

**Arrangement:** two ducts through the north bay, one through the south — favouring whichever dimension is least constrained at each point. Two 9×9s will pass the tall space and one 9×9 the low space; 6×10 is the more conservative fit and still gives 8.4″ equivalent round at a quiet 492 fpm.

**Pair them by consequence, not by convenience:** the supply gets the better path. With an elevated horizontal air handler this falls out naturally — supply leaves at mid-height into the tall space, and the low triangle takes a duct running *under* the unit.

### Why a horizontal air handler, elevated

Not because a vertical one wouldn't fit behind the bar — it would. Because of where the connections land:

- A **vertical upflow** unit exits through the **top**, straight into the stair soffit where there is least room.
- A **horizontal** unit exits **sideways at mid-height**, supply one end and return the other, both where they can turn into the under-stair space.

Elevating it a foot or two adds duct routing space beneath, **condensate fall** — a horizontal drain pan needs slope to a drain, and elevation is the cheapest way to buy it — and side service access.

### Main floor

Open space; not a constraint. The cabinet here passes the two risers through and is the natural place to take **the office supply straight up through the floor**, keeping that room's supply out of the attic entirely. The office is 87 CFM — 42% of the second floor — so this solves the biggest room with the shortest and safest run.

### Second floor

Three shapes were considered:

| | Approach | Verdict |
|---|---|---|
| A | Straight cabinet wall from the chimney | **Rejected** — lands mid-latch on the attic access |
| B | **Diagonal from the chimney to the corner** | **Preferred** — puts the attic access *inside* the cabinet, fully contained |
| C | Ducts leaning south on the main level, exiting straight into the knee wall | Fallback — avoids the cabinet but puts duct in the attic |

B costs a little floor area and buys a clean elevation with one access point instead of two. It has a quiet second advantage: a diagonal face is a better place to turn a duct than a square corner, and a 45° transition carries roughly half the equivalent length of two 90s — which you are spending anyway at that point.

**The attic is used deliberately, for returns only.** One return riser comes up and splits in two, running to the far corners of both rooms; supply arrives short and central. That is the governing principle applied.

---

## Room-by-room notes

**The two old second-floor ducts are load-bearing, not supplementary.** Both measure about **3 × 10**, which is 5.74″ equivalent round and carries roughly **84 CFM** at design friction — a quiet 403 fpm.

| | Needs | One 3×10 gives |
|---|---:|---:|
| Play Room (west) | 72 | 84 ✓ |
| Office (east, by the window) | 83 | 84 ✓ |

Together **168 CFM — 83% of the floor's 202**. That flips the framing: the old ducts are the *base* and the cabinet riser is the *margin*, which is a cheaper build than the other way round. Worth confirming both are clear and intact end to end, especially the one currently dead-ending under the floor near the east window — at those numbers it is carrying real load, not a nice-to-have.

**Office** — primary supply up through the floor from the main-floor cabinet, keeping it out of the attic entirely. The old duct near the window adds perimeter supply, which is what keeps this floor from being purely central-supply.

**Kids room (west)** — the second old duct, also inside conditioned space.

**Kitchen** — 153 CFM, the second-largest room, and its northern half sits over the crawlspace rather than the basement. Solved by the same principle: a **return** runs from behind the basement bathroom straight through the plank atop the cinder block — where old drain-pipe holes can be widened — out to a register under the kitchen sink. Buffer space, but return only.

The existing supply register sits diagonally across the room from there, which is the best case rather than a compromise: **supply and return at diagonal corners** gives the longest mixing path across a room and is exactly what you would design if free to choose.

---

## Where the design is knowingly unconventional

**Central supply with perimeter return inverts normal practice.** Convention puts supply at the perimeter — under windows, against exterior walls, where the load is and where you want to break the cold-surface draft — and returns centrally. This scheme does the reverse on the second floor.

That is a real trade and it matters more in an old house with mixed glazing than in a tight new one. Two things make it acceptable:

1. The plan already includes **secondary perimeter supply** via the old window-adjacent duct in the office. The scheme is really *primary central + secondary perimeter*, which is a recognised retrofit compromise rather than a straight inversion.
2. There is **room to add supply later** — including a north run — if internal room balance turns out poor. The cabinet is sized with margin and the risers are not the constraint.

**The assumption to check is throw.** Whether a central register at 87 CFM actually reaches the office's far wall is Manual T territory. Rough answer: a typical floor register at that flow throws 8–12 ft against a room around 14–15 ft, so a central position needs ~7 ft. Plausible with margin — but it is a catalog lookup at register selection, not something to take on faith.

---

## The case against a second air handler

Presented in the order that a contractor will engage with it:

1. **The objection is usually right, and doesn't apply here.** Ducts in an unconditioned knee-wall attic genuinely lose 20–30%. That is the correct reason to distrust retrofit second-floor ducting. A conditioned three-level chase removes the premise instead of disputing the number.
2. **The load is modest.** 205 CFM to the second floor, against 524 to the main floor. The second floor is a geometry problem, not a capacity problem.
3. **Both supply and return reach it.** A second air handler quietly solves the *return* problem by putting the blower where the air is. A single unit needs both, or the floor pressurises and the air stops moving — which is the real reason "you can't duct a second floor" is so often true in retrofits. The cabinet has room for both, measured.
4. **The numbers are conservative.** See the ceiling-area caveat above.

**Where to be careful.** Eldr's Manual D uses a flat 1.5× fitting factor, not true fitting equivalent lengths. Real elbows, tees and boots on a three-storey run add 50–150 ft of equivalent length, so any static-pressure figure computed with the default is optimistic. Either raise the factor to something defensible (2.5–3) and say so, or count fittings by hand for the contested run. **Do not hand over a number that flatters the case on a modelling shortcut** — it is the one thing that would cost the credibility everything else earns.

Also worth noting: the current HVAC company specialises in insulation, so envelope work is likely already in their plan. That is an ally for this scheme rather than an obstacle — a tighter envelope lowers the load the ducts have to carry.

---

## Open questions

- **Which dimension constrains the basement ducts** — stud-bay width after the chimney, or the 16″ closet depth. Changes duct proportions, not position.
- **56.5″ or "just under 40″"** for the second-floor cabinet depth. They differ by 16″.
- **The two old ducts** — sizes, and whether the office one can be rescued from its dead end.
- **The knee-wall attic itself** — not yet entered. Estimated ~32″ deep from the 56.5″ reading.
- **The chimney's absolute position** carries a 2″ disagreement with its own tape chain; fine for layout, not for cutting.
- **The second floor's interior geometry** lags the east–west registration applied to the perimeter, so per-room figures on that level are stale until it catches up.

## Equipment

Sized on the larger of heating and cooling, which here is heating: **39,651 BTU/hr = 3.3 tons** on current geometry, rising to roughly **3.8 tons** once `basement_wall` takes the professionals' measured U-value. So the target is **3.5–4 tons**, and 4 is the safer read.

### Bosch IDS Ultra — the leading candidate

The cold-climate member of the IDS family, and the relevant one here: NJ's 99% design temperature is 15°F, and the Ultra delivers **100% heating capacity down to 5°F**, continuing to initiate heating to −13°F. DOE Cold Climate Heat Pump Challenge approved and ENERGY STAR V6.1 Cold Climate certified, tested at Oak Ridge. Uses **R-454B**, an A2L low-GWP refrigerant.

Two-part system: **BOVA** outdoor condenser, **BIVA** indoor air handler.

| Component | Model | W × H × D (in) |
|---|---|---|
| Indoor air handler, 4 ton | BIVA-48MCB-M19X | **22.0 × 54.5 × 24.0** |
| Indoor air handler, 5 ton | BIVA-60MCB-M19X | 22.0 × 54.5 × 24.0 |
| Outdoor condenser, 5 ton | BOVA-60MTB-M19E | 29.125 × 43.3125 × 29.125 |

The 4-ton and 5-ton air handlers share a cabinet. Verified from Bosch's own IDS Ultra spec sheet; the 3-ton system exists per Bosch's product literature but its dimensions are not on the sheet consulted.

**What it means for the basement.** In upflow the unit is 54.5″ tall on a 22 × 24 footprint. Converted to horizontal it lies down: roughly **22–24″ tall** (depending on which face it rests on) on a **54.5 × 24** footprint. Against the ~40″ of headroom at the tall end of the stair wedge, a horizontal unit leaves **16–18″ beneath it** for elevation and a duct — which is the configuration this plan assumes.

Behind the bar either orientation fits: the basement's 84″ to joist bottoms clears an upflow cabinet with 29.5″ to spare. The reason to prefer horizontal is not the unit's height but **where its connections land** — sideways at mid-height, matching the wedge, rather than out of the top into the stair soffit.

Electric heat kits (EHK-05B through EHK-20B, 5–20 kW) fit the cabinet without modification, which is the backup-heat path if the cold-climate performance ever needs supplementing.

### Orientation, generally

**Most residential air handlers are multi-position** — the same cabinet is sold for upflow, downflow, horizontal-left and horizontal-right. The Bosch BVA line ships configured for *upflow or horizontal-right* and is field-convertible to *horizontal-left or downflow*. The IDS Ultra air handler's drain pan is explicitly described as offering "flexibility for VT or HZ applications."

**The drain pan is the part that actually changes.** Condensate has to fall toward a drain in whatever orientation the coil ends up, so conversion is usually a matter of repositioning the pan and sometimes fitting a kit. Ask specifically whether the horizontal conversion needs a part, and confirm the drain fall — a horizontal pan with insufficient slope is a recurring source of overflow.

### The controls trade-off, which is a real decision

The requirement here is variable speed **and** open control rather than a locked ecosystem. Those pull against each other, and it is worth deciding deliberately:

| | Conventional 24V | Bosch communicating |
|---|---|---|
| Thermostat | any — ecobee, Home Assistant, anything | Bosch's own |
| Modulation | **staged**, not continuous | full compressor range |
| Openness | complete | closed |

The good news is that a Bosch variable-speed unit **can** run on a third-party 24V thermostat, because the modulation logic lives in the unit rather than the stat. The IDS Ultra's remote monitoring is documented as working "even without a communicating thermostat." A two-stage-capable smart thermostat is the practical minimum.

The cost is granularity. The Ultra's compressor modulates **35% to 138% in 1% increments**, and a conventional thermostat can only ask for stages, so most of that resolution goes unused. A communicating thermostat unlocks it and closes the system.

**One thing worth confirming before committing:** whether any local telemetry is available, or whether monitoring only goes through Bosch's EasyAir cloud app. Given the house already has an LGTM stack, a local data path would be worth more here than in a typical install.

## Future options, deliberately deferred

- **Garage mudroom conversion.** Split the return off the kitchen run at one end, bring supply across the *conditioned* basement, and enter at the opposite end. The governing principle holds, and supply and return land diagonally opposite — the arrangement you would choose freely. This is the case that shows the scheme extends rather than merely fits.
- **A north supply run** if room balance proves poor.
- **More second-floor supply** beyond the central pair and the two old ducts.
- **Manual T** — register throw and spread — which turns "should reach the far corner" into a calculation, and speaks the contractor's language most directly.
- **Grade line and second-floor ceiling geometry**, the two largest remaining Manual J gaps, both parked while the duct layout takes shape.
