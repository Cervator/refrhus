# Eldr — Manual J / S / D from a 3D model

Eldr reads a Sweet Home 3D house model and computes residential HVAC loads and duct
sizing along the ACCA chain — heating and cooling loads, equipment sizing, and duct
design. The model owns the geometry; a small "side-car" file owns the thermal
assumptions (insulation, setpoints, infiltration, soil temp, per-wall boundaries).
Edit the house, re-run, watch the numbers move.

These are **demo-grade estimates, not an ACCA-certified design** — the honesty
section marks exactly where the line is.

## The ACCA chain, implemented

| Step | Manual | What it answers |
|---|---|---|
| Loads | **Manual J** | winter heat loss / summer heat gain |
| Equipment | **Manual S** | what size unit the load calls for; is the existing one right |
| Distribution | **Manual D** | how big each supply duct needs to be |

## How detailed it gets

- **Solar by the exact degree** — every window's true compass facing (from the model's
  `northDirection`) sets its solar gain; SW/SE glass loads differently.
- **Climate from the model's coordinates** — nearest design-weather station, automatic.
- **The real footprint** — exterior walls follow the room-polygon outline, so a wall on
  an extension/wing is caught even off the bounding rectangle; unconditioned
  garage/crawlspace walls are excluded.
- **Below-grade follows Manual J** — basement walls + slab carry the full outdoor design
  ΔT for heating, with the soil path inside their effective U-value; in summer the soil is
  a heat sink, so they add no cooling load.
- **Buffer walls** — a wall to a garage/crawlspace is neither interior nor fully
  exterior; tagged `buffer`, it's loaded at **50% of the design
  ΔT**.
- **Per-room loads (Manual J 1c)** — each room's own walls/windows/doors/ceiling/floor.
- **Place the air handler** — each supply run gets a routed length; with the blower's
  static pressure, the friction rate is derived the ACCA way.

## Your house, by the numbers — whole-house loads (Manual J)

- Indoor / 99% outdoor design: **70°F / 15°F** (ΔT = 55°F)
- Infiltration: **0.68 ACH**
- Design temps from nearest station: **New York, NY** (lat/long from the model — approximate; set your ACCA station for accuracy)

| Component | Load (BTU/hr) |
|---|---:|
| basement_wall | 4,370 |
| buffer_floor | 5,765 |
| ceiling | 1,550 |
| door | 2,908 |
| exterior_wall | 8,012 |
| floor | 1,866 |
| window | 2,413 |
| infiltration | 11,079 |
| **total** | **37,962** |

**Supply airflow:** 703 CFM (at 50°F supply-air rise)

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

- Indoor / 1% outdoor design: **75°F / 91°F** (ΔT = 16°F) · SHGC **0.35** · 3 occupants

| Component | Load (BTU/hr) |
|---|---:|
| basement_wall | 0 |
| buffer_floor | 1,223 |
| ceiling | 3,284 |
| door | 846 |
| exterior_wall | 2,331 |
| floor | 0 |
| internal | 1,890 |
| solar-NE | 472 |
| solar-NW | 120 |
| solar-SE | 999 |
| solar-SW | 1,300 |
| window | 702 |
| **sensible** | **13,166** |
| latent | 4,405 |
| **total** | **17,571** |

**Supply airflow:** 610 CFM

**Sensible heat ratio:** 0.75 (sensible ÷ total) — how much of the job is temperature rather than moisture. A standard Manual J figure, directly comparable against any professional report, and an equipment-selection input: the lower it runs, the more of the load is dehumidification, which calls for a coil that stays wet rather than a bigger one.

_Those last three rows are not three more components. Every itemised row above them is sensible heat, and they sum to **sensible** — the heat that has to leave to hold the dry-bulb setpoint. **Latent** is a separate quantity: moisture, from the occupants and from the humidity the infiltrating air carries in. That is why it has no component breakdown — no wall, window or roof contributes to it. **Total** is simply the two added. Supply airflow is sized on **sensible** alone, not on the total, which is why the CFM does not come off the bottom line: air carries the sensible load by temperature difference, while the latent load leaves as condensate at the coil rather than by moving more air._

_Solar reads each window's exact bearing (grouped for display by nearest 8-point, e.g. `solar-SW`), from the model's compass `northDirection`._

## Manual S — Equipment Sizing

- Design load (heating): **37,962 BTU/hr = 3.2 tons**
- Recommended (smallest size that meets the load): **3.5 tons** (+11% vs load)
- Next size up: **4.0 tons** (+26% vs load)
- Existing unit: **4.0 tons** → +26% vs load → **oversized** ⚠
  - _short-cycling, poor humidity control, added wear_

_Demo estimate, not ACCA-certified. Sized on the larger of heating/cooling (here: heating)._

## Eldr — Per-Room Loads (Manual J 1c)

| Room | Heating (BTU/hr) | Cooling sens. (BTU/hr) | Design CFM |
|---|---:|---:|---:|
| Kitchen | 7,558 | 2,686 | 140 |
| Main Bed | 6,087 | 2,597 | 120 |
| Utility Room | 5,227 | 562 | 97 |
| Living room | 4,599 | 1,897 | 88 |
| Future Media Room | 4,693 | 596 | 87 |
| Office | 2,378 | 1,384 | 64 |
| Play Room | 2,460 | 1,166 | 54 |
| Kids Room | 1,440 | 903 | 42 |
| Main Bath | 817 | 407 | 19 |
| Upper Bath | 599 | 317 | 15 |
| Upstairs Hallway | 434 | 209 | 10 |
| Main Closet | 458 | 118 | 8 |
| Bathroom | 451 | 35 | 8 |
| Closet | 239 | 112 | 5 |
| Closet | 203 | 75 | 4 |
| Closet | 181 | 70 | 3 |
| **16 rooms** | | | **764** |

_Each room's load is from the exterior walls, windows, doors and ceiling/floor attributed to it, plus infiltration on its own volume; design CFM is the larger of heating/cooling airflow. Served rooms sum to **764 CFM** vs the whole-house **703 CFM** — the gap is space not carried here: floor area not yet drawn as rooms (halls, stairs, unfinished), plus tiny rooms below the 3-CFM run threshold. Draw more rooms and it closes._

## Manual D — Duct Sizing (round, equal-friction)

- Friction rate: **0.08 in.wc / 100 ft** (design rate — not derived from static pressure)
- Air handler: **Air Handler** — run length = unit → room (Manhattan + vertical) × fitting factor.

| Run | CFM | Exact dia | Duct | Velocity | Length | Drop |
|---|---:|---:|---:|---:|---:|---:|
| main trunk | 764 | 13.1″ | **14″** | 715 fpm | — | — |
| Kitchen | 140 | 6.9″ | **7″** | 524 fpm | 45 ft | 0.036″ |
| Main Bed | 120 | 6.5″ | **7″** | 450 fpm | 39 ft | 0.032″ |
| Living room | 88 | 5.8″ | **6″** | 447 fpm | 26 ft | 0.021″ |
| Main Closet | 8 | 2.4″ | **4″** | 97 fpm | 30 ft | 0.024″ |
| Kids Room | 42 | 4.4″ | **5″** | 307 fpm | 42 ft | 0.034″ |
| Main Bath | 19 | 3.2″ | **4″** | 216 fpm | 32 ft | 0.025″ |
| Closet | 3 | 1.7″ | **4″** | 38 fpm | 38 ft | 0.030″ |
| Office | 64 | 5.1″ | **6″** | 326 fpm | 48 ft | 0.039″ |
| Upper Bath | 15 | 2.9″ | **4″** | 168 fpm | 39 ft | 0.031″ |
| Closet (2) | 5 | 2.0″ | **4″** | 60 fpm | 53 ft | 0.043″ |
| Play Room | 54 | 4.8″ | **5″** | 396 fpm | 41 ft | 0.033″ |
| Closet (3) | 4 | 1.8″ | **4″** | 43 fpm | 58 ft | 0.047″ |
| Upstairs Hallway | 10 | 2.5″ | **4″** | 111 fpm | 27 ft | 0.022″ |
| Utility Room | 97 | 6.0″ | **7″** | 362 fpm | 16 ft | 0.012″ |
| Future Media Room | 87 | 5.8″ | **6″** | 443 fpm | 15 ft | 0.012″ |
| Bathroom | 8 | 2.4″ | **4″** | 96 fpm | 15 ft | 0.012″ |

_Round duct, equal-friction, demo-grade. Total effective length uses a fitting fudge factor, not true fitting equivalent lengths; a full Manual D adds those and rectangular/oval sizing via equivalent diameter._

## What's demo-grade today (the honest line)

- **Assemblies are assumptions, not a takeoff** — the side-car U-values, not measured construction. Real numbers move the loads.
- **Infiltration is an estimate** (0.68 ACH) — a blower-door test is the real input.
- **Design weather is nearest-station** (New York, NY), not the certified ASHRAE station for the address.
- **Below-grade resistance rides on the side-car** — the soil path lives in the declared `basement_wall` / `floor` U-value, and Eldr applies one such value per category no matter how deep the surface sits or how much of a basement wall stands above grade.
- **Storey heights are whatever the model says** — Sweet Home 3D gives each level a default height, and a level nobody re-measured looks identical to one that was; the *Level heights* table above shows what each level used and what volume it contributed.
- **Buffer-space temperatures are policy, not measurement** — an attic with no observed summer temperature gets a sol-air estimate (outdoor air plus a flat solar uplift, no roof geometry or ventilation rate); the *Buffer spaces* table above prints the factor and temperature each surface actually got.
- **149.5 ft² of conditioned floor has no level drawn beneath it** — modeled as `buffer_floor` over undrawn space. That is a gap in the drawing, not a measurement; draw those spaces and the assumption is replaced by geometry.
- **Duct run lengths use a fitting fudge factor**, not true fitting equivalent lengths; round duct only; no return-side sizing yet.
- **The envelope follows drawn rooms** — interior space not yet drawn as a room reads as outdoors and can over-count until it's drawn.

## What it would take to aspire to ACCA compliance

ACCA (Air Conditioning Contractors of America) runs a software-approval program against
their manuals. Moving from demo-grade toward that bar needs: the full Manual J 8th-ed
procedure (detailed fenestration, infiltration by tightness class, duct gains, internal-
gain schedules); certified ASHRAE design conditions for the address; real building data
(a construction takeoff + a blower-door test); a zone-aware bottom boundary and true
fitting equivalent lengths; then validation against ACCA's reference suite. The
architecture is already the right shape — geometry in the model, thermal in the side-car,
each Manual its own tested module — so the path is "add fidelity," not "rewrite."

## Near-term roadmap

- Zone-aware bottom boundary (basement slab vs. crawl vs. slab-on-grade extensions).
- True fitting equivalent lengths + return-duct sizing.
- Per-wall height/area splits (a wall that's part exterior, part buffer).
- Attic / knee-wall geometry; an interview step for the side-car; a Sweet Home 3D plugin.

*Eldr is read-only — it never modifies the house model. Estimates here are for demonstration and are not a substitute for a certified Manual J/S/D design.*