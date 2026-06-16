# Refrhus — construction history & model ground truth

The interpretation key for `Home.xml`. The model encodes a house that grew in
stages, so **the levels are deliberately different shapes** — apparent
"misalignment" between levels is usually real construction history, not a tracing
error. Read this before trusting (or "fixing") any cross-level overlay.

Captured from owner knowledge on 2026-06-13, alongside the first overlay
assessment (see `realms/realm-siliconsaga/docs/plans/2026-06-13-sh3d-overlay-tool-design.md`).

## Build sequence

1. **Original house** — roughly **800 sqft**. The current **Basement is the correct
   shape of this first edition**; the original main-floor exterior walls stood
   directly atop the **entire basement perimeter**.
2. **Garage added** — *not* original. Sits at an odd split-level height (~4 ft,
   roughly midway between basement floor and main floor). On the survey it is
   bundled with the house with **no wall drawn between garage and house**.
3. **Two main-floor extensions:**
   - **Kitchen extended north** (~8 ft up on the diagram), then a **deck** added
     north of that. The little wall **stump by "DINING AREA"** marks where the
     *original* exterior wall started, running east.
   - **Primary bedroom extended south.** The **original exterior wall crosses
     where "COVERED PORCH" begins** — i.e. the porch region is the southern
     extension.
4. **Upstairs finished** — awkwardly. The 2nd floor was expanded **south** over the
   extended bedroom (ending in a **gable with a window**, not the original sloped
   roof). It was **not** expanded north over the kitchen extension.

## Levels & elevations (from Home.xml)

| Level | elev | notes |
|---|---|---|
| Basement | 0 ft | Original ~800 sqft footprint. Background: floor plan (image 0). |
| Garage | 4 ft | Added later; split-level. Background: **survey** (image 1) — its own frame. |
| Crawlspace | 4 ft (~3–4 ft tall) | Under the kitchen north extension. Floor matches garage height. Partial, not a full level. No background. |
| basement-main-transition | 7 ft (~1 ft tall) | Thin split-level transition (stair landing). No background. |
| Main (FIRST FLOOR) | 8.4 ft | Original core + kitchen north extension + bedroom south extension. Background: floor plan (image 0). |
| 2nd floor | 16.8 ft | **Partial** floor. Original core hit only on **W & E** sides + south bedroom extension. North edge = knee-wall attic, inset ~3–4 ft **south** of the original exterior wall. Some N–S walls **angled** (roofline — not a true full floor). Background: floor plan (image 0). |

Heights are correct; the split-level/extension reality is already encoded in the
elevations. **The only thing needing work is in-plane (X/Y) frame consistency.**

## The "8 ft mystery" — resolved

Long misremembered as a level *height* confusion. It is actually the **kitchen's
~8 ft north extension**, in-plane:

- **Main** reaches ~8 ft north of the original exterior wall (the kitchen addition).
- The **2nd-floor** north wall ("BEDROOM 4" knee wall) sits ~**3–4 ft south** of
  that original exterior wall.
- So Main's north edge and the 2nd-floor north wall are separated by the extension
  plus the knee-wall inset — they are **not supposed to match.** (The first
  assessment measured ~243 cm / 8 ft between the Main and 2nd-floor wall-bbox north
  edges, while their south edges matched within 3 cm.)

## Alignment invariants (what *should* line up across levels)

Use these — and only these — to register levels into one plan frame:

- **East & West walls** align across Basement / Main / 2nd floor (the original
  perimeter). Exceptions: the **garage**, and the **south** (extended) part of the
  2nd floor.
- **Staircase** roughly aligns first ↔ second (scale / exact placement may be a
  little off — verify, don't assume).

**Do NOT** expect north/south walls to align — they diverge by era (kitchen +8 ft
north; bedroom/2nd-floor extension south; knee-wall inset).

## Two registration seams

1. **Floor-plan levels vs. each other** — Basement / Main / 2nd all trace the same
   not-to-scale floor-plan bitmap (image 0) at independently eyeballed origins.
   Align via the E/W walls + stairs.
2. **Survey frame vs. floor-plan frame** — the Garage uses the authoritative survey
   (image 1) in a separate coordinate frame; it does not currently agree with the
   floor-plan frame. The **survey is authoritative for the true exterior footprint**;
   the floor plan is explicitly *not to scale* (good for interior layout only).

## Background-image facts (for any registration math)

Placement, taken verbatim from `PlanComponent.paintBackgroundImage`:

- `plan = pixel · scale − origin`; image top-left sits at plan `(−xOrigin, −yOrigin)`.
- `scale = scaleDistance / dist(scaleStart, scaleEnd)` (cm per image-pixel).
- Plan **Y is down**; SH3D background images **cannot be rotated** (the two scale
  points only set a scalar scale) — any rotation must be baked into the image file.

| Image | file | size | cm/px | used by | origin(s) |
|---|---|---|---|---|---|
| Floor plan (not to scale) | `0` | 1940×1500 | 1.5646 | Basement, Main, 2nd | (−10.2, 788.7) / (574.3, 308.4) / (1902.2, 121.4) |
| Survey (authoritative) | `1` | 645×1020 | 3.9862 | Garage | (320.0, 1013.5) |
