# Installation

## The import line

```pine
//@version=6
indicator("My indicator")
import The_Peaceful_Lizard/std_time/1 as t
```

The alias is yours to choose. Every example in this wiki uses `t`, and short is
worth something here because you will type it constantly.

## Requirements

**Pine v6 only.** The library uses enums, user-defined types and methods, none
of which exist before v6.

**Works from any script kind.** An `indicator`, a `strategy` or another
`library` can all import it.

## Every imported name takes the alias

This catches everyone once, and the error message does not mention imports:

```pine
t.DateTime d = t.new_datetime(2025, 6, 15)   // correct
DateTime   d = t.new_datetime(2025, 6, 15)   // "{typeKeyword}" is not a valid type keyword
```

Types, enums and enum members all take it: `t.DateTime`, `t.Session`,
`t.Exchange.NYSE`, `t.Overflow.REJECT`, `t.Weekday.FRIDAY`.

The signatures on the reference pages are shown as the **library** declares
them, where `DateTime` is unqualified and correct. Copying a signature into your
own script is the usual way to hit this.

## Compiled size

**An import does not spend your script's token budget.** TradingView compiles a
library as its own unit, and importing one does not copy its code into the
importing script, so `std_time`'s own weight is not subtracted from yours.

The library's own weight is about **92,000** compiled tokens, measured against
the 100,256 cap when the library itself was published. That is a fact about this
library's publication, not a tax on yours.

Two things that do apply to your script:

- The **server-side syntax check does not enforce the token cap.** A script can
  check clean and still fail to add to the chart.
- String data costs **two compiled tokens per character**, so your own constant
  tables are the first place to look if you run out.

[Performance and Limits](Performance-and-Limits) has the detail.

## Check it works

```pine
//@version=6
indicator("std_time smoke test")
import The_Peaceful_Lizard/std_time/1 as t

t.DateTime d = t.unix_to_date_zone(time, t.Zone.NEW_YORK)
plot(d.is_trading_day(t.Exchange.NYSE) ? 1 : 0)
```

On a US equity chart that plots 1 on trading days and 0 on holidays. If it
compiles and plots, the import resolved and the calendar is answering.

## Where to go next

- New to the model: [Core Concepts](Core-Concepts), then the numbered run in
  the sidebar.
- Coming from Pine's built-ins:
  [Migrating from Pine Built-ins](Migrating-from-Pine-Built-ins).
- Looking for a specific function: [API Index](API-Index).

---

Previous: [Home](Home) &nbsp;·&nbsp; Next: [Quick Start](Quick-Start)
