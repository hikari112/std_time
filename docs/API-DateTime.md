# DateTime

> Concepts first: read **[Core Concepts](Core-Concepts)** before this page.

`DateTime` is a civil date-time carrying a fixed offset, java.time's `OffsetDateTime`, not its `ZonedDateTime`. It records what a clock read and how far that clock sat from UTC. It does not know a zone's rules, so an offset stored in March is still that offset in July.

## The type

### DateTime

*type*

A civil date-time held together with the fixed UTC offset it is expressed in. This is java.time's OffsetDateTime: a local civil time plus an offset, not a zone.

| Field | Declared as | Meaning |
|---|---|---|
| `Year` | `int Year = 1970` | Calendar year, proleptic Gregorian. |
| `Month` | `int Month = 1` | Month of year, 1-12. |
| `Day` | `int Day = 1` | Day of month, 1-31. |
| `Hour` | `int Hour = 0` | Hour of day, 0-23. |
| `Minute` | `int Minute = 0` | Minute of hour, 0-59. |
| `Second` | `int Second = 0` | Second of minute, 0-59. |
| `MS` | `int MS = 0` | Millisecond of second, 0-999. |
| `UTC` | `float UTC = 0.0` | Offset from UTC in hours that this civil time is expressed in. A float because real offsets are not all whole hours: India is +5:30, Nepal +5:45, the Chatham Islands +12:45. |

## Members

| | Summary |
|---|---|
| [`adjusted`](#adjusted) | Roll a date onto a trading day using an ISDA business-day convention. |
| [`clamp_to`](#clamp_to) | This instant confined to a range: lo when earlier than lo, hi when later than hi, otherwise itself. |
| [`closed_for_holiday`](#closed_for_holiday) | Whether an exchange is shut for a holiday, as a three-valued answer that says so when the question falls outside the calendar's range. |
| [`compare`](#compare) | Compare two date-times as instants, so differing offsets compare correctly. |
| [`day_of_year`](#day_of_year) | Day of the year, 1 for 1 January. |
| [`days_between`](#days_between) | Whole calendar days from this date to another, ignoring time of day. |
| [`earlier`](#earlier) | The earlier of two date-times, as instants. |
| [`end_of`](#end_of) | The last instant of the unit containing this date-time, i.e. one millisecond before the next unit begins. |
| [`equals`](#equals) | Whether two date-times denote the same civil fields and the same offset. |
| [`fomc_day`](#fomc_day) | Whether a date falls on either day of a scheduled FOMC meeting. |
| [`fomc_decision_day`](#fomc_decision_day) | Whether a date is the second day of an FOMC meeting, when the statement is released. |
| [`format`](#format) | Format this date-time with a pattern. |
| [`holiday_name`](#holiday_name) | The name of the holiday or closure shutting an exchange on a date. |
| [`is_after`](#is_after) | Whether this date-time is strictly later than another, as instants. |
| [`is_before`](#is_before) | Whether this date-time is strictly earlier than another, as instants. |
| [`is_between`](#is_between) | Whether this instant falls in the half-open span [lo, hi). |
| [`is_early_close`](#is_early_close) | Whether an exchange closes early on a date. |
| [`is_expiry_day`](#is_expiry_day) | Whether a date is an expiry of a given cycle. |
| [`is_holiday`](#is_holiday) | Whether an exchange is closed for a scheduled holiday. |
| [`is_leap`](#is_leap) | Whether this date's year is a leap year. |
| [`is_month_end`](#is_month_end) | Whether this is the last day of its month. |
| [`is_month_start`](#is_month_start) | Whether this is the first day of its month. |
| [`is_quarter_end`](#is_quarter_end) | Whether this is the last day of its quarter. |
| [`is_quarter_start`](#is_quarter_start) | Whether this is the first day of its quarter. |
| [`is_trading_day`](#is_trading_day) | Whether an exchange holds a regular session on a date: not a weekend, not a scheduled holiday. |
| [`is_triple_witching`](#is_triple_witching) | Whether a date is a quarterly expiry, when index futures, index options and equity options all expire together. |
| [`is_weekday`](#is_weekday) | Whether this date falls Monday to Friday. |
| [`is_weekend`](#is_weekend) | Whether this date falls on a Saturday or Sunday. |
| [`is_year_end`](#is_year_end) | Whether this is 31 December. |
| [`is_year_start`](#is_year_start) | Whether this is 1 January. |
| [`iso_week`](#iso_week) | ISO-8601 week number. |
| [`iso_week_year`](#iso_week_year) | ISO-8601 week-based year, which is not always the calendar year: 2027-01-01 belongs to week-year 2026. |
| [`later`](#later) | The later of two date-times, as instants. |
| [`length_of_month`](#length_of_month) | Number of days in this date's month. |
| [`length_of_year`](#length_of_year) | Number of days in this date's year. |
| [`minus_days`](#minus_days) | Subtract whole calendar days, preserving wall-clock time of day. |
| [`minus_hours`](#minus_hours) | Subtract hours from the instant. |
| [`minus_minutes`](#minus_minutes) | Subtract minutes from the instant. |
| [`minus_months`](#minus_months) | Subtract whole calendar months, with plus_months' clamping rule: 31 March minus one month is 28 or 29 February. |
| [`minus_ms`](#minus_ms) | Subtract milliseconds from the instant. |
| [`minus_period`](#minus_period) | Subtract a Period from a DateTime. |
| [`minus_seconds`](#minus_seconds) | Subtract seconds from the instant. |
| [`minus_trading_days`](#minus_trading_days) | Move backward a number of trading days. |
| [`minus_weeks`](#minus_weeks) | Subtract whole calendar weeks, preserving wall-clock time of day. |
| [`minus_years`](#minus_years) | Subtract whole calendar years, with the same clamping rule: 29 February minus one year is 28 February. |
| [`months_between`](#months_between) | Whole calendar months from this date to another, in the sense of java.time's ChronoUnit.MONTHS.between: a partial month does not count. |
| [`next_or_same_weekday`](#next_or_same_weekday) | This date when it already falls on the given weekday, otherwise the nearest one after it that does, java.time's TemporalAdjusters.nextOrSame, and the natural spelling of "the coming Friday... |
| [`next_trading_day`](#next_trading_day) | The next trading day strictly after a date, skipping weekends and scheduled holidays. |
| [`next_weekday`](#next_weekday) | The nearest date strictly after this one that falls on the given weekday, java.time's TemporalAdjusters.next. |
| [`normalized`](#normalized) | A copy of this DateTime with the day clamped into the length of its month. |
| [`period_between`](#period_between) | The Period between two dates, following java.time's Period.between: whole months first, then the day remainder, with years and months truncated toward zero so every component carries the same sign. |
| [`plus_days`](#plus_days) | Add whole calendar days, preserving wall-clock time of day. |
| [`plus_hours`](#plus_hours) | Add hours to the instant. |
| [`plus_minutes`](#plus_minutes) | Add minutes to the instant. |
| [`plus_months`](#plus_months) | Add whole calendar months, following java.time: the day of month is clamped to the length of the target month, so 31 January plus one month is 28 or 29 February. |
| [`plus_ms`](#plus_ms) | Add milliseconds to the instant. |
| [`plus_period`](#plus_period) | Add a Period. |
| [`plus_seconds`](#plus_seconds) | Add seconds to the instant. |
| [`plus_trading_days`](#plus_trading_days) | Move forward or backward a number of trading days, skipping weekends and holidays. |
| [`plus_weeks`](#plus_weeks) | Add whole calendar weeks, preserving wall-clock time of day. |
| [`plus_years`](#plus_years) | Add whole calendar years, with the same clamping rule as plus_months: 29 February plus one year is 28 February. |
| [`prev_trading_day`](#prev_trading_day) | The previous trading day strictly before a date. |
| [`previous_weekday`](#previous_weekday) | The nearest date strictly before this one that falls on the given weekday, java.time's TemporalAdjusters.previous. |
| [`round_to`](#round_to) | Round this date-time to a unit boundary. |
| [`same_instant`](#same_instant) | Whether two date-times are the same instant, regardless of the offset each is expressed in. |
| [`session_close`](#session_close) | The instant an exchange's session closes on a date, accounting for early closes. |
| [`session_open`](#session_open) | The instant an exchange's session opens on a date. |
| [`start_of`](#start_of) | The first instant of the unit containing this date-time. |
| [`to_iso`](#to_iso) | Format a DateTime as a full ISO-8601 date-time with its offset designator: the form that survives a round trip, so parse_iso(d.to_iso()) gives back d. |
| [`to_iso_date`](#to_iso_date) | Format a DateTime as an ISO-8601 date only. |
| [`to_iso_local`](#to_iso_local) | Format a DateTime as an ISO-8601 date-time string without the offset designator, i.e. as a local wall-clock reading. |
| [`to_iso_ordinal_date`](#to_iso_ordinal_date) | Format a DateTime as an ISO-8601 ordinal date. |
| [`to_iso_time`](#to_iso_time) | Format a DateTime as an ISO-8601 time only. |
| [`to_iso_week_date`](#to_iso_week_date) | Format a DateTime as an ISO-8601 week date. |
| [`to_unix`](#to_unix) | The Unix timestamp this DateTime denotes, using the offset it carries. |
| [`to_zone_same_instant`](#to_zone_same_instant) | The same moment expressed in another zone. |
| [`to_zone_same_local`](#to_zone_same_local) | The same wall clock reinterpreted in another zone, which denotes a different moment. |
| [`trading_day_of_month`](#trading_day_of_month) | The ordinal of a date among its month's trading days: 1 on the month's first trading day, trading_days_in_month on its last. |
| [`trading_days_between`](#trading_days_between) | Count of trading days between two dates. |
| [`until`](#until) | The whole number of units from this date-time to another, the generic form of days_between and months_between, so a unit can be chosen at runtime. |
| [`week_of_month`](#week_of_month) | Which week-row of its month this date falls in, where week 1 is the possibly-partial week containing the 1st. |
| [`weekday`](#weekday) | The weekday of this date, computed from the calendar on every call. |
| [`weekday_ordinal_in_month`](#weekday_ordinal_in_month) | Which occurrence of its own weekday this date is within its month: the 3rd Friday answers 3. |
| [`weekdays_between`](#weekdays_between) | Count of weekdays (Monday through Friday) between two dates, closed form: no loop and no calendar. |
| [`weekly_expiry`](#weekly_expiry) | The expiry of the weekly contract covering a date: that week's Friday, rolled back to the previous trading day when the Friday does not trade. |
| [`with_date`](#with_date) | A copy with the date replaced and the time of day kept. |
| [`with_day`](#with_day) | A copy with the day of month replaced. |
| [`with_day_of_year`](#with_day_of_year) | A copy moved to a given ordinal day of the year, keeping the time of day. |
| [`with_hour`](#with_hour) | A copy with the hour replaced. |
| [`with_minute`](#with_minute) | A copy with the minute replaced. |
| [`with_month`](#with_month) | A copy with the month replaced, clamping the day into the new month. |
| [`with_ms`](#with_ms) | A copy with the millisecond replaced. |
| [`with_offset`](#with_offset) | A copy expressed in a different fixed offset, keeping the civil fields and therefore changing the instant. |
| [`with_second`](#with_second) | A copy with the second replaced. |
| [`with_time`](#with_time) | A copy with the time of day replaced and the date kept. |
| [`with_weekday`](#with_weekday) | A copy moved to a given weekday within the same week, where the week begins on week_start. |
| [`with_year`](#with_year) | A copy with the year replaced. |

## Reference

### adjusted

```pine
DateTime.adjusted(BusinessDay conv, Exchange ex = Exchange.NYSE)
```

Roll a date onto a trading day using an ISDA business-day convention. The modified variants refuse to cross a month boundary and turn back instead, which is what makes them "modified". Named as a participle, like normalized() and negated(): it returns a rolled date and leaves the receiver alone.

| Parameter | Meaning |
|---|---|
| `conv` | The convention. |
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; A DateTime at midnight on the adjusted date: midnight, not this receiver's time of day, because a business-day roll is a question about the day.

**Raises** &nbsp; if the 30-day walk finds no trading day; the shipped calendars cannot produce that, so hitting it means the calendar data is broken.

### clamp_to

```pine
DateTime.clamp_to(DateTime lo, DateTime hi)
```

This instant confined to a range: lo when earlier than lo, hi when later than hi, otherwise itself.

| Parameter | Meaning |
|---|---|
| `lo` | Lower bound. |
| `hi` | Upper bound. |

**Returns** &nbsp; The clamped DateTime..

### closed_for_holiday

```pine
DateTime.closed_for_holiday(Exchange ex = Exchange.NYSE)
```

Whether an exchange is shut for a holiday, as a three-valued answer that says so when the question falls outside the calendar's range. This is what is_holiday cannot do: bool has no room for "not known", so is_holiday reads a date past the horizon as an ordinary trading day. On a tabled calendar that is a wrong answer rather than a missing one, which is the whole reason this exists. No is_ prefix, for the reason fomc_decision_day carries none: every is_ name here promises a bool.

| Parameter | Meaning |
|---|---|
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; YES, NO, or UNKNOWN when the year lies outside calendar_from to calendar_through. UNKNOWN is a value and not na: test it against the enum or with is_yes(), never with na()..

**See also** &nbsp; [`calendar_from`](API-Exchange#calendar_from), [`calendar_through`](API-Exchange#calendar_through), [`fomc_decision_day`](API-DateTime#fomc_decision_day), [`is_holiday`](API-DateTime#is_holiday), [`is_yes`](API-Enums#is_yes)

### compare

```pine
DateTime.compare(DateTime other)
```

Compare two date-times as instants, so differing offsets compare correctly.

| Parameter | Meaning |
|---|---|
| `other` | The second DateTime. |

**Returns** &nbsp; -1 when this is earlier, 0 when they are the same instant, 1 when this is later..

### day_of_year

```pine
DateTime.day_of_year()
```

Day of the year, 1 for 1 January.

**Returns** &nbsp; Ordinal day in [1, 366]..

### days_between

```pine
DateTime.days_between(DateTime other)
```

Whole calendar days from this date to another, ignoring time of day.

| Parameter | Meaning |
|---|---|
| `other` | The ending DateTime. |

**Returns** &nbsp; Signed day count; negative when other is earlier..

### earlier

```pine
DateTime.earlier(DateTime other)
```

The earlier of two date-times, as instants.

| Parameter | Meaning |
|---|---|
| `other` | The second DateTime. |

**Returns** &nbsp; Whichever is earlier; this when they are equal..

### end_of

```pine
DateTime.end_of(TimeUnit unit, Weekday week_start = Weekday.MONDAY)
```

The last instant of the unit containing this date-time, i.e. one millisecond before the next unit begins.

| Parameter | Meaning |
|---|---|
| `unit` | The unit. |
| `week_start` | Which day a week begins on, used only for TimeUnit.WEEK. Default MONDAY. |

**Returns** &nbsp; A new DateTime at the end of the unit, in the same offset the receiver carried; see start_of for what that means across a daylight-saving transition..

**See also** &nbsp; [`start_of`](API-DateTime#start_of)

### equals

```pine
DateTime.equals(DateTime other)
```

Whether two date-times denote the same civil fields and the same offset. Distinct from compare, which asks whether they are the same instant: 12:00-05:00 and 17:00Z are equal as instants but not as records.

| Parameter | Meaning |
|---|---|
| `other` | The second DateTime. |

**Returns** &nbsp; true when every field matches..

### fomc_day

```pine
DateTime.fomc_day()
```

Whether a date falls on either day of a scheduled FOMC meeting. No is_ prefix, for the same reason as fomc_decision_day: the answer is a Known, not a bool.

**Returns** &nbsp; YES, NO, or UNKNOWN when the date lies outside the published window. UNKNOWN is not a no..

**See also** &nbsp; [`fomc_decision_day`](API-DateTime#fomc_decision_day)

### fomc_decision_day

```pine
DateTime.fomc_decision_day()
```

Whether a date is the second day of an FOMC meeting, when the statement is released. No is_ prefix, because it does not return a bool: every other is_ name here promises one, and `if d.is_fomc_decision_day()` would look as though it should compile when it cannot.

**Returns** &nbsp; YES, NO, or UNKNOWN when the date lies outside the published window. UNKNOWN is not a no..

### format

```pine
DateTime.format(string pattern)
```

Format this date-time with a pattern. The pattern letters are str.format_time's, so a pattern carries across unchanged, but the two are not substitutes for each other; see the section note above. Supports G y Y M d D E e u w Q H k h K m s S a X Z z V, single-quoted literals, and '' for a literal quote. Note y is the calendar year and Y is the ISO week-based year: they differ for a few days each January, the confusion behind the "YYYY versus yyyy" bug.

| Parameter | Meaning |
|---|---|
| `pattern` | The format pattern, e.g. "yyyy-MM-dd HH:mm:ss". |

**Returns** &nbsp; The formatted string. Characters outside the pattern language pass through as literals (that is what keeps the T in "yyyy-MM-ddTHH:mm:ss"), with one exception: the reserved letters L B F W O p x g n N c q raise, because they are real DateTimeFormatter fields this library does not implement, and printing one back as text would look like an answer. Single-quote any of them you want literally.

**Raises** &nbsp; on an unterminated quote too.

**See also** &nbsp; [`format_time`](API-Functions#format_time)

### holiday_name

```pine
DateTime.holiday_name(Exchange ex = Exchange.NYSE)
```

The name of the holiday or closure shutting an exchange on a date. This is the calendar's source: is_holiday is defined as this being non-na, so the name and the predicate cannot disagree, and the tabled unscheduled closures are named too: "September 11 attacks", "Hurricane Sandy", "National day of mourning". Names are English only, per the header. Weekends carry no name, exactly as they are not holidays.

| Parameter | Meaning |
|---|---|
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; The holiday's name, or na when the exchange holds a session that day and there is nothing to name..

**See also** &nbsp; [`is_holiday`](API-DateTime#is_holiday)

### is_after

```pine
DateTime.is_after(DateTime other)
```

Whether this date-time is strictly later than another, as instants.

| Parameter | Meaning |
|---|---|
| `other` | The second DateTime. |

**Returns** &nbsp; true when this is later..

### is_before

```pine
DateTime.is_before(DateTime other)
```

Whether this date-time is strictly earlier than another, as instants.

| Parameter | Meaning |
|---|---|
| `other` | The second DateTime. |

**Returns** &nbsp; true when this is earlier..

### is_between

```pine
DateTime.is_between(DateTime lo, DateTime hi)
```

Whether this instant falls in the half-open span [lo, hi). Half-open so that adjacent spans tile without overlapping.

| Parameter | Meaning |
|---|---|
| `lo` | Inclusive lower bound. |
| `hi` | Exclusive upper bound. |

**Returns** &nbsp; true when lo <= this < hi, as instants..

### is_early_close

```pine
DateTime.is_early_close(Exchange ex = Exchange.NYSE)
```

Whether an exchange closes early on a date. Returns false on a day the exchange is shut: a closed market is not an early close.

| Parameter | Meaning |
|---|---|
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; true when the session ends before its usual time..

### is_expiry_day

```pine
DateTime.is_expiry_day(ExpiryKind kind = ExpiryKind.MONTHLY)
```

Whether a date is an expiry of a given cycle. DAILY answers is_trading_day on the US listing calendar: SPX, NDX and XSP list an expiry every session, and a day the market never opened settles nothing, so the tabled unscheduled closures answer false. WEEKLY and MONTHLY are the weekly_expiry and monthly_expiry_day rules; QUARTERLY is MONTHLY confined to the four witching months; VIX is the monthly VIX settlement date by vix_settlement_day's rule; the weekly VX cycle is not modelled.

| Parameter | Meaning |
|---|---|
| `kind` | The expiry cycle to test against. Default MONTHLY, the classic third-Friday cycle. |

**Returns** &nbsp; true when the date is an expiry of that cycle.

**Raises** &nbsp; on an ExpiryKind the switch does not handle, a library bug, and a loud one by design, because a new cycle silently answering false would read as "never expires".

**See also** &nbsp; [`is_trading_day`](API-DateTime#is_trading_day), [`monthly_expiry_day`](API-Functions#monthly_expiry_day), [`vix_settlement_day`](API-Functions#vix_settlement_day), [`weekly_expiry`](API-DateTime#weekly_expiry)

### is_holiday

```pine
DateTime.is_holiday(Exchange ex = Exchange.NYSE)
```

Whether an exchange is closed for a scheduled holiday. Defined as holiday_name being non-na: one source of truth, so the predicate can never contradict the name. Weekends are not holidays; ask is_trading_day for that. Unscheduled closures are included for the past but cannot be for the future; see the closure names in the source.

| Parameter | Meaning |
|---|---|
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; true when the exchange holds no session that day..

**See also** &nbsp; [`holiday_name`](API-DateTime#holiday_name), [`is_trading_day`](API-DateTime#is_trading_day)

### is_leap

```pine
DateTime.is_leap()
```

Whether this date's year is a leap year.

**Returns** &nbsp; true in a leap year..

### is_month_end

```pine
DateTime.is_month_end()
```

Whether this is the last day of its month.

**Returns** &nbsp; true on the final day..

### is_month_start

```pine
DateTime.is_month_start()
```

Whether this is the first day of its month.

**Returns** &nbsp; true on the 1st..

### is_quarter_end

```pine
DateTime.is_quarter_end()
```

Whether this is the last day of its quarter.

**Returns** &nbsp; true on the final day of March, June, September or December..

### is_quarter_start

```pine
DateTime.is_quarter_start()
```

Whether this is the first day of its quarter.

**Returns** &nbsp; true on 1 January, 1 April, 1 July or 1 October..

### is_trading_day

```pine
DateTime.is_trading_day(Exchange ex = Exchange.NYSE)
```

Whether an exchange holds a regular session on a date: not a weekend, not a scheduled holiday. CRYPTO trades every calendar day, weekends included.

| Parameter | Meaning |
|---|---|
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; true when the exchange is open, whether or not it closes early..

### is_triple_witching

```pine
DateTime.is_triple_witching()
```

Whether a date is a quarterly expiry, when index futures, index options and equity options all expire together. The QUARTERLY arm of is_expiry_day under its traditional name; one rule, two spellings, and this one routes through the other so they cannot drift apart.

**Returns** &nbsp; true on a March, June, September or December expiry..

**See also** &nbsp; [`is_expiry_day`](API-DateTime#is_expiry_day)

### is_weekday

```pine
DateTime.is_weekday()
```

Whether this date falls Monday to Friday.

**Returns** &nbsp; true on a weekday..

### is_weekend

```pine
DateTime.is_weekend()
```

Whether this date falls on a Saturday or Sunday. Says nothing about whether a market is open; ask is_trading_day for that.

**Returns** &nbsp; true at the weekend..

**See also** &nbsp; [`is_trading_day`](API-DateTime#is_trading_day)

### is_year_end

```pine
DateTime.is_year_end()
```

Whether this is 31 December.

**Returns** &nbsp; true on the last day of the year..

### is_year_start

```pine
DateTime.is_year_start()
```

Whether this is 1 January.

**Returns** &nbsp; true on the first day of the year..

### iso_week

```pine
DateTime.iso_week()
```

ISO-8601 week number. Week 1 is the week containing the first Thursday of the year, so early January can belong to week 52 or 53 of the previous week-based year. Pair this with iso_week_year, never with the calendar year.

**Returns** &nbsp; ISO week number in [1, 53]..

**See also** &nbsp; [`iso_week_year`](API-DateTime#iso_week_year)

### iso_week_year

```pine
DateTime.iso_week_year()
```

ISO-8601 week-based year, which is not always the calendar year: 2027-01-01 belongs to week-year 2026. Getting this wrong is exactly the "YYYY versus yyyy" formatting bug.

**Returns** &nbsp; ISO week-based year..

### later

```pine
DateTime.later(DateTime other)
```

The later of two date-times, as instants.

| Parameter | Meaning |
|---|---|
| `other` | The second DateTime. |

**Returns** &nbsp; Whichever is later; this when they are equal..

### length_of_month

```pine
DateTime.length_of_month()
```

Number of days in this date's month.

**Returns** &nbsp; 28, 29, 30 or 31..

### length_of_year

```pine
DateTime.length_of_year()
```

Number of days in this date's year.

**Returns** &nbsp; 365 or 366..

### minus_days

```pine
DateTime.minus_days(int n)
```

Subtract whole calendar days, preserving wall-clock time of day. Delegates to plus_days with -n.

| Parameter | Meaning |
|---|---|
| `n` | Days to subtract; a negative n adds. |

**Returns** &nbsp; A new DateTime..

**See also** &nbsp; [`plus_days`](API-DateTime#plus_days)

### minus_hours

```pine
DateTime.minus_hours(int n)
```

Subtract hours from the instant. Delegates to plus_hours with -n.

| Parameter | Meaning |
|---|---|
| `n` | Hours to subtract; a negative n adds. |

**Returns** &nbsp; A new DateTime in the same offset..

**See also** &nbsp; [`plus_hours`](API-DateTime#plus_hours)

### minus_minutes

```pine
DateTime.minus_minutes(int n)
```

Subtract minutes from the instant. Delegates to plus_minutes with -n.

| Parameter | Meaning |
|---|---|
| `n` | Minutes to subtract; a negative n adds. |

**Returns** &nbsp; A new DateTime in the same offset..

**See also** &nbsp; [`plus_minutes`](API-DateTime#plus_minutes)

### minus_months

```pine
DateTime.minus_months(int n, Overflow ovf = Overflow.CONSTRAIN)
```

Subtract whole calendar months, with plus_months' clamping rule: 31 March minus one month is 28 or 29 February. Delegates to plus_months with -n.

| Parameter | Meaning |
|---|---|
| `n` | Months to subtract; a negative n adds. |
| `ovf` | What to do when the day does not exist in the target month. Default CONSTRAIN. |

**Returns** &nbsp; A new DateTime, or na when ovf is REJECT and the day does not exist..

**See also** &nbsp; [`plus_months`](API-DateTime#plus_months)

### minus_ms

```pine
DateTime.minus_ms(int n)
```

Subtract milliseconds from the instant. Delegates to plus_ms with -n.

| Parameter | Meaning |
|---|---|
| `n` | Milliseconds to subtract; a negative n adds. |

**Returns** &nbsp; A new DateTime in the same offset..

**See also** &nbsp; [`plus_ms`](API-DateTime#plus_ms)

### minus_period

```pine
DateTime.minus_period(Period p, Overflow ovf = Overflow.CONSTRAIN)
```

Subtract a Period from a DateTime. Lives here rather than beside its eight minus_* siblings because it delegates through negated() just above, and Pine requires a definition to precede its use. Months are still applied before days: the period is negated first, exactly java.time's minus.

| Parameter | Meaning |
|---|---|
| `p` | The Period to subtract. |
| `ovf` | What to do when the month step lands on a day that does not exist. Default CONSTRAIN. |

**Returns** &nbsp; A new DateTime, or na when ovf is REJECT and the day does not exist..

### minus_seconds

```pine
DateTime.minus_seconds(int n)
```

Subtract seconds from the instant. Delegates to plus_seconds with -n.

| Parameter | Meaning |
|---|---|
| `n` | Seconds to subtract; a negative n adds. |

**Returns** &nbsp; A new DateTime in the same offset..

**See also** &nbsp; [`plus_seconds`](API-DateTime#plus_seconds)

### minus_trading_days

```pine
DateTime.minus_trading_days(int n, Exchange ex = Exchange.NYSE)
```

Move backward a number of trading days. Delegates to plus_trading_days with -n, so it shares the bounded walk, the zero-returns-the-same-date rule, and the RAISE.

| Parameter | Meaning |
|---|---|
| `n` | Trading days to move back; a negative n moves forward. |
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; A DateTime at midnight on the resulting trading day.

**Raises** &nbsp; exactly as plus_trading_days does when the bounded walk cannot resolve.

**See also** &nbsp; [`plus_trading_days`](API-DateTime#plus_trading_days)

### minus_weeks

```pine
DateTime.minus_weeks(int n)
```

Subtract whole calendar weeks, preserving wall-clock time of day. Delegates to plus_weeks with -n.

| Parameter | Meaning |
|---|---|
| `n` | Weeks to subtract; a negative n adds. |

**Returns** &nbsp; A new DateTime..

**See also** &nbsp; [`plus_weeks`](API-DateTime#plus_weeks)

### minus_years

```pine
DateTime.minus_years(int n, Overflow ovf = Overflow.CONSTRAIN)
```

Subtract whole calendar years, with the same clamping rule: 29 February minus one year is 28 February. Delegates to plus_years with -n.

| Parameter | Meaning |
|---|---|
| `n` | Years to subtract; a negative n adds. |
| `ovf` | What to do when the day does not exist in the target month. Default CONSTRAIN. |

**Returns** &nbsp; A new DateTime, or na when ovf is REJECT and the day does not exist..

**See also** &nbsp; [`plus_years`](API-DateTime#plus_years)

### months_between

```pine
DateTime.months_between(DateTime other)
```

Whole calendar months from this date to another, in the sense of java.time's ChronoUnit.MONTHS.between: a partial month does not count. Note the deliberate asymmetry with plus_months: months_between(31 Jan, 29 Feb) is 0, yet 31 January plus one month clamps to 29 February. Clamping makes plus_months non-injective (29 and 31 January both land on 29 February), so the two are not inverses at a clamped boundary. This matches java.time and is inherent to clamped month arithmetic.

| Parameter | Meaning |
|---|---|
| `other` | The ending DateTime. |

**Returns** &nbsp; Signed whole-month count..

**See also** &nbsp; [`plus_months`](API-DateTime#plus_months)

### next_or_same_weekday

```pine
DateTime.next_or_same_weekday(Weekday dow)
```

This date when it already falls on the given weekday, otherwise the nearest one after it that does, java.time's TemporalAdjusters.nextOrSame, and the natural spelling of "the coming Friday, counting today".

| Parameter | Meaning |
|---|---|
| `dow` | The weekday wanted. |

**Returns** &nbsp; A new DateTime, 0 to 6 days forward, keeping the time of day..

### next_trading_day

```pine
DateTime.next_trading_day(Exchange ex = Exchange.NYSE)
```

The next trading day strictly after a date, skipping weekends and scheduled holidays. The exact inverse of prev_trading_day: both route through is_trading_day, so both honour the ad-hoc closure table that no rule generates: the 2001 September closure and Hurricane Sandy are trading days to a rule and are not trading days here.

| Parameter | Meaning |
|---|---|
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; A DateTime at midnight on that trading day.

**Raises** &nbsp; exactly as plus_trading_days does; this is its one-step walk.

**See also** &nbsp; [`is_trading_day`](API-DateTime#is_trading_day), [`plus_trading_days`](API-DateTime#plus_trading_days), [`prev_trading_day`](API-DateTime#prev_trading_day)

### next_weekday

```pine
DateTime.next_weekday(Weekday dow)
```

The nearest date strictly after this one that falls on the given weekday, java.time's TemporalAdjusters.next. Strictly: asked from a Friday, the next Friday is a full week away, because "next" excludes today.

| Parameter | Meaning |
|---|---|
| `dow` | The weekday wanted. |

**Returns** &nbsp; A new DateTime, 1 to 7 days forward, keeping the time of day..

### normalized

```pine
DateTime.normalized()
```

A copy of this DateTime with the day clamped into the length of its month. Repairs a record whose fields were assigned directly, which is the only way this library can hold a date its constructor would have refused. Routes through the same repair as the withers.

**Returns** &nbsp; A new, self-consistent DateTime, or na when a field other than the day is out of range: a day past the end of its month clamps, but a Month of 13 is a typo, not an overflow, and is refused..

### period_between

```pine
DateTime.period_between(DateTime other)
```

The Period between two dates, following java.time's Period.between: whole months first, then the day remainder, with years and months truncated toward zero so every component carries the same sign.

| Parameter | Meaning |
|---|---|
| `other` | The ending DateTime. |

**Returns** &nbsp; A Period p for which this.plus_period(p) always lands on other's date..

**See also** &nbsp; [`plus_period`](API-DateTime#plus_period)

### plus_days

```pine
DateTime.plus_days(int n)
```

Add whole calendar days, preserving wall-clock time of day.

| Parameter | Meaning |
|---|---|
| `n` | Days to add; may be negative. |

**Returns** &nbsp; A new DateTime..

### plus_hours

```pine
DateTime.plus_hours(int n)
```

Add hours to the instant.

| Parameter | Meaning |
|---|---|
| `n` | Hours to add; may be negative. |

**Returns** &nbsp; A new DateTime in the same offset..

### plus_minutes

```pine
DateTime.plus_minutes(int n)
```

Add minutes to the instant.

| Parameter | Meaning |
|---|---|
| `n` | Minutes to add; may be negative. |

**Returns** &nbsp; A new DateTime in the same offset..

### plus_months

```pine
DateTime.plus_months(int n, Overflow ovf = Overflow.CONSTRAIN)
```

Add whole calendar months, following java.time: the day of month is clamped to the length of the target month, so 31 January plus one month is 28 or 29 February. Not commutative with plus_days: adding a month then a day differs from adding a day then a month.

| Parameter | Meaning |
|---|---|
| `n` | Months to add; may be negative. |
| `ovf` | What to do when the day does not exist in the target month. Default CONSTRAIN. |

**Returns** &nbsp; A new DateTime, or na when ovf is REJECT and the day does not exist..

**See also** &nbsp; [`plus_days`](API-DateTime#plus_days)

### plus_ms

```pine
DateTime.plus_ms(int n)
```

Add milliseconds to the instant.

| Parameter | Meaning |
|---|---|
| `n` | Milliseconds to add; may be negative. |

**Returns** &nbsp; A new DateTime in the same offset..

### plus_period

```pine
DateTime.plus_period(Period p, Overflow ovf = Overflow.CONSTRAIN)
```

Add a Period. Months are applied before days, matching java.time; the two orders can land on different dates.

| Parameter | Meaning |
|---|---|
| `p` | The Period to add. |
| `ovf` | What to do when the month step lands on a day that does not exist. Default CONSTRAIN. |

**Returns** &nbsp; A new DateTime, or na when ovf is REJECT and the day does not exist..

### plus_seconds

```pine
DateTime.plus_seconds(int n)
```

Add seconds to the instant.

| Parameter | Meaning |
|---|---|
| `n` | Seconds to add; may be negative. |

**Returns** &nbsp; A new DateTime in the same offset..

### plus_trading_days

```pine
DateTime.plus_trading_days(int n, Exchange ex = Exchange.NYSE)
```

Move forward or backward a number of trading days, skipping weekends and holidays. Zero returns the same date whether or not it trades; use adjusted for that. Named plus_trading_days rather than add_trading_days to join the nine plus_* methods above: one family of movers, one verb.

| Parameter | Meaning |
|---|---|
| `n` | Trading days to move; negative moves backward. |
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; A DateTime at midnight on the resulting trading day.

**Raises** &nbsp; when the bounded walk of |n| * 2 + 30 calendar days does not contain |n| trading days. No shipped calendar can do that, so reaching the error means the calendar data is wrong.

### plus_weeks

```pine
DateTime.plus_weeks(int n)
```

Add whole calendar weeks, preserving wall-clock time of day.

| Parameter | Meaning |
|---|---|
| `n` | Weeks to add; may be negative. |

**Returns** &nbsp; A new DateTime..

### plus_years

```pine
DateTime.plus_years(int n, Overflow ovf = Overflow.CONSTRAIN)
```

Add whole calendar years, with the same clamping rule as plus_months: 29 February plus one year is 28 February.

| Parameter | Meaning |
|---|---|
| `n` | Years to add; may be negative. |
| `ovf` | What to do when the day does not exist in the target month. Default CONSTRAIN. |

**Returns** &nbsp; A new DateTime, or na when ovf is REJECT and the day does not exist..

**See also** &nbsp; [`plus_months`](API-DateTime#plus_months)

### prev_trading_day

```pine
DateTime.prev_trading_day(Exchange ex = Exchange.NYSE)
```

The previous trading day strictly before a date.

| Parameter | Meaning |
|---|---|
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; A DateTime at midnight on that trading day.

**Raises** &nbsp; exactly as plus_trading_days does; this is its one-step walk.

**See also** &nbsp; [`plus_trading_days`](API-DateTime#plus_trading_days)

### previous_weekday

```pine
DateTime.previous_weekday(Weekday dow)
```

The nearest date strictly before this one that falls on the given weekday, java.time's TemporalAdjusters.previous. Strictly: asked from a Friday, the previous Friday is a full week back.

| Parameter | Meaning |
|---|---|
| `dow` | The weekday wanted. |

**Returns** &nbsp; A new DateTime, 1 to 7 days back, keeping the time of day..

### round_to

```pine
DateTime.round_to(TimeUnit unit, RoundMode mode = RoundMode.FLOOR, Weekday week_start = Weekday.MONDAY)
```

Round this date-time to a unit boundary. Modes are applied to elapsed time since the Unix epoch, so TRUNC means toward 1970 and HALF_EXPAND breaks exact ties away from it.

| Parameter | Meaning |
|---|---|
| `unit` | The unit to round to. |
| `mode` | The rounding mode. Default FLOOR. |
| `week_start` | Which day a week begins on, used only for TimeUnit.WEEK. Default MONDAY, matching start_of and end_of: without it a Sunday-week user could floor and ceil to a Sunday week but not round to one. |

**Returns** &nbsp; A new DateTime on a unit boundary, in the same offset the receiver carried; see start_of for what that means across a daylight-saving transition..

**See also** &nbsp; [`start_of`](API-DateTime#start_of)

### same_instant

```pine
DateTime.same_instant(DateTime other)
```

Whether two date-times are the same instant, regardless of the offset each is expressed in.

| Parameter | Meaning |
|---|---|
| `other` | The second DateTime. |

**Returns** &nbsp; true when they denote the same moment..

### session_close

```pine
DateTime.session_close(Exchange ex = Exchange.NYSE)
```

The instant an exchange's session closes on a date, accounting for early closes.

| Parameter | Meaning |
|---|---|
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; Unix timestamp in milliseconds, or na when the exchange is closed that day..

### session_open

```pine
DateTime.session_open(Exchange ex = Exchange.NYSE)
```

The instant an exchange's session opens on a date. For CME this is 17:00 Chicago on the previous calendar day, because a Globex session opens the evening before the date it settles on.

| Parameter | Meaning |
|---|---|
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; Unix timestamp in milliseconds, or na when the exchange is closed that day..

### start_of

```pine
DateTime.start_of(TimeUnit unit, Weekday week_start = Weekday.MONDAY)
```

The first instant of the unit containing this date-time.

| Parameter | Meaning |
|---|---|
| `unit` | The unit to truncate to. |
| `week_start` | Which day a week begins on, used only for TimeUnit.WEEK. Default MONDAY, the ISO-8601 convention; pass SUNDAY for the common US one. |

**Returns** &nbsp; A new DateTime at the start of the unit, in the same offset the receiver carried. For a fixed-offset record that is the only reading available, but it means start_of(DAY) is not necessarily local midnight in a zone that changed offset that day. Use today() for that, or re-resolve through Zone.to_unix..

**See also** &nbsp; [`to_unix`](API-Zone#to_unix)

### to_iso

```pine
DateTime.to_iso()
```

Format a DateTime as a full ISO-8601 date-time with its offset designator: the form that survives a round trip, so parse_iso(d.to_iso()) gives back d. The short name belongs to the offset-carrying form: it keeps the offset the type carries, and it matches Interval's to_iso, which also emits offsets. The offset-less spelling is to_iso_local.

**Returns** &nbsp; A string of the form "YYYY-MM-DDTHH:MM:SS+HH:MM", or ending in "Z" at UTC..

**See also** &nbsp; [`parse_iso`](API-Functions#parse_iso), [`to_iso_local`](API-DateTime#to_iso_local)

### to_iso_date

```pine
DateTime.to_iso_date()
```

Format a DateTime as an ISO-8601 date only.

**Returns** &nbsp; A string of the form "YYYY-MM-DD"..

### to_iso_local

```pine
DateTime.to_iso_local()
```

Format a DateTime as an ISO-8601 date-time string without the offset designator, i.e. as a local wall-clock reading. Lossy on purpose: two different instants print identically, so this is for a human reading a label, never for anything that will be parsed back. to_iso is the round-tripping form.

**Returns** &nbsp; A string of the form "YYYY-MM-DDTHH:MM:SS"..

**See also** &nbsp; [`to_iso`](API-Interval#to_iso)

### to_iso_ordinal_date

```pine
DateTime.to_iso_ordinal_date()
```

Format a DateTime as an ISO-8601 ordinal date.

**Returns** &nbsp; A string of the form "YYYY-DDD"..

### to_iso_time

```pine
DateTime.to_iso_time()
```

Format a DateTime as an ISO-8601 time only.

**Returns** &nbsp; A string of the form "HH:MM:SS"..

### to_iso_week_date

```pine
DateTime.to_iso_week_date()
```

Format a DateTime as an ISO-8601 week date. Note the year shown is the week-based year, which for early January can differ from the calendar year.

**Returns** &nbsp; A string of the form "YYYY-Www-D"..

### to_unix

```pine
DateTime.to_unix()
```

The Unix timestamp this DateTime denotes, using the offset it carries.

**Returns** &nbsp; Unix timestamp in milliseconds..

### to_zone_same_instant

```pine
DateTime.to_zone_same_instant(Zone z)
```

The same moment expressed in another zone. 12:00 in New York becomes 17:00 in London; it is still the same instant.

| Parameter | Meaning |
|---|---|
| `z` | The target zone. |

**Returns** &nbsp; A new DateTime with the target zone's offset in force..

### to_zone_same_local

```pine
DateTime.to_zone_same_local(Zone z, Resolver res = Resolver.COMPATIBLE)
```

The same wall clock reinterpreted in another zone, which denotes a different moment. 12:00 in New York becomes 12:00 in London, an hour that arrives five hours earlier.

| Parameter | Meaning |
|---|---|
| `z` | The target zone. |
| `res` | How to resolve a local time the target zone skipped or repeated. Default COMPATIBLE. |

**Returns** &nbsp; A new DateTime, or na when res is REJECT and the local time is impossible or ambiguous..

### trading_day_of_month

```pine
DateTime.trading_day_of_month(Exchange ex = Exchange.NYSE)
```

The ordinal of a date among its month's trading days: 1 on the month's first trading day, trading_days_in_month on its last. The number "T+n of the month" strategies key on.

| Parameter | Meaning |
|---|---|
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; Ordinal in [1, trading_days_in_month(...)], or na when the date is not itself a trading day: a Saturday holds no position in a sequence it is not part of, and 0 would be an in-band stand-in for "none", which the header's error rules forbid..

**See also** &nbsp; [`trading_days_in_month`](API-Functions#trading_days_in_month)

### trading_days_between

```pine
DateTime.trading_days_between(DateTime other, Exchange ex = Exchange.NYSE)
```

Count of trading days between two dates. The span counted is always half-open on the earlier of the two (the earlier date counts when it trades, the later never does), and the result is negated when other comes first. Half-open so consecutive spans add up; anchored on the earlier date rather than on `this` so the function is exactly antisymmetric, as a signed difference has to be. One consequence: a reversed pair counts its end, so with 1 January a holiday, trading_days_between(5 Jan, 1 Jan) is -1 and not -2.

| Parameter | Meaning |
|---|---|
| `other` | The ending DateTime. |
| `ex` | The exchange. Default NYSE. |

**Returns** &nbsp; Signed count; negative when other is earlier..

### until

```pine
DateTime.until(DateTime other, TimeUnit unit)
```

The whole number of units from this date-time to another, the generic form of days_between and months_between, so a unit can be chosen at runtime.

| Parameter | Meaning |
|---|---|
| `other` | The ending DateTime. |
| `unit` | The unit to count in. |

**Returns** &nbsp; Signed whole count; partial units do not count..

**See also** &nbsp; [`days_between`](API-DateTime#days_between), [`months_between`](API-DateTime#months_between)

### week_of_month

```pine
DateTime.week_of_month(Weekday week_start = Weekday.MONDAY)
```

Which week-row of its month this date falls in, where week 1 is the possibly-partial week containing the 1st. The answer depends on which day begins a week: the 9th of a month can sit in week 2 or week 3 of that same month, so the convention is a parameter rather than an assumption.

| Parameter | Meaning |
|---|---|
| `week_start` | Which day the week begins on. Default MONDAY, the ISO convention. |

**Returns** &nbsp; Week of month in [1, 6]..

### weekday

```pine
DateTime.weekday()
```

The weekday of this date, computed from the calendar on every call. There is no cached weekday field to go stale, so the answer is correct however the record was built.

**Returns** &nbsp; The Weekday..

### weekday_ordinal_in_month

```pine
DateTime.weekday_ordinal_in_month()
```

Which occurrence of its own weekday this date is within its month: the 3rd Friday answers 3. The inverse of nth_weekday_of_month, and unlike week_of_month it needs no week-start convention: it counts only days sharing this date's weekday, so where a week begins cannot matter.

**Returns** &nbsp; Ordinal in [1, 5]. Inverse in the exact sense that nth_weekday_of_month(Year, Month, this.weekday(), the answer) lands back on this day..

**See also** &nbsp; [`nth_weekday_of_month`](API-Functions#nth_weekday_of_month), [`week_of_month`](API-DateTime#week_of_month)

### weekdays_between

```pine
DateTime.weekdays_between(DateTime other)
```

Count of weekdays (Monday through Friday) between two dates, closed form: no loop and no calendar. This is exactly what trading_days_between degenerates to when no exchange calendar applies, and it keeps that function's whole contract: the span counted is half-open on the earlier date (the earlier date counts when it is a weekday, the later never does), and the result is negated when other comes first, so the function is exactly antisymmetric.

| Parameter | Meaning |
|---|---|
| `other` | The ending DateTime. |

**Returns** &nbsp; Signed count; negative when other is earlier..

**See also** &nbsp; [`trading_days_between`](API-DateTime#trading_days_between)

### weekly_expiry

```pine
DateTime.weekly_expiry()
```

The expiry of the weekly contract covering a date: that week's Friday, rolled back to the previous trading day when the Friday does not trade.

**Returns** &nbsp; A DateTime at midnight on the weekly expiry date..

### with_date

```pine
DateTime.with_date(int Year, int Month, int Day, Overflow ovf = Overflow.CONSTRAIN)
```

A copy with the date replaced and the time of day kept.

| Parameter | Meaning |
|---|---|
| `Year` | The new year. |
| `Month` | The new month, 1-12. |
| `Day` | The new day of month, 1 or greater. |
| `ovf` | What to do when the day is past the end of the target month. Default CONSTRAIN. |

**Returns** &nbsp; A new DateTime, or na. As in with_day, Overflow decides only what happens past the end of the month; a Month outside 1-12 or a Day below 1 is na whichever Overflow you pass..

**See also** &nbsp; [`with_day`](API-DateTime#with_day)

### with_day

```pine
DateTime.with_day(int Day, Overflow ovf = Overflow.CONSTRAIN)
```

A copy with the day of month replaced.

| Parameter | Meaning |
|---|---|
| `Day` | The new day of month, 1 or greater. |
| `ovf` | What to do when the day is past the end of this month. Default CONSTRAIN. |

**Returns** &nbsp; A new DateTime, or na. Overflow governs one direction only: a day past the end of the month clamps under CONSTRAIN and is na under REJECT, but a day below 1 is na under both, because it is not an overflow at all: nothing sensible to clamp it to..

### with_day_of_year

```pine
DateTime.with_day_of_year(int Doy)
```

A copy moved to a given ordinal day of the year, keeping the time of day.

| Parameter | Meaning |
|---|---|
| `Doy` | Ordinal day, 1-366. |

**Returns** &nbsp; A new DateTime.

**Raises** &nbsp; when the ordinal does not exist in this year: a 366th day of a common year is a caller bug, not a date the calendar declines to have.

### with_hour

```pine
DateTime.with_hour(int Hour)
```

A copy with the hour replaced.

| Parameter | Meaning |
|---|---|
| `Hour` | The new hour, 0-23. |

**Returns** &nbsp; A new DateTime.

**Raises** &nbsp; when the hour is out of range.

### with_minute

```pine
DateTime.with_minute(int Minute)
```

A copy with the minute replaced.

| Parameter | Meaning |
|---|---|
| `Minute` | The new minute, 0-59. |

**Returns** &nbsp; A new DateTime.

**Raises** &nbsp; when the minute is out of range.

### with_month

```pine
DateTime.with_month(int Month, Overflow ovf = Overflow.CONSTRAIN)
```

A copy with the month replaced, clamping the day into the new month.

| Parameter | Meaning |
|---|---|
| `Month` | The new month, 1-12. |
| `ovf` | What to do when the day does not exist in the target. Default CONSTRAIN. |

**Returns** &nbsp; A new DateTime, or na when the month is out of range or the day does not exist under REJECT..

### with_ms

```pine
DateTime.with_ms(int MS)
```

A copy with the millisecond replaced.

| Parameter | Meaning |
|---|---|
| `MS` | The new millisecond, 0-999. |

**Returns** &nbsp; A new DateTime.

**Raises** &nbsp; when it is out of range.

### with_offset

```pine
DateTime.with_offset(float utc)
```

A copy expressed in a different fixed offset, keeping the civil fields and therefore changing the instant. To keep the instant instead, use to_zone_same_instant.

| Parameter | Meaning |
|---|---|
| `utc` | The new offset from UTC in hours. |

**Returns** &nbsp; A new DateTime denoting a different moment..

**See also** &nbsp; [`to_zone_same_instant`](API-DateTime#to_zone_same_instant)

### with_second

```pine
DateTime.with_second(int Second)
```

A copy with the second replaced.

| Parameter | Meaning |
|---|---|
| `Second` | The new second, 0-59. |

**Returns** &nbsp; A new DateTime.

**Raises** &nbsp; when the second is out of range.

### with_time

```pine
DateTime.with_time(int Hour, int Minute = 0, int Second = 0, int MS = 0)
```

A copy with the time of day replaced and the date kept.

| Parameter | Meaning |
|---|---|
| `Hour` | The new hour, 0-23. |
| `Minute` | The new minute, 0-59. Default 0. |
| `Second` | The new second, 0-59. Default 0. |
| `MS` | The new millisecond, 0-999. Default 0. |

**Returns** &nbsp; A new DateTime.

**Raises** &nbsp; when any component is out of range.

### with_weekday

```pine
DateTime.with_weekday(Weekday dow, Weekday week_start = Weekday.MONDAY)
```

A copy moved to a given weekday within the same week, where the week begins on week_start. Never moves the date by more than six days.

| Parameter | Meaning |
|---|---|
| `dow` | The weekday wanted. |
| `week_start` | Which day the week begins on. Default MONDAY, the ISO convention. |

**Returns** &nbsp; A new DateTime..

### with_year

```pine
DateTime.with_year(int Year, Overflow ovf = Overflow.CONSTRAIN)
```

A copy with the year replaced. The day is clamped, so 29 February in a leap year becomes 28 February in a common one.

| Parameter | Meaning |
|---|---|
| `Year` | The new calendar year. |
| `ovf` | What to do when the day does not exist in the target. Default CONSTRAIN. |

**Returns** &nbsp; A new DateTime, or na under REJECT when the day does not exist..

---

[API Index](API-Index) &nbsp;·&nbsp; [Task Index](Task-Index) &nbsp;·&nbsp; [Glossary](Glossary)
