# Session

> Concepts first: read **[Sessions](Sessions)** before this page.

Signatures below are shown as the library declares them. From a script that imports it, every type and enum name takes your import alias: `t.DateTime`, `t.Overflow.REJECT`, `t.Exchange.NYSE`. A bare `DateTime` will not compile.

A `Session` is a recurring local-time window on selected weekdays, resolved against a real calendar. Defined that way rather than as a pair of timestamps, it survives daylight saving, holidays and half days without any of them being special-cased at the call site.

## The type

### Session

*type*

A recurring local-time window, resolved against a calendar.

| Field | Declared as | Meaning |
|---|---|---|
| `Name` | `string Name = "Session"` | Human-readable label. |
| `Tz` | `Zone Tz = Zone.NEW_YORK` | The zone the start and end times are quoted in. |
| `StartMin` | `int StartMin = 570` | Start, in minutes past local midnight. |
| `EndMin` | `int EndMin = 960` | End, in minutes past local midnight. When it is at or before StartMin the window crosses midnight and is labelled by the date it started on. |
| `DayMask` | `int DayMask = 62` | Which weekdays a session may start on, as a bit per weekday: bit 0 Sunday through bit 6 Saturday. Monday to Friday is 62. Build it with day_mask() rather than writing the number. |
| `Cal` | `Exchange Cal = na` | The exchange calendar governing holidays and half days, or na for no calendar at all, which is what foreign exchange, and any market whose holidays this library does not model, actually wants. There is no separate "holiday aware" flag: a session either names a calendar or it does not, and the pair of a flag and a calendar could hold the state "calendar off, calendar NYSE", which is not a thing a session can be. |
| `EarlyClose` | `bool EarlyClose = false` | When true the end is pulled in to the exchange's actual close on a half day. This is what makes a session box shrink correctly on the day after Thanksgiving. Requires a Cal, since there is nothing to ask otherwise. |
| `BreakStartMin` | `int BreakStartMin = na` | Start of the intraday break, in minutes past local midnight, or na for a session that trades straight through. Given with BreakEndMin or not at all. |
| `BreakEndMin` | `int BreakEndMin = na` | End of the intraday break, where trading resumes. The pair is a hole inside one window rather than a boundary between two, which is how TradingView's own session strings read it: "0900-1130,1230-1530" is a single session. So bounds() still reports the whole envelope, one window per start date, and every window accessor keeps counting the day once. Only one break per session, which is all any market modelled here takes. |

## Members

| | Summary |
|---|---|
| [`bars_per_session`](#bars_per_session) | How many chart bars of a given timeframe this session holds on a date, counting a clipped final bar as a bar. |
| [`bounds`](#bounds) | The instants this session occupies on a given start date, or na when it does not run that day. |
| [`break_bounds`](#break_bounds) | The intraday break inside this session's window on a given start date. |
| [`crosses_midnight`](#crosses_midnight) | Whether this session's window crosses local midnight. |
| [`is_first_bar`](#is_first_bar) | Whether a bar is the first bar of this session. |
| [`is_last_bar`](#is_last_bar) | Whether a bar is the last bar of this session, answered on that bar, not one bar later. |
| [`is_open`](#is_open) | Whether this session is trading at an instant. |
| [`length_minutes`](#length_minutes) | The nominal length of this session in minutes, before any half-day adjustment. |
| [`progress`](#progress) | How far through this session's envelope an instant sits. |
| [`time_to_close`](#time_to_close) | Milliseconds until this session's envelope closes. |
| [`time_to_open`](#time_to_open) | Milliseconds until this session's next open, strictly after the given instant. |
| [`to_spec`](#to_spec) | This session as a TradingView-style string, e.g. "0930-1600:23456", or "0900-1130,1230-1530:23456" when the session breaks for lunch. |
| [`window_after`](#window_after) | The next window of this session that opens strictly after an instant: the upcoming-next window. |
| [`window_at`](#window_at) | The session window containing an instant, if any. |
| [`window_before`](#window_before) | The most recent window of this session that has already ended at an instant: the completed-previous window. |
| [`window_of_bar`](#window_of_bar) | The session window a bar touches, which is not the window that contains one of the bar's edges. |
| [`windows_between`](#windows_between) | Every window of this session that intersects a span, in ascending order. |

## Reference

### bars_per_session

```pine
Session.bars_per_session(DateTime on, int timeframe_ms)
```

How many chart bars of a given timeframe this session holds on a date, counting a clipped final bar as a bar. The duration comes from bounds(), so a half day counts its shortened length (42 rather than 78 five-minute bars when the NYSE closes at 13:00), and a day the session does not run counts nothing. This is the number to size per-session drawing budgets from, e.g. against max_boxes_count = 500; sizing from fixed hours instead miscounts on the days the calendar shortens.

| Parameter | Meaning |
|---|---|
| `on` | The session's start date, as bounds() reads it: only Year, Month and Day are read. |
| `timeframe_ms` | The bar interval in milliseconds. |

**Returns** &nbsp; The bar count, or na when the session does not run that day.

**Raises** &nbsp; when timeframe_ms is not positive: a zero-width bar is not a timeframe.

### bounds

```pine
Session.bounds(DateTime on)
```

The instants this session occupies on a given start date, or na when it does not run that day. For a session that crosses midnight the end lands on the following calendar day, and that day is the one the holiday and half-day tests are asked about, because it is the day the session settles into.

| Parameter | Meaning |
|---|---|
| `on` | The session's start date. Only its Year, Month and Day are read: a session's window comes from its own times and zone, so any time of day or offset the record carries is not part of the question. |

**Returns** &nbsp; A half-open Interval of instants, or na when the session does not run..

### break_bounds

```pine
Session.break_bounds(DateTime on)
```

The intraday break inside this session's window on a given start date. The break is a hole in one window, not a gap between two: bounds() reports the whole envelope around it, and this reports the part of that envelope nobody trades. is_open() is the two put together.

| Parameter | Meaning |
|---|---|
| `on` | The session's start date, read exactly as bounds() reads it: only Year, Month and Day. |

**Returns** &nbsp; A half-open Interval, or na when the session carries no break, does not run that day, or shuts early enough that the break no longer fits inside the window..

**See also** &nbsp; [`is_open`](API-Session#is_open)

### crosses_midnight

```pine
Session.crosses_midnight()
```

Whether this session's window crosses local midnight. Derived from the times rather than stored, so it cannot disagree with them.

**Returns** &nbsp; true when the end is at or before the start..

### is_first_bar

```pine
Session.is_first_bar(int bar_open, int bar_close)
```

Whether a bar is the first bar of this session. Pass Pine's `time` and `time_close`.

| Parameter | Meaning |
|---|---|
| `bar_open` | The bar's opening time, Unix milliseconds. |
| `bar_close` | The bar's closing time, Unix milliseconds. |

**Returns** &nbsp; true when the bar contains the session open..

### is_last_bar

```pine
Session.is_last_bar(int bar_open, int bar_close)
```

Whether a bar is the last bar of this session, answered on that bar, not one bar later. Pass Pine's `time` and `time_close`. The usual Pine idiom compares this bar's session state with the previous bar's, which cannot resolve until the next bar exists; this compares the bar against a close instant computed from the calendar, so it needs no lookahead and behaves the same on historical and realtime bars. Half days are handled, because the close comes from the calendar rather than from fixed hours.

| Parameter | Meaning |
|---|---|
| `bar_open` | The bar's opening time, Unix milliseconds. |
| `bar_close` | The bar's closing time, Unix milliseconds. |

**Returns** &nbsp; true when the session's close falls inside this bar..

### is_open

```pine
Session.is_open(int unix_ms)
```

Whether this session is trading at an instant. An intraday break is not trading, so a session with a lunch answers false through it while bounds() still reports the envelope around it.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |

**Returns** &nbsp; true when inside the session and outside its break..

### length_minutes

```pine
Session.length_minutes()
```

The nominal length of this session in minutes, before any half-day adjustment.

**Returns** &nbsp; Minutes from open to close..

### progress

```pine
Session.progress(int unix_ms)
```

How far through this session's envelope an instant sits. Wall-clock, so it runs on through an intraday break instead of pausing at it: plotted, it stays monotone across lunch. Measure against traded time yourself, off break_bounds, if that is the reading you want.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |

**Returns** &nbsp; A fraction in [0, 1), or na when no window contains the instant..

**See also** &nbsp; [`break_bounds`](API-Session#break_bounds)

### time_to_close

```pine
Session.time_to_close(int unix_ms)
```

Milliseconds until this session's envelope closes. Measured through an intraday break rather than around it, for the same reason progress is wall-clock.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |

**Returns** &nbsp; Milliseconds remaining, or na when no window contains the instant..

### time_to_open

```pine
Session.time_to_open(int unix_ms, int max_days = 10)
```

Milliseconds until this session's next open, strictly after the given instant. It answers the same question whether or not the session is currently running: while it runs, the answer is the distance to the next open, not zero. Ask is_open() whether the session is open now; a zero here would make one number do two jobs, a real distance and a flag. Strictly-after matches next_trading_day and next_fomc_after. Routed through window_after, whose result this is the distance to, so the two cannot disagree.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `max_days` | How many days ahead to search. Default 10, enough to clear a holiday weekend. |

**Returns** &nbsp; Milliseconds until the next open, or na when no open falls within max_days..

**See also** &nbsp; [`is_open`](API-Session#is_open), [`next_fomc_after`](API-Functions#next_fomc_after), [`next_trading_day`](API-DateTime#next_trading_day), [`window_after`](API-Session#window_after)

### to_spec

```pine
Session.to_spec()
```

This session as a TradingView-style string, e.g. "0930-1600:23456", or "0900-1130,1230-1530:23456" when the session breaks for lunch. The format is TradingView's, so it carries exactly what TradingView's carries (the window, the break and the day mask), and not Tz, Cal or EarlyClose. Those are parameters of parse_session rather than fields of the string, so a full round-trip is parse_session(s.to_spec(), s.Tz, s.Name, s.Cal, s.EarlyClose); pass the string alone and you get the defaults, which for a US_REGULAR session means one that trades on Christmas. The string stays narrow so that it can be pasted into, or out of, a Pine session input.

**Returns** &nbsp; The session string..

**See also** &nbsp; [`parse_session`](API-Functions#parse_session)

### window_after

```pine
Session.window_after(int unix_ms, int max_days = 10)
```

The next window of this session that opens strictly after an instant: the upcoming-next window. While the session runs, the answer is the window after the running one; window_at holds the running one. This is the window time_to_open measures the distance to: that function answers when, this answers what, and the one routes through the other so they cannot disagree.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `max_days` | How many start dates ahead to search. Default 10, enough to clear a holiday weekend. |

**Returns** &nbsp; The next upcoming Interval, or na when none opens within max_days; na means only that..

**See also** &nbsp; [`time_to_open`](API-Session#time_to_open), [`window_at`](API-Session#window_at)

### window_at

```pine
Session.window_at(int unix_ms)
```

The session window containing an instant, if any. Checks the window dated that day and the one dated the day before, so a session that began the previous evening is found.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |

**Returns** &nbsp; The Interval in progress, or na when the session is not running..

### window_before

```pine
Session.window_before(int unix_ms, int max_days = 10)
```

The most recent window of this session that has already ended at an instant: the completed-previous window. While the session runs, the running window is not this answer, because it has not completed; window_at holds it. The look-back counterpart of window_after below.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. An instant exactly at a close belongs to the window it closes (the windows are half-open), so that window already counts as completed. |
| `max_days` | How many start dates back to search. Default 10, enough to clear a holiday weekend. |

**Returns** &nbsp; The completed Interval nearest before the instant, or na when none ends within max_days, the one meaning na carries here..

**See also** &nbsp; [`window_after`](API-Session#window_after), [`window_at`](API-Session#window_at)

### window_of_bar

```pine
Session.window_of_bar(int bar_open, int bar_close)
```

The session window a bar touches, which is not the window that contains one of the bar's edges. A bar can be larger than the session: a 4h bar 09:30-13:30 New York straddles the whole of a 10:00-12:00 window, and then neither edge is inside the session, so an edge probe finds nothing and the bar registers as neither the first nor the last of a session it wholly contains. Overlap is the correct test. Exported because it is the accessor is_first_bar and is_last_bar answer from, and without it a caller who gets true from is_first_bar has no way to ask what window that was: window_at is instant-keyed, so on a 1H bar 09:00-10:00 New York, whose open precedes the session open, it returns na for the very bar the predicate just flagged. Scans the same neighbourhood window_at walks plus the following day, so a bar crossing local midnight still finds the window it runs into.

| Parameter | Meaning |
|---|---|
| `bar_open` | The bar's opening time, Unix milliseconds. Pine's `time`. |
| `bar_close` | The bar's closing time, Unix milliseconds. Pine's `time_close`. |

**Returns** &nbsp; The Interval the bar overlaps, or na when the bar touches no session window..

**See also** &nbsp; [`is_first_bar`](API-Session#is_first_bar), [`is_last_bar`](API-Session#is_last_bar), [`window_at`](API-Session#window_at)

### windows_between

```pine
Session.windows_between(int from_ms, int to_ms)
```

Every window of this session that intersects a span, in ascending order. Routed through bounds(), so each window carries the same holiday and half-day treatment every other accessor here reports. Intersection is on instants, not dates: a window that crosses midnight and opened the evening before from_ms is included when it runs into the span, which is why the scan starts one start date early.

| Parameter | Meaning |
|---|---|
| `from_ms` | Start of the span, Unix milliseconds. Inclusive. |
| `to_ms` | End of the span, Unix milliseconds. Exclusive: a window beginning exactly at to_ms is not reported, and an empty span intersects nothing. |

**Returns** &nbsp; Array of Intervals, ascending by start, possibly empty.

**Raises** &nbsp; when to_ms is before from_ms, which is not a span, and when the span covers more than 20000 start dates: the same cap expiries_between draws, stated here because a caller sizing a drawing pool from this array needs the bound that caps it: at most one window per start date over a scan that begins one date early, so never more than 20002 entries.

**See also** &nbsp; [`expiries_between`](API-Functions#expiries_between)

---

[API Index](API-Index) &nbsp;·&nbsp; [Task Index](Task-Index) &nbsp;·&nbsp; [Glossary](Glossary)
