# Duct model audit

Generated from the drawn objects in `sh3d-internals/Home.xml`, compared against [`ducting-register-schedule.md`](ducting-register-schedule.md). **71 objects** carry `Ducting:` in their name.

Cross-section is taken as the two smaller dimensions of each box — the longest is assumed to be the run direction. Capacity is the equal-friction figure at 0.08 in.wc/100 ft, so it is what the duct *could* carry, not what it does.

---

## The system as drawn

Two plenums on the air handler, feeding six trunk systems:

```
SUPPLY PLENUM  (22x12 section — 1,660 CFM capacity, comfortably over the 1,179 needed)
├── SE supply trunk 1 → 2 → 3 → 4      south, past the stairs, rising to Main and 2nd
├── SW supply trunk                    west of the stairs, open-air junction
└── North supply trunk 1 → 2 → 3 → 4   north, then the 3 registers near the unit

RETURN PLENUM  (12x12 section — 763 CFM capacity)
├── SE return trunk 1 → 2              two destinations
├── SW return trunk 1 → 2 → 3 → 4      living room + SW basement
└── North return trunk 1 → 2           main bedrooms + kitchen, via the crawlspace
```

Mudroom extensions are drawn and marked `FUTURE`; they are excluded from the load arithmetic below.

## Four things worth looking at

**1. The return plenum is undersized — the clearest problem in the model.**
Its 12x12 section carries **763 CFM**, and the whole house returns **1,179**. Supply and return must balance, so the return side has to move the same air the supply side does. The supply plenum was drawn generously at 22x12; the return needs comparable treatment — roughly **12x20** at the unit end.

**2. The north return trunk is about half the size it needs.**
At 8x8 it carries **259 CFM**, but it serves the main bedrooms (227) plus the kitchen (251) — **478 CFM**. It wants roughly 12x12, matching what the SE return trunks already are.

**3. The main-bedroom return branch is the known bottleneck, now visible in the model.**
Drawn at 7.5x4, it carries **91 CFM** against the 227 that room needs. This is the existing duct through the inaccessible crawlspace and it is not fixable by re-ducting. The plan of record is a **transfer grille above the bedroom door** first, with a second return via the SE corner only if that proves insufficient. Worth a note on the object so a future reader does not treat it as a sizing error to correct.

**4. The SE supply riser may be oversized, which is its own problem.**
SE supply trunks 3 and 4 are 12x12 — **763 CFM** of capacity. If they carry only the second floor's 228, that is **228 fpm**, very slow. Slow trunks are exactly what makes the near takeoff steal from the far one, and this one splits three ways at the top. If it is genuinely carrying main-floor branches on the way up, 12x12 is right; if it is a dedicated second-floor riser, it wants to be nearer 9–10″ equivalent.

## Where flat oval would help

Nine runs are drawn 4″ deep — shallow enough that the shape is doing real work, and exactly where flat oval beats a rectangular box on friction for the same depth:

`office east 4` · `little kids room 5` · `play room east 2` · `both main bedrooms` · `main bed room 1` · `main bed room 2` · `west kitchen and west basement` · `west living room 2` · `SW return branch`

## Modelling caveats

Sizes here are read off box dimensions, and the longest edge is *assumed* to be the run direction. Where a box is nearly cubic that assumption is weak. Objects do not all touch, and no elbows, tees or takeoffs are modelled — so run lengths are indicative and **total effective length is not derivable from this model**. That matters, because effective length is what a static-pressure argument turns on.


## Plenums

| Level | Object | Run | Section | Equiv | Capacity |
|---|---|---:|---|---:|---:|
| Basement | Return plenum | 120″ | 12.0x12.0 | 13.1″ | 763 |
| Basement | Supply plenum | 24″ | 22.0x12.0 | 17.6″ | 1660 |

## Trunks

| Level | Object | Run | Section | Equiv | Capacity |
|---|---|---:|---|---:|---:|
| Basement | North return trunk 1 | 64″ | 8.0x8.0 | 8.7″ | 259 |
| Basement | North return trunk 2 | 82″ | 8.0x8.0 | 8.7″ | 259 |
| Basement | North supply trunk 1 | 52″ | 12.0x11.5 | 12.8″ | 720 |
| Basement | North supply trunk 2 | 24″ | 8.0x8.0 | 8.7″ | 259 |
| Basement | North supply trunk 3 | 32″ | 8.0x8.0 | 8.7″ | 259 |
| Basement | North supply trunk 4 | 32″ | 10.0x6.0 | 8.4″ | 232 |
| Basement | SE return trunk 1 | 20″ | 12.0x11.6 | 12.9″ | 728 |
| Basement | SE return trunk 2 | 100″ | 12.0x12.0 | 13.1″ | 763 |
| Main | SE return trunk 2 | 100″ | 12.0x12.0 | 13.1″ | 763 |
| Basement | SE supply trunk 1 | 30″ | 16.0x12.0 | 15.1″ | 1111 |
| Basement | SE supply trunk 2 | 16″ | 16.0x12.0 | 15.1″ | 1111 |
| Basement | SE supply trunk 3 | 98″ | 12.0x12.0 | 13.1″ | 763 |
| Main | SE supply trunk 4 | 100″ | 12.0x12.0 | 13.1″ | 763 |
| Basement | SW return trunk 1 | 20″ | 9.0x9.0 | 9.8″ | 354 |
| Basement | SW return trunk 2 | 64″ | ⌀9.0 | 9.0″ | 279 |
| Basement | SW return trunk 3 | 36″ | ⌀9.0 | 9.0″ | 279 |
| Basement | SW return trunk 4 | 90″ | ⌀9.0 | 9.0″ | 279 |
| Basement | SW supply trunk | 31″ | 16.0x11.0 | 14.4″ | 985 |

## Branches

| Level | Object | Run | Section | Equiv | Capacity |
|---|---|---:|---|---:|---:|
| Crawlspac | FUTURE North return branch for mudroom *(future)* | 205″ | 6.0x6.0 | 6.6″ | 120 |
| Basement | North return branch for kitchen 1 | 98″ | 8.0x8.0 | 8.7″ | 259 |
| Basement | North return branch for kitchen 2 | 30″ | 8.0x8.0 | 8.7″ | 259 |
| Basement | North return branch for kitchen 3 | 66″ | 8.0x8.0 | 8.7″ | 259 |
| Basement | North return branch for kitchen 4 | 32″ | 14.5x6.0 | 10.0″ | 366 |
| Basement | North supply branch for living room east 1 | 58″ | 8.0x8.0 | 8.7″ | 259 |
| Basement | North supply branch for living room east 2 | 17″ | 6.6x4.0 | 5.6″ | 78 |
| Basement | North supply branch for main bathroom 1 | 28″ | 7.0x6.0 | 7.1″ | 147 |
| basement- | North supply branch for main bathroom 2 | 24″ | 8.8x5.9 | 7.8″ | 191 |
| Basement | North supply branch for orphaned kitchen register | 24″ | 9.2x9.0 | 10.0″ | 367 |
| Basement | SW return branch for living room and SW basement | 34″ | 12.0x4.0 | 7.3″ | 160 |
| Basement | FUTURE supply branch for mud room 1 *(future)* | 30″ | ⌀6.0 | 6.0″ | 95 |
| Basement | FUTURE supply branch for mud room 2 *(future)* | 30″ | ⌀6.0 | 6.0″ | 95 |
| Basement | FUTURE supply branch for mud room 3 *(future)* | 18″ | ⌀6.0 | 6.0″ | 95 |
| basement- | Return branch for both main bedrooms | 360″ | 7.5x4.0 | 5.9″ | 91 |
| basement- | Return branch for main bed room 1 | 40″ | 7.5x4.0 | 5.9″ | 91 |
| basement- | Return branch for main bed room 2 | 24″ | 10.0x4.0 | 6.7″ | 129 |
| Basement | Return branch for main floor kids room 1 | 40″ | 8.0x8.0 | 8.7″ | 259 |
| Main | Return branch for main floor kids room 2 | 20″ | 8.0x8.0 | 8.7″ | 259 |
| Basement | Supply branch for little kids room 1 | 36″ | ⌀8.0 | 8.0″ | 204 |
| Basement | Supply branch for little kids room 2 | 108″ | ⌀8.0 | 8.0″ | 204 |
| Basement | Supply branch for little kids room 3 | 12″ | 8.0x8.0 | 8.7″ | 259 |
| basement- | Supply branch for little kids room 4 | 57″ | 10.2x8.0 | 9.9″ | 358 |
| basement- | Supply branch for little kids room 5 | 24″ | 10.0x4.0 | 6.7″ | 129 |
| Basement | Supply branch for main bed north and basement east 1 | 36″ | ⌀8.0 | 8.0″ | 204 |
| Basement | Supply branch for main bed north and basement east 2 | 82″ | ⌀8.0 | 8.0″ | 204 |
| Basement | Supply branch for main bed north and basement east 3 | 40″ | 8.0x8.0 | 8.7″ | 259 |
| Basement | Supply branch for office east 1 | 36″ | ⌀8.0 | 8.0″ | 204 |
| Basement | Supply branch for office east 2 | 127″ | ⌀8.0 | 8.0″ | 204 |
| Basement | Supply branch for office east 3 | 12″ | 8.0x8.0 | 8.7″ | 259 |
| basement- | Supply branch for office east 4 | 124″ | 10.0x4.0 | 6.7″ | 129 |
| basement- | Supply branch for office east 4 | 40″ | 8.5x8.0 | 9.0″ | 280 |
| Basement | Supply branch for play room east 1 | 43″ | ⌀4.6 | 4.6″ | 46 |
| Basement | Supply branch for play room east 2 | 132″ | 10.0x4.0 | 6.7″ | 129 |
| Basement | Supply branch for west kitchen and west basement 1 | 56″ | ⌀8.0 | 8.0″ | 204 |
| Basement | Supply branch for west kitchen and west basement 2 | 120″ | ⌀8.0 | 8.0″ | 204 |
| Basement | Supply branch for west kitchen and west basement 3 | 76″ | ⌀8.0 | 8.0″ | 204 |
| Basement | Supply branch for west kitchen and west basement 4 | 32″ | 10.5x4.0 | 6.9″ | 137 |
| Basement | Supply branch for west living room 1 | 80″ | ⌀6.0 | 6.0″ | 95 |
| Basement | Supply branch for west living room 2 | 24″ | 10.5x4.0 | 6.9″ | 137 |
| Basement | Supply branch for west living room and future mud room 1 | 56″ | ⌀8.0 | 8.0″ | 204 |
| Basement | Supply branch for west living room and future mud room 2 | 144″ | ⌀8.0 | 8.0″ | 204 |
| Main | Tiny closet supply register for minimal airflow | 8″ | 4.0x4.0 | 4.4″ | 41 |
| 2nd floor | return branch for office 1 | 116″ | 10.0x6.0 | 8.4″ | 232 |
| 2nd floor | return branch for office 2 | 18″ | 10.0x6.0 | 8.4″ | 232 |
| 2nd floor | return branch for play room south 1 | 207″ | 10.0x6.0 | 8.4″ | 232 |
| 2nd floor | return branch for play room south 2 | 40″ | 10.0x6.0 | 8.4″ | 232 |
| Main | supply branch for main bed west | 94″ | 16.0x6.0 | 10.4″ | 411 |
| Main | supply branch for office west | 32″ | 8.0x8.0 | 8.7″ | 259 |
| 2nd floor | supply branch for play room south 1 | 92″ | 10.0x6.0 | 8.4″ | 232 |
| 2nd floor | supply branch for play room south 2 | 26″ | 10.0x6.0 | 8.4″ | 232 |
