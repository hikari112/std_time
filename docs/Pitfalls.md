# Pitfalls

Traps that produce a plausible wrong answer rather than an error. Each one is
documented at its own definition in the source; collected here they become
something you can check against.

## 1. `na()` on a `Known` is dead code

```pine
Known k = d.closed_for_holiday(t.Exchange.SSE)
if na(k)        // never true. na(Known.UNKNOWN) is false.
    handle_unknown()
```

The branch never runs and the `UNKNOWN` flows onward as though it had been
checked. Test against the enum:

```pine
if k == t.Known.UNKNOWN
```

`is_yes()` collapses the three values to a bool by reading `UNKNOWN` as false,
which is only safe once you have checked coverage.

## 2. `is_holiday` past a calendar's horizon

`bool` cannot hold `na`, so past `calendar_through()` a tabled holiday reads as
an ordinary trading day. Not missing: wrong.

Affected calendars: `SSE`, `BSE` and `SGX` past 2026, `HKEX` past 2049, `JPX`
past 2099. Ask `closed_for_holiday()` there instead. See
[Exchange Calendars](Exchange-Calendars).

## 3. `plus_days(1)` and `plus_ms(MS_DAY)` differ twice a year

Civil arithmetic preserves wall-clock time; exact arithmetic preserves elapsed
time. On a daylight-saving Sunday the civil day is 23 or 25 hours long, so the
two give answers an hour apart. Pick by what you meant:
[Civil and Exact Arithmetic](Civil-and-Exact-Arithmetic).

## 4. `Y` is not `y`

`y` is the calendar year. `Y` is the ISO week-based year. They disagree for a
few days each January, which is what makes `"YYYY-MM-dd"` written for
`"yyyy-MM-dd"` such a well-camouflaged bug: it is right for about 360 days a
year.

```pine
d = t.new_datetime(2027, 1, 1)
d.format("yyyy")     // "2027"
d.format("YYYY")     // "2026", because 1 January 2027 is in ISO week 53 of 2026
```

## 5. `DateTime b = a` aliases

Pine's UDTs are reference types, so `b.Month := 3` changes `a` too. Use
`.copy()` or a wither. Full treatment on [Value Semantics](Value-Semantics).

## 6. Setting a field directly can build an impossible date

`d.Month := 2` on a 31st leaves the record holding 31 February, which
`new_datetime` would have refused, and every adjuster downstream inherits it.
`normalized()` repairs it.

## 7. A `Session` with no `Cal` trades through every holiday

That is the default and it is deliberate, but it means this session works
through Thanksgiving in silence:

```pine
sess = t.new_session("mine", t.Zone.NEW_YORK, 570, 960)   // Cal is na
```

Name a calendar when you want holidays honoured, and set `EarlyClose` when you
want half days to shorten the box.

## 8. `DateTime.to_unix` and `Zone.to_unix` are different questions

The first reads the fixed offset the record carries. The second reads civil
fields as local time in a zone and consults the rules. Using the first with a
hand-set `UTC` field is how a New York evening bar ends up an hour out in July.

## 9. `format_time` will not take `syminfo.timezone`

It takes a `Zone`, checked at compile time, where `str.format_time` takes a
string that is not. This is deliberate: a UTC default would let a ported call
compile cleanly and then silently mislabel every evening New York bar. Use
`z.to_iana()` when you need the string form for a built-in.

## 10. Reserved pattern letters raise

`L B F W O p x g n N c q` are real `DateTimeFormatter` fields this library does
not implement. Printing them back as literal text would look like an answer, so
they raise instead. Single-quote any you want literally.

## 11. Span functions refuse rather than truncate

`holidays_between`, `expiries_between` and `windows_between` raise past a
20,000-day span. They do not silently return a partial answer. Derive the span
from the visible range rather than passing the whole chart.

## 12. `trading_day_of_month` returns `na`, not 0, on a non-trading day

`na` means the question has no answer for that date. Zero would be a real
ordinal.

## 13. `russell_rebalance_day` is a week late in four known years

It implements the unmodified last-Friday-in-June rule. Since 2018 FTSE Russell
moves reconstitution to the preceding Friday when the last Friday falls on 29 or
30 June. That affects 2018 and 2023, and will affect 2028 and 2029. The function
does not model the exception and says so.

## 14. `next_expiry_after` raises on `ExpiryKind.VIX`

VIX settles in the morning auction, so a close-shaped `Hour` parameter cannot
name its moment. Use `next_vix_settlement_after` instead. The raise exists
because silently ignoring the `Hour` would be worse.

## 15. `changed()` returns `false` on the first bar

`na` on either side gives `false`, not `na`, because `bool` cannot hold `na`.
Guard bar one with `bar_index` or `nz()` rather than reading `false` as "no
boundary".

## 16. `ACT/252` under `CRYPTO` is not a crypto convention

Every calendar day is a trading day under `CRYPTO`, so `ACT/252` degenerates to
actual days over 252, a denominator no crypto desk uses. Crypto tenors are
`ACT/365F`.

---

Previous: [Choosing the Right Tool](Choosing-the-Right-Tool)
&nbsp;·&nbsp; Up: [Home](Home)
&nbsp;·&nbsp; See also: [Error Model](Error-Model), [FAQ](FAQ)
