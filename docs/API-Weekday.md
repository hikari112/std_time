# Weekday

> Concepts first: read **[Core Concepts](Core-Concepts)** before this page.

`Weekday` is an enum rather than a bare int because 0=Sunday versus 1=Monday confusion is the most common class of date bug. Three numbering schemes meet here and none of them agree: this library counts Sunday as 0, ISO-8601 counts Monday as 1, and Pine's own `dayofweek` counts Sunday as 1. `to_int`, `to_iso_dow` and `to_pine_dow` are the three ways out.

## Members

| | Summary |
|---|---|
| [`abbr`](#abbr) | The three-letter English abbreviation of a weekday. |
| [`days_until`](#days_until) | Forward distance in days from this weekday to another, never negative. |
| [`minus`](#minus) | The weekday n days earlier in the weekly cycle, wrapping. |
| [`name`](#name) | The English name of a weekday. |
| [`plus`](#plus) | The weekday n days later in the weekly cycle, wrapping. |
| [`to_int`](#to_int) | Numeric code for a weekday, 0 = Sunday through 6 = Saturday. |
| [`to_iso_dow`](#to_iso_dow) | ISO-8601 numbering for this weekday, 1 = Monday through 7 = Sunday. |
| [`to_pine_dow`](#to_pine_dow) | This weekday in Pine's own numbering, where Sunday is 1, the scale used by the dayofweek.* constants and returned by the dayofweek built-in. |

## Reference

### abbr

```pine
Weekday.abbr()
```

The three-letter English abbreviation of a weekday.

**Returns** &nbsp; The abbreviation, e.g. "Fri".

### days_until

```pine
Weekday.days_until(Weekday other)
```

Forward distance in days from this weekday to another, never negative. A method so the direction reads off the call: `friday.days_until(monday)`.

| Parameter | Meaning |
|---|---|
| `other` | The target weekday. |

**Returns** &nbsp; Days to advance from this to reach other, in [0, 6]. Zero when they are the same day: a week later is not what "until" means here.

### minus

```pine
Weekday.minus(int n)
```

The weekday n days earlier in the weekly cycle, wrapping.

| Parameter | Meaning |
|---|---|
| `n` | Days to go back; may be negative. |

**Returns** &nbsp; The resulting Weekday.

### name

```pine
Weekday.name()
```

The English name of a weekday.

**Returns** &nbsp; The full name, e.g. "Friday".

### plus

```pine
Weekday.plus(int n)
```

The weekday n days later in the weekly cycle, wrapping.

| Parameter | Meaning |
|---|---|
| `n` | Days to advance; may be negative. |

**Returns** &nbsp; The resulting Weekday.

### to_int

```pine
Weekday.to_int()
```

Numeric code for a weekday, 0 = Sunday through 6 = Saturday.

**Returns** &nbsp; Integer code in [0, 6].

### to_iso_dow

```pine
Weekday.to_iso_dow()
```

ISO-8601 numbering for this weekday, 1 = Monday through 7 = Sunday. One of three numbering schemes carried by this type: to_int() is 0-based Sunday-first, to_pine_dow() is Pine's 1-based Sunday-first, and this is ISO's 1-based Monday-first. All three live on the enum so a signature never has to say which scheme a bare int is in.

**Returns** &nbsp; ISO weekday in [1, 7].

### to_pine_dow

```pine
Weekday.to_pine_dow()
```

This weekday in Pine's own numbering, where Sunday is 1, the scale used by the dayofweek.* constants and returned by the dayofweek built-in. Distinct from to_int(), which is 0-based.

**Returns** &nbsp; An integer in [1, 7] comparable with dayofweek.monday and friends.

## Enums

| | Summary |
|---|---|
| [`Weekday`](#weekday) | Day of the week. |

### Weekday

*enum*

Day of the week. An enum rather than a bare int because 0=Sunday versus 1=Monday confusion is the most common class of date bug. Use `.to_int()` when the numeric code is needed.

| Member | Declared as | Meaning |
|---|---|---|
| `SUNDAY` | `SUNDAY = "Sunday"` | Sunday, numeric code 0. |
| `MONDAY` | `MONDAY = "Monday"` | Monday, numeric code 1. |
| `TUESDAY` | `TUESDAY = "Tuesday"` | Tuesday, numeric code 2. |
| `WEDNESDAY` | `WEDNESDAY = "Wednesday"` | Wednesday, numeric code 3. |
| `THURSDAY` | `THURSDAY = "Thursday"` | Thursday, numeric code 4. |
| `FRIDAY` | `FRIDAY = "Friday"` | Friday, numeric code 5. |
| `SATURDAY` | `SATURDAY = "Saturday"` | Saturday, numeric code 6. |

---

[API Index](API-Index) &nbsp;·&nbsp; [Task Index](Task-Index) &nbsp;·&nbsp; [Glossary](Glossary)
