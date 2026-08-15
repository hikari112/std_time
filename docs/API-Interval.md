# Interval

> Concepts first: read **[Core Concepts](Core-Concepts)** before this page.

An `Interval` is a half-open span of instants, `[FromMS, ToMS)`. Half-open so that consecutive intervals tile a timeline without overlapping at the join.

## The type

### Interval

*type*

A half-open span of instants, [FromMS, ToMS).

| Field | Declared as | Meaning |
|---|---|---|
| `FromMS` | `int FromMS = 0` | Inclusive start, Unix milliseconds. |
| `ToMS` | `int ToMS = 0` | Exclusive end, Unix milliseconds. |

## Members

| | Summary |
|---|---|
| [`abuts`](#abuts) | Whether two intervals meet exactly end to start without overlapping: the condition under which they can be joined into one without a hole or a double count. |
| [`contains`](#contains) | Whether an instant falls inside this interval. |
| [`duration`](#duration) | The length of this interval in milliseconds. |
| [`encloses`](#encloses) | Whether this interval wholly contains another. |
| [`equals`](#equals) | Whether two intervals have identical endpoints. |
| [`gap`](#gap) | The empty span between two intervals that neither overlap nor touch. |
| [`intersection`](#intersection) | The overlapping part of two intervals. |
| [`is_empty`](#is_empty) | Whether this interval contains no instants at all. |
| [`overlaps`](#overlaps) | Whether two intervals share any instant. |
| [`to_iso`](#to_iso) | This interval in ISO-8601 interval form, "start/end", with both endpoints in UTC. |

## Reference

### abuts

```pine
Interval.abuts(Interval other)
```

Whether two intervals meet exactly end to start without overlapping: the condition under which they can be joined into one without a hole or a double count.

| Parameter | Meaning |
|---|---|
| `other` | The second Interval. |

**Returns** &nbsp; true when one ends precisely where the other begins.

### contains

```pine
Interval.contains(int unix_ms)
```

Whether an instant falls inside this interval. The interval is half-open, [FromMS, ToMS), so back-to-back intervals never both claim the same instant.

| Parameter | Meaning |
|---|---|
| `unix_ms` | Unix timestamp in milliseconds. |

**Returns** &nbsp; true when FromMS <= unix_ms < ToMS.

### duration

```pine
Interval.duration()
```

The length of this interval in milliseconds.

**Returns** &nbsp; Milliseconds spanned; zero when empty.

### encloses

```pine
Interval.encloses(Interval other)
```

Whether this interval wholly contains another.

| Parameter | Meaning |
|---|---|
| `other` | The inner Interval. |

**Returns** &nbsp; true when other lies entirely within this.

### equals

```pine
Interval.equals(Interval other)
```

Whether two intervals have identical endpoints.

| Parameter | Meaning |
|---|---|
| `other` | The second Interval. |

**Returns** &nbsp; true when both endpoints match.

### gap

```pine
Interval.gap(Interval other)
```

The empty span between two intervals that neither overlap nor touch.

| Parameter | Meaning |
|---|---|
| `other` | The second Interval. |

**Returns** &nbsp; The gap Interval, or na when they overlap or abut.

### intersection

```pine
Interval.intersection(Interval other)
```

The overlapping part of two intervals.

| Parameter | Meaning |
|---|---|
| `other` | The second Interval. |

**Returns** &nbsp; The shared Interval, or na when they do not overlap.

### is_empty

```pine
Interval.is_empty()
```

Whether this interval contains no instants at all.

**Returns** &nbsp; true when the end is not after the start.

### overlaps

```pine
Interval.overlaps(Interval other)
```

Whether two intervals share any instant. Half-open, so intervals that merely touch do not overlap.

| Parameter | Meaning |
|---|---|
| `other` | The second Interval. |

**Returns** &nbsp; true when they intersect.

### to_iso

```pine
Interval.to_iso()
```

This interval in ISO-8601 interval form, "start/end", with both endpoints in UTC.

**Returns** &nbsp; A string such as "2026-08-21T13:30:00Z/2026-08-21T20:00:00Z".

---

[API Index](API-Index) &nbsp;·&nbsp; [Task Index](Task-Index) &nbsp;·&nbsp; [Glossary](Glossary)
