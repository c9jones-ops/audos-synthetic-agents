#!/usr/bin/env python3
"""Ember canon data generator.

Generates all canon/data/ CSVs deterministically from model-design.md.
Re-running always produces identical output (fixed seed). Asserts tie-out
rules and prints a reconciliation report. Never enters a run.
"""

import csv
import random
from pathlib import Path

random.seed(20260811)

OUT = Path(__file__).resolve().parent.parent / "canon" / "data"
OUT.mkdir(parents=True, exist_ok=True)

MONTHS = []
y, m = 2024, 8
for _ in range(31):
    MONTHS.append(f"{y:04d}-{m:02d}")
    m += 1
    if m == 13:
        y, m = y + 1, 1

T0 = "2026-08"
TTM = MONTHS[MONTHS.index(T0) - 11 : MONTHS.index(T0) + 1]
LOADED = 1.14


def r100(x):
    return int(round(x / 100.0) * 100)


# ---------------------------------------------------------------- roster (9 core FTE at T0)
# (id, name, title, hire, term, salary_2024)  — Stephen & Katie real (public roles);
# all other names invented; site names no staff, collision-clean per snapshot.
ROSTER = [
    ("F1", "Stephen Muscarella", "Co-founder / Product & Brand", None, None, 66000),
    ("C1", "Katie Muscarella", "CEO", None, None, 102000),
    ("O1", "Marcus Webb", "Ops & Fulfillment Lead", None, None, 70000),
    ("O2", "Dina Alvarez", "Fulfillment Associate", None, None, 44000),
    ("M1", "Priya Shah", "Ecommerce Manager", None, None, 78000),
    ("M2", "Jonah Kim", "Content & Social Manager", "2025-02", None, 58000),
    ("X1", "Renee Caldwell", "Customer Experience Lead", None, None, 51000),
    ("W1", "Tom Iverson", "Wholesale Account Manager", "2025-03", None, 64000),
    ("Q1", "Sofia Reyes", "Production & QC Coordinator", "2024-10", None, 57000),
]


def salary_for(base24, month):
    year = int(month[:4])
    s = base24
    if year >= 2025:
        s = r100(s * 1.04)
    if year >= 2026:
        s = r100(s * 1.035)
    if year >= 2027:
        s = r100(s * 1.03)
    return s


def active(p, month):
    _, _, _, hire, term, _ = p
    if hire and month < hire:
        return False
    if term and month >= term:
        return False
    return True


# ---------------------------------------------------------------- revenue architecture
FAMILIES = ["skillets", "dutch_ovens", "griddles_other", "care_accessories", "sets"]
FAM_SHARE = {"skillets": 0.58, "dutch_ovens": 0.17, "griddles_other": 0.09,
             "care_accessories": 0.11, "sets": 0.05}
# landed COGS as % of net revenue by family and channel economics
FAM_COGS_RATE = {"skillets": 0.35, "dutch_ovens": 0.38, "griddles_other": 0.37,
                 "care_accessories": 0.30, "sets": 0.40}
AVG_UNIT_PRICE_DTC = {"skillets": 165, "dutch_ovens": 285, "griddles_other": 145,
                      "care_accessories": 38, "sets": 420}

SEASON = {1: 0.72, 2: 0.75, 3: 0.84, 4: 0.86, 5: 0.92, 6: 0.87,
          7: 0.80, 8: 0.86, 9: 0.97, 10: 1.02, 11: 1.50, 12: 1.58}

# monthly total revenue: base grows ~24%/yr; spikes: Nov-25 gift guide, Mar-26 launch
SPIKES = {"2025-11": 96000, "2025-12": 58000, "2026-03": 112000, "2026-04": 64000,
          "2026-05": 22000, "2026-06": 10000}
BASE_START = 181000  # de-seasonalized monthly base Aug 2024
BASE_GROWTH = 0.0045  # ~5.5% annualized — baseline nearly flat; growth lives in the spikes


def month_base(i):
    return BASE_START * ((1 + BASE_GROWTH) ** i)


revenue_month = {}
for i, mo in enumerate(MONTHS):
    v = month_base(i) * SEASON[int(mo[5:])] * (1 + random.uniform(-0.06, 0.06))
    v += SPIKES.get(mo, 0)
    revenue_month[mo] = round(v)

# channel split: wholesale share grows 20% -> 29% across window; marketplace ~5%
def wh_share(i):
    return 0.20 + (0.29 - 0.20) * (i / (len(MONTHS) - 1))


chan_rev = {}  # (month, channel) -> revenue
for i, mo in enumerate(MONTHS):
    w = round(revenue_month[mo] * wh_share(i) * (1 + random.uniform(-0.10, 0.10)))
    mkt = round(revenue_month[mo] * 0.05 * (1 + random.uniform(-0.15, 0.15)))
    d = revenue_month[mo] - w - mkt
    chan_rev[(mo, "wholesale")] = w
    chan_rev[(mo, "marketplace")] = mkt
    chan_rev[(mo, "dtc")] = d

# family split within month (stable shares, slight noise, renormalized)
fam_rev = {}
for mo in MONTHS:
    weights = {f: FAM_SHARE[f] * (1 + random.uniform(-0.08, 0.08)) for f in FAMILIES}
    tot_w = sum(weights.values())
    alloc = {f: round(revenue_month[mo] * weights[f] / tot_w) for f in FAMILIES}
    resid = revenue_month[mo] - sum(alloc.values())
    alloc["skillets"] += resid
    for f in FAMILIES:
        fam_rev[(mo, f)] = alloc[f]

# ---------------------------------------------------------------- customers (wholesale doors + aggregates)
# (name, share of wholesale, start, end)  — all door names invented
DOORS = [
    ("Hearth & Hand Provisions (3 doors)", 0.115, "2024-08", None),
    ("Copper Birch Kitchen Co.", 0.083, "2024-08", None),
    ("Northline Mercantile (2 doors)", 0.078, "2024-08", None),
    ("The Larder & Co.", 0.064, "2025-01", None),
    ("Fogtown General", 0.058, "2024-08", None),
    ("Camp & Pantry (4 doors)", 0.088, "2025-03", None),
    ("Juniper Home", 0.049, "2025-05", None),
    ("Stonepath Outfitters", 0.045, "2025-08", None),
    ("Milltown Kitchen Supply", 0.041, "2025-10", None),
    ("Wren & Ash", 0.038, "2026-01", None),
    ("Bluff City Cook Shop", 0.034, "2026-03", None),
    ("Old Post Provisions", 0.030, "2026-05", None),
]

customer_rows = []  # (month, customer, channel, revenue, units)
for i, mo in enumerate(MONTHS):
    w_total = chan_rev[(mo, "wholesale")]
    allocated = 0
    for name, share, start, end in DOORS:
        if mo < start or (end and mo >= end):
            continue
        amt = round(w_total * share * (1 + random.uniform(-0.20, 0.20)))
        units = max(1, round(amt / 92))  # avg wholesale unit net price ~ $92
        customer_rows.append((mo, name, "wholesale", amt, units))
        allocated += amt
    resid = w_total - allocated
    if resid < 0:  # clamp: shrink the long tail never negative
        # remove overshoot from the largest row this month
        raise AssertionError(f"wholesale overallocation {mo}")
    customer_rows.append((mo, "Wholesale — other doors", "wholesale", resid,
                          max(1, round(resid / 92))))
    d = chan_rev[(mo, "dtc")]
    customer_rows.append((mo, "DTC (aggregate)", "dtc", d, max(1, round(d / 148))))
    mk = chan_rev[(mo, "marketplace")]
    customer_rows.append((mo, "Marketplace", "marketplace", mk, max(1, round(mk / 141))))

# ---------------------------------------------------------------- P&L, inventory, cash
# channel COGS-rate multipliers vs family base (wholesale nets less revenue per unit,
# so COGS as % of NET revenue is higher; handled at blended level here)
def month_cogs(mo):
    base = 0.0
    for f in FAMILIES:
        base += fam_rev[(mo, f)] * FAM_COGS_RATE[f]
    # wholesale share raises effective blended COGS% (same unit cost, lower net price)
    w_frac = chan_rev[(mo, "wholesale")] / revenue_month[mo]
    return round(base * (1 + 0.55 * w_frac))


# foundry purchase schedule: inventory purchases (cash) vs COGS (P&L) differ.
# Regular monthly replenishment + big seasonal runs. The Q4-2026 committed run:
# deposit 2026-09 ($118K), balance 2026-11 ($122K).
PURCHASES = {}
for i, mo in enumerate(MONTHS):
    PURCHASES[mo] = round(month_base(i) * 0.345 * (1 + random.uniform(-0.12, 0.12)))
for mo, extra in {"2024-09": 48000, "2025-03": 34000, "2025-08": 52000,
                  "2025-09": 32000, "2025-11": 18000,
                  "2026-03": 58000, "2026-07": 44000,
                  "2026-08": 54000, "2026-09": 96000, "2026-10": 22000,
                  "2026-11": 82000, "2027-01": 40000}.items():
    PURCHASES[mo] += extra

FF_INFLOWS = {"2024-11": 90000}   # the F&F bridge SAFE (in-window)
CAPEX = {"2025-10": 26000,   # No.5 pattern/tooling, installment 1 of 2
         "2025-12": 26000,   # tooling installment 2
         "2026-02": 20000,   # trade-show booth + fixtures
         "2026-06": 24000}   # second seasoning oven
MKT_BASE = 19000

pnl = []
cash = 52000
inventory = 335000
for i, mo in enumerate(MONTHS):
    rev = revenue_month[mo]
    cogs = month_cogs(mo)
    dtc_orders = max(1, round(chan_rev[(mo, "dtc")] / 148))
    fulfillment = round(dtc_orders * 16 + chan_rev[(mo, "wholesale")] * 0.030)
    mseason = {10: 1.5, 11: 2.0, 12: 1.4}.get(int(mo[5:]), 1.0)
    if mo == '2026-10':
        mseason = 0.9   # panic-phase marketing cut, the classic self-inflicted wound
    if mo == '2026-11':
        mseason = 1.6   # partially restored for BFCM, too late for early-funnel
    marketing = round(MKT_BASE * ((1 + 0.013) ** i) * mseason * (1 + random.uniform(-0.10, 0.10)))
    payroll = sum(salary_for(p[5], mo) / 12.0 * LOADED for p in ROSTER if active(p, mo))
    seasonal_labor = 10000 if int(mo[5:]) in (11, 12) else (5000 if int(mo[5:]) == 10 else 0)
    overhead = round(14200 + 62 * i + random.choice([0, 500, 1000]))  # rent/3PL base/software/insurance
    payroll_r = round(payroll)
    total_costs = cogs + fulfillment + marketing + payroll_r + seasonal_labor + overhead
    ebitda = rev - total_costs
    inventory = inventory + PURCHASES[mo] - cogs
    ar_swing = {"2025-09": 14000, "2025-12": -30000, "2026-01": 19000,
                "2026-06": -14000, "2026-07": 10000, "2026-09": 12000,
                "2026-10": 34000, "2026-12": -46000, "2027-01": 30000,
                "2027-02": -34000}.get(mo, 0)
    # 2026-10 +34K = payables stretched in the panic (visible emergency action);
    # 2027-02 -34K = those payables caught up after Q4 collections
    draws = 0  # Stephen takes salary only
    cash += (ebitda + cogs - PURCHASES[mo] + FF_INFLOWS.get(mo, 0)
             + ar_swing - CAPEX.get(mo, 0) - draws)
    pnl.append({
        "month": mo, "revenue_net": rev, "cogs": cogs, "fulfillment_shipping": fulfillment,
        "marketing": marketing, "payroll_loaded": payroll_r,
        "seasonal_labor": seasonal_labor, "overhead_other": overhead,
        "total_costs": round(total_costs), "ebitda": round(ebitda),
        "ebitda_margin_pct": round(ebitda / rev * 100, 1),
        "inventory_purchases": PURCHASES[mo],
        "inventory_balance_eom": round(inventory),
        "cash_balance_eom": round(cash),
    })

# ---------------------------------------------------------------- channels.csv (orders + revenue)
channel_rows = []
for mo in MONTHS:
    for ch, aov in (("dtc", 148), ("wholesale", None), ("marketplace", 141)):
        rev = chan_rev[(mo, ch)]
        orders = (max(1, round(rev / aov)) if aov else
                  sum(1 for r in customer_rows if r[0] == mo and r[2] == "wholesale" and r[3] > 0))
        channel_rows.append((mo, ch, orders, rev))

# ---------------------------------------------------------------- revenue-by-line.csv
line_rows = []
for mo in MONTHS:
    for f in FAMILIES:
        rev = fam_rev[(mo, f)]
        cogs_f = round(rev * FAM_COGS_RATE[f] *
                       (1 + 0.55 * chan_rev[(mo, "wholesale")] / revenue_month[mo]))
        direct = round(rev * 0.012)  # packaging inserts, damages, misc direct
        line_rows.append((mo, f, rev, cogs_f, direct))

# ---------------------------------------------------------------- pipeline snapshots (wholesale/retail opportunities)
PIPELINE = [
    ("2026-08-11", "National kitchen retailer — 46-door test order", "wholesale", "buyer-meeting", 210000, 0.30, 62, 18, "2027-02", "meeting June 24 + warm follow-up email late July; no PO, no terms discussed"),
    ("2026-08-11", "Camp & Pantry expansion to 9 doors", "wholesale", "verbal", 54000, 0.55, 34, 9, "2026-10", "existing chain, real velocity data"),
    ("2026-08-11", "Corporate gifting — fintech holiday order", "dtc", "proposal", 38000, 0.40, 21, 6, "2026-11", "500 No.8s engraved; margin-rich if run fits"),
    ("2026-08-11", "Museum-store program (2 doors)", "wholesale", "qualified", 22000, 0.35, 40, 15, "2027-01", ""),
    ("2026-08-11", "Specialty grocer endcap pilot", "wholesale", "discussing", 30000, 0.25, 12, 4, "2026-11", "care kits + No.6"),
    ("2026-11-11", "National kitchen retailer — 46-door test order", "wholesale", "po-received", 240000, 0.85, 154, 3, "2027-03", "PO LARGER than discussed; net-90; compliance manual is 40 pages"),
    ("2026-11-11", "Camp & Pantry expansion to 9 doors", "wholesale", "won", 54000, 1.0, 126, 0, "2026-10", "shipped"),
    ("2026-11-11", "Corporate gifting — fintech holiday order", "dtc", "lost", 38000, 0.0, 113, 30, "", "couldn't commit engraving capacity in Q4 crunch"),
    ("2027-02-11", "National retailer — rollout decision post-test", "wholesale", "awaiting-sell-through", 780000, 0.35, 246, 11, "2027-08", "test shipped Feb; sell-through report due May"),
    ("2027-02-11", "Museum-store program (2 doors)", "wholesale", "won", 22000, 1.0, 224, 0, "2027-01", ""),
    ("2027-02-11", "Spring wholesale push — 30 new independents", "wholesale", "campaign", 90000, 0.40, 20, 2, "2027-05", "Tom's list; Stephen calls it 'basically done'"),
]

# ---------------------------------------------------------------- write CSVs
def write(name, header, rows):
    with open(OUT / name, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


write("pnl-monthly.csv", list(pnl[0].keys()), [list(r.values()) for r in pnl])
write("revenue-by-line.csv",
      ["month", "line", "revenue_usd", "landed_cogs_usd", "direct_costs_usd"], line_rows)
write("customers.csv",
      ["month", "customer", "channel", "revenue_usd", "units"], customer_rows)
hc = []
for mo in MONTHS:
    for p in ROSTER:
        if active(p, mo):
            pid, name, title, hire, term, s24 = p
            sal = salary_for(s24, mo)
            hc.append((mo, pid, name, title, 1.0, sal, round(sal / 12.0 * LOADED)))
write("headcount.csv",
      ["month", "person_id", "name", "title", "fte", "base_salary_annual",
       "loaded_monthly_cost"], hc)
write("pipeline.csv",
      ["as_of", "opportunity", "channel", "stage", "value_usd", "probability",
       "age_days", "days_since_last_activity", "expected_start", "notes"], PIPELINE)
write("channels.csv", ["month", "channel", "orders", "revenue_usd"], channel_rows)

# ---------------------------------------------------------------- tie-out report
for mo in MONTHS:
    assert sum(v for (m, f), v in fam_rev.items() if m == mo) == revenue_month[mo], mo
    assert sum(r[3] for r in customer_rows if r[0] == mo) == revenue_month[mo], f"cust {mo}"
    assert sum(chan_rev[(mo, c)] for c in ("dtc", "wholesale", "marketplace")) == revenue_month[mo], mo

min_cash = min(r["cash_balance_eom"] for r in pnl)
assert min_cash > 5000, f"cash floor violated: {min_cash}"
inv = 335000
for r in pnl:
    inv = inv + r["inventory_purchases"] - r["cogs"]
    assert abs(inv - r["inventory_balance_eom"]) <= 1, r["month"]
    assert inv > 0, f"inventory negative {r['month']}"

rev_ttm = sum(revenue_month[mo] for mo in TTM)
cogs_ttm = sum(r["cogs"] for r in pnl if r["month"] in TTM)
ebitda_ttm = sum(r["ebitda"] for r in pnl if r["month"] in TTM)
wh_ttm = sum(chan_rev[(mo, "wholesale")] for mo in TTM)
dtc_ttm = sum(chan_rev[(mo, "dtc")] for mo in TTM)
q4_25 = sum(revenue_month[mo] for mo in ("2025-10", "2025-11", "2025-12"))
cy25 = sum(revenue_month[mo] for mo in MONTHS if mo.startswith("2025"))
cy24_5mo = sum(revenue_month[mo] for mo in MONTHS if mo.startswith("2024"))
prior_ttm = MONTHS[MONTHS.index(T0) - 23 : MONTHS.index(T0) - 11]
rev_prior = sum(revenue_month[mo] for mo in prior_ttm)
nospike = rev_ttm - sum(SPIKES.get(mo, 0) for mo in TTM)
nospike_prior = rev_prior - sum(SPIKES.get(mo, 0) for mo in prior_ttm)
cash_t0 = next(r["cash_balance_eom"] for r in pnl if r["month"] == T0)
inv_t0 = next(r["inventory_balance_eom"] for r in pnl if r["month"] == T0)
# forward cash minimum after T0 (finding A)
fwd = [(r["month"], r["cash_balance_eom"]) for r in pnl if r["month"] > T0]
low = min(fwd, key=lambda x: x[1])

print("=== EMBER TIE-OUT REPORT (TTM Sep 2025 – Aug 2026) ===")
print(f"Revenue TTM:        ${rev_ttm:,.0f}   (prior TTM ${rev_prior:,.0f}, {(rev_ttm/rev_prior-1)*100:+.1f}%)")
print(f"CY2025 revenue:     ${cy25:,.0f}   CY2024 (Aug-Dec) ${cy24_5mo:,.0f}")
print(f"Blended gross margin: {(rev_ttm-cogs_ttm)/rev_ttm*100:.1f}%  [guardrail 50-60]")
print(f"EBITDA TTM:         ${ebitda_ttm:,.0f}  ({ebitda_ttm/rev_ttm*100:.1f}%)")
print(f"Channel mix TTM:    DTC {dtc_ttm/rev_ttm*100:.0f}% / wholesale {wh_ttm/rev_ttm*100:.0f}% / mkt {100-dtc_ttm/rev_ttm*100-wh_ttm/rev_ttm*100:.0f}%")
print(f"Q4-2025 share of CY2025: {q4_25/cy25*100:.0f}%  [guardrail 30-40]")
print(f"Cash at T0:         ${cash_t0:,.0f}    Inventory at T0: ${inv_t0:,.0f}")
print(f"Forward cash minimum: ${low[1]:,.0f} in {low[0]}  [buried finding A]")
print(f"Growth ex-spikes (internal): {(nospike/nospike_prior-1)*100:+.1f}% (vs {(rev_ttm/rev_prior-1)*100:+.1f}% headline)")
spike_mos = ("2025-11", "2026-03")
ttm_ex = sum(revenue_month[m] for m in TTM if m not in spike_mos)
prior_ex = sum(revenue_month[m] for m in prior_ttm)
growth_dollars = rev_ttm - rev_prior
spike_yoy = sum(revenue_month[m] for m in spike_mos) - sum(revenue_month[m] for m in ("2024-11", "2025-03"))
print(f"Finding C (analyst-reproducible): spike months Nov-25+Mar-26 = {spike_yoy/growth_dollars*100:.0f}% of YoY dollar growth; month-exclusion baseline ~+11-16% depending on method")
jan_cash = {m: r["cash_balance_eom"] for m in ("2025-01", "2026-01", "2027-01") for r in pnl if r["month"] == m}
print(f"January cash cushion by year: {jan_cash}  [finding A texture]")
print(f"Minimum cash across full window: ${min_cash:,.0f} in {[r['month'] for r in pnl if r['cash_balance_eom'] == min_cash][0]}")
skil_ttm = sum(fam_rev[(mo, 'skillets')] for mo in TTM)
print(f"Skillets TTM:       ${skil_ttm:,.0f} ({skil_ttm/rev_ttm*100:.0f}%)")
mkt_ttm = sum(r["marketing"] for r in pnl if r["month"] in TTM)
pay_ttm = sum(r["payroll_loaded"] for r in pnl if r["month"] in TTM)
print(f"Marketing % TTM:    {mkt_ttm/rev_ttm*100:.1f}%   Payroll % TTM: {pay_ttm/rev_ttm*100:.1f}%")
print(f"Inventory days at T0: {inv_t0/(cogs_ttm/365):.0f}")
print(f"Headcount: Aug24={sum(1 for p in ROSTER if active(p,'2024-08'))}  T0={sum(1 for p in ROSTER if active(p, T0))}")
print("All tie-out assertions passed.")
