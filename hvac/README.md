# HVAC — load calculations, professional and our own

Two independent Manual J estimates of this house, kept side by side so they can be compared and so the drift between successive Eldr runs stays visible. [Eldr](https://github.com/SiliconSaga/eldr) is our own engine: it reads `../sh3d-internals/Home.xml` for geometry and `../eldr-sidecar.yaml` for the thermal assumptions geometry cannot hold.

The design intent, duct scheme and as-built notes live one level up in [`../ducting-plan.md`](../ducting-plan.md) and [`../ducting-design.md`](../ducting-design.md). This directory is only load calculations and their inputs.

## Why keep old runs

Because the totals lie. Between 2026-08-12 and 2026-08-14 the whole-house heating figure moved **31,540 → 31,757 BTU/hr — 0.7%** — while almost every component underneath it moved by thousands:

| Component | 2026-08-12 | 2026-08-14 | Δ |
|---|---:|---:|---:|
| basement_wall | 1,589 | 4,370 | **+2,781** |
| floor | 762 | 1,866 | **+1,104** |
| buffer_floor | — | 404 | **+404** |
| ceiling | 1,465 | 707 | **−758** |
| infiltration | 14,392 | 11,079 | **−3,313** |
| exterior_wall · window · door | 8,012 · 2,413 · 2,908 | unchanged | 0 |
| **total** | **31,540** | **31,757** | **+217** |

Four separate corrections that happened to very nearly cancel. Anyone comparing only the bottom lines would conclude nothing had changed. That is the argument for keeping every run rather than overwriting one file.

## The professional reports

`manual-j-professional/` — ACCA-approved Manual J by NJ Energy Auditor (JL), commissioned 2026-08. Three *progressions* modelling the same house at increasing tightness, which together form the do-the-envelope-work-first decision tool: each one shows what the equipment could shrink to if the preceding work is done.

| File | What it models | Heat | Cool |
|---|---|---:|---:|
| `2026-08-12-manual-j-progression-a-as-is.pdf` | As-is today | 54,260 | 28,485 |
| `2026-08-12-manual-j-progression-b-plus-insulation.pdf` | + insulation | — | — |
| `2026-08-12-manual-j-progression-c-plus-air-sealing.pdf` | + air sealing | — | — |
| `2026-08-12-3d-floorplan.pdf` | Their scan-derived floor plan | — | — |

**Read page 3 of any progression first.** The *Construction Details* table is where the real information is — every assembly with its area, U-value and HTM. Page 6 carries General / Internal / Infiltration / Ventilation.

### Two things in these PDFs that are easy to miss

**The measured blower door exists only in handwriting.** Progression C's Infiltration panel prints `Blower Door · 1,751 CFM50 · ACH 0.32`, but is annotated **"speculative"** — C models the *proposed post-air-sealing* state. The margin note beside it is the real measurement:

> **"At Audit BD was 3751! w/ACH 0.68"**

So the measured as-is figure is **3,751 CFM50 → ACH 0.68**, and that is what `../eldr-sidecar.yaml` now uses. Progression A's `ACH4 Heating 0.85 / Cooling 0.44` are **not** measurements — A's method line reads `Tightness: Loose`, an ACCA tightness-class estimate. Don't cite them as measured.

Worth recording: 3,751 CFM50 × 60 ÷ 16,457 ft³ = 13.7 ACH50, over an LBL N-factor of ~20 (two storeys, shielding class 4) = **0.68**. That volume is Eldr's independently computed conditioned volume, to the cubic foot.

**They load below-grade surfaces at the full outdoor ΔT.** Divide HTM by U on every below-grade row — 16.58/0.293, 16.82/0.297, 4.98/0.088, and the slab's 1.13/0.020 — and all four give **56.6**, against their design ΔT of 57 × a 0.995 elevation factor. The soil path lives inside the U-value, which is why U-0.293 is far below bare 8" masonry (~1.0 alone). That is standard Manual J, and finding it is what corrected Eldr, which had been applying an effective U *and* a ground ΔT — discounting twice. Their below-grade **cooling** HTMs do not divide out to a constant (5.73 / 9.19 / 7.73), so cooling below grade is not a single ΔT; their slab cooling HTM is 0.00, matching what Eldr does.

## Our runs

`eldr-runs/` — Eldr output, one dated pair per run plus the comparison write-up.

| File | Vintage |
|---|---|
| `2026-08-12-eldr-report-pre-level-stack.md` | Before the level-stack work. Ceilings and floors came from level *bounding boxes*; no buffer floors existed at all. |
| `2026-08-12-eldr-overview-pre-level-stack.md` | Narrative form of the same run. |
| `2026-08-12-eldr-vs-manualj-comparison.md` | First cross-check against Progression A, with an email draft to JL. **Its below-grade-wall line of 4,540 BTU/hr is stale** — the engine has produced 1,589 since before that document was written, and 4,370 since the below-grade fix. |
| `2026-08-14-eldr-report-level-stack.md` | Resolved floors/ceilings, per-space buffer policies, hot-attic cooling, below-grade at full ΔT, measured ACH. Carries an *Assumptions behind these numbers* section that did not exist before. |
| `2026-08-14-eldr-overview-level-stack.md` | Narrative form. |

Regenerate with the engine checked out beside this repo:

```bash
PYTHONPATH=components/eldr components/eldr/.venv/bin/python -m eldr.cli \
  hoards/refrhus/Refrhus.sh3d hoards/refrhus/eldr-sidecar.yaml
```

Add `--overview` for the narrative form, `--json` for structured output, `--walls` to list wall ids for tagging.

## Where the two still disagree, and why

Same house, two engines, and the gaps are now nameable rather than mysterious:

| Line | Eldr | Theirs | Status |
|---|---:|---:|---|
| Floor **area** | 971.9 ft² | 978 ft² | ✅ within 0.6% |
| Floors load | 1,866 + 404 | 8,608 | `assemblies.buffer_floor` is unset, so ~293 ft² of framed floor borrows the slab's U-0.05 where they measured **U-0.521** |
| Ceilings | 707 | 5,008 | Our `ceiling: 0.026` is R-38; their construction page says **R-11 / R-13 / R-19**. Their ceiling *area* is 1,547 ft² against our 984 — probably sloped and knee-wall surfaces counted differently, and unresolved |
| Below-grade walls | 4,370 | 9,271 | Convention now matches. Remaining gap is our `basement_wall: 0.07`, below even their *finished* 0.088 and far below their bare 0.293 |
| Basement wall **area** | ~1,135 ft² | 774 ft² | They split each wall at the grade line; Eldr has no grade-line concept and classes the whole wall below-grade |
| Occupants | 3 | 5 | Side-car input |
| SHR | 0.70 | 0.90 | Our assumed 30-grain humidity difference vs their station's 27.805 |

The pattern: **the geometry agrees and the assemblies do not.** Every remaining gap is a side-car number nobody has measured yet, or the grade-line split Eldr cannot model.

## The measurement that would settle the most

Interior surface temperature gives heat flux directly, because the interior air film is a known resistance:

```
q = (T_air − T_surface) / 0.68        BTU/hr·ft²
U_eff = q / (T_indoor − T_outdoor)
```

Taken on the **bare cinder block** and on the **R-11 panelled** section, that measures the two assemblies currently in dispute — their 0.293 and 0.088 against our 0.07 — without arguing about convention.

Take a **vertical profile, not a single reading**: below grade the soil path lengthens with depth, so the wall runs coldest near the grade line and warmest at the slab. That gradient *is* the depth-dependent U that Manual J tabulates, measured on this house instead of read from a table. Every foot from slab to ceiling, on both wall types, and the slab too.

Conditions matter more than instrument quality — a cold stable day, indoor temperature held for several hours, no sun on the wall, nothing blowing across it. Measure air temperature 2–3 ft off the wall and log the outdoor temperature at the same moment. An IR thermometer is fine on block and painted wood (emissivity ~0.9); a taped-on thermistor under a scrap of insulation is better. The weak link is that 0.68 film resistance, so treat results as ±10% — ample to separate 0.07 from 0.29.
