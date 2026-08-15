# Period

> Concepts first: read **[Civil and Exact Arithmetic](Civil-and-Exact-Arithmetic)** before this page.

A `Period` is a calendar-flavoured amount of time in the sense of java.time's `Period`: years, months and days. It is not convertible to milliseconds without a reference date, because months and years have no fixed length.

## The type

### Period

*type*

A calendar-flavoured amount of time, in the sense of java.time's Period. It is not convertible to milliseconds without a reference date, because months and years have no fixed length.

| Field | Declared as | Meaning |
|---|---|---|
| `Years` | `int Years = 0` | Whole years. |
| `Months` | `int Months = 0` | Whole months. |
| `Days` | `int Days = 0` | Whole days. |

## Members

| | Summary |
|---|---|
| [`equals`](#equals) | Whether two periods have identical fields. |
| [`is_negative`](#is_negative) | Whether any field of this period is negative. |
| [`is_zero`](#is_zero) | Whether every field of this period is zero. |
| [`minus`](#minus) | The difference of two periods, field by field. |
| [`multiplied_by`](#multiplied_by) | This period with every field scaled. |
| [`negated`](#negated) | This period with every field's sign flipped. |
| [`normalized`](#normalized) | This period with surplus months folded into years, as java.time's Period.normalized: 1 year 15 months becomes 2 years 3 months. |
| [`plus`](#plus) | The sum of two periods, field by field. |
| [`to_iso`](#to_iso) | This period in ISO-8601 form, e.g. "P1Y2M3D". |
| [`to_total_months`](#to_total_months) | The years and months of this period expressed as a month count. |

## Reference

### equals

```pine
Period.equals(Period other)
```

Whether two periods have identical fields. 12 months and 1 year are not equal under this test; normalise both first if that is what you meant.

| Parameter | Meaning |
|---|---|
| `other` | The second Period. |

**Returns** &nbsp; true when the fields match.

### is_negative

```pine
Period.is_negative()
```

Whether any field of this period is negative. A period can be mixed, e.g. 1 year minus 5 days, so this asks whether any component points backward.

**Returns** &nbsp; true when some field is negative.

### is_zero

```pine
Period.is_zero()
```

Whether every field of this period is zero.

**Returns** &nbsp; true for a zero period.

### minus

```pine
Period.minus(Period other)
```

The difference of two periods, field by field.

| Parameter | Meaning |
|---|---|
| `other` | The Period to subtract. |

**Returns** &nbsp; A new Period.

### multiplied_by

```pine
Period.multiplied_by(int n)
```

This period with every field scaled.

| Parameter | Meaning |
|---|---|
| `n` | The multiplier. |

**Returns** &nbsp; A new Period.

### negated

```pine
Period.negated()
```

This period with every field's sign flipped.

**Returns** &nbsp; A new Period.

### normalized

```pine
Period.normalized()
```

This period with surplus months folded into years, as java.time's Period.normalized: 1 year 15 months becomes 2 years 3 months. Days are left alone, because a day is not a fraction of a month.

**Returns** &nbsp; A new Period.

### plus

```pine
Period.plus(Period other)
```

The sum of two periods, field by field. Not normalised, because 1 month plus 30 days is not a fixed quantity; call normalized() if you want months folded into years.

| Parameter | Meaning |
|---|---|
| `other` | The second Period. |

**Returns** &nbsp; A new Period.

### to_iso

```pine
Period.to_iso()
```

This period in ISO-8601 form, e.g. "P1Y2M3D". A zero period is "P0D", as in java.time.

**Returns** &nbsp; The ISO-8601 period string.

### to_total_months

```pine
Period.to_total_months()
```

The years and months of this period expressed as a month count. Days are excluded, since they do not convert.

**Returns** &nbsp; Total whole months.

---

[API Index](API-Index) &nbsp;·&nbsp; [Task Index](Task-Index) &nbsp;·&nbsp; [Glossary](Glossary)
