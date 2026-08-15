# Error Model

Five ways a call can fail to give you an ordinary answer. Every `@returns` in
the library names exactly one of them, so the contract is in the annotation and
you do not have to infer it.

## The five clauses

### RAISE

The arguments cannot mean anything: 31 February, `nth = 0`, an hour of 25, a
bounded walk that runs past its limit. This is a caller bug, and it is reported
at the call site rather than passed downstream as a value that surfaces
somewhere unrelated.

```pine
t.new_datetime(2025, 2, 31)     // raises
t.nth_weekday_of_month(2025, 6, t.Weekday.FRIDAY, 0)   // raises: nth = 0
```

The library carries 51 `RAISES` clauses. Every one of them has a raise behind
it.

### `na`

The call is well formed and no answer exists. The fifth Friday of a month that
has four. A session window on a day the session does not run. Every parser and
every `try_*` form, because malformed input is data rather than a caller bug.

```pine
t.nth_weekday_of_month(2025, 6, t.Weekday.FRIDAY, 5)   // na: June 2025 has four
t.parse_iso("not a date")                              // na
```

### `Known.UNKNOWN`

Well formed, the answer exists in the world, and the table here does not reach
it. The economic calendar and `closed_for_holiday()` return this.

It is a value, never `na`. This matters:

```pine
Known k = d.closed_for_holiday(t.Exchange.SSE)
if na(k)                    // dead code: na(Known.UNKNOWN) is false
    ...
if k == t.Known.UNKNOWN     // correct
    ...
```

`Known` exists because Pine's `bool` cannot hold `na` at all. `bool x = na` is a
compile error, though `int`, enum and object types accept it. So "return na,
never false" is not expressible for a yes/no question.

The enum is also the stronger contract. `UNKNOWN` will not type-check anywhere a
`bool` is expected, so reading "not known" as "no" has to be written down, via
`is_yes()`, rather than happening by default.

### `false`

Well formed, and the answer is no within what the library models. `is_holiday`,
`is_trading_day`, `is_open`, `is_leap_year`.

Note the qualifier. `is_holiday` means "closed by the published calendar", not
"nothing else can close the market".

### In-band number

Only when the number is a real value of the result range, never as a stand-in
for "none".

This is why `Session.time_to_close` does not return 0 while the session runs. 0
is a real distance, so it cannot also be a flag. It returns the distance to the
next close, and `na` when there is none.

## Two failures side by side

The clearest illustration is one function with both:

```pine
t.nth_weekday_of_month(2025, 6, t.Weekday.FRIDAY, 0)   // RAISES
t.nth_weekday_of_month(2025, 6, t.Weekday.FRIDAY, 5)   // na
```

`nth = 0` is an invalid argument: there is no zeroth Friday in any month, so the
question is malformed. A fifth Friday is a valid question about a month that
happens not to contain one. Different failures, different clauses.

## Where two clauses meet

The date withers are the one place `na` and RAISE overlap, and `Overflow` picks
between them. A day past the end of a month clamps under `CONSTRAIN` and is `na`
under `REJECT`.

The time withers raise instead. There is nothing to clamp an hour of 25 to.

## Choosing the raising or non-raising form

Several operations come in both shapes. Use the raising one for values you
constructed, and the `try_` one for anything that came from outside:

| Trusted input | Untrusted input |
|---|---|
| `new_datetime(...)` | `try_new_datetime(...)` |
| direct field access | `is_valid_date(...)` first |

`is_valid_date` is the exact predicate `new_datetime` enforces, so the two
cannot drift apart.

## Reading an error message

Raises name the function and the offending value:

```
new_session: DayMask must be in [0, 127], got -1
plus_trading_days: could not resolve 500 trading days within 1030 calendar days
next_expiry_after: ExpiryKind.VIX is a.m.-settled and has no close-shaped Hour. Use next_vix_settlement_after
```

A message ending "this is a library bug" means a dispatch switch met a value it
does not handle. That is not something you can cause from the outside; please
report it.

---

Previous: [Value Semantics](Value-Semantics)
&nbsp;·&nbsp; Next: [Time Zones](Time-Zones)
&nbsp;·&nbsp; See also: [Pitfalls](Pitfalls)
