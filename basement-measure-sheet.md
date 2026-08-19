# Basement measuring sheet — posts, joist spans, chimney, stairs

Take this down with you. Every number below is **what the model currently claims**, so you are checking rather than starting cold. Where the model is a guess it says so.

All measurements in **inches**. Report anything you like as a raw number plus what you measured from — I will convert and place.

---

## The two datums

**E–W (call it *x*) is already authoritative.** The joist grid is measured and the model matches it: interior width **394.0″ (32.83 ft)** between the cinderblock inner faces. Do not re-measure this unless something looks wrong.

**N–S (call it *y*) is NOT.** The model claims interior **264.8″ (22.07 ft)** north face to south face, and nothing has ever confirmed it. This is the single most valuable number on the sheet, because every post's y-position is measured from it.

For anything E–W, **report by joist** rather than by tape from a wall — the joists are the accurate ruler here, and a tape run 30 ft across a basement is not. "The NW post's east face is 2″ west of joist-07" beats "the NW post is 102″ from the west wall" every time.

For anything N–S, tape from the **north interior cinder face** where you can reach it, and say which face you measured from if you had to use the south.

---

## 1. Interior N–S dimension — the priority

Measure cinder inner face to cinder inner face, north to south, at **three E–W positions**: near the west wall, near the stairs, and in the east/utility zone where the block is bare.

| Where | Model claims | You measure |
|---|---:|---|
| West / den zone | 264.8″ | |
| Center / stairs | 264.8″ | |
| East / utility (bare block) | 264.8″ | |

The model has one number for all three, which is almost certainly wrong given the house grew in phases. Three different readings are a *finding*, not a problem.

**Note the surface you hit.** `basement-structure.md` records that the east/utility side has a heavy timber sill on a parge bed, the west/den is rim-only behind paneling, and the centre has a doubled rim. If you are measuring to paneling rather than block on the west, say so — that is roughly the 8″ estimate the current width depends on.

## 2. Joist spans, N–S

The joists run north–south. The model gives the two main beams a length of **271.0″**, which against a 264.8″ interior implies about 3″ of bearing at each end.

Measure the **full length** of a joist at three E–W positions, and note how much sits on the sill at each end if you can see it.

| Joist | Model length | You measure | Bearing N / S |
|---|---:|---|---|
| One in the west/den field (joist-05…08) | 271.0″ | | |
| joist-12 or joist-15 (the 3.5″ beams by the stairs) | 271.0″ | | |
| One in the east/utility field (joist-19…22) | 271.0″ | | |

If these differ from each other, that difference *is* the phased-build stagger and it is worth having.

## 3. The six posts

Named in the model, all on the Basement level. **Suspect every y value** — NW and N share an identical y, and SW and S are within 0.3″, which is what copy-placement looks like rather than measurement.

| Post | Model x | Model y | From N face | Nearest joist (model) |
|---|---:|---:|---:|---|
| NW post | 384.5 | 322.9 | 76.7″ | 3.0″ **west** of joist-07 (387.5) |
| SW post | 366.5 | 418.7 | 172.5″ | between joist-05 (355.1) and joist-06 (371.1) |
| N post | 455.4 | 322.9 | 76.7″ | between joist-11 (451.3) and the joist-12 beam (459.6) |
| S post | 455.1 | 419.0 | 172.8″ | same bay as N post |
| NE post | 560.4 | 326.8 | 80.6″ | 1.5″ **west** of joist-19 (561.9) |
| SE post | 560.1 | 399.0 | 152.8″ | same as NE post |

For each post, record:

- **E–W:** which joist it sits nearest, and the offset from that joist's face — *"west face of the post is 2¼″ east of joist-07's east face."*
- **N–S:** tape from the north interior cinder face to the post's **north face**, and give me the post's depth so I can derive the rest.
- **Actual size and material.** The model says 6×6 for all six. Confirm — a steel lally column is ~3.5″ diameter and would change both the geometry and how it reads in the plan. Wood 4×4 versus 6×6 matters too.

**Watch for the two easy-to-miss ones.** Per the notes, the middle pair sits by the stairs with one embedded in the bar, and the east pair is low-profile and obvious in person but invisible in the 2D plan.

## 4. Beam lines — the open question from `basement-structure.md`

The structure notes say the beams **do not form one line**, and the exact latitudes were never pinned. This is the other half of nailing the posts, because a post sits under a beam.

- **North girder** — 3 posts, west wall → NE post, then *turns north* without reaching the east wall. Measure its y from the north face at both ends: is it truly level, or does it step?
- **East cross-beam** — chimney → east wall, seated in a cinder pocket. Measure its y. The joist-15 beam is recorded as passing *behind the chimney without bearing on it* — confirm that, it matters structurally.
- **SW beam** — SW + S posts, stairs → west wall, sitting **further south** than the east cross-beam. Measure how much further south.

## 5. Chimney

The model has an unnamed **36″ × 24″** block at x 550.3, y 380.2 — that is almost certainly the chimney, but nothing says so. Confirm the footprint and its position relative to the nearest joist and to the north face.

Also worth noting: does the east cross-beam actually bear *on* the chimney, or into a pocket beside it?

## 6. Stairs

Model: **36″ wide × 96″ long**, at x 478.9, y 412.5, which puts it between the two 3.5″ zone-edge beams. Confirm width and run length, and its position relative to joist-12 and joist-15.

## 7. The through-holes — the highest-leverage thing here

You mentioned holes going through from basement to main floor. **These are worth more than anything else on this sheet**, and `ducting-plan.md` §5a already names one of them as the shared datum: a single point piercing both the basement ceiling and the main-floor wall cavity registers the two coordinate frames against each other, exactly the way the joists do within one level.

For **each** hole you can find:

- **E–W:** which joist bay it is in, and the offset from that joist.
- **N–S:** distance from the north interior cinder face.
- **Upstairs:** where it lands relative to something permanent on the main floor — a wall corner, a door jamb, a stud you can locate.

Two of these on opposite sides of the house would let me register the whole main floor to the basement rather than to a traced background image, which is the actual cause of the few-inch wall drift and the crawlspace gap.

---

## What I will do with it

1. Set the interior N–S dimension per zone and correct the joist spans.
2. Re-place all six posts against the joist grid E–W and the measured north face N–S.
3. Pin the three beam latitudes.
4. Name the unnamed members. **Most basement structure is currently modelled as objects literally called `Box`** — the chimney, the girders, several posts. That is why the plan is hard to read and why the 6th post went missing once already. Naming them costs nothing and makes the next session cheaper.
5. If you get the through-holes, re-register the main floor to the basement and re-run Eldr — the crawlspace and void gaps should shrink on their own.

Anything you cannot reach, say so and I will leave it flagged rather than guessing. A known gap is worth more than a plausible number.
