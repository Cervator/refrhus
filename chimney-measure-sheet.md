# Chimney measuring sheet — all three levels

The chimney is the first piece of the duct plan, and it earns that place twice over: it defines what the utility chase has to route *around*, and because it pierces every level it is a **cross-level datum** — the same trick as the basement-to-main through-holes, already built into the house.

That second point is worth being deliberate about. Measure the chimney's position against something local on each level and the three levels register to each other for free, in both axes. It is the cheapest registration available and it needs no new holes.

---

## What the model currently believes

Treat all of this as unverified. The chimney has never been measured.

| Level | Object | Position | Size | Notes |
|---|---|---|---|---|
| Basement | `Box` | x 550.30, y 380.21 | 36 × 24 | the fat lower section |
| Basement | `Chimney Void` room | x 500.31–512.50, y 395.16–416.34 | 12.2 × 21.2 | **does not overlap the box** |
| Main | `Chimney Void Main` room | x 495.58–514.34, y 398.32–414.44 | 18.8 × 16.1 | |

**The void and the box disagree by about 40″ east–west**, which is the first thing to resolve. One of them is in the wrong place, and the measurements below will say which.

---

## Per level, the same three questions

For each of Basement, Main and 2nd floor:

1. **Footprint.** East–west and north–south, at a stated height off that floor. If it steps, measure above and below the step and note the height where it changes.
2. **Position, against two local references.** Not a long tape across the room — the same rule as the basement work. Good references per level:
   - **Basement:** nearest joist number and offset from its face; distance from the north or south cinder face.
   - **Main:** distance from a wall face you can name (the living-room south wall, the central dividing wall line) and from a door jamb.
   - **2nd floor:** distance from the nearest wall face and from the stair opening.
3. **Is it masonry all the way, or is there a chase built around it?** A framed chase changes what the duct can hug.

## Basement, extra

You noted it is **fatter here up to near the ceiling, where a main beam lands on the northern part where it stops**. That geometry matters more than the rest of the sheet, because it decides how much floor the utility cabinet can claim.

- Height from the basement floor to where the fat section ends.
- Footprint of the fat section, and of whatever continues above it.
- **Which beam bears on it, and where.** `basement-structure.md` records the east cross-beam running chimney → east wall in a cinder pocket, with the joist-15 beam passing *behind* the chimney without bearing on it. Confirm both — if the joist-15 beam does bear on the chimney, that is a structural fact worth having right before anyone cuts anything.

## 2nd floor, extra

- Does it pass through conditioned space, a closet, or the knee-wall attic?
- Clearance around it — how much room is there to run a duct alongside?

---

## Then: the utility cabinet

Once the chimney is placed on all three levels, the cabinet is the next object to model. What to capture while you are up and down the stairs anyway:

- **Where the three levels line up vertically.** The cabinet only works where it can be stacked; the chimney and the maintenance wall are the two fixed vertical elements to work around.
- **Available footprint on each level** — how much floor can the cabinet take without eating a room.
- **The basement end:** the air handler goes under the stairs behind the bar, so the cabinet's basement footprint is really "where the trunk leaves the unit and turns up".

The `ducting-plan.md` §5 maintenance wall already carries the constraint that matters most: the chase is **one stud space deep with room for exactly one more inside the bedroom**, which is why that section recommends rectangular wall-stack duct (3.25 × 10 or 3.25 × 12) over round. If the utility cabinet can be deeper than that wall, round duct becomes possible and the whole thing gets easier — so measuring the cabinet's available depth is directly load-bearing on the duct choice.
