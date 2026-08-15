# Choosing the Right Tool

Several questions can be asked more than one way here, and the choices are not
interchangeable. This page is the decision table for the ones that come up.

## "Is the market open?"

Two different questions wearing the same words.

| You want | Ask | Because |
|---|---|---|
| Does this **date** trade at all | `d.is_trading_day(ex)` | A calendar question about a day |
| Is the market trading at this **instant** | `sess.is_open(ms)` | A clock question, and it excludes the lunch break |

There is no instant-plus-exchange layer, no `is_market_open(t, ex)`. That is
deliberate: an exchange knows which days trade, a session knows which minutes
do. Mixing them would need a session anyway, so you name one.

If you also want the boundaries rather than a yes or no, use
`session_open(ex)` and `session_close(ex)`, which are the instants for that
exchange's regular hours on a given date, half days included.

## "Turn this civil time into an instant"

| Situation | Use |
|---|---|
| The record already carries the right offset | `d.to_unix()` |
| You have wall-clock fields and a zone | `z.to_unix(Y, M, D, h, m)` |

The first is arithmetic on a record and cannot fail. The second consults the
daylight-saving rules and can discover the moment never existed, which is why it
takes a `Resolver`. Using the first with a hand-set `UTC` field is how a New
York evening bar ends up an hour out in July.

## "Is it a holiday?"

| Situation | Use | Returns |
|---|---|---|
| Inside the calendar's stated window | `d.is_holiday(ex)` | `bool` |
| Anywhere, including past the horizon | `d.closed_for_holiday(ex)` | `Known` |
| You want to know *why* it is shut | `d.holiday_name(ex)` | `string`, or `na` |

`is_holiday` is fine when you have checked `calendar_through()` first. Past a
horizon it reads a tabled holiday as an ordinary trading day, which is a wrong
answer rather than a missing one.

## "Format this"

| Situation | Use |
|---|---|
| You hold a `DateTime` | `d.format(pattern)` |
| You hold an instant and a zone | `format_time(ms, pattern, z)` |
| You need a built-in to do it | `str.format_time(ms, pattern, z.to_iana())` |

The third is there because sometimes you genuinely need Pine's own function. The
first two give you the ISO week-based year `Y`, which the built-in does not.

## "Move this date"

| You mean | Use |
|---|---|
| Same time tomorrow | `plus_days(1)` |
| Twenty-four hours later | `plus_hours(24)` |
| Same date next month, clamped | `plus_months(1)` |
| The next day the market opens | `next_trading_day(ex)` |
| Two trading days from now | `plus_trading_days(2, ex)` |
| This date, or the next open one | `adjusted(BusinessDay.FOLLOWING, ex)` |

The last two differ on a date that already trades: `plus_trading_days(0)`
returns the same date whether or not it trades, while `adjusted` is the one that
fixes it.

## "Change one field"

| Situation | Use |
|---|---|
| Almost always | a wither: `with_month(3)` |
| You want a mutable copy | `.copy()`, then assign |
| Never | assign to a field on a record someone else holds |

Withers copy and validate. A direct field assignment aliases and can leave the
record holding 31 February. See [Value Semantics](Value-Semantics).

## "Compare two dates"

| You mean | Use |
|---|---|
| Same fields, offset included | `a.equals(b)` |
| Same moment in time | `a.same_instant(b)` |
| Ordering | `compare`, `is_before`, `is_after` |

`==` does not compile on two UDTs in Pine, so there is no accidental option
here, only a deliberate one. `12:00+00:00` and `07:00-05:00` are the same
instant and are not equal records.

## "How long between these?"

| You mean | Use |
|---|---|
| Whole calendar days | `days_between` |
| Whole months | `months_between` |
| Broken into years, months, days | `period_between` |
| Any single unit, chosen at runtime | `until(other, unit)` |
| Trading days | `trading_days_between(other, ex)` |
| A year fraction for pricing | `year_fraction(t0, t1, basis, ex)` |
| Just weekdays, no calendar | `weekdays_between` |

## "Detect a new day"

| Situation | Use |
|---|---|
| In any zone, on any chart | `changed(time[1], time, TimeUnit.DAY, z)` |
| The first bar of a session | `sess.is_first_bar(time, time_close)` |
| The last bar of a session | `sess.is_last_bar(time, time_close)` |

`changed` is a civil boundary in a zone. The session markers are about a
market's hours, and they fire on the bar itself rather than one bar late.

---

Previous: [Formatting and Parsing](Formatting-and-Parsing)
&nbsp;·&nbsp; Next: [Pitfalls](Pitfalls)
&nbsp;·&nbsp; See also: [Task Index](Task-Index)
