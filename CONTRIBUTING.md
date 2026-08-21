# Contributing

This module cites guidelines that changed substantially between 2023 and 2026 — PALS was revised in 2025, the Surviving Sepsis paediatric guidelines in 2026, the paediatric sepsis definition in 2024, and the WHO young-infant recommendations in 2024. It will go out of date. The most valuable contribution anyone can make is telling me where it already has.

## Clinical corrections — highest priority

Open an issue titled **`[Clinical] Unit N — short description`** and include:

1. **What the module says** — quote it, and give the unit and section number.
2. **What it should say.**
3. **The source** — guideline name, issuing body, year and edition, or the citation with a DOI or PubMed ID. A link to a summary or a course slide is not enough; the primary source is what will be checked.
4. **Whether it is a safety issue.** A wrong dose, a wrong threshold, a contraindication omitted, or an algorithm step in the wrong order is urgent. Say so, and I will prioritise it.

Please raise doses, cut-offs and contraindications as separate issues from wording or emphasis, so the urgent ones do not queue behind the stylistic ones.

## Guideline updates

Open an issue titled **`[Update] <guideline name> <year>`** with the citation, what changed, and which units it affects. If a recommendation was *reviewed and not changed*, that is also worth recording — it saves the next person checking.

## Educational design

Design decisions are documented with their evidence in **Appendix G**, including a section on where the design is weaker than it looks. Disagreement is welcome, but argue against the evidence cited there rather than from preference — the whole point of that appendix is to make the design contestable.

Useful contributions here include: standard-setting data if you run a formal Angoff or Ebel panel; evaluation data if you use the module with a cohort (Kirkpatrick levels 2–4 are currently unmeasured for this module); accessibility failures found with a screen reader or at 200% zoom.

## New assessment items

Items are welcome, especially for units where the bank is thin. Each item needs:

- A clinical stem with enough detail to be answerable and no detail that gives it away
- Four options, one unambiguously best, with plausible distractors that represent real errors clinicians make
- A rationale that explains **why the wrong options are wrong**, not only why the right one is right
- The unit it belongs to, and whether it is UG or PG level

Items testing recall of an isolated number are lower value than items testing a decision.

## Translations

Translation into Indian languages would substantially extend reach, particularly for nursing and frontline health-worker audiences. Open an issue before starting so effort is not duplicated. A translation is a derivative work: it must carry the CC BY-NC-SA 4.0 licence and must **remove the Vikkypaedia name, the signatory name and the photograph** from the certificate block, substituting its own (see the licence section of the README).

## Technical

The module is a single self-contained HTML file with no build step, no dependencies and no network requests. That constraint is deliberate — it is what lets the module run offline on a phone in a district hospital. Pull requests that introduce a framework, a bundler, a CDN dependency or any external request will not be merged.

Anything that touches storage must keep learner data local to the device. No analytics, no telemetry, no account, no exceptions.

If you change the DOM structure, check that the runtime still works: checkpoints are injected before the first question in each unit, appendix bodies are swapped in and out when locked, and the "Export a configured copy" function sanitises the live DOM back to a pristine state before serialising. Breaking any of these is easy to do and not obvious until a learner exports a corrupted file.

## Code of conduct

Discuss the content, not the contributor. Clinical disagreement is expected and useful; assume the other person has seen patients you have not.

## Attribution

Contributors of accepted clinical corrections and assessment items will be acknowledged in the repository unless they ask not to be.
