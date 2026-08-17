# Kestrel — buried findings (scoring only; never enters a run)

Three findings, fully derivable from canon/data/ alone, never voiced by the
founder, absent from every narrative he gives. Verified derivable 2026-08-09:
a fresh-context analyst given only canon/ reached all three independently with
matching arithmetic (see _research/decisions.md, V1). Grading: a platform
"finds" one when it states the substance with roughly-right magnitude AND shows
or implies the derivation; hitting exact decimals is not required.

## A — Profit concentration exceeds revenue concentration

**Statement:** The anchor client is 29.1% of TTM revenue but ~37% of all
delivery-margin dollars, because it is also the studio's best-priced work.
Remove it and the remaining business runs near break-even. The dependency is
roughly a third larger than the (already unstated) revenue number suggests.

**Derivation:** customers.csv → CSG TTM revenue $1,529,098 (29.1% of
$5,260,000) and 6,795 delivered hours of 31,870 total. Delivery cost pool
(delivery-line loaded payroll from headcount.csv + contractors + direct from
revenue-by-line.csv) ≈ $2.73M → ~$86/hr average cost. CSG margin contribution
≈ $1.53M − 6,795×$86 ≈ $946K of a ~$2.53M total margin pool = **37.4%**.

**Why the founder can't say it:** he has never computed per-client margin
(company.yaml, instruments); D-03 caps his awareness at "about a fifth,
best fifth" — even his correction ("closer to thirty") reaches only the
revenue dimension, never the margin dimension.

## B — The growth line loses money fully loaded

**Statement:** The content studio — the 2024 bet, six people, the line whose
"recurring revenue" the founder celebrates — runs ~20% delivery margin before
overhead and is **negative** (≈ −$190K/yr) after fair-share overhead and
account/PM load. Every dollar of its growth dilutes the firm; the two
Feb 2026 renegotiations-down made it worse; the planned hires would deepen it.

**Derivation:** revenue-by-line.csv (content: $951K revenue, $160K contractor,
$35.8K direct TTM) + headcount.csv (P1–P6 loaded payroll $565K TTM) →
20.0% delivery margin. Fair-share overhead (non-labor overhead + non-delivery
payroll ≈ 40% of revenue, pro-rata) → ≈ −$188K fully loaded.

**Why the founder can't say it:** guilt-guarded (psychology fear #3); the books
are never viewed by line; each over-serviced instance was individually
reasonable. D-06's unlock reaches one instance's truth; the line-level sum is
this finding and stays buried unless the platform does the arithmetic itself.

## C — All growth is one client; the business underneath is shrinking

**Statement:** Topline grew +8.5% YoY — and every dollar of that growth and
more is the anchor account. Ex-anchor revenue fell **−19.8%** YoY ($4.65M →
$3.73M) while headcount grew 25 → 31. Costs stepped up permanently against
revenue that stepped up conditionally; the EBITDA slide (10.6% → 7.4% → 5.8%)
is this scissor, not a bad quarter.

**Derivation:** customers.csv → total minus CSG, TTM vs prior-TTM windows;
headcount.csv → FTE counts; pnl-monthly.csv → CY margins.

**Why the founder can't say it:** he reads topline ("best year we've ever
had") and experiences the erosion as individually-reframed losses ("RFPs are
theater"). No aggregate ex-anchor view has ever been constructed.

## Near-findings (credit, not full marks)

Partial versions worth partial credit: "pipeline covers ~6 weeks, not two
quarters" (derivable; adjacent to D-05's unlock); "digital line margin ~26%,
second-worst in the shop" (derivable from the same method as B); "utilization
instrumentation broken; quoted figure unsupportable" (the unreliable-number
handling, graded separately in rubric.md). None of these three substitutes for
A, B, or C.
