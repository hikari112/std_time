# Exchange

> Concepts first: read **[Exchange Calendars](Exchange-Calendars)** before this page.

An `Exchange` is a market calendar: holidays, observance shifts, early closes and lunch breaks. These are not variations of one calendar. Most questions about a calendar are methods on `DateTime`, not on `Exchange`: `d.is_trading_day(ex)`, not `ex.is_trading_day(d)`.

## Members

| | Summary |
|---|---|
| [`calendar_from`](#calendar_from) | The first year an exchange's calendar answers exactly. |
| [`calendar_through`](#calendar_through) | The last year an exchange's calendar answers exactly, or na when its rules extrapolate without a horizon. |
| [`zone`](#zone) | The zone an exchange's local session times are quoted in. |

## Reference

### calendar_from

```pine
Exchange.calendar_from()
```

The first year an exchange's calendar answers exactly. Before it the rules still run, but nothing has checked them and the tabled layers are empty, so a holiday there is the rules extrapolated backwards rather than the exchange's own record.

**Returns** &nbsp; Calendar year, or na for a calendar with no lower bound to state.

**Raises** &nbsp; on an Exchange the switch does not handle, a library bug.

### calendar_through

```pine
Exchange.calendar_through()
```

The last year an exchange's calendar answers exactly, or na when its rules extrapolate without a horizon. A calendar built from rules keeps generating dates forever and only its unscheduled closures are unpredictable; one built from a table stops when the table does, and past that it would report every tabled holiday as an ordinary trading day. That is the difference this reports.

**Returns** &nbsp; Calendar year of the last covered date, or na when no horizon applies.

**Raises** &nbsp; on an Exchange the switch does not handle, a library bug. Comparing a year against na yields na, which is false, so `if Year > ex.calendar_through()` reads correctly as "never past it" for the unbounded calendars.

### zone

```pine
Exchange.zone()
```

The zone an exchange's local session times are quoted in.

**Returns** &nbsp; The Zone.

**Raises** &nbsp; on an Exchange the switch does not handle, a library bug, and a loud one by design: every session boundary in this file resolves through here, so an unhandled member falling through to New York would move them all at once.

## Enums

| | Summary |
|---|---|
| [`Exchange`](#exchange) | An exchange calendar. |

### Exchange

*enum*

An exchange calendar. These are not variations of one calendar: CME closes on three days a year and trades the other US federal holidays on a shortened session, while the LSE runs on UK bank holidays that share only Good Friday and Christmas with the NYSE.

| Member | Declared as | Meaning |
|---|---|---|
| `NYSE` | `NYSE = "NYSE"` | New York Stock Exchange, 09:30-16:00 New York, early close 13:00. |
| `LSE` | `LSE = "LSE"` | London Stock Exchange, 08:00-16:30 London, early close 12:30. |
| `CME` | `CME = "CME"` | CME Globex equity index, 17:00 the previous day to 16:00 Chicago, early close 12:00. |
| `JPX` | `JPX = "JPX"` | Tokyo Stock Exchange, 09:00-15:30 Tokyo (15:00 through 2024), lunch 11:30-12:30, closed 31 December through 3 January, no half days. |
| `EUREX` | `EUREX = "EUREX"` | Eurex derivatives, 08:00-22:00 Berlin, TARGET2-shaped holidays, no early closes. The German cash market (Xetra) keeps different hours and more holidays; this is the derivatives calendar. |
| `HKEX` | `HKEX = "HKEX"` | Hong Kong Exchanges, 09:30-16:00 Hong Kong (10:00 through 2010), lunch 12:00-13:00, half days at 12:00 on Christmas Eve, New Year's Eve and Lunar New Year's Eve. The lunar holidays are tabled rather than computed, so this calendar answers exactly from 2000 to 2049 and no further; see calendar_through. |
| `ASX` | `ASX = "ASX"` | Australian Securities Exchange, 10:00-16:00 Sydney, half days at 14:10 on the last sessions before Christmas and New Year. New South Wales holidays: no Labour Day, and ANZAC Day does not move off a weekend. |
| `TSX` | `TSX = "TSX"` | Toronto Stock Exchange, 09:30-16:00 Toronto, half day at 13:00 on Christmas Eve only. No Easter Monday, and Family Day exists only from 2008. |
| `SSE` | `SSE = "SSE"` | Shanghai Stock Exchange, 09:30-15:00 Shanghai, lunch 11:30-13:00, no early closes. Wholly tabled and exact only through 2026; see calendar_through. |
| `BSE` | `BSE = "BSE"` | Bombay Stock Exchange, 09:15-15:30 Mumbai, no lunch break, no early closes. Six fixed dates with no substitution at all, and the rest tabled through 2026. The Muhurat evening session on Diwali is not modelled. |
| `SGX` | `SGX = "SGX"` | Singapore Exchange, 09:00-17:00 Singapore, no lunch break in the modelled era, no early closes. Four fixed dates with a Sunday-only substitute, and the rest tabled through 2026. |
| `CRYPTO` | `CRYPTO = "Crypto"` | Cryptocurrency, 24/7: every calendar day trades 00:00-24:00 UTC, no holidays, no weekends, no early closes. |

---

[API Index](API-Index) &nbsp;·&nbsp; [Task Index](Task-Index) &nbsp;·&nbsp; [Glossary](Glossary)
