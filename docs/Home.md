# std_time

A calendar for Pine Script v6. Civil dates, time zones with real daylight-saving
rules, twelve exchange calendars, sessions, option expiries and ISDA day counts,
in one import.

It exists because "what day is it in Tokyo" and "is the market open" are
questions an indicator asks constantly, and Pine's built-ins answer only
halfway. They can format a timestamp; they cannot tell Thanksgiving from a
Thursday.

Everything routes through one conversion. The civil and epoch pair at the core
is Howard Hinnant's algorithm, the one C++20 adopted for `<chrono>`.
Day-of-week, ISO weeks, DST boundaries, holidays and expiries are all derived
from it, so there is no second implementation that can quietly disagree with the
first.

## Three ways in

**New to it?** Read the model in order, starting with
[Core Concepts](Core-Concepts). Twelve short pages, each building on the last.
The two that save the most debugging are
[Civil and Exact Arithmetic](Civil-and-Exact-Arithmetic) and
[Value Semantics](Value-Semantics).

**Know what you want?** [API Index](API-Index) lists all 240 exports
alphabetically in one page, so Ctrl-F finds anything.
[Task Index](Task-Index) sorts the same set by the question you arrived with.

**Deciding whether to trust it?** [Verification](Verification) names the oracle,
the range and the counts for every layer, and lists what the harnesses cannot
reach. [Scope and Limitations](Scope-and-Limitations) is the matching list of
what is not modelled, including three divergences from published exchange data
that are known and deliberate.

## What it covers

| Area | What you get |
|---|---|
| Civil arithmetic | `DateTime` with withers and adjusters, calendar time kept apart from exact time the way java.time keeps `Period` apart from `Duration` |
| Zones | Thirteen zones with their actual DST rules, and gaps and overlaps resolved explicitly rather than guessed |
| Exchange calendars | NYSE, LSE, CME, JPX, EUREX, HKEX, ASX, TSX, SSE, BSE, SGX and 24/7 crypto, with named closures, half days and lunch breaks |
| Sessions | Bounds, windows, progress, bar counts, and a last-bar flag that fires on the closing bar itself |
| Trading days | Add, count and roll by ISDA business-day conventions; year fractions under the standard day counts |
| Expiries | Monthly, weekly, quarterly and 0DTE, plus the VIX settlement rule |
| Text | ISO-8601 in and out, week dates, durations, and a relative formatter |

## The part worth knowing before anything else

Two questions that look the same and are not:

- `plus_days(1)` moves the calendar and keeps the wall-clock time. `plus_ms(86400000)` moves the instant. On two Sundays a year they differ by an hour.
- `DateTime.to_unix()` reads the fixed offset a record carries. `Zone.to_unix(...)` reads civil fields as local time in a zone and consults the rules, which is the only one of the two that can tell you the moment you asked about never happened.

Getting these the wrong way round is the classic date bug, and the API is shaped
to make the choice visible rather than to hide it.

## Honesty

Every exchange calendar reports the years it answers exactly, through
`calendar_from()` and `calendar_through()`. Past a horizon,
`closed_for_holiday()` answers `Known.UNKNOWN`, which is a value and is not a
no. Each zone declares the first year its rules are exact. Unscheduled closures
are recorded for the past, because no table predicts the next hurricane.

Where the library is knowingly wrong, it says so and says by how much: the JPX
close is 30 minutes early for every session from 5 November to 30 December 2024,
and the HKEX open half an hour early for 43 sessions in early 2011. Both are on
[Scope and Limitations](Scope-and-Limitations).

## Licence

Mozilla Public License 2.0. Copyright (c) 2026 Jesse Sanford, published on
TradingView as `The_Peaceful_Lizard`.

---

Next: [Installation](Installation) &nbsp;·&nbsp; [Core Concepts](Core-Concepts)
