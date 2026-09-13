# Refr Hus — HVAC design package

A 1950s house, measured by hand and rebuilt as a dimensioned model, with a Manual J load calculation and a duct design derived from it. **This package exists to be handed to an HVAC contractor** — the numbers below are open to challenge and the reasoning behind each one is written down.

Everything here is generated from or checked against the model in this repository. Where a figure is an assumption rather than a measurement, it says so.

---

## The numbers

| | |
|---|---:|
| Heating load, 70°F / 15°F design | **39,694 BTU/hr** |
| Cooling load, 75°F / 91°F design | **23,125 BTU/hr** (18,228 sensible) |
| Sensible heat ratio | 0.79 |
| Design supply airflow | **1,225 CFM** |
| Manual S on today's model | 3.5 tons |
| **Size to quote** | **4.0 tons** — see below |
| Existing unit | 4.0 tons |
| Duct, straight runs | 344 ft across 31 runs |
| Registers and grilles | 25 |
| Ductwork, installed, pre-incentive | $4,600–12,100 |

**Quote the 4 ton, not the 3.5.** The load calculation runs against geometry that is knowingly incomplete, and every gap in it points the same way: there is no grade line, so basement walls are classed below-grade over their full height; and a third of the second-floor ceiling surface is not drawn at all. Taking the professionals' measured basement U-value alone moves the load to ~3.8 tons. The sizing verdict on the existing unit has flipped between *oversized* and *well-matched* three times as corrections landed — **a verdict that flips with each correction is one to hold loosely**, and rounding up is the cheap direction to be wrong in.

**All pricing on this site is pre-incentive.** No rebate or tax credit is netted off anywhere, so the figures can be compared against a quote directly.

**Airflow is computed on a 30°F supply-air rise**, which is the heat-pump figure. A 50°F rise is a gas furnace and undersizes every heating-driven duct by 1.67× — this design was rebuilt once after that error, and it is the single most consequential number on the page.

## The question this package is asking

**One air handler, or two?** The current proposal is a second *internal* ducted handler — two units with ducts, rather than a head per room with none. That is a materially better idea than the knee-wall attic unit originally suggested, and this package argues with it on its merits rather than dismissing it.

**What two internal handlers genuinely buy:** real per-floor zoning, which a single unit cannot have here — neither the basement nor the second floor alone can be a hard zone without starving the blower. And much shorter runs, which attacks static pressure directly instead of arguing about it.

**What the single unit offers against that:** the same conditioned-duct benefit obtained a different way, through a three-level chase that **has to be built anyway** for the main floor — with half the equipment, one filter, and one maintenance schedule.

**The honest criterion is static pressure and nothing else.** If one unit can move 1,225 CFM through this layout at an acceptable external static pressure, it is the better buy. If it cannot, two internal handlers is the right answer — and the attic unit never was. That question is settled by fitting counts this model cannot supply, which is the one thing worth asking a contractor for.

Supporting detail: [the duct scheme](ducting-scheme.md) for the full argument, [the register schedule](ducting-register-schedule.md) for how a single plenum carrying four takeoffs keeps the largest duct in the house to 10″, and [the handover plan](ducting-handover-plan.md) for the second-floor riser.

---

## Documents

### The design

- **[Ducting scheme](ducting-scheme.md)** — the primer. Start here. Governing principle: supplies stay inside the thermal envelope, returns may cross buffer spaces.
- **[Register schedule](ducting-register-schedule.md)** — per-register airflow, duct size and face size, with the trunk hierarchy and the zoning reasoning.
- **[Parts list](ducting-parts-list.md)** — generated from the model: per-run section, material, length and bend count, plus material totals.
- **[Handover plan](ducting-handover-plan.md)** — modelling conventions, and what remains open.
- **[Model audit](ducting-model-audit.md)** — what is actually drawn, checked against the schedule.

### The house

- **[History](HISTORY.md)** — what was built when, and which walls are original.
- **[Basement structure](basement-structure.md)** · **[joists](basement-joists.md)** · **[post details](basement-post-details.html)**
- **[Measurement records](basement-measure-sheet.md)** · **[chimney](chimney-measure-sheet.md)**
- **[Load calculations](hvac/)** — the current Eldr run, the professional Manual J reports, and where the two disagree.

---

## What we are being upfront about

**Total effective length is not derivable from this model.** No elbows, tees or takeoffs are drawn, and the duct sizing uses a flat fitting factor rather than true equivalent lengths. Real fittings on a three-storey run add 50–150 ft of equivalent length.

This matters more than any other caveat, because **the second-unit question will be decided on static pressure.** Going in with an acknowledged gap is stronger than being caught with an optimistic number — and supplying the fitting counts is work a contractor is better placed to do anyway.

**The main-floor return path is the known weak point**, and it is not a grille problem. A single 4x8 running 30 ft through an inaccessible crawlspace carries the Main Bed, Kids Room and Utility Room returns between them. That reads as roughly four times the airflow it should take. It wants verifying on site, and it is the first thing worth quoting.

**Some loads are deliberately conservative.** Second-floor airflow is biased ×1.35 and the basement ×0.70, because the second floor is known to run hot and the basement holds temperature on its own. Those biases are stated, not buried. The second floor's ceiling area is also modelled at 984 ft² against a professional report's 1,547 — which makes our second-floor number the cautious one.

**This is not an ACCA-certified calculation.** It is a defensible Manual J estimate from a measured model, offered as a starting point for a conversation, not as a substitute for a professional report.

---

*The model, the engine and every document here are public. The load engine is [Eldr](https://github.com/SiliconSaga/eldr).*
