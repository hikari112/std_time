# Trading Days and Day Counts

Three related things: moving by trading days, rolling a date off a closed day,
and measuring the fraction of a year between two instants. They come together
because an option tenor is all three at once.

## Weekday, business day, trading day

Three different words for three different things, used precisely throughout:

- **Weekday.** Monday to Friday. A calendar fact, no exchange involved.
  `is_weekday()`, `weekdays_between()`.
- **Trading day.** A day the exchange's calendar says it is open. Weekends and
  holidays excluded. `is_trading_day(ex)`.
- **Business day.** A trading day, used specifically in the ISDA sense of
  rolling a date that landed on a closed one.

`weekdays_between` is closed form: no loop, no calendar. It is exactly what
`trading_days_between` degenerates to under a calendar with no holidays.

## Moving

```pine
d.next_trading_day(ex)          // the next one, whatever d is
d.prev_trading_day(ex)
d.plus_trading_days(2, ex)      // T+2
d.minus_trading_days(5, ex)
```

`plus_trading_days(0)` returns the same date whether or not it trades. That is
deliberate: moving zero days is not a request to fix the date. Use `adjusted`
for that.

The walk is bounded at `abs(n) * 2 + 30` calendar days and **raises** if it runs
out, because roughly 1.45 calendar days per trading day is the worst real case
and running out means the calendar data is wrong.

## Rolling: the ISDA conventions

`adjusted(conv, ex)` moves a date off a non-trading day by the named rule:

| Convention | Behaviour |
|---|---|
| `UNADJUSTED` | Leave it alone even if the market is shut |
| `FOLLOWING` | Move forward to the next trading day |
| `MOD_FOLLOWING` | Move forward, unless that crosses into the next month, then backward |
| `PRECEDING` | Move backward to the previous trading day |
| `MOD_PRECEDING` | Move backward, unless that crosses into the previous month, then forward |

The two modified forms exist so a schedule of month-end payments stays inside
its months. It returns a `DateTime` at midnight rather than preserving the
receiver's time of day, because a business-day roll is a statement about which
*day* settles.

A three-month forward, rolled the way a swap desk would:

```pine
d.plus_period(t.parse_tenor("3M")).adjusted(t.BusinessDay.MOD_FOLLOWING, ex)
```

## Positions within a month

```pine
t.first_trading_day_of_month(2025, 6, ex)
t.last_trading_day_of_month(2025, 6, ex)
t.trading_days_in_month(2025, 6, ex)     // 19 to 23 on the equity calendars
d.trading_day_of_month(ex)               // which one this is, 1-based
```

`trading_day_of_month` returns `na` on a day the market is shut, not 0. Zero
would be a real ordinal, so it cannot also mean "no answer". This is the
in-band-number clause from the [Error Model](Error-Model).

## Counting a span

`trading_days_between` is half-open on the earlier of the two dates: the earlier
date counts when it trades, the later never does, and the result is negated when
the arguments come the other way round. Half-open so consecutive spans add up
without double-counting the join.

It does not walk the calendar. See
[Performance and Limits](Performance-and-Limits) for why that matters and how
the proposal-and-filter approach works.

## Day counts

The convention is the denominator of every rate and the tau of every option
price. Per the ISDA 2006 Definitions:

| Convention | Numerator over denominator |
|---|---|
| `ACT_365F` | Actual days over a fixed 365. The usual option tenor, and what crypto derivatives actually quote |
| `ACT_360` | Actual days over 360. Money-market convention |
| `ACT_ACT_ISDA` | Actual days, leap-year days over 366 and the rest over 365 |
| `D30_360` | 30/360 Bond Basis: a 31st becomes a 30th, and the end date flattens only when the start already has |
| `D30E_360` | 30E/360 Eurobond: both ends flatten unconditionally |
| `ACT_252` | Trading days over 252. Business-day time in equity volatility |

```pine
int   expiry = t.monthly_expiry(2025, 12)
float tau    = t.year_fraction(time, expiry, t.DayCount.ACT_365F)
int   n      = t.day_count_days(time, expiry, t.DayCount.D30_360)
```

`day_count_days` exposes the numerator separately because for the 30/360 family
it is not recoverable from the fraction alone.

Two traps worth naming. `ACT_252` needs an exchange, since it counts trading
days, and under `Exchange.CRYPTO` every calendar day is a trading day, so it
degenerates to actual days over 252, a denominator no crypto desk uses. Crypto
tenors are `ACT_365F`.

The 30/360 and 30E/360 implementations reproduce 14 published ISDA worked
examples, both as year fractions and as raw integer numerators.

---

Previous: [Exchange Calendars](Exchange-Calendars)
&nbsp;·&nbsp; Next: [Expiries](Expiries)
&nbsp;·&nbsp; Reference: [API-DateTime](API-DateTime), [API-Functions](API-Functions)
