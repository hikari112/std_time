# Civil and Exact Arithmetic

Two families of arithmetic that look alike and are not interchangeable. Picking
the wrong one is the most common date bug there is, and the reason this library
gives them different names instead of one `add()` with a unit argument.

## The distinction

**Civil arithmetic** moves the calendar and preserves wall-clock time. If it was
09:30 before, it is 09:30 after, whatever the clocks did in between.

**Exact arithmetic** moves the instant. Add 86,400,000 milliseconds and you get
a moment exactly one day of elapsed time later, which on two days a year is not
the same time of day.

| Civil | Exact |
|---|---|
| `plus_days`, `minus_days` | `plus_ms`, `minus_ms` |
| `plus_weeks`, `minus_weeks` | `plus_seconds`, `minus_seconds` |
| `plus_months`, `minus_months` | `plus_minutes`, `minus_minutes` |
| `plus_years`, `minus_years` | `plus_hours`, `minus_hours` |
| `plus_period`, `minus_period` | |

The same split runs through the amount types. `Period` holds years, months and
days and cannot be converted to milliseconds without a reference date, because
months and years have no fixed length. An exact amount is just an `int` of
milliseconds.

## Why "+1 day" is not "+86400000 ms"

On the Sunday a daylight-saving transition happens, the civil day is 23 or 25
hours long. `plus_days(1)` from Saturday 09:30 gives Sunday 09:30. Adding
`MS_DAY` gives Sunday 08:30 or 10:30, depending on the direction.

Both answers are correct answers to different questions. "Same time tomorrow" is
civil. "Twenty-four hours from now" is exact. A library that offers only one of
them forces you to write the other by hand, and that is where the hour goes
missing.

## Why "+1 month" has no length at all

31 January plus one month is a date that does not exist. There are only two
defensible things to do about it, and the library makes you pick with the
`Overflow` enum:

- `Overflow.CONSTRAIN` clamps to the last valid day, so you get 28 or 29
  February. This is java.time's behaviour and the default here.
- `Overflow.REJECT` returns `na` rather than inventing a date.

```pine
d = t.new_datetime(2025, 1, 31)
d.plus_months(1)                          // 2025-02-28
d.plus_months(1, t.Overflow.REJECT)       // na
```

A day below 1 is `na` under both, because that is not an overflow at all and
there is nothing sensible to clamp it to.

## Month arithmetic is not associative, and that is deliberate

```pine
d = t.new_datetime(2025, 1, 31)
d.plus_months(1).plus_months(1)   // 2025-03-28, via the 28 February clamp
d.plus_months(2)                  // 2025-03-31
```

Both are right. Clamping loses information, so applying it twice loses it twice.
If you need the second answer, ask for two months in one call. This is the same
behaviour java.time has, for the same reason.

## Differences come in both flavours too

`days_between` and `months_between` count whole units. `months_between` follows
`ChronoUnit.MONTHS.between`: a partial month does not count.

`period_between` returns a `Period`, decomposing the gap into years, months and
days, with every component carrying the same sign.

`until(other, unit)` is the generic form, so the unit can be chosen at runtime.

One note on `period_between`. It follows java.time's `Period.between`
definition, but it is not bug-compatible with java.time's implementation: over
1970 to 2200 the two disagree on 18 date pairs out of 4,550, and in all 18 cases
java.time fails its own documented round-trip promise. The library matches the
specification rather than the reference implementation, and the round-trip
`a.plus_period(a.period_between(b)) == b` holds.

## Rounding and truncation

`start_of(unit)`, `end_of(unit)` and `round_to(unit, mode)` snap a `DateTime` to
a unit boundary. `RoundMode` follows TC39 Temporal, applied to elapsed time
since the epoch:

| Mode | Direction |
|---|---|
| `FLOOR` | Toward the earlier boundary |
| `CEIL` | Toward the later boundary |
| `TRUNC` | Toward the epoch, so FLOOR after 1970 and CEIL before it |
| `HALF_EXPAND` | Nearest boundary, exact ties away from the epoch |

`TimeUnit.WEEK` takes a `week_start` parameter rather than assuming one, because
the answer genuinely differs and there is no correct default across markets.

---

Previous: [Core Concepts](Core-Concepts)
&nbsp;·&nbsp; Next: [Value Semantics](Value-Semantics)
&nbsp;·&nbsp; Reference: [API-DateTime](API-DateTime), [API-Period](API-Period)
