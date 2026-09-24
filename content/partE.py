from gen import *

part("E", "Special populations, systems and future directions", "Units 16&ndash;20 · ~7 hours",
     "The children most likely to die are the ones in whom the standard rules change: the severely malnourished child, the young infant, the not-quite-well child whose diagnosis is hiding, and the child with a complex chronic condition. Then the systems around them &mdash; referral, communication, safeguarding and improvement &mdash; and what is coming next.")

# ------------------------------------------------------------------ UNIT 16
unit(16, "E", "Severe wasting and nutritional oedema: when the rules invert",
  "Almost everything you learned in Parts B and C changes in a severely malnourished child. Applying standard emergency protocols to them is one of the commonest and most lethal errors in paediatrics &mdash; and it is entirely avoidable.",
  [("e", "Identify severe wasting and nutritional oedema using WHO anthropometric and clinical criteria."),
   ("e", "State how fluids, feeding, antibiotics and transfusion differ in the malnourished child, and the physiology behind each."),
   ("a", "Recognise and prevent refeeding syndrome."),
   ("x", "Structure an inpatient pathway that links to community management and to India's Nutrition Rehabilitation Centres.")],
  [
   sec(1, "Recognise it", '''
  <p>In children aged 6&ndash;59 months, <b>severe wasting and/or nutritional oedema</b> (the 2023 WHO terms for what used to be called severe acute malnutrition) is any one of:</p>
  <ul>
    <li>weight-for-length or weight-for-height below &minus;3 SD of the WHO standards;</li>
    <li>mid-upper arm circumference <b>below 115 mm</b>;</li>
    <li><b>bilateral pitting oedema</b> of nutritional origin.</li>
  </ul>
  <p>Any medical complication, failure of the appetite test, or severe oedema means inpatient care. For infants under six months, the 2023 WHO guideline uses a broader concept &mdash; infants <b>at risk of poor growth and development</b> &mdash; and emphasises supporting breastfeeding and the mother&ndash;infant pair.</p>''' + evidence('''<p>WHO guideline on the prevention and management of wasting and nutritional oedema (acute malnutrition) in infants and children under 5 years. Geneva: WHO; 2023. It is the first WHO guideline to cover moderate wasting and infants under six months in detail. Fluid management details in this unit follow the long-standing WHO hospital-care protocol, which the 2023 guideline did not replace.</p>''', "Source")),

   sec(2, "Why the rules invert", table(
     ["Adaptation", "Consequence", "What changes"],
     [["Reductive adaptation: slowed heart, kidney and liver function", "The heart cannot handle a fluid load; the kidney cannot excrete sodium", "<b>No routine boluses.</b> Slow rehydration, watching pulse, breathing and liver size"],
      ["Low body potassium and magnesium, excess body sodium", "Arrhythmia; oedema worsened by sodium", "Supplement potassium and magnesium; restrict sodium &mdash; hence ReSoMal instead of standard ORS"],
      ["Poor heat regulation", "Hypothermia is frequent and lethal", "Keep warm: covered head, skin-to-skin, warm room"],
      ["Low glycogen", "Hypoglycaemia, especially overnight", "Feed every 2&ndash;3 hours, day and night"],
      ["Blunted immune response", "Infection without fever or raised white count", "<b>Antibiotics for every child with complicated malnutrition</b>"],
      ["Low cardiac reserve", "Transfusion can cause heart failure", "Transfuse only for Hb below 4 g/dL (or below 6 g/dL with respiratory distress): 10 mL/kg slowly over 3 hours"],
      ["Free iron in the absence of binding proteins", "Promotes infection and oxidative injury", "<b>No iron</b> until rehabilitation, when appetite has returned"]])),

   sec(3, "The fluid decision", algo("Dehydration and shock in the malnourished child (WHO)", '''  DEHYDRATION WITHOUT SHOCK — oral or nasogastric ReSoMal
     5 mL/kg every 30 minutes for 2 hours, then
     5–10 mL/kg/hour for 4–10 hours, alternating with F-75
     STOP if: pulse or breathing rate rises, liver enlarges,
              eyelids puff up (signs of over-hydration)
  SHOCK (lethargic or unconscious, cold hands, weak fast pulse)
     IV 15 mL/kg over 1 hour: Ringer's lactate with 5% glucose
     (or half-normal saline with 5% glucose)
     check pulse and breathing every 5–10 minutes
     improving → repeat 15 mL/kg over 1 hour, then switch to
                 ReSoMal orally or by NG tube
     NOT improving → assume septic shock: maintenance IV fluid,
                 transfuse 10 mL/kg slowly if severe anaemia,
                 antibiotics, senior help
  NEVER the standard Plan C volumes''') + danger('''<p>The same child who needed 100 mL/kg in Plan C if well nourished can die of heart failure from it when severely wasted. Before any IV fluid in a child with diarrhoea, <b>look at the arms and feel the feet</b>.</p>''')),

   sec(4, "The ten steps", algo("WHO ten steps — inpatient care", '''  STABILISATION (days 1–7)
   1  treat and prevent HYPOGLYCAEMIA
   2  treat and prevent HYPOTHERMIA
   3  treat and prevent DEHYDRATION (ReSoMal, section 3)
   4  correct ELECTROLYTES (potassium, magnesium; restrict sodium)
   5  treat INFECTION (antibiotics for all with complications)
   6  correct MICRONUTRIENTS (no iron yet)
   7  start cautious FEEDING: F-75, small, frequent, including night
  REHABILITATION (weeks 2–6)
   8  CATCH-UP GROWTH: F-100 or RUTF once appetite returns
   9  SENSORY STIMULATION and emotional support
  10  PREPARE FOR FOLLOW-UP''') + pitfall('''<p><b>Refeeding syndrome.</b> Reintroducing carbohydrate drives phosphate, potassium and magnesium into cells; blood levels crash, causing arrhythmia, heart failure and death, usually on days 2&ndash;5 of feeding. It is why WHO starts with low-energy F-75 and increases slowly. Without phosphate measurement, prevent it by protocol: start low, go slow, and suspect it in any child who deteriorates on days 2&ndash;5.</p>''', "The day-three death")),

   sec(5, "Across settings", tracks(
     ["Daily electrolytes including phosphate and magnesium during refeeding",
      "Prompt testing for tuberculosis and HIV; echocardiography if heart failure is suspected",
      "Dietitian and developmental therapy input"],
     ["The WHO ten steps were designed for this setting and need almost no technology: warmth, F-75, feeds every 2&ndash;3 hours including night, ReSoMal, potassium and magnesium, antibiotics, no iron",
      "A MUAC tape and an oedema check are the screening tools &mdash; usable by an Anganwadi worker or ASHA with no scales",
      "Defaulting is the main cause of treatment failure, and it is economic, not clinical. Children without complications who pass the appetite test do well with community-based management using RUTF",
      "A child not gaining weight on correct feeding has an undiagnosed infection &mdash; tuberculosis, HIV, urinary infection &mdash; until proven otherwise"]) + india('''<p>India carries a large share of the world's wasted children. Facility care runs through <b>Nutrition Rehabilitation Centres (NRCs)</b>, following the WHO steps, linked to community identification by Anganwadi workers and ASHAs under ICDS and POSHAN Abhiyaan. Know where your nearest NRC is and how to refer to it.</p>''')),
  ],
  [Q("A 14-month-old with visible severe wasting and MUAC 102 mm has had watery diarrhoea for three days. She is irritable, has sunken eyes and drinks eagerly; hands are warm and pulse is normal. What is the correct rehydration plan?",
     ["Ringer's lactate 30 mL/kg over 30 minutes, then 70 mL/kg over 2&frac12; hours (WHO Plan C).",
      "ReSoMal 5 mL/kg every 30 minutes for 2 hours, then 5&ndash;10 mL/kg/hour, alternating with F-75, watching pulse, breathing and liver size.",
      "Standard ORS 75 mL/kg over 4 hours (Plan B).",
      "Withhold all fluids and feeds until the diarrhoea stops."],
     1,
     "What has MUAC 102 mm just changed about every fluid rule you know?",
     "She is dehydrated but not shocked. For a severely wasted child, which solution has less sodium and more potassium &mdash; and which volumes are safe for her heart?",
     "She has severe wasting with dehydration but <b>no shock</b>. Rehydrate slowly with <b>ReSoMal</b>, orally or by nasogastric tube, alternating with F-75, and stop if the pulse or breathing rate rises, the liver enlarges or the eyelids puff up.",
     "<b>A</b> &mdash; Plan C volumes can precipitate heart failure in a severely wasted child. <b>C</b> &mdash; standard ORS has too much sodium and too little potassium for her. <b>D</b> &mdash; withholding fluid and food worsens dehydration, hypoglycaemia and hypothermia.",
     "Measure the arm before you open the drip.",
     "section 3, ‘The fluid decision’"),
   Q("On day 3 of treatment with F-75, a severely wasted 2-year-old who had been improving becomes breathless and oedematous, with a heart rate of 170/min. What is the most likely cause?",
     ["Refeeding syndrome.",
      "Normal rehabilitation-phase catch-up growth.",
      "Iron toxicity from routine supplements.",
      "Worsening of nutritional oedema from too little protein."],
     0,
     "What happens to phosphate, potassium and magnesium when a starved body starts receiving carbohydrate?",
     "Days 2&ndash;5 of feeding, cardiac failure, a previously improving child. Which complication has exactly that timing?",
     "Deterioration with heart failure on <b>days 2&ndash;5 of feeding</b> is <b>refeeding syndrome</b> until proven otherwise: insulin drives phosphate, potassium and magnesium into cells and blood levels crash. Reduce the feed volume, check and replace electrolytes including phosphate if possible, and treat the heart failure.",
     "<b>B</b> &mdash; catch-up growth comes later and does not cause heart failure. <b>C</b> &mdash; iron should not have been given in stabilisation, and toxicity would not look like this. <b>D</b> &mdash; the problem is the speed of refeeding, not too little protein.",
     "In malnutrition the most dangerous day is often not day one, but day three.",
     "section 4, ‘The ten steps’")]
)

# ------------------------------------------------------------------ UNIT 17
unit(17, "E", "The sick young infant (under 2 months)",
  "In the first two months of life, serious illness looks like almost nothing: a baby who is not feeding well, who is a little quiet, a little cold. By the time it looks like something, it is late.",
  [("e", "Use the WHO seven-sign algorithm to identify possible serious bacterial infection in infants aged 0&ndash;59 days."),
   ("e", "Recognise the young-infant emergencies that are not infection: hypoglycaemia, hypothermia, duct-dependent heart disease, surgical and metabolic crises."),
   ("a", "Apply the WHO 2024 recommendations for managing serious bacterial infection, including when referral is not possible."),
   ("x", "Recognise the infant presentations of inherited metabolic disease and non-accidental head injury.")],
  [
   sec(1, "The seven signs", table(
     ["WHO sign of possible serious bacterial infection (0&ndash;59 days)"],
     [["Not feeding well, or not able to feed at all"],
      ["Movement only when stimulated, or no movement at all"],
      ["Temperature 38 &deg;C or above"],
      ["Temperature below 35.5 &deg;C"],
      ["Severe chest indrawing"],
      ["Convulsions"],
      ["Fast breathing (60/min or more) in an infant aged 0&ndash;6 days"]]) + evidence('''<p>WHO recommendations for management of serious bacterial infections in infants aged 0&ndash;59 days (2024) recommend this seven-sign algorithm for identifying infants who need further evaluation (strong recommendation, moderate-certainty evidence). In the source analysis it had a sensitivity of about 0.79 and specificity of about 0.77 &mdash; it will miss some infants, which is why follow-up and safety-netting still matter.</p>''', "Source")),

   sec(2, "What WHO 2024 recommends when referral is not possible", table(
     ["Group", "Recommendation"],
     [["<b>Critical illness</b> (e.g. unable to feed, no movement, convulsions)", "Refer. If referral is impossible: IM/IV ampicillin plus gentamicin for at least 10 days"],
      ["<b>Clinical severe infection</b> (any other sign except fast breathing alone)", "Refer. If impossible: oral amoxicillin for at least 7 days plus IM gentamicin for at least 7 days (or, if 7 days of injections are not feasible, gentamicin for 2 days)"],
      ["<b>Fast breathing alone, 0&ndash;6 days</b>", "Refer. If impossible: oral amoxicillin for at least 7 days"],
      ["<b>Fast breathing alone, 7&ndash;59 days</b>", "Oral amoxicillin for at least 7 days; can be managed outside hospital according to clinical judgement"]]) + '''
  <p class="dash-status">Doses (Appendix E): amoxicillin 50 mg/kg twice daily in the first week of life, then three times daily; gentamicin 5 mg/kg daily in the first week, then 7.5 mg/kg daily. In hospital, follow your SNCU or paediatric ward protocol and local resistance patterns.</p>''' + india('''<p>India's <b>F-IMNCI</b>, the <b>Home-Based Newborn Care</b> and <b>Home-Based Young Child Care</b> programmes, and the <b>SNCU and NBSU</b> network are the delivery system for exactly these infants. ASHAs visiting at home are often the first to see the seven signs; the quality of what happens next depends on whether the facility they refer to recognises the infant as an emergency.</p>'''), lvl="a"),

   sec(3, "Young-infant emergencies that are not infection", table(
     ["Emergency", "Clues", "First action"],
     [["<b>Hypoglycaemia</b>", "Jittery, lethargic, poor feeding, apnoea, seizures", "Glucose at the bedside; 10% glucose 2 mL/kg IV then an infusion (neonatal dosing); feed"],
      ["<b>Hypothermia</b>", "Cold to touch, lethargic, poor feeding", "Skin-to-skin (Kangaroo Mother Care), warm room, cap; look for sepsis"],
      ["<b>Duct-dependent heart disease</b>", "Shock or deep cyanosis in the first weeks; weak femoral pulses; big liver", "Prostaglandin E1; discuss with cardiology (Unit 10)"],
      ["<b>Surgical emergencies</b>", "<b>Bilious (green) vomiting</b>; distension; blood in stool; projectile vomiting at 3&ndash;6 weeks", "Bilious vomiting is malrotation with volvulus until proven otherwise: nil by mouth, gastric tube, fluids, <b>urgent surgical review</b>"],
      ["<b>Inherited metabolic disease</b>", "Well at birth, then poor feeding, vomiting, lethargy, seizures, unusual odour, after feeds start", "Glucose, gas, ammonia; stop protein feeds; glucose infusion; metabolic team"],
      ["<b>Non-accidental head injury</b>", "Irritability, vomiting, seizures, a bulging fontanelle, unexplained bruises", "Treat, then safeguard (Unit 20)"]]) + pearl('''<p>Green vomit in a baby is a surgical emergency until a surgeon says otherwise. Hours matter: a volvulus can infarct the whole midgut.</p>''')),

   sec(4, "Across settings", tracks(
     ["SNCU or NICU care with blood cultures, CSF and inflammatory markers before antibiotics",
      "Echocardiography, prostaglandin, paediatric surgery and metabolic testing on site"],
     ["The seven signs need no equipment. A thermometer and a watch are enough",
      "Give the first dose of antibiotics <b>before</b> referral, and keep the baby warm on the journey with skin-to-skin contact",
      "If referral is refused or impossible, the WHO 2024 outpatient regimens are evidence-based options &mdash; not a failure of care",
      "Keep the mother and baby together; breastfeeding continues unless the infant cannot feed"])),
  ],
  [Q("A 20-day-old is brought by an ASHA because she has been feeding poorly for a day. Temperature 35.2 &deg;C, respiratory rate 52/min, no chest indrawing, moves normally. Which is correct?",
     ["She has no WHO sign of serious infection, because her breathing rate is below 60/min.",
      "She has fast breathing alone, so oral amoxicillin at home is sufficient.",
      "She has signs of possible serious bacterial infection: warm her, give the first antibiotic doses, and refer.",
      "Low temperature at this age is normal; advise the mother to wrap her more warmly and return in two days."],
     2,
     "Count her signs against the seven. Is a low temperature one of them?",
     "Two signs are present: not feeding well, and temperature below 35.5 &deg;C. Which group does that put her in?",
     "Poor feeding and a temperature below <b>35.5 &deg;C</b> are both WHO signs of <b>possible serious bacterial infection</b> &mdash; clinical severe infection. Warm her (skin-to-skin), give the first antibiotic doses, and refer. If referral is impossible, WHO 2024 gives an outpatient regimen of oral amoxicillin plus gentamicin.",
     "<b>A</b> &mdash; she has two of the seven signs; fast breathing is not the only one. <b>B</b> &mdash; she does not have fast breathing alone, and at 52/min she has no fast breathing at all. <b>D</b> &mdash; a low temperature in a young infant is as ominous as fever.",
     "In young infants, cold is a fever. Treat it as seriously.",
     "section 1, ‘The seven signs’"),
   Q("A 10-day-old has vomited green fluid three times this morning. He was well yesterday; his abdomen is soft and he is not distended. What should happen next?",
     ["Reassure: a soft abdomen excludes a surgical cause; review tomorrow.",
      "Treat as gastroenteritis with oral rehydration.",
      "Change to a lactose-free formula.",
      "Nil by mouth, gastric tube, IV fluids and urgent surgical review for possible malrotation with volvulus."],
     3,
     "What colour of vomit makes a paediatric surgeon come to the emergency room at night?",
     "Bilious vomiting in a neonate is a surgical emergency until proven otherwise &mdash; even when the abdomen looks normal. Why does a soft abdomen not reassure you?",
     "<b>Bilious vomiting in a neonate is malrotation with volvulus until proven otherwise.</b> The abdomen is often soft and undistended early. Stop feeds, pass a gastric tube, start IV fluids and get an urgent surgical review and contrast study; hours of delay can cost the whole midgut.",
     "<b>A</b> &mdash; a soft abdomen is common early in volvulus. <b>B</b> &mdash; gastroenteritis does not cause bilious vomiting as the first sign in a well neonate. <b>C</b> &mdash; formula changes have no role here.",
     "Green vomit: a surgeon, today.",
     "section 3, ‘Young-infant emergencies that are not infection’")]
)

# ------------------------------------------------------------------ UNIT 18
unit(18, "E", "Occult red flags in the not-quite-well child",
  "Not every sick child is crashing. Some come to OPD for the fourth time, after three courses of antibiotics, with a parent who keeps saying the same sentence: &ldquo;He is just not the same child.&rdquo; That sentence deserves more diagnostic weight than most blood tests.",
  [("e", "Build a structured differential for prolonged fever, pallor, weight loss and lymphadenopathy."),
   ("e", "Recognise the red flags of childhood cancer, tuberculosis and immunodeficiency."),
   ("e", "Give a specific, documented safety-net to every family sent home without a diagnosis."),
   ("a", "Plan a staged, affordable investigation pathway, and know when to stop giving antibiotics and start investigating.")],
  [
   sec(1, "The parent's concern is a vital sign", '''
  <p>Parental concern independently predicts serious illness and deterioration, which is why it is an escalation trigger in modern early-warning systems. Phrases that should raise your suspicion:</p>
  <ul>
    <li>&ldquo;He is not himself.&rdquo; &ldquo;She is not playing.&rdquo;</li>
    <li>&ldquo;He has never been like this before.&rdquo;</li>
    <li>&ldquo;I have brought him three times and he is getting worse.&rdquo;</li>
    <li>&ldquo;He wakes at night crying with leg pain.&rdquo;</li>
  </ul>
  <p>The reverse matters too: a child who is genuinely playing is rarely about to collapse. Put a toy in front of them and watch.</p>'''),

   sec(2, "Prolonged fever", table(
     ["Category", "Consider", "Discriminating step"],
     [["<b>Infection</b> (about half)", "Tuberculosis, enteric fever, urinary infection, endocarditis, deep abscess, osteomyelitis, malaria, kala-azar, scrub typhus, brucellosis, HIV", "Contact, travel, animal and food history; urine; blood culture; chest X-ray"],
      ["<b>Malignancy</b>", "Leukaemia, lymphoma, neuroblastoma", "Full blood count <b>with a film examined by a person</b>; LDH; imaging"],
      ["<b>Inflammatory</b>", "Systemic JIA, Kawasaki disease, SLE, inflammatory bowel disease, HLH", "Rash and arthritis pattern, mucocutaneous signs, ferritin"],
      ["<b>Other</b>", "Drug fever, thyrotoxicosis, fabricated illness", "Medication review; fever documented by staff"]]) + india('''<p><b>Tuberculosis</b> is the single most important missed diagnosis in a child with prolonged fever, weight loss or faltering growth. Take a contact history in every such child; a normal chest X-ray does not exclude abdominal, nodal or CNS TB. Use the national programme's diagnostic algorithms and rapid molecular tests (CBNAAT/Truenat) on gastric aspirate, induced sputum or other specimens where available.</p>''')),

   sec(3, "Cancer red flags", table(
     ["Presentation", "Red flags", "Think of"],
     [["Pallor, bruising, fever", "Unexplained pallor, bleeding, bone pain, big liver or spleen, lymphadenopathy", "Leukaemia, lymphoma"],
      ["Headache", "Morning headache with vomiting, neurological signs, squint, ataxia, head tilt, rising head circumference in an infant", "Brain tumour"],
      ["Abdominal mass", "Any mass; hypertension; eyes that dart (opsoclonus); bruising around the eyes", "Neuroblastoma, Wilms tumour, hepatoblastoma"],
      ["Bone or limb pain", "Pain waking the child at night, a limp without injury, a &ldquo;sprain&rdquo; that does not settle", "Bone tumours, leukaemia"],
      ["Eye", "White pupil (leukocoria), new squint, absent red reflex", "Retinoblastoma"],
      ["Lymph node", "Over 2 cm, hard, matted, painless, growing beyond 2&ndash;4 weeks, supraclavicular at any size, with weight loss or night sweats", "Lymphoma, tuberculosis"]]) + pearl('''<p>Two four-second habits: <b>check the red reflex</b> in every infant and young child, and <b>feel the abdomen properly</b> in every child with vague symptoms. Retinoblastoma and Wilms tumour are curable when found early.</p>''')),

   sec(4, "Safety-netting", '''
  <p>Every child sent home without a diagnosis needs a specific, documented safety-net. &ldquo;Come back if worse&rdquo; does not work.</p>''' + algo("The four-part safety-net", '''  1  WHAT I THINK this is, and how long it should last
  2  EXACTLY WHAT should bring you back immediately:
       a rash that does not fade under a glass · fast breathing or
       sucking in of the ribs · refusing all feeds · floppy or hard
       to wake · a fit · cold, mottled hands and feet · no urine for
       8–12 hours · fever beyond the day I told you
  3  WHERE to go and HOW — the facility, the hours, what to do at
       2 a.m. (transport is a clinical variable)
  4  A PLANNED REVIEW at a definite time and place
  then DOCUMENT the words you used''')),
  ],
  [Q("A 5-year-old has had three weeks of intermittent fever, has become pale, refuses to walk in the mornings because of leg pain, and has a 2.5 cm firm cervical node. What is the most appropriate next step?",
     ["A further 10-day course of oral antibiotics and review in two weeks.",
      "Reassure: growing pains and a reactive node.",
      "Full blood count with a film examined by a person, plus LDH and uric acid, and urgent paediatric referral.",
      "Start empirical anti-tuberculosis treatment without further investigation."],
     2,
     "Fever, pallor, bone pain that stops a child walking, and a node over 2 cm. What cluster is that?",
     "Which single test could show the answer today &mdash; and does it need to be read by a machine or a person?",
     "Prolonged fever, pallor, bone pain limiting walking and a significant node is <b>leukaemia until proven otherwise</b>. A blood count with a <b>film examined by a person</b> can show blasts; LDH and uric acid support the diagnosis and warn of tumour lysis. Refer urgently.",
     "<b>A</b> &mdash; another course of antibiotics delays a cancer diagnosis. <b>B</b> &mdash; growing pains do not cause fever, pallor or refusal to walk. <b>D</b> &mdash; empirical TB treatment without investigation risks missing leukaemia and exposes the child to unnecessary drugs.",
     "The fourth course of antibiotics is usually the moment to stop and investigate.",
     "section 3, ‘Cancer red flags’"),
   Q("You are discharging a 3-year-old with a viral illness at 11 p.m. Which safety-net advice is most effective?",
     ["&ldquo;Come back if he gets worse.&rdquo;",
      "&ldquo;Come back straight away to this emergency department, at any hour, if he is breathing fast or sucking in at the ribs, is hard to wake, has a rash that doesn't fade when you press a glass on it, stops drinking, or passes no urine for 12 hours; otherwise see me in the clinic on Thursday at 10 a.m.&rdquo;",
      "&ldquo;Give paracetamol and he will be fine.&rdquo;",
      "&ldquo;Call your family doctor if you are worried.&rdquo;"],
     1,
     "Which answer would still work for a frightened parent at 3 a.m.?",
     "A usable safety-net names what to watch for, where to go, when, and a planned review. Which option contains all four?",
     "Effective safety-netting names <b>specific signs</b>, <b>where and when</b> to return (including at night), and a <b>planned review</b>. Document the words you used.",
     "<b>A</b> &mdash; &ldquo;worse&rdquo; means different things to different parents. <b>C</b> &mdash; false reassurance, and no plan if you are wrong. <b>D</b> &mdash; a family doctor may not be reachable at 3 a.m., and it gives no signs to watch for.",
     "A safety-net is a treatment. Prescribe it as carefully as a drug.",
     "section 4, ‘Safety-netting’")]
)

# ------------------------------------------------------------------ UNIT 19
unit(19, "E", "The child with chronic and complex illness",
  "Children with medical complexity are a small fraction of paediatric patients and a large fraction of emergencies, admissions and deaths. They also attract a predictable set of errors.",
  [("e", "Recognise diagnostic overshadowing and take a structured baseline history from a carer."),
   ("e", "Manage the common device emergencies: a blocked tracheostomy, a shunt malfunction, a dislodged gastrostomy, a febrile central line."),
   ("a", "Recognise condition-specific crises &mdash; adrenal, metabolic, sickle cell, febrile neutropenia, cyanotic spell &mdash; and act within the correct time."),
   ("x", "Discuss ceilings of treatment and an emergency care plan with a family, within Indian law and practice.")],
  [
   sec(1, "Diagnostic overshadowing", danger('''<p>A new symptom in a child with cerebral palsy, Down syndrome, autism or a chronic condition is put down to the known diagnosis and not investigated. The child with cerebral palsy who is &ldquo;irritable because of spasticity&rdquo; has a fractured femur, a torsion, a corneal abrasion, dental pain or a urinary infection. <b>Assume a new symptom has a new cause.</b></p>''', "The central error") + '''
  <p>Ask the carer three questions: <b>What is normal for this child?</b> (tone, alertness, saturations, feeding, seizure frequency) <b>What is different today? What usually works?</b> The carer of a complex child is often the most expert person in the room.</p>'''),

   sec(2, "Device emergencies", table(
     ["Device", "Emergency", "Action"],
     [["<b>Tracheostomy</b>", "Blocked or displaced tube: distress with little air movement", "Suction; remove the inner tube if present; if a suction catheter will not pass, <b>change the tube</b> (same size, then smaller). If that fails, ventilate by mask over the face or by the stoma, and call for help."],
      ["<b>VP shunt</b>", "Blockage or infection: headache, vomiting, drowsiness, bulging fontanelle, fever", "A raised-pressure emergency (Unit 13): urgent imaging and neurosurgery. Do not send home a drowsy child with a shunt."],
      ["<b>Gastrostomy</b>", "Dislodged tube", "The tract closes within hours: replace it, or keep it open with a catheter, then confirm position before use"],
      ["<b>Central line</b>", "Fever", "Line infection until proven otherwise: cultures from the line and a vein, antibiotics now"],
      ["<b>Home ventilator</b>", "Circuit or power failure", "Disconnect and ventilate by bag with oxygen. Do not troubleshoot a machine while the child is not breathing."]])),

   sec(3, "Condition-specific crises", table(
     ["Condition", "Crisis", "Immediate action"],
     [["Adrenal insufficiency, CAH, long-term steroids", "Shock, hypoglycaemia, low sodium, high potassium during illness", "<b>Hydrocortisone immediately</b> IV or IM (about 25 mg under 1 year, 50 mg 1&ndash;5 years, 100 mg over 5 years), with glucose and saline. Never delay for tests."],
      ["Inherited metabolic disease", "Decompensation: vomiting, encephalopathy, high ammonia", "Stop protein, high glucose infusion, urgent ammonia, the family's emergency letter, metabolic team"],
      ["Sickle cell disease", "Pain crisis, acute chest syndrome, splenic sequestration, stroke", "Prompt, adequate analgesia; oxygen; fluids; infection screen; transfusion as indicated. A suddenly enlarging spleen with falling haemoglobin is sequestration &mdash; transfuse."],
      ["Child on chemotherapy", "<b>Febrile neutropenia</b>", "Broad-spectrum IV antibiotics <b>within one hour of arrival</b>, before the count is back"],
      ["Tetralogy of Fallot", "Hypercyanotic spell", "Knee-to-chest, oxygen, calm the child, morphine, fluid; then phenylephrine or a beta-blocker. Avoid inotropes that increase contractility."]]) + '''
  <p class="dash-status">Hydrocortisone stress doses vary between national guidelines; use the child's own emergency letter if they have one, and Appendix E.</p>''', lvl="a"),

   sec(4, "Ceilings of treatment and emergency care plans", '''
  <p>For a child with a progressive, life-limiting condition, the most important conversation happens before the crisis, in clinic, unhurried. Frame it around what the family hopes for and fears, not around a list of things to withhold. Record an emergency care plan the family carries with them.</p>''' + india('''<p>Indian law on withholding and withdrawing life-sustaining treatment has developed through Supreme Court judgments recognising advance medical directives and passive euthanasia, with procedures simplified in 2023; institutional practice still varies widely and decisions for children are made with extended families. Involve senior colleagues and your institution's ethics committee, document carefully, and prioritise palliative care and symptom relief, which remain under-provided for children.</p>'''), tier="good", lvl="x"),
  ],
  [Q("A 4-year-old with a tracheostomy is in severe respiratory distress. Oxygen to the tracheostomy does not help, the chest barely moves, and a suction catheter will not pass down the tube. What next?",
     ["Increase the oxygen flow and observe.",
      "Request a chest X-ray before intervening.",
      "Give nebulised salbutamol through the tracheostomy.",
      "Remove and replace the tracheostomy tube; if replacement fails, ventilate by face mask or via the stoma while calling for help."],
     3,
     "If a suction catheter will not pass, where is the obstruction?",
     "The tube itself is blocked or displaced. A blocked tracheostomy is a complete airway obstruction. Which option removes the obstruction?",
     "A suction catheter that will not pass means the tube is <b>blocked or displaced</b> &mdash; complete airway obstruction. <b>Change the tube</b> (same size, then smaller); if that fails, ventilate by mask over the face or the stoma, and call for help.",
     "<b>A</b> &mdash; oxygen cannot pass a blocked tube. <b>B</b> &mdash; the child will arrest before the film is taken. <b>C</b> &mdash; the problem is a blocked tube, not bronchospasm.",
     "In a tracheostomy emergency, the tube is guilty until proven innocent.",
     "section 2, ‘Device emergencies’"),
   Q("A 6-year-old on maintenance chemotherapy has a temperature of 38.6 &deg;C and looks reasonably well. The blood count will take two hours. What is the correct action?",
     ["Wait for the neutrophil count before deciding on antibiotics.",
      "Take cultures and give broad-spectrum IV antibiotics within one hour of arrival, without waiting for the count.",
      "Give oral antibiotics and review tomorrow.",
      "Give paracetamol and observe for four hours."],
     1,
     "Does a child with few neutrophils look as sick as their infection is?",
     "Febrile neutropenia has a time target with mortality attached. Is it measured from arrival or from the blood result?",
     "Treat as <b>febrile neutropenia</b>: cultures, then broad-spectrum <b>IV antibiotics within one hour of arrival</b>, without waiting for the count. Neutropenic children mount little inflammatory response and can deteriorate within hours despite looking well.",
     "<b>A</b> &mdash; a two-hour wait breaks the time target. <b>C</b> &mdash; oral antibiotics and next-day review are not appropriate before risk assessment. <b>D</b> &mdash; paracetamol masks the fever without treating the infection.",
     "In a child on chemotherapy, the fever is the emergency; the count only tells you how big.",
     "section 3, ‘Condition-specific crises’")]
)

# ------------------------------------------------------------------ UNIT 20
unit(20, "E", "Referral, transport, safeguarding, quality and future directions",
  "In a referral-dependent health system, the quality of the transfer decision often matters more than any single drug. The conversation with the parents is not the soft part of care &mdash; it is the part they will remember for the rest of their lives. And nothing in this module helps a child unless a system delivers it reliably at 3 a.m.",
  [("e", "Decide when to refer, stabilise before transfer, and hand over using ISBAR."),
   ("e", "Communicate serious news to a family, and support family presence during resuscitation."),
   ("e", "Recognise features of abuse and neglect and know the mandatory reporting duties under POCSO."),
   ("a", "Design a small quality-improvement project with outcome, process and balancing measures."),
   ("x", "Appraise emerging tools &mdash; machine-learning prediction, point-of-care ultrasound, host-response tests &mdash; for use in a low-resource setting.")],
  [
   sec(1, "Refer while the child is still compensating", '''
  <p>The commonest transport disaster is the child sent after decompensation, in an unequipped vehicle, without a stable airway, with staff who cannot manage deterioration on the way.</p>''' + algo("Before any transfer", '''  A  airway secure; if intubated, position confirmed and taped;
     suction in the vehicle
  B  oxygen for the journey PLUS 50% reserve; saturation monitored
  C  two working IV or IO lines, secured and visible
  D  glucose checked; seizures controlled; rescue drugs drawn up
  E  child WARM — cap, blankets, warm vehicle
  +  notes, drugs and times, weight, investigations
  +  ACCEPTANCE by a named person at the receiving unit, by phone
  +  parent informed and travelling if possible
  +  "what is most likely to go wrong in the next hour — and is the
     drug and equipment for it in the vehicle?"''') + '''
  <p><b>ISBAR handover:</b> Identify yourself and the child · Situation · Background · Assessment (with vital signs and weight) · Recommendation (what you need, by when).</p>''' + tracks(
     ["A paediatric retrieval team stabilises and transports with full monitoring and ventilation",
      "The referring doctor's job is early referral, stabilisation to the team's advice and complete documentation"],
     ["<b>You are the retrieval team.</b> The checklist is your work, finished before the vehicle leaves",
      "Phone and secure acceptance from a named person first; an unannounced child may be turned away, and a family may not survive a second journey financially",
      "Treat cost and transport as clinical variables. Ask whether the family can reach and afford the referral centre, and use 108/102 ambulance services and government scheme coverage (such as PM-JAY) where eligible",
      "Send oxygen and a trained escort if at all possible, with a written note that includes your phone number"])),

   sec(2, "Talking to families", '''
  <p><b>SPIKES</b> adapts well to paediatrics: <b>S</b>etting (private, seated, both parents if possible, an interpreter &mdash; never a sibling) · <b>P</b>erception (&ldquo;What have you been told so far?&rdquo;) · <b>I</b>nvitation (&ldquo;How much would you like me to explain?&rdquo;) · <b>K</b>nowledge (a warning shot, then plain words; say &ldquo;died&rdquo;; use the child's name) · <b>E</b>mpathy (stop talking; allow silence) · <b>S</b>ummary and strategy (what happens next, and when you will speak again).</p>''' + evidence('''<p>Offering parents the choice to be present during their child's resuscitation is supported by resuscitation guidelines and by evidence on bereavement: parents who were present generally report less anxiety and better-adjusted grief, and they rarely obstruct care. It needs a designated staff member to stay with them and explain.</p>''', "Family presence")),

   sec(3, "Safeguarding", '''
  <p>Features that should raise concern:</p>
  <ul>
    <li>A history that is absent, changing, inconsistent between carers, or impossible for the child's development &mdash; a 3-month-old who cannot roll did not roll off the bed.</li>
    <li>Unexplained delay in seeking care.</li>
    <li><b>Any bruise in a non-mobile infant</b>; bruises on the torso, ears or neck under 4 years; patterned bruises.</li>
    <li>Sharply demarcated, glove-and-stocking or cigarette-shaped burns.</li>
    <li>Rib fractures, metaphyseal fractures, fractures of different ages, retinal haemorrhages, unexplained intracranial injury.</li>
    <li>Neglect: faltering growth that recovers in hospital, untreated dental disease, missed immunisations.</li>
    <li>Fabricated or induced illness: symptoms seen only by one carer; findings that never match the reported severity.</li>
  </ul>''' + india('''<p>The <b>Protection of Children from Sexual Offences (POCSO) Act, 2012</b> makes it mandatory for anyone, including doctors, who knows of or suspects a sexual offence against a child to report it to the Special Juvenile Police Unit or local police; failure to report is itself an offence. Medical examination and treatment of a child survivor must not be refused or delayed. Beyond POCSO, report concerns about abuse or neglect to the District Child Protection Unit or Child Welfare Committee under the Juvenile Justice Act, and use <b>Childline 1098</b>. Know who your hospital's designated safeguarding person is before you need them.</p>''')),

   sec(4, "Quality improvement: closing the know&ndash;do gap", table(
     ["Element", "Example"],
     [["Aim", "&ldquo;Increase the proportion of children with suspected sepsis receiving antibiotics within 60 minutes of recognition from 35% to 80% within 6 months.&rdquo;"],
      ["Outcome measure", "Time from recognition to first antibiotic dose"],
      ["Process measures", "Documented triage category; recorded weight; time to IV or IO access"],
      ["Balancing measure", "Total antibiotic use &mdash; to detect over-treatment of children who were not septic"],
      ["Changes to test", "A sepsis grab-box; a weight-banded dose card; nurse-initiated antibiotic preparation; a run chart at the nursing station"]]) + '''
  <p>Improvements that reliably narrow the gap: pre-calculated weight-banded emergency drug charts; checklists for intubation, transfer and sepsis; in-situ simulation in the real clinical space; structured handover; and no-blame mortality review with documented actions. Report projects using SQUIRE 2.0.</p>''', tier="good", lvl="a"),

   sec(5, "Future directions", table(
     ["Direction", "Where it stands", "The honest caveat"],
     [["Machine-learning deterioration prediction", "Can outperform threshold scores in high-income hospitals with rich electronic records", "Mostly built on data that district hospitals do not collect; discrimination in a development set says nothing about whether outcomes improve &mdash; the EPOCH lesson again"],
      ["Sepsis sub-phenotypes", "Distinct biological endotypes are being identified", "The most plausible route out of guidelines built on low-certainty evidence &mdash; not yet at the bedside"],
      ["Point-of-care ultrasound", "Handheld probes are cheap; useful for lungs, volume and heart function", "Operator-dependent; needs training and governance or it produces confident errors"],
      ["Rapid diagnostics and host-response tests", "Could distinguish bacterial from viral illness and cut antibiotic use", "Cost and supply chain, not the technology, are the constraint"],
      ["Oxygen systems and pulse oximetry", "Measurable mortality impact in childhood pneumonia", "The highest-yield &ldquo;technology&rdquo; here, and the least discussed"]]) + pearl('''<p>Nothing in this module is hard to understand. Almost all of it is hard to do reliably at three in the morning, on the fortieth child of the shift, when the cylinder is empty and the family cannot afford the referral. That is the real clinical problem &mdash; and the reason systems matter as much as knowledge.</p>''', "The closing argument"), tier="nice", lvl="x"),
  ],
  [Q("A 3-month-old has a bruise on the left cheek. The parents say she rolled off a sofa. On examination she cannot yet roll over. What is the most appropriate action?",
     ["Reassure the parents; facial bruises are common at this age.",
      "Treat as a safeguarding concern: examine fully, document carefully, involve the senior and safeguarding lead, and look for hidden injuries.",
      "Discharge with advice about safer sleeping surfaces.",
      "Confront the parents and ask directly which of them hit the baby."],
     1,
     "Can a baby who cannot roll fall off a sofa by rolling?",
     "Any bruise in a non-mobile infant is a red flag, and here the history does not fit the child's development. What does that combination require?",
     "A bruise in a <b>non-mobile infant</b> with a history that <b>does not fit her development</b> is a safeguarding concern. Examine fully (including skin, fontanelle, eyes and mouth), document exactly, involve senior and safeguarding colleagues, and investigate for hidden injuries according to local protocol.",
     "<b>A</b> &mdash; bruises are rare in infants who cannot move independently. <b>C</b> &mdash; discharging without assessment could return the baby to harm. <b>D</b> &mdash; accusation is not your role; it damages the assessment and can put the child at greater risk.",
     "In a baby who cannot move, a bruise needs an explanation that fits. When it does not, protect the child first.",
     "section 3, ‘Safeguarding’"),
   Q("A CHC is transferring a 2-year-old with septic shock who has responded partly to fluid and antibiotics. The ambulance is ready. Which step is most important before the vehicle leaves?",
     ["Wait for the full laboratory results so they can go with the child.",
      "Complete the stabilisation checklist and phone the receiving unit to secure acceptance from a named doctor.",
      "Send the child quickly with a verbal message for the family to pass on.",
      "Remove the IV line so it does not fall out on the road."],
     1,
     "What can a child arriving unannounced at a full tertiary centre face?",
     "The two things that most often cause transfer disasters are an unstable child and an unexpected arrival. Which option prevents both?",
     "Finish the <b>stabilisation checklist</b> (airway, oxygen plus reserve, secured lines, glucose, warmth, documents) and <b>phone for acceptance by a named person</b>. An unannounced child may be turned away, and a second journey can be dangerous and unaffordable.",
     "<b>A</b> &mdash; waiting for results delays transfer while the child may decompensate; send them on later. <b>C</b> &mdash; verbal messages passed through a frightened family lose critical information. <b>D</b> &mdash; a child in septic shock needs secured access during transport, not less of it.",
     "The transfer starts with the phone call, not with the ambulance.",
     "section 1, ‘Refer while the child is still compensating’")]
)
