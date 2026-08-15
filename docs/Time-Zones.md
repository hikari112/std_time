# Time Zones

Pine's built-ins can tell you the offset at an instant. Nothing built in can
tell you *when a transition happens*. That is what this part of the library is
for.

## An offset is not a zone

A `DateTime` carries a `float UTC` field. That is a fixed offset, and it is
inert: store `-5` in March and the record still says `-5` in July. In java.time
terms a `DateTime` is an `OffsetDateTime`, and the library is consistent about
this. Throughout, `float utc` always means a fixed offset, and anything that
follows a daylight-saving rule is always a `Zone`.

The consequence shows up as two conversion functions rather than one with a
flag:

```pine
d.to_unix()                                    // reads the offset the record carries
t.Zone.NEW_YORK.to_unix(2025, 3, 9, 2, 30)     // reads civil fields as local in a zone
```

They answer different questions. The first is arithmetic on a record. The second
has to consult the rules, and can discover that the moment you asked about does
not exist.

## The thirteen zones, and how far back each is exact

Zones model rules, not history. Each declares the first year its rules are
exact through `rules_from()`. Before that year the oldest known rule is
extrapolated backward, and should not be trusted.

| Zone | IANA | Exact from | Note |
|---|---|---|---|
| `UTC` | UTC | 1970 | No offset, no daylight saving, ever |
| `NEW_YORK` | America/New_York | 1976 | US rule, era-aware |
| `CHICAGO` | America/Chicago | 1976 | US rule, era-aware |
| `TORONTO` | America/Toronto | 1976 | Shares the US rule; tzdb records no difference from New York after 1976 |
| `LONDON` | Europe/London | 1996 | EU rule, harmonised |
| `FRANKFURT` | Europe/Berlin | 1996 | EU rule, harmonised |
| `SYDNEY` | Australia/Sydney | 2008 | Southern hemisphere, rule wraps the year |
| `SHANGHAI` | Asia/Shanghai | 1992 | China observed DST only 1986 to 1991 |
| `TOKYO` | Asia/Tokyo | 1970 | No daylight saving since 1952 |
| `HONG_KONG` | Asia/Hong_Kong | 1980 | Fixed +8; last observed DST in 1979 |
| `SINGAPORE` | Asia/Singapore | 1982 | Fixed +8; was +7:30 before |
| `MUMBAI` | Asia/Kolkata | 1970 | Fixed +5:30 since 1945 |
| `DUBAI` | Asia/Dubai | 1970 | Fixed +4 since 1920 |

The US rule is era-aware in three bands: the Energy Policy Act rule from 2007,
the 1987 to 2006 rule, and the 1976 to 1986 rule before that. The EU rule
switches at 01:00 UTC across every member state, which is why `DstRule` carries
an `AtUTC` flag: the union changes at the same *instant*, not the same local
time.

## Gaps and overlaps

Twice a year a local time is not a well-posed question.

**A gap** is spring forward. 02:30 on the second Sunday in March simply never
happened in New York; the clock went from 01:59:59 to 03:00:00.

**An overlap** is fall back. 01:30 on the first Sunday in November happened
twice, an hour apart.

A fixed-offset `DateTime` cannot express either, which is precisely why
`Zone.to_unix` is a separate function that takes a `Resolver`. You can also ask
directly:

```pine
t.Zone.NEW_YORK.is_gap(2025, 3, 9, 2, 30)         // true: never happened
t.Zone.NEW_YORK.is_ambiguous(2025, 11, 2, 1, 30)  // true: happened twice
```

## Resolvers

`Resolver` is named for Noda Time's `ZoneLocalMappingResolver` and Temporal's
`disambiguation` option.

| Resolver | In a gap | In an overlap |
|---|---|---|
| `COMPATIBLE` | Shift forward by the gap length | Take the earlier instant |
| `EARLIER` | Shift backward out of the gap | Take the earlier instant |
| `LATER` | Shift forward out of the gap | Take the later instant |
| `REJECT` | `na` | `na` |

`COMPATIBLE` is the default and matches java.time and Temporal. Use `REJECT`
when the civil time came from user input and you would rather find out that it
was impossible than silently accept a shifted answer:

```pine
int ms = t.Zone.NEW_YORK.to_unix(y, m, d, hh, mm, 0, 0, t.Resolver.REJECT)
if na(ms)
    // ask is_gap / is_ambiguous to tell the user which one it was
```

## Finding the transitions themselves

```pine
int  springs = t.dst_start(2025, t.Zone.NEW_YORK)  // the instant clocks go forward
int  falls   = t.dst_end(2025, t.Zone.NEW_YORK)    // the instant they go back
bool summer  = t.is_dst(time, t.Zone.NEW_YORK)     // was daylight time in force
float off    = t.offset_at(time, t.Zone.LONDON)    // the offset in force, in hours
```

`zone_offset_string(ms, z)` gives the offset in the spelling Pine's own timezone
arguments accept, and `z.to_iana()` gives the identifier string, which is the
bridge back to the built-ins.

## Detecting a new day, week or month in any zone

`changed()` is the zone-aware boundary test, and it is the reason you do not
need the chart's own session grid to know when a day rolled over somewhere else:

```pine
bool new_tokyo_day = t.changed(time[1], time, t.TimeUnit.DAY, t.Zone.TOKYO)
```

It compares civil fields only, deliberately. Across a daylight-saving transition
the two records name the same local boundary while carrying different offsets,
and both `equals()` and an instant comparison would read that as a change.

`na` on either side returns `false`, not `na`, because `bool` cannot hold `na`.
Guard the first bar.

## Adding a zone is out of scope

`DstRule` expresses a rule as data so that adding a member to the `Zone` enum is
a constant rather than a new code path. It is not an escape hatch: no high-level
entry point takes a `DstRule`, so one cannot be handed to `unix_to_date_zone`,
`Zone.to_unix`, a `Session` or an `Exchange`. The single direct consumer is
`offset_at_rule`, which computes an offset and nothing else.

---

Previous: [Error Model](Error-Model)
&nbsp;·&nbsp; Next: [Exchange Calendars](Exchange-Calendars)
&nbsp;·&nbsp; Reference: [API-Zone](API-Zone)
