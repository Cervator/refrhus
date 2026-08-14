# Eldr vs. the HVAC company Manual J (Progression A) — 2026-08

Cross-check of our model-based estimate (Eldr, read off the Sweet Home 3D model) against the HVAC company's Progression A (as-is), shown as a step-by-step progression of our own as we swap estimates for their measured inputs.

## Whole-house heating (BTU/hr), by component

| Component | Ours: as-is (estimates) | + their design temps & ACH | + our volume-bug fix | Their Progression A |
|---|---:|---:|---:|---:|
| Infiltration | 14,392 | 25,355 | 14,352 | 13,154 |
| Above-grade walls | 8,012 | 8,303 | 8,303 | 10,432 |
| Below-grade walls | 4,540 | 4,540 | 4,540 | 9,271 |
| Windows | 2,413 | 2,501 | 2,501 | 5,554 |
| Ceilings | 1,465 | 1,518 | 1,518 | 5,008 |
| Doors | 2,908 | 3,013 | 3,013 | 2,233 |
| Floors | 762 | 762 | 762 | 8,608 |
| **Heating total** | **34,491** | **45,993** | **34,989** | **54,260** |
| **Cooling total** | 14,628 | 17,550 | 13,903 | 28,485 |

Columns: (1) our defaults + auto lat/long design temps; (2) their ACCA design temps (70/13 heating, 75/89 cooling) + blower ACH 0.85; (3) plus our conditioned-volume fix; (4) their as-is Manual J.

## Reading it
- **Col 1→2** — their design temps + real ACH: infiltration jumps 14.4k → 25.4k; the conductive lines barely move (just a 2°-colder design day).
- **Col 2→3** — our fix: col 2 was counting garage/crawlspace/basement in the infiltration *volume* (~2× too big). Corrected to conditioned volume only, infiltration drops to 14.4k — landing on their 13.2k. (Col 2's total looked closer to theirs only by accident; the oversized volume was masking it.)
- **Col 3 vs their A** — infiltration now matched, so the whole remaining gap is conductive, in four nameable lines below.

## Where we differ (and why)
- **Below-grade walls (4.5k vs 9.3k) — we may be the more accurate one.** We couple basement walls + slab to ~50°F deep soil, not 13°F outdoor air. If their report loaded them at full outdoor design temp, that over-states basement loss.
- **Floors (0.8k vs 8.6k) — they're likely more accurate.** Their ~8.6k on ~978 sq ft reads like floor over unconditioned space (crawlspace/garage); we treat the lowest floor as slab-on-grade and under-count it (buffer-floor handling is a to-do).
- **Windows & ceilings (~6.5k of the gap) — assumptions to reconcile.** We default to double-pane (U-0.30) + R-38 ceiling; their numbers imply ~single-pane (U≈0.64) + ~R-17. Factual question about the house.
- **Cooling / hot attic (next-step model).** Our cooling is low mostly because we don't yet amplify the ceiling for a hot attic (120–140°F from roof solar → their ceiling cooling ~4,400 vs our ~370). Next step: a sol-air / attic-temperature input on the ceiling.

## Open items on our side
- Volume-bug fix: applied locally (`geometry.py`), 144 tests still pass; needs its own PR + a multi-level test.
- Buffer floors over crawlspace/garage: not fully split yet.
- Hot-attic cooling gain: sol-air / attic-temp model (per above).

---

## Email version

**Subject:** Manual J cross-check — our estimate converging on your Progression A

Hi JL,

We've been running an independent Manual J straight off a 3D model of the house, and I lined it up against your Progression A (as-is). Here's how our number moves as we swap our estimates for your measured inputs, one step at a time:

**Whole-house heating (BTU/hr), by component**

| Component | Ours: as-is | + your temps & ACH | + our volume fix | Your Progression A |
|---|---:|---:|---:|---:|
| Infiltration | 14,392 | 25,355 | 14,352 | 13,154 |
| Above-grade walls | 8,012 | 8,303 | 8,303 | 10,432 |
| Below-grade walls | 4,540 | 4,540 | 4,540 | 9,271 |
| Windows | 2,413 | 2,501 | 2,501 | 5,554 |
| Ceilings | 1,465 | 1,518 | 1,518 | 5,008 |
| Doors | 2,908 | 3,013 | 3,013 | 2,233 |
| Floors | 762 | 762 | 762 | 8,608 |
| **Heating total** | **34,491** | **45,993** | **34,989** | **54,260** |
| **Cooling total** | 14,628 | 17,550 | 13,903 | 28,485 |

Reading the columns:
- **Your design temps (70/13, 75/89) + blower ACH 0.85:** infiltration jumps to 25.4k; the conductive lines barely move.
- **Our volume fix:** our first pass counted the garage/crawlspace/basement in the infiltration *volume* — ~2× too big. Fixed to conditioned volume only, **infiltration drops to 14.4k, right on your 13.2k.** (The middle column's total only looked closer to yours because the oversized volume was masking it.)
- **Now that infiltration matches, the whole remaining gap is conductive** — four identifiable lines:

- **Below-grade walls (4.5k vs 9.3k) — we may be the more accurate one.** We couple the basement walls + slab to ~50°F deep soil, not 13°F outdoor air, since that's where the heat goes. If the report loaded them at full outdoor design temp, that over-states basement loss — worth a look.
- **Floors (0.8k vs 8.6k) — you're right, we under-count.** I pulled your construction-detail page: the 978 sq ft is a **714 sq ft basement slab** (U-0.020, ground-coupled → 807 BTU, matching us) plus **264 sq ft of *uninsulated* floor over the crawlspace** (U-0.521 → ~7,800 BTU). That exposed crawl floor is real and our stack model misses it entirely — we're adding it. (It's also a prime insulation target: insulating it kills most of that 7,800.)
- **Windows & ceilings — our defaults were too good.** Your detail page shows a **mix of single-pane (U-0.90), single+storm (0.57) and LowE double (0.53–0.55)** windows and an **R-11 to R-19 attic**, vs our uniform double-pane (U-0.30) + R-38. Adopting your real assemblies closes most of the rest.

**Cooling** stays lower on our side mostly because we don't yet model **hot-attic gain** — a summer attic hits 120–140°F from roof solar, so the ceiling should see a far larger ΔT than outdoor air (your ceiling cooling ~4,400 vs our ~370). That's our next modeling step.

Net: with your measured inputs + our volume fix, our heating differs from yours almost entirely on the basement treatment and the window/ceiling assemblies — all nameable. Confirm the window type, attic R, and how the below-grade walls were loaded, and I think we reconcile to within a few percent.

Best,
Rasmus
