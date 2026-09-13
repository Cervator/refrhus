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
| Manual S recommendation | **3.5 tons** |
| Existing unit | 4.0 tons — **oversized by 21%** |
| Duct, straight runs | 344 ft across 31 runs |
| Registers and grilles | 25 |

**Airflow is computed on a 30°F supply-air rise**, which is the heat-pump figure. A 50°F rise is a gas furnace and undersizes every heating-driven duct by 1.67× — this design was rebuilt once after that error, and it is the single most consequential number on the page.

## The question this package is asking

Two contractors have proposed **a second air handler for the second floor**. This package is the argument for doing it with **one**, made in the same units they would use.

The case rests on three things, each with its own document:

1. **The load is 3.3 tons and the existing unit is already 4.0.** A second handler adds capacity to a house that is oversized today. See the Manual S section of any [run archive](hvac/).
2. **A single plenum can carry four takeoffs**, which keeps the largest duct in the house to 10″ rather than the 16″ a single main trunk would need. See [the register schedule](ducting-register-schedule.md).
3. **The second-floor riser is sized and routed**, through a known chase, with the reducing schedule worked out. See [the handover plan](ducting-handover-plan.md).

If that case fails, it will fail on **static pressure** — see the honesty section below.

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
- **[Load-calculation runs](hvac/)** — every Eldr run, archived with what changed.

---

## What we are being upfront about

**Total effective length is not derivable from this model.** No elbows, tees or takeoffs are drawn, and the duct sizing uses a flat fitting factor rather than true equivalent lengths. Real fittings on a three-storey run add 50–150 ft of equivalent length.

This matters more than any other caveat, because **the second-unit question will be decided on static pressure.** Going in with an acknowledged gap is stronger than being caught with an optimistic number — and supplying the fitting counts is work a contractor is better placed to do anyway.

**The main-floor return path is the known weak point**, and it is not a grille problem. A single 4x8 running 30 ft through an inaccessible crawlspace carries the Main Bed, Kids Room and Utility Room returns between them. That reads as roughly four times the airflow it should take. It wants verifying on site, and it is the first thing worth quoting.

**Some loads are deliberately conservative.** Second-floor airflow is biased ×1.35 and the basement ×0.70, because the second floor is known to run hot and the basement holds temperature on its own. Those biases are stated, not buried. The second floor's ceiling area is also modelled at 984 ft² against a professional report's 1,547 — which makes our second-floor number the cautious one.

**This is not an ACCA-certified calculation.** It is a defensible Manual J estimate from a measured model, offered as a starting point for a conversation, not as a substitute for a professional report.

---

*The model, the engine and every document here are public. The load engine is [Eldr](https://github.com/SiliconSaga/eldr).*
