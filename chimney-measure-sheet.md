# Chimney measuring sheet — all three levels

The chimney is the first piece of the duct plan, and it earns that place twice over: it defines what the utility chase has to route *around*, and because it pierces every level it is a **cross-level datum** — the same trick as the basement-to-main through-holes, already built into the house.

That second point is worth being deliberate about. Measure the chimney's position against something local on each level and the three levels register to each other for free, in both axes. It is the cheapest registration available and it needs no new holes.

Reply: Unfortunately not - only the basement has raw chimney cinder. Main floor and 2nd floor wraps it in drywall. We could generously assume the drywall just adds an inch on the south face of the chimney just to be able to move on,but that isn't authoritative.

---

## What the model currently believes

Treat all of this as unverified. The chimney has never been measured.

| Level | Object | Position | Size | Notes |
|---|---|---|---|---|
| Basement | `Box` | x 550.30, y 380.21 | 36 × 24 | the fat lower section |
| Basement | `Chimney Void` room | x 500.31–512.50, y 395.16–416.34 | 12.2 × 21.2 | **does not overlap the box** |
| Main | `Chimney Void Main` room | x 495.58–514.34, y 398.32–414.44 | 18.8 × 16.1 | |

Basement: the south wall of the chimney is just about 16 inches across - maybe slightly less depending on the spot. One full cinder block. The west face of the chimey is about an inch from the centerline wall's east face. The east wall is likewise 16 inches, so again one full cinder block.

The wood paneling on the east face of the centerline wall at this spot adds a little thickness to the wall. The beam called joist 15 is directly above that wall, and may be flush if it wasn't for the wood panelling. It still roughly looks like an inch between the beam and the side of the chimney, the wood panelling is pretty thin.

However, things are already wrong. There is almost exactly 12 inches between the beam and joist 16, then 13.25 from that to joist 17. But the schematic has joist 16 directly above the eastern edge of the chimney, which is not at all right, it sits several inches further west, not quite at the middle, but closer to the middle of the chimney than the eastern edge.

I moved the wall west x point to 501.5 and sized at 16 inches wide, and it now looks better, but I am concerned about the center-point of the easternmost "wall" of the chimney vs its overall width since it isn't a thin wall, we're dealing with cinder blocks. But we also might not be since there's an actual true void in the middle for the exhaust. That wouldn't work if we just had two cinder blocks on each level. Are there specialized chimney blocks that just happen to measure the same as two cinder blocks?

In either case on the north side of the chiney almost exactly 12 inches down from the bottom of the joists there is a stepped down wall of cinder blocks - roughly one cinder block in size all the way down (although it looks like they're stacked vertically in at least one spot). The main girder sits atop what looks like a 4x4 wooden beam stump, sitting atop the top cinder block.

So the true box in the basement appears to just be 16x16, or 16x24 where the 8 more inches get added on the north side. That may be enough to at least try to true up the location of the chimney box in the basement

The main floor chimney box is immediately harder to diagnose, since I don't have a frame of reference of where the 16x16 center is. The south face is about 19.5 inches across. The east wall is 20.25. It is about 94.25 inches from the south face of the chimney to the north face of the stump wall that should be approximately where the original south wall of the house stands. Not too far off the measurement of 94 inches in the basement. Encouraging,

The chimney box in the bedroom is integrated into the interior wall on its north side, on the other side of that wall is a closet.

The box in the 2nd floor is slightly more open as there's a gap between the north wall and the interior wall, not currently shown on the schematic at all. But even the base placement of the chimney box/void on the main and 2nd floor is wrong since the basement was wrong. 

The box dimensions on the 2nd floor:
- south wall 17 and 5/8ths
- east wall also 17 and 5/8ths
- north wall however is 18.25

It appears that there is a tiny bit of original wood panelling in the thin gap between the north face of the chimney box and the bathroom wall, which is 4.875 inches across

It is 56.5 inches from the south face of the chimney box to the north face of the south wall, behind which is the knee wall attic that then goes to the edge of the original house box. I don't have a good way to measure the knee wall attic but one surmises it would be somewhere around 94 - 56.5 inches deep here, based on chimney vs inner cinder block wall in the basement, give or take a little for drywall and such.

So the utility closet here would have just under 40 inches from chimney to knee wall attic.
In the basement there is about 45 inches from the chimney to the door frame into the other side of the basement
On the main floor there is open bedroom for something wider still, but we might not want an overly long closet so you don't get dead space unreachable from a closet door

Added challenge: in the basement the top of the stairs are only about 40 inches up by the chimney, then it drops about 8 inches per step every 8 inches. That produces a fairly small triangle of surface that would be exposed to the void under the stairs on what would be the south side of the air handler.

**The void and the box disagree by about 40″ east–west**, which is the first thing to resolve. One of them is in the wrong place, and the measurements below will say which.

---

## Per level, the same three questions

For each of Basement, Main and 2nd floor:

1. **Footprint.** East–west and north–south, at a stated height off that floor. If it steps, measure above and below the step and note the height where it changes.
2. **Position, against two local references.** Not a long tape across the room — the same rule as the basement work. Good references per level:
   - **Basement:** nearest joist number and offset from its face; distance from the north or south cinder face.
     - 94 inches from south face of chimney to south cinder block wall
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
