# Design Notes

Where the ideas came from, and the decisions that are not obvious from the API.

## Provenance

| Part | Source |
|---|---|
| Civil conversions | H. Hinnant, *chrono-Compatible Low-Level Date Algorithms*, the `days_from_civil` and `civil_from_days` pair C++20 adopted for `<chrono>` |
| Adjuster semantics | java.time `TemporalAdjusters.dayOfWeekInMonth` |
| Arithmetic semantics | java.time `LocalDate.plusMonths`, `Period.between` |
| Overflow policy | TC39 Temporal `overflow: constrain \| reject` |
| Resolver semantics | Noda Time `ZoneLocalMappingResolver`, Temporal `disambiguation` |
| Rounding modes | TC39 Temporal |
| ISO week date | ISO 8601 §4.1.4 |
| Easter | Anonymous Gregorian computus, Meeus / Jones / Butcher |
| Business-day conventions and day counts | ISDA 2006 Definitions |
| Bracketed zone suffix | RFC 9557 |

## One canonical conversion

Everything derives from the Hinnant pair. Day-of-week, the adjusters, ISO weeks,
DST boundaries, the holiday calendars and the expiry cycles are all computed
from it rather than reimplemented.

This is a correctness property. A library with two date implementations has two
chances to be wrong and no way to notice when they disagree. The same reasoning
appears throughout at smaller scale: `is_holiday` is *defined* as `holiday_name`
being non-`na`, so a date cannot be closed and nameless; `is_valid_date` is the
exact predicate `new_datetime` enforces, so the constructor and the predicate
cannot drift; `crosses_midnight` is derived from the times rather than stored,
because a stored flag can disagree with the fields it describes and eventually
does.

## Enums instead of ints and bools

`Weekday` is an enum because 0=Sunday versus 1=Monday confusion is the most
common class of date bug. `Known` is an enum because Pine's `bool` cannot hold
`na` at all, so "not known" has no room in a yes/no answer. `Known.UNKNOWN` will
not type-check where a `bool` is wanted, which means reading it as "no" has to
be written down via `is_yes()` rather than happening by default.

## Four calling rules

The convention exists so a signature can be predicted rather than looked up: a
question about a civil date is a method on `DateTime`, a function that builds a
date takes loose ints, a function that takes an instant takes it first, and
`float utc` always means a fixed offset. The one exception, `Zone.to_unix` and
its probes, is documented at its definitions. It reads civil fields as local in
a zone, which is the one thing a `DateTime` cannot express.

## Deviating from java.time on `period_between`

`period_between` follows java.time's *specification* rather than its
*implementation*. Over 1970 to 2200 the two disagree on 18 date pairs out of
4,550, and in every one of those java.time fails its own documented round-trip
promise. The property `a.plus_period(a.period_between(b)) == b` holds here.

Choosing the spec over the reference implementation is a real decision and worth
stating rather than leaving as a silent difference.

## Base-36 dated tables

Unscheduled closures and lunar holidays live in dated tables. A `yyyymmdd` key
reads better, but string data compiles at two tokens per character, and roughly
twelve hundred dates at eight digits each is five figures of compiled weight for
keys the code only ever compares whole.

Storing three base-36 digits of the day number instead saved 6,135 characters,
about 12,000 compiled tokens, and brought the library from 104,509 under the
100,256 publish cap. The tables also carry leading and trailing sentinel commas,
so a date can never match as a substring of its neighbour and membership builds
only a five-byte needle rather than copying the whole table per call.

## Counting without walking

Asking a calendar day by day costs one holiday-chain call per day, and over
thirty years that is enough to reach Pine's per-loop time limit, which is a
runtime error rather than merely slow.

So `trading_days_between` and `holidays_between` invert it: propose the handful
of days a calendar could shut on, test only those, and subtract from a
closed-form weekday count. The proposal is allowed to be wrong in one direction
only. A proposed non-holiday gets filtered out; a day never proposed would be
invisible. So the anchors are a superset over each calendar's whole modelled
range, and membership stays with the same `is_holiday` every other accessor
uses, so this cannot become a second opinion about what a holiday is.

## Sessions defined by rule, not by timestamps

A session is a recurring local-time window resolved against a calendar. Defined
that way it survives daylight saving, holidays and half days without any of them
being special-cased at the call site.

That definition is also what makes `is_last_bar` answer on the bar itself. The
close instant comes from the calendar, so the test is a comparison against a
known bound rather than an inference from the next bar's existence.

Breaks are modelled as a hole inside one window rather than a boundary between
two, matching how TradingView's own session strings read them, so day markers
fire once.

## Calendars are opt-in on a session

`Session.Cal` defaults to `na`. A default of NYSE would shut a Tokyo session on
Thanksgiving and trade it through Golden Week. There is no separate
"holiday aware" flag either, because a flag plus a calendar could hold the state
"calendar off, calendar NYSE", which is not a thing a session can be.

## Errors as five named clauses

Rather than a general "returns na on failure", every `@returns` commits to one
of RAISE, `na`, `Known.UNKNOWN`, `false`, or an in-band number. The distinction
that does the most work is the first two: `nth_weekday_of_month` raises on
`nth = 0`, an invalid argument, and returns `na` for a fifth Friday a month does
not contain, a valid question with no answer.

The in-band clause is why `time_to_close` does not return 0 while a session
runs. Zero is a real distance, so it cannot also be a flag.

## What was deliberately left out

A general `parse(str, pattern)`. A `DstRule` escape hatch for zones outside the
enum. Locale data. An instant-plus-exchange convenience layer. Each is absent
because a partial version would fail in ways that look like data problems rather
than like missing features.

---

Previous: [Versioning and Data Currency](Versioning-and-Data-Currency)
&nbsp;·&nbsp; Next: [FAQ](FAQ)
&nbsp;·&nbsp; See also: [Scope and Limitations](Scope-and-Limitations)
