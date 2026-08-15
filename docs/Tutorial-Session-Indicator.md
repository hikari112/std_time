# Tutorial: a session indicator

One indicator, built in five steps, ending in something publishable. It draws
the regular session, marks its first and last bars on the bar itself, shades
half days differently, and prints a countdown.

Each step compiles on its own, so you can stop anywhere.

## Step 1: the frame

```pine
//@version=6
indicator("Session Map", overlay = true, max_boxes_count = 100)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.US_REGULAR)

plot(na)
```

`var` matters. A session is configuration, not per-bar work, so it is built once
on the first bar and reused. `max_boxes_count` is raised because we will draw
one box per day and Pine's default is 50.

## Step 2: one box per session, correctly bounded

```pine
//@version=6
indicator("Session Map", overlay = true, max_boxes_count = 100)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.US_REGULAR)
var box today = na

if t.changed(time[1], time, t.TimeUnit.DAY, t.Zone.NEW_YORK)
    t.Interval iv = sess.bounds(t.unix_to_date_zone(time, t.Zone.NEW_YORK))
    if not na(iv)
        today := box.new(left = iv.FromMS, top = high, right = iv.ToMS,
                         bottom = low, xloc = xloc.bar_time,
                         bgcolor = color.new(color.blue, 92),
                         border_color = color.new(color.blue, 60))

plot(na)
```

Two library calls carry this. `changed` gives a real New York day boundary
whatever the chart's own timezone is, and `bounds` returns the session's actual
window for that date. On a half day the right edge already comes in to 13:00,
because `US_REGULAR` names the NYSE calendar and sets `EarlyClose`.

`bounds` returns `na` on a day the session does not run, which is the guard.

## Step 3: grow the box to the day's real range

```pine
//@version=6
indicator("Session Map", overlay = true, max_boxes_count = 100)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.US_REGULAR)
var box today = na

if t.changed(time[1], time, t.TimeUnit.DAY, t.Zone.NEW_YORK)
    t.Interval iv = sess.bounds(t.unix_to_date_zone(time, t.Zone.NEW_YORK))
    today := na(iv) ? na
             : box.new(left = iv.FromMS, top = high, right = iv.ToMS,
                       bottom = low, xloc = xloc.bar_time,
                       bgcolor = color.new(color.blue, 92),
                       border_color = color.new(color.blue, 60))

if not na(today) and sess.is_open(time)
    box.set_top(today, math.max(box.get_top(today), high))
    box.set_bottom(today, math.min(box.get_bottom(today), low))

plot(na)
```

`is_open` excludes any lunch break, which does not matter for the NYSE but does
if you point this at `TSE_REGULAR` or `HKEX_REGULAR`.

## Step 4: mark the first and last bars, on the bar

```pine
//@version=6
indicator("Session Map", overlay = true, max_boxes_count = 100,
          max_labels_count = 200)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.US_REGULAR)
var box today = na

if t.changed(time[1], time, t.TimeUnit.DAY, t.Zone.NEW_YORK)
    t.Interval iv = sess.bounds(t.unix_to_date_zone(time, t.Zone.NEW_YORK))
    today := na(iv) ? na
             : box.new(left = iv.FromMS, top = high, right = iv.ToMS,
                       bottom = low, xloc = xloc.bar_time,
                       bgcolor = color.new(color.blue, 92),
                       border_color = color.new(color.blue, 60))

if not na(today) and sess.is_open(time)
    box.set_top(today, math.max(box.get_top(today), high))
    box.set_bottom(today, math.min(box.get_bottom(today), low))

if sess.is_first_bar(time, time_close)
    label.new(bar_index, low, "open", yloc = yloc.belowbar,
              style = label.style_label_up, size = size.tiny)

if sess.is_last_bar(time, time_close)
    label.new(bar_index, high, "close", yloc = yloc.abovebar,
              style = label.style_label_down, size = size.tiny)

plot(na)
```

This is the step that is hard without the library. The usual idiom infers the
close from the data, so it lands one bar late and never fires on the chart's
final bar. Here the close instant comes from the calendar, and the test is the
bar's own `[time, time_close)` window against it. No lookahead, and it behaves
the same on historical and realtime bars.

It is right on half days too, because the bound comes from `session_close()`.

## Step 5: half-day colour and a countdown

```pine
//@version=6
indicator("Session Map", overlay = true, max_boxes_count = 100,
          max_labels_count = 200)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.US_REGULAR)
var box today = na

t.DateTime d = t.unix_to_date_zone(time, t.Zone.NEW_YORK)
bool half    = d.is_early_close(t.Exchange.NYSE)

if t.changed(time[1], time, t.TimeUnit.DAY, t.Zone.NEW_YORK)
    t.Interval iv = sess.bounds(d)
    today := na(iv) ? na
             : box.new(left = iv.FromMS, top = high, right = iv.ToMS,
                       bottom = low, xloc = xloc.bar_time,
                       bgcolor = color.new(half ? color.orange : color.blue, 92),
                       border_color = color.new(half ? color.orange : color.blue, 60))

if not na(today) and sess.is_open(time)
    box.set_top(today, math.max(box.get_top(today), high))
    box.set_bottom(today, math.min(box.get_bottom(today), low))

if sess.is_first_bar(time, time_close)
    label.new(bar_index, low, "open", yloc = yloc.belowbar,
              style = label.style_label_up, size = size.tiny)

if sess.is_last_bar(time, time_close)
    label.new(bar_index, high, half ? "early close" : "close",
              yloc = yloc.abovebar, style = label.style_label_down,
              size = size.tiny)

if barstate.islast
    int left = sess.time_to_close(timenow)
    string msg = na(left)
                 ? "shut, opens in " + t.format_duration(sess.time_to_open(timenow), 2)
                 : t.format_duration(left, 2) + " to close"
    label.new(bar_index + 3, close, msg, xloc = xloc.bar_index,
              style = label.style_label_left, size = size.small)

plot(na)
```

Two details in the last step. `is_early_close` returns `false` on a day the
market is shut, because a closed market is not an early close, so the box colour
cannot mislead. And `time_to_close` returns `na` when shut rather than 0, which
is what lets the countdown say "shut" instead of "0s".

## Pointing it at another market

Change two lines:

```pine
var t.Session sess = t.session_of(t.SessionId.TSE_REGULAR)
```

and the zone in the three places it appears, to `t.Zone.TOKYO`. The lunch break
then falls out of `is_open` automatically, the box still spans the whole
envelope, and the day markers still fire once, because a break is modelled as a
hole in one window rather than a boundary between two.

## What to read next

- [Sessions](Sessions) for the model behind `bounds`, `is_last_bar` and breaks.
- [Recipes](Recipes) for shorter answers to other problems.
- [Performance and Limits](Performance-and-Limits) before you scale the drawing
  up, since Pine caps boxes and labels at 500 each.

---

Previous: [Quick Start](Quick-Start)
&nbsp;·&nbsp; Next: [Recipes](Recipes)
