"""Generate the std_time API reference pages from the library source.

The library documents itself completely: every export carries an @function,
@enum or @type block, every parameter an @param, every function a @returns,
every enum and type field a @field. This script reformats those blocks into
Markdown. It does not rewrite them; the prose on the generated pages is the
prose in the source, so the reference cannot drift from the code.

Pages group by receiver type rather than by the source file's section banners,
because a reader holds a DateTime and asks what it can do; nobody holds "the
ordinal/fields section".

Run from the repo root:  python tools/build_reference.py
Exits non-zero if the source stops documenting itself completely.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "std_time.pine"
DOCS = ROOT / "docs"

EXPECTED_EXPORTS = 240

# Receiver -> (page, human name). Types fold onto their receiver's page.
PAGES = {
    "DateTime": ("API-DateTime", "DateTime"),
    "Session": ("API-Session", "Session"),
    "Zone": ("API-Zone", "Zone"),
    "Exchange": ("API-Exchange", "Exchange"),
    "Period": ("API-Period", "Period"),
    "Interval": ("API-Interval", "Interval"),
    "Weekday": ("API-Weekday", "Weekday"),
}
FUNCTIONS_PAGE = "API-Functions"
ENUMS_PAGE = "API-Enums"

# Which page each exported type's field table belongs on.
TYPE_HOME = {
    "DateTime": "API-DateTime",
    "Session": "API-Session",
    "Interval": "API-Interval",
    "Period": "API-Period",
    "DstRule": "API-Zone",
}

# An enum that is also a receiver lives with its own methods rather than in the
# enum pile: Exchange's three accessors alone would be a stub page, and a reader
# looking up Zone.rules_from wants the zone list on the same screen.
ENUM_HOME = {
    "Zone": "API-Zone",
    "Exchange": "API-Exchange",
    "Weekday": "API-Weekday",
}

# Concepts page each API page should send a cold reader to first.
CONCEPTS = {
    "API-DateTime": ("Core-Concepts", "Core Concepts"),
    "API-Session": ("Sessions", "Sessions"),
    "API-Zone": ("Time-Zones", "Time Zones"),
    "API-Exchange": ("Exchange-Calendars", "Exchange Calendars"),
    "API-Period": ("Civil-and-Exact-Arithmetic", "Civil and Exact Arithmetic"),
    "API-Interval": ("Core-Concepts", "Core Concepts"),
    "API-Weekday": ("Core-Concepts", "Core Concepts"),
    "API-Functions": ("Core-Concepts", "Core Concepts"),
    "API-Enums": ("Core-Concepts", "Core Concepts"),
}

PAGE_INTROS = {
    "API-DateTime": (
        "`DateTime` is a civil date-time carrying a fixed offset, java.time's "
        "`OffsetDateTime`, not its `ZonedDateTime`. It records what a clock read "
        "and how far that clock sat from UTC. It does not know a zone's rules, so "
        "an offset stored in March is still that offset in July."
    ),
    "API-Session": (
        "A `Session` is a recurring local-time window on selected weekdays, "
        "resolved against a real calendar. Defined that way rather than as a pair "
        "of timestamps, it survives daylight saving, holidays and half days "
        "without any of them being special-cased at the call site."
    ),
    "API-Zone": (
        "A `Zone` is a standard offset plus a daylight-saving rule, not a fixed "
        "offset. Everything that needs real zone behaviour goes through here. "
        "`DstRule` is the data a zone's rule is expressed as."
    ),
    "API-Exchange": (
        "An `Exchange` is a market calendar: holidays, observance shifts, early "
        "closes and lunch breaks. These are not variations of one calendar. Most "
        "questions about a calendar are methods on `DateTime`, not on `Exchange`: "
        "`d.is_trading_day(ex)`, not `ex.is_trading_day(d)`."
    ),
    "API-Period": (
        "A `Period` is a calendar-flavoured amount of time in the sense of "
        "java.time's `Period`: years, months and days. It is not convertible to "
        "milliseconds without a reference date, because months and years have no "
        "fixed length."
    ),
    "API-Interval": (
        "An `Interval` is a half-open span of instants, `[FromMS, ToMS)`. Half-open "
        "so that consecutive intervals tile a timeline without overlapping at the "
        "join."
    ),
    "API-Weekday": (
        "`Weekday` is an enum rather than a bare int because 0=Sunday versus "
        "1=Monday confusion is the most common class of date bug. Three numbering "
        "schemes meet here and none of them agree: this library counts Sunday as "
        "0, ISO-8601 counts Monday as 1, and Pine's own `dayofweek` counts Sunday "
        "as 1. `to_int`, `to_iso_dow` and `to_pine_dow` are the three ways out."
    ),
    "API-Functions": (
        "The free functions. By the library's calling convention a function that "
        "builds a date takes loose ints, and a function that takes an instant "
        "takes it first and stays a free function, so constructors, instant "
        "accessors, parsers and formatters live here rather than as methods."
    ),
    "API-Enums": (
        "The option enums: the ones that name a choice rather than a thing. "
        "Enums stand in for bare ints and bools throughout the library, because a "
        "`Weekday` cannot be silently off by one and a `Known.UNKNOWN` will not "
        "type-check where a bool is expected. The three enums that carry methods "
        "of their own live with them: [Zone](API-Zone), "
        "[Exchange](API-Exchange) and [Weekday](API-Weekday)."
    ),
}


class Export:
    def __init__(self, name, kind, receiver, signature, params, returns,
                 description, fields, line):
        self.name = name
        self.kind = kind            # function | method | enum | type
        self.receiver = receiver    # type name for methods, else None
        self.signature = signature
        self.params = params        # [(name, text)]
        self.returns = returns
        self.description = description
        self.fields = fields        # [(name, text)] for enum/type
        self.line = line

    @property
    def page(self):
        if self.kind == "enum":
            return ENUM_HOME.get(self.name, ENUMS_PAGE)
        if self.kind == "type":
            return TYPE_HOME.get(self.name, FUNCTIONS_PAGE)
        if self.kind == "method" and self.receiver in PAGES:
            return PAGES[self.receiver][0]
        if self.kind == "method":
            return ENUMS_PAGE      # Known.is_yes
        return FUNCTIONS_PAGE

    @property
    def display(self):
        """Name as a caller writes it."""
        if self.kind == "method":
            return f"{self.receiver}.{self.name}"
        return self.name

    @property
    def anchor(self):
        return self.name

    @property
    def kind_label(self):
        return {"function": "function", "method": "method",
                "enum": "enum", "type": "type"}[self.kind]


def tag_text(line):
    """Text of a '// @tag  body' line, minus the tag and its padding."""
    body = line[2:].strip()
    return body.split(None, 1)[1].strip() if len(body.split(None, 1)) > 1 else ""


def parse(source_lines):
    exports = []
    for i, line in enumerate(source_lines):
        if not line.startswith("export "):
            continue

        # Walk back over the contiguous comment block.
        doc, j = [], i - 1
        while j >= 0 and source_lines[j].startswith("//"):
            doc.append(source_lines[j])
            j -= 1
        doc.reverse()

        rest = line[len("export "):]
        if rest.startswith("enum "):
            kind, name = "enum", rest[5:].strip()
        elif rest.startswith("type "):
            kind, name = "type", rest[5:].strip()
        elif rest.startswith("method "):
            kind, name = "method", rest[7:].split("(")[0].strip()
        else:
            kind, name = "function", rest.split("(")[0].strip()

        # Signature: the declaration minus 'export ' and the trailing '=>'.
        signature = rest[:-2].strip() if rest.rstrip().endswith("=>") else rest.strip()

        receiver = None
        if kind == "method":
            inner = signature[signature.find("(") + 1:signature.rfind(")")]
            first = inner.split(",")[0].strip()
            receiver = first.split()[0] if first else None

        description, returns = "", ""
        params, fields = [], []
        for d in doc:
            stripped = d[2:].strip()
            if stripped.startswith("@function ") or stripped.startswith("@enum ") \
                    or stripped.startswith("@type "):
                description = tag_text(d)
            elif stripped.startswith("@param "):
                body = stripped[len("@param "):].strip()
                parts = body.split(None, 1)
                params.append((parts[0], parts[1].strip() if len(parts) > 1 else ""))
            elif stripped.startswith("@field "):
                body = stripped[len("@field "):].strip()
                parts = body.split(None, 1)
                fields.append((parts[0], parts[1].strip() if len(parts) > 1 else ""))
            elif stripped.startswith("@returns"):
                returns = tag_text(d)
            elif description and not stripped.startswith("@"):
                # Continuation lines inside a doc block (the enum prose blocks
                # use them); keep them as part of the description.
                cont = stripped.lstrip()
                if cont:
                    description += " " + cont

        # Declared fields for enums and types, in source order.
        if kind in ("enum", "type"):
            declared, k = [], i + 1
            while k < len(source_lines) and source_lines[k].startswith("    ") \
                    and source_lines[k].strip():
                declared.append(source_lines[k].strip())
                k += 1
            merged = []
            for idx, (fname, ftext) in enumerate(fields):
                decl = declared[idx] if idx < len(declared) else ""
                merged.append((fname, ftext, decl))
            fields = merged

        exports.append(Export(name, kind, receiver, signature, params, returns,
                              description, fields, i + 1))
    return exports


def check(exports, source_lines):
    """The doc contract. A library edit that breaks it fails the build."""
    problems = []
    if len(exports) != EXPECTED_EXPORTS:
        problems.append(
            f"expected {EXPECTED_EXPORTS} exports, found {len(exports)}. "
            f"If the library genuinely changed, update EXPECTED_EXPORTS."
        )
    for e in exports:
        if not e.description:
            problems.append(f"{e.display} (line {e.line}): no @function/@enum/@type text")
        if e.kind in ("function", "method"):
            if not e.returns:
                problems.append(f"{e.display} (line {e.line}): no @returns")
            inner = e.signature[e.signature.find("(") + 1:e.signature.rfind(")")]
            n_sig = len([p for p in inner.split(",") if p.strip()]) if inner.strip() else 0
            if n_sig != len(e.params):
                problems.append(
                    f"{e.display} (line {e.line}): {n_sig} parameters in the "
                    f"signature, {len(e.params)} documented"
                )
        else:
            for fname, ftext, decl in e.fields:
                if not decl:
                    problems.append(f"{e.display}.{fname}: documented but not declared")

    # GitHub derives one anchor per heading, so two exports sharing a name on one
    # page would make every deep link to the second silently land on the first.
    by_page = {}
    for e in exports:
        by_page.setdefault(e.page, []).append(e)
    for page, page_exports in by_page.items():
        seen = {}
        for e in page_exports:
            if e.anchor in seen:
                problems.append(
                    f"{page}: '{e.anchor}' is the anchor for both "
                    f"{seen[e.anchor]} and {e.display}; deep links would collide"
                )
            seen[e.anchor] = e.display
    return problems


def md_escape(text):
    return text.replace("|", "\\|")


# Tokens that end in a period without ending a sentence. Kept explicit rather
# than guessed at: the next sentence often starts on a lowercase identifier
# ("... largest unit first. str.format_time cannot do this"), so requiring a
# capital letter after the period would miss half the real boundaries.
ABBREVIATIONS = {"e.g", "i.e", "cf", "vs", "etc", "approx", "no", "ibid"}

SUMMARY_LIMIT = 200


def first_sentence(text):
    """The first sentence, for the summary tables.

    A period inside an identifier (`str.format_time`, `Zone.to_unix`) is never
    followed by whitespace, so requiring whitespace excludes those for free.
    What is left is genuine sentence ends and a short list of abbreviations.
    """
    for m in re.finditer(r"\.(?=\s)", text):
        before = re.search(r"([A-Za-z.]+)$", text[:m.start()])
        if before and before.group(1).lower() in ABBREVIATIONS:
            continue
        out = text[:m.start() + 1]
        break
    else:
        out = text

    if len(out) <= SUMMARY_LIMIT:
        return out

    # A long first sentence: cut at the last clause boundary that fits, so the
    # summary ends on a complete thought rather than mid-phrase.
    head = out[:SUMMARY_LIMIT]
    cut = max(head.rfind(": "), head.rfind("; "))
    if cut > SUMMARY_LIMIT // 3:
        return head[:cut].rstrip(" ,") + "."
    cut = head.rfind(", ")
    if cut > SUMMARY_LIMIT // 3:
        return head[:cut].rstrip() + "..."
    return head.rsplit(" ", 1)[0].rstrip(" ,") + "..."


def render_signature(e):
    if e.kind != "method":
        return e.signature
    inner = e.signature[e.signature.find("(") + 1:e.signature.rfind(")")]
    rest = ", ".join(p.strip() for p in inner.split(",")[1:] if p.strip())
    return f"{e.receiver}.{e.name}({rest})"


def render_export(e):
    out = [f"### {e.anchor}", ""]

    if e.kind in ("enum", "type"):
        out.append(f"*{e.kind_label}*")
        out.append("")
        out.append(e.description)
        out.append("")
        out.append("| Member | Declared as | Meaning |" if e.kind == "enum"
                   else "| Field | Declared as | Meaning |")
        out.append("|---|---|---|")
        for fname, ftext, decl in e.fields:
            out.append(f"| `{fname}` | `{md_escape(decl)}` | {md_escape(ftext)} |")
        out.append("")
        return "\n".join(out)

    out.append("```pine")
    out.append(render_signature(e))
    out.append("```")
    out.append("")
    out.append(e.description)
    out.append("")

    if e.params:
        shown = e.params[1:] if e.kind == "method" else e.params
        if shown:
            out.append("| Parameter | Meaning |")
            out.append("|---|---|")
            for pname, ptext in shown:
                out.append(f"| `{pname}` | {md_escape(ptext)} |")
            out.append("")

    if e.returns:
        out.append(f"**Returns** &nbsp; {e.returns}")
        out.append("")

    return "\n".join(out)


def render_page(page, exports, all_exports):
    concept_page, concept_name = CONCEPTS[page]
    title = page.replace("API-", "")

    out = [f"# {title}", ""]
    out.append(f"> Concepts first: read **[{concept_name}]({concept_page})** "
               f"before this page.")
    out.append("")
    if page in PAGE_INTROS:
        out.append(PAGE_INTROS[page])
        out.append("")

    types = [e for e in exports if e.kind == "type"]
    enums = [e for e in exports if e.kind == "enum"]
    callables = [e for e in exports if e.kind in ("function", "method")]

    if types:
        out.append("## The type")
        out.append("")
        for e in types:
            out.append(render_export(e))

    if callables:
        out.append("## Members")
        out.append("")
        out.append("| | Summary |")
        out.append("|---|---|")
        for e in sorted(callables, key=lambda x: x.name):
            out.append(f"| [`{e.name}`](#{e.anchor.lower()}) | "
                       f"{md_escape(first_sentence(e.description))} |")
        out.append("")
        out.append("## Reference")
        out.append("")
        for e in sorted(callables, key=lambda x: x.name):
            out.append(render_export(e))

    if enums:
        out.append("## Enums")
        out.append("")
        out.append("| | Summary |")
        out.append("|---|---|")
        for e in sorted(enums, key=lambda x: x.name):
            out.append(f"| [`{e.name}`](#{e.anchor.lower()}) | "
                       f"{md_escape(first_sentence(e.description))} |")
        out.append("")
        for e in sorted(enums, key=lambda x: x.name):
            out.append(render_export(e))

    out.append("---")
    out.append("")
    out.append("[API Index](API-Index) &nbsp;·&nbsp; [Task Index](Task-Index) "
               "&nbsp;·&nbsp; [Glossary](Glossary)")
    out.append("")
    return "\n".join(out)


def render_index(exports):
    out = ["# API Index", ""]
    out.append(f"Every export in `std_time`, all {len(exports)} of them, in one "
               "list, so that Ctrl-F finds anything. Sorted by name; the same "
               "set sorted by the question you arrived with is on "
               "[Task Index](Task-Index).")
    out.append("")
    out.append("| Name | Kind | On | Summary |")
    out.append("|---|---|---|---|")
    for e in sorted(exports, key=lambda x: (x.name.lower(), x.display)):
        on = e.receiver if e.kind == "method" else ""
        out.append(
            f"| [`{e.display}`]({e.page}#{e.anchor.lower()}) | {e.kind_label} "
            f"| {on} | {md_escape(first_sentence(e.description))} |"
        )
    out.append("")
    return "\n".join(out)


def main():
    if not SOURCE.exists():
        sys.exit(f"source not found: {SOURCE}")
    source_lines = SOURCE.read_text(encoding="utf-8", errors="replace").split("\n")

    exports = parse(source_lines)
    problems = check(exports, source_lines)
    if problems:
        print("The library stopped documenting itself completely:\n", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        sys.exit(1)

    DOCS.mkdir(parents=True, exist_ok=True)

    by_page = {}
    for e in exports:
        by_page.setdefault(e.page, []).append(e)

    written = 0
    for page, page_exports in sorted(by_page.items()):
        (DOCS / f"{page}.md").write_text(
            render_page(page, page_exports, exports), encoding="utf-8")
        written += len(page_exports)
        print(f"  {page + '.md':24s} {len(page_exports):3d} exports")

    (DOCS / "API-Index.md").write_text(render_index(exports), encoding="utf-8")
    print(f"  {'API-Index.md':24s} {len(exports):3d} rows")

    if written != len(exports):
        sys.exit(f"emitted {written} exports but parsed {len(exports)}")
    print(f"\n{len(exports)} exports across {len(by_page)} pages, all documented.")


if __name__ == "__main__":
    main()
