# Verification

What was checked, against what, over which range, and what the checks cannot
reach. A calendar can be wrong in a way a moving average cannot, so this page
states its evidence rather than its confidence.

## The oracles

| Layer | Checked against |
|---|---|
| Civil conversions | Python `datetime`, `date.toordinal` |
| Easter and Good Friday | `dateutil` |
| Zone rules | `zoneinfo`, the IANA time zone database |
| Exchange calendars | `exchange_calendars` (XNYS, XLON, CMES, XTKS, XEUR, XHKG, XASX, XTSE, XSHG, XBOM, XSES) |
| Day counts | The ISDA 2006 published worked examples |
| VIX settlement | The published Cboe calendars |
| Pattern formatter | `strftime` plus pinned Java-convention vectors |

## Civil core

Round-trips against `date.toordinal` over 1970 to 2200: 4,716 of 4,716 exact.
Every day-of-week from 2000 to 2100 brute-forced, along with the adjusters at
nth +1 to +5 and -1 to -3. Easter and Good Friday match `dateutil` across 1970
to 2200.

## Zone engine

Brute force rather than sampling: every transition instant the IANA database
contains, in every modelled zone, probed at one second before, at, and one
second after. **1,106 transition instants matched exactly across 1970 to 2100**,
with 16,416 gap and overlap probes corroborated against IANA's own `fold=0` and
`fold=1` answers.

## Exchange calendars

Every calendar was diffed date by date against its reference over the range
below, and every one reaches zero differences apart from the three deliberate
divergences named further down.

| Calendar | Reference | Diffed over | Sessions |
|---|---|---|---|
| NYSE | XNYS | 1976-01-01 to 2035-12-31 | 7,794 |
| LSE | XLON | 1976-01-01 to 2035-12-31 | 7,833 |
| CME | CMES | 2000-01-01 to 2035-12-31 | 7,995 |
| JPX | XTKS | 2006-08-14 to 2027-08-13 | |
| EUREX | XEUR | 2006-08-14 to 2027-08-13 | |
| HKEX | XHKG | 2000-01-01 to 2049-12-31 | 12,336 |
| ASX | XASX | 1995-01-01 to 2049-12-31 | 13,923 |
| TSX | XTSE | 1995-01-01 to 2049-12-31 | 13,811 |
| SSE | XSHG | 2005-12-26 to 2026-12-31 | 5,101 |
| BSE | XBOM | 2006-01-01 to 2026-12-31 | |
| SGX | XSES | 2006-01-01 to 2026-12-31 | |

Lunch breaks were checked as instants, not just as flags. The Hong Kong break
matches XHKG to the millisecond on all 12,336 sessions, including the 99 half
days. The Tokyo 11:30 to 12:30 break matches XTKS on all 5,135 sessions from
2006 to 2027. Shanghai's 11:30 to 13:00 break matches XSHG on all 5,101.

## The rules themselves, not a restatement of them

This is the check worth understanding, because until it existed the suite had a
hole.

Every other harness diffs a hand-written Python mirror against an exchange
calendar. That checks the mirror. It does not check the Pine: inserting a
spurious holiday into the library's own ASX rule chain left all eight harnesses
green, because nothing read the Pine's rule bodies.

The fix transpiles the holiday-name chains straight out of the Pine source and
executes them. All 25 transpiled functions now run against all eight oracles and
every one diffs to zero: NYSE and LSE over 15,652 weekdays each, CME 9,391, JPX
and EUREX 5,480 each, HKEX 13,045, ASX and TSX 14,349 each. Replaying the ASX
mutation now fails, with 55 mismatches, and fails on ASX alone.

## Sessions, expiries and day counts

5,276 US sessions are all exactly 390 minutes, or 210 on half days, across every
daylight-saving transition from 2015 to 2035. Over 1,004 sessions,
`is_last_bar` flags exactly the closing minute bar and neither neighbour.

The VIX rule reproduces **all 72 published Cboe settlement dates from 2021 to
2026**, including all four Tuesday exceptions, pinned as literals.

30/360 and 30E/360 reproduce 14 published ISDA worked examples, both as year
fractions and as raw integer numerators.

## Three deliberate divergences

Each is pinned in both directions, so the suite fails if the divergence grows
*or* disappears.

1. **CME session close.** The library models Globex equity index closing at
   16:00 Chicago; CMES labels it 17:00. Opens must match to the millisecond and
   closes must be exactly one hour earlier.
2. **CME, 11 to 14 September 2001.** `exchange_calendars` lists those four days
   as ordinary sessions. CME was down from the 11th and the equity-index complex
   did not resume until the 17th. The library closes them and exempts them from
   the diff. This is a gap in the reference, not an error here.
3. **JPX close, 5 November to 30 December 2024.** The library models the TSE
   close move at year granularity, so those sessions close 30 minutes early.
   Every divergent session is walked and pinned rather than sampled.

## What the checks cannot reach

Stated because a verification page that lists only its successes is not evidence.

- **The FOMC table has no external oracle available offline.** It is checked
  structurally instead. Those checks would catch a mistyped digit, a duplicated
  line or a missing meeting. They would **not** catch a meeting that moved by
  one day and stayed a Tuesday. The retrieval date and source URL are pinned in
  the source for re-diffing.
- **Pine's copy-on-assignment and UDT aliasing are not exercised.** No Python
  harness can exercise them. See [Value Semantics](Value-Semantics) for the
  behaviour you have to hold in your head instead.
- **`period_between` has no independent oracle.** It is verified by its defining
  round-trip property, with OpenJDK's `LocalDate.until` transcribed alongside for
  comparison. Of 4,550 date pairs the two disagree on 18, and in all 18 java.time
  fails its own documented round-trip promise.
- **Session instants in daylight-saving zones hold only to 2037.** Past the
  32-bit boundary the *reference* misapplies daylight saving, so there is
  nothing to diff against. Hong Kong, on a fixed offset, runs clean to 2049.
- **NYSE and LSE rules run unchecked before 1976**, and JPX from 2000 to 2005,
  because the references do not reach there.
- **Unscheduled closures are recorded for the past only.** No table predicts the
  next hurricane.
- **VIX past the last published Cboe calendar is projection.** Cboe can move any
  future date by circular, which no rule predicts.

---

Previous: [Scope and Limitations](Scope-and-Limitations)
&nbsp;·&nbsp; Next: [Performance and Limits](Performance-and-Limits)
&nbsp;·&nbsp; See also: [Versioning and Data Currency](Versioning-and-Data-Currency)
