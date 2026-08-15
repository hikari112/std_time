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
from it, so there is no second implementation that can quietly disagree with
the first.

## What it covers

- **Civil arithmetic.** `DateTime` with withers and adjusters, and calendar
  time kept apart from exact time the way java.time keeps `Period` apart from
  `Duration`. `plus_months` moves the calendar, `plus_ms` moves the instant,
  and confusing the two is the one-hour bug this API shape exists to prevent.
- **Zones, not offsets.** Thirteen zones with their actual daylight-saving
  rules. Spring-forward gaps and fall-back overlaps are resolved explicitly,
  with the resolver as an argument rather than a guess.
- **Twelve exchange calendars.** NYSE, LSE, CME, JPX, EUREX, HKEX, ASX, TSX,
  SSE, BSE, SGX, and 24/7 crypto. Holidays, observance shifts, early closes,
  lunch breaks, and unscheduled closures each carrying its name: ask
  `holiday_name()` why the market is shut and it answers "Hurricane Sandy".
- **Sessions.** Bounds, windows, progress, bar counts, and a last-bar-of-day
  flag computed from the calendar instead of inferred from the next bar, so it
  fires on the closing bar itself, half days included.
- **Trading-day arithmetic.** Add, count, and roll by ISDA business-day
  conventions. Year fractions under the standard day counts.
- **Expiries.** Monthly, weekly, quarterly and 0DTE, plus the VIX settlement
  rule.
- **Formatting and parsing.** ISO-8601 both directions, week dates, durations,
  and a relative formatter for "3d 4h ago".

## Documentation

The [wiki](https://github.com/hikari112/std_time/wiki) is the manual. Start
with [Core Concepts](https://github.com/hikari112/std_time/wiki/Core-Concepts)
if you are new to the model, or the
[API Index](https://github.com/hikari112/std_time/wiki/API-Index) if you know
what you are looking for.

The reference pages are generated from the library's own annotations by
`tools/build_reference.py`, so they cannot drift from the code.

## Honesty

A calendar can be wrong in a way a moving average cannot, so this one states
its own limits. Every exchange calendar reports the years it answers exactly,
through `calendar_from()` and `calendar_through()`. Past a horizon,
`closed_for_holiday()` answers `Known.UNKNOWN`, which is not a no. Each zone
declares the first year its rules are exact. The
[Scope and Limitations](https://github.com/hikari112/std_time/wiki/Scope-and-Limitations)
page is the full list, including the divergences from published exchange data
that are known and deliberate.

## Licence

Mozilla Public License 2.0. See [LICENSE](LICENSE).

Copyright (c) 2026 Jesse Sanford, published on TradingView as
`The_Peaceful_Lizard`.
