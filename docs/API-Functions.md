# Functions

> Concepts first: read **[Core Concepts](Core-Concepts)** before this page.

The free functions. By the library's calling convention a function that builds a date takes loose ints, and a function that takes an instant takes it first and stays a free function, so constructors, instant accessors, parsers and formatters live here rather than as methods.

## Members

| | Summary |
|---|---|
| [`changed`](#changed) | Whether a unit boundary in a zone falls between two instants: the "is this a new day?" test, answered against a real calendar instead of the chart's own session grid. |
| [`date_from_day_of_year`](#date_from_day_of_year) | Civil date for an ordinal day of the year. |
| [`date_from_iso_week`](#date_from_iso_week) | Civil date for an ISO-8601 week date. |
| [`date_to_unix`](#date_to_unix) | Convert a civil date-time to a Unix timestamp. |
| [`date_to_weekday`](#date_to_weekday) | Day of week for a civil date, derived from the same civil algorithm as every other function here. |
| [`day_count_days`](#day_count_days) | The whole-day count a convention measures between two instants: the numerator year_fraction divides, exposed because for the 30/360 family it is not recoverable from the fraction alone. |
| [`day_mask`](#day_mask) | The weekday bitmask for a contiguous run of days, from one weekday through another inclusive, wrapping past Saturday if it has to. |
| [`days_from_civil`](#days_from_civil) | Days elapsed from 1970-01-01 to a civil date. |
| [`days_in_month`](#days_in_month) | Number of days in a given month. |
| [`days_in_year`](#days_in_year) | Number of days in a given year. |
| [`dst_end`](#dst_end) | The instant daylight saving ends in a zone in a year. |
| [`dst_start`](#dst_start) | The instant daylight saving begins in a zone in a year. |
| [`easter_sunday`](#easter_sunday) | Easter Sunday, by the anonymous Gregorian computus (Meeus / Jones / Butcher). |
| [`epoch`](#epoch) | The Unix epoch, 1970-01-01T00:00:00Z. |
| [`expiries_between`](#expiries_between) | Every expiry of a cycle whose date falls in a span. |
| [`first_trading_day_of_month`](#first_trading_day_of_month) | The first trading day of a month. |
| [`fomc_known_from`](#fomc_known_from) | The first year for which the FOMC meeting table is known. |
| [`fomc_known_through`](#fomc_known_through) | The last year for which the FOMC meeting table is known. |
| [`format_duration`](#format_duration) | Format a span of milliseconds as a human-readable duration, largest unit first. |
| [`format_iso_duration`](#format_iso_duration) | A span of milliseconds in ISO-8601 duration form, e.g. "P2DT4H13M9S". |
| [`format_ixdtf`](#format_ixdtf) | Format an instant in the RFC 9557 extended format, which appends the zone in brackets so the reader knows which rules produced the offset. |
| [`format_relative`](#format_relative) | An instant described relative to another, the way a human says it: "3d 4h ago" for the past, "in 2h 15m" for the future, "now" within a second either way. |
| [`format_time`](#format_time) | Format an instant in a zone. |
| [`format_yymmdd`](#format_yymmdd) | Format a timestamp as the six-character yyMMdd date fragment used by OPRA-style option symbols, resolved in a zone you name rather than in the chart's... |
| [`good_friday`](#good_friday) | Good Friday, the Friday before Easter Sunday. |
| [`holidays_between`](#holidays_between) | Every date an exchange is closed for a holiday within a span. |
| [`is_dst`](#is_dst) | Whether daylight saving is in force in a zone at an instant. |
| [`is_leap_year`](#is_leap_year) | Whether a year is a leap year in the proleptic Gregorian calendar. |
| [`is_valid_date`](#is_valid_date) | Whether a civil moment exists, without raising. |
| [`last_trading_day_of_month`](#last_trading_day_of_month) | The last trading day of a month. |
| [`merge_intervals`](#merge_intervals) | The union of a set of intervals: overlapping or exactly abutting spans are joined and empty ones are dropped, so the result is the instants the inputs cover... |
| [`month_abbr`](#month_abbr) | The three-letter English abbreviation of a month. |
| [`month_from_name`](#month_from_name) | The month number for an English month name or three-letter abbreviation, case-insensitive. |
| [`month_name`](#month_name) | The English name of a month. |
| [`monthly_expiry`](#monthly_expiry) | Unix timestamp of a standard US equity monthly option expiry at a chosen local close time. |
| [`monthly_expiry_day`](#monthly_expiry_day) | Standard US equity monthly option expiry: the third Friday of the month, moved to the preceding Thursday when that Friday is a market holiday. |
| [`new_datetime`](#new_datetime) | Build a DateTime from civil fields. |
| [`new_interval`](#new_interval) | Build an interval from two instants, ordering them so the result is never reversed. |
| [`new_session`](#new_session) | Build a custom session. |
| [`next_expiry_after`](#next_expiry_after) | The next expiry of a close-settled cycle strictly after an instant. |
| [`next_fomc_after`](#next_fomc_after) | The instant of the next FOMC decision strictly after a given one. |
| [`next_holiday_after`](#next_holiday_after) | The next date an exchange is closed for a holiday, strictly after the date an instant falls on in that exchange's zone. |
| [`next_vix_settlement_after`](#next_vix_settlement_after) | The instant of the next VIX final settlement strictly after a given one. |
| [`now`](#now) | The current moment, in a zone. |
| [`nth_weekday_of_month`](#nth_weekday_of_month) | Day of month of the nth given weekday, following java.time's dayOfWeekInMonth semantics. |
| [`offset_at`](#offset_at) | Offset from UTC in force in a zone at an instant, daylight saving applied. |
| [`offset_at_rule`](#offset_at_rule) | Offset in force at an instant under an arbitrary rule. |
| [`parse_iso`](#parse_iso) | Parse an ISO-8601 date-time. |
| [`parse_iso_duration`](#parse_iso_duration) | Parse an ISO-8601 duration such as "P2DT4H13M9S", "PT1.5S" or "-PT10M" (the form format_iso_duration emits) into exact milliseconds, round-tripping everything that formatter can produce. |
| [`parse_iso_period`](#parse_iso_period) | Parse an ISO-8601 period such as "P1Y2M3D", "P3M", "P1W", "-P10D" or "P-1Y-2M-3D". |
| [`parse_session`](#parse_session) | Parse a TradingView-style session string such as "0930-1600" or "0930-1600:23456", where the digits after the colon are weekdays with 1 meaning Sunday. |
| [`parse_tenor`](#parse_tenor) | Parse a tenor string such as "1D", "2W", "3M" or "1Y" into a Period. |
| [`quarter`](#quarter) | Calendar quarter containing a month, or the fiscal quarter, when the fiscal year begins in some other month. |
| [`quarterly_expiry`](#quarterly_expiry) | Unix timestamp of a quarterly expiry. |
| [`russell_rebalance_day`](#russell_rebalance_day) | FTSE Russell annual reconstitution: the last Friday in June, one of the highest-volume closes of the year. |
| [`session_of`](#session_of) | One of the built-in standard sessions. |
| [`sort_intervals`](#sort_intervals) | Sort an array of intervals in place by start, ties by end, and return the same array so a call can chain. |
| [`today`](#today) | The current date at true local midnight in a zone, meaning the record's own to_unix() is the instant that midnight actually happened. |
| [`trading_days_in_month`](#trading_days_in_month) | How many trading days a month holds. |
| [`try_new_datetime`](#try_new_datetime) | Build a DateTime, returning na instead of raising when the fields do not describe a real moment. |
| [`unix_to_date`](#unix_to_date) | Convert a Unix timestamp to a civil date-time. |
| [`unix_to_date_zone`](#unix_to_date_zone) | Convert an instant to civil time in a zone, daylight saving applied. |
| [`vix_settlement`](#vix_settlement) | Unix timestamp of a VIX final settlement: the Special Opening Quotation moment, when Cboe's opening auction in the constituent SPX series prints the settlement value. |
| [`vix_settlement_day`](#vix_settlement_day) | VIX final settlement day for a contract month: the Wednesday thirty days before the following month's third Friday... |
| [`weekday_from_int`](#weekday_from_int) | Weekday for a numeric code, 0 = Sunday through 6 = Saturday. |
| [`weekday_from_name`](#weekday_from_name) | The Weekday for an English day name or three-letter abbreviation, case-insensitive. |
| [`weekday_from_pine_dow`](#weekday_from_pine_dow) | The Weekday for a value from Pine's dayofweek built-in or the dayofweek.* constants, where Sunday is 1. |
| [`year_fraction`](#year_fraction) | Year fraction between two instants under a day-count convention. |
| [`zone_from_iana`](#zone_from_iana) | The Zone for an IANA identifier, so a string from syminfo.timezone or a user input can be turned into something the rule engine understands. |
| [`zone_offset_string`](#zone_offset_string) | The offset in force in a zone at an instant, spelled the way Pine's timezone arguments accept it. |

## Reference

### changed

```pine
changed(int prev_ms, int cur_ms, TimeUnit unit, Zone z = Zone.UTC, Weekday week_start = Weekday.MONDAY)
```

Whether a unit boundary in a zone falls between two instants: the "is this a new day?" test, answered against a real calendar instead of the chart's own session grid. Pass Pine's `time[1]` and `time`. Because the boundary is resolved in a named zone, this is how you detect a new Tokyo day on a chart quoted in New York, which a bar-index comparison cannot do.

| Parameter | Meaning |
|---|---|
| `prev_ms` | The earlier instant, Unix milliseconds. Pine's `time[1]`. |
| `cur_ms` | The later instant, Unix milliseconds. Pine's `time`. |
| `unit` | The unit whose boundary is being watched. |
| `z` | The zone the boundary is resolved in. Default UTC. |
| `week_start` | Which day a week begins on, used only for TimeUnit.WEEK. Default MONDAY. |

**Returns** &nbsp; true when the two instants sit in different units. Equal instants return false, and so does an na on either side: bool cannot hold na, so there is no third answer to give; guard the first bar with nz() or a bar_index test rather than reading false as "no boundary". The repeated hour of an autumn transition is one civil hour and reports no boundary: 01:30 happens twice in London that morning, and both truncate to the same 01:00..

### date_from_day_of_year

```pine
date_from_day_of_year(int Year, int Doy)
```

Civil date for an ordinal day of the year. Inverse of day_of_year. Takes loose ints because it builds a date; see the calling convention in the header.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Doy` | Ordinal day in [1, 366]. |

**Returns** &nbsp; A DateTime at midnight UTC on that date.

**Raises** &nbsp; when Doy is outside [1, days_in_year(Year)]; a 366th day of a common year is a caller bug.

**See also** &nbsp; [`day_of_year`](API-DateTime#day_of_year), [`days_in_year`](API-Functions#days_in_year)

### date_from_iso_week

```pine
date_from_iso_week(int WeekYear, int Week, Weekday dow = Weekday.MONDAY)
```

Civil date for an ISO-8601 week date. Inverse of the iso_week / iso_week_year / Weekday.to_iso_dow triple. Takes loose ints because it builds a date.

| Parameter | Meaning |
|---|---|
| `WeekYear` | ISO week-based year. |
| `Week` | ISO week number in [1, 53]. |
| `dow` | Which day of that week. Default MONDAY, the first day of an ISO week. A Weekday rather than the raw ISO digit, so 0 and 8 are unrepresentable instead of runtime errors. |

**Returns** &nbsp; A DateTime at midnight UTC on that date.

**Raises** &nbsp; when Week is outside [1, iso_weeks_in_year(WeekYear)]: the bound is that week-year's own length, 52 or 53, not a flat 53.

**See also** &nbsp; [`iso_week_year`](API-DateTime#iso_week_year), [`to_iso_dow`](API-Weekday#to_iso_dow)

### date_to_unix

```pine
date_to_unix(int Year, int Month, int Day, int Hour = 0, int Minute = 0, int Second = 0, int MS = 0, float utc = 0.0)
```

Convert a civil date-time to a Unix timestamp. Inverse of unix_to_date.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `Day` | Day of month, 1-31. |
| `Hour` | Hour of day, 0-23. Default 0. |
| `Minute` | Minute of hour, 0-59. Default 0. |
| `Second` | Second of minute, 0-59. Default 0. |
| `MS` | Millisecond of second, 0-999. Default 0. |
| `utc` | Offset from UTC in hours that the supplied civil time is expressed in. Default 0. |

**Returns** &nbsp; Unix timestamp in milliseconds.

**Raises** &nbsp; when Hour is outside [0, 23], Minute or Second outside [0, 59], MS outside [0, 999], or when Month and Day are ones days_from_civil refuses. Like that function it does not check Day against the length of its month, so this converts 31 February rather than rejecting it; new_datetime is the validating way in.

**See also** &nbsp; [`days_from_civil`](API-Functions#days_from_civil), [`new_datetime`](API-Functions#new_datetime), [`unix_to_date`](API-Functions#unix_to_date)

### date_to_weekday

```pine
date_to_weekday(int Year, int Month, int Day)
```

Day of week for a civil date, derived from the same civil algorithm as every other function here.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `Day` | Day of month, 1-31. |

**Returns** &nbsp; The Weekday..

### day_count_days

```pine
day_count_days(int t0, int t1, DayCount basis = DayCount.ACT_365F, Exchange ex = Exchange.NYSE)
```

The whole-day count a convention measures between two instants: the numerator year_fraction divides, exposed because for the 30/360 family it is not recoverable from the fraction alone. The ACT conventions count actual civil days between the endpoints resolved in the exchange's zone; the 30/360 pair counts its flattened numerator with the same end-date rules year_fraction applies; ACT/252 counts trading days. Two caveats: year_fraction's ACT/365F and ACT/360 divide exact elapsed milliseconds rather than this whole-day count, so days over 365 reproduces the fraction only when both endpoints share a wall-clock time; and ACT/ACT ISDA has no single denominator, so its count is the actual days but no one division rebuilds the fraction.

| Parameter | Meaning |
|---|---|
| `t0` | Start instant, Unix milliseconds. |
| `t1` | End instant, Unix milliseconds. |
| `basis` | The day-count convention. Default ACT/365F. |
| `ex` | The exchange whose zone resolves the endpoints into civil dates, and whose calendar counts ACT/252. Default NYSE. |

**Returns** &nbsp; Signed day count; negative when t1 is before t0..

**See also** &nbsp; [`year_fraction`](API-Functions#year_fraction)

### day_mask

```pine
day_mask(Weekday from_dow, Weekday to_dow)
```

The weekday bitmask for a contiguous run of days, from one weekday through another inclusive, wrapping past Saturday if it has to. Every preset in this file is such a run, and this exists so that none of them, and none of your sessions, is written as a bare number nobody can read: day_mask(Weekday.MONDAY, Weekday.FRIDAY) is 62, day_mask(Weekday.SUNDAY, Weekday.FRIDAY) is 63, day_mask(Weekday.SUNDAY, Weekday.THURSDAY) is 31.

| Parameter | Meaning |
|---|---|
| `from_dow` | First weekday of the run. |
| `to_dow` | Last weekday of the run, inclusive. Equal to from_dow means a single day. |

**Returns** &nbsp; A mask in [1, 127], bit 0 Sunday through bit 6 Saturday..

### days_from_civil

```pine
days_from_civil(int Year, int Month, int Day)
```

Days elapsed from 1970-01-01 to a civil date. Hinnant's days_from_civil: exact for any proleptic Gregorian date, no loops or tables.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `Day` | Day of month, 1-31. |

**Returns** &nbsp; Signed day count relative to the Unix epoch.

**Raises** &nbsp; when Month is outside [1, 12] or Day outside [1, 31]. It does not check Day against the length of that month: this is the arithmetic floor of the library, and 31 February is caught one layer up by is_valid_date and new_datetime.

**See also** &nbsp; [`is_valid_date`](API-Functions#is_valid_date), [`new_datetime`](API-Functions#new_datetime)

### days_in_month

```pine
days_in_month(int Year, int Month)
```

Number of days in a given month.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year (needed for February). |
| `Month` | Month of year, 1-12. |

**Returns** &nbsp; 28, 29, 30 or 31.

**Raises** &nbsp; when Month is outside [1, 12]; there is no month 13 to have a length.

### days_in_year

```pine
days_in_year(int Year)
```

Number of days in a given year.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |

**Returns** &nbsp; 365, or 366 in a leap year..

### dst_end

```pine
dst_end(int Year, Zone z)
```

The instant daylight saving ends in a zone in a year. For a southern-hemisphere zone this is EARLIER in the calendar year than dst_start, because the daylight period spans the year boundary.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `z` | The zone. |

**Returns** &nbsp; Unix timestamp in milliseconds, or na when the zone has no daylight saving..

**See also** &nbsp; [`dst_start`](API-Functions#dst_start)

### dst_start

```pine
dst_start(int Year, Zone z)
```

The instant daylight saving begins in a zone in a year. There is no built-in equivalent: Pine can tell you the offset at a timestamp, but not when it changes. No `_at` suffix: in offset_at, offset_at_rule and window_at, `_at` means "the value in force at an instant", and this takes a year and returns an instant.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `z` | The zone. |

**Returns** &nbsp; Unix timestamp in milliseconds, or na when the zone has no daylight saving..

**See also** &nbsp; [`offset_at_rule`](API-Functions#offset_at_rule), [`window_at`](API-Session#window_at)

### easter_sunday

```pine
easter_sunday(int Year)
```

Easter Sunday, by the anonymous Gregorian computus (Meeus / Jones / Butcher).

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |

**Returns** &nbsp; A DateTime at midnight UTC on Easter Sunday of that year..

### epoch

```pine
epoch()
```

The Unix epoch, 1970-01-01T00:00:00Z.

**Returns** &nbsp; A DateTime at the epoch..

### expiries_between

```pine
expiries_between(int from_ms, int to_ms, ExpiryKind kind, Zone z = Zone.NEW_YORK)
```

Every expiry of a cycle whose date falls in a span. Returns dates rather than instants, which is what lets one function serve all five kinds: the a.m.-settled VIX and the close-settled equity cycles do not share an hour, but they all own a calendar day. One guarded walk routed through is_expiry_day rather than five steppers, so this function cannot disagree with the predicate it enumerates.

| Parameter | Meaning |
|---|---|
| `from_ms` | Start of the span, Unix milliseconds. Inclusive by date: an expiry on the civil date this instant falls on in z is reported, whatever the time of day. |
| `to_ms` | End of the span, Unix milliseconds. Exclusive by date: an expiry on the civil date this instant falls on is not reported. |
| `kind` | The expiry cycle to enumerate. |
| `z` | The zone the endpoints are resolved to civil dates in. Default NEW_YORK, where every cycle here is listed. |

**Returns** &nbsp; Array of DateTimes at midnight, ascending, possibly empty; an empty span holds no expiries.

**Raises** &nbsp; when to_ms is before from_ms, which is not a span, and when the span exceeds 20000 calendar days, refused outright, not silently truncated.

**See also** &nbsp; [`is_expiry_day`](API-DateTime#is_expiry_day)

### first_trading_day_of_month

```pine
first_trading_day_of_month(int Year, int Month, Exchange ex = Exchange.NYSE)
```

The first trading day of a month.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; A DateTime at midnight on that day.

**Raises** &nbsp; when Month is outside [1, 12], failing in the caller's own terms rather than from days_in_month a call deeper. RAISES when the whole month holds no trading day, which no shipped calendar can produce and therefore means the calendar is wrong.

**See also** &nbsp; [`days_in_month`](API-Functions#days_in_month)

### fomc_known_from

```pine
fomc_known_from()
```

The first year for which the FOMC meeting table is known.

**Returns** &nbsp; Calendar year of the first covered date..

### fomc_known_through

```pine
fomc_known_through()
```

The last year for which the FOMC meeting table is known. Outside the window the predicates answer Known.UNKNOWN, a value, not na. Test it as one: `if x == Known.UNKNOWN`, or gate on this year first. `if na(x)` is dead code, because na(Known.UNKNOWN) is false: the branch never runs and the UNKNOWN flows on as though it had been checked.

**Returns** &nbsp; Calendar year of the last covered date..

### format_duration

```pine
format_duration(int ms, int parts = 2)
```

Format a span of milliseconds as a human-readable duration, largest unit first. str.format_time cannot do this: it wraps past 24 hours and has no day field, so a 50-hour countdown formats as two hours. For a countdown, pass target - timenow.

| Parameter | Meaning |
|---|---|
| `ms` | The span in milliseconds; negative spans are prefixed with a minus sign. na in gives na out, rather than a string built around the word "NaN". |
| `parts` | How many units to show, 1-4. Default 2, so "2d 4h" rather than "2d 4h 13m 9s". |

**Returns** &nbsp; A string such as "2d 4h", "13m 9s" or "0s", or na when ms is na.

**Raises** &nbsp; when parts is outside [1, 4]: parts is the caller's formatting choice rather than data, so it is a bug, which is why it raises while an na span does not.

**See also** &nbsp; [`format_time`](API-Functions#format_time)

### format_iso_duration

```pine
format_iso_duration(int ms)
```

A span of milliseconds in ISO-8601 duration form, e.g. "P2DT4H13M9S". Distinct from a Period's ISO form: this is exact machine time, so it never contains years or months, which have no fixed length. Sub-second spans keep a decimal fraction on the seconds field (500 is "PT0.5S", 1500 is "PT1.5S"), so that "PT0S" is the spelling of zero and of nothing else; truncating instead would print 500 as "PT0S" and -500 as "-PT0S", which is not a duration at all.

| Parameter | Meaning |
|---|---|
| `ms` | The span in milliseconds; negative spans are prefixed with a minus sign. na in gives na out, the same guard format_duration carries and for the same reason. |

**Returns** &nbsp; The ISO-8601 duration string, or na when ms is na..

### format_ixdtf

```pine
format_ixdtf(int unix_ms, Zone z)
```

Format an instant in the RFC 9557 extended format, which appends the zone in brackets so the reader knows which rules produced the offset. This is the form the JS Temporal proposal adopted, and it survives a round trip that a bare offset does not: "+01:00" could be London in summer or Berlin in winter.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `z` | The zone to express it in. |

**Returns** &nbsp; A string of the form "YYYY-MM-DDTHH:MM:SS+HH:MM[Area/Location]"..

### format_relative

```pine
format_relative(int unix_ms, int now_ms, int parts = 2)
```

An instant described relative to another, the way a human says it: "3d 4h ago" for the past, "in 2h 15m" for the future, "now" within a second either way. A wrapper over format_duration that folds the sign into direction words, because "-2h 15m" is arithmetic rather than language. The sub-second band exists because format_duration spells anything under a second "0s", and "in 0s" is not a thing anyone says.

| Parameter | Meaning |
|---|---|
| `unix_ms` | The instant being described, Unix milliseconds. |
| `now_ms` | The instant it is measured from, typically timenow. |
| `parts` | How many units to show, 1-4, passed through to format_duration. Default 2. |

**Returns** &nbsp; A string such as "3d 4h ago", "in 2h 15m" or "now", or na when either instant is na, matching format_duration.

**Raises** &nbsp; when parts is outside [1, 4]. The check is here, not just in the delegate: the "now" branch returns before format_duration runs, and a bad parts value should fail on every call, not only once the instants drift more than a second apart.

**See also** &nbsp; [`format_duration`](API-Functions#format_duration)

### format_time

```pine
format_time(int unix_ms, string pattern, Zone z)
```

Format an instant in a zone. Takes a Zone rather than a timezone string, so it is not a drop-in for str.format_time despite the matching shape: pass syminfo.timezone here and it will not compile; a Zone is checked at compile time and a string is not. Unlike the built-in, `z` and `V` resolve to the IANA identifier and `Y` gives the true ISO week-based year.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `pattern` | The format pattern. |
| `z` | The zone to express the instant in. Required, with no default. This is the migration path from str.format_time, whose own default is the chart's timezone: a UTC default here would let a ported call compile cleanly and then silently mislabel every evening New York bar. Use z.to_iana() when you need the string form for a built-in. |

**Returns** &nbsp; The formatted string.

**Raises** &nbsp; as format does: a reserved pattern letter, or an unterminated quote.

### format_yymmdd

```pine
format_yymmdd(int unix_ms, Zone z = Zone.NEW_YORK)
```

Format a timestamp as the six-character yyMMdd date fragment used by OPRA-style option symbols, resolved in a zone you name rather than in the chart's, so changing symbol cannot change the date this prints.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `z` | The zone to resolve the date in. Default NEW_YORK, which is where OPRA quotes an expiry. A Zone rather than a fixed offset, so US daylight saving is applied by rule instead of being the caller's problem. |

**Returns** &nbsp; Six-character string, e.g. "260821"..

### good_friday

```pine
good_friday(int Year)
```

Good Friday, the Friday before Easter Sunday.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |

**Returns** &nbsp; A DateTime at midnight UTC on Good Friday of that year..

### holidays_between

```pine
holidays_between(int from_ms, int to_ms, Exchange ex = Exchange.NYSE)
```

Every date an exchange is closed for a holiday within a span. The market-calendar sibling of expiries_between, with the same date-keyed contract, and the walk routes through is_holiday, so this function cannot disagree with the predicate it enumerates. Weekends are not holidays and are not reported.

| Parameter | Meaning |
|---|---|
| `from_ms` | Start of the span, Unix milliseconds. Inclusive by date: a holiday on the civil date this instant falls on in the exchange's zone is reported, whatever the time of day. |
| `to_ms` | End of the span, Unix milliseconds. Exclusive by date: a holiday on the civil date this instant falls on is not reported. |
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; Array of DateTimes at midnight, ascending, possibly empty: CRYPTO's answer is always empty, as is any empty span's.

**Raises** &nbsp; when to_ms is before from_ms, which is not a span, and when the span exceeds 20000 calendar days, refused outright rather than silently truncated.

**See also** &nbsp; [`expiries_between`](API-Functions#expiries_between), [`is_holiday`](API-DateTime#is_holiday)

### is_dst

```pine
is_dst(int unix_ms, Zone z)
```

Whether daylight saving is in force in a zone at an instant.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `z` | The zone. |

**Returns** &nbsp; true when the offset differs from the zone's standard offset..

### is_leap_year

```pine
is_leap_year(int Year)
```

Whether a year is a leap year in the proleptic Gregorian calendar.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |

**Returns** &nbsp; true when the year has 366 days..

### is_valid_date

```pine
is_valid_date(int Year, int Month, int Day, int Hour = 0, int Minute = 0, int Second = 0, int MS = 0)
```

Whether a civil moment exists, without raising. This is the exact predicate new_datetime enforces, time-of-day fields included: the trailing parameters exist so that anything the constructor can refuse can be tested here first. The constructors raise because a wrong date is almost always a bug; use this form, or try_new_datetime, when the input is untrusted and a refusal is expected.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year. |
| `Day` | Day of month. |
| `Hour` | Hour of day, 0-23. Default 0, so a three-argument call is still a pure date question. |
| `Minute` | Minute of hour, 0-59. Default 0. |
| `Second` | Second of minute, 0-59. Default 0. |
| `MS` | Millisecond of second, 0-999. Default 0. |

**Returns** &nbsp; true when the moment is real..

**See also** &nbsp; [`try_new_datetime`](API-Functions#try_new_datetime)

### last_trading_day_of_month

```pine
last_trading_day_of_month(int Year, int Month, Exchange ex = Exchange.NYSE)
```

The last trading day of a month. The month-end anchor of turn-of-month effects and the settlement date of anything that marks on the month's final print.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; A DateTime at midnight on that day.

**Raises** &nbsp; when Month is outside [1, 12], and when the whole month holds no trading day: impossible with the shipped calendars, so it signals broken calendar data.

### merge_intervals

```pine
merge_intervals(array<Interval> intervals)
```

The union of a set of intervals: overlapping or exactly abutting spans are joined and empty ones are dropped, so the result is the instants the inputs cover, and nothing about how raggedly they covered them. The input is left untouched: the sweep runs on a copy, and every returned Interval is newly built, so mutating an input interval afterwards cannot corrupt the union.

| Parameter | Meaning |
|---|---|
| `intervals` | The intervals to merge. |

**Returns** &nbsp; A new array of non-empty, pairwise disjoint, non-abutting intervals in ascending order; empty when the input is empty or holds only empty intervals.

**Raises** &nbsp; when intervals is na.

### month_abbr

```pine
month_abbr(int Month)
```

The three-letter English abbreviation of a month.

| Parameter | Meaning |
|---|---|
| `Month` | Month of year, 1-12. |

**Returns** &nbsp; The abbreviation, e.g. "Aug"..

### month_from_name

```pine
month_from_name(string name)
```

The month number for an English month name or three-letter abbreviation, case-insensitive.

| Parameter | Meaning |
|---|---|
| `name` | The month name, e.g. "August" or "Aug". |

**Returns** &nbsp; Month in [1, 12], or na when unrecognised..

### month_name

```pine
month_name(int Month)
```

The English name of a month.

| Parameter | Meaning |
|---|---|
| `Month` | Month of year, 1-12. |

**Returns** &nbsp; The full name, e.g. "August".

**Raises** &nbsp; when Month is outside [1, 12]. The switch is seeded "December" so that arm needs no case of its own; without the bound check, a 13 would print December.

### monthly_expiry

```pine
monthly_expiry(int Year, int Month, int Hour = 16, Zone z = Zone.NEW_YORK)
```

Unix timestamp of a standard US equity monthly option expiry at a chosen local close time.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `Hour` | Local hour of the close. Default 16 (16:00 New York). |
| `z` | The zone the close time is quoted in. Default NEW_YORK. A Zone rather than a `float utc`, because the New York close follows daylight-saving rules that no single fixed offset can express; in this file `float utc` always means a fixed offset. |

**Returns** &nbsp; Unix timestamp in milliseconds, resolved through Resolver.COMPATIBLE. At the 16:00 default no US transition is reachable, so the resolver never fires..

### monthly_expiry_day

```pine
monthly_expiry_day(int Year, int Month)
```

Standard US equity monthly option expiry: the third Friday of the month, moved to the preceding Thursday when that Friday is a market holiday.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |

**Returns** &nbsp; Day of month on which the monthly contract expires..

### new_datetime

```pine
new_datetime(int Year, int Month, int Day, int Hour = 0, int Minute = 0, int Second = 0, int MS = 0, float utc = 0.0)
```

Build a DateTime from civil fields. RAISES on fields that do not describe a real moment: 31 February is neither clamped, which the caller did not ask for, nor na, which would only surface the mistake at some unrelated call site downstream. Use try_new_datetime for untrusted input, or a wither with Overflow.CONSTRAIN to clamp instead.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `Day` | Day of month, 1 to the length of that month. |
| `Hour` | Hour of day, 0-23. Default 0. |
| `Minute` | Minute of hour, 0-59. Default 0. |
| `Second` | Second of minute, 0-59. Default 0. |
| `MS` | Millisecond of second, 0-999. Default 0. |
| `utc` | Offset from UTC in hours the fields are expressed in. Default 0. |

**Returns** &nbsp; A populated DateTime.

**Raises** &nbsp; when the fields do not describe a real moment; is_valid_date is the predicate, so 31 February and hour 24 are both refused. try_new_datetime is the non-raising form.

**See also** &nbsp; [`is_valid_date`](API-Functions#is_valid_date), [`try_new_datetime`](API-Functions#try_new_datetime)

### new_interval

```pine
new_interval(int a, int b)
```

Build an interval from two instants, ordering them so the result is never reversed.

| Parameter | Meaning |
|---|---|
| `a` | One endpoint, Unix milliseconds. |
| `b` | The other endpoint, Unix milliseconds. |

**Returns** &nbsp; A half-open Interval [min, max)..

### new_session

```pine
new_session(string Name, Zone Tz, int StartMin, int EndMin, int DayMask = 62, Exchange Cal = na, bool EarlyClose = false, int BreakStartMin = na, int BreakEndMin = na)
```

Build a custom session.

| Parameter | Meaning |
|---|---|
| `Name` | Human-readable label. |
| `Tz` | The zone the times are quoted in. |
| `StartMin` | Start, minutes past local midnight. |
| `EndMin` | End, minutes past local midnight; at or before StartMin means it crosses midnight. |
| `DayMask` | Weekday bitmask, bit 0 Sunday. Default 62, which is day_mask(MONDAY, FRIDAY), spelled as a literal only because Pine requires a parameter default to be constant. |
| `Cal` | The exchange calendar, or na for none. Default na: a session built from bare times says nothing about holidays, and an NYSE default would shut new_session("Tokyo", Zone.TOKYO, 540, 930) on Thanksgiving and trade it through Golden Week. |
| `EarlyClose` | Whether to pull the end in on a half day. Default false. Raises if set without a Cal. |
| `BreakStartMin` | Start of an intraday break, minutes past local midnight, or na for none. Default na. |
| `BreakEndMin` | End of that break. Default na. Given with BreakStartMin or not at all. |

**Returns** &nbsp; The Session.

**Raises** &nbsp; on five things a Session cannot mean: StartMin or EndMin outside a day, a DayMask outside [0, 127], EarlyClose set without a Cal to read the early close from, half a break pair, and a break that is not strictly inside the window. All five are caller errors, not missing data.

### next_expiry_after

```pine
next_expiry_after(int unix_ms, int Hour = 16, Zone z = Zone.NEW_YORK, ExpiryKind kind = ExpiryKind.MONTHLY)
```

The next expiry of a close-settled cycle strictly after an instant. One function rather than one per cycle because the four equity cycles genuinely share this signature: all four settle at the close, so one Hour quotes them all. VIX does not; see kind.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `Hour` | Local hour of the close. Default 16. |
| `z` | The zone the instant is read in and the close time is quoted in. Default NEW_YORK. |
| `kind` | The expiry cycle to walk. Default MONTHLY, the classic third-Friday cycle. RAISES on ExpiryKind.VIX: VIX settles at 09:30 in the morning, an instant a close-shaped Hour cannot name, and silently ignoring the Hour would be worse than an error; use next_vix_settlement_after, which quotes the settlement moment in its own terms. |

**Returns** &nbsp; Unix timestamp in milliseconds of the next expiry of that cycle.

**Raises** &nbsp; on ExpiryKind.VIX, see kind. RAISES under DAILY when a 30-day walk finds no trading day, which only broken calendar data can cause.

### next_fomc_after

```pine
next_fomc_after(int unix_ms, int Hour = 14, Zone z = Zone.NEW_YORK)
```

The instant of the next FOMC decision strictly after a given one.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `Hour` | Local hour of the statement. Default 14, when the statement is normally released. |
| `z` | The zone the instant is read in and the statement hour is quoted in. Default NEW_YORK, which is where the Fed publishes. A parameter because the hour and the zone are one fact ("14:00 New York"), and the three other exports that pair an Hour with an instant (monthly_expiry, quarterly_expiry, next_expiry_after) take both. |

**Returns** &nbsp; Unix timestamp in milliseconds, or na when the next meeting falls outside the published window..

### next_holiday_after

```pine
next_holiday_after(int unix_ms, Exchange ex = Exchange.NYSE)
```

The next date an exchange is closed for a holiday, strictly after the date an instant falls on in that exchange's zone. Strictly after, like next_trading_day and next_fomc_after: at noon on Good Friday the answer is the next holiday, not the one in progress. Ask holiday_name what the returned date is closed for.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; A DateTime at midnight on the next holiday, or na when no holiday falls within a 400-calendar-day scan. na rather than a raise, because "no holiday ahead" is an answer and not a caller bug: CRYPTO never closes, so it always answers na, and every other shipped calendar closes at least once inside any 400-day window..

**See also** &nbsp; [`holiday_name`](API-DateTime#holiday_name), [`next_fomc_after`](API-Functions#next_fomc_after), [`next_trading_day`](API-DateTime#next_trading_day)

### next_vix_settlement_after

```pine
next_vix_settlement_after(int unix_ms, int Hour = 9, int Minute = 30, Zone z = Zone.NEW_YORK)
```

The instant of the next VIX final settlement strictly after a given one. The VIX member of the next_expiry_after family, split out because its settlement is a morning auction rather than a close; next_expiry_after's kind parameter says why one Hour default cannot serve both.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `Hour` | Local hour of the settlement moment. Default 9. |
| `Minute` | Local minute of the settlement moment. Default 30. |
| `z` | The zone the instant is read in and the settlement time is quoted in. Default NEW_YORK. |

**Returns** &nbsp; Unix timestamp in milliseconds of the next VIX settlement. The one-month step is exhaustive: a settlement lands mid-month, so the following month's is strictly ahead of any instant this month's has already passed..

**See also** &nbsp; [`next_expiry_after`](API-Functions#next_expiry_after)

### now

```pine
now(Zone z = Zone.UTC)
```

The current moment, in a zone.

| Parameter | Meaning |
|---|---|
| `z` | The zone to express it in. Default UTC. |

**Returns** &nbsp; A DateTime for now..

### nth_weekday_of_month

```pine
nth_weekday_of_month(int Year, int Month, Weekday dow, int nth)
```

Day of month of the nth given weekday, following java.time's dayOfWeekInMonth semantics.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `dow` | Weekday wanted. |
| `nth` | Positive counts from the start of the month (1 = first); negative counts back from the end (-1 = last). Zero is invalid. |

**Returns** &nbsp; Day of month, or na when that occurrence does not exist in the month (e.g. a fifth Friday that the month does not contain).

**Raises** &nbsp; when nth is 0, which names no occurrence: an invalid argument, not a missing date.

### offset_at

```pine
offset_at(int unix_ms, Zone z)
```

Offset from UTC in force in a zone at an instant, daylight saving applied.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `z` | The zone. |

**Returns** &nbsp; Offset in hours..

### offset_at_rule

```pine
offset_at_rule(int unix_ms, float std_off, DstRule dr)
```

Offset in force at an instant under an arbitrary rule. This computes an offset and nothing more; it is not a way to run the rest of the library against a zone the Zone enum does not ship, because nothing else here accepts a DstRule.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `std_off` | The zone's standard offset in hours. |
| `dr` | The daylight-saving rule. |

**Returns** &nbsp; Offset from UTC in hours at that instant..

### parse_iso

```pine
parse_iso(string s)
```

Parse an ISO-8601 date-time. Accepts more than timestamp() does: extended ("2026-08-21") and basic ("20260821") forms, week dates ("2026-W34-5"), ordinal dates ("2026-233"), an optional time after T or a space, fractional seconds, every offset spelling (Z, +05, +0530, +05:30), and an RFC 9557 bracketed zone suffix, which is read and discarded.

| Parameter | Meaning |
|---|---|
| `s` | The string to parse. |

**Returns** &nbsp; A DateTime carrying any offset found, or na when the string is not valid ISO-8601. Returns na rather than guessing..

### parse_iso_duration

```pine
parse_iso_duration(string s)
```

Parse an ISO-8601 duration such as "P2DT4H13M9S", "PT1.5S" or "-PT10M" (the form format_iso_duration emits) into exact milliseconds, round-tripping everything that formatter can produce. Years, months and weeks are refused even though ISO allows them: a duration is machine time, and those are calendar amounts whose meaning depends on a reference date: parse_iso_period reads them into a Period instead. Both "." and "," start a fraction, the same licence parse_iso grants, and fraction digits past the third are truncated the same way; the fraction is accepted on the seconds field only, the one place the formatter puts one. A leading "-" negates the whole span, as the formatter spells it; per-component signs are java.time's Duration.toString dialect, which nothing here emits, and are not read.

| Parameter | Meaning |
|---|---|
| `s` | The string to parse. |

**Returns** &nbsp; The span in milliseconds, or na when the string is not a valid date-part-free ISO duration. na and never a raise: malformed input is data rather than a caller bug, the clause every parser in this file follows..

**See also** &nbsp; [`format_iso_duration`](API-Functions#format_iso_duration), [`parse_iso_period`](API-Functions#parse_iso_period)

### parse_iso_period

```pine
parse_iso_period(string s)
```

Parse an ISO-8601 period such as "P1Y2M3D", "P3M", "P1W", "-P10D" or "P-1Y-2M-3D". Both negative forms are accepted because java.time emits per-component signs from toString but also parses a leading minus, and a parser that took only one of them would fail to read back its own output. Only the date part is accepted: a time component is not a Period, because months and hours are different kinds of quantity.

| Parameter | Meaning |
|---|---|
| `s` | The string to parse. |

**Returns** &nbsp; The Period, or na when the string is not a valid date-only ISO period. A week form becomes days: "P1W" parses as 7 days, not a fourth field, because a week is exactly seven days, unlike a month..

### parse_session

```pine
parse_session(string spec, Zone Tz, string Name = "", Exchange Cal = na, bool EarlyClose = false)
```

Parse a TradingView-style session string such as "0930-1600" or "0930-1600:23456", where the digits after the colon are weekdays with 1 meaning Sunday. A single comma in the time part marks an intraday break, as in "0900-1130,1230-1530". Recognising the format Pine users already write avoids inventing a second one.

| Parameter | Meaning |
|---|---|
| `spec` | The session string. |
| `Tz` | The zone the times are quoted in. |
| `Name` | Label for the session. Default the spec itself. |
| `Cal` | The exchange calendar, or na for none. Default na, since a bare time range says nothing about holidays. |
| `EarlyClose` | Whether to pull the end in on a half day. Default false. Raises if set without a Cal. |

**Returns** &nbsp; The Session, or na when the string is malformed or the times are not a legal clock range. "2430" and "-100" are na rather than a Session with 1470 or -60 minutes in it: this returns only Sessions new_session would have built. A string with two or more commas is na too: TradingView writes those, and this model has one break to put them in..

**See also** &nbsp; [`new_session`](API-Functions#new_session)

### parse_tenor

```pine
parse_tenor(string tenor)
```

Parse a tenor string such as "1D", "2W", "3M" or "1Y" into a Period. Case-insensitive. Rejects by returning na, like every other parser here: a parser's input is by definition untrusted, and raising would have made this the one function you cannot safely point at an input.string.

| Parameter | Meaning |
|---|---|
| `tenor` | The tenor string: an integer followed by D, W, M or Y. |

**Returns** &nbsp; The equivalent Period, or na when the string is not a tenor. A week becomes seven days; a month stays a month, because they are not the same kind of quantity..

### quarter

```pine
quarter(int Month, int fiscal_start = 1)
```

Calendar quarter containing a month, or the fiscal quarter, when the fiscal year begins in some other month.

| Parameter | Meaning |
|---|---|
| `Month` | Month of year, 1-12. |
| `fiscal_start` | Month the fiscal year begins in, 1-12. Default 1, which makes this the plain calendar quarter every internal caller relies on. Pass 4 for an April fiscal year (Japan, the UK): April answers 1 and March answers 4. Pass 10 for the US federal October year. |

**Returns** &nbsp; Quarter in [1, 4].

**Raises** &nbsp; when Month or fiscal_start is outside [1, 12]; a 13th month has no quarter.

### quarterly_expiry

```pine
quarterly_expiry(int Year, int Q, int Hour = 16, Zone z = Zone.NEW_YORK)
```

Unix timestamp of a quarterly expiry.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Q` | Quarter, 1-4. |
| `Hour` | Local hour of the close. Default 16. |
| `z` | The zone the close time is quoted in. Default NEW_YORK. Forwarded to monthly_expiry, which is the only reason a quarterly expiry could be computed in New York alone. |

**Returns** &nbsp; Unix timestamp in milliseconds.

**Raises** &nbsp; when Q is outside [1, 4]. Q is not a month: a 5 would multiply into month 15, which days_in_month refuses several calls deeper, naming a function the caller never invoked. Checking the bound here fails in the caller's own terms.

**See also** &nbsp; [`days_in_month`](API-Functions#days_in_month)

### russell_rebalance_day

```pine
russell_rebalance_day(int Year)
```

FTSE Russell annual reconstitution: the last Friday in June, one of the highest-volume closes of the year. This one is a rule, so unlike the FOMC table it answers for any year. One exception is not modelled: since 2018 FTSE Russell moves reconstitution to the preceding Friday when the last Friday falls on 29 or 30 June, so this function is a week late for such years: 2018 and 2023 realized; 2028 and 2029 come next.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |

**Returns** &nbsp; Day of month in June, by the unmodified last-Friday rule..

### session_of

```pine
session_of(SessionId id)
```

One of the built-in standard sessions.

| Parameter | Meaning |
|---|---|
| `id` | Which session. |

**Returns** &nbsp; The Session..

### sort_intervals

```pine
sort_intervals(array<Interval> intervals)
```

Sort an array of intervals in place by start, ties by end, and return the same array so a call can chain. In place because that is what array.sort does; a caller who needs the original untouched copies first. Hand-rolled because Pine's array.sort does not accept UDT arrays. Insertion sort: stable, so equal intervals keep their input order, and quadratic, which at the sizes an indicator holds does not matter.

| Parameter | Meaning |
|---|---|
| `intervals` | The intervals to sort. |

**Returns** &nbsp; The same array, now ascending by FromMS then ToMS.

**Raises** &nbsp; when intervals is na: there is no array even to return.

### today

```pine
today(Zone z)
```

The current date at true local midnight in a zone, meaning the record's own to_unix() is the instant that midnight actually happened. The second resolution matters: start_of() truncates the civil fields while holding the offset in force at the original instant, which is correct for a fixed-offset record and wrong for a zone. At 15:00 New York on 1 November 2026 the record carries -05:00, but local midnight that day was still -04:00, so the un-resolved answer would be off by an hour on both transition days in every zone that observes daylight saving.

| Parameter | Meaning |
|---|---|
| `z` | The zone to resolve the date in. Required, with no default: "today" is a different date either side of the dateline, so there is no zone this function could pick that is right for a caller who did not think about it. |

**Returns** &nbsp; A DateTime at the start of today, carrying the offset in force at that midnight..

**See also** &nbsp; [`start_of`](API-DateTime#start_of), [`to_unix`](API-Zone#to_unix)

### trading_days_in_month

```pine
trading_days_in_month(int Year, int Month, Exchange ex = Exchange.NYSE)
```

How many trading days a month holds. The monthly slice of the ACT/252 denominator, and the per-month budget number for anything drawn once per session.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; The count: 19 to 23 on the equity calendars, up to 31 under CRYPTO, where every calendar day trades.

**Raises** &nbsp; when Month is outside [1, 12].

### try_new_datetime

```pine
try_new_datetime(int Year, int Month, int Day, int Hour = 0, int Minute = 0, int Second = 0, int MS = 0, float utc = 0.0)
```

Build a DateTime, returning na instead of raising when the fields do not describe a real moment. The non-throwing counterpart of new_datetime, for input you did not write yourself. A third behaviour is also available: the withers take an Overflow and can clamp an impossible day into the month rather than refusing it.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year. |
| `Month` | Month of year, 1-12. |
| `Day` | Day of month. |
| `Hour` | Hour of day, 0-23. Default 0. |
| `Minute` | Minute of hour, 0-59. Default 0. |
| `Second` | Second of minute, 0-59. Default 0. |
| `MS` | Millisecond, 0-999. Default 0. |
| `utc` | Offset from UTC in hours. Default 0. |

**Returns** &nbsp; A DateTime, or na when the input is not a real moment..

**See also** &nbsp; [`new_datetime`](API-Functions#new_datetime)

### unix_to_date

```pine
unix_to_date(int unix_ms, float utc = 0.0)
```

Convert a Unix timestamp to a civil date-time. Inverse of date_to_unix. Hinnant's civil_from_days for the date part.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `utc` | Offset from UTC in hours to express the result in. Default 0. |

**Returns** &nbsp; A DateTime carrying the civil fields, the offset used, and the day of week..

**See also** &nbsp; [`date_to_unix`](API-Functions#date_to_unix)

### unix_to_date_zone

```pine
unix_to_date_zone(int unix_ms, Zone z)
```

Convert an instant to civil time in a zone, daylight saving applied.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `z` | The zone. |

**Returns** &nbsp; A DateTime whose UTC field carries the offset actually in force..

### vix_settlement

```pine
vix_settlement(int Year, int Month, int Hour = 9, int Minute = 30, Zone z = Zone.NEW_YORK)
```

Unix timestamp of a VIX final settlement: the Special Opening Quotation moment, when Cboe's opening auction in the constituent SPX series prints the settlement value. VIX is a.m.-settled: the default is 09:30 New York, the SPX opening auction, the same instant as Cboe's native 08:30 Chicago under both standard and daylight time, not 16:00, which is why this function does not share monthly_expiry's default. It takes a Minute because the settlement falls on the half hour; the close-settled expiries need none. Two trading facts a caller may want alongside the instant: the expiring VX future stops trading at 08:00 Chicago that morning, and the last day to trade expiring VIX options is the business day before this date.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year of the settlement. |
| `Month` | Month of the settlement, 1-12. |
| `Hour` | Local hour of the settlement moment. Default 9. |
| `Minute` | Local minute of the settlement moment. Default 30. |
| `z` | The zone the settlement time is quoted in. Default NEW_YORK, matching the convention here that US-listed expiry times are quoted in New York. |

**Returns** &nbsp; Unix timestamp in milliseconds, resolved through Resolver.COMPATIBLE. At the 09:30 default no US transition is reachable, so the resolver never fires.

**Raises** &nbsp; as vix_settlement_day does, on a Month outside [1, 12].

**See also** &nbsp; [`monthly_expiry`](API-Functions#monthly_expiry), [`vix_settlement_day`](API-Functions#vix_settlement_day)

### vix_settlement_day

```pine
vix_settlement_day(int Year, int Month)
```

VIX final settlement day for a contract month: the Wednesday thirty days before the following month's third Friday, stepped to the business day immediately preceding it when that Wednesday or that Friday is a Cboe holiday. Both holiday branches occur in practice: Good Friday on the third Friday moved 2022-03 and 2025-03 to Tuesday, Juneteenth on the computed Wednesday moved 2024-06, and Juneteenth observed on the Friday moves 2026-05. The rule reproduces every settlement on the published Cboe calendars 2021-2026, the four Tuesday exceptions included. Scheduled-holiday rules only, like monthly_expiry_day and for the same reason: the exchange knew the calendar when it listed the contract, and an unscheduled closure moves settlement by circular, which no rule predicts. The Cboe holiday set is the NYSE rule set this library already carries, Juneteenth epoch 2022 and the Saturday-observed-Friday rule included: the 2026-05 and projected 2027-05 exceptions both hang on those two details. Source: the Cboe VIX fact-sheet wording plus circular C2024051300.

| Parameter | Meaning |
|---|---|
| `Year` | Calendar year of the settlement. |
| `Month` | Month of the settlement, 1-12. Also the contract month: the anchor Friday lives in the following month, but thirty days back always lands in this one, so the walked answer cannot leave it either. |

**Returns** &nbsp; Day of month on which the VIX contract settles: mid-month, a Wednesday unless a holiday stepped it.

**Raises** &nbsp; when Month is outside [1, 12]: a 13th month would compute the third Friday of a 14th, and days_in_month would then refuse a call the caller never made. RAISES when no business day precedes the computed Wednesday within a week: a full week of consecutive mid-month closures does not happen, so this signals a broken holiday table.

**See also** &nbsp; [`days_in_month`](API-Functions#days_in_month), [`monthly_expiry_day`](API-Functions#monthly_expiry_day)

### weekday_from_int

```pine
weekday_from_int(int n)
```

Weekday for a numeric code, 0 = Sunday through 6 = Saturday.

| Parameter | Meaning |
|---|---|
| `n` | Integer code; values outside [0, 6] wrap by non-negative modulo rather than erroring, so arithmetic on codes is safe. |

**Returns** &nbsp; The corresponding Weekday..

### weekday_from_name

```pine
weekday_from_name(string name)
```

The Weekday for an English day name or three-letter abbreviation, case-insensitive.

| Parameter | Meaning |
|---|---|
| `name` | The day name, e.g. "Friday" or "Fri". |

**Returns** &nbsp; The Weekday, or na when unrecognised..

### weekday_from_pine_dow

```pine
weekday_from_pine_dow(int n)
```

The Weekday for a value from Pine's dayofweek built-in or the dayofweek.* constants, where Sunday is 1.

| Parameter | Meaning |
|---|---|
| `n` | Pine day-of-week value in [1, 7]. |

**Returns** &nbsp; The Weekday..

### year_fraction

```pine
year_fraction(int t0, int t1, DayCount basis = DayCount.ACT_365F, Exchange ex = Exchange.NYSE)
```

Year fraction between two instants under a day-count convention. ACT/365F and ACT/360 use exact elapsed milliseconds, which is what an option tenor needs; the 30/360 family and ACT/ACT are bond conventions evaluated on civil dates; ACT/252 counts trading days on the given exchange.

| Parameter | Meaning |
|---|---|
| `t0` | Start instant, Unix milliseconds. |
| `t1` | End instant, Unix milliseconds. |
| `basis` | The day-count convention. Default ACT/365F. |
| `ex` | The exchange this tenor is measured in: its calendar for ACT/252, and its clock for every convention that counts days rather than milliseconds. Default NYSE. ACT/365F and ACT/360 are pure elapsed milliseconds and ignore it entirely. Under CRYPTO, ACT/252 counts every calendar day: see the DayCount notes; the convention crypto actually uses is ACT/365F. |

**Returns** &nbsp; Year fraction; negative when t1 is before t0..

### zone_from_iana

```pine
zone_from_iana(string name)
```

The Zone for an IANA identifier, so a string from syminfo.timezone or a user input can be turned into something the rule engine understands.

| Parameter | Meaning |
|---|---|
| `name` | The IANA identifier, e.g. "America/New_York". Case-sensitive. |

**Returns** &nbsp; The Zone, or na when the identifier is not one this library models. na means "not modelled", not UTC..

### zone_offset_string

```pine
zone_offset_string(int unix_ms, Zone z)
```

The offset in force in a zone at an instant, spelled the way Pine's timezone arguments accept it. Useful when a built-in needs a fixed offset rather than a zone name.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |
| `z` | The zone. |

**Returns** &nbsp; A string such as "UTC-04:00"..

---

[API Index](API-Index) &nbsp;·&nbsp; [Task Index](Task-Index) &nbsp;·&nbsp; [Glossary](Glossary)
