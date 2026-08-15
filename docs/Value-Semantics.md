# Value Semantics

Read this before assigning to a field.

Pine's user-defined types are reference types. Everything on this page follows
from that one fact, and it is the only way this library can end up holding a
date its own constructor would have refused.

## 1. Assignment aliases, it does not copy

```pine
t.DateTime a = t.new_datetime(2025, 6, 15)
t.DateTime b = a
b.Month := 3        // a.Month is now 3 as well
```

This applies to every type here without exception: `DateTime`, `Period`,
`Interval`, `Session` and `DstRule`.

Two ways out:

- **`.copy()`**, Pine's built-in shallow copy, when you want an independent
  record.
- **The withers**, which copy for you and validate on the way through.

```pine
t.DateTime b = a.with_month(3)     // a is untouched
```

Prefer the wither. It is shorter, and unlike a raw field assignment it cannot
produce a record the constructor would have rejected.

## 2. Which fields carry a promise

Most fields accept every value their type can hold, and setting one on an
instance you own is safe. These are the exceptions, because other functions read
them as a promise:

**`DateTime`: `Year`, `Month`, `Day`, `Hour`, `Minute`, `Second`, `MS`.**
Together they have to name a real moment. Set `Month` to 2 on a 31st and the
record holds 31 February, a date `new_datetime` would have refused, and every
adjuster downstream inherits it.

```pine
t.DateTime d = t.new_datetime(2025, 1, 31)
d.Month := 2                 // d is now 31 February
t.DateTime fixed = d.normalized()   // 2025-02-28
```

`normalized()` repairs a day past the end of its month. It returns `na` if
something other than the day is out of range, because a `Month` of 13 is a typo
rather than an overflow.

**`Session`: `StartMin`, `EndMin`, `DayMask`, and the break pair.** Minutes must
be within a day, the mask must be 7 bits, and the break must be set as a pair
and ordered strictly inside the window. `new_session` enforces all of it. A
negative mask makes the weekday test meaningless rather than merely empty, and a
hand-set break can put a hole where the market actually trades.

**`Interval`: `FromMS` must not exceed `ToMS`.** `new_interval` orders them for
you.

Everything else is safe to set directly: `DateTime.UTC`, `Session.Name`, `Tz`
and `Cal`, and `Period` and `DstRule` in full. `Session.EarlyClose` is the odd
one, meaningful only alongside a `Cal` to read closes from, which is why
`new_session` refuses the flag on its own.

There is no derived weekday field to keep in sync. `weekday()` computes from the
calendar on every call and cannot go stale.

## 3. Building one without positional arguments

Pine's `.new()` takes named arguments and every field here has a default, so a
partly specified record needs no wrapper function and no long positional call:

```pine
t.Period.new(Months = 3)                      // three months, no years, no days
t.DstRule.new(StartMonth = 4, EndMonth = 9)
t.Interval.new(ToMS = ms)
```

`DateTime` is the exception. Prefer `new_datetime`, which validates the field
set as a whole, or `try_new_datetime` when the input is untrusted and you want
`na` instead of a raise.

## 4. `==` does not compile on two UDTs

In Pine this is a type error, not reference equality. Use the explicit methods:

- `equals()` compares field by field. Available on `DateTime`, `Period` and
  `Interval`.
- `same_instant()` compares two `DateTime`s by the moment they denote, so
  `12:00+00:00` and `07:00-05:00` are the same instant and are not equal
  records.
- `compare()`, `is_before()`, `is_after()` for ordering.

---

Previous: [Civil and Exact Arithmetic](Civil-and-Exact-Arithmetic)
&nbsp;·&nbsp; Next: [Error Model](Error-Model)
&nbsp;·&nbsp; Reference: [API-DateTime](API-DateTime)
