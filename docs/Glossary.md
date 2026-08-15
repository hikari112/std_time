# Glossary

Terms used precisely throughout the wiki. Where a word has a loose everyday
meaning and a narrow one here, the narrow one is what the pages mean.

**Adjuster.** A function that moves a date to a related date by a rule rather
than by a count: `next_weekday`, `nth_weekday_of_month`, `date_from_iso_week`.
Named for java.time's `TemporalAdjusters`.

**Ambiguous time.** A local time that happened twice, because a fall-back
transition repeated it. Ask `Zone.is_ambiguous`. See also *overlap*.

**Business day.** A day the market is open, used specifically in the ISDA sense
of rolling a date that lands on a closed day. Governed by `BusinessDay`. Not
interchangeable with *weekday*.

**Civil time.** What a clock on a wall reads: year, month, day, hour, minute. It
says nothing on its own about which instant it refers to until you supply an
offset or a zone. Contrast *instant*.

**Constrain.** The `Overflow` mode that clamps a date past the end of a month to
the last valid day, so 31 January plus one month is 28 or 29 February. The
default, and java.time's behaviour.

**Day count.** The convention that decides the denominator of a rate or the tau
of an option price: `ACT/365F`, `ACT/360`, `ACT/ACT ISDA`, `30/360`, `30E/360`,
`ACT/252`. Per the ISDA 2006 Definitions.

**Early close.** A scheduled short session, not a closure. The market trades.
`is_early_close` returns `false` on a day the market is shut, because a closed
market is not an early close.

**Envelope.** A session's whole window including any break inside it. `bounds()`
returns the envelope; `break_bounds()` returns the hole.

**Exact time.** Arithmetic on instants, measured in milliseconds. Contrast
*civil time*. The `plus_ms` family, not the `plus_days` family.

**Gap.** A local time that never happened, because a spring-forward transition
skipped it. Ask `Zone.is_gap`.

**Half-open.** A span that includes its start and excludes its end,
`[from, to)`. Every `Interval` here is half-open, so consecutive intervals tile
a timeline without overlapping at the join.

**Horizon.** The last year a calendar answers exactly, from
`calendar_through()`. `na` means rule-driven with no horizon. Past a horizon
`closed_for_holiday()` answers `Known.UNKNOWN`.

**In-band.** A return value that is a real value of the result range rather than
a flag. The reason `time_to_close` does not return 0 while a session runs: 0 is
a real distance.

**Instant.** A moment on the timeline, as Unix milliseconds. Unambiguous
worldwide. Contrast *civil time*.

**ISO week-based year.** The year an ISO week belongs to, which disagrees with
the calendar year for a few days each January. Pattern letter `Y`, as against
`y` for the calendar year.

**Observance shift.** A holiday moved off a weekend to a neighbouring weekday.
Different exchanges shift differently, and some do not shift at all.

**Offset.** A fixed distance from UTC, in hours, carried by a `DateTime` as a
`float`. Inert: it does not change with the seasons. Contrast *zone*.

**Overlap.** The hour that happens twice at a fall-back transition. Resolved by
a `Resolver`.

**Period.** A calendar-flavoured amount of time: years, months, days. Not
convertible to milliseconds without a reference date. java.time's `Period`.

**Proleptic Gregorian.** The Gregorian calendar projected backward past its 1582
introduction. Arithmetic, not history: those dates never happened as written,
and year 0 exists.

**Resolver.** The strategy for turning an impossible or ambiguous local time
into an instant: `COMPATIBLE`, `EARLIER`, `LATER`, `REJECT`. Named for Noda
Time's `ZoneLocalMappingResolver`.

**Session.** A recurring local-time window on selected weekdays, resolved
against a calendar. Not a pair of timestamps.

**SOQ.** Special Opening Quotation. The value Cboe's opening auction in the
constituent SPX series prints, which is what VIX settles against, and the reason
VIX settlement is a morning instant rather than a close.

**Trading day.** A day the exchange's calendar says it is open. Weekends and
holidays excluded. Not the same as a *weekday*.

**Triple witching.** The quarterly expiry in March, June, September and
December, when several contract classes expire together.

**Unscheduled closure.** A market closure no rule predicts: a hurricane, a
blackout, a state funeral. Recorded in a dated table, and therefore complete
only for the past.

**Wither.** A method returning a copy with one field changed: `with_year`,
`with_month`, `with_time`. Named after the `withX` convention in java.time. They
copy and validate, which is why they are safer than assigning to a field.

**Zone.** A standard offset plus a daylight-saving rule, so it changes with the
seasons. Always a `Zone` value here, never a `float`. Contrast *offset*.

---

Up: [Home](Home) &nbsp;·&nbsp; [API Index](API-Index)
