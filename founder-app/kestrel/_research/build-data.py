#!/usr/bin/env python3
"""Kestrel canon data generator.

Generates all canon/data/ CSVs deterministically from the design in
model-design.md. Re-running always produces identical output (fixed seed).
Asserts the tie-out rules at the end and prints a reconciliation report.
Calibration material — never enters a test run.
"""

import csv
import random
from pathlib import Path

random.seed(20260809)

OUT = Path(__file__).resolve().parent.parent / "canon" / "data"
OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- calendar
MONTHS = []  # "YYYY-MM" strings, Aug 2024 .. Feb 2027 inclusive (31 months)
y, m = 2024, 8
for _ in range(31):
    MONTHS.append(f"{y:04d}-{m:02d}")
    m += 1
    if m == 13:
        y, m = y + 1, 1

T0 = "2026-08"
TTM_T0 = MONTHS[MONTHS.index(T0) - 11 : MONTHS.index(T0) + 1]  # Sep 25..Aug 26

LOADED = 1.16  # payroll load factor: employer taxes + benefits + 401k match


def r500(x):
    return int(round(x / 500.0) * 500)


# ---------------------------------------------------------------- roster
# (id, name, title, line, hire, term, salary_2024)
# line is the person's primary revenue line; "ops" = non-delivery.
ROSTER = [
    ("F1", "Matt Watson", "Founder / CEO / Exec Creative Director", "leadership", None, None, 135000),
    ("O1", "Priya Raman", "Director of Operations & Finance", "ops", None, None, 110000),
    ("X1", "Jamie Fentress", "Studio Coordinator", "ops", None, None, 58000),
    ("C1", "Noah Bergstrom", "Creative Director", "brand", None, None, 129000),
    ("D1", "Elise Tran", "Senior Designer", "brand", None, None, 98000),
    ("D2", "Marcus Feld", "Senior Designer", "brand", None, None, 95000),
    ("D3", "Hannah Okafor", "Designer", "brand", None, None, 85000),
    ("D4", "Tyler Grieve", "Designer", "brand", None, None, 82000),
    ("D5", "Sofia Marchetti", "Designer", "digital", None, None, 80000),
    ("D6", "Ben Auerbach", "Junior Designer", "brand", None, None, 66000),
    ("D7", "Devon Lund", "Junior Designer", "digital", None, None, 63000),
    ("D8", "Ingrid Halvorsen", "Designer", "brand", "2026-03", None, 80000),
    ("E1", "Sam Kessler", "Technical Lead", "digital", None, None, 120000),
    ("E2", "Aiko Tanabe", "Senior Developer", "digital", None, None, 105000),
    ("E3", "Rob Delgado", "Developer", "digital", None, None, 94000),
    ("E4", "Mira Shah", "Developer", "digital", None, None, 91000),
    ("E5", "Felix Nguyen", "Junior Developer", "digital", None, None, 75000),
    ("E6", "Jordan Pike", "Design Engineer", "digital", None, None, 88000),
    ("P1", "Dana Whitfield", "Content Studio Lead", "content", None, None, 94000),
    ("P2", "Leo Marsh", "Videographer", "content", None, None, 77000),
    ("P3", "Quinn Adebayo", "Producer", "content", "2024-09", None, 69000),
    ("P4", "Tess Rowan", "Content Strategist", "content", "2024-10", None, 72000),
    ("P5", "Milo Vance", "Editor", "content", "2024-11", None, 67000),
    ("P6", "Ana Petrova", "Motion Designer", "content", "2024-12", None, 80000),
    ("P7", "Kai Emerson", "Content Producer", "content", "2026-11", None, 70000),
    ("S1", "Owen Marek", "Strategy Director", "strategy", None, None, 126000),
    ("S2", "Lena Fischer", "Senior Strategist", "strategy", None, "2025-11", 112000),
    ("A1", "Rachel Osei", "Account Director", "account", None, None, 110000),
    ("A2", "Tom Brandt", "Account Manager", "account", None, None, 82000),
    ("A3", "Maya Lindqvist", "Account Manager", "account", None, None, 79000),
    ("A4", "Chris Doyle", "Account Manager", "account", "2025-06", None, 82000),
    ("M1", "Erin Sato", "Senior Project Manager", "pm", None, None, 95000),
    ("M2", "Paul Okonkwo", "Project Manager", "pm", "2025-07", None, 88000),
]

DELIVERY_LINES = {"brand", "digital", "content", "strategy", "cmo"}


def salary_for(base24, month):
    year = int(month[:4])
    s = base24
    if year >= 2025:
        s = r500(s * 1.035)
    if year >= 2026:
        s = r500(s * 1.035)
    if year >= 2027:
        s = r500(s * 1.03)
    return s


def active(person, month):
    _, _, _, _, hire, term, _ = person
    if hire and month < hire:
        return False
    if term and month >= term:  # term month = first month NOT employed
        return False
    return True


# ---------------------------------------------------------------- revenue: bottom-up lines
# Content retainers: (client, monthly fee schedule as list of (start, end_excl, fee))
CONTENT_RETAINERS = {
    "Cascadia Sport Group": [("2025-07", None, 28000)],
    "Timberline Credit Union": [("2024-08", None, 14000)],
    "Peak & Pine Outfitters": [("2024-11", None, 11000)],
    "Copper Kettle Hospitality": [("2025-02", None, 8500)],
    "Violet Ridge Vineyards": [("2024-08", "2026-02", 8500), ("2026-02", None, 7500)],
    "TrailWorks Foundation": [("2024-09", "2026-02", 7500), ("2026-02", None, 6500)],
    # Signed T+90d at $6,500/mo — breaks the T-6 pricing-floor commitment.
    "Sable House Goods": [("2026-12", None, 6500)],
}

CMO_ENGAGEMENTS = {
    "Copperline Coffee Roasters": [("2025-03", None, 20000)],
    "Halewood Bikes": [("2025-10", "2026-11", 26000)],
    "Sift Analytics": [("2026-02", None, 17000)],
}


def sched_fee(schedules, month):
    total = 0
    for start, end, fee in schedules:
        if month >= start and (end is None or month < end):
            total += fee
    return total


def month_frac(i, n):
    return i / max(n - 1, 1)


# Top-down project lines: shaped + scaled to exact TTM targets.
LINE_TTM_TARGETS = {"brand": 1780000, "digital": 1350000, "strategy": 510000}

SEASON = {  # project-work seasonality multipliers by calendar month
    1: 0.82, 2: 0.95, 3: 1.05, 4: 1.05, 5: 1.02, 6: 1.0,
    7: 0.92, 8: 0.98, 9: 1.1, 10: 1.12, 11: 1.0, 12: 0.75,
}


def build_project_line(base_start, base_end, lump, events=None):
    vals = []
    for i, mo in enumerate(MONTHS):
        base = base_start + (base_end - base_start) * month_frac(i, len(MONTHS))
        v = base * SEASON[int(mo[5:])] * (1 + random.uniform(-lump, lump))
        if events:
            v += events.get(mo, 0)
        vals.append(max(v, 0))
    return vals


raw = {
    # CSG brand work begins Jul 2025 (multi-property identity program).
    # Base project business is FLAT-TO-SOFT across the window — growth comes from
    # CSG and the new lines. This is what makes finding C true.
    "brand": build_project_line(170000, 124000, 0.22, events={
        "2025-07": 30000, "2025-08": 42000, "2025-09": 38000, "2025-10": 30000,
        "2025-11": 24000, "2026-01": 20000, "2026-03": 30000, "2026-05": 24000,
        "2026-07": 22000, "2026-09": 20000, "2026-10": 26000, "2027-01": 14000,
    }),
    "digital": build_project_line(126000, 93000, 0.28, events={
        "2025-09": 18000, "2025-10": 24000, "2026-02": 20000, "2026-04": 16000,
        "2026-06": 18000, "2026-10": 14000,
    }),
    # Strategy dips after Lena Fischer departs Nov 2025; Matt partially absorbs.
    "strategy": [],
}
for i, mo in enumerate(MONTHS):
    base = 50000 - 2000 * month_frac(i, len(MONTHS))
    if mo >= "2025-11":
        base *= 0.72  # S2 departure; founder absorbs some, rest lost
    if mo >= "2026-05":
        base *= 1.1  # partial recovery via Matt's weekends
    v = base * SEASON[int(mo[5:])] * (1 + random.uniform(-0.3, 0.3))
    raw["strategy"].append(max(v, 0))


def scale_to_ttm(vals, target):
    cur = sum(vals[MONTHS.index(mo)] for mo in TTM_T0)
    f = target / cur
    return [v * f for v in vals]


line_rev = {}
for line, target in LINE_TTM_TARGETS.items():
    line_rev[line] = [round(v) for v in scale_to_ttm(raw[line], target)]

# Bottom-up lines: retainers + small add-on projects (content shoots etc.).
content_addons = {
    "2024-12": 6000, "2025-05": 9000, "2025-09": 7000, "2025-12": 8000,
    "2026-03": 6000, "2026-06": 9000, "2026-08": 5000, "2026-12": 7000,
}
line_rev["content"] = [
    sum(sched_fee(s, mo) for s in CONTENT_RETAINERS.values()) + content_addons.get(mo, 0)
    for mo in MONTHS
]
line_rev["cmo"] = [
    sum(sched_fee(s, mo) for s in CMO_ENGAGEMENTS.values())
    + (12000 if mo in ("2025-03", "2025-10", "2026-02") else 0)  # onboarding fees
    for mo in MONTHS
]

LINES = ["brand", "digital", "content", "strategy", "cmo"]
revenue_month = {mo: sum(line_rev[l][i] for l in LINES) for i, mo in enumerate(MONTHS)}

# ---------------------------------------------------------------- clients
# Project-line clients: fixed shares of their line, active windows; Other = residual.
# (client, line, share, start, end_excl, realized hourly rate)
PROJECT_CLIENTS = [
    ("Cascadia Sport Group", "brand", 0.42, "2025-07", None, 225),
    ("Cascadia Sport Group", "digital", 0.33, "2025-09", None, 225),
    ("Fernhill Health", "brand", 0.14, "2024-08", "2025-10", 175),
    ("Bright Basin Energy", "digital", 0.26, "2024-08", None, 150),
    ("Juniper & Co.", "brand", 0.12, "2024-11", None, 170),
    ("Old Harbor Seafood", "brand", 0.10, "2025-03", None, 165),
    ("Stonebriar Wealth", "digital", 0.14, "2024-08", "2026-05", 145),
    ("Meridian Robotics", "strategy", 0.30, "2024-08", None, 195),
    ("Larkspur Beverage Co", "strategy", 0.16, "2025-01", "2026-01", 190),
    ("Violet Ridge Vineyards", "brand", 0.05, "2024-08", None, 150),
]
CLIENT_RATES = {
    "Cascadia Sport Group": 225, "Timberline Credit Union": 120,
    "Peak & Pine Outfitters": 110, "Copper Kettle Hospitality": 95,
    "Violet Ridge Vineyards": 100, "TrailWorks Foundation": 90,
    "Sable House Goods": 92, "Copperline Coffee Roasters": 260,
    "Halewood Bikes": 260, "Sift Analytics": 260,
    "Fernhill Health": 175, "Bright Basin Energy": 150, "Juniper & Co.": 170,
    "Old Harbor Seafood": 165, "Stonebriar Wealth": 145, "Meridian Robotics": 195,
    "Larkspur Beverage Co": 190, "Other (long tail)": 135,
}

client_rows = []  # (month, client, line, revenue, hours)
for i, mo in enumerate(MONTHS):
    for line in LINES:
        total = line_rev[line][i]
        allocated = 0
        if line == "content":
            for cl, scheds in CONTENT_RETAINERS.items():
                fee = sched_fee(scheds, mo)
                if fee:
                    client_rows.append((mo, cl, line, fee, fee / CLIENT_RATES[cl]))
                    allocated += fee
        elif line == "cmo":
            for cl, scheds in CMO_ENGAGEMENTS.items():
                fee = sched_fee(scheds, mo)
                if mo in ("2025-03",) and cl == "Copperline Coffee Roasters":
                    fee += 12000
                if mo in ("2025-10",) and cl == "Halewood Bikes":
                    fee += 12000
                if mo in ("2026-02",) and cl == "Sift Analytics":
                    fee += 12000
                if fee:
                    client_rows.append((mo, cl, line, fee, fee / CLIENT_RATES[cl]))
                    allocated += fee
        else:
            for cl, cline, share, start, end, rate in PROJECT_CLIENTS:
                if cline != line:
                    continue
                if mo < start or (end and mo >= end):
                    continue
                amt = round(total * share)
                client_rows.append((mo, cl, line, amt, amt / rate))
                allocated += amt
        resid = total - allocated
        if resid < 0:  # only possible on bottom-up lines via addons; clamp check
            raise AssertionError(f"negative residual {line} {mo}")
        if resid > 0:
            client_rows.append((mo, "Other (long tail)", line, resid,
                                resid / CLIENT_RATES["Other (long tail)"]))

# ---------------------------------------------------------------- costs
contractor_by_line = {}
for i, mo in enumerate(MONTHS):
    c = {}
    c["content"] = 9000 + (3000 if mo >= "2025-01" else 0) + random.choice([0, 0, 2000, 4000])
    c["digital"] = 6500 + random.choice([0, 0, 1500, 3500, 6000])
    c["brand"] = random.choice([0, 0, 0, 1500, 3000])
    c["strategy"] = 0
    c["cmo"] = 0
    contractor_by_line[mo] = c

direct_by_line = {}
for i, mo in enumerate(MONTHS):
    direct_by_line[mo] = {
        "brand": 3200 + random.choice([0, 400, 800]),
        "digital": 1600 + random.choice([0, 300, 600]),
        "content": 2400 + random.choice([0, 400, 900]),
        "strategy": 400, "cmo": 300,
    }

OVERHEAD = {}
for i, mo in enumerate(MONTHS):
    fac = 20800 if mo < "2025-01" else (21900 if mo < "2026-01" else 22600)
    soft = 11200 + round(2400 * month_frac(i, len(MONTHS)))
    sm = 24000 + (9000 if int(mo[5:]) in (2, 9) else 0) + random.choice([0, 1000, 2000])
    admin = 24500 + random.choice([0, 1000, 2500]) + (6000 if int(mo[5:]) == 4 else 0)
    OVERHEAD[mo] = {"facilities": fac, "software_tools": soft,
                    "sales_marketing": sm, "admin_other": admin}

# ---------------------------------------------------------------- P&L + cash
pnl = []
cash = 310000
AR_SWINGS = {"2025-04": -32000, "2025-05": 24000, "2026-01": -85000,
             "2026-03": 85000, "2026-09": -30000, "2026-10": 22000,
             "2026-12": -46000, "2027-01": 30000}
CAPEX = {"2024-10": 65000, "2025-01": 30000, "2025-09": 35000}
DRAWS_EXTRA = {"2025-06": 60000}  # owner distribution (home remodel)

for i, mo in enumerate(MONTHS):
    payroll = sum(salary_for(p[6], mo) / 12.0 * LOADED for p in ROSTER if active(p, mo))
    contract = sum(contractor_by_line[mo].values())
    direct = sum(direct_by_line[mo].values())
    oh = OVERHEAD[mo]
    total_cost = payroll + contract + direct + sum(oh.values())
    rev = revenue_month[mo]
    ebitda = rev - total_cost
    draws = 8000 if mo < "2025-01" else 12000
    # S-corp quarterly estimated-tax distributions: ~28% of trailing-quarter EBITDA
    tax_dist = 0
    if int(mo[5:]) in (1, 4, 6, 9) and i >= 3:
        trailing = sum(p["ebitda"] for p in pnl[i - 3 : i])
        tax_dist = max(0, round(trailing * 0.28))
    cash += (ebitda * 0.9 - draws - tax_dist - CAPEX.get(mo, 0)
             - DRAWS_EXTRA.get(mo, 0) + AR_SWINGS.get(mo, 0))
    pnl.append({
        "month": mo, "revenue_fees": rev, "payroll_loaded": round(payroll),
        "contractors": contract, "direct_project_costs": direct,
        "facilities": oh["facilities"], "software_tools": oh["software_tools"],
        "sales_marketing": oh["sales_marketing"], "admin_other": oh["admin_other"],
        "total_costs": round(total_cost), "ebitda": round(ebitda),
        "ebitda_margin_pct": round(ebitda / rev * 100, 1),
        "cash_balance_eom": round(cash),
    })

# ---------------------------------------------------------------- channels (signed new-business bookings)
CHANNELS = ["referral", "existing_client_expansion", "inbound", "partner", "outbound"]
channel_rows = []  # (month, channel, line, amount)
BOOK_EVENTS = {"2025-06": ("referral", "brand", 610000),   # CSG program (ex-colleague referral)
               "2025-10": ("referral", "cmo", 300000),     # Halewood CMO
               "2026-02": ("inbound", "cmo", 200000),      # Sift Analytics (via the blog)
               "2026-12": ("referral", "content", 78000)}  # Sable House retainer (annualized)
# Which lines each channel's ordinary bookings buy (deterministic, separate RNG
# stream so all previously generated figures stay identical).
rng_line = random.Random(20260810)
CHANNEL_LINE_WEIGHTS = {
    "referral": [("brand", 5), ("digital", 3), ("strategy", 2)],
    "existing_client_expansion": [("digital", 4), ("content", 3), ("brand", 2), ("strategy", 1)],
    "inbound": [("content", 5), ("digital", 3), ("brand", 1)],
    "partner": [("digital", 7), ("brand", 3)],
    "outbound": [("content", 6), ("digital", 4)],
}
def pick_line(ch):
    pool = [l for l, w in CHANNEL_LINE_WEIGHTS[ch] for _ in range(w)]
    return rng_line.choice(pool)

for i, mo in enumerate(MONTHS):
    base = {"referral": random.choice([0, 30000, 55000, 80000]),
            "existing_client_expansion": random.choice([0, 25000, 45000, 60000]),
            "inbound": random.choice([0, 0, 12000, 25000]),
            "partner": random.choice([0, 0, 0, 18000]),
            "outbound": random.choice([0, 0, 0, 0, 9000])}
    if mo >= "2026-09":  # founder buried in delivery; BD slows
        base = {k: round(v * 0.6) for k, v in base.items()}
    for ch in CHANNELS:
        if base[ch] > 0:
            channel_rows.append((mo, ch, pick_line(ch), base[ch]))
        else:
            channel_rows.append((mo, ch, "", 0))
    if mo in BOOK_EVENTS:
        ch, line, amt = BOOK_EVENTS[mo]
        channel_rows.append((mo, ch, line, amt))

# ---------------------------------------------------------------- pipeline snapshots
PIPELINE = [
    # as_of, opportunity, line, stage, value, prob, age_days, last_activity_days, expected_start, notes
    ("2026-08-09", "Fernhill Health system rebrand (RFP)", "brand", "proposal", 420000, 0.35, 74, 12, "2026-11", "incumbent also bidding"),
    ("2026-08-09", "Larkspur Beverage Co relaunch", "brand", "verbal", 300000, 0.50, 63, 41, "2026-10", "CEO said yes in June; no SOW; procurement silent"),
    ("2026-08-09", "Bright Basin Energy replatform", "digital", "proposal", 180000, 0.40, 38, 6, "2026-10", ""),
    ("2026-08-09", "CSG 'Project Nest' arena content expansion", "content", "discussing", 240000, 0.45, 29, 3, "2027-01", "would add ~$20K/mo to CSG"),
    ("2026-08-09", "Juniper & Co. packaging system", "brand", "qualified", 90000, 0.25, 21, 9, "2026-11", ""),
    ("2026-08-09", "Stonebriar Wealth site refresh", "digital", "qualified", 75000, 0.30, 44, 18, "2026-12", "former client returning"),
    ("2026-08-09", "Old Harbor Seafood identity refresh", "brand", "qualified", 60000, 0.30, 17, 5, "2026-11", ""),
    ("2026-08-09", "Meridian Robotics launch strategy", "strategy", "proposal", 85000, 0.40, 26, 8, "2026-10", "needs Matt personally"),
    ("2026-08-09", "Sift Analytics CMO expansion", "cmo", "discussing", 96000, 0.30, 15, 4, "2026-09", "+$8K/mo; Matt capacity question"),
    ("2026-08-09", "Sable House Goods content retainer", "content", "qualified", 78000, 0.40, 33, 11, "2026-11", "$6.5K/mo ask; below the February floor"),
    ("2026-08-09", "Alpine Credit web audit", "digital", "qualified", 40000, 0.30, 12, 2, "2026-10", ""),
    ("2026-11-09", "Larkspur Beverage Co relaunch", "brand", "verbal", 300000, 0.30, 155, 96, "2027-02", "zombie; nobody has called it"),
    ("2026-11-09", "CSG 'Project Nest' arena content expansion", "content", "proposal", 240000, 0.60, 121, 7, "2027-02", ""),
    ("2026-11-09", "Bright Basin Energy replatform", "digital", "won-pending-sow", 180000, 0.85, 130, 4, "2026-12", "start slipped once already"),
    ("2026-11-09", "Halcyon Health Plans brand audit", "brand", "qualified", 65000, 0.30, 18, 6, "2027-01", "inbound via a talk Priya gave"),
    ("2026-11-09", "Meridian Robotics launch strategy", "strategy", "lost", 85000, 0.0, 118, 30, "", "went quiet; Matt never sent revised scope"),
    ("2026-11-09", "Juniper & Co. packaging system", "brand", "qualified", 90000, 0.25, 113, 40, "2027-01", "stalled"),
    ("2027-02-09", "CSG 'Project Nest' arena content expansion", "content", "paused", 240000, 0.20, 213, 31, "", "paused pending CSG procurement review"),
    ("2027-02-09", "Larkspur Beverage Co relaunch", "brand", "lost", 300000, 0.0, 247, 140, "", "no formal no; everyone knows"),
    ("2027-02-09", "Halcyon Health Plans brand audit", "brand", "proposal", 65000, 0.45, 110, 9, "2027-04", ""),
    ("2027-02-09", "Fernhill Health digital follow-on", "digital", "qualified", 120000, 0.25, 34, 12, "2027-05", "lost the rebrand; door reopened"),
    ("2027-02-09", "Timberline Credit Union refresh", "brand", "qualified", 70000, 0.35, 27, 8, "2027-04", ""),
]

# ---------------------------------------------------------------- write CSVs
def write_csv(name, header, rows):
    with open(OUT / name, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


write_csv("pnl-monthly.csv", list(pnl[0].keys()), [list(r.values()) for r in pnl])

write_csv("revenue-by-line.csv",
          ["month", "line", "revenue_usd", "contractor_costs_usd", "direct_costs_usd"],
          [(mo, l, line_rev[l][i], contractor_by_line[mo][l], direct_by_line[mo][l])
           for i, mo in enumerate(MONTHS) for l in LINES])

write_csv("customers.csv",
          ["month", "client", "line", "revenue_usd", "delivered_hours"],
          [(mo, cl, l, rev, round(hrs, 1)) for mo, cl, l, rev, hrs in client_rows])

hc_rows = []
for mo in MONTHS:
    for p in ROSTER:
        if active(p, mo):
            pid, name, title, line, hire, term, s24 = p
            sal = salary_for(s24, mo)
            hc_rows.append((mo, pid, name, title, line,
                            1.0, sal, round(sal / 12.0 * LOADED)))
write_csv("headcount.csv",
          ["month", "person_id", "name", "title", "primary_line", "fte",
           "base_salary_annual", "loaded_monthly_cost"], hc_rows)

write_csv("pipeline.csv",
          ["as_of", "opportunity", "line", "stage", "value_usd", "probability",
           "age_days", "days_since_last_activity", "expected_start", "notes"],
          PIPELINE)

write_csv("channels.csv",
          ["month", "channel", "line", "signed_new_business_usd"], channel_rows)

# ---------------------------------------------------------------- tie-out report
def ttm(series_by_month):
    return sum(series_by_month[mo] for mo in TTM_T0)


line_by_month = {mo: {l: line_rev[l][i] for l in LINES} for i, mo in enumerate(MONTHS)}
cust_by_month = {}
for mo, cl, l, rev, hrs in client_rows:
    cust_by_month[mo] = cust_by_month.get(mo, 0) + rev

for i, mo in enumerate(MONTHS):
    assert sum(line_by_month[mo].values()) == revenue_month[mo], mo
    assert cust_by_month[mo] == revenue_month[mo], f"customer tie {mo}"

hc_count = {mo: sum(1 for p in ROSTER if active(p, mo)) for mo in MONTHS}
assert hc_count["2024-08"] == 25, hc_count["2024-08"]
assert hc_count[T0] == 31, hc_count[T0]
assert hc_count["2027-02"] == 32, hc_count["2027-02"]

rev_ttm = ttm(revenue_month)
pay_ttm = sum(r["payroll_loaded"] for r in pnl if r["month"] in TTM_T0)
ebitda_ttm = sum(r["ebitda"] for r in pnl if r["month"] in TTM_T0)
csg_ttm = sum(rev for mo, cl, l, rev, h in client_rows
              if cl == "Cascadia Sport Group" and mo in TTM_T0)
recur_ttm = sum(line_rev["content"][i] + line_rev["cmo"][i]
                for i, mo in enumerate(MONTHS) if mo in TTM_T0)

# buried finding computations
del_cost_ttm = 0
for mo in TTM_T0:
    del_cost_ttm += sum(salary_for(p[6], mo) / 12.0 * LOADED for p in ROSTER
                        if active(p, mo) and p[3] in DELIVERY_LINES)
    del_cost_ttm += sum(contractor_by_line[mo].values())
    del_cost_ttm += sum(direct_by_line[mo].values())
hours_ttm = sum(h for mo, cl, l, r, h in client_rows if mo in TTM_T0)
cost_per_hour = del_cost_ttm / hours_ttm
csg_hours = sum(h for mo, cl, l, r, h in client_rows
                if cl == "Cascadia Sport Group" and mo in TTM_T0)
csg_margin = csg_ttm - csg_hours * cost_per_hour
total_margin = rev_ttm - del_cost_ttm

content_ttm = ttm({mo: line_rev["content"][i] for i, mo in enumerate(MONTHS)})
content_cost = sum(salary_for(p[6], mo) / 12.0 * LOADED for mo in TTM_T0 for p in ROSTER
                   if active(p, mo) and p[3] == "content")
content_cost += sum(contractor_by_line[mo]["content"] + direct_by_line[mo]["content"]
                    for mo in TTM_T0)

fte_t0 = hc_count[T0]
print("=== KESTREL TIE-OUT REPORT (TTM Sep 2025 – Aug 2026) ===")
print(f"Fee revenue TTM:        ${rev_ttm:,.0f}")
print(f"Revenue / head (T0):    ${rev_ttm / fte_t0:,.0f}  [guardrail 120-220K]")
print(f"Payroll % of revenue:   {pay_ttm / rev_ttm * 100:.1f}%  [guardrail 50-65%]")
print(f"EBITDA TTM:             ${ebitda_ttm:,.0f}  ({ebitda_ttm / rev_ttm * 100:.1f}%)  [typical 8-13%]")
print(f"Delivery margin:        {total_margin / rev_ttm * 100:.1f}%  [healthy 50-60%]")
print(f"Recurring share:        {recur_ttm / rev_ttm * 100:.1f}%  (founder claims 'more than half')")
print(f"CSG revenue share:      {csg_ttm / rev_ttm * 100:.1f}%  (${csg_ttm:,.0f})  [>25% = flagged risk]")
print(f"CSG share of delivery-margin $: {csg_margin / total_margin * 100:.1f}%  [buried finding A]")
print(f"Content line margin:    {(content_ttm - content_cost) / content_ttm * 100:.1f}% "
      f"(rev ${content_ttm:,.0f} / cost ${content_cost:,.0f})  [buried finding B]")
cy24_run = sum(revenue_month[mo] for mo in MONTHS[:5]) / 5 * 12
print(f"CY2024 implied run-rate: ${cy24_run:,.0f} @ 25-29 FTE")
first12 = MONTHS[0:12]
rev_first12 = sum(revenue_month[mo] for mo in first12)
fte_avg_first12 = sum(hc_count[mo] for mo in first12) / 12
print(f"First-12mo rev/avg-head: ${rev_first12 / fte_avg_first12:,.0f}  vs T0 ${rev_ttm / fte_t0:,.0f}")
prior_ttm = MONTHS[MONTHS.index(T0) - 23 : MONTHS.index(T0) - 11]  # Sep 24..Aug 25
ex_csg_now = rev_ttm - csg_ttm
csg_prior = sum(rev for mo, cl, l, rev, h in client_rows
                if cl == "Cascadia Sport Group" and mo in prior_ttm)
rev_prior = sum(revenue_month[mo] for mo in prior_ttm)
ex_csg_prior = rev_prior - csg_prior
print(f"Ex-CSG revenue TTM:     ${ex_csg_now:,.0f} now vs ${ex_csg_prior:,.0f} prior year "
      f"({(ex_csg_now / ex_csg_prior - 1) * 100:+.1f}%)  [buried finding C]")
print(f"EBITDA by CY: ", {yr: round(sum(r['ebitda'] for r in pnl if r['month'].startswith(yr)) /
      max(sum(r['revenue_fees'] for r in pnl if r['month'].startswith(yr)), 1) * 100, 1)
      for yr in ("2024", "2025", "2026")})
w = sum(v * p for _, _, _, s, v, p, *_ in
        [r for r in PIPELINE if r[0] == "2026-08-09"] for _ in [0]) if False else \
    sum(r[4] * r[5] for r in PIPELINE if r[0] == "2026-08-09")
print(f"Pipeline weighted (T0): ${w:,.0f} = {w / (rev_ttm / 52):.1f} weeks of revenue")
print(f"Cash EOM Aug 2026:      ${pnl[MONTHS.index(T0)]['cash_balance_eom']:,.0f} (start Aug 2024: $310,000)")
print(f"Headcount: Aug24={hc_count['2024-08']}  T0={hc_count[T0]}  Feb27={hc_count['2027-02']}")
ch_line = {}
ch_tot = {}
for mo, ch, line, amt in channel_rows:
    if mo in TTM_T0 and amt:
        ch_line[(ch, line)] = ch_line.get((ch, line), 0) + amt
        ch_tot[ch] = ch_tot.get(ch, 0) + amt
print("New business TTM by channel x line:")
for ch in CHANNELS:
    parts = {l: v for (c, l), v in ch_line.items() if c == ch}
    tot = ch_tot.get(ch, 0)
    detail = ", ".join(f"{l} {v/1000:.0f}K" for l, v in sorted(parts.items(), key=lambda x: -x[1]))
    print(f"  {ch:26s} ${tot/1000:6.0f}K  ({detail})")
line_book = {}
for (c, l), v in ch_line.items():
    line_book[l] = line_book.get(l, 0) + v
print("  by line:", {l: f"{v/1000:.0f}K" for l, v in sorted(line_book.items(), key=lambda x: -x[1])})
print("All tie-out assertions passed.")
