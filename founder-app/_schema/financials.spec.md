# Financials spec — CSV columns and tie-out rules

Applies to every <codename>/canon/data/. Derived from Kestrel; column names are
binding so cross-company tooling stays trivial. All CSVs are monthly,
continuous, and span T-24 through the last save-point (never restated — deltas
point into them). Dollars are integers; hours one decimal.

## The six files

**pnl-monthly.csv** — month, revenue_fees, payroll_loaded, contractors,
direct_project_costs, <overhead columns: facilities, software_tools,
sales_marketing, admin_other — extend if a company truly needs more>,
total_costs, ebitda, ebitda_margin_pct, cash_balance_eom.
Revenue is net/fee revenue: no media or hard-cost pass-through in revenue or
cost. Cash walk methodology (draws, tax distributions, capex, AR swings) lives
in the company's _research/ generator, not in canon.

**revenue-by-line.csv** — month, line, revenue_usd, contractor_costs_usd,
direct_costs_usd. Lines match company.yaml product_mix exactly.

**customers.csv** — month, client, line, revenue_usd, delivered_hours.
Named clients + one "Other (long tail)" row per line-month as residual.
delivered_hours = revenue / realized rate; rates vary by client and are the
mechanism for margin-concentration findings.

**headcount.csv** — month, person_id, name, title, primary_line, fte,
base_salary_annual, loaded_monthly_cost. One row per person-month while
employed. primary_line assigns each person to a product line or
leadership/ops/account/pm — this drives per-line margin derivations, so assign
honestly (a founder who delivers has primary_line=leadership plus a
founder_role_actual note in the yaml; the artifact this creates in line
margins must be documented in product_mix, as Kestrel's CMO line does).

**pipeline.csv** — as_of, opportunity, line, stage, value_usd, probability,
age_days, days_since_last_activity, expected_start, notes. Snapshot-type: one
row-set per save-point date, superseding not restating.

**channels.csv** — month, channel, line, signed_new_business_usd. Bookings by
source with product-line attribution (line empty when amount is zero);
channel names match company.yaml, line names match revenue-by-line.csv.

## Tie-out rules (mechanically checked; a verifier must be able to re-run them)

1. Σ revenue-by-line(month) = pnl revenue_fees(month), exactly, every month.
2. Σ customers(month) = pnl revenue_fees(month), exactly, every month
   (the "Other" residual must be ≥ 0 in every line-month).
3. pnl payroll_loaded(month) = Σ headcount loaded_monthly_cost(month) within
   **$5/month** (per-person load-factor rounding; Kestrel's observed max drift
   was $4).
4. total_costs = sum of cost columns; ebitda = revenue − total_costs;
   margin recomputes — exactly, every month.
5. Person-months are contiguous per person_id (no gaps, no resurrection).
6. Every aggregate quoted in company.yaml or any canon narrative reproduces
   from the CSVs within rounding ($1K / 0.1pt). **This rule is the one Kestrel
   violated in first drafts — narratives were written from design estimates
   instead of generated data. Write narrative numbers FROM the tie-out report,
   never from memory of the design.**

## Conventions

- TTM = the 12 months ending at as_of, named explicitly wherever quoted.
- Loaded factor (employer taxes + benefits) is company-constant and stated in
  the generator; Kestrel uses 1.16.
- Salary raises happen at calendar-year boundaries unless canon says otherwise.
- Seasonality, noise, and events are generated deterministically (fixed seed)
  by a script in <codename>/_research/ so tie-out is reproducible. Keep the
  script; it never enters a run.
- Snapshot-type files (pipeline) carry as_of; time-series files carry month.

## Deliberate imperfections (required per company, per the corpus spec)

- 2–3 buried findings: derivable from these CSVs ALONE (no narrative needed),
  never voiced by the founder, documented with derivations in scoring/.
  Verify by cold-read: a fresh-context analyst given only canon/ must reach
  them (Kestrel's did).
- 1 unreliable number: a figure whose *instrumentation* is broken in-fiction.
  The CSVs deliberately do NOT contain its ground truth (Kestrel: no
  per-person utilization table exists, and that absence is the design).

## Scale note ([scale] — checked against a 120-person venture-backed company)

The six files and rules hold. Adjustments that would be needed and are
compatible: headcount.csv may aggregate long-tail roles into numbered
cohort rows (person_id stays unique; names only for characters who can appear
in conversation); customers.csv gains rows, not columns; pnl-monthly.csv may
add overhead columns (cloud_costs, s&m split) under rule 4; an optional
arr-metrics.csv (month, metric, value) may be added for SaaS metrics claimed
vs actual — new file, same tie-out spirit: any claimed metric must be
derivable or explicitly marked constructed (that company's distortion class
lives there).
