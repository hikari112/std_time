# Recipes

Worked answers to things people actually build. Every block compiles as written
against `The_Peaceful_Lizard/std_time/1`.

Each recipe says what it prevents, because the naive version usually works most
days, which is what makes it dangerous.

## 1. A session box that shrinks on a half day

```pine
//@version=6
indicator("session box", overlay = true)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.US_REGULAR)

if t.changed(time[1], time, t.TimeUnit.DAY, t.Zone.NEW_YORK)
    t.Interval iv = sess.bounds(t.unix_to_date_zone(time, t.Zone.NEW_YORK))
    if not na(iv)
        box.new(left = iv.FromMS, top = high, right = iv.ToMS, bottom = low,
                xloc = xloc.bar_time, bgcolor = color.new(color.blue, 90))
```

**Prevents** a box drawn to 16:00 on the day after Thanksgiving, three hours
past a market that shut at 13:00. `US_REGULAR` names the NYSE calendar and sets
`EarlyClose`, so `bounds` returns the real close.

## 2. Fire on the closing bar, not one bar later

```pine
//@version=6
indicator("close marker", overlay = true)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.US_REGULAR)

if sess.is_last_bar(time, time_close)
    label.new(bar_index, high, "close", style = label.style_label_down)
```

**Prevents** the one-bar lag in `in_session and not in_session[1]`, which cannot
be true until the next bar exists and never fires at all on the chart's last
bar.

## 3. Countdown that survives past 24 hours

```pine
//@version=6
indicator("countdown", overlay = true)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.US_REGULAR)
int left = sess.time_to_close(timenow)

if barstate.islast
    label.new(bar_index, high,
              na(left) ? "shut, opens in " + t.format_duration(sess.time_to_open(timenow), 2)
                       : t.format_duration(left, 2),
              style = label.style_label_down)
```

**Prevents** two things. `str.format_time` wraps past 24 hours and has no day
field, so a weekend countdown reads as two hours. And `time_to_close` returns
`na` when shut rather than 0, so "shut" and "closing now" cannot be confused.

## 4. Option tenor for pricing

```pine
//@version=6
indicator("tenor", overlay = false)
import The_Peaceful_Lizard/std_time/1 as t

int   expiry = t.next_expiry_after(time, 16, t.Zone.NEW_YORK, t.ExpiryKind.MONTHLY)
float tau    = t.year_fraction(time, expiry, t.DayCount.ACT_365F)
float tau_bd = t.year_fraction(time, expiry, t.DayCount.ACT_252, t.Exchange.NYSE)

plot(tau,    "ACT/365F")
plot(tau_bd, "ACT/252")
```

**Prevents** hand-rolled `(expiry - now) / 31536000000.0`, which is `ACT/365F`
only by accident and silently wrong under every other convention. Note
`ExpiryKind.VIX` raises here: it settles in the morning, so use
`next_vix_settlement_after` instead.

## 5. VIX settlement, which is not a close

```pine
//@version=6
indicator("vix settle", overlay = false)
import The_Peaceful_Lizard/std_time/1 as t

int settle = t.next_vix_settlement_after(time)
int days   = t.day_count_days(time, settle, t.DayCount.ACT_365F)

plot(days, "days to settlement")
```

**Prevents** treating VIX like the equity cycle. Its date is anchored in the
*following* month, thirty days before that month's third Friday, and it settles
at the 09:30 opening auction rather than the close.

## 6. Is it shut, and can I trust the answer

```pine
//@version=6
indicator("honest holiday", overlay = false)
import The_Peaceful_Lizard/std_time/1 as t

t.DateTime d  = t.unix_to_date_zone(time, t.Zone.SHANGHAI)
t.Known    k  = d.closed_for_holiday(t.Exchange.SSE)
int through   = t.Exchange.SSE.calendar_through()
bool covered  = na(through) or d.Year <= through

plot(k == t.Known.YES ? 1 : k == t.Known.NO ? 0 : -1)
plot(covered ? 1 : 0)
```

**Prevents** a confident wrong answer past 2026, where `is_holiday` reads a
tabled holiday as an ordinary trading day. `na(through)` first, because a
rule-driven calendar returns `na` and a bare comparison against it is `na`,
which reads as false.

## 7. Why is the market shut

```pine
//@version=6
indicator("named closure", overlay = true)
import The_Peaceful_Lizard/std_time/1 as t

t.DateTime d = t.unix_to_date_zone(time, t.Zone.NEW_YORK)
string why   = d.holiday_name(t.Exchange.NYSE)
bool starts  = not na(why) and na(why[1])

if starts
    label.new(bar_index, high, why, style = label.style_label_down)
```

**Prevents** a boolean that tells you nothing. On 29 October 2012 this says
"Hurricane Sandy". Keep the call out of the `if` condition: a call behind a
short-circuiting `and` is not guaranteed to run every bar, and you are reading
its history.

## 8. Settlement dates a swap desk would recognise

```pine
//@version=6
indicator("roll", overlay = false)
import The_Peaceful_Lizard/std_time/1 as t

var t.Exchange ex = t.Exchange.NYSE
t.DateTime d  = t.unix_to_date_zone(time, t.Zone.NEW_YORK)

t.DateTime t2 = d.plus_trading_days(2, ex)
t.DateTime m3 = d.plus_period(t.parse_tenor("3M")).adjusted(t.BusinessDay.MOD_FOLLOWING, ex)

plot(t2.to_unix(), "T+2")
plot(m3.to_unix(), "3M, modified following")
```

**Prevents** a three-month forward landing on Christmas, and prevents a
`FOLLOWING` roll pushing a month-end payment into the next month, which is what
`MOD_FOLLOWING` exists to stop.

## 9. Nth-of-the-month strategies

```pine
//@version=6
indicator("t plus n", overlay = false)
import The_Peaceful_Lizard/std_time/1 as t

var t.Exchange ex = t.Exchange.NYSE
t.DateTime d = t.unix_to_date_zone(time, t.Zone.NEW_YORK)
int nth      = d.trading_day_of_month(ex)

plot(nth, "trading day of month")
plot(t.trading_days_in_month(d.Year, d.Month, ex), "days this month")
```

**Prevents** counting calendar days and calling it the third trading day.
`trading_day_of_month` returns `na`, not 0, on a day the market is shut.

## 10. A session that is not a preset

```pine
//@version=6
indicator("custom session", overlay = true)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session tokyo = t.parse_session("0900-1130,1230-1530:23456",
                                      t.Zone.TOKYO, Cal = t.Exchange.JPX)
var t.Session fx = t.new_session("FX Asia", t.Zone.TOKYO, 0, 9 * 60,
                                 t.day_mask(t.Weekday.SUNDAY, t.Weekday.FRIDAY))

bgcolor(tokyo.is_open(time) ? color.new(color.orange, 92) : na)
plot(fx.is_open(time) ? 1 : 0)
```

**Prevents** two mistakes. The comma models Tokyo's lunch as a hole in one
window, so day markers still fire once. And `fx` names no calendar, deliberately:
a default of NYSE would shut a Tokyo session on Thanksgiving and trade it
through Golden Week.

## 11. Shade holidays across the visible range

```pine
//@version=6
indicator("holiday shading", overlay = true)
import The_Peaceful_Lizard/std_time/1 as t

if barstate.islast
    int a = chart.left_visible_bar_time
    int b = chart.right_visible_bar_time
    array<t.DateTime> hol = t.holidays_between(a, b, t.Exchange.NYSE)
    for i = 0 to array.size(hol) > 0 ? array.size(hol) - 1 : na
        t.DateTime h = array.get(hol, i)
        line.new(h.to_unix(), low, h.to_unix(), high, xloc = xloc.bar_time,
                 color = color.red, width = 2)
```

**Prevents** hitting the per-loop time limit by walking every day, and prevents
a silent truncation: `holidays_between` **raises** past a 20,000-day span rather
than returning a partial answer, so deriving the span from the visible range is
not just tidy, it is what keeps the call legal.

## 12. Sizing a per-session buffer

```pine
//@version=6
indicator("bar budget", overlay = false)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.TSE_REGULAR)
t.DateTime d = t.unix_to_date_zone(time, t.Zone.TOKYO)
int budget   = sess.bars_per_session(d, 5 * 60 * 1000)

plot(budget, "5m bars today")
```

**Prevents** a fixed array size that overflows on a full day or wastes space on
a half day. On a session with a lunch break the morning and afternoon are
rounded independently, which is the number you actually need.

---

Previous: [Tutorial: session indicator](Tutorial-Session-Indicator)
&nbsp;·&nbsp; Next: [Migrating from Pine Built-ins](Migrating-from-Pine-Built-ins)
