# Approach to the Sick Child

**Live:** https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-Module-Approach-to-a-Sick-child/
**All Vikkypaedia modules:** https://vikramsakaleshpurkumar-byte.github.io/

A mastery-based, self-paced module on recognising and resuscitating the seriously ill child in the first hour. It is aligned to **WHO ETAT (2016)**, the **Surviving Sepsis Campaign paediatric guidelines 2026**, **AHA/AAP PALS 2025**, the **WHO wasting and nutritional oedema guideline (2023)** and the **WHO recommendations on serious bacterial infection in young infants (2024)**, and it is read across the resource gradient.

**Version 3.0.0** (built 2026-09-24) is a complete rebuild on the Vikkypaedia Standard engine (v2.1). It expands the earlier 16 units to 20. Progress from the earlier edition is not carried over, because the units and questions have changed; learners who used it see a one-time notice.

## What it is

- One self-contained HTML file. No CDN, no framework, no network request. It works offline on a phone.
- 20 units in 5 Parts, about 28 notional hours. It has 40 checkpoint questions with two-tier hints and rationales that explain why the wrong options are wrong, plus 30 fresh integrative items for the final assessment.
- Parts: **A** Foundations · **B** ABCDE · **C** Resuscitating shock · **D** Specific emergencies (poisoning, status epilepticus and raised ICP, snake and scorpion envenomation, trauma, burns and drowning) · **E** Special populations and systems (severe wasting, the young infant, occult red flags, complex children, referral, safeguarding, QI and future directions).
- Every clinical unit has an **India lens**. Where management genuinely differs, it has **ideal and resource-constrained panels** side by side.

## Who it is for

| Learner | Default depth |
|---|---|
| MBBS students, interns, nurses | Essentials: Parts A–C |
| MBBS doctors, PG residents (MD/DNB) | Advanced: Parts A–D |
| Paediatricians, intensivists, faculty | Expert: all 20 units and appendices |

## What makes it different

- **Mastery, never completion.** There is no "mark as read" button. A unit is mastered when both of its checkpoints are currently correct.
- **Part-by-Part unlocking**, and experienced clinicians can clear Parts by challenge.
- **Spaced retrieval** at 1, 3, 7, 21 and 60 days, with a review queue and a due badge in the top bar.
- **Confidence-weighted answering.** Learners say how sure they are before answering; "confident and wrong" is flagged and calibration is shown.
- **A next-step card**, a study-days strip that never shames, and short notices when a unit or Part is earned. There are no points, badges or leaderboards.
- **The Vikkypaedia Passport** gives one learner profile and one progress summary across every module on this site, with no server.
- **The drug, fluid and equipment annex is never locked**, and any appendix can be printed.

## What the 2026 sepsis guideline changed, and how the module teaches it

- **Without intensive care:** no fluid bolus for sepsis without hypotension (a strong recommendation). For septic shock with hypotension, up to 40 mL/kg in 10–20 mL/kg boluses.
- **With intensive care:** up to 40–60 mL/kg in the first hour, in 10–20 mL/kg boluses.
- **Fluid choice:** balanced crystalloid preferred over 0.9% saline; crystalloid over albumin.
- **Antimicrobials:** within 1 hour for septic shock; within 3 hours for sepsis without shock.
- **Lactate** is measured as part of the first evaluation.
- **Vasoactives:** start them through a peripheral line rather than waiting for central access. The guideline found insufficient evidence to prefer adrenaline or noradrenaline.
- **Hydrocortisone:** not for shock that responds to fluid and vasoactives.

## Certification

The module certifies on three independent criteria:

1. **Coverage:** all 40 checkpoints currently correct.
2. **Retention:** at least 15 of the 20 units evidenced by an item answered correctly 24 hours or more after first passing it.
3. **Applied performance:** a closed-book assessment of 50 items in 75 minutes, 2 attempts, a 24-hour lock between attempts, and a **provisional** 80% cut score.

**Set your own cut score** with the Angoff, Ebel and Hofstee worksheets in Appendix C before any consequential use.

The certificate carries a default signature for Dr Vikram Sakaleshpur Kumar. It is rendered in the Great Vibes script font (SIL Open Font License) and can be replaced in Faculty settings.

## Enrolment and completion records

A four-step first run collects the learner's name and plan, stored in the browser only. The learner can download a JSON **completion record**, and `verify.html` checks it offline. **Records are self-attested:** the checksum is computed by code inside the module, so a match shows the record was not casually altered, not that the learner sat the assessment. Anything used for promotion or credentialling needs a server with authenticated sign-in, which this module deliberately does not have.

## Faculty adoption

1. Open the module and go to Final assessment → Faculty settings. Set the signatory, signature image, cut score and retention bar.
2. Click **Export a configured copy**, then rename the file to `index.html` and publish it.
3. Appendix A has a Miller's-pyramid blueprint, key-feature problems, 12 OSCE stations, WPBA tools and an entrustment scale.
4. Appendix B has four branching scenarios that run on a doll with printed vital-sign cards.
5. Appendix C has delivery models, a worked flipped session and the standard-setting worksheets.

## Rebuilding and testing it

```bash
python content/build_content.py   # units 1–20 from content/*.py → build/20_…60_*.html
python content/appendices.py      # Appendices A–G → build/80_appendices.html
python build.py                   # assemble index.html with structural assertions
python tests/test_full.py; python tests/test_ui.py; python tests/test_enrol.py
python tests/test_search.py; python tests/test_sig.py; python tests/test_loops.py
python tests/contrast.py; python tests/offline_test.py; python tests/print_test.py
```

`build/05_module.html` holds every module-specific engine value. `build/90_script.html`, `build/89_loops.js`, `build/06_loops.css` and `build/00_head.html` are the shared Vikkypaedia Standard.

## Privacy

Everything is stored in the learner's browser. There is no account, no server, no analytics and no telemetry. The DPDP Act 2023 is satisfied by collecting nothing centrally.

## Known limitations

- Fixed Leitner intervals, not fitted forgetting curves.
- Two checkpoints per unit is thin sampling.
- Placement is rule-based.
- The assessment is unproctored, and completion records are self-attested.
- The cut score is provisional.
- Kirkpatrick levels 3 and 4 are unmeasured.
- Accessibility targets WCAG 2.2 AA but has not been independently audited.
- The clinical content has not been externally peer reviewed.
- NMC CBME codes are deliberately left blank in Appendix D; fill them in from Volume II (2024).
- India epidemiology changes each year; check the current SRS bulletins.

## Contributing, licence and citation

See `CONTRIBUTING.md`: clinical corrections come first and need primary sources. Licensed CC BY-NC-SA 4.0, **excluding** the Vikkypaedia name, the name and likeness of Dr Vikram Sakaleshpur Kumar, and the certificate signature block (see `LICENSE.md`).

> Sakaleshpur Kumar V. *Approach to the Sick Child: an evidence-governed, competency-based digital module for resource-constrained settings.* Vikkypaedia; 2026. Available from: https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-Module-Approach-to-a-Sick-child/

## Disclaimer

This module is education, not a clinical protocol, and not certification to practise. Verify every dose against your institution's protocol and a current formulary.
