# Eldr — Heating Load (Phase 1, whole-house)

- Indoor / 99% outdoor design: **70°F / 15°F** (ΔT = 55°F)
- Infiltration: **0.50 ACH**
- Design temps from nearest station: **New York, NY** (lat/long from the model — approximate; set your ACCA station for accuracy)

| Component | Load (BTU/hr) |
|---|---:|
| basement_wall | 1,589 |
| ceiling | 1,465 |
| door | 2,908 |
| exterior_wall | 8,012 |
| floor | 762 |
| window | 2,413 |
| infiltration | 14,392 |
| **total** | **31,540** |

**Supply airflow:** 584 CFM (at 50°F supply-air rise)

_Phase 1 whole-house estimate. Not ACCA-certified. Room-by-room to follow._

## Eldr — Cooling Load (Manual J 1b, whole-house)

- Indoor / 1% outdoor design: **75°F / 91°F** (ΔT = 16°F) · SHGC **0.35** · 3 occupants

| Component | Load (BTU/hr) |
|---|---:|
| basement_wall | 0 |
| ceiling | 426 |
| door | 846 |
| exterior_wall | 2,331 |
| floor | 0 |
| internal | 1,890 |
| solar-NE | 472 |
| solar-NW | 120 |
| solar-SE | 999 |
| solar-SW | 1,300 |
| window | 702 |
| **sensible** | **9,086** |
| latent | 5,543 |
| **total** | **14,628** |

**Supply airflow:** 421 CFM

_Solar reads each window's exact bearing (grouped for display by nearest 8-point, e.g. `solar-SW`), from the model's compass `northDirection`._

## Manual S — Equipment Sizing

- Design load (heating): **31,540 BTU/hr = 2.6 tons**
- Recommended (smallest size that meets the load): **3.0 tons** (+14% vs load)
- Next size up: **3.5 tons** (+33% vs load)
- Existing unit: **4.0 tons** → +52% vs load → **oversized** ⚠
  - _short-cycling, poor humidity control, added wear_

_Demo estimate, not ACCA-certified. Sized on the larger of heating/cooling (here: heating)._

## Eldr — Per-Room Loads (Manual J 1c)

| Room | Heating (BTU/hr) | Cooling sens. (BTU/hr) | Design CFM |
|---|---:|---:|---:|
| Main Bed | 3,415 | 1,870 | 87 |
| Kitchen | 4,170 | 1,428 | 77 |
| Living room | 3,208 | 1,404 | 65 |
| Utility Room | 2,814 | 541 | 52 |
| Future Media Room | 2,510 | 580 | 46 |
| Play Room | 2,181 | 645 | 40 |
| Office | 2,049 | 770 | 38 |
| Kids Room | 1,266 | 766 | 35 |
| Main Bath | 739 | 340 | 16 |
| Upper Bath | 498 | 127 | 9 |
| Main Closet | 389 | 102 | 7 |
| Upstairs Hallway | 376 | 99 | 7 |
| Closet | 208 | 55 | 4 |
| Bathroom | 203 | 21 | 4 |
| Closet | 192 | 54 | 4 |
| **15 rooms** | | | **491** |

_Each room's load is from the exterior walls, windows, doors and ceiling/floor attributed to it, plus infiltration on its own volume; design CFM is the larger of heating/cooling airflow. Served rooms sum to **491 CFM** vs the whole-house **584 CFM** — the gap is space not carried here: floor area not yet drawn as rooms (halls, stairs, unfinished), plus tiny rooms below the 3-CFM run threshold. Draw more rooms and it closes._

## Manual D — Duct Sizing (round, equal-friction)

- Friction rate: **0.08 in.wc / 100 ft** (design rate — not derived from static pressure)
- Air handler: **Air Handler** — run length = unit → room (Manhattan + vertical) × fitting factor.

| Run | CFM | Exact dia | Duct | Velocity | Length | Drop |
|---|---:|---:|---:|---:|---:|---:|
| main trunk | 491 | 11.1″ | **12″** | 626 fpm | — | — |
| Kitchen | 77 | 5.5″ | **6″** | 393 fpm | 45 ft | 0.036″ |
| Main Bed | 87 | 5.8″ | **6″** | 441 fpm | 39 ft | 0.032″ |
| Living room | 65 | 5.2″ | **6″** | 331 fpm | 26 ft | 0.021″ |
| Main Closet | 7 | 2.2″ | **4″** | 83 fpm | 30 ft | 0.024″ |
| Kids Room | 35 | 4.1″ | **5″** | 260 fpm | 42 ft | 0.034″ |
| Main Bath | 16 | 3.0″ | **4″** | 180 fpm | 32 ft | 0.025″ |
| Office | 38 | 4.2″ | **5″** | 278 fpm | 48 ft | 0.039″ |
| Upper Bath | 9 | 2.5″ | **4″** | 106 fpm | 39 ft | 0.031″ |
| Closet | 4 | 1.8″ | **4″** | 44 fpm | 53 ft | 0.043″ |
| Play Room | 40 | 4.3″ | **5″** | 296 fpm | 41 ft | 0.033″ |
| Closet (2) | 4 | 1.7″ | **4″** | 41 fpm | 58 ft | 0.047″ |
| Upstairs Hallway | 7 | 2.2″ | **4″** | 80 fpm | 27 ft | 0.022″ |
| Utility Room | 52 | 4.8″ | **5″** | 382 fpm | 16 ft | 0.012″ |
| Future Media Room | 46 | 4.5″ | **5″** | 341 fpm | 15 ft | 0.012″ |
| Bathroom | 4 | 1.8″ | **4″** | 43 fpm | 15 ft | 0.012″ |

_Round duct, equal-friction, demo-grade. Total effective length uses a fitting fudge factor, not true fitting equivalent lengths; a full Manual D adds those and rectangular/oval sizing via equivalent diameter._
