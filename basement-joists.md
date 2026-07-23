# Basement joist bays — spacing reference

Derived from `sh3d-internals/Home.xml` (the `basement-main-transition` level), west→east.
Measured ~**5–7 ft off the south wall**; because some eastern joists **drift** (not
perfectly parallel, up to ~½″ over a few feet), these are the spacings *at that Y* —
other Y bands differ slightly. Relative spacing is confident to ~1/8″.

**On-center** = center-to-center to the previous member. **Clear** = gap between the
previous member's east face and this one's west face. Widths tag the member type:
**1.5″ = floor joist**, **3.5″ = main beam** (named `… - beam`), **6–8″ = a post / other
member** (`Box`) placed in the line. (The ~0.75″ center-vs-face offset cancels in every
difference, so it doesn't touch these numbers.)

| Member | Width | Center x (in) | On-center (in) | Clear (in) |
|---|---:|---:|---:|---:|
| joist-01 | 1.5 | 291.00 | — | — |
| joist-02 | 1.5 | 307.00 | 16.00 | 14.50 |
| Box | 6.0 | 314.37 | 7.37 | 3.62 |
| joist-03 | 1.5 | 323.12 | 8.75 | 5.00 |
| Box | 6.0 | 331.50 | 8.38 | 4.63 |
| joist-04 | 1.5 | 339.00 | 7.50 | 3.75 |
| joist-05 | 1.5 | 355.12 | 16.12 | 14.62 |
| joist-06 | 1.5 | 371.12 | 16.00 | 14.50 |
| joist-07 | 1.5 | 387.50 | 16.37 | 14.88 |
| joist-08 | 1.5 | 403.38 | 15.87 | 14.38 |
| joist-09 | 1.5 | 419.00 | 15.62 | 14.13 |
| joist-10 | 1.5 | 435.50 | 16.50 | 15.00 |
| joist-11 *(last regular, W)* | 1.5 | 451.25 | 15.75 | 14.25 |
| **joist-12 — beam** | 3.5 | 459.62 | 8.38 | 5.88 |
| joist-13 | 1.5 | 473.00 | 13.37 | 10.87 |
| joist-14 *(the extra)* | 1.5 | 485.75 | 12.75 | 11.25 |
| **joist-15 — beam** | 3.5 | 499.75 | 14.00 | 11.50 |
| joist-16 *(last regular, E)* | 1.5 | 515.25 | 15.50 | 13.00 |
| joist-17 | 1.5 | 530.12 | 14.88 | 13.38 |
| Box | 7.5 | 536.45 | 6.32 | 1.82 |
| joist-18 | 1.5 | 545.50 | 9.05 | 4.55 |
| joist-19 | 1.5 | 561.88 | 16.37 | 14.88 |
| Box | 7.5 | 570.19 | 8.32 | 3.82 |
| joist-20 | 1.5 | 578.25 | 8.06 | 3.56 |
| joist-21 | 1.5 | 593.88 | 15.62 | 14.13 |
| joist-22 | 1.5 | 610.00 | 16.12 | 14.63 |
| Box | 8.0 | 615.44 | 5.44 | 0.69 |
| joist-23 | 1.5 | 626.25 | 10.81 | 6.06 |
| joist-24 | 1.5 | 642.12 | 15.87 | 14.38 |
| Box | 8.0 | 647.14 | 5.01 | 0.26 |
| joist-25 | 1.5 | 658.25 | 11.11 | 6.36 |
| Box | 8.0 | 663.86 | 5.61 | 0.86 |
| joist-26 | 1.5 | 674.50 | 10.64 | 5.89 |

## Reading it

- **The regular field is ~16″ on-center** (joist-02→11 and 17→22 run 15.6–16.5″ o.c., ~14.5″ clear) — standard framing.
- **The stair zone** breaks it: the two **3.5″ main beams** (joist-12 and joist-15) flank a tighter pair of joists (13 + the extra 14).
- **Posts** — the 6–8″ `Box` members sit in the line, several mid-bay (their small "clear" values reflect a post landing right next to a joist, not a joist bay).
- **Joist field width:** west face of joist-01 (290.25″) to east face of joist-26 (675.25″) = **385.0″ = 32.08 ft** *(at the measured Y)*.

## Basement width — now realized in the model

With both cinderblock walls placed to the joist datum (east 1″ to raw cinder, west ~8″
through paneling), the model now carries the true E–W basement dimension:

| | inches | ft |
|---|---:|---:|
| joist field (face→face) | 385.0 | 32.08 |
| + east gap to raw cinder (confident) | 1.0 | |
| + west gap through paneling (~est.) | 8.0 | |
| **interior width** (block inner face → inner face) | **394.0** | **32.83** |
| + two 8″ cinderblock walls | 16.0 | |
| **exterior width** | **410.0** | **34.17** |

So the basement is ~**32.8 ft interior / 34.2 ft exterior** E–W — pinned on the east,
the only slack the ~8″ west estimate (confirm the raw west block face on the scan visit).
This is the datum the Main and 2nd floors now re-register to (via the E/W-align invariant
in `HISTORY.md`).
