from gen import *

part("C", "Resuscitating shock: the core skill", "Units 8&ndash;11 · ~8 hours",
     "More preventable child deaths pass through shock than through any other door. This Part is built around the 2026 Surviving Sepsis Campaign paediatric guideline, the FEAST trial, and the one skill that separates good from dangerous shock care: knowing when fluid helps and when it kills.")

# ------------------------------------------------------------------ UNIT 8
unit(8, "C", "Fluids done right",
  "Fluid is the most commonly prescribed and least often reassessed drug in paediatric emergency care. Given well it saves the dehydrated child; given reflexively it has killed febrile children in a large randomised trial. This unit is about the difference.",
  [("e", "Give a fluid bolus correctly: choice of fluid, aliquot size, speed, and the four reassessment questions after every aliquot."),
   ("e", "State the 2026 Surviving Sepsis fluid recommendations for settings with and without intensive care."),
   ("a", "Identify the children in whom the standard bolus is wrong: cardiogenic shock, severe malnutrition, severe anaemia and dengue."),
   ("x", "Read the FEAST trial critically &mdash; what it showed, where it was done, and what it does and does not change in an Indian district hospital.")],
  [
   sec(1, "How to give a bolus", '''
  <p>A fluid bolus is a test with a treatment attached. Give a measured aliquot, then ask whether the child got better, and whether the child can take more.</p>''' + algo("The bolus cycle", '''  CHOOSE   balanced crystalloid (Ringer's lactate, Plasma-Lyte)
           0.9% saline if balanced fluid is not available
           not albumin as a first choice · never 5% dextrose
  MEASURE  10–20 mL/kg, pushed with a syringe or pressure bag
           over 5–20 minutes (gravity is too slow in a small cannula)
  REASSESS after EVERY aliquot — four questions:
     1. Is the heart rate falling?
     2. Is perfusion improving? (refill, skin temperature, pulses)
     3. Is the child more alert? Is urine coming?
     4. STOP SIGNALS: new crackles · liver edge moving down ·
        gallop · rising respiratory rate or work of breathing ·
        falling SpO2
  REPEAT   only if 1–3 are "not yet" and 4 is "none"''') + pearl('''<p>The fourth question is the one people skip. A liver edge that has moved 2 cm down since the last bolus is the child telling you the heart has had enough. Mark it on the skin with a pen before the first bolus.</p>''')),

   sec(2, "What the 2026 Surviving Sepsis guideline recommends", table(
     ["Setting and child", "Recommendation (strength)"],
     [["<b>Intensive care available</b>, septic shock", "Up to <b>40&ndash;60 mL/kg</b> of bolus fluid in the first hour, as <b>10&ndash;20 mL/kg per bolus</b>, titrated to perfusion and stopped for signs of overload (conditional)"],
      ["<b>No intensive care</b>, sepsis <b>without hypotension</b>", "<b>No fluid bolus</b> (strong recommendation against). Give maintenance fluid and treat the cause."],
      ["<b>No intensive care</b>, septic shock <b>with hypotension</b>", "Up to <b>40 mL/kg</b> of bolus fluid in the first hour, 10&ndash;20 mL/kg per bolus, with reassessment (conditional)"],
      ["Choice of fluid", "Crystalloid rather than albumin (conditional); <b>balanced or buffered crystalloid rather than 0.9% saline</b> (conditional), with saline acceptable if balanced fluid is unavailable"]]) + evidence('''<p>Weiss SL, Peters MJ, et al. <i>Surviving Sepsis Campaign International Guidelines for the Management of Sepsis and Septic Shock in Children 2026</i>. Pediatr Crit Care Med 2026;27(4):379&ndash;434 (co-published in Intensive Care Medicine). 61 statements; only three rest on high- or moderate-certainty evidence. The strong recommendation <i>against</i> bolus therapy for non-hypotensive sepsis without intensive care is one of the few firm statements in the whole guideline &mdash; and it comes from FEAST.</p>''', "Source")),

   sec(3, "FEAST: what it showed and where", evidence('''<p><b>FEAST</b> (Maitland et al., <i>NEJM</i> 2011) randomised 3,141 febrile African children with impaired perfusion to a 20&ndash;40 mL/kg bolus of saline or albumin, or to maintenance fluid only. <b>Bolus therapy increased 48-hour mortality</b> (roughly 10.6% vs 7.3%), consistently across subgroups. Later analyses pointed to cardiovascular collapse, rather than simple fluid overload, as the main mode of excess death.</p>
  <p><b>Read the setting.</b> The hospitals had no mechanical ventilation and no inotrope infusions. Many children had malaria and severe anaemia. Children with gastroenteritis, severe malnutrition and non-infectious causes of shock were excluded, and very few were hypotensive.</p>
  <p><b>The defensible reading</b> is not &ldquo;fluid is bad&rdquo;. It is: <i>large boluses are dangerous in febrile children without hypotension when you cannot support the airway and heart the bolus may unmask.</i> That is exactly the population the 2026 strong recommendation addresses.</p>''', "Read the negative trial carefully") + '''
  <p>Two errors follow from FEAST, in opposite directions. One is ignoring it and giving 60 mL/kg reflexively to every febrile child with cool hands in a hospital with no ventilator. The other is over-generalising it and withholding fluid from the child with diarrhoeal hypovolaemia or frank hypotension, in whom fluid remains life-saving and who were never in the trial.</p>''', lvl="a"),

   sec(4, "Four groups in whom the standard bolus is wrong", table(
     ["Group", "Why", "What to do instead"],
     [["<b>Cardiogenic shock</b>", "The problem is the pump; volume causes pulmonary oedema and arrest", "Small aliquots (5&ndash;10 mL/kg) only if clearly under-filled; inotrope; treat arrhythmia (Unit 10)"],
      ["<b>Severe malnutrition</b>", "Heart and kidneys handle sodium and water poorly; overload kills", "WHO: only for shock with lethargy or unconsciousness, 15 mL/kg over one hour with dextrose, watching pulse and respiratory rate every 5&ndash;10 minutes (Unit 16)"],
      ["<b>Severe anaemia</b>", "The problem is oxygen-carrying capacity, not volume", "Transfuse; do not flood"],
      ["<b>Dengue with plasma leak</b>", "Leak is phase-dependent; fluid given in the recovery phase returns as pulmonary oedema", "Follow the national dengue guideline: titrated crystalloid by haematocrit and clinical response, with early reduction as the leak stops"]]) + india('''<p><b>Dengue</b> is the single commonest reason a paediatric ward in India faces a fluid decision, and it has its own rules. Recognise the <b>critical phase</b> (usually days 3&ndash;7, as the fever falls): rising haematocrit with falling platelets, abdominal pain, persistent vomiting, mucosal bleeding, lethargy, a large liver. Fluid is given as titrated infusions guided by haematocrit and perfusion, not repeated large boluses, and is tapered as the leak stops. Most deaths now come from late recognition of shock <i>or</i> from over-infusion &mdash; not from lack of fluid alone. Use the current national (NCVBDC) dengue guideline and your state protocol.</p>''')),

   sec(5, "Across settings", tracks(
     ["Balanced crystalloid, 10&ndash;20 mL/kg aliquots, up to 40&ndash;60 mL/kg in the first hour if the child keeps responding",
      "Stop signals checked after each aliquot; move to a vasoactive rather than more fluid when they appear",
      "Point-of-care ultrasound, serial lactate and echocardiography to guide titration",
      "Ventilation available if fluid unmasks a failing heart"],
     ["Hypotensive shock, or obvious hypovolaemia from diarrhoea or bleeding: fluid is life-saving &mdash; give it, 10&ndash;20 mL/kg, reassessing each time, up to 40 mL/kg",
      "Febrile child with poor perfusion but a normal blood pressure: <b>no bolus</b>. Maintenance fluid, antibiotics now, glucose, treat severe anaemia, keep warm, transfer",
      "Use what you have: Ringer's lactate is on the essential medicines list and usually available; saline is acceptable",
      "A liver edge marked in pen, a watch and a written reassessment every 15 minutes are the monitoring you can always have"])),

   sec(6, "Maintenance fluid", '''
  <p><b>Holliday&ndash;Segar (&ldquo;4-2-1&rdquo;), per hour:</b> 4 mL/kg for the first 10 kg, plus 2 mL/kg for the next 10 kg, plus 1 mL/kg for each kg above 20. Per day: 100, 50 and 20 mL/kg respectively.</p>''' + danger('''<p><b>Use isotonic maintenance fluid in hospitalised children</b> &mdash; 0.9% saline or a balanced solution, with glucose as needed. Hypotonic fluids (0.18% or 0.45% saline) caused a generation of avoidable hospital-acquired hyponatraemic seizures and deaths, because sick children secrete antidiuretic hormone and retain free water. Measure electrolytes if IV fluid continues beyond 24 hours, and reduce volumes in meningitis, pneumonia and after surgery, where water retention is greatest.</p>''', "The lesson paid for in children's lives")),
  ],
  [Q("At a district hospital with no ventilator or inotrope infusions, a 3-year-old has fever, heart rate 170/min, capillary refill 4 seconds and BP 92/58 mmHg. Glucose is normal and haemoglobin 10 g/dL. The nearest PICU is three hours away. What is the most defensible fluid plan?",
     ["60 mL/kg of 0.9% saline over the first hour, then reassess.",
      "No bolus: start maintenance fluid, give antibiotics immediately, keep warm, and arrange urgent transfer.",
      "Withhold all fluid and antibiotics until arrival at the referral hospital.",
      "20 mL/kg of 5% dextrose over 10 minutes."],
     1,
     "Is this child hypotensive for his age? And does this hospital have intensive care?",
     "70 + (2 &times; 3) = 76 mmHg: his pressure is above that. Now find the 2026 recommendation for sepsis without hypotension where intensive care is not available.",
     "He has sepsis with poor perfusion but <b>no hypotension</b>, in a setting <b>without intensive care</b>: the 2026 guideline strongly recommends <b>against</b> a fluid bolus. What saves him is antibiotics now, maintenance fluid, glucose and anaemia checks, warmth and early transfer while he is still compensating.",
     "<b>A</b> &mdash; this is the FEAST population, in whom large boluses increased mortality. <b>C</b> &mdash; withholding antibiotics is indefensible; they are the intervention with the clearest benefit. <b>D</b> &mdash; 5% dextrose is not a resuscitation fluid; it becomes free water and can cause hyponatraemia.",
     "Strong recommendations are rare in paediatric sepsis. This is one of them. Know it cold.",
     "section 2, ‘What the 2026 Surviving Sepsis guideline recommends’"),
   Q("In a PICU-backed emergency department, a 6-year-old in septic shock has received two 20 mL/kg boluses of Ringer's lactate. Heart rate has fallen from 165 to 150/min, but crackles have appeared at both bases and the liver edge has moved from 1 cm to 3 cm below the costal margin. Capillary refill is still 4 seconds. What next?",
     ["A third 20 mL/kg bolus, since the child has only had 40 mL/kg and the guideline allows up to 60 mL/kg.",
      "Switch to 5% albumin, 20 mL/kg, because crystalloid is leaking into the lungs.",
      "Stop boluses; start a vasoactive infusion (peripheral line is acceptable) and prepare respiratory support.",
      "Give furosemide and repeat the bolus once the crackles clear."],
     2,
     "Which of the four reassessment questions just returned a stop signal?",
     "&ldquo;Up to 60 mL/kg&rdquo; is a ceiling, not a target. When crackles and a descending liver appear, what does the guideline tell you to move to instead of more fluid?",
     "New crackles and a liver edge moving down are <b>stop signals</b>: the child is no longer fluid-responsive without harm. Shock persists, so move to a <b>vasoactive infusion</b> &mdash; which the 2026 guideline suggests starting through a peripheral line rather than waiting for central access &mdash; and prepare for respiratory support.",
     "<b>A</b> &mdash; treats the ceiling as a target and ignores the stop signals. <b>B</b> &mdash; the 2026 guideline prefers crystalloid over albumin, and more volume of any kind is the wrong direction. <b>D</b> &mdash; a diuretic in a child still in shock worsens perfusion; the problem is not too much water but a heart and vessels that need support.",
     "&ldquo;Up to&rdquo; means stop earlier when the child tells you to.",
     "section 1, ‘How to give a bolus’")]
)

# ------------------------------------------------------------------ UNIT 9
unit(9, "C", "Sepsis and septic shock: the first hour",
  "Sepsis is the final common pathway for most preventable childhood deaths. It is also where the gap between what guidelines recommend and what a district hospital can deliver is widest &mdash; which makes intelligent adaptation, not protocol recitation, the real skill.",
  [("e", "Recognise sepsis clinically and say the word aloud, so the team starts the clock."),
   ("e", "Deliver the first hour: oxygen, access, cultures, antimicrobials within the recommended time, glucose, and a setting-appropriate fluid plan."),
   ("a", "Choose empirical antimicrobials for community-acquired sepsis in India, including when to add cover for scrub typhus, malaria and resistant organisms."),
   ("x", "Explain what the 2026 guideline changed and why most of it rests on low-certainty evidence.")],
  [
   sec(1, "Recognition comes before definitions", '''
  <p>Screen clinically: an unwell-looking child with fever or a low temperature, tachycardia, poor perfusion, altered behaviour, or a rising early-warning score. <b>Say &ldquo;this could be sepsis&rdquo; aloud.</b> Naming it starts the clock for the whole team.</p>
  <p>The 2026 guideline found insufficient evidence to recommend any particular systematic screening tool beyond established clinical pathways. What it does strongly recommend is that every hospital has a <b>sepsis performance-improvement programme with standard operating procedures</b> &mdash; a local pathway that people actually use.</p>''' + pitfall('''<p>Waiting for the Phoenix score, a lactate or a CRP before acting. Phoenix identifies children who already have organ dysfunction; waiting for two points means waiting for organ failure. Treat on suspicion; classify later.</p>''')),

   sec(2, "The first hour", fig("sepsis1h", "Paediatric sepsis &mdash; the first hour", '''0 min    RECOGNISE · say "sepsis" · call senior help · start the clock
0–15     oxygen · IV or IO access (IO after 2 attempts or 90 s)
         blood culture BEFORE antibiotics (never delaying them)
         bedside GLUCOSE · LACTATE · gas · Hb · electrolytes
15–60    ANTIMICROBIALS
           septic shock ........... within 1 hour  (strong)
           sepsis without shock ... within 3 hours, after
                                    rapid evaluation
         FLUID — depends on setting and blood pressure (Unit 8)
           ICU available: 10–20 mL/kg boluses, up to 40–60 mL/kg
           no ICU, no hypotension: NO bolus — maintenance only
           no ICU, hypotension: 10–20 mL/kg boluses, up to 40 mL/kg
         VASOACTIVE if shock persists after fluid (Unit 10)
         correct glucose and calcium · treat severe anaemia
ONGOING  SOURCE CONTROL · reassess every 15 minutes
         transfer early if the setting cannot escalate''')),

   sec(3, "Antimicrobials: time, choice and source", '''
  <p><b>Time.</b> For suspected septic shock, the 2026 guideline strongly recommends antimicrobials <b>as soon as possible, ideally within one hour</b>. For probable sepsis without shock, as soon as possible after appropriate evaluation, <b>ideally within three hours</b>. Take a blood culture first when it does not cause delay.</p>
  <p><b>Choice.</b> Empirical cover must match the likely organisms and your local resistance pattern:</p>''' + table(
     ["Situation", "A common starting point (check your antibiogram)"],
     [["Community-acquired sepsis, previously well child", "Third-generation cephalosporin (ceftriaxone or cefotaxime) &plusmn; an aminoglycoside"],
      ["Suspected staphylococcal or toxic shock (skin focus, erythroderma)", "Add an anti-staphylococcal agent; add clindamycin for toxin suppression"],
      ["Hospital-acquired, recent antibiotics, known ESBL colonisation", "Carbapenem or local equivalent; reserve these, do not start with them by habit"],
      ["Fever with eschar, rash, transaminitis, low platelets", "Add doxycycline or azithromycin for scrub typhus and other rickettsial illness"],
      ["Malaria-endemic area", "Test, and give IV artesunate for severe malaria"],
      ["Young infant under 2 months", "See Unit 17 (WHO 2024 regimens)"]]) + '''
  <p><b>Source control</b> &mdash; drain the abscess, remove the infected line, operate on the perforation. No antibiotic beats drainage.</p>''' + india('''<p>Antimicrobial resistance in Indian community isolates, especially Gram-negative organisms, is high and regionally variable. The ICMR AMR surveillance network publishes annual reports, and ICMR's treatment guidelines for antimicrobial use are a better anchor than any textbook table. Ask your microbiology department for a one-page paediatric antibiogram and put it next to the sepsis pathway.</p>''')),

   sec(4, "Adjuncts: what the evidence supports", table(
     ["Intervention", "2026 position and practical reading"],
     [["Hydrocortisone", "Suggested <b>against</b> in children whose shock responds to fluid and vasoactives. Insufficient evidence for or against in refractory shock. Give stress-dose steroids where adrenal insufficiency is known or likely (chronic steroid use, congenital adrenal hyperplasia, purpura fulminans)."],
      ["Procalcitonin", "Suggested against its routine use to guide stopping antibiotics."],
      ["Molecular rapid diagnostics", "Insufficient evidence for routine use."],
      ["Blood transfusion", "Once stabilised, a restrictive threshold (around 7 g/dL) is appropriate for most critically ill children (TRIPICU); higher in cyanotic heart disease, active bleeding or unstable shock."],
      ["IV immunoglobulin, blood purification, &ldquo;metabolic resuscitation&rdquo; cocktails", "Not for routine use."],
      ["Glucose", "Avoid hypoglycaemia and extreme hyperglycaemia; no insulin-driven tight control."]]) + evidence('''<p>Of 61 statements in the 2026 guideline, only three rest on high- or moderate-certainty evidence. Almost everything you do for a septic child is a conditional recommendation built on low-certainty evidence. That is a reason to individualise and reassess constantly, and to be sceptical of anyone who presents a sepsis bundle as settled science &mdash; not a reason for nihilism.</p>'''), tier="good", lvl="x"),

   sec(5, "The first hour across settings", tracks(
     ["Oxygen; IV or IO within 90 seconds; cultures drawn",
      "Antimicrobials within 1 hour for septic shock",
      "Balanced crystalloid in 10&ndash;20 mL/kg boluses to 40&ndash;60 mL/kg, stopping on overload signs",
      "Vasoactive infusion if shock persists; serial lactate; source control; ventilation when needed"],
     ["Oxygen; IV or IO; bedside glucose and haemoglobin",
      "<b>Antibiotics immediately</b> &mdash; the intervention with the clearest benefit and the one most often delayed. Add doxycycline where scrub typhus is plausible; test for and treat malaria where endemic",
      "No bolus in a non-hypotensive child; boluses only for hypotension or obvious hypovolaemia, up to 40 mL/kg",
      "Correct hypoglycaemia and transfuse severe anaemia &mdash; here they change outcome more than fluid volume",
      "Phone the receiving unit and transfer while the child is still compensating, with weight, drugs and times written down"]) + '''
  <p>The divergence is guideline-concordant, not a compromise: the Surviving Sepsis paediatric guidelines have issued setting-specific recommendations since 2020, precisely because of FEAST.</p>'''),
  ],
  [Q("A 20-month-old with fever and a spreading non-blanching rash has heart rate 180/min, capillary refill 5 seconds and is drowsy. IV access failed twice in 90 seconds. What is the correct sequence in the next ten minutes?",
     ["Keep trying peripheral access; antibiotics can wait until a vein is secured and blood cultures are drawn.",
      "Intraosseous access, blood culture from it if possible, then antibiotics immediately &mdash; with fluid decisions following the setting-specific plan.",
      "Give oral amoxicillin now and reassess the rash in an hour.",
      "Wait for the platelet count before any invasive procedure."],
     1,
     "What is the time target for antimicrobials in suspected septic shock, and what does the access rule say after two attempts or 90 seconds?",
     "A purpuric rash with shock is meningococcal sepsis until proven otherwise. Which option gets antibiotics in within the hour without abandoning the culture?",
     "This is suspected <b>septic shock</b> with a purpuric rash. After two failed attempts or 90 seconds, go <b>intraosseous</b>. Draw a culture if you can do so without delay, then give <b>antibiotics immediately</b> &mdash; within the hour. Fluid follows the setting-specific plan.",
     "<b>A</b> &mdash; persisting with failed peripheral attempts spends the child's reserve; the culture never justifies delaying antibiotics in shock. <b>C</b> &mdash; oral antibiotics are inappropriate in shock. <b>D</b> &mdash; IO insertion and antibiotic administration do not need a platelet count.",
     "Purpura plus fever plus a sick child: the first antibiotic dose is the most important thing you will do all day.",
     "section 2, ‘The first hour’"),
   Q("A 10-year-old in septic shock has responded to fluid and a low-dose adrenaline infusion: heart rate and perfusion are improving and he is more alert. A colleague suggests adding IV hydrocortisone &ldquo;to be safe&rdquo;. He has no history of steroid use. What does the 2026 guideline suggest?",
     ["Give hydrocortisone to every child on any vasoactive infusion.",
      "Give hydrocortisone only if the random cortisol is low.",
      "Give methylprednisolone rather than hydrocortisone.",
      "Do not give hydrocortisone to a child whose shock is responding to fluid and vasoactives."],
     3,
     "Is this child's shock responding, or refractory?",
     "The guideline treats two situations differently: shock that is responding, and shock that remains unstable despite fluid and catecholamines. Which situation is this?",
     "The 2026 guideline suggests <b>against</b> IV hydrocortisone in children whose shock responds to fluid and vasoactive therapy. Steroids remain appropriate where adrenal insufficiency is known or likely; for truly refractory shock the evidence is insufficient either way.",
     "<b>A</b> &mdash; routine steroids for all vasoactive-treated children are not supported. <b>B</b> &mdash; a single random cortisol in critical illness is hard to interpret and is not the guideline's trigger. <b>C</b> &mdash; there is no evidence supporting methylprednisolone here.",
     "&ldquo;To be safe&rdquo; is not an indication. Every drug given to a septic child should have a reason you can say aloud.",
     "section 4, ‘Adjuncts’")]
)

# ------------------------------------------------------------------ UNIT 10
unit(10, "C", "When fluid fails: vasoactives, access and the failing heart",
  "When a child is still shocked after appropriate fluid, the next minutes decide the outcome: a vasoactive started early through whatever line you have, an intraosseous needle instead of a fifth venous attempt, and the recognition that some shocked children have a heart problem, not a volume problem.",
  [("e", "Obtain intraosseous access within the recommended time and use it for every resuscitation drug and fluid."),
   ("e", "Recognise anaphylaxis and give intramuscular adrenaline at the correct dose."),
   ("a", "Start and titrate a vasoactive infusion through a peripheral or intraosseous line, as the 2026 guideline suggests."),
   ("a", "Recognise cardiogenic shock from myocarditis, SVT or a duct-dependent lesion, and change management accordingly."),
   ("x", "Describe the options when shock remains refractory to catecholamines, and what the evidence does and does not support.")],
  [
   sec(1, "Access in the shocked child", algo("Access algorithm", '''  PERIPHERAL IV   two attempts OR 90 seconds, whichever comes first
        │         (in decompensated shock)
        ▼
  INTRAOSSEOUS    proximal tibia: 1–2 cm below and medial to the
        │         tibial tuberosity · alternatives: distal femur,
        │         distal tibia, proximal humerus (older children)
        │         anything that goes IV can go IO — fluids, blood,
        │         antibiotics, vasoactives
        │         flush firmly; push fluid with a syringe or pressure bag
        │         avoid: a fractured bone, a bone already punctured,
        │                infection over the site
        ▼
  CENTRAL VENOUS  once resuscitation is under way, by a competent
                  operator, ultrasound-guided''') + pearl('''<p>IO access should be a reflex, not a last resort. It is fast, has a high first-attempt success rate, and every minute spent on a fifth peripheral attempt is a minute without drugs.</p>''')),

   sec(2, "Vasoactives: start early, start peripherally", '''
  <p>When shock persists after appropriate fluid &mdash; or fluid is stopped by overload signs &mdash; start a vasoactive infusion.</p>''' + table(
     ["2026 Surviving Sepsis statement", "What it means at the bedside"],
     [["Start vasoactives through <b>peripheral venous access</b> rather than delay until central access is obtained (conditional)", "Do not wait for a central line. Use a dilute solution in a good peripheral or IO line and watch the site."],
      ["<b>Insufficient evidence</b> to recommend adrenaline over noradrenaline, or vice versa, as first-line", "Choose by physiology and familiarity: adrenaline where the picture is cold, low-output shock; noradrenaline where it is warm, vasodilated shock. Reassess and switch or add as needed."],
      ["For high-dose requirements, <b>add vasopressin or further titrate catecholamines</b> (conditional)", "Refractory shock needs senior and intensive-care input."]]) + table(
     ["Agent", "Usual starting range", "Main effect"],
     [["Adrenaline (epinephrine)", "0.05&ndash;0.3 microgram/kg/min", "Inotropy and heart rate; vasoconstriction at higher doses"],
      ["Noradrenaline (norepinephrine)", "0.05&ndash;0.3 microgram/kg/min", "Vasoconstriction"],
      ["Dopamine", "5&ndash;10 microgram/kg/min", "Mixed; where adrenaline or noradrenaline are unavailable"],
      ["Dobutamine", "5&ndash;10 microgram/kg/min", "Inotropy with vasodilatation &mdash; low-output states, myocarditis"],
      ["Milrinone", "0.25&ndash;0.75 microgram/kg/min (with or without load)", "Inotropy and vasodilatation; specialist use"]]) + '''
  <p class="dash-status">Doses and dilutions: verify against Appendix E and your unit protocol. Extravasation of vasoconstrictors causes tissue injury &mdash; check the site every 15 minutes.</p>''', lvl="a"),

   sec(3, "Anaphylaxis: the distributive shock with a specific drug", '''
  <p>Sudden onset after exposure; skin or mucosal involvement (urticaria, angioedema) with respiratory compromise (stridor, wheeze) or hypotension &mdash; or hypotension alone after a known allergen.</p>''' + algo("Anaphylaxis", '''  ADRENALINE IM, anterolateral thigh, NOW
     0.01 mg/kg of 1 mg/mL (1:1000) solution · max 0.5 mg
     (practical doses: under 6 years 0.15 mg · 6–12 years 0.3 mg ·
      over 12 years 0.5 mg)
     repeat after 5 minutes if no improvement
  lie flat with legs raised (sit up if breathing is the problem)
  oxygen · IV/IO access · crystalloid 10–20 mL/kg if hypotensive
  refractory after two IM doses → adrenaline infusion, senior help
  antihistamines and steroids are ADJUNCTS — never instead of adrenaline''') + pitfall('''<p>Giving chlorpheniramine and hydrocortisone and waiting. Neither treats airway swelling or shock. Delayed adrenaline is the commonest avoidable feature of fatal anaphylaxis. Also: anti-snake venom reactions are anaphylaxis &mdash; same drug, same dose (Unit 14).</p>''')),

   sec(4, "The failing heart", '''
  <p>Suspect a cardiac cause in any shocked child with <b>a big liver, a gallop, crackles, raised neck veins, a heart rate that does not vary, or worsening after fluid</b>.</p>''' + table(
     ["Cause", "Clues", "Key action"],
     [["<b>Myocarditis</b>", "Recent viral illness; tachycardia out of proportion to fever; gallop; big liver; chest X-ray cardiomegaly; ECG changes", "Minimal fluid; inotrope (dobutamine, milrinone or low-dose adrenaline); early PICU. Intubation is high-risk &mdash; most experienced operator, cardiovascular support ready."],
      ["<b>SVT</b>", "Heart rate typically over 220/min in infants, over 180/min in children; narrow QRS; no beat-to-beat variation", "Vagal manoeuvres (ice to the face in infants); adenosine 0.1 mg/kg rapid push with flush (max 6 mg), then 0.2 mg/kg (max 12 mg); synchronised cardioversion if unstable"],
      ["<b>Duct-dependent lesion</b> in a neonate (days to weeks old)", "Shock or cyanosis in the first weeks; weak femoral pulses (coarctation, hypoplastic left heart); pre- and post-ductal saturation difference", "<b>Prostaglandin E1</b> infusion to reopen the duct; watch for apnoea. This is a cardiology emergency."],
      ["<b>Scorpion envenomation</b>", "Sting, sweating, priapism, cold limbs, hypertension then hypotension, pulmonary oedema", "Prazosin and scorpion antivenom; dobutamine for low output (Unit 14)"]]) + danger('''<p>Rapid sequence induction in a child with myocarditis or a failing heart is one of the highest-risk procedures in paediatrics. Sympatholytic drugs and positive-pressure ventilation can precipitate arrest. Plan it with the most experienced operator available, with an inotrope running and adrenaline drawn up.</p>'''), lvl="a"),

   sec(5, "Across settings", tracks(
     ["Infusion pumps, arterial line and echocardiography to guide the choice of vasoactive",
      "Central access placed once the child is stabilised; vasopressin and ECMO referral for refractory shock",
      "Paediatric cardiology on call for arrhythmia and duct-dependent lesions"],
     ["IO access is always available: a hollow needle and a syringe are enough in an emergency",
      "Where there is no infusion pump, a carefully calculated adrenaline or dopamine infusion by a burette with a drop counter, with the site watched constantly, is the pragmatic option",
      "IM adrenaline for anaphylaxis needs no equipment beyond a syringe &mdash; keep a labelled ampoule with every snakebite and vaccination tray",
      "A child with a suspected cardiac cause of shock should be discussed with the referral centre early; ask about prostaglandin before transfer of a sick neonate"]), tier="good"),
  ],
  [Q("A 7-year-old in septic shock at a teaching hospital has received 40 mL/kg of Ringer's lactate. She has crackles at both bases and her liver is 3 cm below the costal margin. Capillary refill is 4 seconds and BP 78/40 mmHg. A central line is planned but the anaesthetist is 45 minutes away. What now?",
     ["Wait for the central line before starting any vasoactive, to avoid extravasation.",
      "Give a further 20 mL/kg bolus while waiting for the central line.",
      "Start a dilute adrenaline or noradrenaline infusion through a peripheral or IO line now, watching the site.",
      "Give IV hydrocortisone and reassess in an hour."],
     2,
     "What did the 2026 guideline say about peripheral access for vasoactives?",
     "She has overload signs, so more fluid is wrong. Is waiting 45 minutes for a central line compatible with ongoing hypotensive shock?",
     "She is still in shock and has overload signs, so fluid is no longer the answer. The 2026 guideline suggests <b>starting vasoactives through a peripheral line rather than delaying for central access</b>. Choose adrenaline or noradrenaline by physiology; the guideline found insufficient evidence to prefer one.",
     "<b>A</b> &mdash; 45 minutes of hypotension is far more dangerous than a watched peripheral infusion. <b>B</b> &mdash; crackles and a descending liver are stop signals. <b>D</b> &mdash; hydrocortisone does not treat hypotension in the next ten minutes, and routine use is not recommended.",
     "The line you have is the line you use. Watch it; don't wait for a better one.",
     "section 2, ‘Vasoactives: start early, start peripherally’"),
   Q("A 4-year-old develops generalised urticaria, stridor and a BP of 70/40 mmHg five minutes into an anti-snake venom infusion. What is the first drug and dose?",
     ["Chlorpheniramine IV, then hydrocortisone IV.",
      "Adrenaline 0.01 mg/kg of 1 mg/mL solution intramuscularly into the anterolateral thigh, and stop the infusion.",
      "Adrenaline 0.1 mg/kg of 1:10,000 solution IV push.",
      "Nebulised salbutamol and observe."],
     1,
     "What is this reaction, and which drug treats airway swelling and shock at the same time?",
     "An ASV reaction with stridor and hypotension is anaphylaxis. The first-line drug has one route and one dose that you should know without calculation.",
     "This is <b>anaphylaxis</b> to anti-snake venom. Stop the infusion and give <b>IM adrenaline 0.01 mg/kg of 1 mg/mL</b> (max 0.5 mg) into the thigh; repeat after five minutes if needed. Once the reaction settles, ASV is usually restarted cautiously, because the envenomation still needs treating.",
     "<b>A</b> &mdash; antihistamines and steroids are adjuncts; they do not treat stridor or hypotension. <b>C</b> &mdash; this is ten times the IV cardiac-arrest dose and would be dangerous; IV adrenaline for anaphylaxis is an infusion in specialist hands. <b>D</b> &mdash; salbutamol does nothing for upper-airway swelling or shock.",
     "Keep adrenaline drawn up whenever ASV is running. The reaction is common; the delay should never be.",
     "section 3, ‘Anaphylaxis’")]
)

# ------------------------------------------------------------------ UNIT 11
unit(11, "C", "Dehydration, diarrhoea and diabetic ketoacidosis",
  "Oral rehydration solution is one of the most consequential medical inventions of the twentieth century, and it is still under-used. DKA is the one place in paediatrics where being too enthusiastic with fluid and insulin is more dangerous than being too slow.",
  [("e", "Classify dehydration with WHO criteria and apply Plans A, B and C correctly."),
   ("e", "Recognise DKA in a child presenting with vomiting, abdominal pain or fast breathing, and start a safe first hour."),
   ("a", "Manage DKA through the first 24 hours, including potassium, the switch to dextrose, and clinical recognition of cerebral oedema."),
   ("x", "Interpret the PECARN FLUID trial and its effect on DKA fluid practice.")],
  [
   sec(1, "Assessing dehydration", table(
     ["Sign", "No dehydration", "Some dehydration", "Severe dehydration"],
     [["Condition", "Well, alert", "Restless, irritable", "Lethargic or unconscious"],
      ["Eyes", "Normal", "Sunken", "Sunken"],
      ["Thirst", "Drinks normally", "Thirsty, drinks eagerly", "Drinks poorly or not able to drink"],
      ["Skin pinch", "Goes back quickly", "Goes back slowly", "Goes back very slowly (over 2 s)"],
      ["WHO plan", "<b>Plan A</b>: fluids at home, continue feeding, zinc", "<b>Plan B</b>: ORS 75 mL/kg over 4 hours at the facility", "<b>Plan C</b>: IV fluid"]]) + '''
  <p>Two or more signs in a column place the child in that column. The most useful single signs of significant dehydration in children are prolonged capillary refill, abnormal skin turgor and an abnormal breathing pattern; dry mucosa alone is weak evidence &mdash; a mouth-breathing child has a dry mouth.</p>'''),

   sec(2, "WHO Plan C", table(
     ["Age", "First 30 mL/kg", "Then 70 mL/kg"],
     [["Under 12 months", "over 1 hour", "over 5 hours"],
      ["12 months and older", "over 30 minutes", "over 2&frac12; hours"]]) + '''
  <p>Use Ringer's lactate (or 0.9% saline if unavailable). Repeat the first portion once if the radial pulse is still weak. Reassess every 15&ndash;30 minutes; start ORS by mouth (about 5 mL/kg/h) as soon as the child can drink; reclassify at the end and switch to Plan A or B. Give <b>zinc</b> for 10&ndash;14 days and continue feeding.</p>''' + danger('''<p><b>Look for severe malnutrition before starting Plan C.</b> In a child with severe wasting or nutritional oedema, Plan C can kill: rehydration is slower, by mouth or nasogastric tube with ReSoMal where possible, and IV fluid is reserved for shock (Unit 16).</p>''')),

   sec(3, "DKA: recognise it", '''
  <p><b>Diagnosis:</b> hyperglycaemia (blood glucose over 11 mmol/L, about 200 mg/dL) <b>and</b> ketosis (blood β-hydroxybutyrate 3 mmol/L or more, or moderate-to-large urine ketones) <b>and</b> acidosis (venous pH below 7.3 or bicarbonate below 18 mmol/L). Severity: mild pH below 7.3, moderate below 7.2, severe below 7.1.</p>''' + india('''<p>A large proportion of Indian children with type 1 diabetes present in DKA at diagnosis, often after being treated for &ldquo;gastroenteritis&rdquo;, &ldquo;acute abdomen&rdquo; or &ldquo;pneumonia&rdquo;. Deep, sighing Kussmaul breathing is repeatedly misread as a chest problem. <b>Check a capillary glucose in every child with unexplained vomiting, abdominal pain, dehydration or fast breathing.</b> It costs a few rupees and prevents deaths.</p>''')),

   sec(4, "DKA: the first hours", algo("DKA — first hours (ISPAD 2022)", '''  WEIGH · assess · but note: clinical assessment OVERESTIMATES the
  deficit in DKA. Assume about 5–7% (moderate) or 7–10% (severe).
  SHOCK (uncommon — look for another cause too):
     0.9% saline or balanced fluid, 20 mL/kg rapidly, reassess
  NO SHOCK but volume-depleted:
     10–20 mL/kg over 20–30 minutes
  THEN deficit + maintenance, replaced evenly over 24–48 h,
     isotonic (0.9% saline or balanced) initially
  POTASSIUM: add 40 mmol/L once the child passes urine and K is
     not high — total body K is ALWAYS depleted
  INSULIN: 0.05–0.1 unit/kg/hour by infusion, started at least
     1 hour AFTER fluids began · NO insulin bolus
  When glucose falls below about 14–17 mmol/L (250–300 mg/dL):
     ADD glucose to the fluid — do not stop the insulin, which is
     what clears the ketones
  NO BICARBONATE except in exceptional, life-threatening
     hyperkalaemia or cardiovascular collapse
  MONITOR hourly: glucose, neuro obs, fluid balance
          2–4 hourly: electrolytes, gas, ketones''') + evidence('''<p><b>PECARN FLUID</b> (Kuppermann et al., <i>NEJM</i> 2018): 1,389 DKA episodes randomised in a factorial design to faster or slower rehydration with 0.9% or 0.45% saline. Neither rate nor sodium content significantly changed rates of clinically apparent cerebral injury or neurocognitive outcome. It relaxed the extreme fluid caution of earlier decades &mdash; but ISPAD still advises replacing the deficit over 24&ndash;48 hours rather than rushing, and cerebral oedema remains the leading cause of DKA death in children.</p>''')),

   sec(5, "Cerebral oedema: diagnose it clinically, treat it immediately", '''
  <p>Usually 4&ndash;12 hours into treatment, but it can be present at arrival. Warning signs: <b>headache</b>, <b>recurrent vomiting</b>, <b>slowing heart rate with rising blood pressure</b>, falling or fluctuating consciousness, irritability, incontinence, cranial nerve palsy, abnormal posturing.</p>''' + danger('''<p>Treat on clinical suspicion, <b>before imaging</b>: <b>mannitol 0.5&ndash;1 g/kg over 10&ndash;15 minutes</b>, or <b>3% saline 2.5&ndash;5 mL/kg over 10&ndash;15 minutes</b>; head up; reduce the fluid rate; call for help. A normal early CT does not exclude cerebral oedema.</p>''', "Do not wait for the scan")),

   sec(6, "Across settings", tracks(
     ["Insulin by syringe pump, fluids by volumetric pump; hourly glucose and neuro obs; 2&ndash;4-hourly gas, electrolytes and ketones",
      "Hyperosmolar therapy drawn up and labelled at the bedside",
      "HDU nursing ratio for moderate and severe DKA"],
     ["<b>ORS is the headline act, not the fallback.</b> WHO Plans A and B with zinc and continued feeding resolve the great majority of diarrhoeal dehydration without a cannula",
      "Without an insulin pump, hourly subcutaneous or intramuscular rapid-acting insulin regimens are a recognised alternative &mdash; never a bolus, never large intermittent doses, always with hourly glucometer checks",
      "Without laboratory potassium, add it only once urine is passed, and watch for arrhythmia",
      "Cerebral oedema is diagnosed and treated clinically: mannitol or 3% saline at the bedside, without waiting for imaging you may not have",
      "Transfer moderate and severe DKA to a unit that can monitor hourly &mdash; after the first hour of fluid, with insulin plan and flow chart written down"])),
  ],
  [Q("An 11-year-old with new-onset DKA (pH 7.05) had 10 mL/kg saline and an insulin infusion started at hour 2. At hour 6 he complains of headache, vomits twice, and his heart rate falls from 120 to 74/min while his blood pressure rises. What is the next action?",
     ["Request an urgent CT head and act on the result.",
      "Treat presumed cerebral oedema now with mannitol or 3% saline, raise the head, and reduce the fluid rate.",
      "Increase the insulin infusion to clear the ketones faster.",
      "Give IV sodium bicarbonate to correct the acidosis."],
     1,
     "What does a falling heart rate with a rising blood pressure mean in a child being treated for DKA?",
     "Headache, vomiting and a Cushing-type response, hours into treatment. Should treatment wait for imaging?",
     "Headache, vomiting and bradycardia with rising blood pressure during DKA treatment is <b>cerebral oedema</b> until proven otherwise &mdash; the leading cause of DKA death in children. Treat <b>immediately on clinical grounds</b> with mannitol 0.5&ndash;1 g/kg or 3% saline 2.5&ndash;5 mL/kg, head up, reduced fluid rate, senior help.",
     "<b>A</b> &mdash; imaging must never delay hyperosmolar therapy, and an early CT can be normal. <b>C</b> &mdash; faster insulin lowers osmolality faster; it does not help the brain. <b>D</b> &mdash; bicarbonate is associated with cerebral injury in paediatric DKA.",
     "In DKA, the most dangerous complication is diagnosed by listening to the child, not by looking at the scan.",
     "section 5, ‘Cerebral oedema’"),
   Q("A 14-month-old weighing 9 kg has severe dehydration from acute watery diarrhoea and no signs of malnutrition. What is the correct initial WHO Plan C regimen?",
     ["Ringer's lactate 30 mL/kg over 1 hour, then 70 mL/kg over 5 hours.",
      "5% dextrose 100 mL/kg over 6 hours.",
      "ORS 75 mL/kg over 4 hours by mouth.",
      "Ringer's lactate 30 mL/kg over 30 minutes, then 70 mL/kg over 2&frac12; hours."],
     3,
     "Plan C has two schedules. Which one applies at 14 months?",
     "The slower schedule (1 hour, then 5 hours) is for infants under 12 months. This child is over 12 months.",
     "For a child <b>12 months or older</b> in severe dehydration: <b>30 mL/kg over 30 minutes, then 70 mL/kg over 2&frac12; hours</b> of Ringer's lactate. Start ORS as soon as he can drink, give zinc for 10&ndash;14 days and continue feeding.",
     "<b>A</b> &mdash; that is the schedule for infants under 12 months. <b>B</b> &mdash; 5% dextrose is not a rehydration fluid and causes hyponatraemia. <b>C</b> &mdash; Plan B is for some dehydration; this child is severely dehydrated.",
     "The 30-mL/kg first portion is the resuscitation. The 70 mL/kg is the rehydration. Both matter.",
     "section 2, ‘WHO Plan C’")]
)
