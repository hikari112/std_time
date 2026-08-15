# Core Concepts

Six ideas. If you read only one page before using the library, read this one.
Every other page assumes it.

## 1. One conversion, everything else derived

There is exactly one place where a calendar date becomes a number of
milliseconds, and one place where it comes back. That pair is Howard Hinnant's
`days_from_civil` and `civil_from_days`, the algorithm C++20 adopted for
`<chrono>`: exact, branchless, no loops, no lookup tables, valid across the
whole proleptic Gregorian range.

Day-of-week, the adjusters, ISO weeks, DST boundaries, the holiday calendars and
the expiry cycles are all computed from that pair rather than reimplemented.
This is a correctness property, not a tidiness one. A library with two date
implementations has two chances to be wrong and no way to notice when they
disagree.

## 2. Civil time and exact time are different kinds of arithmetic

java.time separates `Period` (years, months, days) from `Duration`
(milliseconds) because they are not interchangeable. "+1 day" across a
daylight-saving boundary is not "+86400000 ms", and "+1 month" has no fixed
length at all.

Here that split is carried in the names:

| Moves the calendar | Moves the instant |
|---|---|
| `plus_days`, `plus_weeks` | `plus_ms`, `plus_seconds` |
| `plus_months`, `plus_years` | `plus_minutes`, `plus_hours` |
| `plus_period` | |

Reach for the wrong family and you get the classic one-hour bug. This is
important enough to have its own page:
[Civil and Exact Arithmetic](Civil-and-Exact-Arithmetic).

## 3. An offset is not a zone

A `DateTime` carries a fixed offset from UTC. In java.time terms that makes it
an `OffsetDateTime`, not a `ZonedDateTime`. It is a valid thing to be, and it is
not a zone: store `-5` in March and it is still `-5` in July.

Anything that needs real zone behaviour goes through the `Zone` enum and the
rule engine behind it. The two conversions are deliberately separate functions:

- `DateTime.to_unix()` reads the offset the record carries, literally.
- `Zone.to_unix(...)` reads civil fields as local time in a zone, and takes a
  `Resolver` because a local time can be impossible or ambiguous.

They are not one function with a flag, because they answer different questions.
See [Time Zones](Time-Zones).

## 4. Four rules, so a signature can be predicted rather than looked up

The calling convention is four rules with one stated exception. Learn them once
and you can guess most of the API.

1. **A question about a civil date is a method on `DateTime`.**
   `d.is_trading_day(ex)`, `d.iso_week()`, `d.adjusted(conv)`. There is no
   `(Year, Month, Day)` overload of any of them.
2. **A function that builds a date takes loose ints, and only builders do.**
   `new_datetime`, `nth_weekday_of_month`, `date_from_iso_week`,
   `monthly_expiry_day`. A bare int triple always means construction.
3. **A function that takes an instant takes it first, and stays a free
   function.** `unix_to_date(t, utc)`, `offset_at(t, z)`,
   `format_time(t, pattern, z)`, `next_fomc_after(t)`.
4. **`float utc` always means a fixed offset.** A zone that follows a
   daylight-saving rule is always a `Zone`. No parameter in the library is a
   float that behaves like a rule.

The exception: `Zone.to_unix` and its gap and overlap probes take loose ints
without being builders, because they read civil fields as local in a zone, which
is the one thing a `DateTime` cannot express.

## 5. Failure has five shapes, and each one is named

Every `@returns` in the library commits to exactly one of these. Guessing which
one applies is the single most common way to misuse a date library.

| Shape | Means | Example |
|---|---|---|
| **RAISE** | The arguments cannot mean anything. A caller bug. | 31 February, `nth = 0`, an hour of 25 |
| **`na`** | Well formed, and no answer exists. | The fifth Friday of a four-Friday month |
| **`Known.UNKNOWN`** | Well formed, the answer exists in the world, the table here does not reach it. | An FOMC date past the published calendar |
| **`false`** | Well formed, and the answer is no. | `is_holiday`, `is_trading_day` |
| **in-band number** | Only when the number is a real value of the result range, never as a stand-in for "none". | |

`Known.UNKNOWN` is a value, not `na`. Testing it with `na()` is dead code.
Full treatment on [Error Model](Error-Model).

## 6. Coverage is stated, not assumed

Exchange calendars are rules where a rule exists and a dated table where none
does. No rule predicts a hurricane or a state funeral, so unscheduled closures
live in a table, and a table is complete only for the past.

Every calendar therefore reports the years it answers exactly, through
`calendar_from()` and `calendar_through()`. A rule-driven calendar has no
horizon and reports `na` for one. A tabled calendar stops where its data stops:
Hong Kong at 2049, Tokyo at 2099, Shanghai, Bombay and Singapore at the end of
2026.

Past a horizon `is_holiday` cannot help you, because a `bool` has no room for
"not known" and will read a tabled holiday as an ordinary trading day. Ask
`closed_for_holiday()` there instead. See
[Exchange Calendars](Exchange-Calendars) and
[Scope and Limitations](Scope-and-Limitations).

## Which type am I holding?

Five types, and the choice is two questions.

**Is it a moment, or an amount of time?**

- A moment: `DateTime` for civil fields plus an offset, or a bare `int` of Unix
  milliseconds for an instant.
- An amount: `Period` for calendar amounts (years, months, days), plain `int`
  milliseconds for exact ones, `Interval` for a half-open span between two
  instants.

**Does it need to know about daylight saving?**

- No: `DateTime` and its fixed `UTC` field are enough.
- Yes: go through `Zone`. `DstRule` is the data a zone's rule is made of, and
  you will rarely construct one.

`Session` is the sixth thing, and it is none of the above: a recurring
local-time window resolved against a calendar. See [Sessions](Sessions).

---

Next: [Civil and Exact Arithmetic](Civil-and-Exact-Arithmetic)
&nbsp;·&nbsp; Up: [Home](Home)
