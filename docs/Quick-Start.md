# Quick Start

Four things that work, in the order they stop being surprising. Every block on
this page compiles as written.

## 1. A date you can ask questions of

```pine
//@version=6
indicator("quick start 1", overlay = true)
import The_Peaceful_Lizard/std_time/1 as t

t.DateTime d = t.unix_to_date_zone(time, t.Zone.NEW_YORK)

plot(d.is_trading_day(t.Exchange.NYSE) ? 1 : 0)
```

`unix_to_date_zone` turns the bar's instant into civil fields in a real zone,
daylight saving included. From there everything is a method on the record.

Note `t.DateTime`, not `DateTime`. Imported types take your alias.

## 2. Is the market shut, and why

```pine
//@version=6
indicator("quick start 2", overlay = true)
import The_Peaceful_Lizard/std_time/1 as t

t.DateTime d = t.unix_to_date_zone(time, t.Zone.NEW_YORK)
string why = d.holiday_name(t.Exchange.NYSE)
bool starts = not na(why) and na(why[1])

if starts
    label.new(bar_index, high, why, style = label.style_label_down)
```

`why` is assigned on every bar and `why[1]` reads its own history, so the label
fires once per closure rather than on every bar of one. Keeping the call out of
the `if` condition matters: a call placed behind a short-circuiting `and` is not
guaranteed to run every bar, and a function whose history you read has to.

`holiday_name` is the source of truth: `is_holiday` is *defined* as this being
non-`na`, so the predicate and the name cannot disagree. On 29 and 30 October
2012 it answers "Hurricane Sandy".

## 3. A session box that survives half days

```pine
//@version=6
indicator("quick start 3", overlay = true)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.US_REGULAR)

if t.changed(time[1], time, t.TimeUnit.DAY, t.Zone.NEW_YORK)
    t.Interval iv = sess.bounds(t.unix_to_date_zone(time, t.Zone.NEW_YORK))
    if not na(iv)
        box.new(left = iv.FromMS, top = high, right = iv.ToMS, bottom = low,
                xloc = xloc.bar_time, bgcolor = color.new(color.blue, 90),
                border_color = color.blue)
```

Two things are doing work here. `changed` detects a new New York day on any
chart, in any zone. `bounds` returns the session's actual window for that date,
so the day after Thanksgiving draws to 13:00 rather than 16:00, without you
special-casing it.

`var` on the session matters: it is configuration, not per-bar work.

## 4. Fire on the closing bar, not one bar later

```pine
//@version=6
indicator("quick start 4", overlay = true)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.US_REGULAR)

if sess.is_last_bar(time, time_close)
    label.new(bar_index, high, "close", style = label.style_label_down)
```

The usual Pine idiom infers the session end from the data, so it cannot be true
until the next bar exists, and on the chart's final bar it never fires at all.
This computes the close instant from the calendar and compares the bar's own
window against it, so it lands on the bar itself, historical and realtime alike,
half days included.

## Where to go next

- The model, in order: [Core Concepts](Core-Concepts).
- Something specific: [Task Index](Task-Index) or [API Index](API-Index).
- Coming from the built-ins:
  [Migrating from Pine Built-ins](Migrating-from-Pine-Built-ins).
- More worked examples: [Recipes](Recipes).

---

Previous: [Installation](Installation) &nbsp;·&nbsp; Next: [Core Concepts](Core-Concepts)
