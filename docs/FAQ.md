# FAQ

**Why won't `DateTime d = ...` compile?**
Imported types take your import alias: `t.DateTime d = ...`. The error says
`"{typeKeyword}" is not a valid type keyword` and never mentions imports, which
is why this catches everyone once. Signatures on the reference pages are shown
as the library declares them, unqualified, so copying one into your own script
produces this.

**Why won't `format_time` take `syminfo.timezone`?**
It takes a `Zone`, which is checked at compile time, where `str.format_time`
takes a string that is not. A UTC default would let a ported call compile
cleanly and then silently mislabel every evening New York bar. Use
`z.to_iana()` when you need the string form for a built-in.

**Why does `next_expiry_after` raise on `ExpiryKind.VIX`?**
VIX settles at the morning opening auction, so a close-shaped `Hour` parameter
cannot name its moment. Silently ignoring the `Hour` you passed would be worse
than an error. Use `next_vix_settlement_after`.

**Why is there no `parse(str, pattern)`?**
The built-ins do not offer one either, ISO covers the formats machine-written
dates actually arrive in, and a partial implementation would fail in ways that
look like data problems. `parse_iso` returns `na` rather than guessing.

**Why is there no `is_market_open(ms, exchange)`?**
An exchange knows which *days* trade; a session knows which *minutes* do.
Answering that question needs a session anyway, so you name one:
`sess.is_open(ms)`. See [Choosing the Right Tool](Choosing-the-Right-Tool).

**`if na(k)` on a `Known` never fires. Why?**
`na(Known.UNKNOWN)` is `false`. `UNKNOWN` is a value, not `na`. Test
`k == t.Known.UNKNOWN`.

**Why does `is_holiday` say a date trades when I know it does not?**
You are probably past that calendar's horizon. `bool` has no room for "not
known", so a tabled holiday outside the window reads as an ordinary trading day.
Check `calendar_through()` and ask `closed_for_holiday()` instead.

**Why does `31 January plus one month plus one month` differ from `plus two months`?**
Clamping loses information, so applying it twice loses it twice. The first gives
28 March, the second 31 March. Both are correct answers to different questions,
and java.time behaves the same way.

**Why does `plus_trading_days(0)` not move a date off a holiday?**
Moving zero days is not a request to fix the date. `adjusted(conv, ex)` is the
one that rolls.

**Why does `trading_day_of_month` return `na` instead of 0?**
Zero would be a real ordinal. `na` means the question has no answer for that
date.

**Why does `time_to_open` not return 0 while the session is running?**
Zero is a real distance, so it cannot also be a flag. It answers the same
question either way: how far to the *next* open.

**Why did my session box not shrink on the day after Thanksgiving?**
The session needs `EarlyClose = true` and a `Cal` to read the early close from.
`new_session` raises if you set the flag without a calendar.

**Why does my custom session trade through holidays?**
`Session.Cal` defaults to `na`, deliberately. Name a calendar.

**`b.Month := 3` changed `a` as well. Why?**
Pine's user-defined types are reference types, so assignment aliases rather than
copies. Use `.copy()` or a wither. See [Value Semantics](Value-Semantics).

**Why can't I write `a == b` on two `DateTime`s?**
`==` on two UDTs is a type error in Pine, not reference equality. Use `equals()`
for field equality or `same_instant()` for the moment.

**My script checks clean but will not add to the chart.**
The server-side check does not enforce the 100,256 compiled-token cap, so that
is the usual cause. It will not be the import: a library compiles as its own
unit and does not spend your script's budget. Look at your own string constants
first, at two compiled tokens per character. See
[Performance and Limits](Performance-and-Limits).

**`holidays_between` raised on my range.**
It refuses spans over 20,000 days rather than silently truncating. Derive the
span from what you are drawing, such as the visible range.

**Is the FOMC calendar trustworthy?**
Within its window, `fomc_known_from()` to `fomc_known_through()`, it is a
transcription of the published schedule. It has no offline oracle, so it is
checked structurally: that would catch a mistyped digit or a missing meeting,
but not a meeting that moved one day and stayed a Tuesday. Outside the window it
answers `Known.UNKNOWN`.

**Does `russell_rebalance_day` handle the 29 and 30 June exception?**
No, and it says so. It implements the unmodified last-Friday-in-June rule, so it
is a week late for 2018, 2023, 2028 and 2029.

**Why is the JPX close 30 minutes early in late 2024?**
The Tokyo close moved on 2024-11-05 and the library models the close at year
granularity. It is a known, deliberate divergence, pinned in the test suite. See
[Scope and Limitations](Scope-and-Limitations).

**Can I add a time zone?**
Not from outside. `DstRule` expresses rules as data so that adding a `Zone`
member is a constant rather than a code path, but no high-level entry point
takes a `DstRule`. Zones outside the enum are out of scope.

**Are leap seconds handled?**
They do not exist in Unix time and are not modelled.

---

Previous: [Design Notes](Design-Notes)
&nbsp;·&nbsp; Up: [Home](Home)
&nbsp;·&nbsp; See also: [Pitfalls](Pitfalls)
