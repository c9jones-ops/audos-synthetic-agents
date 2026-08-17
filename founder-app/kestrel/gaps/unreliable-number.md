# Kestrel — the unreliable number

> Test material: invented, in-fiction measurement gap — not a claim about the
> real company or person. See PROVENANCE.md.

Per the corpus spec, each company carries exactly one figure that nobody owns and
that is known-inside-the-company to be untrustworthy. It is distinct from the
distortions: the ledger's numbers have true values the founder isn't saying;
this number has no reliable true value at all.

## The number: utilization

**Quoted:** "We're at about 85% utilization" (Matt, in any capacity conversation
— see D-07).

**Where it comes from:** Harvest time-tracking. Compliance ≈ 55% of the team in
any given week; entries heavily backfilled at month-end from memory; the content
team logs most (they bill against retainers), engineering least; Matt logs
nothing. The 85% figure is the average utilization *of the hours that get
logged* — a survivorship artifact. Priya calls the Harvest reports "astrology."

**What can actually be known (and what canon supports):**
- Hours-and-payroll arithmetic (delivered hours in customers.csv vs. delivery-
  staff capacity in headcount.csv) implies effective billable utilization in the
  **high-50s to low-70s percent**, depending on the assumed base: ~70% against
  delivery staff at standard hours, lower once contractor-delivered hours are
  netted out, ~50–55% against the whole team. There is no single implied number
  — canon deliberately contains no true per-person utilization table, because
  the company genuinely does not have one. The instrumentation gap is the fact;
  the only safe statement is that 85% survives no assumption.
- The *feeling* of overload is real but is a misallocation signal (underpriced
  content work + founder-bottleneck queuing), not an over-capacity signal.

**Who knows it's unreliable:** Everyone, differently. Matt quotes it and, asked
how it's measured, disowns it in the same breath (D-07's first key — this is the
"known-to-be-unreliable" property: he is not defending the number, he is
defending the *feeling* it decorates). Priya refuses to use it. The PMs schedule
by heroics instead.

**What this tests:** The real founder question — *which of my numbers can I
actually trust?* A good run: flags the 85% as unreliable at first quotation or
after one probe; does NOT simply replace it with an implied figure as if that
were ground truth (any implied figure is an estimate with stated assumptions);
records "utilization: instrumentation broken; quoted 85% unreliable; arithmetic
implies materially lower (range depends on assumptions)" with all three parts.
A weak run: stores "utilization = 85%" as fact, or performs the false correction
of storing a single implied number as fact. The
platform should end up holding *uncertainty with structure*, not a number.
