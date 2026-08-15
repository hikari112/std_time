# Formatting and Parsing

This part of the library makes it self-sufficient rather than a supplement to
`str.format_time`. The pattern letters are the same, so a pattern moves between
them unchanged, but the functions are not substitutes for each other.

## Two formatters

```pine
d.format("yyyy-MM-dd HH:mm")              // from a DateTime record
t.format_time(time, "HH:mm", t.Zone.TOKYO)  // from an instant, in a zone
```

`format` works from a record that already carries an offset. `format_time` takes
an instant and a `Zone`, resolves the offset through the rules, and formats
that.

`format_time` takes a **`Zone`, not a string**. Passing `syminfo.timezone` will
not compile, and that is deliberate: a UTC default would let a ported
`str.format_time` call compile cleanly and then silently mislabel every evening
New York bar. Use `z.to_iana()` when you need the string form for a built-in.

## Two things `str.format_time` cannot do

**`Y` is the ISO week-based year, distinct from `y`.** A week-year disagrees
with the calendar year for a few days each January, which is what makes
`"YYYY"` written for `"yyyy"` such a well-camouflaged bug: right for about 360
days a year.

**The offset designator reflects the rules this library applied**, not the
chart's timezone.

## Pattern letters

| Letter | Field | Notes |
|---|---|---|
| `G` | Era | |
| `y` | Calendar year | |
| `Y` | ISO week-based year | Not the same as `y` |
| `M` | Month | |
| `d` | Day of month | |
| `D` | Day of year | |
| `E` | Day name | |
| `e` | Weekday number, locale form | |
| `u` | ISO weekday, 1 = Monday | |
| `w` | ISO week of year | |
| `Q` | Quarter | |
| `H` | Hour, 0-23 | |
| `k` | Hour, 1-24 | |
| `h` | Hour, 1-12 | |
| `K` | Hour, 0-11 | |
| `m` | Minute | |
| `s` | Second | |
| `S` | Fraction of a second | Width follows the letter count |
| `a` | AM or PM | |
| `X` | ISO offset, `Z` for zero | |
| `Z` | RFC 822 offset | |
| `z`, `V` | Zone identifier | Falls back to the offset when no zone is known |

Repeat a letter to pad or widen: `MM` is `06`, `MMM` is `Jun`.

Single quotes escape literal text, and `''` is a literal quote. Characters
outside the pattern language pass through, which is what keeps the `T` in
`"yyyy-MM-ddTHH:mm:ss"`.

## Reserved letters raise

`L B F W O p x g n N c q` are real `DateTimeFormatter` fields this library does
not implement. They **raise** rather than printing back as literal text, because
a letter printed back would look like an answer. Single-quote any you want
literally.

An unterminated quote raises too.

## ISO 8601, both directions

`parse_iso` accepts more than `timestamp()` does: extended and basic forms, week
dates, ordinal dates, fractional seconds, every offset spelling, and the RFC
9557 bracketed-zone suffix.

```pine
t.parse_iso("2025-06-15T09:30:00-04:00")
t.parse_iso("2025-W25-1")            // week date
t.parse_iso("2025-166")              // ordinal date
t.parse_iso("20250615T093000Z")      // basic form
```

Parsers return `na` on malformed input rather than raising, because malformed
input is data rather than a caller bug. That is the `na` clause of the
[Error Model](Error-Model).

Going out:

| Call | Produces |
|---|---|
| `to_iso()` | Full date-time with offset, the round-trip form |
| `to_iso_date()` | `2025-06-15` |
| `to_iso_time()` | `09:30:00` |
| `to_iso_local()` | Date and time, no offset |
| `to_iso_week_date()` | `2025-W25-1` |
| `to_iso_ordinal_date()` | `2025-166` |
| `format_ixdtf(ms, z)` | RFC 9557, with the zone in brackets |

`parse_iso(d.to_iso())` gives back `d`.

## Durations and periods

Two different things, and they parse with different functions.

```pine
t.parse_iso_period("P1Y2M3D")     // calendar amount, returns a Period
t.parse_iso_duration("PT1.5S")    // exact amount, returns milliseconds
```

A week form becomes days: `"P1W"` parses as 7 days, not a fourth field, because
a week is exactly seven days unlike a month.

Out again with `p.to_iso()` and `format_iso_duration(ms)`.

## Human-readable output

```pine
t.format_duration(ms, 2)              // "3d 4h"
t.format_relative(target, timenow, 2) // "in 2h 15m", "3d 4h ago", "now"
```

`format_duration` exists because `str.format_time` cannot do this: it wraps past
24 hours and has no day field, so a 50-hour countdown formats as two hours.
`parts` chooses how many units to show, 1 to 4, and outside that range it
raises.

## There is no pattern-driven parser

`parse(str, pattern)` is deliberately absent. The built-ins do not offer one
either, ISO covers the formats machine-written dates actually arrive in, and a
partial implementation would fail in ways that look like data problems.

---

Previous: [Sessions](Sessions)
&nbsp;·&nbsp; Next: [Choosing the Right Tool](Choosing-the-Right-Tool)
&nbsp;·&nbsp; Reference: [API-Functions](API-Functions)
