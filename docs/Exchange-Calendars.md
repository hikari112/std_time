# Exchange Calendars

Twelve calendars. They are not variations of one calendar: CME closes on three
days a year and trades the other US federal holidays on a shortened session,
while the LSE runs on UK bank holidays that share only Good Friday and Christmas
with the NYSE.

## Rules where a rule exists, a table where none does

Most holidays follow a statute. Thanksgiving is the fourth Thursday in November,
and that is true for every year, past or future, so it is computed.

Unscheduled closures are not derivable from anything. A hurricane, a blackout, a
state funeral. Those live in a dated table, and a table is complete only for the
past. This is why `is_holiday` must never be read as "and nothing else can close
the market".

Every closure is named, and the name is the source of truth: `is_holiday` is
defined as `holiday_name` being non-`na`, so a date cannot be closed and
nameless, or named and open.

```pine
d = t.new_datetime(2012, 10, 30)
d.holiday_name(t.Exchange.NYSE)    // "Hurricane Sandy"
d.is_holiday(t.Exchange.NYSE)      // true
d.holiday_name(t.Exchange.CME)     // na: CME traded through it
```

## The twelve

Hours are local to the exchange's own zone. "Exact from" and "exact through" are
what `calendar_from()` and `calendar_through()` return; `na` through means a
rule-driven calendar with no horizon.

| Calendar | Zone | Hours | Lunch | Early close | Exact from | Exact through |
|---|---|---|---|---|---|---|
| `NYSE` | New York | 09:30-16:00 | none | 13:00 | 1976 | no horizon |
| `LSE` | London | 08:00-16:30 | none | 12:30 | 1976 | no horizon |
| `CME` | Chicago | 17:00 prev day to 16:00 | none | 12:00 | 2000 | no horizon |
| `JPX` | Tokyo | 09:00-15:30 | 11:30-12:30 | none | 2000 | 2099 |
| `EUREX` | Berlin | 08:00-22:00 | none | none | 2006 | no horizon |
| `HKEX` | Hong Kong | 09:30-16:00 | 12:00-13:00 | 12:00 | 2000 | 2049 |
| `ASX` | Sydney | 10:00-16:00 | none | 14:10 | 1995 | no horizon |
| `TSX` | Toronto | 09:30-16:00 | none | 13:00 | 1995 | no horizon |
| `SSE` | Shanghai | 09:30-15:00 | 11:30-13:00 | none | 2006 | 2026 |
| `BSE` | Mumbai | 09:15-15:30 | none | none | 2006 | 2026 |
| `SGX` | Singapore | 09:00-17:00 | none | none | 2006 | 2026 |
| `CRYPTO` | UTC | 00:00-24:00 | none | none | no bound | no horizon |

### Notes that matter per calendar

**NYSE.** Juneteenth from 2022. Unscheduled closures named individually,
including four days after the September 11 attacks, two for Hurricane Sandy, and
five national days of mourning. Election Day appears twice, in 1976 and 1980,
because the exchange observed it until 1980 and then stopped.

**LSE.** Bank holidays with substitute Mondays, plus one-off royal closures:
jubilees, two royal weddings, the 2022 state funeral and the 2023 coronation. In
several of those years the spring bank holiday also moved, so the moved-away
dates are recorded as open.

**CME.** The Globex equity-index schedule. Closes on three holidays a year and
trades the rest on a shortened session. Its unscheduled closures are a different
set from the NYSE's: CME traded through Hurricane Sandy. September 2001 they
share, but for different lengths, because the equity-index complex did not
resume until the 17th.

**JPX.** Closed 31 December through 3 January, no half days. Carries the Happy
Monday moves, the sandwich rule, and substitute chains. Equinox holidays use the
standard 1980-2099 approximation, which is why the horizon is 2099.

**EUREX.** The derivatives calendar, TARGET2-shaped. The German cash market
(Xetra) keeps different hours and more holidays and is not this calendar.

**HKEX.** Lunar festivals are tabled rather than computed, hence the 2049
horizon. Half days at 12:00 on Christmas Eve, New Year's Eve and Lunar New
Year's Eve, and on a half day the lunch break disappears with the close.
Typhoon and black-rainstorm closures are recorded, named "Severe weather
closure".

**ASX.** New South Wales holidays: no Labour Day, and ANZAC Day does not move
off a weekend. Half days at 14:10 before Christmas and New Year.

**TSX.** Christmas Eve half day only, at 13:00, and only when 24 December is
itself a session. No Easter Monday. Family Day exists only from 2008.

**SSE.** Wholly tabled. State Council holiday blocks have changed length three
times in twenty years, so nothing extrapolates them.

**BSE.** Six fixed dates with no substitution at all, the rest tabled. The two
Saturdays the exchange traded as special sessions are recorded. The Diwali
Muhurat evening session is not modelled.

**SGX.** Four fixed dates with a Sunday-only substitute, the rest tabled.

**CRYPTO.** Every calendar day trades, weekends included. There is nothing to
check and no horizon to state.

## Horizons, and why `is_holiday` is not enough

A tabled calendar stops where its data stops. Past that point `is_holiday`
cannot help you, because Pine's `bool` has no room for "not known" and will read
a tabled holiday as an ordinary trading day. That is a wrong answer, not a
missing one.

`closed_for_holiday()` returns `Known` instead:

```pine
d = t.new_datetime(2030, 10, 1)
d.is_holiday(t.Exchange.SSE)            // false, and not to be trusted: past 2026
d.closed_for_holiday(t.Exchange.SSE)    // Known.UNKNOWN
```

The safe shape is to check coverage first:

```pine
int through = t.Exchange.SSE.calendar_through()
if not na(through) and d.Year > through
    // outside the table; do not present an answer as certain
```

`Known.UNKNOWN` is a value, not `na`. `if na(k)` is dead code. See
[Error Model](Error-Model).

## Three known divergences from the reference data

Each of these is deliberate, and pinned in the test suite in both directions so
it fails if it grows *or* silently disappears.

**JPX, 5 November to 30 December 2024.** The Tokyo close moved from 15:00 to
15:30 on 2024-11-05. The library models the close at year granularity, so every
session in that window closes 30 minutes early. Chosen as the smaller error than
applying the new close to all of 2024.

**HKEX, early 2011.** The open moved from 10:00 to 09:30 on 2011-03-07. Same
year-granular gate, so 43 sessions before that date open half an hour early.

**CME sessions.** The library models Globex equity index as 17:00 the previous
day to 16:00 Chicago. `exchange_calendars` labels the same session 17:00 to
17:00, so the closes differ by exactly one hour by construction. The library
also closes the four days after 11 September 2001 that the reference trades;
that one is a gap in the reference, not an error here.

---

Previous: [Time Zones](Time-Zones)
&nbsp;·&nbsp; Next: [Trading Days and Day Counts](Trading-Days-and-Day-Counts)
&nbsp;·&nbsp; Reference: [API-Exchange](API-Exchange)
&nbsp;·&nbsp; See also: [Scope and Limitations](Scope-and-Limitations)
