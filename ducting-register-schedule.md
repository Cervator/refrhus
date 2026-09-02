# Register schedule — working document

**This file is meant to be edited directly.** It is the per-register duct schedule for the proposed scheme, generated 2026-09-02 and then hand-tuned as the layout firms up. Sizes come from Eldr's equal-friction math at 0.08 in.wc/100 ft; the reasoning behind the airflow lives in [`ducting-scheme.md`](ducting-scheme.md).

Airflow is biased on purpose — **second floor ×1.35**, **basement ×0.70**, main floor unchanged — and computed on a **30°F supply-air rise**, the heat-pump figure. (A 50°F rise is a gas furnace and undersizes every heating-driven duct by 1.67×; see the side-car comment.)

---

## Schedule

| Level | Room | Room CFM | Supplies | CFM each | Duct | fpm | Returns | CFM each | Duct | fpm |
|---|---|---:|:-:|---:|:-:|---:|:-:|---:|:-:|---:|
| Basement | Future Media Room | 85 | 1 | 85 | 6″ | 435 | 1 | 85 | 6″ | 435 |
| Basement | Utility Room | 82 | 1 | 82 | 6″ | 415 | 1 | 82 | 6″ | 415 |
| Main | Kitchen | 251 | **1** ⚠ | 251 | 9″ | 569 | 1 | 251 | 9″ | 569 |
| Main | Main Bed | 227 | 2 | 113 | 7″ | 424 | 1 | 227 | 9″ | 513 |
| Main | Living room | 143 | 2 | 71 | 6″ | 363 | 1 | 143 | 7″ | 534 |
| Main | Kids Room | 64 | 1 | 64 | 6″ | 324 | 1 | 64 | 6″ | 324 |
| Main | Main Bath | 36 | 1 | 36 | 5″ | 263 | — | — | — | — |
| Main | Main Closet | 17 | 1 | 17 | 4″ | 191 | — | — | — | — |
| 2nd | Play Room | 115 | 1 | 115 | 7″ | 429 | 1 | 115 | 7″ | 429 |
| 2nd | Office | 113 | 2 | 56 | 5″ | 413 | 1 | 113 | 7″ | 421 |
| 2nd | Upper Bath | 28 | 1 | 28 | 4″ | 324 | — | — | — | — |
| 2nd | Upstairs Hallway | 20 | 1 | 20 | 4″ | 233 | — | — | — | — |

**⚠ The kitchen wants a second supply.** A single register at 251 CFM is roughly twice what a standard residential supply register handles comfortably — it will be noisy and it will throw a draft. Splitting it into two at ~125 CFM each puts both on **7″** and behaves far better. It is the one place the plan as sketched runs into a real limit.

Room-name mapping, since the model and conversation differ: the 2nd-floor "kids room" is **Play Room**; the main-floor "small kids room" is **Kids Room**; "bathroom" with supply only is **Main Bath**.

## Trunks and risers

| | CFM | Round | Rectangular |
|---|---:|---|---|
| Basement branch | 167 | 8″ | 6×8 |
| Main branch | 737 | 14″ | 9×16 |
| 2nd floor riser | 276 | 9″ | 6×12 |
| **Trunk at the unit** | **1,179** | **16″** | **9×24** or 10×20 |

## Returns are not a mirror of the supply side

Total return must equal total supply — that is mass balance and there is no way around it. But the return side is **a smaller number of larger openings**, not a duplicate schedule:

- **Fewer.** Rooms without their own return give their air up through door undercuts or transfer grilles. Here the Main Bath, Main Closet, Upper Bath and Upstairs Hallway all do.
- **Larger per CFM.** Returns are designed at lower velocity — roughly 400–600 fpm against a supply branch's 600–900 — so the same airflow wants a bigger duct.
- **Much larger at the grille.** A supply register is limited by throw and noise to roughly **100–150 CFM**. A return grille does not throw, so one can comfortably take **300–500 CFM**. That asymmetry is why one return can serve what needed two supplies.

### Balance per level

| Level | Total supply | Return registers | Together they must carry |
|---|---:|:-:|---:|
| Basement | 167 | 2 | 167 |
| Main | 737 | 4 | 737 |
| 2nd floor | 276 | 2 | 276 |

### Using return placement to balance the second floor

The idea of oversizing the Play Room's return to drag air across from the Office is a real technique, and the numbers work. The constraint is only that the floor's two returns sum to 276.

A worked split:

| | Supply | Return | Net |
|---|---:|---:|---|
| Office | 113 | 100 | 13 CFM leaves |
| Play Room | 115 | 176 | 61 CFM arrives |
| Upper Bath | 28 | — | 28 CFM migrates out |
| Upstairs Hallway | 20 | — | 20 CFM migrates out |
| | **276** | **276** | balanced |

That drives 61 CFM of cross-flow into the Play Room — the Office's surplus plus everything supplied to the bath and hallway. Shrink the Office return further to pull harder; the pair just has to keep summing to 276.

**The mechanism only works if the air has a path.** Door undercuts of ¾″ or transfer grilles between the office, bathroom and play room are what make this real rather than theoretical — without them the rooms just pressurise and the flow stops.

## Notes for editing

- **Splitting a room's supply does not change its total** — two registers at half the CFM each, and each duct drops about one nominal size.
- **Velocities above ~700 fpm on a branch start to be audible.** Everything in the table is currently well under.
- **Under 10 CFM, do not run a duct.** The remaining small rooms — closets, the chimney voids, the bar area, the stair void — are served by transfer.
- **Future work is out of scope here.** The garage mudroom conversion is deliberately absent; see the future-options section of `ducting-scheme.md`.
