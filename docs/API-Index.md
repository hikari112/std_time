# API Index

Every export in `std_time`, all 240 of them, in one list, so that Ctrl-F finds anything. Sorted by name; the same set sorted by the question you arrived with is on [Task Index](Task-Index).

| Name | Kind | On | Summary |
|---|---|---|---|
| [`Weekday.abbr`](API-Weekday#abbr) | method | Weekday | The three-letter English abbreviation of a weekday. |
| [`Interval.abuts`](API-Interval#abuts) | method | Interval | Whether two intervals meet exactly end to start without overlapping: the condition under which they can be joined into one without a hole or a double count. |
| [`DateTime.adjusted`](API-DateTime#adjusted) | method | DateTime | Roll a date onto a trading day using an ISDA business-day convention. |
| [`Session.bars_per_session`](API-Session#bars_per_session) | method | Session | How many chart bars of a given timeframe this session holds on a date, counting a clipped final bar as a bar. |
| [`Session.bounds`](API-Session#bounds) | method | Session | The instants this session occupies on a given start date, or na when it does not run that day. |
| [`Session.break_bounds`](API-Session#break_bounds) | method | Session | The intraday break inside this session's window on a given start date. |
| [`BusinessDay`](API-Enums#businessday) | enum |  | ISDA business-day conventions: how to roll a date that lands on a non-trading day. |
| [`Exchange.calendar_from`](API-Exchange#calendar_from) | method | Exchange | The first year an exchange's calendar answers exactly. |
| [`Exchange.calendar_through`](API-Exchange#calendar_through) | method | Exchange | The last year an exchange's calendar answers exactly, or na when its rules extrapolate without a horizon. |
| [`changed`](API-Functions#changed) | function |  | Whether a unit boundary in a zone falls between two instants: the "is this a new day?" test, answered against a real calendar instead of the chart's own session grid. |
| [`DateTime.clamp_to`](API-DateTime#clamp_to) | method | DateTime | This instant confined to a range: lo when earlier than lo, hi when later than hi, otherwise itself. |
| [`DateTime.closed_for_holiday`](API-DateTime#closed_for_holiday) | method | DateTime | Whether an exchange is shut for a holiday, as a three-valued answer that says so when the question falls outside the calendar's range. |
| [`DateTime.compare`](API-DateTime#compare) | method | DateTime | Compare two date-times as instants, so differing offsets compare correctly. |
| [`Interval.contains`](API-Interval#contains) | method | Interval | Whether an instant falls inside this interval. |
| [`Session.crosses_midnight`](API-Session#crosses_midnight) | method | Session | Whether this session's window crosses local midnight. |
| [`date_from_day_of_year`](API-Functions#date_from_day_of_year) | function |  | Civil date for an ordinal day of the year. |
| [`date_from_iso_week`](API-Functions#date_from_iso_week) | function |  | Civil date for an ISO-8601 week date. |
| [`date_to_unix`](API-Functions#date_to_unix) | function |  | Convert a civil date-time to a Unix timestamp. |
| [`date_to_weekday`](API-Functions#date_to_weekday) | function |  | Day of week for a civil date, derived from the same civil algorithm as every other function here. |
| [`DateTime`](API-DateTime#datetime) | type |  | A civil date-time held together with the fixed UTC offset it is expressed in. |
| [`day_count_days`](API-Functions#day_count_days) | function |  | The whole-day count a convention measures between two instants: the numerator year_fraction divides, exposed because for the 30/360 family it is not recoverable from the fraction alone. |
| [`day_mask`](API-Functions#day_mask) | function |  | The weekday bitmask for a contiguous run of days, from one weekday through another inclusive, wrapping past Saturday if it has to. |
| [`DateTime.day_of_year`](API-DateTime#day_of_year) | method | DateTime | Day of the year, 1 for 1 January. |
| [`DayCount`](API-Enums#daycount) | enum |  | Day-count conventions, per the ISDA 2006 Definitions. |
| [`DateTime.days_between`](API-DateTime#days_between) | method | DateTime | Whole calendar days from this date to another, ignoring time of day. |
| [`days_from_civil`](API-Functions#days_from_civil) | function |  | Days elapsed from 1970-01-01 to a civil date. |
| [`days_in_month`](API-Functions#days_in_month) | function |  | Number of days in a given month. |
| [`days_in_year`](API-Functions#days_in_year) | function |  | Number of days in a given year. |
| [`Weekday.days_until`](API-Weekday#days_until) | method | Weekday | Forward distance in days from this weekday to another, never negative. |
| [`dst_end`](API-Functions#dst_end) | function |  | The instant daylight saving ends in a zone in a year. |
| [`dst_start`](API-Functions#dst_start) | function |  | The instant daylight saving begins in a zone in a year. |
| [`DstRule`](API-Zone#dstrule) | type |  | A daylight-saving rule, expressed as data so that adding a zone to the Zone enum is a constant rather than a new code path. |
| [`Interval.duration`](API-Interval#duration) | method | Interval | The length of this interval in milliseconds. |
| [`DateTime.earlier`](API-DateTime#earlier) | method | DateTime | The earlier of two date-times, as instants. |
| [`easter_sunday`](API-Functions#easter_sunday) | function |  | Easter Sunday, by the anonymous Gregorian computus (Meeus / Jones / Butcher). |
| [`Interval.encloses`](API-Interval#encloses) | method | Interval | Whether this interval wholly contains another. |
| [`DateTime.end_of`](API-DateTime#end_of) | method | DateTime | The last instant of the unit containing this date-time, i.e. one millisecond before the next unit begins. |
| [`epoch`](API-Functions#epoch) | function |  | The Unix epoch, 1970-01-01T00:00:00Z. |
| [`DateTime.equals`](API-DateTime#equals) | method | DateTime | Whether two date-times denote the same civil fields and the same offset. |
| [`Interval.equals`](API-Interval#equals) | method | Interval | Whether two intervals have identical endpoints. |
| [`Period.equals`](API-Period#equals) | method | Period | Whether two periods have identical fields. |
| [`Exchange`](API-Exchange#exchange) | enum |  | An exchange calendar. |
| [`expiries_between`](API-Functions#expiries_between) | function |  | Every expiry of a cycle whose date falls in a span. |
| [`ExpiryKind`](API-Enums#expirykind) | enum |  | A listed expiry cycle. |
| [`first_trading_day_of_month`](API-Functions#first_trading_day_of_month) | function |  | The first trading day of a month. |
| [`DateTime.fomc_day`](API-DateTime#fomc_day) | method | DateTime | Whether a date falls on either day of a scheduled FOMC meeting. |
| [`DateTime.fomc_decision_day`](API-DateTime#fomc_decision_day) | method | DateTime | Whether a date is the second day of an FOMC meeting, when the statement is released. |
| [`fomc_known_from`](API-Functions#fomc_known_from) | function |  | The first year for which the FOMC meeting table is known. |
| [`fomc_known_through`](API-Functions#fomc_known_through) | function |  | The last year for which the FOMC meeting table is known. |
| [`DateTime.format`](API-DateTime#format) | method | DateTime | Format this date-time with a pattern. |
| [`format_duration`](API-Functions#format_duration) | function |  | Format a span of milliseconds as a human-readable duration, largest unit first. |
| [`format_iso_duration`](API-Functions#format_iso_duration) | function |  | A span of milliseconds in ISO-8601 duration form, e.g. "P2DT4H13M9S". |
| [`format_ixdtf`](API-Functions#format_ixdtf) | function |  | Format an instant in the RFC 9557 extended format, which appends the zone in brackets so the reader knows which rules produced the offset. |
| [`format_relative`](API-Functions#format_relative) | function |  | An instant described relative to another, the way a human says it: "3d 4h ago" for the past, "in 2h 15m" for the future, "now" within a second either way. |
| [`format_time`](API-Functions#format_time) | function |  | Format an instant in a zone. |
| [`format_yymmdd`](API-Functions#format_yymmdd) | function |  | Format a timestamp as the six-character yyMMdd date fragment used by OPRA-style option symbols, resolved in a zone you name rather than in the chart's... |
| [`Interval.gap`](API-Interval#gap) | method | Interval | The empty span between two intervals that neither overlap nor touch. |
| [`good_friday`](API-Functions#good_friday) | function |  | Good Friday, the Friday before Easter Sunday. |
| [`DateTime.holiday_name`](API-DateTime#holiday_name) | method | DateTime | The name of the holiday or closure shutting an exchange on a date. |
| [`holidays_between`](API-Functions#holidays_between) | function |  | Every date an exchange is closed for a holiday within a span. |
| [`Interval.intersection`](API-Interval#intersection) | method | Interval | The overlapping part of two intervals. |
| [`Interval`](API-Interval#interval) | type |  | A half-open span of instants, [FromMS, ToMS). |
| [`DateTime.is_after`](API-DateTime#is_after) | method | DateTime | Whether this date-time is strictly later than another, as instants. |
| [`Zone.is_ambiguous`](API-Zone#is_ambiguous) | method | Zone | Whether a local civil time happened twice, because a fall-back transition repeated it. |
| [`DateTime.is_before`](API-DateTime#is_before) | method | DateTime | Whether this date-time is strictly earlier than another, as instants. |
| [`DateTime.is_between`](API-DateTime#is_between) | method | DateTime | Whether this instant falls in the half-open span [lo, hi). |
| [`is_dst`](API-Functions#is_dst) | function |  | Whether daylight saving is in force in a zone at an instant. |
| [`DateTime.is_early_close`](API-DateTime#is_early_close) | method | DateTime | Whether an exchange closes early on a date. |
| [`Interval.is_empty`](API-Interval#is_empty) | method | Interval | Whether this interval contains no instants at all. |
| [`DateTime.is_expiry_day`](API-DateTime#is_expiry_day) | method | DateTime | Whether a date is an expiry of a given cycle. |
| [`Session.is_first_bar`](API-Session#is_first_bar) | method | Session | Whether a bar is the first bar of this session. |
| [`Zone.is_gap`](API-Zone#is_gap) | method | Zone | Whether a local civil time never happened, because a spring-forward transition skipped over it. |
| [`DateTime.is_holiday`](API-DateTime#is_holiday) | method | DateTime | Whether an exchange is closed for a scheduled holiday. |
| [`Session.is_last_bar`](API-Session#is_last_bar) | method | Session | Whether a bar is the last bar of this session, answered on that bar, not one bar later. |
| [`DateTime.is_leap`](API-DateTime#is_leap) | method | DateTime | Whether this date's year is a leap year. |
| [`is_leap_year`](API-Functions#is_leap_year) | function |  | Whether a year is a leap year in the proleptic Gregorian calendar. |
| [`DateTime.is_month_end`](API-DateTime#is_month_end) | method | DateTime | Whether this is the last day of its month. |
| [`DateTime.is_month_start`](API-DateTime#is_month_start) | method | DateTime | Whether this is the first day of its month. |
| [`Period.is_negative`](API-Period#is_negative) | method | Period | Whether any field of this period is negative. |
| [`Session.is_open`](API-Session#is_open) | method | Session | Whether this session is trading at an instant. |
| [`DateTime.is_quarter_end`](API-DateTime#is_quarter_end) | method | DateTime | Whether this is the last day of its quarter. |
| [`DateTime.is_quarter_start`](API-DateTime#is_quarter_start) | method | DateTime | Whether this is the first day of its quarter. |
| [`DateTime.is_trading_day`](API-DateTime#is_trading_day) | method | DateTime | Whether an exchange holds a regular session on a date: not a weekend, not a scheduled holiday. |
| [`DateTime.is_triple_witching`](API-DateTime#is_triple_witching) | method | DateTime | Whether a date is a quarterly expiry, when index futures, index options and equity options all expire together. |
| [`is_valid_date`](API-Functions#is_valid_date) | function |  | Whether a civil moment exists, without raising. |
| [`DateTime.is_weekday`](API-DateTime#is_weekday) | method | DateTime | Whether this date falls Monday to Friday. |
| [`DateTime.is_weekend`](API-DateTime#is_weekend) | method | DateTime | Whether this date falls on a Saturday or Sunday. |
| [`DateTime.is_year_end`](API-DateTime#is_year_end) | method | DateTime | Whether this is 31 December. |
| [`DateTime.is_year_start`](API-DateTime#is_year_start) | method | DateTime | Whether this is 1 January. |
| [`Known.is_yes`](API-Enums#is_yes) | method | Known | Collapse a three-valued answer to a bool, treating UNKNOWN as false. |
| [`Period.is_zero`](API-Period#is_zero) | method | Period | Whether every field of this period is zero. |
| [`DateTime.iso_week`](API-DateTime#iso_week) | method | DateTime | ISO-8601 week number. |
| [`DateTime.iso_week_year`](API-DateTime#iso_week_year) | method | DateTime | ISO-8601 week-based year, which is not always the calendar year: 2027-01-01 belongs to week-year 2026. |
| [`Known`](API-Enums#known) | enum |  | A three-valued answer, for questions a dated table or a bounded calendar cannot answer outside its window. |
| [`last_trading_day_of_month`](API-Functions#last_trading_day_of_month) | function |  | The last trading day of a month. |
| [`DateTime.later`](API-DateTime#later) | method | DateTime | The later of two date-times, as instants. |
| [`Session.length_minutes`](API-Session#length_minutes) | method | Session | The nominal length of this session in minutes, before any half-day adjustment. |
| [`DateTime.length_of_month`](API-DateTime#length_of_month) | method | DateTime | Number of days in this date's month. |
| [`DateTime.length_of_year`](API-DateTime#length_of_year) | method | DateTime | Number of days in this date's year. |
| [`merge_intervals`](API-Functions#merge_intervals) | function |  | The union of a set of intervals: overlapping or exactly abutting spans are joined and empty ones are dropped, so the result is the instants the inputs cover... |
| [`Period.minus`](API-Period#minus) | method | Period | The difference of two periods, field by field. |
| [`Weekday.minus`](API-Weekday#minus) | method | Weekday | The weekday n days earlier in the weekly cycle, wrapping. |
| [`DateTime.minus_days`](API-DateTime#minus_days) | method | DateTime | Subtract whole calendar days, preserving wall-clock time of day. |
| [`DateTime.minus_hours`](API-DateTime#minus_hours) | method | DateTime | Subtract hours from the instant. |
| [`DateTime.minus_minutes`](API-DateTime#minus_minutes) | method | DateTime | Subtract minutes from the instant. |
| [`DateTime.minus_months`](API-DateTime#minus_months) | method | DateTime | Subtract whole calendar months, with plus_months' clamping rule: 31 March minus one month is 28 or 29 February. |
| [`DateTime.minus_ms`](API-DateTime#minus_ms) | method | DateTime | Subtract milliseconds from the instant. |
| [`DateTime.minus_period`](API-DateTime#minus_period) | method | DateTime | Subtract a Period from a DateTime. |
| [`DateTime.minus_seconds`](API-DateTime#minus_seconds) | method | DateTime | Subtract seconds from the instant. |
| [`DateTime.minus_trading_days`](API-DateTime#minus_trading_days) | method | DateTime | Move backward a number of trading days. |
| [`DateTime.minus_weeks`](API-DateTime#minus_weeks) | method | DateTime | Subtract whole calendar weeks, preserving wall-clock time of day. |
| [`DateTime.minus_years`](API-DateTime#minus_years) | method | DateTime | Subtract whole calendar years, with the same clamping rule: 29 February minus one year is 28 February. |
| [`month_abbr`](API-Functions#month_abbr) | function |  | The three-letter English abbreviation of a month. |
| [`month_from_name`](API-Functions#month_from_name) | function |  | The month number for an English month name or three-letter abbreviation, case-insensitive. |
| [`month_name`](API-Functions#month_name) | function |  | The English name of a month. |
| [`monthly_expiry`](API-Functions#monthly_expiry) | function |  | Unix timestamp of a standard US equity monthly option expiry at a chosen local close time. |
| [`monthly_expiry_day`](API-Functions#monthly_expiry_day) | function |  | Standard US equity monthly option expiry: the third Friday of the month, moved to the preceding Thursday when that Friday is a market holiday. |
| [`DateTime.months_between`](API-DateTime#months_between) | method | DateTime | Whole calendar months from this date to another, in the sense of java.time's ChronoUnit.MONTHS.between: a partial month does not count. |
| [`Period.multiplied_by`](API-Period#multiplied_by) | method | Period | This period with every field scaled. |
| [`Weekday.name`](API-Weekday#name) | method | Weekday | The English name of a weekday. |
| [`Period.negated`](API-Period#negated) | method | Period | This period with every field's sign flipped. |
| [`new_datetime`](API-Functions#new_datetime) | function |  | Build a DateTime from civil fields. |
| [`new_interval`](API-Functions#new_interval) | function |  | Build an interval from two instants, ordering them so the result is never reversed. |
| [`new_session`](API-Functions#new_session) | function |  | Build a custom session. |
| [`next_expiry_after`](API-Functions#next_expiry_after) | function |  | The next expiry of a close-settled cycle strictly after an instant. |
| [`next_fomc_after`](API-Functions#next_fomc_after) | function |  | The instant of the next FOMC decision strictly after a given one. |
| [`next_holiday_after`](API-Functions#next_holiday_after) | function |  | The next date an exchange is closed for a holiday, strictly after the date an instant falls on in that exchange's zone. |
| [`DateTime.next_or_same_weekday`](API-DateTime#next_or_same_weekday) | method | DateTime | This date when it already falls on the given weekday, otherwise the nearest one after it that does, java.time's TemporalAdjusters.nextOrSame, and the natural spelling of "the coming Friday... |
| [`DateTime.next_trading_day`](API-DateTime#next_trading_day) | method | DateTime | The next trading day strictly after a date, skipping weekends and scheduled holidays. |
| [`next_vix_settlement_after`](API-Functions#next_vix_settlement_after) | function |  | The instant of the next VIX final settlement strictly after a given one. |
| [`DateTime.next_weekday`](API-DateTime#next_weekday) | method | DateTime | The nearest date strictly after this one that falls on the given weekday, java.time's TemporalAdjusters.next. |
| [`DateTime.normalized`](API-DateTime#normalized) | method | DateTime | A copy of this DateTime with the day clamped into the length of its month. |
| [`Period.normalized`](API-Period#normalized) | method | Period | This period with surplus months folded into years, as java.time's Period.normalized: 1 year 15 months becomes 2 years 3 months. |
| [`now`](API-Functions#now) | function |  | The current moment, in a zone. |
| [`nth_weekday_of_month`](API-Functions#nth_weekday_of_month) | function |  | Day of month of the nth given weekday, following java.time's dayOfWeekInMonth semantics. |
| [`offset_at`](API-Functions#offset_at) | function |  | Offset from UTC in force in a zone at an instant, daylight saving applied. |
| [`offset_at_rule`](API-Functions#offset_at_rule) | function |  | Offset in force at an instant under an arbitrary rule. |
| [`Overflow`](API-Enums#overflow) | enum |  | What to do when calendar arithmetic lands on a day that does not exist, e.g. 31 January plus one month. |
| [`Interval.overlaps`](API-Interval#overlaps) | method | Interval | Whether two intervals share any instant. |
| [`parse_iso`](API-Functions#parse_iso) | function |  | Parse an ISO-8601 date-time. |
| [`parse_iso_duration`](API-Functions#parse_iso_duration) | function |  | Parse an ISO-8601 duration such as "P2DT4H13M9S", "PT1.5S" or "-PT10M" (the form format_iso_duration emits) into exact milliseconds, round-tripping everything that formatter can produce. |
| [`parse_iso_period`](API-Functions#parse_iso_period) | function |  | Parse an ISO-8601 period such as "P1Y2M3D", "P3M", "P1W", "-P10D" or "P-1Y-2M-3D". |
| [`parse_session`](API-Functions#parse_session) | function |  | Parse a TradingView-style session string such as "0930-1600" or "0930-1600:23456", where the digits after the colon are weekdays with 1 meaning Sunday. |
| [`parse_tenor`](API-Functions#parse_tenor) | function |  | Parse a tenor string such as "1D", "2W", "3M" or "1Y" into a Period. |
| [`Period`](API-Period#period) | type |  | A calendar-flavoured amount of time, in the sense of java.time's Period. |
| [`DateTime.period_between`](API-DateTime#period_between) | method | DateTime | The Period between two dates, following java.time's Period.between: whole months first, then the day remainder, with years and months truncated toward zero so every component carries the same sign. |
| [`Period.plus`](API-Period#plus) | method | Period | The sum of two periods, field by field. |
| [`Weekday.plus`](API-Weekday#plus) | method | Weekday | The weekday n days later in the weekly cycle, wrapping. |
| [`DateTime.plus_days`](API-DateTime#plus_days) | method | DateTime | Add whole calendar days, preserving wall-clock time of day. |
| [`DateTime.plus_hours`](API-DateTime#plus_hours) | method | DateTime | Add hours to the instant. |
| [`DateTime.plus_minutes`](API-DateTime#plus_minutes) | method | DateTime | Add minutes to the instant. |
| [`DateTime.plus_months`](API-DateTime#plus_months) | method | DateTime | Add whole calendar months, following java.time: the day of month is clamped to the length of the target month, so 31 January plus one month is 28 or 29 February. |
| [`DateTime.plus_ms`](API-DateTime#plus_ms) | method | DateTime | Add milliseconds to the instant. |
| [`DateTime.plus_period`](API-DateTime#plus_period) | method | DateTime | Add a Period. |
| [`DateTime.plus_seconds`](API-DateTime#plus_seconds) | method | DateTime | Add seconds to the instant. |
| [`DateTime.plus_trading_days`](API-DateTime#plus_trading_days) | method | DateTime | Move forward or backward a number of trading days, skipping weekends and holidays. |
| [`DateTime.plus_weeks`](API-DateTime#plus_weeks) | method | DateTime | Add whole calendar weeks, preserving wall-clock time of day. |
| [`DateTime.plus_years`](API-DateTime#plus_years) | method | DateTime | Add whole calendar years, with the same clamping rule as plus_months: 29 February plus one year is 28 February. |
| [`DateTime.prev_trading_day`](API-DateTime#prev_trading_day) | method | DateTime | The previous trading day strictly before a date. |
| [`DateTime.previous_weekday`](API-DateTime#previous_weekday) | method | DateTime | The nearest date strictly before this one that falls on the given weekday, java.time's TemporalAdjusters.previous. |
| [`Session.progress`](API-Session#progress) | method | Session | How far through this session's envelope an instant sits. |
| [`quarter`](API-Functions#quarter) | function |  | Calendar quarter containing a month, or the fiscal quarter, when the fiscal year begins in some other month. |
| [`quarterly_expiry`](API-Functions#quarterly_expiry) | function |  | Unix timestamp of a quarterly expiry. |
| [`Resolver`](API-Enums#resolver) | enum |  | How to resolve a local time that a daylight-saving transition made impossible or ambiguous. |
| [`DateTime.round_to`](API-DateTime#round_to) | method | DateTime | Round this date-time to a unit boundary. |
| [`RoundMode`](API-Enums#roundmode) | enum |  | How to round a date-time to a unit boundary. |
| [`Zone.rule`](API-Zone#rule) | method | Zone | The daylight-saving rule in force for a zone in a given year. |
| [`Zone.rules_from`](API-Zone#rules_from) | method | Zone | The first year from which a zone's rules are modelled exactly. |
| [`russell_rebalance_day`](API-Functions#russell_rebalance_day) | function |  | FTSE Russell annual reconstitution: the last Friday in June, one of the highest-volume closes of the year. |
| [`DateTime.same_instant`](API-DateTime#same_instant) | method | DateTime | Whether two date-times are the same instant, regardless of the offset each is expressed in. |
| [`Session`](API-Session#session) | type |  | A recurring local-time window, resolved against a calendar. |
| [`DateTime.session_close`](API-DateTime#session_close) | method | DateTime | The instant an exchange's session closes on a date, accounting for early closes. |
| [`session_of`](API-Functions#session_of) | function |  | One of the built-in standard sessions. |
| [`DateTime.session_open`](API-DateTime#session_open) | method | DateTime | The instant an exchange's session opens on a date. |
| [`SessionId`](API-Enums#sessionid) | enum |  | Standard trading sessions, ready to use. |
| [`sort_intervals`](API-Functions#sort_intervals) | function |  | Sort an array of intervals in place by start, ties by end, and return the same array so a call can chain. |
| [`DateTime.start_of`](API-DateTime#start_of) | method | DateTime | The first instant of the unit containing this date-time. |
| [`Zone.std_offset`](API-Zone#std_offset) | method | Zone | The standard, i.e. winter, offset of a zone in hours. |
| [`Session.time_to_close`](API-Session#time_to_close) | method | Session | Milliseconds until this session's envelope closes. |
| [`Session.time_to_open`](API-Session#time_to_open) | method | Session | Milliseconds until this session's next open, strictly after the given instant. |
| [`TimeUnit`](API-Enums#timeunit) | enum |  | A unit of time, used by the truncation and rounding helpers. |
| [`Zone.to_iana`](API-Zone#to_iana) | method | Zone | The IANA identifier for a zone, e.g. "America/New_York". |
| [`Weekday.to_int`](API-Weekday#to_int) | method | Weekday | Numeric code for a weekday, 0 = Sunday through 6 = Saturday. |
| [`DateTime.to_iso`](API-DateTime#to_iso) | method | DateTime | Format a DateTime as a full ISO-8601 date-time with its offset designator: the form that survives a round trip, so parse_iso(d.to_iso()) gives back d. |
| [`Interval.to_iso`](API-Interval#to_iso) | method | Interval | This interval in ISO-8601 interval form, "start/end", with both endpoints in UTC. |
| [`Period.to_iso`](API-Period#to_iso) | method | Period | This period in ISO-8601 form, e.g. "P1Y2M3D". |
| [`DateTime.to_iso_date`](API-DateTime#to_iso_date) | method | DateTime | Format a DateTime as an ISO-8601 date only. |
| [`Weekday.to_iso_dow`](API-Weekday#to_iso_dow) | method | Weekday | ISO-8601 numbering for this weekday, 1 = Monday through 7 = Sunday. |
| [`DateTime.to_iso_local`](API-DateTime#to_iso_local) | method | DateTime | Format a DateTime as an ISO-8601 date-time string without the offset designator, i.e. as a local wall-clock reading. |
| [`DateTime.to_iso_ordinal_date`](API-DateTime#to_iso_ordinal_date) | method | DateTime | Format a DateTime as an ISO-8601 ordinal date. |
| [`DateTime.to_iso_time`](API-DateTime#to_iso_time) | method | DateTime | Format a DateTime as an ISO-8601 time only. |
| [`DateTime.to_iso_week_date`](API-DateTime#to_iso_week_date) | method | DateTime | Format a DateTime as an ISO-8601 week date. |
| [`Weekday.to_pine_dow`](API-Weekday#to_pine_dow) | method | Weekday | This weekday in Pine's own numbering, where Sunday is 1, the scale used by the dayofweek.* constants and returned by the dayofweek built-in. |
| [`Session.to_spec`](API-Session#to_spec) | method | Session | This session as a TradingView-style string, e.g. "0930-1600:23456", or "0900-1130,1230-1530:23456" when the session breaks for lunch. |
| [`Period.to_total_months`](API-Period#to_total_months) | method | Period | The years and months of this period expressed as a month count. |
| [`DateTime.to_unix`](API-DateTime#to_unix) | method | DateTime | The Unix timestamp this DateTime denotes, using the offset it carries. |
| [`Zone.to_unix`](API-Zone#to_unix) | method | Zone | Convert a local civil time in this zone to an instant, resolving gaps and overlaps explicitly rather than silently. |
| [`DateTime.to_zone_same_instant`](API-DateTime#to_zone_same_instant) | method | DateTime | The same moment expressed in another zone. |
| [`DateTime.to_zone_same_local`](API-DateTime#to_zone_same_local) | method | DateTime | The same wall clock reinterpreted in another zone, which denotes a different moment. |
| [`today`](API-Functions#today) | function |  | The current date at true local midnight in a zone, meaning the record's own to_unix() is the instant that midnight actually happened. |
| [`DateTime.trading_day_of_month`](API-DateTime#trading_day_of_month) | method | DateTime | The ordinal of a date among its month's trading days: 1 on the month's first trading day, trading_days_in_month on its last. |
| [`DateTime.trading_days_between`](API-DateTime#trading_days_between) | method | DateTime | Count of trading days between two dates. |
| [`trading_days_in_month`](API-Functions#trading_days_in_month) | function |  | How many trading days a month holds. |
| [`try_new_datetime`](API-Functions#try_new_datetime) | function |  | Build a DateTime, returning na instead of raising when the fields do not describe a real moment. |
| [`unix_to_date`](API-Functions#unix_to_date) | function |  | Convert a Unix timestamp to a civil date-time. |
| [`unix_to_date_zone`](API-Functions#unix_to_date_zone) | function |  | Convert an instant to civil time in a zone, daylight saving applied. |
| [`DateTime.until`](API-DateTime#until) | method | DateTime | The whole number of units from this date-time to another, the generic form of days_between and months_between, so a unit can be chosen at runtime. |
| [`vix_settlement`](API-Functions#vix_settlement) | function |  | Unix timestamp of a VIX final settlement: the Special Opening Quotation moment, when Cboe's opening auction in the constituent SPX series prints the settlement value. |
| [`vix_settlement_day`](API-Functions#vix_settlement_day) | function |  | VIX final settlement day for a contract month: the Wednesday thirty days before the following month's third Friday... |
| [`DateTime.week_of_month`](API-DateTime#week_of_month) | method | DateTime | Which week-row of its month this date falls in, where week 1 is the possibly-partial week containing the 1st. |
| [`DateTime.weekday`](API-DateTime#weekday) | method | DateTime | The weekday of this date, computed from the calendar on every call. |
| [`Weekday`](API-Weekday#weekday) | enum |  | Day of the week. |
| [`weekday_from_int`](API-Functions#weekday_from_int) | function |  | Weekday for a numeric code, 0 = Sunday through 6 = Saturday. |
| [`weekday_from_name`](API-Functions#weekday_from_name) | function |  | The Weekday for an English day name or three-letter abbreviation, case-insensitive. |
| [`weekday_from_pine_dow`](API-Functions#weekday_from_pine_dow) | function |  | The Weekday for a value from Pine's dayofweek built-in or the dayofweek.* constants, where Sunday is 1. |
| [`DateTime.weekday_ordinal_in_month`](API-DateTime#weekday_ordinal_in_month) | method | DateTime | Which occurrence of its own weekday this date is within its month: the 3rd Friday answers 3. |
| [`DateTime.weekdays_between`](API-DateTime#weekdays_between) | method | DateTime | Count of weekdays (Monday through Friday) between two dates, closed form: no loop and no calendar. |
| [`DateTime.weekly_expiry`](API-DateTime#weekly_expiry) | method | DateTime | The expiry of the weekly contract covering a date: that week's Friday, rolled back to the previous trading day when the Friday does not trade. |
| [`Session.window_after`](API-Session#window_after) | method | Session | The next window of this session that opens strictly after an instant: the upcoming-next window. |
| [`Session.window_at`](API-Session#window_at) | method | Session | The session window containing an instant, if any. |
| [`Session.window_before`](API-Session#window_before) | method | Session | The most recent window of this session that has already ended at an instant: the completed-previous window. |
| [`Session.window_of_bar`](API-Session#window_of_bar) | method | Session | The session window a bar touches, which is not the window that contains one of the bar's edges. |
| [`Session.windows_between`](API-Session#windows_between) | method | Session | Every window of this session that intersects a span, in ascending order. |
| [`DateTime.with_date`](API-DateTime#with_date) | method | DateTime | A copy with the date replaced and the time of day kept. |
| [`DateTime.with_day`](API-DateTime#with_day) | method | DateTime | A copy with the day of month replaced. |
| [`DateTime.with_day_of_year`](API-DateTime#with_day_of_year) | method | DateTime | A copy moved to a given ordinal day of the year, keeping the time of day. |
| [`DateTime.with_hour`](API-DateTime#with_hour) | method | DateTime | A copy with the hour replaced. |
| [`DateTime.with_minute`](API-DateTime#with_minute) | method | DateTime | A copy with the minute replaced. |
| [`DateTime.with_month`](API-DateTime#with_month) | method | DateTime | A copy with the month replaced, clamping the day into the new month. |
| [`DateTime.with_ms`](API-DateTime#with_ms) | method | DateTime | A copy with the millisecond replaced. |
| [`DateTime.with_offset`](API-DateTime#with_offset) | method | DateTime | A copy expressed in a different fixed offset, keeping the civil fields and therefore changing the instant. |
| [`DateTime.with_second`](API-DateTime#with_second) | method | DateTime | A copy with the second replaced. |
| [`DateTime.with_time`](API-DateTime#with_time) | method | DateTime | A copy with the time of day replaced and the date kept. |
| [`DateTime.with_weekday`](API-DateTime#with_weekday) | method | DateTime | A copy moved to a given weekday within the same week, where the week begins on week_start. |
| [`DateTime.with_year`](API-DateTime#with_year) | method | DateTime | A copy with the year replaced. |
| [`year_fraction`](API-Functions#year_fraction) | function |  | Year fraction between two instants under a day-count convention. |
| [`Exchange.zone`](API-Exchange#zone) | method | Exchange | The zone an exchange's local session times are quoted in. |
| [`Zone`](API-Zone#zone) | enum |  | A time zone, meaning a standard offset plus a daylight-saving rule, not a fixed offset. |
| [`zone_from_iana`](API-Functions#zone_from_iana) | function |  | The Zone for an IANA identifier, so a string from syminfo.timezone or a user input can be turned into something the rule engine understands. |
| [`zone_offset_string`](API-Functions#zone_offset_string) | function |  | The offset in force in a zone at an instant, spelled the way Pine's timezone arguments accept it. |
