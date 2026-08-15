# Zone

> Concepts first: read **[Time Zones](Time-Zones)** before this page.

A `Zone` is a standard offset plus a daylight-saving rule, not a fixed offset. Everything that needs real zone behaviour goes through here. `DstRule` is the data a zone's rule is expressed as.

## The type

### DstRule

*type*

A daylight-saving rule, expressed as data so that adding a zone to the Zone enum is a constant rather than a new code path. It is not an escape hatch for zones the enum does not ship: no high-level entry point takes a DstRule, so one cannot be handed to unix_to_date_zone, Zone.to_unix, a Session or an Exchange. Zones outside the enum are out of scope. The one direct consumer is offset_at_rule, which computes an offset and nothing else.

| Field | Declared as | Meaning |
|---|---|---|
| `StartMonth` | `int StartMonth = 3` | Month daylight time begins, 1-12. |
| `StartDow` | `Weekday StartDow = Weekday.SUNDAY` | Weekday the transition falls on. |
| `StartNth` | `int StartNth = 2` | Which occurrence: 1 = first, -1 = last, as nth_weekday_of_month. |
| `StartAtHour` | `int StartAtHour = 2` | Local hour of the transition, read as standard time unless StartAtUTC. |
| `StartAtUTC` | `bool StartAtUTC = false` | When true, StartAtHour is UTC rather than local. The EU switches at 01:00 UTC across every member state, so its rule cannot be expressed without this flag. |
| `EndMonth` | `int EndMonth = 11` | Month daylight time ends, 1-12. When EndMonth is less than StartMonth the rule is southern-hemisphere and wraps the year boundary. |
| `EndDow` | `Weekday EndDow = Weekday.SUNDAY` | Weekday the transition falls on. |
| `EndNth` | `int EndNth = 1` | Which occurrence. |
| `EndAtHour` | `int EndAtHour = 2` | Local hour of the transition, read as daylight time unless EndAtUTC. |
| `EndAtUTC` | `bool EndAtUTC = false` | When true, EndAtHour is UTC rather than local. |
| `ShiftHours` | `float ShiftHours = 1.0` | How far the clock moves, in hours. A float, and not assumed to be 1: Lord Howe Island shifts 30 minutes. Zero means the zone has no daylight saving. |

## Members

| | Summary |
|---|---|
| [`is_ambiguous`](#is_ambiguous) | Whether a local civil time happened twice, because a fall-back transition repeated it. |
| [`is_gap`](#is_gap) | Whether a local civil time never happened, because a spring-forward transition skipped over it. |
| [`rule`](#rule) | The daylight-saving rule in force for a zone in a given year. |
| [`rules_from`](#rules_from) | The first year from which a zone's rules are modelled exactly. |
| [`std_offset`](#std_offset) | The standard, i.e. winter, offset of a zone in hours. |
| [`to_iana`](#to_iana) | The IANA identifier for a zone, e.g. "America/New_York". |
| [`to_unix`](#to_unix) | Convert a local civil time in this zone to an instant, resolving gaps and overlaps explicitly rather than silently. |

## Reference

### is_ambiguous

```pine
Zone.is_ambiguous(int Year, int Month, int Day, int Hour = 0, int Minute = 0, int Second = 0, int MS = 0)
```

Whether a local civil time happened twice, because a fall-back transition repeated it.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `Day` | Day of month, 1-31. |
| `Hour` | Hour of day, 0-23. Default 0. |
| `Minute` | Minute of hour, 0-59. Default 0. |
| `Second` | Second of minute, 0-59. Default 0. |
| `MS` | Millisecond of second, 0-999. Default 0. |

**Returns** &nbsp; true when the local time is ambiguous..

### is_gap

```pine
Zone.is_gap(int Year, int Month, int Day, int Hour = 0, int Minute = 0, int Second = 0, int MS = 0)
```

Whether a local civil time never happened, because a spring-forward transition skipped over it.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `Day` | Day of month, 1-31. |
| `Hour` | Hour of day, 0-23. Default 0. |
| `Minute` | Minute of hour, 0-59. Default 0. |
| `Second` | Second of minute, 0-59. Default 0. |
| `MS` | Millisecond of second, 0-999. Default 0. |

**Returns** &nbsp; true when the local time does not exist..

### rule

```pine
Zone.rule(int Year)
```

The daylight-saving rule in force for a zone in a given year. Rules change by legislation, so this takes a year rather than being a constant.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |

**Returns** &nbsp; The DstRule; one with ShiftHours zero when the zone does not observe daylight saving.

**Raises** &nbsp; on a Zone the switch does not handle, a library bug. A no_dst_rule() seed would instead claim that an unhandled zone observes no daylight saving.

### rules_from

```pine
Zone.rules_from()
```

The first year from which a zone's rules are modelled exactly. Before it, results are the oldest rule extrapolated backward and should not be trusted.

**Returns** &nbsp; Calendar year.

**Raises** &nbsp; on a Zone the switch does not handle, a library bug. A 1970 seed would instead assert exactness for a zone nobody has checked.

### std_offset

```pine
Zone.std_offset()
```

The standard, i.e. winter, offset of a zone in hours.

**Returns** &nbsp; Offset from UTC in hours, ignoring daylight saving.

**Raises** &nbsp; on a Zone the switch does not handle, a library bug rather than a caller one. The switch is total so a new member cannot silently read as UTC.

### to_iana

```pine
Zone.to_iana()
```

The IANA identifier for a zone, e.g. "America/New_York". This is the bridge to the built-ins: hand it to timestamp(), str.format_time() or any other Pine function that wants a timezone string. Written out rather than read off the enum's string value so that renaming a label can never silently change output.

**Returns** &nbsp; The IANA identifier.

**Raises** &nbsp; on a Zone the switch does not handle, a library bug. A silent fallback would hand a wrong timezone string on to timestamp() and str.format_time().

**See also** &nbsp; [`format_time`](API-Functions#format_time)

### to_unix

```pine
Zone.to_unix(int Year, int Month, int Day, int Hour = 0, int Minute = 0, int Second = 0, int MS = 0, Resolver res = Resolver.COMPATIBLE)
```

Convert a local civil time in this zone to an instant, resolving gaps and overlaps explicitly rather than silently. This is the zone-aware inverse of unix_to_date_zone; DateTime.to_unix is the fixed-offset one and answers a different question.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `Day` | Day of month, 1-31. |
| `Hour` | Hour of day, 0-23. Default 0. |
| `Minute` | Minute of hour, 0-59. Default 0. |
| `Second` | Second of minute, 0-59. Default 0. |
| `MS` | Millisecond of second, 0-999. Default 0. |
| `res` | How to resolve a gap or an overlap. Default COMPATIBLE, matching java.time and Temporal. |

**Returns** &nbsp; Unix timestamp in milliseconds, or na when res is REJECT and the local time is impossible or ambiguous..

**See also** &nbsp; [`unix_to_date_zone`](API-Functions#unix_to_date_zone)

## Enums

| | Summary |
|---|---|
| [`Zone`](#zone) | A time zone, meaning a standard offset plus a daylight-saving rule, not a fixed offset. |

### Zone

*enum*

A time zone, meaning a standard offset plus a daylight-saving rule, not a fixed offset. Use `z.rules_from()` to ask how far back a zone's rules are exact.

| Member | Declared as | Meaning |
|---|---|---|
| `UTC` | `UTC = "UTC"` | No offset, no daylight saving, ever. |
| `NEW_YORK` | `NEW_YORK = "America/New_York"` | America/New_York. US rules, exact from 1976. |
| `CHICAGO` | `CHICAGO = "America/Chicago"` | America/Chicago. US rules, exact from 1976. |
| `LONDON` | `LONDON = "Europe/London"` | Europe/London. EU rules, exact from 1996. |
| `FRANKFURT` | `FRANKFURT = "Europe/Berlin"` | Europe/Berlin. EU rules, exact from 1996. |
| `SYDNEY` | `SYDNEY = "Australia/Sydney"` | Australia/Sydney. Southern hemisphere, exact from 2008. |
| `TORONTO` | `TORONTO = "America/Toronto"` | America/Toronto. Shares the United States rule, and has done since 1976: the tzdb records no offset difference from New York after that year. |
| `SHANGHAI` | `SHANGHAI = "Asia/Shanghai"` | Asia/Shanghai. No daylight saving since 1991, so exact from 1992; China observed it only from 1986 to 1991. |
| `TOKYO` | `TOKYO = "Asia/Tokyo"` | Asia/Tokyo. No daylight saving since 1952. |
| `HONG_KONG` | `HONG_KONG = "Asia/Hong_Kong"` | Asia/Hong_Kong. Fixed +8; last observed daylight saving in 1979, exact from 1980. |
| `SINGAPORE` | `SINGAPORE = "Asia/Singapore"` | Asia/Singapore. Fixed +8 since 1982 (it was +7:30 before), so exact from 1982. |
| `MUMBAI` | `MUMBAI = "Asia/Kolkata"` | Asia/Kolkata. Fixed +5:30 since 1945, so exact for the whole of Unix time. |
| `DUBAI` | `DUBAI = "Asia/Dubai"` | Asia/Dubai. Fixed +4 since 1920, so exact for the whole of Unix time. |

---

[API Index](API-Index) &nbsp;·&nbsp; [Task Index](Task-Index) &nbsp;·&nbsp; [Glossary](Glossary)
