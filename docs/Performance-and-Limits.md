# Performance and Limits

Pine imposes limits that a date library of this size runs into, and this one was
shaped by them. This is the page java.time would call thread safety: not about
correctness, but about what happens when you call the wrong thing in the wrong
place.

## Compiled token budget

TradingView's publish limit is **100,256 compiled tokens**, and there is no
server-side check for it. The library compiles at roughly **92,000**, leaving
about 8,000 for the script that imports it.

That number is not an accident. String data costs two compiled tokens per
character, and the dated closure tables originally pushed the library to
**104,509**, over the cap. Re-encoding 1,227 dates as three-character base-36
day numbers saved 6,135 characters, about 12,000 tokens, and brought it under.

Practical consequences:

- An indicator importing `std_time` has a working budget of roughly 8,000
  compiled tokens. That is generous for logic and thin for large string
  literals or long `switch` chains of your own.
- The server-side syntax check does **not** enforce the token cap. Only an
  on-chart compile does, so a script that checks clean can still fail to add.
- If you are near the limit, string constants are the first place to look.

## Operations that walk

Most of the library is closed-form arithmetic. These are the ones that iterate,
with the bounds the source documents.

| Call | Walks | Bound |
|---|---|---|
| `plus_trading_days(n, ex)` | Calendar days until `n` trading days are found | `abs(n) * 2 + 30` days, then **raises** |
| `minus_trading_days(n, ex)` | Same, delegated with `-n` | Same |
| `adjusted(conv, ex)` | Outward to the nearest trading day | 30 days, then **raises** |
| `next_expiry_after(...)` | Forward for a trading day | 30 days, then **raises** |
| `trading_day_of_month()` | From the 1st of the month | Up to 31 days |
| `next_fomc_after(ms)` | Forward through the table | Up to 401 days |
| `window_before` / `window_after` | Backward or forward for a session day | `max_days`, default 10 |

The raises are deliberate. Running out means the calendar data is wrong, and
returning the cursor would give you neither the answer nor necessarily a trading
day.

## Span functions refuse rather than truncate

`holidays_between`, `expiries_between` and `windows_between` all **raise** when
the span exceeds **20,000 calendar days**, roughly 54 years. They do not return
a partial answer.

`windows_between` documents a companion bound: at most one window per start
date over a scan that begins one date early, so never more than **20,002**
entries. That number exists so you can size a drawing pool from it rather than
guessing.

Derive spans from what you are actually drawing:

```pine
// bounded by the visible range, not by the whole chart
int from_ms = chart.left_visible_bar_time
int to_ms   = chart.right_visible_bar_time
```

## Counting trading days does not walk them

This is the reason a thirty-year count is possible at all.

Asking the calendar day by day costs one full holiday-chain call per day. Over
thirty years that is about 11,000 of them, and on the tabled calendars each one
searches a table of several kilobytes. That is enough to reach Pine's per-loop
time limit, which is a runtime error rather than merely slow.

`trading_days_between` and `holidays_between` invert it. They propose the
handful of days a calendar could possibly shut on, test only those with the same
`is_holiday` every other accessor uses, and subtract from a closed-form weekday
count. In practice that tests between **3 and 16 per cent** of the days in a
span.

The proposal is deliberately generous and is allowed to be wrong in one
direction only. A day proposed that is not a holiday gets discarded by the
filter; a day never proposed would be invisible. So the anchors are a superset
over each calendar's whole modelled range, not only the years a reference
reaches.

## Calling discipline on a chart

Nothing here allocates per bar unless you ask it to, but the walkers are still
work. Three habits cover most of it:

- **Hoist what does not change.** A `Session` or an `Exchange` is configuration.
  Build it once with `var`, not on every bar.
- **Compute date-heavy things on the bars that need them.** A holiday scan for a
  table you draw once belongs under `barstate.islast`, not in the main path.
- **Do not put a walker inside a loop.** `plus_trading_days` in a loop over bars
  is the shape that reaches the per-loop time limit.

## Drawing limits are yours, not the library's

`windows_between` and `holidays_between` return arrays, and Pine caps boxes,
lines and labels at 500 each. The 20,002 bound above is what lets you size a
pool safely; the pool itself is your script's responsibility.

---

Previous: [Verification](Verification)
&nbsp;·&nbsp; Next: [Versioning and Data Currency](Versioning-and-Data-Currency)
&nbsp;·&nbsp; See also: [Scope and Limitations](Scope-and-Limitations)
