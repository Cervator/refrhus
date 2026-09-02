# Register schedule — working document

**This file is meant to be edited directly.** It is the per-register duct schedule for the proposed scheme, generated 2026-09-02 and hand-tuned as the layout firms up. Sizes come from Eldr's equal-friction math at 0.08 in.wc/100 ft; the reasoning behind the airflow lives in [`ducting-scheme.md`](ducting-scheme.md).

Airflow is biased on purpose — **second floor ×1.35**, **basement ×0.70**, main floor unchanged — and computed on a **30°F supply-air rise**, the heat-pump figure. (A 50°F rise is a gas furnace and undersizes every heating-driven duct by 1.67×.)

**Every size below is per individual duct**, not per room. A room with two supplies gets two ducts of the size shown.

---

## Schedule

| Level | Room | Room CFM | Sup | CFM ea | Round | Rect | fpm | Ret | CFM ea | Round | Rect | fpm |
|---|---|---:|:-:|---:|:-:|:-:|---:|:-:|---:|:-:|:-:|---:|
| Basement | Future Media Room | 85 | 1 | 85 | 6″ | 3x10 | 435 | 1 | 85 | 6″ | 3x10 | 435 |
| Basement | Utility Room | 82 | 1 | 82 | 6″ | 3x10 | 415 | 1 | 82 | 6″ | 3x10 | 415 |
| Main | Kitchen | 251 | 2 | 126 | 7″ | 4x10 | 470 | 1 | 251 | 9″ | 5x14 | 569 |
| Main | Main Bed | 227 | 2 | 113 | 7″ | 4x10 | 424 | 1 | 227 | 9″ | 5x14 | 513 |
| Main | Living room | 143 | 2 | 71 | 6″ | 3x10 | 363 | 1 | 143 | 7″ | 4x12 | 534 |
| Main | Kids Room | 64 | 1 | 64 | 6″ | 3x8 | 324 | 1 | 64 | 6″ | 3x8 | 324 |
| Main | Main Bath | 36 | 1 | 36 | 5″ | 3x6 | 263 | — | — | — | — | — |
| Main | Main Closet | 17 | 1 | 17 | 4″ | 3x6 | 191 | — | — | — | — | — |
| 2nd | Play Room | 115 | 1 | 115 | 7″ | 4x10 | 429 | 1 | 115 | 7″ | 4x10 | 429 |
| 2nd | Office | 113 | 2 | 56 | 5″ | 3x8 | 413 | 1 | 113 | 7″ | 4x10 | 421 |
| 2nd | Upper Bath | 28 | 1 | 28 | 4″ | 3x6 | 324 | — | — | — | — | — |
| 2nd | Upstairs Hallway | 20 | 1 | 20 | 4″ | 3x6 | 233 | — | — | — | — | — |

Rectangular sizes are the shallowest option holding an **aspect ratio at or under 4:1**. Flatter than that costs friction and makes fittings awkward, so a 3x20 is not a real substitute for a 4x14 even though the areas are similar.

Room-name mapping, since the model and conversation differ: the 2nd-floor "kids room" is **Play Room**; the main-floor "small kids room" is **Kids Room**; "bathroom" with supply only is **Main Bath**.

---

## What a trunk actually is

The duct system is a hierarchy, and each level is sized by **the air passing through that particular segment** — not by anything upstream or downstream:

| Term | What it is | How it is sized |
|---|---|---|
| **Plenum** | The sheet-metal box bolted straight onto the air handler — one on the supply outlet, one on the return inlet | By the unit's opening, not by CFM. Its job is transition. |
| **Trunk** | The main duct leaving the plenum, carrying the bulk of the air | By total CFM passing through it |
| **Sub-trunk** | A trunk serving one zone or floor, fed from the main trunk or straight off the plenum | By that zone's total CFM |
| **Branch / runout** | The duct serving a single register | By that register's CFM |

**Anything serving more than one register is a trunk.** So yes — the large duct going up to the second floor is a trunk, and so is the return coming back down from it. Both carry 276 CFM and serve four registers before splitting.

**A trunk shrinks as branches leave it.** Two standard ways to handle that:

- **Reducing trunk** — step it down after each takeoff. Keeps velocity roughly constant, uses less metal, needs more fittings.
- **Extended plenum** — hold one size for most of the run and reduce once near the end. Simpler, slightly more material, and much the more common choice in residential work.

### The main trunk may not need to exist

| Segment | CFM | Round | Rectangular |
|---|---:|:-:|:-:|
| Basement sub-trunk | 167 | 8″ | 4x14 |
| Main sub-trunk | 737 | 14″ | 8x20 |
| 2nd floor sub-trunk | 276 | 9″ | 5x16 |
| *Main trunk at the unit* | *1,179* | *16″* | *10x22* |

That 16″ figure assumes **one** duct leaves the plenum and splits later. It does not have to be built that way, and in this basement it probably should not be — a 16″ round plus insulation hanging under joists at 84″ is a real intrusion.

**If the plenum carries takeoffs directly, the 16″ duct never exists.** Splitting the main floor into two sub-trunks makes the largest single duct in the house a **10″**:

| Off the plenum | Serves | CFM | Round |
|---|---|---:|:-:|
| Basement | Future Media, Utility | 167 | 8″ |
| Main — south | Main Bed 227, Living room 143 | 370 | **10″** |
| Main — north | Kitchen 251, Kids Room 64, Main Bath 36, Main Closet 17 | 368 | **10″** |
| 2nd floor riser | Office, Play Room, Upper Bath, Hallway | 276 | 9″ |

Four takeoffs, nothing above 10″, and the south/north split happens to follow the routing already planned — south through the stairs, north through the basement bathroom and west along the girder. The cost is a larger plenum with room for four connections, and enough spacing between them that they do not rob one another.

---

## Returns are not a mirror of the supply side

Total return must equal total supply — mass balance, no way around it. But the return side is **a smaller number of larger openings**:

- **Fewer.** Rooms without their own return give their air up through door undercuts or transfer grilles. Here that is Main Bath, Main Closet, Upper Bath and Upstairs Hallway.
- **Larger per CFM.** Returns are designed at lower velocity — roughly 400–600 fpm against a supply branch's 600–900 — so the same airflow wants a bigger duct.
- **Much larger at the grille.** A supply register is limited by throw and noise to roughly **100–150 CFM**. A return grille does not throw, so one can comfortably take **300–500 CFM**. That asymmetry is why one return serves what needed two supplies.

### Balance per level

| Level | Total supply | Return registers | Together they must carry |
|---|---:|:-:|---:|
| Basement | 167 | 2 | 167 |
| Main | 737 | 4 | 737 |
| 2nd floor | 276 | 2 | 276 |

### Using return placement to balance the second floor

Oversizing the Play Room's return to drag air across from the Office is a real technique, and the numbers work. The only constraint is that the floor's two returns sum to 276.

| | Supply | Return | Net |
|---|---:|---:|---|
| Office | 113 | 100 | 13 CFM leaves |
| Play Room | 115 | 176 | 61 CFM arrives |
| Upper Bath | 28 | — | 28 CFM migrates out |
| Upstairs Hallway | 20 | — | 20 CFM migrates out |
| | **276** | **276** | balanced |

That drives 61 CFM of cross-flow into the Play Room — the Office's surplus plus everything supplied to the bath and hallway. Shrink the Office return further to pull harder; the pair just has to keep summing to 276.

**The mechanism only works if the air has a path.** Door undercuts of ¾″ or transfer grilles between office, bathroom and play room are what make this real rather than theoretical — without them the rooms pressurise and the flow stops.

## Notes for editing

- **Splitting a room's supply does not change its total** — two registers at half the CFM each, and each duct drops about one nominal size.
- **Velocities above ~700 fpm on a branch start to be audible.** Everything here is well under.
- **Under 10 CFM, do not run a duct.** Closets, chimney voids, the bar area and the stair void are served by transfer.
- **Future work is out of scope here.** The garage mudroom conversion is deliberately absent; see the future-options section of `ducting-scheme.md`.
