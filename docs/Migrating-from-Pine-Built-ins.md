# Migrating from Pine Built-ins

What each built-in becomes, and what you get for the change. Nothing here is
deprecated: Pine's own functions are fine for what they do, and this page is
about the cases where they answer only half the question.

## The mapping

| Built-in | `std_time` | What changes |
|---|---|---|
| `dayofweek` | `d.weekday()` | A `Weekday` enum instead of an int, so 0-versus-1 confusion cannot compile |
| `dayofweek.monday` | `t.Weekday.MONDAY` | Same, and `to_pine_dow()` converts back |
| `timestamp(tz, y, m, d, h, mi)` | `z.to_unix(y, m, d, h, mi)` | Gaps and overlaps are resolved explicitly rather than silently |
| `str.format_time(ms, f, tz)` | `t.format_time(ms, f, z)` | A `Zone` checked at compile time, and a real ISO week-year `Y` |
| `time(tf, session)` | `sess.is_open(ms)` | Holidays, half days and lunch breaks honoured |
| session state change | `sess.is_last_bar(time, time_close)` | Fires on the closing bar, not one bar later |
| `ta.change(time("D"))` | `t.changed(time[1], time, t.TimeUnit.DAY, z)` | A real civil day boundary in a named zone |
| hand-rolled holiday list | `d.is_trading_day(ex)` | Twelve calendars, observance shifts, named closures |
| `year`, `month`, `dayofmonth` | `d.Year`, `d.Month`, `d.Day` | Fields of one record you can also do arithmetic on |

## Day of week

```pine
//@version=6
indicator("dow", overlay = false)
import The_Peaceful_Lizard/std_time/1 as t

t.DateTime d = t.unix_to_date_zone(time, t.Zone.NEW_YORK)

bool friday_new  = d.weekday() == t.Weekday.FRIDAY
bool friday_old  = dayofweek == dayofweek.friday
int  back_to_pine = d.weekday().to_pine_dow()

plot(friday_new == friday_old ? 1 : 0)
plot(back_to_pine)
```

Three numbering schemes meet here and none agree: this library counts Sunday as
0, ISO counts Monday as 1, Pine counts Sunday as 1. `to_int`, `to_iso_dow` and
`to_pine_dow` are the three ways out, and the enum means you rarely need any of
them.

## Building an instant from civil fields

```pine
//@version=6
indicator("timestamp", overlay = false)
import The_Peaceful_Lizard/std_time/1 as t

int old_way = timestamp("America/New_York", 2025, 3, 9, 2, 30)
int new_way = t.Zone.NEW_YORK.to_unix(2025, 3, 9, 2, 30)
int refused = t.Zone.NEW_YORK.to_unix(2025, 3, 9, 2, 30, 0, 0, t.Resolver.REJECT)

plot(old_way)
plot(new_way)
plot(refused)
```

02:30 on 9 March 2025 never happened in New York. The built-in gives you
something anyway. `Resolver.REJECT` returns `na` so you find out, and
`is_gap`/`is_ambiguous` tell you which of the two problems it was.

## Formatting

```pine
//@version=6
indicator("format", overlay = false)
import The_Peaceful_Lizard/std_time/1 as t

string a = str.format_time(time, "yyyy-MM-dd", t.Zone.TOKYO.to_iana())
string b = t.format_time(time, "yyyy-MM-dd", t.Zone.TOKYO)
string c = t.format_time(time, "YYYY-'W'ww", t.Zone.TOKYO)

plot(str.length(a) + str.length(b) + str.length(c))
```

`format_time` takes a `Zone`, not a string, so `syminfo.timezone` will not
compile into it. That is deliberate: a string typo is a runtime surprise, and a
UTC default would silently mislabel every evening New York bar. Use
`z.to_iana()` when you genuinely want the built-in, as in `a`.

`Y` is the ISO week-based year, which `str.format_time` does not offer.

## Session membership

```pine
//@version=6
indicator("session", overlay = true)
import The_Peaceful_Lizard/std_time/1 as t

var t.Session sess = t.session_of(t.SessionId.US_REGULAR)

bool in_new = sess.is_open(time)
bool in_old = not na(time("1", "0930-1600", "America/New_York"))

bgcolor(in_new ? color.new(color.green, 90) : na)
plot(in_new == in_old ? 0 : 1)
```

The two agree on ordinary days. They part company on Thanksgiving, when the
built-in session string still reports a session, and on the day after, when it
reports one until 16:00 though the market shut at 13:00.

## New day in another zone

```pine
//@version=6
indicator("boundary", overlay = false)
import The_Peaceful_Lizard/std_time/1 as t

bool new_tokyo = t.changed(time[1], time, t.TimeUnit.DAY, t.Zone.TOKYO)
bool new_ny    = t.changed(time[1], time, t.TimeUnit.DAY, t.Zone.NEW_YORK)
bool new_week  = t.changed(time[1], time, t.TimeUnit.WEEK, t.Zone.LONDON, t.Weekday.MONDAY)

plot(new_tokyo ? 1 : 0)
plot(new_ny ? 2 : 0)
plot(new_week ? 3 : 0)
```

`changed` compares civil fields, so a daylight-saving transition does not read as
a boundary. It returns `false` rather than `na` when either side is `na`, so
guard bar one if that matters.

## Things to expect while porting

- **Every imported type takes your alias.** `t.DateTime`, not `DateTime`. The
  error message does not mention imports.
- **`plus_days` is not `plus_hours(24)`.** Pick by what you meant. See
  [Civil and Exact Arithmetic](Civil-and-Exact-Arithmetic).
- **Assignment aliases.** `t.DateTime b = a` does not copy. See
  [Value Semantics](Value-Semantics).
- **You have about 8,000 compiled tokens** left after the import. See
  [Performance and Limits](Performance-and-Limits).

---

Previous: [Recipes](Recipes)
&nbsp;·&nbsp; Up: [Home](Home)
&nbsp;·&nbsp; See also: [Pitfalls](Pitfalls)
