# Enums

> Concepts first: read **[Core Concepts](Core-Concepts)** before this page.

Signatures below are shown as the library declares them. From a script that imports it, every type and enum name takes your import alias: `t.DateTime`, `t.Overflow.REJECT`, `t.Exchange.NYSE`. A bare `DateTime` will not compile.

The option enums: the ones that name a choice rather than a thing. Enums stand in for bare ints and bools throughout the library, because a `Weekday` cannot be silently off by one and a `Known.UNKNOWN` will not type-check where a bool is expected. The three enums that carry methods of their own live with them: [Zone](API-Zone), [Exchange](API-Exchange) and [Weekday](API-Weekday).

## Members

| | Summary |
|---|---|
| [`is_yes`](#is_yes) | Collapse a three-valued answer to a bool, treating UNKNOWN as false. |

## Reference

### is_yes

```pine
Known.is_yes()
```

Collapse a three-valued answer to a bool, treating UNKNOWN as false. Only call this after checking coverage first (fomc_known_from and fomc_known_through, or calendar_from and calendar_through), because it reads "not known" as "no".

**Returns** &nbsp; true only for YES..

**See also** &nbsp; [`calendar_from`](API-Exchange#calendar_from), [`calendar_through`](API-Exchange#calendar_through), [`fomc_known_from`](API-Functions#fomc_known_from), [`fomc_known_through`](API-Functions#fomc_known_through)

## Enums

| | Summary |
|---|---|
| [`BusinessDay`](#businessday) | ISDA business-day conventions: how to roll a date that lands on a non-trading day. |
| [`DayCount`](#daycount) | Day-count conventions, per the ISDA 2006 Definitions. |
| [`ExpiryKind`](#expirykind) | A listed expiry cycle. |
| [`Known`](#known) | A three-valued answer, for questions a dated table or a bounded calendar cannot answer outside its window. |
| [`Overflow`](#overflow) | What to do when calendar arithmetic lands on a day that does not exist, e.g. 31 January plus one month. |
| [`Resolver`](#resolver) | How to resolve a local time that a daylight-saving transition made impossible or ambiguous. |
| [`RoundMode`](#roundmode) | How to round a date-time to a unit boundary. |
| [`SessionId`](#sessionid) | Standard trading sessions, ready to use. |
| [`TimeUnit`](#timeunit) | A unit of time, used by the truncation and rounding helpers. |

### BusinessDay

*enum*

ISDA business-day conventions: how to roll a date that lands on a non-trading day.

| Member | Declared as | Meaning |
|---|---|---|
| `UNADJUSTED` | `UNADJUSTED = "Unadjusted"` | Leave the date alone even if the market is shut. |
| `FOLLOWING` | `FOLLOWING = "Following"` | Move forward to the next trading day. |
| `MOD_FOLLOWING` | `MOD_FOLLOWING = "Modified following"` | Move forward, unless that crosses into the next month, in which case move backward instead. |
| `PRECEDING` | `PRECEDING = "Preceding"` | Move backward to the previous trading day. |
| `MOD_PRECEDING` | `MOD_PRECEDING = "Modified preceding"` | Move backward, unless that crosses into the previous month, in which case move forward instead. |

### DayCount

*enum*

Day-count conventions, per the ISDA 2006 Definitions. The convention is the denominator of every rate and the tau of every option price.

| Member | Declared as | Meaning |
|---|---|---|
| `ACT_365F` | `ACT_365F = "ACT/365F"` | Actual days over a fixed 365. The usual choice for an option tenor, and the convention crypto derivatives actually quote. |
| `ACT_360` | `ACT_360 = "ACT/360"` | Actual days over 360. Money-market convention. |
| `ACT_ACT_ISDA` | `ACT_ACT_ISDA = "ACT/ACT ISDA"` | Actual days, split so that days in a leap year are divided by 366 and the rest by 365. |
| `D30_360` | `D30_360 = "30/360 Bond Basis"` | 30/360 Bond Basis: a 31st becomes a 30th, and the end date flattens only when the start already has. |
| `D30E_360` | `D30E_360 = "30E/360"` | 30E/360 Eurobond: both ends flatten unconditionally. |
| `ACT_252` | `ACT_252 = "ACT/252"` | Trading days over 252. The convention behind business-day time in equity volatility. Under Exchange.CRYPTO every calendar day is a trading day, so this degenerates to actual days over 252, a denominator no crypto desk uses. Crypto tenors are ACT_365F. |

### ExpiryKind

*enum*

A listed expiry cycle. The first four are the p.m.-settled US equity cycles and share a close-shaped clock; VIX is a.m.-settled off the following month's third Friday, which is why it alone keeps its own instant functions; see the section banner above.

| Member | Declared as | Meaning |
|---|---|---|
| `DAILY` | `DAILY = "Daily"` | Every trading day: SPX, NDX and XSP list an expiry each session, so this cycle is the trading calendar itself. |
| `WEEKLY` | `WEEKLY = "Weekly"` | The week's Friday, stepped back to the previous trading day when that Friday does not trade. |
| `MONTHLY` | `MONTHLY = "Monthly"` | The classic third-Friday monthly, stepped to the previous day when that Friday is a scheduled holiday. |
| `QUARTERLY` | `QUARTERLY = "Quarterly"` | The monthly of March, June, September and December, the triple-witching months. |
| `VIX` | `VIX = "VIX"` | The VIX final-settlement cycle: the Wednesday thirty days before the following month's third Friday, stepped to the previous business day on the two-branch holiday rule. |

### Known

*enum*

A three-valued answer, for questions a dated table or a bounded calendar cannot answer outside its window. This exists because Pine's bool cannot hold na: int, enum and object types can, bool cannot, so "return na, never false" is not expressible for a yes/no question. The enum is also the stronger contract: UNKNOWN will not type-check anywhere a bool is expected, so a caller cannot accidentally read "not known" as "no".

| Member | Declared as | Meaning |
|---|---|---|
| `YES` | `YES = "Yes"` | The date is in the table, or inside the calendar and shut. |
| `NO` | `NO = "No"` | The date is covered and is not one. |
| `UNKNOWN` | `UNKNOWN = "Unknown"` | The date lies outside the covered window. Not a no. |

### Overflow

*enum*

What to do when calendar arithmetic lands on a day that does not exist, e.g. 31 January plus one month. Named for TC39 Temporal's `overflow` option.

| Member | Declared as | Meaning |
|---|---|---|
| `CONSTRAIN` | `CONSTRAIN = "Constrain"` | Clamp to the last valid day of the month, so 31 January plus one month is 28 or 29 February. This is java.time's behaviour and the default. |
| `REJECT` | `REJECT = "Reject"` | Return na rather than invent a date. |

### Resolver

*enum*

How to resolve a local time that a daylight-saving transition made impossible or ambiguous. Named for Noda Time's ZoneLocalMappingResolver and Temporal's `disambiguation` option.

| Member | Declared as | Meaning |
|---|---|---|
| `EARLIER` | `EARLIER = "Earlier"` | Take the earlier of the two instants in an overlap; shift backward out of a gap. |
| `LATER` | `LATER = "Later"` | Take the later of the two instants in an overlap; shift forward out of a gap. |
| `COMPATIBLE` | `COMPATIBLE = "Compatible"` | Gaps shift forward by the gap length, overlaps take the earlier instant. Matches java.time and Temporal defaults. |
| `REJECT` | `REJECT = "Reject"` | Return na rather than resolve. |

### RoundMode

*enum*

How to round a date-time to a unit boundary. Modes follow TC39 Temporal, and are applied to the elapsed time since the Unix epoch, so TRUNC means toward the epoch.

| Member | Declared as | Meaning |
|---|---|---|
| `FLOOR` | `FLOOR = "Floor"` | Toward the earlier boundary. |
| `CEIL` | `CEIL = "Ceiling"` | Toward the later boundary. |
| `TRUNC` | `TRUNC = "Truncate"` | Toward the epoch: FLOOR after 1970, CEIL before it. |
| `HALF_EXPAND` | `HALF_EXPAND = "Half expand"` | Nearest boundary; exact ties go away from the epoch. |

### SessionId

*enum*

Standard trading sessions, ready to use. Times are the market conventions, not an exchange feed.

| Member | Declared as | Meaning |
|---|---|---|
| `US_PREMARKET` | `US_PREMARKET = "US pre-market"` | 04:00-09:30 New York, NYSE calendar. |
| `US_REGULAR` | `US_REGULAR = "US regular"` | 09:30-16:00 New York, NYSE calendar, half days respected. |
| `US_AFTERHOURS` | `US_AFTERHOURS = "US after-hours"` | 16:00-20:00 New York, NYSE calendar. |
| `US_EXTENDED` | `US_EXTENDED = "US extended"` | 04:00-20:00 New York, the whole extended day. |
| `FX_SYDNEY` | `FX_SYDNEY = "FX Sydney"` | 21:00-06:00 UTC, opens Sunday evening. |
| `FX_TOKYO` | `FX_TOKYO = "FX Tokyo"` | 00:00-09:00 UTC. |
| `FX_LONDON` | `FX_LONDON = "FX London"` | 08:00-17:00 UTC. |
| `FX_NEWYORK` | `FX_NEWYORK = "FX New York"` | 13:00-22:00 UTC. |
| `FX_LONDON_NY` | `FX_LONDON_NY = "FX London/New York overlap"` | 13:00-17:00 UTC, the overlap where liquidity peaks. |
| `KZ_ASIAN` | `KZ_ASIAN = "Asian range"` | 20:00-00:00 New York, the Asian range. |
| `KZ_LONDON` | `KZ_LONDON = "London killzone"` | 02:00-05:00 New York. |
| `KZ_NEWYORK` | `KZ_NEWYORK = "New York killzone"` | 07:00-10:00 New York. |
| `KZ_LONDON_CLOSE` | `KZ_LONDON_CLOSE = "London close"` | 10:00-12:00 New York. |
| `CME_RTH` | `CME_RTH = "CME regular"` | 08:30-15:15 Chicago, CME calendar, half days respected. |
| `CME_ETH` | `CME_ETH = "CME Globex"` | 17:00-16:00 Chicago, the Globex day, CME calendar, half days respected. |
| `LSE_REGULAR` | `LSE_REGULAR = "LSE regular"` | 08:00-16:30 London, LSE calendar, half days respected. |
| `XETRA_REGULAR` | `XETRA_REGULAR = "Xetra regular"` | 09:00-17:30 Frankfurt, the German cash market. Named for Xetra rather than Eurex because these are the cash hours; Eurex derivatives are EUREX_REGULAR below. German cash-market holidays are not modelled, and this preset carries no calendar at all rather than borrowing the derivatives one: Xetra closes on days Eurex trades. |
| `HKEX_REGULAR` | `TSE_REGULAR = "TSE regular"` | 09:30-16:00 Hong Kong with lunch 12:00-13:00, the schedule from 7 March 2011, HKEX calendar, half days honoured. Before that date the open was 10:00; a preset is one set of hours, so the older era opens half an hour early. On a half day the close comes in to 12:00 and the lunch break disappears with it, which is what the exchange actually does. |
| `ASX_REGULAR` | `EUREX_REGULAR = "Eurex regular"` | 10:00-16:00 Sydney, ASX calendar, half days honoured. The half day ends at 14:10 and falls on the last session before Christmas and the last of the year, so it moves off 24 and 31 December when those land on a weekend. |
| `TSX_REGULAR` | `HKEX_REGULAR = "HKEX regular"` | 09:30-16:00 Toronto, TSX calendar, half days honoured. Christmas Eve only, at 13:00, and only when 24 December is itself a session. |
| `SSE_REGULAR` | `ASX_REGULAR = "ASX regular"` | 09:30-15:00 Shanghai with lunch 11:30-13:00, SSE calendar. The longest lunch break of any market here, and the only preset besides HKEX and TSE to carry one. |
| `BSE_REGULAR` | `TSX_REGULAR = "TSX regular"` | 09:15-15:30 Mumbai, BSE calendar, no lunch break. The Diwali Muhurat evening session is not modelled. |
| `SGX_REGULAR` | `SSE_REGULAR = "SSE regular"` | 09:00-17:00 Singapore, SGX calendar, no lunch break: the reference calendar models none in this era, and the pre-2011 one it dropped is not reconstructed here. |
| `TSE_REGULAR` | `BSE_REGULAR = "BSE regular"` | 09:00-15:30 Tokyo with lunch 11:30-12:30, the schedule from 5 November 2024, JPX calendar. Before that date the close was 15:00; a preset is one set of hours, so the older era is wrong by 30 minutes. The lunch break has held at these times for as long as the exchange calendars record. |
| `EUREX_REGULAR` | `SGX_REGULAR = "SGX regular"` | 08:00-22:00 Berlin, EUREX calendar: the real derivatives session, TARGET2-shaped holidays, no half days. |
| `CRYPTO_DAY` | `CRYPTO_DAY = "Crypto day"` | 00:00-24:00 UTC, all seven days, CRYPTO calendar: the UTC day boundary crypto convention settles on. Always open, which makes is_first_bar and is_last_bar the daily-boundary markers. |

### TimeUnit

*enum*

A unit of time, used by the truncation and rounding helpers.

| Member | Declared as | Meaning |
|---|---|---|
| `MS` | `MS = "Millisecond"` | Millisecond. |
| `SECOND` | `SECOND = "Second"` | Second. |
| `MINUTE` | `MINUTE = "Minute"` | Minute. |
| `HOUR` | `HOUR = "Hour"` | Hour. |
| `DAY` | `DAY = "Day"` | Calendar day. |
| `WEEK` | `WEEK = "Week"` | Calendar week, starting on a configurable day. |
| `MONTH` | `MONTH = "Month"` | Calendar month. |
| `QUARTER` | `QUARTER = "Quarter"` | Calendar quarter, three months starting in January. |
| `YEAR` | `YEAR = "Year"` | Calendar year. |

---

[API Index](API-Index) &nbsp;·&nbsp; [Task Index](Task-Index) &nbsp;·&nbsp; [Glossary](Glossary)
