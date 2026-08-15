# Expiries

Five listed cycles under one `ExpiryKind`, so a scanner can take the cycle as
data rather than branching on it.

## The five cycles

| Cycle | What it is |
|---|---|
| `DAILY` | Every trading day. SPX, NDX and XSP list an expiry each session, so this cycle *is* the trading calendar |
| `WEEKLY` | That week's Friday, rolled back to the previous trading day when the Friday does not trade |
| `MONTHLY` | The classic third Friday, stepped to the previous day when that Friday is a scheduled holiday |
| `QUARTERLY` | The monthly of March, June, September and December, the triple-witching months |
| `VIX` | The Wednesday thirty days before the following month's third Friday |

Four of the five settle at the close, which is why they share
`next_expiry_after` and its `Hour` parameter. VIX is the odd one out in both
dimensions at once, and that shapes the API.

## Why VIX keeps its own functions

Its date is anchored in the *following* month, and it settles in the *morning*,
at the 09:30 New York opening auction that prints the Special Opening Quotation.
A close-shaped `Hour` cannot name that moment.

So VIX has its own instant pair, `vix_settlement` and
`next_vix_settlement_after`, and joins the others only where the date alone
matters: `is_expiry_day` and `expiries_between`.

Passing `ExpiryKind.VIX` to `next_expiry_after` raises rather than quietly
ignoring the `Hour` you supplied:

```
next_expiry_after: ExpiryKind.VIX is a.m.-settled and has no close-shaped Hour. Use next_vix_settlement_after
```

## The VIX rule in full

The Wednesday thirty days before the following month's third Friday, stepped to
the business day immediately preceding it when *either* that Wednesday or that
Friday is a Cboe holiday.

Both branches happen in practice:

- Good Friday landing on the third Friday moved 2022-03 and 2025-03 to a Tuesday.
- Juneteenth landing on the computed Wednesday moved 2024-06.
- Juneteenth observed on the Friday moves 2026-05.

The Cboe holiday set is the NYSE rule set the library already carries, with the
Juneteenth epoch of 2022 and the Saturday-observed-on-Friday rule included. The
2026-05 and projected 2027-05 exceptions both hang on those two details.

The rule reproduces every settlement on the published Cboe calendars from 2021
to 2026, all four Tuesday exceptions included. Past the last published calendar
the same arithmetic runs as projection, and Cboe can move any future date by
circular, which no rule predicts.

Note the thirty-days-back arithmetic needs no weekday check: thirty days before
a Friday is a Wednesday by identity, since 30 is two days past four whole weeks.

## Scheduled holidays only

`monthly_expiry_day` and `vix_settlement_day` step for scheduled holidays and
not for unscheduled closures, deliberately and for the same reason: the exchange
knew the published calendar when it listed the contract. An unscheduled closure
moves settlement by circular, which no rule predicts.

## Tenors

`parse_tenor` turns the strings a desk actually writes into a `Period`:

| String | Meaning |
|---|---|
| `"1D"`, `"7D"` | Days |
| `"2W"` | Weeks, as 14 days |
| `"3M"`, `"6M"` | Months |
| `"1Y"` | Years |

Combined with `plus_period` and `adjusted`, that is the whole "three months
forward, rolled modified following" story in three calls. See
[Trading Days and Day Counts](Trading-Days-and-Day-Counts).

## Scanning a range

`expiries_between(from_ms, to_ms, kind, z)` returns the dates ascending. It
**raises** past a 20,000-day span rather than silently truncating, so derive the
span from what you are drawing rather than passing the whole chart. See
[Performance and Limits](Performance-and-Limits).

`is_triple_witching()` is the quarterly test on a date you already hold, and
`is_expiry_day(kind)` the general one.

---

Previous: [Trading Days and Day Counts](Trading-Days-and-Day-Counts)
&nbsp;·&nbsp; Next: [Sessions](Sessions)
&nbsp;·&nbsp; Reference: [API-Functions](API-Functions), [API-DateTime](API-DateTime)
