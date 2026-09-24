from gen import *

part("D", "Specific emergencies", "Units 12&ndash;15 · ~8 hours",
     "The ABCDE spine keeps a child alive; these four units tell you what to do once you know why the child is sick. They are chosen for India's burden: household poisons, seizures, snake and scorpion envenomation, and injury.")

# ------------------------------------------------------------------ UNIT 12
unit(12, "D", "Poisoning: toxidromes, decontamination, antidotes and India's common poisons",
  "Most poisoned children need good supportive care and nothing else. A few need one specific drug, fast. The skill is knowing which child is which &mdash; and knowing the handful of poisons in Indian homes that change the plan.",
  [("e", "Stabilise a poisoned child with the ABCDE approach, including glucose, before thinking about the poison."),
   ("e", "Recognise the four common toxidromes from bedside signs."),
   ("a", "Decide when activated charcoal helps and when it is contraindicated; know why emesis and routine lavage are not used."),
   ("a", "Manage organophosphate, hydrocarbon (kerosene), paracetamol, iron and button-battery ingestions."),
   ("x", "Recognise the poisons with no antidote and a high fatality rate &mdash; aluminium phosphide, paraquat, yellow phosphorus &mdash; and plan early referral.")],
  [
   sec(1, "Treat the child, then the poison", algo("The poisoned child", ''' 1. ABCDE        airway and breathing first — most deaths are
                 from respiratory depression or aspiration
 2. GLUCOSE      in every child with altered consciousness
 3. HISTORY      what · how much (worst-case estimate) · when ·
                 what else is in the house · what was given at home
                 · bring the container
 4. TOXIDROME    pupils · skin · secretions · heart rate · BP ·
                 temperature · bowel sounds · breath odour
 5. DECONTAMINATE only if it helps and is safe (section 3)
 6. ANTIDOTE     for the few that have one (section 4)
 7. OBSERVE      for the known time course of the poison
 8. PREVENT      safe storage counselling, before discharge''') + '''
  <p>Take the <b>worst-case</b> amount: the number of tablets missing from the strip, the full volume of the bottle. Children share, siblings hide things, and parents under-estimate.</p>'''),

   sec(2, "Toxidromes", table(
     ["Toxidrome", "Pupils", "Skin and secretions", "Other signs", "Typical agents"],
     [["<b>Cholinergic</b>", "Pinpoint", "Wet: sweating, salivation, tears, bronchorrhoea", "Bradycardia, wheeze, vomiting, diarrhoea, fasciculation, weakness", "Organophosphate and carbamate pesticides"],
      ["<b>Anticholinergic</b>", "Dilated", "Dry, hot, flushed", "Delirium, tachycardia, urinary retention, absent bowel sounds", "Datura (dhatura) seeds, antihistamines, tricyclics"],
      ["<b>Opioid</b>", "Pinpoint", "Normal", "Slow shallow breathing, coma", "Opioids, some antidiarrhoeals, poppy-husk preparations"],
      ["<b>Sympathomimetic</b>", "Dilated", "Sweaty", "Agitation, tachycardia, hypertension, hyperthermia, seizures", "Amphetamines, excess salbutamol or theophylline"]]) + pearl('''<p>Cholinergic and anticholinergic both change the pupils and the heart rate &mdash; <b>feel the skin</b>. Wet means cholinergic; dry means anticholinergic. The armpit is the quickest place to check.</p>''')),

   sec(3, "Decontamination: less than you were taught", table(
     ["Method", "Current position"],
     [["<b>Activated charcoal</b> 1 g/kg (max 50 g)", "Consider within about 1 hour of a potentially serious ingestion of a substance charcoal binds, <b>only if the airway is protected</b> (alert, or intubated). Not for hydrocarbons, corrosives, iron, alcohols or lithium."],
      ["<b>Induced vomiting</b>", "Not used. It delays charcoal, risks aspiration and does not improve outcome."],
      ["<b>Gastric lavage</b>", "Not routine. Rarely considered for a recent, life-threatening ingestion with no good alternative, with the airway protected. Never for hydrocarbons or corrosives."],
      ["<b>Whole-bowel irrigation</b>", "Specialist use: iron, sustained-release preparations, packets."],
      ["<b>Skin and eye</b>", "Remove clothing and wash skin with soap and water for organophosphates; irrigate eyes. Staff wear gloves."]]) + pitfall('''<p>Making a child vomit after kerosene or a corrosive. Vomiting turns a stomach problem into a lung problem (hydrocarbon aspiration pneumonitis) or burns the oesophagus a second time. Households are often advised to do this; ask, and counsel against it.</p>''')),

   sec(4, "Antidotes worth knowing", table(
     ["Poison", "Antidote", "Notes"],
     [["Organophosphate, carbamate", "<b>Atropine</b>", "Titrate to a clear chest and dry secretions (section 5)"],
      ["Opioid", "<b>Naloxone</b> 0.1 mg/kg IV/IO/IM (max 2 mg), repeat as needed", "Short-acting &mdash; watch for re-sedation; infusion may be needed"],
      ["Paracetamol", "<b>N-acetylcysteine</b>", "Best within 8 hours of ingestion; see section 6"],
      ["Iron", "<b>Desferrioxamine</b> IV", "For systemic toxicity or high levels"],
      ["Digoxin, oleander (cardiac glycosides)", "Digoxin-specific antibody fragments where available", "Otherwise atropine for bradycardia, manage potassium, pacing in specialist units"],
      ["Benzodiazepines", "Flumazenil &mdash; <b>rarely</b>", "Can precipitate seizures; not for undifferentiated coma"],
      ["Methaemoglobinaemia (nitrites, dapsone, some dyes)", "<b>Methylene blue</b>", "Avoid in G6PD deficiency"]]) + '''
  <p class="dash-status">Doses: see Appendix E and verify against your unit protocol. Your state or regional <b>poison information centre</b> can advise in real time &mdash; keep the number on the resuscitation trolley.</p>''', lvl="a"),

   sec(5, "Organophosphates and carbamates", '''
  <p>India's most important paediatric poisoning: pesticides stored in homes, in soft-drink bottles, or on clothing and skin after field work.</p>''' + algo("Atropinisation", '''  AIRWAY first · suction · oxygen · ventilate if weak
  DECONTAMINATE skin and clothing (staff wear gloves)
  ATROPINE  0.02–0.05 mg/kg IV, DOUBLE the dose every 5 minutes
            until ATROPINISED:
              clear chest on auscultation (no crackles, no wheeze)
              heart rate adequate for age
              adequate blood pressure · dry axillae
              pupils no longer pinpoint
  then an INFUSION of about 10–20% of the total loading dose per
  hour, titrated — watch for toxicity (delirium, fever, ileus,
  urinary retention) and for relapse
  SEIZURES → benzodiazepine''') + evidence('''<p>The endpoint is a <b>clear chest</b>, not pupil size and not heart rate alone: children die of bronchorrhoea and respiratory failure. Doses needed can be far larger than usual. <b>Pralidoxime</b> is used in many Indian units, but its benefit is uncertain &mdash; a large randomised trial in Sri Lanka (Eddleston et al., <i>PLoS Med</i> 2009) found no mortality benefit. Follow your local protocol; never let it delay atropine or ventilation. Watch for the <b>intermediate syndrome</b> &mdash; neck flexor and proximal weakness with respiratory failure 1&ndash;4 days later, after the cholinergic phase has settled.</p>''')),

   sec(6, "Kerosene, paracetamol, iron and button batteries", table(
     ["Poison", "Danger", "What to do"],
     [["<b>Kerosene and other hydrocarbons</b>", "Aspiration pneumonitis; fever and chest signs can appear hours later", "No emesis, no lavage, no charcoal. Oxygen. Observe at least 6 hours: a child who is symptom-free with normal oxygen saturation and chest examination at 6 hours can usually go home. Chest X-ray if symptomatic. Antibiotics and steroids are not routine."],
      ["<b>Paracetamol</b>", "Liver failure, often after a deceptively well first day", "Serious risk is generally considered above about 150 mg/kg in a single acute ingestion (thresholds vary by country). Measure a level at 4 hours or later and use the nomogram; start <b>N-acetylcysteine</b> without waiting for a level if it will not be available within 8 hours of ingestion, or if the ingestion is staggered or unclear."],
      ["<b>Iron</b>", "Vomiting, bloody diarrhoea, then apparent recovery, then shock, acidosis and liver failure", "Calculate elemental iron: over about 60 mg/kg is potentially serious. Abdominal X-ray may show tablets. Charcoal does not bind iron. Desferrioxamine for systemic toxicity; discuss with a poison centre."],
      ["<b>Button battery</b>", "Oesophageal burn within 2 hours; late fistula and catastrophic bleeding", "X-ray neck, chest and abdomen. A battery in the oesophagus is an emergency: endoscopic removal within hours. While awaiting removal, honey (children over 1 year) is used in some protocols to reduce injury &mdash; follow your local ENT or poison centre advice."]]), lvl="a"),

   sec(7, "The poisons with no antidote", danger('''<p><b>Aluminium or zinc phosphide</b> (rodenticide tablets; garlicky odour): refractory shock, arrhythmia, acidosis; very high fatality, no antidote. <b>Paraquat</b> (herbicide): mouth ulcers, then kidney, liver and progressive lung fibrosis; oxygen may worsen the lung injury. <b>Yellow phosphorus</b> (some rat poisons and firecrackers): delayed liver failure after a symptom-free interval. For all three: supportive care, early senior involvement and early referral to a centre with intensive care and, for yellow phosphorus, access to liver-transplant assessment. Take every such history seriously even when the child looks well.</p>''', "Recognise them, refer them early") + india('''<p>Paediatric poisoning in India is dominated by household products and farm chemicals: <b>kerosene</b> stored in drink bottles, <b>organophosphate and carbamate</b> pesticides, <b>rodenticides</b>, corrosives, <b>datura</b>, <b>oleander</b> seeds, iron tablets meant for a pregnant mother, and adult medicines. In adolescents, deliberate self-poisoning with pesticides and medicines is common: every adolescent poisoning needs a confidential, non-judgemental psychosocial assessment before discharge. Unregulated traditional preparations can contain lead or other heavy metals. The IAP Standard Treatment Guidelines include a chapter on poisoning in children.</p>'''), tier="good", lvl="a"),
  ],
  [Q("A 4-year-old is drowsy after playing where crops were recently sprayed. He has pinpoint pupils, copious oral secretions, crackles and wheeze, heart rate 64/min and muscle twitching. After airway support and oxygen, what is the priority?",
     ["Atropine IV, doubling the dose every five minutes until the chest is clear and secretions dry.",
      "Naloxone 0.1 mg/kg IV.",
      "Activated charcoal by nasogastric tube.",
      "Nebulised salbutamol for the wheeze."],
     0,
     "Wet skin, wet chest, small pupils, slow heart. Which toxidrome?",
     "In this toxidrome, what do children actually die of &mdash; and which drug dries it up? What is its endpoint?",
     "This is the <b>cholinergic toxidrome</b> from organophosphate or carbamate exposure. Children die of bronchorrhoea and respiratory failure, so the priority is <b>atropine, doubling every five minutes to a clear chest and dry secretions</b>. Decontaminate skin and clothing; staff wear gloves.",
     "<b>B</b> &mdash; naloxone reverses opioids; opioid toxicity does not cause secretions, fasciculation or wheeze. <b>C</b> &mdash; the exposure was probably through skin and inhalation, and a drowsy child with copious secretions has an unprotected airway. <b>D</b> &mdash; the wheeze is bronchorrhoea and bronchospasm from acetylcholine excess; salbutamol will not dry the chest.",
     "In organophosphate poisoning, listen to the chest to decide the next dose of atropine. The pupils will mislead you.",
     "section 5, ‘Organophosphates and carbamates’"),
   Q("A 2-year-old drank &ldquo;a mouthful&rdquo; of kerosene from a soft-drink bottle 30 minutes ago. He coughed and gagged at the time but is now playing, with a respiratory rate of 28/min, SpO₂ 98% in air and a clear chest. His mother has already made him vomit once at home. What is the best plan?",
     ["Gastric lavage now to remove the remaining kerosene.",
      "Activated charcoal 1 g/kg and discharge.",
      "Start IV antibiotics and steroids to prevent pneumonitis.",
      "No emesis, lavage or charcoal; observe for at least 6 hours, and advise the family about safe storage."],
     3,
     "Where does kerosene do its damage &mdash; the stomach or the lungs?",
     "Every option that puts more kerosene near the airway is wrong. Of the rest, which has a time course matched to how aspiration pneumonitis develops?",
     "Hydrocarbon toxicity is <b>aspiration pneumonitis</b>, which can appear hours later. Do not add risk: <b>no emesis, no lavage, no charcoal</b>. Observe for at least 6 hours; if he remains well with normal oxygen saturation and chest at 6 hours he can usually go home. Counsel the family on storage &mdash; and against inducing vomiting.",
     "<b>A</b> &mdash; lavage increases aspiration risk. <b>B</b> &mdash; charcoal does not bind hydrocarbons and provokes vomiting; discharge now misses the window in which pneumonitis appears. <b>C</b> &mdash; neither antibiotics nor steroids are routine; they do not prevent chemical pneumonitis.",
     "With kerosene, the cough at the time of drinking matters more than the volume drunk: it means some reached the airway.",
     "section 6, ‘Kerosene, paracetamol, iron and button batteries’")]
)

# ------------------------------------------------------------------ UNIT 13
unit(13, "D", "Status epilepticus and raised intracranial pressure",
  "Two neurological emergencies where the clock does the damage: a seizure that is not stopped becomes harder to stop with every minute, and a brain under pressure is injured by every minute of low blood pressure or low oxygen.",
  [("e", "Manage a convulsing child with a time-based algorithm, starting benzodiazepines at five minutes by whatever route is available."),
   ("e", "Recognise raised intracranial pressure and impending herniation at the bedside."),
   ("a", "Choose a second-line antiseizure medicine and give it at the correct dose, using the ESETT, EcLiPSE and ConSEPT evidence."),
   ("a", "Apply the neuroprotective measures that lower intracranial pressure or protect cerebral perfusion, and avoid the ones that harm."),
   ("x", "Recognise non-convulsive status and refractory status, and plan escalation.")],
  [
   sec(1, "Status epilepticus: the clock", fig("status", "Convulsive status epilepticus &mdash; time-based", '''0–5 min   ABC · recovery position · oxygen · suction
          GLUCOSE · IV/IO access · note the TIME · do not restrain
          treat hypoglycaemia: 10% glucose 5 mL/kg
5 min     FIRST BENZODIAZEPINE — by the route you have
          IV/IO: lorazepam 0.1 mg/kg (max 4 mg)
                 or diazepam 0.2–0.3 mg/kg (max 10 mg)
          No IV:  buccal or intranasal midazolam 0.3 mg/kg (max 10 mg)
                  or rectal diazepam 0.5 mg/kg (max 10–20 mg)
10 min    SECOND BENZODIAZEPINE if still seizing — ONE repeat only
~20 min   SECOND-LINE MEDICINE — choose ONE
          levetiracetam 40–60 mg/kg IV over 5–15 min (max 3–4.5 g)
          phenytoin 20 mg/kg IV over 20 min, with ECG monitoring
             (or fosphenytoin 20 mg PE/kg)
          valproate 40 mg/kg IV (max 3 g) — avoid in liver disease,
             suspected metabolic or mitochondrial disease, under 2 y
          phenobarbital 20 mg/kg IV — where others are unavailable
~40 min   REFRACTORY: senior and anaesthetic help · a second
          second-line agent, or anaesthetic induction and a
          midazolam infusion with intubation · EEG where available''') + danger('''<p><b>Two benzodiazepine doses is the ceiling.</b> A third and fourth dose do not stop the seizure; they stop the breathing. Move to a second-line agent. And nominate one person to call out the elapsed time aloud &mdash; without a clock, &ldquo;20 minutes&rdquo; becomes an hour.</p>''')),

   sec(2, "Choosing the second-line drug", evidence('''<p><b>ESETT</b> (Kapur et al., <i>NEJM</i> 2019; children and adults with benzodiazepine-refractory status): levetiracetam 60 mg/kg, fosphenytoin 20 mg PE/kg and valproate 40 mg/kg each stopped seizures in roughly half of patients, with no meaningful difference between them. <b>EcLiPSE</b> (UK) and <b>ConSEPT</b> (Australia and New Zealand), both <i>Lancet</i> 2019, compared levetiracetam 40 mg/kg with phenytoin 20 mg/kg in children: levetiracetam was not superior, but it is quicker to give, needs no cardiac monitoring and has fewer serious adverse effects. Choose by <b>availability, contraindications and infusion time</b>, not by efficacy.</p>''', "What the trials showed") + '''
  <p>A seizure that will not stop is a seizure with a cause you have not found. Check <b>glucose, sodium, calcium and magnesium</b>; think of meningitis and encephalitis, cerebral malaria, toxins, raised pressure, and non-accidental head injury in an infant. Hyponatraemic seizures respond to 3% saline, not to antiseizure drugs (Unit 7).</p>''', lvl="a"),

   sec(3, "Raised intracranial pressure", '''
  <p><b>Cerebral perfusion pressure = mean arterial pressure &minus; intracranial pressure.</b> Every intervention either lowers intracranial pressure or protects arterial pressure. Hypotension and hypoxia convert a survivable brain injury into a devastating one.</p>''' + table(
     ["Recognise", "Do", "Avoid"],
     [["Headache worse in the morning or lying down; vomiting; falling consciousness; unequal pupils; abnormal posturing; Cushing triad (high BP, slow pulse, irregular breathing &mdash; late); bulging fontanelle and &ldquo;setting sun&rdquo; eyes in infants",
       "Head up 30&deg;, neck midline · secure airway · normal oxygen (SpO₂ 94% or above) · normal CO₂ (PaCO₂ 35&ndash;40 mmHg) · maintain blood pressure · analgesia and sedation · <b>3% saline 3&ndash;5 mL/kg</b> or <b>mannitol 0.5&ndash;1 g/kg</b> for signs of herniation · treat fever, seizures and low sodium · urgent imaging and neurosurgery",
       "Lumbar puncture · prolonged hyperventilation (brief only, as a bridge for imminent herniation) · hypotonic fluids · steroids in traumatic brain injury · hypoglycaemia and hyperglycaemia"]]) + pearl('''<p>Steroids have a place for vasogenic oedema around tumours and in TB meningitis &mdash; not in traumatic brain injury, where they cause harm.</p>''')),

   sec(4, "Across settings", tracks(
     ["IV lorazepam, then levetiracetam, fosphenytoin or valproate by pump with ECG monitoring",
      "Refractory status: intubation, midazolam or thiopental infusion, continuous EEG",
      "ICP monitoring and neurosurgery available; CT or MRI within the hour"],
     ["No IV is not an obstacle: <b>buccal or intranasal midazolam</b> and rectal diazepam need no cannula and can be given by a nurse or trained parent",
      "The two-dose benzodiazepine ceiling matters more here &mdash; you may have no means of supporting respiratory arrest",
      "Phenobarbital and phenytoin are often the available second-line drugs; give phenytoin slowly, counting the pulse, even without a cardiac monitor",
      "Without EEG, prolonged unexplained unresponsiveness after a seizure should be assumed to be ongoing seizure activity and discussed with a senior",
      "Glucose, sodium, calcium, and assessment for meningitis, cerebral malaria and scrub typhus explain more refractory seizures here than imaging would"]) + india('''<p><b>Neurocysticercosis</b> is a leading cause of acquired epilepsy and of first seizures in Indian children, and <b>Japanese encephalitis</b> and cerebral malaria remain important in endemic districts. Train families of children with epilepsy to use buccal or intranasal midazolam at home; it shortens seizures before the child reaches hospital.</p>''')),
  ],
  [Q("A 3-year-old has been convulsing for 12 minutes and has had two doses of IV midazolam. The seizure continues. Glucose is 5.4 mmol/L and sodium 138 mmol/L. What next?",
     ["A third dose of midazolam.",
      "Immediate CT head before any further drug.",
      "A second-line medicine &mdash; levetiracetam, phenytoin or valproate &mdash; while preparing airway support.",
      "Rectal paracetamol and observation, as this is probably a febrile seizure."],
     2,
     "How many benzodiazepine doses is the ceiling?",
     "He has had two. The glucose and sodium are normal. The trials compared three drugs for exactly this situation &mdash; which step is that?",
     "Two benzodiazepine doses is the ceiling. Move to a <b>second-line medicine</b>. ESETT, EcLiPSE and ConSEPT found levetiracetam, phenytoin (or fosphenytoin) and valproate broadly similar in effect, so choose by availability, contraindications and speed of administration, and prepare for airway support.",
     "<b>A</b> &mdash; a third dose adds respiratory depression, not efficacy. <b>B</b> &mdash; imaging may be needed, but it must not delay stopping the seizure. <b>D</b> &mdash; any seizure lasting over 5 minutes is status epilepticus and is treated as such, fever or not.",
     "The second-line drug you can give fastest is usually the best one.",
     "section 1, ‘Status epilepticus: the clock’, and section 2"),
   Q("A 7-year-old with a head injury from a fall has GCS 7, a dilated left pupil and BP 70/40 mmHg. She is intubated. Which combination best protects her brain in the next 15 minutes?",
     ["Aggressive hyperventilation to a PaCO₂ of 25 mmHg and fluid restriction.",
      "Restore blood pressure with fluid or a vasoactive, keep oxygen and CO₂ normal, head up with neck midline, and give 3% saline for the dilated pupil &mdash; with urgent neurosurgery.",
      "High-dose dexamethasone and hypotonic fluids.",
      "Lumbar puncture to measure the opening pressure."],
     1,
     "Cerebral perfusion pressure = MAP minus ICP. Which of her numbers is making that worse right now?",
     "She is hypotensive and has signs of herniation. You need to raise one side of the equation and lower the other. Which option does both, without adding harm?",
     "Her brain is threatened by both <b>low blood pressure</b> and <b>raised pressure</b>. Restore MAP, keep oxygen and CO₂ normal, position head-up with the neck midline, give <b>3% saline</b> for the herniation signs, and get neurosurgical help. Hypotension and hypoxia are what turn survivable brain injury into devastating injury.",
     "<b>A</b> &mdash; prolonged hyperventilation causes cerebral ischaemia, and fluid restriction worsens her hypotension. <b>C</b> &mdash; steroids harm in traumatic brain injury, and hypotonic fluid worsens cerebral oedema. <b>D</b> &mdash; LP with raised pressure can precipitate herniation.",
     "In head injury, the first neuroprotective drug is whatever restores the blood pressure.",
     "section 3, ‘Raised intracranial pressure’")]
)

# ------------------------------------------------------------------ UNIT 14
unit(14, "D", "Envenomation: snakes and scorpions",
  "India carries the world's largest burden of snakebite deaths, most of them rural, many of them children, and many preventable by one decision taken early: give antivenom, and be ready to ventilate.",
  [("e", "Give correct first aid for snakebite, and name the traditional practices that cause harm."),
   ("e", "Recognise neurotoxic and haemotoxic envenomation, including the painless night-time krait bite."),
   ("a", "Give polyvalent anti-snake venom at the national-protocol dose, repeat it by the 20-minute whole blood clotting test, and manage reactions."),
   ("a", "Recognise the autonomic storm of scorpion envenomation and treat it with prazosin, with or without antivenom.")],
  [
   sec(1, "Snakebite: first aid that works", '''
  <ul>
    <li><b>Reassure</b>, keep the child still, and immobilise the bitten limb like a fracture.</li>
    <li><b>Transport immediately</b> to a facility that has anti-snake venom (ASV) &mdash; by the quickest safe means.</li>
    <li><b>Remove</b> rings, anklets and tight clothing before swelling starts.</li>
  </ul>''' + danger('''<p><b>Do not</b> apply a tight tourniquet, cut or suck the wound, apply ice or chemicals, use &ldquo;snake stones&rdquo;, or delay transport for a traditional healer. These practices cause limb loss and death, and delayed ASV is the commonest avoidable factor in snakebite deaths.</p>''', "Harmful practices")),

   sec(2, "Recognise the syndrome", table(
     ["Syndrome", "Species (India's &ldquo;big four&rdquo;)", "Features"],
     [["<b>Neurotoxic</b>", "Cobra, common krait", "Ptosis (earliest), double vision, difficulty swallowing and speaking, neck weakness, then respiratory paralysis. <b>Krait bites are often painless, happen at night during sleep, and leave no visible mark</b>: a child who wakes with abdominal pain and vomiting and develops ptosis in an endemic area is a krait bite until proven otherwise."],
      ["<b>Haemotoxic (vasculotoxic)</b>", "Russell's viper, saw-scaled viper", "Local swelling and blistering, bleeding from gums or bite site, incoagulable blood, acute kidney injury, shock"]]) + pearl('''<p><b>20-minute whole blood clotting test (20WBCT).</b> Put 2 mL of fresh venous blood in a new, clean, dry glass tube; leave it undisturbed for 20 minutes; tip it once. If the blood has not clotted, it is incoagulable &mdash; a haemotoxic bite &mdash; and ASV is indicated. Repeat every 6 hours to guide further doses.</p>''')),

   sec(3, "Anti-snake venom: national protocol", algo("ASV (Indian national snakebite protocol)", '''  INDICATIONS: any sign of systemic envenomation
     (neurotoxic signs · incoagulable 20WBCT · spontaneous bleeding ·
      shock · kidney injury) or rapidly progressive local swelling
  CHILDREN RECEIVE THE SAME NUMBER OF VIALS AS ADULTS
     (the snake injects the same amount of venom);
     only the infusion volume is adjusted — about 5–10 mL/kg
  NEUROTOXIC:  10 vials over 30 minutes as an infusion
               if no improvement after 1 hour → a second 10 vials
               (maximum 20 vials) · then VENTILATE if needed
  HAEMOTOXIC:  10 vials over 30 minutes (6 for saw-scaled viper
               in the low-dose regimen), then repeat by 20WBCT
               every 6 hours until the blood clots, per the
               protocol followed in your state
  REACTIONS:   stop the infusion · IM adrenaline 0.01 mg/kg
               (max 0.5 mg) · restart cautiously when settled
  NEUROTOXIC ADJUNCT: atropine then neostigmine trial
               (national STG: atropine 0.05 mg/kg, then neostigmine
               0.04 mg/kg; repeat neostigmine if there is a response)''') + evidence('''<p>Source: Ministry of Health and Family Welfare Standard Treatment Guidelines, <i>Management of Snakebite</i> (quick reference guide). Polyvalent ASV in India covers the big four only; bites from other species, such as the hump-nosed pit viper, are not neutralised by it. The neostigmine trial helps mainly in cobra (post-synaptic) envenomation; krait toxins act pre-synaptically and respond poorly &mdash; for krait, <b>ventilation is the life-saving treatment</b> and may be needed for days. Check the dose schedule used in your state before quoting it.</p>''', "Source and limits"), lvl="a"),

   sec(4, "Across settings", tracks(
     ["ASV, adrenaline and a ventilator in the same building",
      "Laboratory coagulation tests, creatinine and urine output monitoring",
      "Dialysis for acute kidney injury after viper bites"],
     ["The PHC or CHC with ASV <b>should give it</b>, not refer first: the first dose is the most important one",
      "20WBCT needs only a clean glass tube and a clock",
      "Bag-mask ventilation by relays of staff and family has kept krait-bitten children alive during transfer",
      "Refer early for ventilation (neurotoxic) and dialysis (haemotoxic with falling urine output) &mdash; after the first ASV dose, with adrenaline drawn up for the journey"])),

   sec(5, "Scorpion sting", '''
  <p>The Indian red scorpion (<i>Mesobuthus tamulus</i>), common in western and southern India, causes an <b>autonomic storm</b>: severe local pain, then sweating, salivation, vomiting, priapism, cold limbs, hypertension and tachycardia, progressing in some children to <b>myocardial dysfunction, pulmonary oedema and shock</b>. Children are more severely affected than adults.</p>''' + table(
     ["Treatment", "Detail"],
     [["<b>Prazosin</b> (the specific treatment)", "30 microgram/kg by mouth (or nasogastric tube), repeated at intervals according to response &mdash; commonly 3&ndash;6-hourly &mdash; until the peripheries are warm and signs of the storm settle. Watch for first-dose hypotension."],
      ["<b>Scorpion antivenom</b>", "In a randomised trial in Indian children (Pandi et al., 2014), scorpion antivenom plus prazosin produced faster recovery than prazosin alone. Give early where available."],
      ["<b>Dobutamine</b>", "For the low-output, hypotensive phase and pulmonary oedema, with oxygen, CPAP or ventilation"],
      ["Avoid", "Atropine for the parasympathetic signs, and nifedipine or other drugs that cause reflex tachycardia"]]) + india('''<p>The prazosin protocol was developed and popularised by Dr H.S. Bawaskar in rural Maharashtra and cut scorpion-sting mortality dramatically at low cost. It is one of the clearest examples of an Indian clinical innovation designed for resource-constrained care.</p>'''), lvl="a"),
  ],
  [Q("A 7-year-old in rural Maharashtra is brought at 3 a.m. having woken with severe abdominal pain and vomiting. There is no visible bite. Over the next hour he develops ptosis and difficulty swallowing. What is the most appropriate action?",
     ["Wait for the snake to be identified before giving antivenom.",
      "Treat as neurotoxic (probably krait) envenomation: give 10 vials of ASV, prepare for ventilation, and consider an atropine&ndash;neostigmine trial.",
      "Give ASV at a reduced paediatric dose calculated by weight.",
      "Treat as an acute abdomen and arrange surgical review."],
     1,
     "What kind of snakebite is painless, happens at night and leaves no mark?",
     "Progressive ptosis and swallowing difficulty after night-time abdominal pain in an endemic area. Is the ASV dose for a child smaller than for an adult?",
     "This is the classic <b>krait</b> presentation. Give <b>ASV at the full dose</b> (10 vials; children receive the same number of vials as adults) and <b>prepare to ventilate</b> &mdash; unrecognised respiratory paralysis is the commonest cause of death. A neostigmine trial is reasonable but works less well in krait bites.",
     "<b>A</b> &mdash; most snakes are never seen; treatment follows the syndrome. <b>C</b> &mdash; the venom dose is the same whatever the size of the child, so the antivenom dose is too. <b>D</b> &mdash; abdominal pain with progressive ptosis is neurotoxic envenomation, not a surgical abdomen.",
     "Ptosis in a child who woke in pain at night: think krait, give ASV, and have a bag-mask in your hand.",
     "section 2, ‘Recognise the syndrome’, and section 3"),
   Q("A 5-year-old stung by a scorpion two hours ago is sweating profusely, has cold extremities, priapism, heart rate 160/min and BP 140/95 mmHg. Crackles are beginning at both bases. What is the specific treatment?",
     ["Atropine to reduce the sweating and salivation.",
      "Nifedipine to lower the blood pressure.",
      "Prazosin 30 microgram/kg, with scorpion antivenom where available, oxygen and respiratory support as needed.",
      "Local anaesthetic infiltration alone and observation."],
     2,
     "What is driving the cold limbs, high blood pressure and pulmonary oedema &mdash; too much of which part of the autonomic system?",
     "The storm is a massive alpha-adrenergic surge. Which drug blocks that receptor without causing reflex tachycardia?",
     "This is the <b>autonomic storm</b> of Indian red scorpion envenomation, with early pulmonary oedema. <b>Prazosin</b>, an alpha-1 blocker, is the specific treatment; adding <b>scorpion antivenom</b> gives faster recovery. Give oxygen and CPAP or ventilation for the pulmonary oedema, and dobutamine if output falls.",
     "<b>A</b> &mdash; atropine worsens the tachycardia and hypertension and is not recommended. <b>B</b> &mdash; nifedipine causes reflex tachycardia and increases myocardial oxygen demand in an already stressed heart. <b>D</b> &mdash; local pain relief is fine for a local sting, but this child has systemic envenomation.",
     "In scorpion stings, cold hands and priapism are the signs to act on &mdash; not the pain.",
     "section 5, ‘Scorpion sting’")]
)

# ------------------------------------------------------------------ UNIT 15
unit(15, "D", "Trauma, burns and drowning",
  "Injury is now a leading cause of death in Indian children beyond infancy, and it is the area where rehearsed teamwork and a few paediatric-specific facts make the most visible difference.",
  [("e", "Conduct a paediatric primary survey (&lt;C&gt;ABCDE) and identify immediately life-threatening injuries."),
   ("e", "Estimate burn surface area in a child and calculate initial burn fluid, including maintenance."),
   ("e", "Give correct first aid for burns and start resuscitation after drowning."),
   ("a", "Apply paediatric injury patterns and decision rules to avoid both missed injury and unnecessary CT."),
   ("x", "Apply paediatric principles of haemorrhage control and blood-product resuscitation.")],
  [
   sec(1, "The paediatric primary survey", algo("<C>ABCDE", ''' <C> CATASTROPHIC HAEMORRHAGE — direct pressure, tourniquet,
     pelvic binder. Blood volume is only ~70–80 mL/kg.
  A  airway with manual in-line stabilisation · jaw thrust, not head
     tilt · collars fit children badly: manual stabilisation, blocks
     and tape are often safer than a struggling child in a collar
  B  the immediately lethal chest injuries: tension pneumothorax ·
     open pneumothorax · massive haemothorax · flail chest ·
     tamponade · airway disruption. Compliant ribs mean serious lung
     contusion WITHOUT rib fractures.
  C  two IV or IO lines · cross-match · treat hypotension as major
     haemorrhage · blood products EARLY; avoid large crystalloid
     volumes (10 mL/kg aliquots while blood is obtained)
  D  AVPU/GCS · pupils · glucose — head injury is the commonest
     cause of paediatric trauma death
  E  log-roll · full survey · then WARM the child (hypothermia,
     acidosis and coagulopathy feed each other)
  ADJUNCTS  analgesia (children are under-treated) · gastric tube ·
            tetanus · and bring the parents in early''') + table(
     ["Paediatric difference", "Consequence"],
     [["Large head, weak neck", "Head injury dominates; high cervical injuries (C1&ndash;C3); spinal cord injury without X-ray abnormality occurs"],
      ["Compliant chest", "Contusion without fractures; tension pneumothorax develops fast. A rib fracture means major force &mdash; or abuse."],
      ["Relatively large, less protected liver and spleen", "Solid-organ injury common; most managed without surgery in a monitored setting. Bicycle handlebars injure duodenum and pancreas."],
      ["Growth plates", "A &ldquo;sprain&rdquo; in a child is often a growth-plate fracture"]])),

   sec(2, "Head injury: who needs a CT?", '''
  <p>Validated decision rules (PECARN, CATCH, CHALICE) identify children at very low risk of clinically important brain injury who can be observed rather than scanned. PECARN, the most widely validated, separates children under and over two years; features such as altered mental status, a palpable skull fracture or signs of basal skull fracture put a child in the high-risk group for CT. Use a rule, record which one, and observe children in the intermediate group with a clear plan for re-examination.</p>''' + pearl('''<p>A decision rule protects children from unnecessary radiation <i>and</i> from a missed bleed. Its value is consistency, not the particular cut-offs &mdash; pick one rule for your department and use it every time.</p>'''), tier="good", lvl="a"),

   sec(3, "Burns", '''
  <ul>
    <li><b>First aid that works:</b> cool running tap water for 20 minutes (useful up to 3 hours after the burn), remove clothing and jewellery, cover with cling film, keep the child warm. <b>Not</b> ice, toothpaste, ink, oil, turmeric or ghee.</li>
    <li><b>Surface area:</b> the adult &ldquo;rule of nines&rdquo; is wrong for children &mdash; the head is proportionally larger and the legs smaller. Use a Lund&ndash;Browder chart, or the child's own palm with fingers as about 1% for scattered burns. Do not count simple erythema.</li>
    <li><b>Airway:</b> facial burns, singed nasal hair, soot in the mouth, hoarseness or stridor mean the airway will swell. Involve the most experienced airway operator early; waiting can make intubation impossible.</li>
  </ul>''' + algo("Burn fluid in children (Parkland-type)", '''  Children with burns over about 10% TBSA need IV fluid.
  RESUSCITATION  3–4 mL × weight (kg) × %TBSA of Ringer's lactate
                 over 24 hours FROM THE TIME OF THE BURN:
                 half in the first 8 hours, half over the next 16
  PLUS MAINTENANCE with glucose (children, unlike adults, need it —
                 small glycogen stores)
  TITRATE to urine output about 1 mL/kg/h (0.5 mL/kg/h in
                 adolescents) — the formula is a starting point only''') + pitfall('''<p>Two classic arithmetic errors: starting the 8-hour clock at arrival instead of at the time of the burn, and forgetting maintenance fluid in a child. Over-resuscitation (&ldquo;fluid creep&rdquo;) is also common: titrate down when urine output is good. Consider inflicted injury when the pattern does not fit the story &mdash; sharply demarcated immersion burns, symmetrical burns of both feet or buttocks, cigarette-sized burns (Unit 20).</p>''')),

   sec(4, "Drowning", '''
  <p>The primary insult is <b>hypoxia</b>. Start resuscitation with <b>five rescue breaths</b>, then compressions if there are no signs of life. There is no meaningful difference between fresh and salt water for initial management, and abdominal thrusts to &ldquo;remove water&rdquo; are harmful. Children rescued from cold water may survive prolonged submersion: continue resuscitation until the child is warmed and senior assessment is made. Every child who needed rescue breaths, or who has cough, breathlessness or low saturation, needs admission and observation for at least several hours &mdash; lung injury can worsen late.</p>''' + india('''<p>Drowning is one of the leading causes of death in Indian children aged 1&ndash;4 years, largely in open wells, ponds, tanks and buckets within metres of home, and in floods. Community measures &mdash; well covers, supervised crèches, barriers &mdash; prevent more deaths than hospital care can. Road traffic injury (often unhelmeted children on two-wheelers), falls, firecracker and cooking burns, and electrocution complete the picture.</p>''')),

   sec(5, "Haemorrhage in children", '''
  <p>Hypotension in an injured child suggests the loss of a large fraction of circulating volume. Give <b>blood early</b> &mdash; red cells and plasma, with platelets in massive transfusion &mdash; rather than repeated crystalloid, which dilutes clotting factors and worsens acidosis. Tranexamic acid is used in significant paediatric trauma haemorrhage in many trauma systems when given early; follow your trauma protocol. Keep the child warm, calcium replaced, and the time to haemorrhage control short.</p>''', tier="nice", lvl="x"),
  ],
  [Q("A 6-year-old weighing 20 kg has 25% TBSA scalds from 1 hour ago. Using 4 mL/kg/%TBSA, how much Ringer's lactate is needed over the rest of the first 8 hours from the burn, and what else must be prescribed?",
     ["2000 mL over the next 7 hours, with no extra maintenance.",
      "1000 mL over the next 8 hours, with no extra maintenance.",
      "500 mL over 8 hours, plus maintenance.",
      "1000 mL over the next 7 hours, plus separate maintenance fluid containing glucose."],
     3,
     "Work out the 24-hour total first. What fraction is due by hour 8, counted from when?",
     "4 &times; 20 &times; 25 = 2000 mL in 24 hours. Half is due in the first 8 hours from the time of the burn &mdash; and one hour has already passed. Then ask what children need that adults do not.",
     "The 24-hour total is 4 &times; 20 &times; 25 = <b>2000 mL</b>. Half, <b>1000 mL</b>, is due within 8 hours of the burn; one hour has passed, so it runs over the <b>remaining 7 hours</b>. Children also need <b>maintenance fluid with glucose</b> because of small glycogen stores. Titrate to urine output of about 1 mL/kg/h.",
     "<b>A</b> &mdash; that is the whole 24-hour volume squeezed into 7 hours. <b>B</b> &mdash; starts the clock at arrival and omits maintenance. <b>C</b> &mdash; halves the calculation incorrectly.",
     "The formula starts at the burn, not at the door, and in children it never stands alone.",
     "section 3, ‘Burns’"),
   Q("A 3-year-old is pulled from a village pond after an unknown time underwater. She is not breathing and has no signs of life. What is the correct first action?",
     ["Five rescue breaths, then start chest compressions and continue CPR.",
      "Abdominal thrusts to expel water from the lungs.",
      "Chest compressions only, since it is a cardiac arrest.",
      "Place her in the recovery position and wait for an ambulance."],
     0,
     "What is the primary insult in drowning?",
     "Drowning arrest is asphyxial. Which option treats hypoxia first, and which one wastes time or causes harm?",
     "In drowning the primary insult is <b>hypoxia</b>, so resuscitation begins with <b>five rescue breaths</b> and then compressions if there are no signs of life. Continue CPR, and continue longer if she is cold.",
     "<b>B</b> &mdash; abdominal thrusts do not remove meaningful water and cause vomiting and aspiration. <b>C</b> &mdash; compression-only CPR omits the treatment for the cause. <b>D</b> &mdash; a child with no signs of life needs CPR now; waiting guarantees death.",
     "In a child, the arrest is almost always about oxygen. Drowning is the purest example.",
     "section 4, ‘Drowning’")]
)
