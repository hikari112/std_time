# Sessions

A session is a recurring local-time window on selected weekdays, resolved
against a real calendar. Defined that way instead of as a pair of timestamps, it
survives daylight saving, holidays and half days without any of them being
special-cased at the call site.

## Getting one

Twenty-six presets cover the common cases:

```pine
sess = t.session_of(t.SessionId.US_REGULAR)     // 09:30-16:00 New York, NYSE calendar
tokyo = t.session_of(t.SessionId.TSE_REGULAR)   // 09:00-15:30 Tokyo, lunch 11:30-12:30
```

Or build one. `new_session` takes minutes past local midnight:

```pine
sess = t.new_session("London open", t.Zone.LONDON, 8 * 60, 9 * 60,
                     t.day_mask(t.Weekday.MONDAY, t.Weekday.FRIDAY),
                     t.Exchange.LSE, true)
```

Or parse a TradingView session string, which is the format you already write:

```pine
sess = t.parse_session("0900-1130,1230-1530:23456", t.Zone.TOKYO, Cal = t.Exchange.JPX)
```

The comma marks an intraday break; the digits after the colon are weekdays with
1 meaning Sunday. `to_spec()` goes back the other way. A string with two or more
commas returns `na`: TradingView writes those, and this model has one break to
put them in.

## Why `is_last_bar` is not a bar late

This is the part worth reading even if you skip the rest.

The usual Pine idiom infers the session end from the data: some form of "was in
session last bar, not in session now". That cannot be true until the next bar
exists. So the flag lands one bar *after* the bar it describes, and on the final
bar of the chart it never lands at all.

This library computes the close instant from the calendar instead. `is_last_bar`
compares the bar's own `[open, close)` window against that instant and answers
on the bar itself, with no lookahead, identically on historical and realtime
bars. Feed it Pine's `time` and `time_close`:

```pine
if sess.is_last_bar(time, time_close)
    label.new(bar_index, high, "close")
```

It is also correct on half days, because the bound comes from `session_close()`,
which already knows the day after Thanksgiving closes at 13:00. A session drawn
from fixed hours does not.

`is_first_bar` is the same idea at the other end.

## Windows and bounds

`bounds(on)` gives the half-open `Interval` a session occupies on a given start
date, or `na` when it does not run that day:

```pine
iv = sess.bounds(t.today(t.Zone.NEW_YORK))
if not na(iv)
    box.new(left = iv.FromMS, right = iv.ToMS, ...)
```

Only `Year`, `Month` and `Day` of the argument are read. A session's window
comes from its own times and zone, so any time of day the record carries is not
part of the question.

For a session that crosses midnight the end lands on the following calendar day,
and *that* day is the one the holiday and half-day tests ask about, because it
is the day the session settles into. A Globex session opening Sunday evening is
Monday's trading day; one that would open Friday evening has no Saturday to
settle into.

The instant-first accessors avoid the date question entirely:

| Call | Answers |
|---|---|
| `window_at(ms)` | The window containing this instant, or `na` |
| `window_before(ms)` | The most recent window that has already ended |
| `window_after(ms)` | The next window that opens strictly after |
| `windows_between(a, b)` | Every window in a span |
| `is_open(ms)` | Whether the market is trading, break excluded |
| `progress(ms)` | How far through the window, 0 to 1 |
| `time_to_close(ms)` | Milliseconds remaining, `na` when shut |
| `time_to_open(ms)` | Distance to the next open, never 0 while running |

`time_to_open` deserves a note. It answers the same question whether or not the
session is running: while it runs, the answer is the distance to the *next*
open, not zero. Zero is a real distance, so it cannot also be a flag.

## Breaks are holes, not boundaries

Three modelled markets take a lunch break: Tokyo, Hong Kong and Shanghai. The
break is a hole inside one window rather than a boundary between two, which is
how TradingView's own session strings read it. `"0900-1130,1230-1530"` is a
single session.

So `bounds()` still reports the whole envelope, one window per start date, and
every window accessor keeps counting the day once. `break_bounds()` reports the
part nobody trades, and `is_open()` is the two put together.

At most one break per session, which is all any market modelled here takes, and
a session that crosses midnight may not carry one at all.

```pine
tokyo = t.session_of(t.SessionId.TSE_REGULAR)
tokyo.is_open(lunchtime_ms)          // false
not na(tokyo.bounds(d))              // true: the envelope still exists
```

On an HKEX half day the close comes in to 12:00 and the lunch break disappears
with it, which is what the exchange actually does.

## Sizing arrays

`bars_per_session(on, timeframe_ms)` counts the bars a session holds on a given
date, taking its duration from `bounds()` so a half day counts its shortened
length: 42 rather than 78 five-minute bars when the NYSE closes at 13:00. A day
the session does not run counts nothing. On a session with a break, the morning
and afternoon are rounded independently, which is what you want for a
per-session buffer on Tokyo or Hong Kong.

## Calendars are opt-in

`Session.Cal` is `na` by default and that is deliberate. A session built from
bare times says nothing about holidays, and an NYSE default would shut
`new_session("Tokyo", Zone.TOKYO, 540, 930)` on Thanksgiving and trade it
through Golden Week. Foreign exchange, and any market whose holidays this
library does not model, genuinely wants no calendar at all.

There is no separate "holiday aware" flag. A session either names a calendar or
it does not. A flag plus a calendar could hold the state "calendar off, calendar
NYSE", which is not a thing a session can be.

`EarlyClose` requires a `Cal`, since there is nothing to ask otherwise, and
`new_session` raises if you set it alone.

## One preset caveat

A preset is one set of hours, so it is wrong before an era change. `TSE_REGULAR`
uses the schedule from 5 November 2024, so earlier dates are 30 minutes off.
`HKEX_REGULAR` uses the schedule from 7 March 2011, so earlier dates open half
an hour early. `XETRA_REGULAR` carries no holiday calendar at all, because
German cash-market holidays are not modelled here, and it says so rather than
borrowing the Eurex one.

---

Previous: [Expiries](Expiries)
&nbsp;·&nbsp; Next: [Formatting and Parsing](Formatting-and-Parsing)
&nbsp;·&nbsp; Reference: [API-Session](API-Session)
&nbsp;·&nbsp; Recipes: [Recipes](Recipes)
