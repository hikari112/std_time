# Scope and Limitations

What the library does not model, does not know, or knows only for a stated
window. None of this is hidden behind a general disclaimer: every limit below is
either reported by a function you can call or stated at the definition it
affects.

## Coverage horizons

Every calendar reports the years it answers exactly.

```pine
t.Exchange.SSE.calendar_from()      // 2006
t.Exchange.SSE.calendar_through()   // 2026
t.Exchange.NYSE.calendar_through()  // na: rule-driven, no horizon
```

| Calendar | Exact from | Exact through | Why the horizon exists |
|---|---|---|---|
| NYSE, LSE, CME, EUREX, ASX, TSX | 1976 / 1976 / 2000 / 2006 / 1995 / 1995 | none | Rule-driven |
| JPX | 2000 | 2099 | Equinox holidays use the standard 1980-2099 approximation |
| HKEX | 2000 | 2049 | Lunar festivals are tabled, not computed |
| SSE, BSE, SGX | 2006 | 2026 | Lunar, lunisolar or Islamic holidays, or annually re-announced |
| CRYPTO | no bound | none | Every calendar day trades |

Shanghai, Bombay and Singapore need their tables refreshed each year to keep
answering. Shanghai's State Council holiday blocks have changed length three
times in twenty years, so nothing extrapolates them.

Past a horizon, `is_holiday` reads a tabled holiday as an ordinary trading day,
because `bool` has no room for "not known". Ask `closed_for_holiday()`, which
returns `Known.UNKNOWN`.

Zones state the same thing through `rules_from()`. Before that year the oldest
known rule is extrapolated backward and should not be trusted. The table is on
[Time Zones](Time-Zones).

## Known divergences from published exchange data

Deliberate, and pinned in the test suite so they cannot drift unnoticed.

- **JPX, 5 November to 30 December 2024:** every session closes 30 minutes
  early. The TSE close moved 15:00 to 15:30 on 2024-11-05 and the library models
  the close at year granularity.
- **HKEX, 43 sessions in early 2011:** the open is modelled half an hour early,
  same year-granular era gate. The Hong Kong open moved 10:00 to 09:30 on
  2011-03-07.
- **CME sessions:** differ from CMES by a labelled one-hour close, because the
  library models the Globex equity-index schedule and the reference labels it
  17:00 to 17:00.

## Not modelled at all

- **Leap seconds.** They do not exist in Unix time and are not modelled here.
- **Pre-1582 dates as history.** The calendar is proleptic Gregorian: it is
  arithmetic, not history. Dates before the cutover never happened as written,
  and year 0 exists under astronomical numbering, unlike common historical usage.
- **CME's daily maintenance halt**, and the hours of CME products other than
  equity index.
- **The XETRA preset carries no holiday calendar.** German cash-market holidays
  are unmodelled, so it runs on the weekday mask alone rather than borrowing the
  Eurex calendar, which closes on different days.
- **The Bombay Muhurat evening session** on Diwali.
- **More than one intraday break per session.** Every market modelled here with
  a break takes exactly one, and a session that crosses midnight may not carry
  one at all.
- **The weekly VX cycle.** `ExpiryKind.VIX` is the monthly settlement.
- **The FTSE Russell reconstitution exception.** `russell_rebalance_day`
  implements the unmodified last-Friday-in-June rule, so it is a week late for
  2018, 2023, 2028 and 2029, when the last Friday falls on 29 or 30 June.
- **Locales.** Month names, day names, holiday names and the relative
  formatter's "in", "ago" and "now" are English only. Locale data is CLDR's job.
- **A general pattern parser.** `parse(str, pattern)` is deliberately absent.
  ISO covers the formats machine-written dates actually arrive in, and a partial
  parser would fail in ways that look like data problems. `parse_iso` returns
  `na` rather than guessing.

## Things that are true but easy to misread

**`is_holiday` means "closed by the published calendar".** It does not mean
"nothing else can close the market". Unscheduled closures are recorded for the
past; no rule predicts the next one.

**Counting trading days does not walk them.** `trading_days_between` and
`holidays_between` propose the handful of days a calendar could shut on, test
only those, and subtract from a closed-form weekday count. The proposal is
per-exchange and deliberately generous. A day it never proposed would be
invisible, so the anchors are a superset over each calendar's whole modelled
range.

**A preset is one set of hours.** `TSE_REGULAR` uses the schedule from 5
November 2024 and `HKEX_REGULAR` the schedule from 7 March 2011, so both are
wrong before their era change by the amounts noted above.

**`ACT/252` under `CRYPTO` degenerates.** Every calendar day is a trading day,
so the convention becomes actual days over 252, which no crypto desk uses.

## What verification could not reach

Listed in full on [Verification](Verification): the FOMC table has no offline
oracle and is checked structurally, Pine's UDT aliasing cannot be exercised by
any Python harness, and session instants in daylight-saving zones hold only to
2037 because the reference itself breaks past the 32-bit boundary.

---

Previous: [Pitfalls](Pitfalls)
&nbsp;·&nbsp; Next: [Verification](Verification)
&nbsp;·&nbsp; See also: [Versioning and Data Currency](Versioning-and-Data-Currency)
