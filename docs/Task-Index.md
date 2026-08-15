# Task Index

The same exports as [API Index](API-Index), grouped by the question you arrived with rather than by name. Two indexes for two ways of remembering things.

## Build a date, or convert one to and from an instant

- [`DateTime.to_unix`](API-DateTime#to_unix) The Unix timestamp this DateTime denotes, using the offset it carries.
- [`DateTime.weekday`](API-DateTime#weekday) The weekday of this date, computed from the calendar on every call.
- [`date_to_unix`](API-Functions#date_to_unix) Convert a civil date-time to a Unix timestamp.
- [`date_to_weekday`](API-Functions#date_to_weekday) Day of week for a civil date, derived from the same civil algorithm as every other function here.
- [`days_from_civil`](API-Functions#days_from_civil) Days elapsed from 1970-01-01 to a civil date.
- [`days_in_month`](API-Functions#days_in_month) Number of days in a given month.
- [`days_in_year`](API-Functions#days_in_year) Number of days in a given year.
- [`is_leap_year`](API-Functions#is_leap_year) Whether a year is a leap year in the proleptic Gregorian calendar.
- [`is_valid_date`](API-Functions#is_valid_date) Whether a civil moment exists, without raising.
- [`new_datetime`](API-Functions#new_datetime) Build a DateTime from civil fields.
- [`unix_to_date`](API-Functions#unix_to_date) Convert a Unix timestamp to a civil date-time.

## Work with weekdays

- [`Weekday.to_int`](API-Weekday#to_int) Numeric code for a weekday, 0 = Sunday through 6 = Saturday.
- [`Weekday.to_iso_dow`](API-Weekday#to_iso_dow) ISO-8601 numbering for this weekday, 1 = Monday through 7 = Sunday.
- [`weekday_from_int`](API-Functions#weekday_from_int) Weekday for a numeric code, 0 = Sunday through 6 = Saturday.

- [`Weekday.minus`](API-Weekday#minus) The weekday n days earlier in the weekly cycle, wrapping.
- [`Weekday.plus`](API-Weekday#plus) The weekday n days later in the weekly cycle, wrapping.

## Find the nth weekday of a month

- [`Weekday.days_until`](API-Weekday#days_until) Forward distance in days from this weekday to another, never negative.
- [`nth_weekday_of_month`](API-Functions#nth_weekday_of_month) Day of month of the nth given weekday, following java.time's dayOfWeekInMonth semantics.

## Ask which week, quarter or day of year this is

- [`DateTime.day_of_year`](API-DateTime#day_of_year) Day of the year, 1 for 1 January.
- [`DateTime.iso_week`](API-DateTime#iso_week) ISO-8601 week number.
- [`DateTime.iso_week_year`](API-DateTime#iso_week_year) ISO-8601 week-based year, which is not always the calendar year: 2027-01-01 belongs to week-year 2026.
- [`DateTime.week_of_month`](API-DateTime#week_of_month) Which week-row of its month this date falls in, where week 1 is the possibly-partial week containing the 1st.
- [`DateTime.weekday_ordinal_in_month`](API-DateTime#weekday_ordinal_in_month) Which occurrence of its own weekday this date is within its month: the 3rd Friday answers 3.
- [`date_from_day_of_year`](API-Functions#date_from_day_of_year) Civil date for an ordinal day of the year.
- [`date_from_iso_week`](API-Functions#date_from_iso_week) Civil date for an ISO-8601 week date.
- [`quarter`](API-Functions#quarter) Calendar quarter containing a month, or the fiscal quarter, when the fiscal year begins in some other month.

## Move a date by calendar amounts

- [`DateTime.minus_days`](API-DateTime#minus_days) Subtract whole calendar days, preserving wall-clock time of day.
- [`DateTime.minus_months`](API-DateTime#minus_months) Subtract whole calendar months, with plus_months' clamping rule: 31 March minus one month is 28 or 29 February.
- [`DateTime.minus_weeks`](API-DateTime#minus_weeks) Subtract whole calendar weeks, preserving wall-clock time of day.
- [`DateTime.minus_years`](API-DateTime#minus_years) Subtract whole calendar years, with the same clamping rule: 29 February minus one year is 28 February.
- [`DateTime.plus_days`](API-DateTime#plus_days) Add whole calendar days, preserving wall-clock time of day.
- [`DateTime.plus_months`](API-DateTime#plus_months) Add whole calendar months, following java.time: the day of month is clamped to the length of the target month, so 31 January plus one month is 28 or 29 February.
- [`DateTime.plus_period`](API-DateTime#plus_period) Add a Period.
- [`DateTime.plus_weeks`](API-DateTime#plus_weeks) Add whole calendar weeks, preserving wall-clock time of day.
- [`DateTime.plus_years`](API-DateTime#plus_years) Add whole calendar years, with the same clamping rule as plus_months: 29 February plus one year is 28 February.

## Move an instant by exact amounts

- [`DateTime.minus_hours`](API-DateTime#minus_hours) Subtract hours from the instant.
- [`DateTime.minus_minutes`](API-DateTime#minus_minutes) Subtract minutes from the instant.
- [`DateTime.minus_ms`](API-DateTime#minus_ms) Subtract milliseconds from the instant.
- [`DateTime.minus_seconds`](API-DateTime#minus_seconds) Subtract seconds from the instant.
- [`DateTime.plus_hours`](API-DateTime#plus_hours) Add hours to the instant.
- [`DateTime.plus_minutes`](API-DateTime#plus_minutes) Add minutes to the instant.
- [`DateTime.plus_ms`](API-DateTime#plus_ms) Add milliseconds to the instant.
- [`DateTime.plus_seconds`](API-DateTime#plus_seconds) Add seconds to the instant.

## Measure the gap between two dates

- [`DateTime.days_between`](API-DateTime#days_between) Whole calendar days from this date to another, ignoring time of day.
- [`DateTime.months_between`](API-DateTime#months_between) Whole calendar months from this date to another, in the sense of java.time's ChronoUnit.MONTHS.between: a partial month does not count.
- [`DateTime.period_between`](API-DateTime#period_between) The Period between two dates, following java.time's Period.between: whole months first, then the day remainder, with years and months truncated toward zero so every component carries the same sign.

## Compare or order two dates

- [`DateTime.compare`](API-DateTime#compare) Compare two date-times as instants, so differing offsets compare correctly.
- [`DateTime.earlier`](API-DateTime#earlier) The earlier of two date-times, as instants.
- [`DateTime.is_after`](API-DateTime#is_after) Whether this date-time is strictly later than another, as instants.
- [`DateTime.is_before`](API-DateTime#is_before) Whether this date-time is strictly earlier than another, as instants.
- [`DateTime.later`](API-DateTime#later) The later of two date-times, as instants.

## Snap a date to a unit boundary

- [`DateTime.end_of`](API-DateTime#end_of) The last instant of the unit containing this date-time, i.e. one millisecond before the next unit begins.
- [`DateTime.round_to`](API-DateTime#round_to) Round this date-time to a unit boundary.
- [`DateTime.start_of`](API-DateTime#start_of) The first instant of the unit containing this date-time.

## Change one field of a date

- [`DateTime.next_or_same_weekday`](API-DateTime#next_or_same_weekday) This date when it already falls on the given weekday, otherwise the nearest one after it that does, java.time's TemporalAdjusters.nextOrSame, and the natural spelling of "the coming Friday...
- [`DateTime.next_weekday`](API-DateTime#next_weekday) The nearest date strictly after this one that falls on the given weekday, java.time's TemporalAdjusters.next.
- [`DateTime.previous_weekday`](API-DateTime#previous_weekday) The nearest date strictly before this one that falls on the given weekday, java.time's TemporalAdjusters.previous.
- [`DateTime.with_date`](API-DateTime#with_date) A copy with the date replaced and the time of day kept.
- [`DateTime.with_day`](API-DateTime#with_day) A copy with the day of month replaced.
- [`DateTime.with_day_of_year`](API-DateTime#with_day_of_year) A copy moved to a given ordinal day of the year, keeping the time of day.
- [`DateTime.with_hour`](API-DateTime#with_hour) A copy with the hour replaced.
- [`DateTime.with_minute`](API-DateTime#with_minute) A copy with the minute replaced.
- [`DateTime.with_month`](API-DateTime#with_month) A copy with the month replaced, clamping the day into the new month.
- [`DateTime.with_ms`](API-DateTime#with_ms) A copy with the millisecond replaced.
- [`DateTime.with_offset`](API-DateTime#with_offset) A copy expressed in a different fixed offset, keeping the civil fields and therefore changing the instant.
- [`DateTime.with_second`](API-DateTime#with_second) A copy with the second replaced.
- [`DateTime.with_time`](API-DateTime#with_time) A copy with the time of day replaced and the date kept.
- [`DateTime.with_weekday`](API-DateTime#with_weekday) A copy moved to a given weekday within the same week, where the week begins on week_start.
- [`DateTime.with_year`](API-DateTime#with_year) A copy with the year replaced.

## Ask a yes or no question about a date

- [`DateTime.clamp_to`](API-DateTime#clamp_to) This instant confined to a range: lo when earlier than lo, hi when later than hi, otherwise itself.
- [`DateTime.is_between`](API-DateTime#is_between) Whether this instant falls in the half-open span [lo, hi).
- [`DateTime.is_leap`](API-DateTime#is_leap) Whether this date's year is a leap year.
- [`DateTime.is_month_end`](API-DateTime#is_month_end) Whether this is the last day of its month.
- [`DateTime.is_month_start`](API-DateTime#is_month_start) Whether this is the first day of its month.
- [`DateTime.is_quarter_end`](API-DateTime#is_quarter_end) Whether this is the last day of its quarter.
- [`DateTime.is_quarter_start`](API-DateTime#is_quarter_start) Whether this is the first day of its quarter.
- [`DateTime.is_weekday`](API-DateTime#is_weekday) Whether this date falls Monday to Friday.
- [`DateTime.is_weekend`](API-DateTime#is_weekend) Whether this date falls on a Saturday or Sunday.
- [`DateTime.is_year_end`](API-DateTime#is_year_end) Whether this is 31 December.
- [`DateTime.is_year_start`](API-DateTime#is_year_start) Whether this is 1 January.
- [`DateTime.length_of_month`](API-DateTime#length_of_month) Number of days in this date's month.
- [`DateTime.length_of_year`](API-DateTime#length_of_year) Number of days in this date's year.
- [`DateTime.until`](API-DateTime#until) The whole number of units from this date-time to another, the generic form of days_between and months_between, so a unit can be chosen at runtime.

## Get today, now, or the epoch

- [`epoch`](API-Functions#epoch) The Unix epoch, 1970-01-01T00:00:00Z.
- [`now`](API-Functions#now) The current moment, in a zone.
- [`today`](API-Functions#today) The current date at true local midnight in a zone, meaning the record's own to_unix() is the instant that midnight actually happened.
- [`try_new_datetime`](API-Functions#try_new_datetime) Build a DateTime, returning na instead of raising when the fields do not describe a real moment.

## Work with time zones and daylight saving

- [`Zone.is_ambiguous`](API-Zone#is_ambiguous) Whether a local civil time happened twice, because a fall-back transition repeated it.
- [`Zone.is_gap`](API-Zone#is_gap) Whether a local civil time never happened, because a spring-forward transition skipped over it.
- [`Zone.rule`](API-Zone#rule) The daylight-saving rule in force for a zone in a given year.
- [`Zone.rules_from`](API-Zone#rules_from) The first year from which a zone's rules are modelled exactly.
- [`Zone.std_offset`](API-Zone#std_offset) The standard, i.e. winter, offset of a zone in hours.
- [`Zone.to_unix`](API-Zone#to_unix) Convert a local civil time in this zone to an instant, resolving gaps and overlaps explicitly rather than silently.
- [`changed`](API-Functions#changed) Whether a unit boundary in a zone falls between two instants: the "is this a new day?" test, answered against a real calendar instead of the chart's own session grid.
- [`dst_end`](API-Functions#dst_end) The instant daylight saving ends in a zone in a year.
- [`dst_start`](API-Functions#dst_start) The instant daylight saving begins in a zone in a year.
- [`is_dst`](API-Functions#is_dst) Whether daylight saving is in force in a zone at an instant.
- [`offset_at`](API-Functions#offset_at) Offset from UTC in force in a zone at an instant, daylight saving applied.
- [`offset_at_rule`](API-Functions#offset_at_rule) Offset in force at an instant under an arbitrary rule.
- [`unix_to_date_zone`](API-Functions#unix_to_date_zone) Convert an instant to civil time in a zone, daylight saving applied.

## Move a date between zones

- [`DateTime.to_zone_same_instant`](API-DateTime#to_zone_same_instant) The same moment expressed in another zone.
- [`DateTime.to_zone_same_local`](API-DateTime#to_zone_same_local) The same wall clock reinterpreted in another zone, which denotes a different moment.

## Find Easter and Good Friday

- [`easter_sunday`](API-Functions#easter_sunday) Easter Sunday, by the anonymous Gregorian computus (Meeus / Jones / Butcher).
- [`good_friday`](API-Functions#good_friday) Good Friday, the Friday before Easter Sunday.

## Work with calendar amounts of time

- [`DateTime.minus_period`](API-DateTime#minus_period) Subtract a Period from a DateTime.
- [`Period.equals`](API-Period#equals) Whether two periods have identical fields.
- [`Period.is_negative`](API-Period#is_negative) Whether any field of this period is negative.
- [`Period.is_zero`](API-Period#is_zero) Whether every field of this period is zero.
- [`Period.minus`](API-Period#minus) The difference of two periods, field by field.
- [`Period.multiplied_by`](API-Period#multiplied_by) This period with every field scaled.
- [`Period.negated`](API-Period#negated) This period with every field's sign flipped.
- [`Period.normalized`](API-Period#normalized) This period with surplus months folded into years, as java.time's Period.normalized: 1 year 15 months becomes 2 years 3 months.
- [`Period.plus`](API-Period#plus) The sum of two periods, field by field.
- [`Period.to_iso`](API-Period#to_iso) This period in ISO-8601 form, e.g. "P1Y2M3D".
- [`Period.to_total_months`](API-Period#to_total_months) The years and months of this period expressed as a month count.
- [`parse_iso_period`](API-Functions#parse_iso_period) Parse an ISO-8601 period such as "P1Y2M3D", "P3M", "P1W", "-P10D" or "P-1Y-2M-3D".

## Work with spans of instants

- [`Interval.contains`](API-Interval#contains) Whether an instant falls inside this interval.
- [`Interval.overlaps`](API-Interval#overlaps) Whether two intervals share any instant.

- [`Interval.abuts`](API-Interval#abuts) Whether two intervals meet exactly end to start without overlapping: the condition under which they can be joined into one without a hole or a double count.
- [`Interval.duration`](API-Interval#duration) The length of this interval in milliseconds.
- [`Interval.encloses`](API-Interval#encloses) Whether this interval wholly contains another.
- [`Interval.equals`](API-Interval#equals) Whether two intervals have identical endpoints.
- [`Interval.gap`](API-Interval#gap) The empty span between two intervals that neither overlap nor touch.
- [`Interval.intersection`](API-Interval#intersection) The overlapping part of two intervals.
- [`Interval.is_empty`](API-Interval#is_empty) Whether this interval contains no instants at all.
- [`merge_intervals`](API-Functions#merge_intervals) The union of a set of intervals: overlapping or exactly abutting spans are joined and empty ones are dropped, so the result is the instants the inputs cover...
- [`new_interval`](API-Functions#new_interval) Build an interval from two instants, ordering them so the result is never reversed.
- [`sort_intervals`](API-Functions#sort_intervals) Sort an array of intervals in place by start, ties by end, and return the same array so a call can chain.

## Ask whether a market is open on a date

- [`DateTime.closed_for_holiday`](API-DateTime#closed_for_holiday) Whether an exchange is shut for a holiday, as a three-valued answer that says so when the question falls outside the calendar's range.
- [`DateTime.holiday_name`](API-DateTime#holiday_name) The name of the holiday or closure shutting an exchange on a date.
- [`DateTime.is_holiday`](API-DateTime#is_holiday) Whether an exchange is closed for a scheduled holiday.
- [`DateTime.is_trading_day`](API-DateTime#is_trading_day) Whether an exchange holds a regular session on a date: not a weekend, not a scheduled holiday.
- [`Exchange.calendar_from`](API-Exchange#calendar_from) The first year an exchange's calendar answers exactly.
- [`Exchange.calendar_through`](API-Exchange#calendar_through) The last year an exchange's calendar answers exactly, or na when its rules extrapolate without a horizon.
- [`Exchange.zone`](API-Exchange#zone) The zone an exchange's local session times are quoted in.
- [`next_holiday_after`](API-Functions#next_holiday_after) The next date an exchange is closed for a holiday, strictly after the date an instant falls on in that exchange's zone.

## Count or move by trading days

- [`DateTime.adjusted`](API-DateTime#adjusted) Roll a date onto a trading day using an ISDA business-day convention.
- [`DateTime.minus_trading_days`](API-DateTime#minus_trading_days) Move backward a number of trading days.
- [`DateTime.next_trading_day`](API-DateTime#next_trading_day) The next trading day strictly after a date, skipping weekends and scheduled holidays.
- [`DateTime.plus_trading_days`](API-DateTime#plus_trading_days) Move forward or backward a number of trading days, skipping weekends and holidays.
- [`DateTime.prev_trading_day`](API-DateTime#prev_trading_day) The previous trading day strictly before a date.
- [`DateTime.trading_day_of_month`](API-DateTime#trading_day_of_month) The ordinal of a date among its month's trading days: 1 on the month's first trading day, trading_days_in_month on its last.
- [`DateTime.trading_days_between`](API-DateTime#trading_days_between) Count of trading days between two dates.
- [`DateTime.weekdays_between`](API-DateTime#weekdays_between) Count of weekdays (Monday through Friday) between two dates, closed form: no loop and no calendar.
- [`first_trading_day_of_month`](API-Functions#first_trading_day_of_month) The first trading day of a month.
- [`last_trading_day_of_month`](API-Functions#last_trading_day_of_month) The last trading day of a month.
- [`trading_days_in_month`](API-Functions#trading_days_in_month) How many trading days a month holds.

## Compute a year fraction for pricing

- [`day_count_days`](API-Functions#day_count_days) The whole-day count a convention measures between two instants: the numerator year_fraction divides, exposed because for the 30/360 family it is not recoverable from the fraction alone.
- [`year_fraction`](API-Functions#year_fraction) Year fraction between two instants under a day-count convention.

## Find an option expiry or VIX settlement

- [`DateTime.is_expiry_day`](API-DateTime#is_expiry_day) Whether a date is an expiry of a given cycle.
- [`DateTime.is_triple_witching`](API-DateTime#is_triple_witching) Whether a date is a quarterly expiry, when index futures, index options and equity options all expire together.
- [`DateTime.weekly_expiry`](API-DateTime#weekly_expiry) The expiry of the weekly contract covering a date: that week's Friday, rolled back to the previous trading day when the Friday does not trade.
- [`ExpiryKind`](API-Enums#expirykind) A listed expiry cycle.
- [`expiries_between`](API-Functions#expiries_between) Every expiry of a cycle whose date falls in a span.
- [`next_expiry_after`](API-Functions#next_expiry_after) The next expiry of a close-settled cycle strictly after an instant.
- [`next_vix_settlement_after`](API-Functions#next_vix_settlement_after) The instant of the next VIX final settlement strictly after a given one.
- [`parse_tenor`](API-Functions#parse_tenor) Parse a tenor string such as "1D", "2W", "3M" or "1Y" into a Period.
- [`quarterly_expiry`](API-Functions#quarterly_expiry) Unix timestamp of a quarterly expiry.
- [`vix_settlement`](API-Functions#vix_settlement) Unix timestamp of a VIX final settlement: the Special Opening Quotation moment, when Cboe's opening auction in the constituent SPX series prints the settlement value.
- [`vix_settlement_day`](API-Functions#vix_settlement_day) VIX final settlement day for a contract month: the Wednesday thirty days before the following month's third Friday...

## Work with trading sessions and bars

- [`Session`](API-Session#session) A recurring local-time window, resolved against a calendar.
- [`Session.bars_per_session`](API-Session#bars_per_session) How many chart bars of a given timeframe this session holds on a date, counting a clipped final bar as a bar.
- [`Session.bounds`](API-Session#bounds) The instants this session occupies on a given start date, or na when it does not run that day.
- [`Session.break_bounds`](API-Session#break_bounds) The intraday break inside this session's window on a given start date.
- [`Session.crosses_midnight`](API-Session#crosses_midnight) Whether this session's window crosses local midnight.
- [`Session.is_first_bar`](API-Session#is_first_bar) Whether a bar is the first bar of this session.
- [`Session.is_last_bar`](API-Session#is_last_bar) Whether a bar is the last bar of this session, answered on that bar, not one bar later.
- [`Session.is_open`](API-Session#is_open) Whether this session is trading at an instant.
- [`Session.length_minutes`](API-Session#length_minutes) The nominal length of this session in minutes, before any half-day adjustment.
- [`Session.progress`](API-Session#progress) How far through this session's envelope an instant sits.
- [`Session.time_to_close`](API-Session#time_to_close) Milliseconds until this session's envelope closes.
- [`Session.time_to_open`](API-Session#time_to_open) Milliseconds until this session's next open, strictly after the given instant.
- [`Session.to_spec`](API-Session#to_spec) This session as a TradingView-style string, e.g. "0930-1600:23456", or "0900-1130,1230-1530:23456" when the session breaks for lunch.
- [`Session.window_after`](API-Session#window_after) The next window of this session that opens strictly after an instant: the upcoming-next window.
- [`Session.window_at`](API-Session#window_at) The session window containing an instant, if any.
- [`Session.window_before`](API-Session#window_before) The most recent window of this session that has already ended at an instant: the completed-previous window.
- [`Session.window_of_bar`](API-Session#window_of_bar) The session window a bar touches, which is not the window that contains one of the bar's edges.
- [`Session.windows_between`](API-Session#windows_between) Every window of this session that intersects a span, in ascending order.
- [`SessionId`](API-Enums#sessionid) Standard trading sessions, ready to use.
- [`day_mask`](API-Functions#day_mask) The weekday bitmask for a contiguous run of days, from one weekday through another inclusive, wrapping past Saturday if it has to.
- [`new_session`](API-Functions#new_session) Build a custom session.
- [`parse_session`](API-Functions#parse_session) Parse a TradingView-style session string such as "0930-1600" or "0930-1600:23456", where the digits after the colon are weekdays with 1 meaning Sunday.
- [`session_of`](API-Functions#session_of) One of the built-in standard sessions.

## Find FOMC dates and index rebalances

- [`DateTime.fomc_day`](API-DateTime#fomc_day) Whether a date falls on either day of a scheduled FOMC meeting.
- [`DateTime.fomc_decision_day`](API-DateTime#fomc_decision_day) Whether a date is the second day of an FOMC meeting, when the statement is released.
- [`Known.is_yes`](API-Enums#is_yes) Collapse a three-valued answer to a bool, treating UNKNOWN as false.
- [`fomc_known_from`](API-Functions#fomc_known_from) The first year for which the FOMC meeting table is known.
- [`fomc_known_through`](API-Functions#fomc_known_through) The last year for which the FOMC meeting table is known.
- [`next_fomc_after`](API-Functions#next_fomc_after) The instant of the next FOMC decision strictly after a given one.
- [`russell_rebalance_day`](API-Functions#russell_rebalance_day) FTSE Russell annual reconstitution: the last Friday in June, one of the highest-volume closes of the year.

## Turn a date into a string

- [`DateTime.to_iso`](API-DateTime#to_iso) Format a DateTime as a full ISO-8601 date-time with its offset designator: the form that survives a round trip, so parse_iso(d.to_iso()) gives back d.
- [`DateTime.to_iso_date`](API-DateTime#to_iso_date) Format a DateTime as an ISO-8601 date only.
- [`DateTime.to_iso_local`](API-DateTime#to_iso_local) Format a DateTime as an ISO-8601 date-time string without the offset designator, i.e. as a local wall-clock reading.
- [`DateTime.to_iso_ordinal_date`](API-DateTime#to_iso_ordinal_date) Format a DateTime as an ISO-8601 ordinal date.
- [`DateTime.to_iso_time`](API-DateTime#to_iso_time) Format a DateTime as an ISO-8601 time only.
- [`DateTime.to_iso_week_date`](API-DateTime#to_iso_week_date) Format a DateTime as an ISO-8601 week date.
- [`Interval.to_iso`](API-Interval#to_iso) This interval in ISO-8601 interval form, "start/end", with both endpoints in UTC.
- [`Weekday.abbr`](API-Weekday#abbr) The three-letter English abbreviation of a weekday.
- [`Weekday.name`](API-Weekday#name) The English name of a weekday.
- [`Zone.to_iana`](API-Zone#to_iana) The IANA identifier for a zone, e.g. "America/New_York".
- [`format_iso_duration`](API-Functions#format_iso_duration) A span of milliseconds in ISO-8601 duration form, e.g. "P2DT4H13M9S".
- [`format_ixdtf`](API-Functions#format_ixdtf) Format an instant in the RFC 9557 extended format, which appends the zone in brackets so the reader knows which rules produced the offset.
- [`format_yymmdd`](API-Functions#format_yymmdd) Format a timestamp as the six-character yyMMdd date fragment used by OPRA-style option symbols, resolved in a zone you name rather than in the chart's...
- [`month_abbr`](API-Functions#month_abbr) The three-letter English abbreviation of a month.
- [`month_name`](API-Functions#month_name) The English name of a month.

- [`DateTime.format`](API-DateTime#format) Format this date-time with a pattern.
- [`format_time`](API-Functions#format_time) Format an instant in a zone.

## Turn a string into a date

- [`parse_iso`](API-Functions#parse_iso) Parse an ISO-8601 date-time.
- [`parse_iso_duration`](API-Functions#parse_iso_duration) Parse an ISO-8601 duration such as "P2DT4H13M9S", "PT1.5S" or "-PT10M" (the form format_iso_duration emits) into exact milliseconds, round-tripping everything that formatter can produce.

## Bridge to Pine's own date built-ins

- [`Weekday.to_pine_dow`](API-Weekday#to_pine_dow) This weekday in Pine's own numbering, where Sunday is 1, the scale used by the dayofweek.* constants and returned by the dayofweek built-in.
- [`format_duration`](API-Functions#format_duration) Format a span of milliseconds as a human-readable duration, largest unit first.
- [`format_relative`](API-Functions#format_relative) An instant described relative to another, the way a human says it: "3d 4h ago" for the past, "in 2h 15m" for the future, "now" within a second either way.
- [`month_from_name`](API-Functions#month_from_name) The month number for an English month name or three-letter abbreviation, case-insensitive.
- [`weekday_from_name`](API-Functions#weekday_from_name) The Weekday for an English day name or three-letter abbreviation, case-insensitive.
- [`weekday_from_pine_dow`](API-Functions#weekday_from_pine_dow) The Weekday for a value from Pine's dayofweek built-in or the dayofweek.* constants, where Sunday is 1.
- [`zone_from_iana`](API-Functions#zone_from_iana) The Zone for an IANA identifier, so a string from syminfo.timezone or a user input can be turned into something the rule engine understands.
- [`zone_offset_string`](API-Functions#zone_offset_string) The offset in force in a zone at an instant, spelled the way Pine's timezone arguments accept it.

## Types and enums

- [`BusinessDay`](API-Enums#businessday) ISDA business-day conventions: how to roll a date that lands on a non-trading day.
- [`DateTime`](API-DateTime#datetime) A civil date-time held together with the fixed UTC offset it is expressed in.
- [`DateTime.equals`](API-DateTime#equals) Whether two date-times denote the same civil fields and the same offset.
- [`DateTime.is_early_close`](API-DateTime#is_early_close) Whether an exchange closes early on a date.
- [`DateTime.normalized`](API-DateTime#normalized) A copy of this DateTime with the day clamped into the length of its month.
- [`DateTime.same_instant`](API-DateTime#same_instant) Whether two date-times are the same instant, regardless of the offset each is expressed in.
- [`DateTime.session_close`](API-DateTime#session_close) The instant an exchange's session closes on a date, accounting for early closes.
- [`DateTime.session_open`](API-DateTime#session_open) The instant an exchange's session opens on a date.
- [`DayCount`](API-Enums#daycount) Day-count conventions, per the ISDA 2006 Definitions.
- [`DstRule`](API-Zone#dstrule) A daylight-saving rule, expressed as data so that adding a zone to the Zone enum is a constant rather than a new code path.
- [`Exchange`](API-Exchange#exchange) An exchange calendar.
- [`Interval`](API-Interval#interval) A half-open span of instants, [FromMS, ToMS).
- [`Known`](API-Enums#known) A three-valued answer, for questions a dated table or a bounded calendar cannot answer outside its window.
- [`Overflow`](API-Enums#overflow) What to do when calendar arithmetic lands on a day that does not exist, e.g. 31 January plus one month.
- [`Period`](API-Period#period) A calendar-flavoured amount of time, in the sense of java.time's Period.
- [`Resolver`](API-Enums#resolver) How to resolve a local time that a daylight-saving transition made impossible or ambiguous.
- [`RoundMode`](API-Enums#roundmode) How to round a date-time to a unit boundary.
- [`TimeUnit`](API-Enums#timeunit) A unit of time, used by the truncation and rounding helpers.
- [`Weekday`](API-Weekday#weekday) Day of the week.
- [`Zone`](API-Zone#zone) A time zone, meaning a standard offset plus a daylight-saving rule, not a fixed offset.
- [`holidays_between`](API-Functions#holidays_between) Every date an exchange is closed for a holiday within a span.
- [`monthly_expiry`](API-Functions#monthly_expiry) Unix timestamp of a standard US equity monthly option expiry at a chosen local close time.
- [`monthly_expiry_day`](API-Functions#monthly_expiry_day) Standard US equity monthly option expiry: the third Friday of the month, moved to the preceding Thursday when that Friday is a market holiday.
