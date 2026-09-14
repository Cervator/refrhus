---
title: Overview
---

# Refr Hus — HVAC design package

A 1950s house in West Orange, NJ, measured by hand and rebuilt as a dimensioned Sweet Home 3D model, with a Manual J load calculation and a duct design derived from it.

This package is written to be handed to an HVAC contractor. Every figure is open to challenge, and the reasoning behind each one is recorded in the linked documents.

## Load and equipment

| | |
|---|---:|
| Heating load, 70°F / 14°F design | **40,331 BTU/hr** |
| Cooling load, 75°F / 91°F design | **23,125 BTU/hr** (18,228 sensible) |
| Sensible heat ratio | 0.79 |
| Design supply airflow | **1,245 CFM** |
| Manual S on the current model | 3.4 tons |
| **Size to quote** | **4.0 tons** |
| Existing unit | 4.0 tons |
| Duct, straight runs | 344 ft across 29 live runs |
| Registers and grilles | 25 |
| Whole job, pre-incentive | **$12,200–29,200** |

Design temperatures come from the Newark, NJ station.

**Airflow assumes a 30°F supply-air rise**, which is the heat-pump figure. A 50°F rise is a gas furnace and undersizes every heating-driven duct by 1.67×.

**Quote 4.0 tons rather than 3.5.** The model omits a grade line — basement walls are classed below-grade over their full height — and roughly a third of the second-floor ceiling area is not drawn. Both omissions understate the load. Adopting the professionals' measured basement U-value alone raises it to about 3.8 tons.

**All pricing is pre-incentive.** No rebate, credit or utility programme is netted off anywhere, so the figures compare against a quote line for line.

## Major proposal options

**One air handler**, relocated to the basement behind the bar, feeding all three floors through a single stacked utility cabinet beside the chimney. This is the design documented here.

**Two air handlers**, the second in the north knee-wall attic, reached through the wall at the top of the stairs. Proposed by the contractor.

| | One unit | Two units |
|---|---|---|
| Per-floor zoning | Damper throttling only | Real, independent |
| Second-floor duct location | Conditioned chase | Unconditioned attic |
| Equipment, filters, condensate paths | One | Two |
| Reaches the south side of the upstairs rooms | Yes | No — see below |

Two handlers buy genuine per-floor zoning, which a single unit cannot provide here: neither the basement nor the second floor alone can be a hard zone without starving the blower.

Against that, the proposed location has two costs. Attic air reaches an estimated 133°F on a summer design day, and the unit, its coil and its supply ducts would sit in it. And a north knee-wall unit does not reach the south side of the upstairs rooms, which carry real load. The suggested remedy — a duct channel along the office wall into the small east attic — is itself a chase, and the single-unit design is built around one that stays inside the envelope and serves all three floors.

**The deciding question is static pressure**, and it needs fitting counts this model does not contain. Ask for those before anything is fabricated.

## Known drawbacks

**Total effective length is not derivable from this model.** No elbows, tees or takeoffs are drawn, and duct sizing uses a flat fitting factor rather than true equivalent lengths. Real fittings on a three-storey run add 50–150 ft of equivalent length. Since the one-unit-versus-two question turns on static pressure, this is the most consequential gap in the package.

**The main-floor return path is undersized.** A single 4x8 duct running 30 ft through an inaccessible crawlspace carries the Main Bed, Kids Room and Utility Room returns — about 374 CFM through 32 in². The buried section cannot be changed; the basement run is open and can be enlarged. Worth verifying on site before pricing a remedy.

**Two kitchen register faces run too fast.** The SE supply has 2″ of height under the cabinetry and runs 806 fpm; the return at 3x20 runs 602. Both need more face area, and both are construction decisions rather than duct decisions.

**Some loads are deliberately biased.** Second-floor airflow is multiplied by 1.35 and the basement by 0.70, because the second floor runs hot and the basement holds temperature unconditioned. The second floor's ceiling area is modelled at 984 ft² against a professional report's 1,547, which makes the second-floor figures conservative.

**This is not an ACCA-certified calculation.** It is a Manual J estimate from a measured model, offered as a starting point rather than as a substitute for a professional report.
