"""Appendices A–G for Approach to the Sick Child. Reuses the Standard's generic
faculty material (C3–C6, PEARLS, G) and adds topic-specific content."""
import os, re
from gen import table, box
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "build", "80_appendices.html")
STD = os.path.join(HERE, "_standard_appendix_source.html")   # NRP-2025 v1.5 appendices — source of the shared faculty and design blocks
std = open(STD, encoding="utf-8").read().split("\n")
pearls = "\n".join(std[242:266]).replace("where the blender was", "where the oxygen and the IO needles were")
appC_generic = "\n".join(std[271 - 1 + 32:271 - 1 + 111 - 4])   # C3 … C6, without closing divs
appG = "\n".join(std[597:666])

def app(letter, title, body):
    return '''
<!-- ===================================================== APPENDIX %s -->
<div class="appendix" id="app%s">
  <h3><span class="caret">▸</span>%s · %s</h3>
  <div class="app-body">
%s
  </div>
</div>
''' % (letter, letter, letter, title, body)

# ------------------------------------------------------------------ A
A = '''    <h4>A1 · Blueprint against Miller's pyramid</h4>
    <p>No single instrument samples all four levels. This is what each part of the programme can honestly claim.</p>
''' + table(["Miller level", "What it means", "Instrument here", "Weight"],
  [["<b>Knows</b>", "Recalls facts, doses, thresholds", "Unit checkpoints; final assessment", "~25%"],
   ["<b>Knows how</b>", "Applies knowledge to a clinical problem", "Case-vignette checkpoints; integrative items; key-feature problems", "~45%"],
   ["<b>Shows how</b>", "Demonstrates in simulation", "OSCE stations (A3); scenarios (Appendix B); DOPS", "~20%"],
   ["<b>Does</b>", "Performs in real practice", "Mini-CEX, CBD, MSF, entrustment (A4)", "~10%"]]) + box("pitfall", "What the written assessment cannot do", "<p>The module's certificate covers only the top two rows. Anyone using it for a consequential decision must add the bottom two, with a mannequin, printed vital-sign cards and a faculty observer.</p>") + '''
    <h4>A2 · Key-feature problems</h4>
    <p>Short answers, no options. They test only the decisions on which the case turns. Use them in remediation clinics and vivas.</p>
    <h5 class="sub">KF1 — The febrile toddler at a district hospital</h5>
    <p><i>A 2-year-old with fever for three days: heart rate 170/min, capillary refill 4 s, BP 90/60 mmHg, alert. No ventilator, no PICU.</i></p>
    <ol>
      <li><b>Is this child hypotensive, and what is your fluid decision?</b><br><small>Model: threshold 74 mmHg, so not hypotensive; no bolus (SSC 2026, strong); maintenance fluid.</small></li>
      <li><b>Name three actions in the first 30 minutes that do change outcome here.</b><br><small>Model: antibiotics within the hour, glucose check and correction, haemoglobin check and transfusion if severe anaemia, early transfer, warmth.</small></li>
    </ol>
    <h5 class="sub">KF2 — The drowsy child with diabetes</h5>
    <p><i>An 11-year-old with DKA, 6 hours into treatment, develops headache and a heart rate falling from 120 to 70/min.</i></p>
    <ol>
      <li><b>What is the diagnosis, and what do you give?</b><br><small>Model: cerebral oedema; mannitol 0.5&ndash;1 g/kg or 3% saline 2.5&ndash;5 mL/kg over 10&ndash;15 minutes, head up, reduce fluids.</small></li>
      <li><b>Does this need a scan first?</b><br><small>Model: no &mdash; treat clinically; image after stabilisation.</small></li>
    </ol>
    <h5 class="sub">KF3 — The wasted child with diarrhoea</h5>
    <p><i>An 18-month-old, MUAC 105 mm, sunken eyes, drinking eagerly, warm hands.</i></p>
    <ol>
      <li><b>Which rehydration solution, how much, how fast?</b><br><small>Model: ReSoMal 5 mL/kg every 30 min for 2 h, then 5&ndash;10 mL/kg/h, alternating with F-75.</small></li>
      <li><b>Name three signs that should make you stop.</b><br><small>Model: rising pulse, rising respiratory rate, enlarging liver, puffy eyelids.</small></li>
    </ol>
    <h5 class="sub">KF4 — Night-time abdominal pain in a farming village</h5>
    <p><i>A 7-year-old woke at 3 a.m. with abdominal pain and vomiting; now has ptosis.</i></p>
    <ol>
      <li><b>Diagnosis and first treatment?</b><br><small>Model: krait envenomation; 10 vials ASV, adrenaline drawn up.</small></li>
      <li><b>What is the life-saving supportive treatment?</b><br><small>Model: ventilation &mdash; bag-mask if nothing else.</small></li>
    </ol>

    <h4>A3 · OSCE stations</h4>
    <p>Twelve stations, 6&ndash;8 minutes each, on a doll with printed vital-sign cards. Score with the six-domain rubric in Appendix C.</p>
''' + table(["#", "Station", "Tests", "Critical failure"],
  [["1", "Paediatric Assessment Triangle from a video or actor", "Category and first move", "Misses abnormal appearance"],
   ["2", "ETAT triage of six cards in 6 minutes", "Emergency, priority, queue", "Queues a child with an emergency sign"],
   ["3", "Airway opening and bag-mask ventilation", "Position, adjunct, E-C grip, rate, chest rise", "No chest rise, not corrected"],
   ["4", "Intraosseous insertion", "Site, technique, confirmation, flush", "Wrong site or no confirmation"],
   ["5", "The bolus cycle", "Fluid choice, aliquot, four reassessment questions", "Misses a stop signal"],
   ["6", "Sepsis first hour, setting-specific", "Time targets, fluid decision by setting", "Bolus in a non-hypotensive child without ICU"],
   ["7", "Status epilepticus to 20 minutes", "Drugs, doses, routes, ceiling", "Third benzodiazepine"],
   ["8", "DKA first hour and cerebral oedema recognition", "Fluid, insulin timing, warning signs", "Insulin bolus or bicarbonate"],
   ["9", "Severe wasting with shock", "15 mL/kg over an hour; monitoring", "Plan C volumes"],
   ["10", "Snakebite: 20WBCT and ASV", "Test, dose, reaction management", "Weight-scaled ASV"],
   ["11", "Anaphylaxis", "IM adrenaline dose and site", "Antihistamine first"],
   ["12", "Breaking bad news (SPIKES), with an actor", "Setting, language, silence, plan", "Euphemism; leaves without a plan"]]) + '''
    <h4>A4 · Workplace-based assessment</h4>
''' + table(["Tool", "Use it for", "Frequency", "Note"],
  [["<b>Mini-CEX</b>", "An observed triage or first-hour assessment", "2&ndash;4 per learner per year", "The feedback is the intervention"],
   ["<b>DOPS</b>", "IO insertion, bag-mask ventilation, bolus administration", "Until entrustment, then annually", "Score the procedure, not the person"],
   ["<b>CBD</b>", "Reasoning behind a case the learner led", "2&ndash;3 per year", "Ask &ldquo;what else did you consider?&rdquo;"],
   ["<b>MSF</b>", "Teamwork and communication, from nurses and peers", "Annual", "Detects the behaviours that cause harm"]]) + '''
    <h5 class="sub">Entrustment scale for the core EPA</h5>
    <p><b>EPA:</b> <i>Recognise, triage and lead the first hour of care of a seriously ill child, including a setting-appropriate fluid decision and timely referral.</i></p>
''' + table(["Level", "Descriptor"],
  [["1", "Observes only"], ["2", "Performs with direct supervision"], ["3", "Performs with indirect supervision, supervisor reachable within minutes"],
   ["4", "Performs unsupervised; supervisor available for the unexpected"], ["5", "Supervises and teaches others"]]) + '''
    <p><b>Minimum standard for a doctor covering a paediatric emergency room alone:</b> level 4 for triage, airway support, IO access and the sepsis first hour; level 3 or above for status epilepticus and DKA.</p>'''

# ------------------------------------------------------------------ B
def scenario(n, title, setup, stages, points):
    rows = "".join("<tr><td class='num'>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % s for s in stages)
    return '''    <h4>Scenario %d — %s</h4>
    <p>%s</p>
    <div class="tw"><table class="reflow"><thead><tr><th class="num">Stage</th><th>Vital-sign card</th><th>Expected actions</th><th>Facilitator trigger</th></tr></thead><tbody>%s</tbody></table></div>
    <p><b>Debrief points:</b> %s</p>
''' % (n, title, setup, rows, points)

B = '''    <p>Four branching scenarios that run on a doll and printed vital-sign cards &mdash; no simulator needed. Show the next card only when the team has done, or clearly failed to do, the expected actions.</p>
''' + scenario(1, "The febrile toddler without a PICU",
  "District hospital, 2 a.m. A 2-year-old, 12 kg, fever 3 days, drowsy. One doctor, two nurses. No ventilator.",
  [("1", "HR 170, RR 40, CRT 4 s, BP 88/56, SpO₂ 95%, glucose 2.2", "PAT, say &ldquo;sepsis&rdquo;, glucose 10% 5 mL/kg, access (IO if needed), antibiotics", "If no glucose check after 3 min: &ldquo;He is now twitching.&rdquo;"),
   ("2", "HR 165, BP 90/58, Hb 5 g/dL", "No bolus (not hypotensive, no ICU); maintenance; blood transfusion; call referral centre", "If a 20 mL/kg bolus is started: next card shows crackles and SpO₂ 88%"),
   ("3", "Stable or deteriorating per branch", "Transfer checklist, ISBAR handover by phone", "Receiving unit asks: &ldquo;What is his weight and what has he had?&rdquo;")],
  "the 2026 setting-specific fluid recommendation; hypoglycaemia and anaemia as outcome-changing actions; the transfer decision as a treatment.") + scenario(2, "Status epilepticus in a toddler",
  "PHC. An 18-month-old, 10 kg, convulsing on arrival, started 8 minutes ago at home. No IV access yet.",
  [("1", "Convulsing, SpO₂ 90%", "Airway, oxygen, glucose, buccal/intranasal midazolam 0.3 mg/kg, note the time", "If no clock: &ldquo;Mother asks how long it has been.&rdquo;"),
   ("2", "Still convulsing at 10 min", "Second benzodiazepine; IO/IV access", "If a third benzodiazepine is proposed: RR falls to 8"),
   ("3", "Still convulsing at 20 min", "Second-line drug (phenobarbital/phenytoin/levetiracetam); look for cause; call for help", "Sodium card: 121 mmol/L &mdash; does the team give 3% saline?")],
  "the two-dose ceiling; route flexibility; searching for a cause.") + scenario(3, "DKA on the ward",
  "Paediatric ward. A 10-year-old, 28 kg, newly diagnosed DKA, pH 7.02, treated for 5 hours.",
  [("1", "HR 110, BP 110/70, GCS 15, glucose 14", "Add glucose to fluids, continue insulin, check potassium", "If insulin is stopped: ketones rise on the next card"),
   ("2", "Headache, vomiting, HR 68, BP 132/86", "Recognise cerebral oedema; mannitol or 3% saline now; head up; reduce fluid", "If CT is requested first: GCS falls to 10"),
   ("3", "Improving", "Senior review, HDU, imaging once stable", "&mdash;")],
  "treating cerebral oedema clinically; insulin and glucose together.") + scenario(4, "Snakebite at a CHC",
  "CHC, 9 p.m. A 9-year-old bitten on the ankle while walking in a paddy field, 2 hours ago. Tourniquet applied by family.",
  [("1", "Swollen leg, gum bleeding", "Remove tourniquet carefully, 20WBCT, IV access, adrenaline drawn up", "20WBCT card: unclotted"),
   ("2", "Unclotted", "10 vials ASV over 30 min", "5 min into infusion: urticaria, stridor, BP 70/40"),
   ("3", "Anaphylaxis", "Stop infusion, IM adrenaline 0.01 mg/kg, fluid; restart ASV when settled", "Urine output falling at 6 h: refer for dialysis with notes")],
  "ASV dose not weight-scaled; reaction management; when to refer.") + pearls

# ------------------------------------------------------------------ C
C = '''    <h4>C1 · Three delivery models</h4>
''' + table(["Model", "Shape", "Best for", "Watch out for"],
  [["<b>Fully self-paced</b>", "Learners work through alone; one skills session at the end", "Large cohorts, interns, CME", "The skills session becoming a demonstration. Cap at 6 learners per doll."],
   ["<b>Flipped, Part by Part</b>", "Learners master a Part before each session; sessions are simulation and discussion", "PG residents, nursing cohorts", "Verify mastery first, or you end up teaching content"],
   ["<b>Intensive, 2 days</b>", "Parts A&ndash;C day one with simulation; D&ndash;E day two", "District outreach, visiting faculty", "Retention: schedule the review checks and a 6-week follow-up"]]) + '''
    <h4>C2 · A worked flipped-classroom session &mdash; Part C, shock</h4>
    <p>90 minutes, 8&ndash;12 learners, 2 dolls, 2 facilitators. Prerequisite: Units 8&ndash;11 mastered.</p>
''' + table(["Time", "Activity", "Purpose"],
  [["0&ndash;5", "Learning contract: &ldquo;Nobody here is being examined.&rdquo;", "Psychological safety"],
   ["5&ndash;15", "Rapid retrieval: the four reassessment questions; the three SSC 2026 fluid recommendations; hypotension formula", "Retrieval practice; shows where the cohort is"],
   ["15&ndash;35", "Deliberate practice: IO insertion on a model bone and the push-pull bolus technique", "The highest-yield procedural skill in Part C"],
   ["35&ndash;55", "Scenario 1 (Appendix B), run twice &mdash; once as a district hospital, once as a PICU-backed ED", "The setting-specific decision under time pressure"],
   ["55&ndash;75", "Debrief both runs, PEARLS, two points maximum", "Consolidation"],
   ["75&ndash;85", "The fifteen-second cardiac check on each other and on a doll with a &ldquo;big liver&rdquo; card", "Makes the stop signal a habit"],
   ["85&ndash;90", "&ldquo;One thing to keep, one thing to change.&rdquo;", "Commitment to change"]]) + "\n" + appC_generic

C = C.replace("A cut score chosen by preference — including the 90%", "A cut score chosen by preference — including the 80%")
C = C.replace("&ldquo;a labour-room nurse who would reliably ventilate a flat baby within 60 seconds and recognise when it was not working, but would hesitate over an unfamiliar drug dose.&rdquo;",
              "&ldquo;a first-year resident who would reliably triage, get access and start antibiotics and a setting-appropriate fluid plan within the hour, but would hesitate over a vasoactive dose or a second-line antiseizure drug.&rdquo;")
C = re.sub(r"Delivery-room audit: time to PPV, DCC rate, routine suction rate, admission temperature", "Emergency-room audit: time from arrival to antibiotics, triage-to-treatment time, weight recorded, bolus decisions by setting", C)
C = C.replace("with a labour-room audit", "with an emergency-room audit")
C = re.sub(r"Admission hypothermia, early neonatal mortality, HIE referrals within window", "Deaths within 24 hours of arrival, unplanned PICU transfers, hospital-acquired hyponatraemia", C)

# ------------------------------------------------------------------ D
D = '''    <p>Map each unit to the <b>competency descriptors</b> of the NMC CBME curriculum. The code column is deliberately blank: codes were revised in the September 2024 guidelines, and Volume II is the only authority. <b>Do not invent codes</b>; fill them in from the current document.</p>
''' + table(["Unit", "Competency descriptor (paraphrased)", "NMC code (verify)", "Domain", "Teaching method", "Assessment"],
  [["1&ndash;3", "Recognise the seriously ill child; explain paediatric physiology relevant to emergencies", "", "K, S", "Self-paced module; case discussion", "Checkpoints; CBD"],
   ["2", "Perform triage using WHO ETAT and the Paediatric Assessment Triangle", "", "S", "Simulation with cards", "OSCE 1&ndash;2"],
   ["4", "Assess and manage the airway and breathing; deliver oxygen and bag-mask ventilation", "", "S", "Skills lab", "DOPS; OSCE 3"],
   ["5, 8&ndash;10", "Recognise and manage shock, including fluid therapy and vascular access", "", "K, S", "Flipped session (C2)", "OSCE 4&ndash;6; Mini-CEX"],
   ["6, 13", "Assess the child with altered sensorium; manage status epilepticus and raised ICP", "", "K, S", "Simulation", "OSCE 7"],
   ["7", "Recognise and treat hypoglycaemia and electrolyte emergencies", "", "K", "Case-based", "Checkpoints"],
   ["11", "Manage dehydration (WHO plans) and DKA", "", "K, S", "Case-based; simulation", "OSCE 8; KF2"],
   ["12, 14", "Manage common poisonings and envenomations", "", "K, S", "Case-based", "OSCE 10; KF4"],
   ["15", "Primary survey of the injured child; burns first aid and fluid", "", "K, S", "Simulation", "Checkpoints"],
   ["16", "Manage severe wasting and nutritional oedema", "", "K, S", "Ward-based; NRC visit", "OSCE 9; KF3"],
   ["17", "Identify and manage serious bacterial infection in young infants", "", "K, S", "IMNCI practice", "Mini-CEX"],
   ["18&ndash;19", "Recognise red flags; manage children with complex needs", "", "K, A", "Case-based", "CBD"],
   ["20", "Refer and transport safely; communicate with families; safeguard children", "", "S, A, C", "Role play", "OSCE 12; MSF"]]) + box("pitfall", "Why the code column is empty", "<p>Invented or outdated competency codes are worse than none &mdash; they propagate into curriculum documents and audits. Fill the column from NMC CBME Volume II (2024) at your institution.</p>")

# ------------------------------------------------------------------ E
E = box("danger", "Verify before every use", "<p>Doses here are drawn from the cited guidelines for learning. Check every dose against your institution's protocol, a current formulary and the child in front of you. Where local protocol differs, follow local protocol. This annex is never locked.</p>") + '''
    <h4>E1 · Resuscitation and emergency drugs</h4>
''' + table(["Drug", "Indication", "Dose", "Notes"],
  [["Adrenaline 1 mg/mL (1:1000) IM", "Anaphylaxis, ASV reaction", "0.01 mg/kg (0.01 mL/kg), max 0.5 mg", "Anterolateral thigh; repeat after 5 min"],
   ["Adrenaline 0.1 mg/mL (1:10,000) IV/IO", "Cardiac arrest", "0.01 mg/kg (0.1 mL/kg), max 1 mg", "Every 3&ndash;5 min (see PALS module)"],
   ["Adrenaline infusion", "Shock", "0.05&ndash;0.3 microgram/kg/min, titrate", "Peripheral or IO acceptable; watch the site"],
   ["Noradrenaline infusion", "Shock (vasodilated)", "0.05&ndash;0.3 microgram/kg/min, titrate", "As above"],
   ["Dopamine infusion", "Shock where others unavailable", "5&ndash;10 microgram/kg/min", ""],
   ["Dobutamine infusion", "Low output, myocarditis, scorpion", "5&ndash;10 microgram/kg/min (up to 20)", ""],
   ["Adenosine", "SVT", "0.1 mg/kg rapid push (max 6 mg); then 0.2 mg/kg (max 12 mg)", "Rapid flush; ECG running"],
   ["Glucose 10%", "Hypoglycaemia", "5 mL/kg IV/IO (neonates 2 mL/kg)", "Then glucose infusion; recheck in 15&ndash;30 min"],
   ["Calcium gluconate 10%", "Hyperkalaemia, hypocalcaemia", "0.5 mL/kg IV slowly (max 20 mL)", "ECG monitoring; avoid extravasation"],
   ["Naloxone", "Opioid toxicity", "0.1 mg/kg (max 2 mg)", "Short-acting; watch for re-sedation"],
   ["Hydrocortisone", "Adrenal crisis", "~25 mg (&lt;1 y), 50 mg (1&ndash;5 y), 100 mg (&gt;5 y) IV/IM", "Use the child's emergency letter if available"],
   ["Prostaglandin E1", "Duct-dependent lesion", "Per cardiology advice", "Apnoea risk; be ready to ventilate"]]) + '''
    <h4>E2 · Fluids</h4>
''' + table(["Situation", "Fluid and volume"],
  [["Septic shock, ICU available", "Balanced crystalloid 10&ndash;20 mL/kg boluses, up to 40&ndash;60 mL/kg in hour 1"],
   ["Sepsis without hypotension, no ICU", "No bolus; maintenance"],
   ["Septic shock with hypotension, no ICU", "10&ndash;20 mL/kg boluses, up to 40 mL/kg"],
   ["Severe dehydration (WHO Plan C)", "Ringer's lactate 30 mL/kg then 70 mL/kg: under 12 m over 1 h + 5 h; 12 m and over 30 min + 2&frac12; h"],
   ["Severe wasting with shock", "15 mL/kg over 1 h of Ringer's lactate with 5% glucose (or half-normal saline with 5% glucose)"],
   ["DKA", "Shock: 20 mL/kg rapidly; otherwise 10&ndash;20 mL/kg over 20&ndash;30 min; deficit + maintenance over 24&ndash;48 h"],
   ["Burns over ~10% TBSA", "3&ndash;4 mL/kg/%TBSA Ringer's lactate in 24 h (half in first 8 h from burn) plus maintenance with glucose"],
   ["Maintenance (Holliday&ndash;Segar)", "4/2/1 mL/kg/h; isotonic with glucose as needed"]]) + '''
    <h4>E3 · Neurological and metabolic emergencies</h4>
''' + table(["Drug", "Dose", "Notes"],
  [["Lorazepam IV/IO", "0.1 mg/kg (max 4 mg)", "Two benzodiazepine doses maximum"],
   ["Diazepam IV / rectal", "0.2&ndash;0.3 mg/kg IV (max 10 mg); 0.5 mg/kg rectal (max 10&ndash;20 mg)", ""],
   ["Midazolam buccal / intranasal", "0.3 mg/kg (max 10 mg)", "No IV needed"],
   ["Levetiracetam IV", "40&ndash;60 mg/kg (max 3&ndash;4.5 g) over 5&ndash;15 min", ""],
   ["Phenytoin IV", "20 mg/kg over 20 min", "ECG or pulse monitoring"],
   ["Valproate IV", "40 mg/kg (max 3 g)", "Avoid in liver or metabolic disease, under 2 years"],
   ["Phenobarbital IV", "20 mg/kg", "Respiratory depression"],
   ["3% saline", "Raised ICP: 3&ndash;5 mL/kg; DKA cerebral oedema: 2.5&ndash;5 mL/kg; hyponatraemic seizure: 3&ndash;5 mL/kg", "Over 10&ndash;20 min"],
   ["Mannitol", "0.5&ndash;1 g/kg over 10&ndash;15 min", ""],
   ["Insulin (DKA)", "0.05&ndash;0.1 unit/kg/h, at least 1 h after fluids start", "No bolus"]]) + '''
    <h4>E4 · Poisoning and envenomation</h4>
''' + table(["Agent", "Dose", "Notes"],
  [["Atropine (organophosphate)", "0.02&ndash;0.05 mg/kg IV, double every 5 min to a clear chest; then infusion ~10&ndash;20% of loading dose/h", "Endpoint is secretions, not pupils"],
   ["Activated charcoal", "1 g/kg (max 50 g)", "Within ~1 h; airway protected; not for hydrocarbons, iron, corrosives, alcohols"],
   ["N-acetylcysteine", "Per national/local regimen", "Start within 8 h of paracetamol ingestion"],
   ["Anti-snake venom (polyvalent)", "10 vials over 30 min (same for children); repeat per protocol", "Neurotoxic: second 10 vials at 1 h if no improvement (max 20)"],
   ["Neostigmine trial (neurotoxic)", "Atropine 0.05 mg/kg then neostigmine 0.04 mg/kg (national STG)", "Most useful in cobra bites"],
   ["Prazosin (scorpion)", "30 microgram/kg orally, repeat according to response", "Watch for first-dose hypotension"]]) + '''
    <h4>E5 · Equipment by weight</h4>
''' + table(["", "Formula or guide"],
  [["Weight estimate (if no scale)", "Use a length-based tape; formula estimates are less accurate"],
   ["Tracheal tube (cuffed)", "(age/4) + 3.5 mm; depth ~3 &times; internal diameter"],
   ["IO needle sites", "Proximal tibia (1&ndash;2 cm below and medial to tuberosity); distal femur; proximal humerus in older children"],
   ["Systolic hypotension", "Under 1 month &lt;60; 1&ndash;12 months &lt;70; 1&ndash;10 years &lt;70 + 2 &times; age; over 10 years &lt;90 mmHg"]])

# ------------------------------------------------------------------ F
F = '''    <h4>Primary guidelines &mdash; the sources this module is written to</h4>
    <ul>
      <li>Weiss SL, Peters MJ, Oczkowski SJW, et&nbsp;al. <b>Surviving Sepsis Campaign International Guidelines for the Management of Sepsis and Septic Shock in Children 2026.</b> Pediatr Crit Care Med 2026;27(4):379&ndash;434. <a href="https://pubmed.ncbi.nlm.nih.gov/41869844/">PubMed</a></li>
      <li>Schlapbach LJ, et&nbsp;al. <b>International consensus criteria for pediatric sepsis and septic shock</b> (Phoenix). JAMA 2024.</li>
      <li><b>Part 8: Pediatric Advanced Life Support.</b> 2025 AHA/AAP Guidelines for CPR and ECC. Pediatrics 2026;157(1):e2025074351.</li>
      <li>World Health Organization. <b>Paediatric emergency triage, assessment and treatment: care of critically-ill children.</b> Geneva: WHO; 2016. <a href="https://www.who.int/publications/i/item/9789241510219">WHO</a></li>
      <li>World Health Organization. <b>Pocket book of hospital care for children</b>, 2nd edition. Geneva: WHO; 2013.</li>
      <li>World Health Organization. <b>WHO guideline on the prevention and management of wasting and nutritional oedema (acute malnutrition) in infants and children under 5 years.</b> Geneva: WHO; 2023.</li>
      <li>World Health Organization. <b>WHO recommendations for management of serious bacterial infections in infants aged 0&ndash;59 days.</b> Geneva: WHO; 2024.</li>
      <li>Glaser N, et&nbsp;al. <b>ISPAD Clinical Practice Consensus Guidelines 2022: Diabetic ketoacidosis and hyperglycemic hyperosmolar state.</b> Pediatr Diabetes 2022.</li>
      <li>Emeriaud G, et&nbsp;al. <b>PALICC-2</b>: Second Pediatric Acute Lung Injury Consensus Conference. Pediatr Crit Care Med 2023.</li>
    </ul>
    <h4>Indian national and professional sources</h4>
    <ul>
      <li>Ministry of Health and Family Welfare. <b>Standard Treatment Guidelines: Management of Snakebite</b> (quick reference guide and full document).</li>
      <li>Indian Academy of Pediatrics. <b>Standard Treatment Guidelines</b>, including <i>Poisoning in Children</i> and <i>Snake Envenomation</i>.</li>
      <li>MoHFW. <b>Facility-based IMNCI (F-IMNCI)</b> and Home-Based Newborn / Young Child Care programme guidance.</li>
      <li>National Center for Vector Borne Diseases Control. <b>National guidelines for clinical management of dengue.</b></li>
      <li>ICMR. <b>Treatment guidelines for antimicrobial use in common syndromes</b>; ICMR AMR surveillance network reports.</li>
      <li><b>Protection of Children from Sexual Offences Act, 2012</b>; Juvenile Justice (Care and Protection of Children) Act, 2015.</li>
      <li>National Medical Commission. <b>Competency-Based Medical Education curriculum</b>, 2024 guidelines (Volume II for competencies).</li>
    </ul>
    <h4>Key trials worth reading in full</h4>
    <ul>
      <li>Maitland K, et&nbsp;al. <b>Mortality after fluid bolus in African children with severe infection (FEAST).</b> N Engl J Med 2011;364:2483&ndash;95.</li>
      <li>Parshuram CS, et&nbsp;al. <b>Effect of a pediatric early warning system on all-cause mortality (EPOCH).</b> JAMA 2018;319:1002&ndash;12.</li>
      <li>Kuppermann N, et&nbsp;al. <b>Clinical trial of fluid infusion rates for pediatric diabetic ketoacidosis (PECARN FLUID).</b> N Engl J Med 2018;378:2275&ndash;87.</li>
      <li>Kapur J, et&nbsp;al. <b>Randomized trial of three anticonvulsant medications for status epilepticus (ESETT).</b> N Engl J Med 2019;381:2103&ndash;13.</li>
      <li>Lyttle MD, et&nbsp;al. <b>Levetiracetam versus phenytoin for second-line treatment of paediatric convulsive status epilepticus (EcLiPSE).</b> Lancet 2019;393:2125&ndash;34.</li>
      <li>Dalziel SR, et&nbsp;al. <b>Levetiracetam versus phenytoin (ConSEPT).</b> Lancet 2019;393:2135&ndash;45.</li>
      <li>Lacroix J, et&nbsp;al. <b>Transfusion strategies for patients in pediatric intensive care units (TRIPICU).</b> N Engl J Med 2007;356:1609&ndash;19.</li>
      <li>Eddleston M, et&nbsp;al. <b>Pralidoxime in acute organophosphorus insecticide poisoning.</b> PLoS Med 2009;6:e1000104.</li>
      <li>Pandi K, et&nbsp;al. <b>Efficacy of scorpion antivenom plus prazosin versus prazosin alone for Mesobuthus tamulus scorpion sting envenomation in children.</b> Arch Dis Child 2014.</li>
    </ul>
    <h4>Educational evidence base</h4>
    <ul>
      <li>Stojan J, et&nbsp;al. <b>BEME Guide No. 69</b> &mdash; technology-enhanced learning in health professions education.</li>
      <li>Regmi K, Jones L (2020) &mdash; systematic review of e-learning in health professions education.</li>
      <li>McGee (2024); Taylor (2023); Trumble (2024) &mdash; self-directed and asynchronous learning.</li>
      <li>van Gaalen AEJ, et&nbsp;al. (2021) &mdash; gamification in health professions education.</li>
      <li>Thompson &amp; Hughes (2023) &mdash; spaced retrieval and retention in clinical education.</li>
      <li>Larsen DP, Butler AC, Roediger HL (2009) &mdash; test-enhanced learning in medical education. Cepeda NJ, et&nbsp;al. (2006) &mdash; distributed practice. Butterfield B, Metcalfe J (2001) &mdash; the hypercorrection effect.</li>
      <li><b>Ottawa 2020 Consensus Statements</b> on programmatic assessment. McKinley RK, Norcini JJ. <b>AMEE Guide No. 85</b> &mdash; standard setting.</li>
    </ul>
''' + box("danger", "Check the edition before you teach from anything", "<p>Paediatric emergency guidance changes often: the sepsis guideline changed in 2026, resuscitation in 2025, malnutrition in 2023, young-infant infection in 2024. Before using any figure from this module in teaching or a protocol, confirm it against the current edition of the primary source. If you are reading this more than three years after the build date in the footer, assume something here is out of date and check.</p>")

# ------------------------------------------------------------------ G (generic, adapted)
G = appG
G = G.replace("sample 50 items from a pool of 78", "sample 50 items from a pool of 70")
G = G.replace("This module has no evidence that it changes delivery-room behaviour or neonatal outcomes.", "This module has no evidence that it changes emergency-room behaviour or child outcomes.")
G = G.replace("WHO guidance on newborn care", "WHO ETAT, IMCI and hospital care guidance for children")
G = G.replace("Part D is unintelligible without Part C", "Part C's fluid decisions make no sense without Part B's recognition of shock")
# strip wrapper lines from the NRP block so we can re-wrap consistently
G = G[G.index('<div class="app-body">') + len('<div class="app-body">'):]
G = G[:G.rindex("</div>\n</div>")] if "</div>\n</div>" in G else G

head = '''<section class="part" id="appendices">
  <div class="part-head">
    <div>
      <span class="pk">Appendices</span>
      <h2>Appendices A&ndash;G</h2>
    </div>
    <span class="part-meta"><span class="app-open-note">Never locked</span></span>
  </div>
  <p class="part-lede">Open from the first minute, whatever your progress. Appendix E (drugs, fluids and equipment) and Appendix F (references) are clinical safety material, and clinical safety material behind a quiz is a patient-safety problem. Every appendix can be printed on its own.</p>
'''
html = head + app("A", "Assessment bank", A) + app("B", "Simulation library", B) + app("C", "Faculty guide", C) + \
       app("D", "Curriculum mapping", D) + app("E", "Drug, fluid and equipment annex", E) + app("F", "References", F) + \
       app("G", "Evidence-governed design", G) + "\n</section>\n"
open(OUT, "w", encoding="utf-8").write(html)
print("wrote", OUT, len(html) // 1024, "KB")
for bad in ["neonat", "NRP", "newborn", "PPV", "labour"]:
    n = len(re.findall(bad, html, re.I))
    if n: print("  check:", bad, n)
