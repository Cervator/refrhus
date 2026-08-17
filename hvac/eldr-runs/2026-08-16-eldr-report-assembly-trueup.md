# Eldr — Heating Load (Phase 1, whole-house)

- Indoor / 99% outdoor design: **70°F / 15°F** (ΔT = 55°F)
- Infiltration: **0.68 ACH**
- Design temps from nearest station: **New York, NY** (lat/long from the model — approximate; set your ACCA station for accuracy)

| Component | Load (BTU/hr) |
|---|---:|
| basement_wall | 4,370 |
| buffer_floor | 5,765 |
| ceiling | 1,550 |
| door | 2,908 |
| exterior_wall | 10,950 |
| floor | 746 |
| window | 4,730 |
| infiltration | 11,079 |
| **total** | **42,097** |

**Supply airflow:** 780 CFM (at 50°F supply-air rise)

_Phase 1 whole-house estimate. Not ACCA-certified. Room-by-room to follow._

## Assumptions behind these numbers

### Level heights

| Level | Height used | Source | Conditioned volume |
|---|---:|---|---:|
| Basement | 7.0 ft | model | 4,749 ft³ |
| Garage | 10.0 ft | model | 0 ft³ |
| Crawlspace | 4.0 ft | model | 0 ft³ |
| basement-main-transition | 1.0 ft | model | 0 ft³ |
| Main | 8.0 ft | model | 7,563 ft³ |
| 2nd floor | 8.0 ft | model | 4,145 ft³ |

_Total conditioned volume **16,457 ft³** — the infiltration basis. Set `levels.<name>.height_ft` to correct a height Sweet Home 3D defaulted. A level contributing 0 ft³ holds no conditioned rooms: a garage or crawlspace, a level given `role: ignore`, or a roomless one Eldr treated as joists/duct chase (which warns separately). Walls have nothing to do with it — a level with conditioned rooms drawn on it contributes whether or not any wall is drawn there._

### Buffer spaces

| Space | Winter factor (of 55°F ΔT) | Winter input | Summer factor (of 16°F ΔT) | Summer input |
|---|---:|---|---:|---|
| attic | 0.50 → 27.5°F | `vented: false` (built-in default) | 3.66 → 58.5°F | sol-air estimate 133.5°F attic air (outdoor 91°F + 42.5°F roof gain) — set `cooling.attic_temp_f` to replace it |
| crawlspace | 0.69 → 38.0°F | `winter_temp_f` 32.0°F (side-car) | 0.50 → 8.0°F | unvented fallback 0.50 (side-car) — winter shorthand, reused for summer |
| garage | 0.50 → 27.5°F | `vented: false` (built-in default) | 0.50 → 8.0°F | `vented: false` (built-in default) — winter shorthand, reused for summer |

_A surface facing a buffer space sees the ΔT shown, not the whole design ΔT; the arrow resolves the factor against that season's own design ΔT. A factor above 1 is not a bug: a sun-heated attic runs hotter than outdoor air, so the ceiling beneath it sees a larger ΔT than an exterior wall does._

### Schematic gaps

⚠ **149.5 ft² of conditioned floor has no level drawn beneath it** — modeled as `buffer_floor` over the undrawn space below (`crawlspace`, unless a level's `below_void` names another), at that space's own fraction of the design ΔT.

- Largest: Main Bed 110.1 ft², Living room 39.4 ft².
- Draw those spaces in Sweet Home 3D to replace the assumption with geometry.
- Undrawn rooms distort the WALLS too, not just the floor: a wall is on the envelope when a conditioned room sits on exactly one side of it, so floor area left undrawn on a level makes the walls bordering it read as facing outdoors. Every such wall is counted as exterior, which inflates the envelope wall area and the conduction above with it, until the rooms are drawn.

### Open questions

Neither errors nor warnings — assumptions in the numbers above that a careful reader should check against their own house before trusting the total.

- **Below-grade surfaces (`basement_wall`, `floor`) are loaded at the full outdoor design ΔT**, the way Manual J loads them. That assumes the U-value declared for them is a Manual J *effective* below-grade value — the assembly plus the resistance of the path through the soil out to grade. If a bare wall-assembly U was supplied instead, the soil is missing from the calculation entirely and these rows overstate the heat loss.
- **One U-value per category, whatever the depth.** In Manual J practice the effective below-grade U falls as the average depth below grade rises, because the soil path gets longer — the same construction is tabulated at several U-values for that reason. Eldr applies one `assemblies` number to every surface in the category, so a wall that is part shallow and part deep gets whichever single value was declared.
- **Below-grade surfaces contribute nothing to the cooling load**, because soil below the summer setpoint is a heat sink rather than a source. Some Manual J implementations do carry a small below-grade cooling load; against one of those, these rows will read low.
- **Eldr has no grade line.** Every wall on a basement level is classed `basement_wall` over its whole height. Manual J practice splits the same physical wall at grade: the buried portion gets the depth-dependent effective U above, and the portion standing proud of grade is an ordinary above-grade wall. If part of this model's basement wall is above grade, it is currently carrying the below-grade assembly. Eldr cannot make that split — the reader has to, either by drawing the wall as two segments or by declaring a `basement_wall` U that averages the two.
- **A wall's own height overrides its level's.** Wall AREA comes from each wall's drawn height, not from the storey height in the *Level heights* table above — that height sets the volume behind the infiltration term and nothing else. The two can disagree with nothing in the model looking out of place, so it is worth checking whenever a wall row reads larger or smaller than expected.

## Eldr — Cooling Load (Manual J 1b, whole-house)

- Indoor / 1% outdoor design: **75°F / 91°F** (ΔT = 16°F) · SHGC **0.35** · 5 occupants

| Component | Load (BTU/hr) |
|---|---:|
| basement_wall | 0 |
| buffer_floor | 1,223 |
| ceiling | 3,284 |
| door | 846 |
| exterior_wall | 3,185 |
| floor | 0 |
| internal | 2,350 |
| solar-NE | 472 |
| solar-NW | 120 |
| solar-SE | 999 |
| solar-SW | 1,300 |
| window | 1,376 |
| infiltration | 3,223 |
| **sensible** | **18,378** |
| latent | 4,805 |
| **total** | **23,183** |

**Supply airflow:** 851 CFM

**Sensible heat ratio:** 0.79 (sensible ÷ total) — how much of the job is temperature rather than moisture. A standard Manual J figure, directly comparable against any professional report, and an equipment-selection input: the lower it runs, the more of the load is dehumidification, which calls for a coil that stays wet rather than a bigger one.

_Those last three rows are not three more components. Every itemised row above them is sensible heat, and they sum to **sensible** — the heat that has to leave to hold the dry-bulb setpoint. **Latent** is a separate quantity: moisture, from the occupants and from the humidity the infiltrating air carries in. That is why it has no component breakdown — no wall, window or roof contributes to it. **Total** is simply the two added. Supply airflow is sized on **sensible** alone, not on the total, which is why the CFM does not come off the bottom line: air carries the sensible load by temperature difference, while the latent load leaves as condensate at the coil rather than by moving more air._

_Solar reads each window's exact bearing (grouped for display by nearest 8-point, e.g. `solar-SW`), from the model's compass `northDirection`._

## Manual S — Equipment Sizing

- Design load (heating): **42,097 BTU/hr = 3.5 tons**
- Recommended (smallest size that meets the load): **4.0 tons** (+14% vs load)
- Next size up: **4.5 tons** (+28% vs load)
- Existing unit: **4.0 tons** → +14% vs load → **well-matched**

_Demo estimate, not ACCA-certified. Sized on the larger of heating/cooling (here: heating)._

## Eldr — Per-Room Loads (Manual J 1c)

| Room | Heating (BTU/hr) | Cooling sens. (BTU/hr) | Design CFM |
|---|---:|---:|---:|
| Main Bed | 7,433 | 3,410 | 158 |
| Kitchen | 8,425 | 3,377 | 156 |
| Living room | 5,455 | 2,656 | 123 |
| Utility Room | 4,788 | 1,103 | 89 |
| Office | 2,823 | 1,889 | 87 |
| Future Media Room | 4,320 | 1,172 | 80 |
| Play Room | 2,750 | 1,568 | 73 |
| Kids Room | 2,013 | 1,206 | 56 |
| Main Bath | 1,123 | 555 | 26 |
| Upper Bath | 653 | 448 | 21 |
| Upstairs Hallway | 498 | 294 | 14 |
| Main Closet | 539 | 218 | 10 |
| Bathroom | 413 | 72 | 8 |
| Closet | 277 | 158 | 7 |
| Closet | 216 | 104 | 5 |
| Closet | 207 | 89 | 4 |
| **16 rooms** | | | **916** |

_Each room's load is from the exterior walls, windows, doors and ceiling/floor attributed to it, plus infiltration on its own volume; design CFM is the larger of heating/cooling airflow. Served rooms sum to **916 CFM** vs the whole-house **780 CFM** — the gap is space not carried here: floor area not yet drawn as rooms (halls, stairs, unfinished), plus tiny rooms below the 3-CFM run threshold. Draw more rooms and it closes._

## Manual D — Duct Sizing (round, equal-friction)

- Friction rate: **0.08 in.wc / 100 ft** (design rate — not derived from static pressure)
- Air handler: **Air Handler** — run length = unit → room (Manhattan + vertical) × fitting factor.

| Run | CFM | Exact dia | Duct | Velocity | Length | Drop |
|---|---:|---:|---:|---:|---:|---:|
| main trunk | 916 | 14.1″ | **16″** | 656 fpm | — | — |
| Kitchen | 156 | 7.2″ | **8″** | 448 fpm | 45 ft | 0.036″ |
| Main Bed | 158 | 7.2″ | **8″** | 452 fpm | 39 ft | 0.032″ |
| Living room | 123 | 6.6″ | **7″** | 460 fpm | 26 ft | 0.021″ |
| Main Closet | 10 | 2.6″ | **4″** | 115 fpm | 30 ft | 0.024″ |
| Kids Room | 56 | 4.9″ | **5″** | 410 fpm | 42 ft | 0.034″ |
| Main Bath | 26 | 3.6″ | **4″** | 294 fpm | 32 ft | 0.025″ |
| Closet | 5 | 1.9″ | **4″** | 55 fpm | 38 ft | 0.030″ |
| Office | 87 | 5.8″ | **6″** | 445 fpm | 48 ft | 0.039″ |
| Upper Bath | 21 | 3.4″ | **4″** | 238 fpm | 39 ft | 0.031″ |
| Closet (2) | 7 | 2.3″ | **4″** | 84 fpm | 53 ft | 0.043″ |
| Play Room | 73 | 5.4″ | **6″** | 370 fpm | 41 ft | 0.033″ |
| Closet (3) | 4 | 1.8″ | **4″** | 47 fpm | 58 ft | 0.047″ |
| Upstairs Hallway | 14 | 2.9″ | **4″** | 156 fpm | 27 ft | 0.022″ |
| Utility Room | 89 | 5.8″ | **6″** | 452 fpm | 16 ft | 0.012″ |
| Future Media Room | 80 | 5.6″ | **6″** | 407 fpm | 15 ft | 0.012″ |
| Bathroom | 8 | 2.3″ | **4″** | 88 fpm | 15 ft | 0.012″ |

_Round duct, equal-friction, demo-grade. Total effective length uses a fitting fudge factor, not true fitting equivalent lengths; a full Manual D adds those and rectangular/oval sizing via equivalent diameter._
