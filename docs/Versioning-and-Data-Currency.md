# Versioning and Data Currency

A calendar library has a shelf life that a maths library does not. Three of the
twelve calendars stop answering at the end of 2026 unless their tables are
extended. This page says when that matters and what the version numbers mean.

## Library versions

TradingView versions a published library by an integer in the import path:

```pine
import The_Peaceful_Lizard/std_time/1 as t
```

An import pins that version. A new publication does **not** change the behaviour
of scripts already importing an older one, so nothing breaks under you. Moving
up is a deliberate edit to the import line.

## What counts as a breaking change

Treated as breaking, and therefore a new version with a note:

- Removing or renaming an export.
- Changing a parameter's type, order or meaning.
- Changing what a function returns for inputs it already answered.
- Moving a calendar's horizon **backward**.

Not treated as breaking:

- Adding an export, an enum member or a calendar.
- Extending a dated table forward, which turns `Known.UNKNOWN` answers into
  `YES` or `NO` without changing any answer that was already given.
- Correcting a documented divergence, since the old answer was stated as wrong.

## Data currency

Ask the library rather than trusting this page, because the library is what your
script actually runs:

```pine
t.Exchange.SSE.calendar_through()   // 2026
t.fomc_known_through()              // 2027
t.Zone.SYDNEY.rules_from()          // 2008
```

| Data | Currency | Refresh needed |
|---|---|---|
| SSE, BSE, SGX holidays | Through 2026 | Yearly, as exchanges publish |
| HKEX lunar festivals | Through 2049 | Once, well ahead |
| JPX equinox approximation | Through 2099 | Not in any working lifetime |
| FOMC meetings | 2021 to 2027 | Yearly, as the committee publishes |
| Rule-driven calendars | No horizon | Only when a statute changes |
| Zone rules | Per `rules_from()` | Only when legislation changes |
| Unscheduled closures | Past only | After each event |

The three tabled calendars are tabled because their holidays are lunar,
lunisolar or Islamic, or are re-announced annually. Shanghai's State Council
holiday blocks have changed length three times in twenty years, so nothing
extrapolates them.

## Writing code that ages well

Gate on the horizon rather than assuming it:

```pine
int through = t.Exchange.SSE.calendar_through()
bool covered = na(through) or d.Year <= through
```

`na` means rule-driven with no horizon, which is why the check is written that
way round. A bare `d.Year <= through` is `na` outside a table and reads as
false, so an NYSE query would look uncovered when it is the opposite.

For anything user-facing, prefer `closed_for_holiday()` over `is_holiday()`, so
a date past the table produces `Known.UNKNOWN` instead of a confident wrong
answer.

## Reporting a calendar error

A date that disagrees with an exchange's published record is a bug, and a useful
report names the calendar, the date, what the library said and what the exchange
published. Three of the divergences in
[Scope and Limitations](Scope-and-Limitations) are already known and deliberate,
so it is worth checking that page first.

---

Previous: [Performance and Limits](Performance-and-Limits)
&nbsp;·&nbsp; Next: [Design Notes](Design-Notes)
&nbsp;·&nbsp; See also: [Verification](Verification)
