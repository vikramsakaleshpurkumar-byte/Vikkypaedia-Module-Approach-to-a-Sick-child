from gen import *

part("B", "The systematic approach: ABCDE", "Units 4&ndash;7 · ~9 hours",
     "Airway before breathing, breathing before circulation &mdash; not because the later letters matter less, but because failure at each step makes the next impossible to fix. Part B builds the spine that every emergency in Parts C and D hangs on.")

# ------------------------------------------------------------------ UNIT 4
unit(4, "B", "Airway and breathing",
  "A child with a patent airway and adequate oxygenation has time. Almost everything else in paediatric resuscitation is buying that time back.",
  [("e", "Open and maintain a child's airway with positioning, suction and simple adjuncts, and deliver effective bag-mask ventilation."),
   ("e", "Classify a breathing problem into one of four patterns and name the first action for each."),
   ("e", "Distinguish respiratory distress from respiratory failure, and act on the difference."),
   ("a", "Choose an oxygen delivery device and a saturation target, and escalate through high-flow, CPAP and ventilation by mechanism."),
   ("x", "Plan a safe paediatric intubation for a shocked or acidotic child, including the physiology that makes induction dangerous.")],
  [
   sec(1, "Four patterns of respiratory illness", '''
  <p>Classify the pattern before you name the disease. The pattern dictates the first action, often before you know the diagnosis.</p>''' + table(
     ["Pattern", "Hallmarks", "Typical causes", "First priority"],
     [["<b>Upper-airway obstruction</b>", "Inspiratory stridor, hoarse or muffled voice, drooling, tripod or sniffing posture", "Croup, foreign body, retropharyngeal abscess, anaphylaxis, epiglottitis, inhalational burn", "Do not upset the child. Position of comfort, oxygen as tolerated, airway help. Nebulised adrenaline for severe croup; IM adrenaline for anaphylaxis."],
      ["<b>Lower-airway obstruction</b>", "Expiratory wheeze, prolonged expiration, hyperinflation", "Asthma, bronchiolitis, aspiration, lower foreign body", "Oxygen; bronchodilators and steroids for asthma; supportive care for bronchiolitis"],
      ["<b>Lung tissue disease</b>", "Grunting, crackles, focal signs, hypoxaemia out of proportion to effort", "Pneumonia, paediatric ARDS, pulmonary oedema, drowning", "Oxygen, then distending pressure (CPAP/PEEP); treat the cause"],
      ["<b>Disordered control of breathing</b>", "Irregular, shallow or apnoeic breathing, or unusually deep breathing, with effort that does not match the physiology", "Raised intracranial pressure, poisoning, post-ictal state, metabolic acidosis (deep Kussmaul breathing), neuromuscular disease", "Support ventilation and treat the brain or metabolic cause. Oxygen alone is not enough."]]) + pearl('''<p><b>Grunting</b> is expiration against a partly closed glottis: the child is making their own PEEP to keep collapsing alveoli open. It means significant lung disease &mdash; or, in a young infant, sepsis, pain or acidosis. Never dismiss a grunting child.</p>''')),

   sec(2, "Distress or failure", table(
     ["", "Respiratory distress", "Respiratory failure"],
     [["Appearance", "Alert, anxious, interactive", "Agitated, then drowsy, then unresponsive"],
      ["Effort", "Increased and sustained", "Increased then falling &mdash; or inadequate from the start"],
      ["Rate", "Fast", "Very fast, or slowing, irregular, apnoeic"],
      ["Oxygenation", "Maintained on modest oxygen", "Hypoxaemia despite oxygen; cyanosis"],
      ["Action", "Oxygen, treat the cause, watch closely", "<b>Assist ventilation now</b> &mdash; bag-mask, then an advanced airway"]]) + '''
  <p>The transition from distress to failure is the tiring child of Unit 3. The two signs that mark it are a <b>falling level of consciousness</b> and a <b>falling respiratory rate without clinical improvement</b>.</p>'''),

   sec(3, "Opening and supporting the airway", algo("The stepwise airway", ''' 1. POSITION    infant: neutral, small shoulder roll · child: sniffing
                trauma: jaw thrust with manual in-line stabilisation
 2. CLEAR       gentle suction under direct vision · no blind finger sweep
 3. ADJUNCT     oropharyngeal airway if unconscious with no gag
                (size: incisors to angle of jaw; insert the right way up
                 in young children, with a tongue depressor)
                nasopharyngeal airway if a gag is present and no base-of-
                skull injury is suspected
 4. VENTILATE   bag-mask with reservoir and high-flow oxygen
                E-C grip · watch the CHEST rise, not the bag
                respiratory arrest with a pulse: 1 breath every 2–3 s
 5. DECOMPRESS  gastric tube · a full stomach splints the diaphragm
 6. ESCALATE    supraglottic airway or tracheal tube by a competent
                operator · confirm with waveform capnography''') + evidence('''<p>Current AHA/AAP paediatric guidance: ventilate infants and children in respiratory arrest with a pulse, or during CPR with an advanced airway, at <b>one breath every 2&ndash;3 seconds (20&ndash;30/min)</b>; cuffed tracheal tubes are acceptable in infants and children, with cuff pressure monitored; routine cricoid pressure during intubation is not recommended. Cardiac arrest management itself is covered in the Vikkypaedia PALS module.</p>''', "What current resuscitation guidance says")),

   sec(4, "Oxygen: how much, how delivered", table(
     ["Device", "Approximate FiO₂", "Use it for"],
     [["Nasal prongs (0.5&ndash;1 L/min infant; 1&ndash;2 L/min child)", "0.3&ndash;0.4", "Mild hypoxaemia in a child who is feeding"],
      ["Simple face mask (&ge;5 L/min, to prevent rebreathing)", "0.35&ndash;0.6", "Moderate distress"],
      ["Non-rebreathing mask with reservoir (10&ndash;15 L/min)", "0.6&ndash;0.9", "Severe hypoxaemia, shock, resuscitation"],
      ["High-flow nasal cannula (about 1&ndash;2 L/kg/min)", "Titratable to 1.0", "Bronchiolitis, pneumonia &mdash; dead-space washout and modest distending pressure"],
      ["Bubble CPAP or CPAP/NIV", "Titratable", "Alveolar collapse, severe pneumonia or bronchiolitis in infants"],
      ["Bag-mask, with or without a tracheal tube", "Up to 1.0", "Respiratory failure, apnoea, arrest"]]) + '''
  <p><b>When to give oxygen.</b> WHO recommends oxygen for children with emergency signs, and for any child with SpO₂ below 90%. In acutely unwell children most services target SpO₂ of 92&ndash;94% or above; aim higher during active resuscitation, and accept lower individualised targets in cyanotic heart disease. Wean deliberately, and never leave a child on high-flow oxygen without monitoring.</p>
  ''' + india('''<p>The commonest failure is supply, not prescription: an empty cylinder, no flow-splitter, no paediatric masks or prongs, no working pulse oximeter. WHO's 2016 ETAT update addressed oxygen flow rates and humidification for exactly this reason, and India's post-2021 investment in PSA oxygen plants changed what many district hospitals can deliver. Auditing &ldquo;was oxygen available and correctly delivered?&rdquo; is often a higher-yield improvement project than any protocol change.</p>''')),

   sec(5, "Supporting the failing airway, across settings", tracks(
     ["Piped, blended oxygen; continuous pulse oximetry and waveform capnography on every supported child",
      "Stepwise escalation: prongs, then high-flow, then CPAP or NIV, then intubation and lung-protective ventilation",
      "A blood gas guides the decision; a video laryngoscope and an anaesthetist are minutes away",
      "The decision to intubate is made early and electively, before exhaustion"],
     ["Oxygen is the intervention. A concentrator or cylinder, a flow-splitter, a pulse oximeter and correctly sized interfaces &mdash; check they exist before the next sick child arrives",
      "Position of comfort on a parent's lap does much of what equipment does",
      "Bubble CPAP, run by trained staff, is an evidence-supported option for infants with severe pneumonia or bronchiolitis where ventilation is unavailable",
      "If you cannot ventilate beyond bag-mask, the decision is <b>when to transfer</b>, not whether to intubate. Make it while the child is still compensating (Unit 20)",
      "Bag-mask ventilation done well is a legitimate destination, not a failure. Intubating a child you then cannot ventilate or monitor can turn a survivable illness into an arrest"])),

   sec(6, "Intubating the sick child safely", '''
  <p>Choose support by mechanism. <b>High-flow</b> helps where dead-space washout and mild distending pressure are enough. <b>CPAP</b> treats alveolar or upper-airway collapse. <b>NIV</b> helps inadequate tidal ventilation with rising CO₂. <b>Intubation</b> is for airway protection, refractory hypoxaemia or hypercapnia, exhaustion, shock unresponsive to resuscitation, and safe transfer.</p>''' + danger('''<p><b>A shocked or acidotic child can arrest at induction.</b> Loss of sympathetic drive, positive-pressure ventilation reducing venous return, and apnoea worsening acidosis all arrive at the same moment. <b>Resuscitate before you intubate</b> where you possibly can: correct volume, start a vasoactive if needed, choose a haemodynamically gentler induction agent, have a push-dose vasopressor drawn up, and pre-oxygenate.</p>''', "Physiological difficulty") + '''
  <ul>
    <li><b>Tube size:</b> cuffed, (age/4) + 3.5 mm; uncuffed, (age/4) + 4 mm. Depth at the lips is roughly three times the internal diameter.</li>
    <li><b>Confirm</b> with waveform capnography plus chest rise and auscultation; secure; X-ray.</li>
    <li><b>DOPES</b> for sudden deterioration in a ventilated child: Displacement · Obstruction · Pneumothorax · Equipment failure · Stomach distension.</li>
  </ul>''', tier="good", lvl="x"),
  ],
  [Q("A 2-year-old starts coughing and has noisy breathing while eating peanuts. She is distressed but coughing forcefully and able to cry and speak. What is the best immediate action?",
     ["Five back blows followed by five chest thrusts now.",
      "A blind finger sweep of the mouth to remove the peanut.",
      "Rapid sequence intubation before the airway closes.",
      "Encourage her to keep coughing, keep her calm and upright, and prepare for deterioration while arranging bronchoscopy."],
     3,
     "What can a forceful cough do that no manoeuvre you perform can match?",
     "Foreign-body manoeuvres are for an <i>ineffective</i> cough &mdash; silent, unable to cry, speak or breathe. Is her cough effective?",
     "An effective cough generates higher airway pressure than any external manoeuvre. <b>Do not interfere</b>: keep her calm, give oxygen if she tolerates it, and arrange urgent assessment and bronchoscopy with airway help ready in case she deteriorates.",
     "<b>A</b> &mdash; back blows and chest thrusts are for an ineffective cough; used now they may dislodge the object into a worse position. <b>B</b> &mdash; blind finger sweeps push objects further in and are never recommended. <b>C</b> &mdash; she is protecting her own airway; intubating now converts a partial, self-managed obstruction into a procedural emergency.",
     "Watch the cough, not the noise. The moment it becomes silent, the plan changes.",
     "section 3, ‘Opening and supporting the airway’"),
   Q("A 9-month-old with pneumonia on nasal prong oxygen at 1 L/min has SpO₂ of 86%, grunting and severe chest indrawing, but is awake and taking a few feeds. The district hospital has no ventilator; the nearest PICU is four hours away by road. What is the most appropriate next step?",
     ["Increase nasal prong flow to 4 L/min and review in the morning.",
      "Start bubble CPAP with trained staff monitoring, and begin arranging transfer now while he is still compensating.",
      "Intubate on the ward to protect the airway before transfer.",
      "Stop oral feeds and give a 20 mL/kg fluid bolus for dehydration."],
     1,
     "Grunting tells you what the lungs need. What is the infant trying to generate for himself?",
     "He needs distending pressure, not just more oxygen, and the decision that matters most in a setting without a ventilator is about timing. Which option does both?",
     "Grunting and hypoxaemia despite oxygen mean alveolar collapse: he needs <b>distending pressure</b>, which bubble CPAP provides and which is evidence-supported for infants with severe pneumonia where ventilation is unavailable. The other decision is <b>transfer while he is still compensating</b> &mdash; not after he tires.",
     "<b>A</b> &mdash; very high prong flow in an infant adds little distending pressure reliably, and &ldquo;review in the morning&rdquo; leaves a hypoxaemic infant unmonitored overnight. <b>C</b> &mdash; intubating without the means to ventilate and monitor him afterwards is dangerous. <b>D</b> &mdash; nothing here suggests shock, and a bolus in severe pneumonia worsens oxygenation.",
     "In a hospital without a ventilator, the transfer decision is itself a treatment. Make it early.",
     "section 5, ‘Supporting the failing airway, across settings’")]
)

# ------------------------------------------------------------------ UNIT 5
unit(5, "B", "Circulation: recognising shock and its types",
  "Shock is not low blood pressure. Shock is inadequate delivery of oxygen and fuel to tissues relative to demand. A child can be deeply shocked with a textbook blood pressure.",
  [("e", "Recognise compensated and decompensated shock at the bedside without laboratory support."),
   ("e", "Classify shock as hypovolaemic, distributive, cardiogenic or obstructive, and state the treatment that differs for each."),
   ("a", "Perform the fifteen-second cardiac check before any bolus, and explain why it prevents a recognisable category of death."),
   ("x", "Use lactate and the Phoenix cardiovascular criteria appropriately, knowing what each can and cannot tell you.")],
  [
   sec(1, "Recognising shock from three organs", '''
  <p>Shock is a clinical diagnosis made from the perfusion of three organs you can examine at the bedside: the <b>brain</b> (level of consciousness, interaction), the <b>skin</b> (temperature gradient, capillary refill, mottling) and the <b>kidney</b> (urine output: below 1 mL/kg/h in infants and young children, below 0.5 mL/kg/h in adolescents).</p>''' + table(
     ["Sign", "Compensated", "Decompensated"],
     [["Heart rate", "Tachycardia", "Extreme tachycardia, then bradycardia (pre-terminal)"],
      ["Blood pressure", "Normal; narrow pulse pressure", "Hypotension"],
      ["Pulses", "Weak peripheral pulses (bounding in warm shock)", "Absent peripheral, weak central pulses"],
      ["Capillary refill", "Over 2&ndash;3 s (cold shock) or flash under 1 s (warm shock)", "Markedly prolonged; mottling"],
      ["Sensorium", "Irritable, anxious, clingy", "Lethargic, unresponsive"],
      ["Urine output", "Reduced", "Anuric"]]) + evidence('''<p><b>Capillary refill has limits.</b> It varies with room temperature, site, pressure and observer, and performs modestly on its own. Use it as one sign in a cluster and as a trend by the same observer. Standardise: sternum or fingertip at heart level, five seconds of pressure, in a warm room.</p>''', "Know the limits of your best sign")),

   sec(2, "Four types of shock &mdash; because treatment diverges", table(
     ["Type", "Mechanism", "Paediatric causes", "Clues", "What changes"],
     [["<b>Hypovolaemic</b> (commonest)", "Low preload", "Diarrhoea, DKA, burns, haemorrhage, dengue plasma leak", "History of losses, dry mucosa, sunken eyes or fontanelle", "Volume is the treatment"],
      ["<b>Distributive</b>", "Low vascular tone, maldistribution", "Sepsis, anaphylaxis, spinal injury", "Warm peripheries, flash refill, wide pulse pressure; fever, urticaria or wheeze", "Fluid plus early vasoactive; IM adrenaline first in anaphylaxis"],
      ["<b>Cardiogenic</b>", "Pump failure or arrhythmia", "Myocarditis, cardiomyopathy, congenital heart disease, SVT, duct-dependent lesion in a neonate, scorpion envenomation", "Big liver, gallop, crackles, raised JVP; <b>worsens with fluid</b>", "Small cautious volume or none; inotrope; treat the rhythm; prostaglandin for a duct-dependent neonate"],
      ["<b>Obstructive</b>", "Mechanical block to flow", "Tension pneumothorax, tamponade, critical coarctation", "Absent breath sounds with tracheal shift; muffled heart sounds with distended neck veins; weak femoral pulses", "Fluid will not fix it: needle decompression, pericardiocentesis, prostaglandin"]]) + pearl('''<p><b>The fifteen-second cardiac check.</b> Before every bolus in an undifferentiated shocked child: feel for the liver edge, listen for a gallop, listen for crackles, look at the neck veins. A big liver in a shocked child means <i>think cardiogenic</i> &mdash; and a 20 mL/kg bolus may kill. This single habit prevents the recognisable death of the &ldquo;septic&rdquo; infant with myocarditis or a duct-dependent lesion who arrests after fluid.</p>''', "The habit that saves the most lives in this unit")),

   sec(3, "Warm and cold shock", '''
  <p>In septic shock, children more often present <b>cold</b> &mdash; high systemic resistance, low cardiac output, prolonged capillary refill and cool, mottled limbs. Adults and adolescents more often present <b>warm</b> &mdash; low resistance, flash refill and bounding pulses. The distinction is imperfect and can change within hours, which is why reassessment after every intervention matters more than the initial label. It remains useful for one decision: which vasoactive to start when fluid is not enough (Unit 10).</p>''', tier="good", lvl="a"),

   sec(4, "Lactate and the Phoenix criteria", '''
  <p>The 2026 Surviving Sepsis Campaign paediatric guideline makes a strong recommendation to <b>measure lactate</b> as part of the initial evaluation. Use it to support recognition and to track response &mdash; never to delay treatment of a child who is clinically shocked.</p>
  <p>The <b>Phoenix criteria</b> (JAMA 2024) define paediatric sepsis as suspected infection with a Phoenix Sepsis Score of at least 2, and septic shock as sepsis with at least one cardiovascular point. Cardiovascular points come from vasoactive medication, lactate and age-adjusted mean arterial pressure.</p>''' + table(
     ["Cardiovascular component", "1 point", "2 points"],
     [["Vasoactive medications", "One", "Two or more"],
      ["Lactate (mmol/L)", "5&ndash;10.9", "11 or more"],
      ["Mean arterial pressure (mmHg), by age", "Below the age threshold (e.g. under 1 month: 17&ndash;30; 1&ndash;11 months: 25&ndash;38; 1&ndash;2 years: 31&ndash;43)", "Below the lower threshold (e.g. under 1 month: &lt;17; 1&ndash;11 months: &lt;25; 1&ndash;2 years: &lt;31)"]]) + pitfall('''<p><b>Using Phoenix to decide whether to treat.</b> Phoenix was built to <i>classify</i> children with established organ dysfunction for research and reporting, largely from data in resourced hospitals. It is not a bedside screening tool, and a child with suspected sepsis who does not yet meet it still needs antibiotics and careful fluid decisions now. The 2026 guideline itself accepts evidence based on either the older 2005 criteria or Phoenix.</p>''', "Misusing a definition as a trigger"), tier="nice", lvl="x"),
  ],
  [Q("A 5-month-old has poor feeding and fast breathing. Heart rate 210/min, cool peripheries, capillary refill 4 seconds. The liver is 4 cm below the costal margin and there is a gallop rhythm. A colleague is drawing up 20 mL/kg of saline. What do you advise?",
     ["Give the 20 mL/kg bolus over 10 minutes and repeat if needed; this is septic shock until proven otherwise.",
      "Withhold all fluid indefinitely and observe.",
      "Give 40 mL/kg over 30 minutes because infants need more fluid than older children.",
      "Hold the large bolus: this looks cardiogenic. Get an ECG for a possible arrhythmia, give at most a cautious 5&ndash;10 mL/kg with reassessment, and prepare inotropic support."],
     3,
     "What did the fifteen-second cardiac check find?",
     "A big liver and a gallop in a shocked infant point to one type of shock. And a heart rate of exactly 210 that does not vary &mdash; what rhythm should you exclude before anything else?",
     "Hepatomegaly plus a gallop in a shocked infant means <b>cardiogenic shock</b> &mdash; myocarditis, cardiomyopathy, a duct-dependent lesion, or SVT causing failure. A standard 20 mL/kg bolus can precipitate pulmonary oedema and arrest. Get an ECG (an invariant 210 suggests SVT, treated with vagal manoeuvres or adenosine, not fluid), give at most a small, cautious aliquot, and prepare an inotrope.",
     "<b>A</b> &mdash; ignores the two findings that change management. <b>B</b> &mdash; titration, not abstinence: if there is genuine volume depletion, a small aliquot with reassessment is reasonable. <b>C</b> &mdash; a larger bolus is the most dangerous option on the list.",
     "&ldquo;Septic until proven otherwise&rdquo; is a useful rule for antibiotics. It is a dangerous rule for fluid.",
     "section 2, ‘Four types of shock’"),
   Q("A 7-year-old with 3 days of fever has heart rate 150/min, capillary refill 5 seconds, cool mottled legs and is drowsy. BP 102/64 mmHg. Point-of-care lactate is not available. Which statement is correct?",
     ["He is not in shock, because his blood pressure is above the hypotension threshold for his age.",
      "He cannot be classified as having septic shock until lactate or Phoenix criteria are available, so treatment should wait.",
      "He is in shock on clinical grounds; start treatment now, and use lactate later, if available, to track the response.",
      "He has warm shock, so noradrenaline should be started before any fluid."],
     2,
     "Which three organs did you examine, and what did each tell you?",
     "Brain (drowsy), skin (5-second refill, mottled, cool) &mdash; do these need a laboratory test to be abnormal? And cool mottled legs: warm shock or cold?",
     "Poor perfusion of brain and skin with a maintained pressure is <b>compensated shock</b>, a clinical diagnosis. Treatment starts now. Lactate is recommended as part of the evaluation and is useful to track the response, but its absence never delays treatment.",
     "<b>A</b> &mdash; his threshold is 70 + (2 &times; 7) = 84 mmHg; a normal pressure is expected in compensated shock. <b>B</b> &mdash; Phoenix classifies; it does not decide whether a sick child is treated. <b>D</b> &mdash; cool, mottled legs with slow refill describe cold shock, and in any case fluid assessment comes first.",
     "Definitions are for counting children. Examination is for treating them.",
     "section 1, ‘Recognising shock from three organs’, and section 4")]
)

# ------------------------------------------------------------------ UNIT 6
unit(6, "B", "Disability: the child with altered sensorium",
  "A child who is not behaving normally has a brain that is not being perfused, oxygenated or fuelled &mdash; or is being poisoned, infected, compressed or is seizing. Those seven words are the differential.",
  [("e", "Assess and record the level of consciousness with AVPU and the paediatric Glasgow Coma Scale, with pupils and posture."),
   ("e", "Perform the first three actions in any child with altered sensorium, beginning with glucose."),
   ("a", "Build a structured differential for non-traumatic coma, including the causes that are seasonal and regional in India."),
   ("a", "Decide when a lumbar puncture is safe, and give antibiotics without waiting for it when it is not.")],
  [
   sec(1, "The first three actions", algo("In any child with altered consciousness", ''' 1. ABC FIRST   airway at risk if responds only to pain (AVPU "P")
                 or worse · oxygen · ventilate if breathing is inadequate
 2. GLUCOSE     bedside capillary glucose in EVERY child with altered
                 consciousness, seizure or shock  ("don't ever forget glucose")
 3. LOOK FOR    pupils · posture · neck stiffness · fontanelle · rash
    THE CAUSE    · breath odour · injuries · toxidrome · temperature''') + '''
  <p>If the glucose is low, treat it before anything else (Unit 7). If the child is convulsing, the time-based algorithm in Unit 13 starts now.</p>'''),

   sec(2, "Measuring the level of consciousness", table(
     ["AVPU", "Approximate GCS", "Meaning"],
     [["<b>A</b>lert", "15", "Normal"],
      ["Responds to <b>V</b>oice", "About 13", "Abnormal; find the cause"],
      ["Responds only to <b>P</b>ain", "About 8", "ETAT &ldquo;coma&rdquo; &mdash; an emergency sign. The airway is at risk."],
      ["<b>U</b>nresponsive", "3", "Airway protection needed now"]]) + '''
  <p>AVPU is fast and consistent between observers, which makes it ideal at triage. The paediatric GCS, with modified verbal and motor scales for pre-verbal children, is better for trending, especially after trauma. Record the components as well as the total, and record the trend: a falling score matters more than any single number.</p>
  <p>Look also at the <b>pupils</b> (size, symmetry, reaction), <b>posture</b> (decorticate or decerebrate) and <b>breathing pattern</b>. A unilateral fixed dilated pupil, abnormal posturing or a Cushing response (high blood pressure, slow pulse, irregular breathing) means raised intracranial pressure with possible herniation &mdash; Unit 13.</p>'''),

   sec(3, "The differential for non-traumatic coma", table(
     ["Category", "Examples", "Clues"],
     [["<b>Infective</b>", "Meningitis, encephalitis (HSV, Japanese encephalitis), cerebral malaria, TB meningitis, scrub typhus, sepsis-associated encephalopathy", "Fever, neck stiffness (unreliable under 18 months), bulging fontanelle, rash, eschar, focal seizures, season and region"],
      ["<b>Metabolic</b>", "Hypoglycaemia, DKA, sodium disorders, hypocalcaemia, uraemia, liver failure, inborn errors, hyperammonaemia", "Deep sighing breathing, ketotic breath, jaundice, big liver, dehydration, consanguinity, decompensation after fasting or illness"],
      ["<b>Toxic</b>", "Organophosphates, kerosene, benzodiazepines, opioids, antihistamines, datura, iron, alcohol, traditional preparations", "A toxidrome (Unit 12). Ask what is in the house and what was given for this illness."],
      ["<b>Structural or vascular</b>", "Tumour, hydrocephalus or shunt block, haemorrhage, stroke, venous sinus thrombosis", "Focal deficit, asymmetric pupils, morning headache and vomiting, a shunt in place"],
      ["<b>Epileptic</b>", "Post-ictal state, non-convulsive status", "Subtle eye deviation, nystagmus, twitching; obtundation that does not lift"],
      ["<b>Inflammatory</b>", "ADEM, autoimmune encephalitis, MIS-C, HLH", "Recent infection, movement disorder, behavioural change, multi-organ involvement"],
      ["<b>Hypoxic-ischaemic</b>", "After arrest, drowning, severe shock", "The event itself"]]) + india('''<p>A child with fever and altered sensorium meets the <b>Acute Encephalitis Syndrome</b> surveillance definition and must be notified. The likely causes shift with season and region: Japanese encephalitis, dengue, scrub typhus, cerebral malaria, enteroviruses and, in particular districts and seasons, hypoglycaemic encephalopathy linked to litchi consumption in undernourished children. <b>Scrub typhus deserves a low threshold for empirical doxycycline or azithromycin</b> &mdash; look for the eschar (Unit 7).</p>''')),

   sec(4, "When is a lumbar puncture safe?", '''
  <p>Suspected meningitis needs cerebrospinal fluid &mdash; but not at the cost of herniation. <b>Defer the LP</b> if any of these are present:</p>
  <ul>
    <li>Reduced or fluctuating consciousness (GCS below 9, or a fall of 3 or more)</li>
    <li>Focal neurological signs, abnormal posture, or unequal or poorly reactive pupils</li>
    <li>Papilloedema, or a slow pulse with high blood pressure</li>
    <li>Shock, respiratory compromise, a recent seizure that has not settled</li>
    <li>Low platelets or a coagulopathy, or infection over the LP site</li>
  </ul>''' + danger('''<p><b>Never let a deferred LP defer the antibiotics.</b> Take blood cultures, give the first dose of an appropriate antibiotic immediately (with antiviral cover where encephalitis is possible), and do the LP later when it is safe. Cultures after antibiotics are less often positive; PCR and CSF cell counts remain informative.</p>''', "The rule that matters more than the list"), tier="must", lvl="a"),
  ],
  [Q("A 4-year-old is brought in drowsy after two days of vomiting. He opens his eyes and groans to a sternal rub but not to his name. His pupils are equal and reactive. Temperature 37.2 &deg;C. What is the single most important immediate test?",
     ["A bedside capillary glucose.",
      "A CT scan of the head.",
      "A lumbar puncture.",
      "Serum electrolytes sent to the laboratory."],
     0,
     "Which cause of coma can be diagnosed in thirty seconds, treated in two minutes, and kills if missed?",
     "He responds only to pain (AVPU &ldquo;P&rdquo;). Before any imaging or laboratory test, what does the first-three-actions rule say?",
     "In every child with altered consciousness, check the <b>glucose</b> at the bedside immediately. Hypoglycaemia is common after vomiting and poor intake, is instantly treatable, and causes permanent harm if missed while waiting for other tests.",
     "<b>B</b> &mdash; imaging may be needed later, but it takes time and moves the child away from resuscitation. <b>C</b> &mdash; a child responding only to pain has a GCS of about 8: LP is unsafe now. <b>D</b> &mdash; electrolytes matter (hyponatraemia is possible) but take longer; glucose comes first and at the bedside.",
     "&ldquo;Don't ever forget glucose&rdquo; is on every emergency poster because it is still forgotten.",
     "section 1, ‘The first three actions’"),
   Q("A 6-year-old with fever and headache for a day has GCS 9, a right pupil larger than the left, heart rate 58/min and BP 138/90 mmHg. Which action is contraindicated right now?",
     ["Blood cultures followed immediately by IV ceftriaxone.",
      "Head-up positioning and airway protection.",
      "An immediate lumbar puncture to confirm meningitis.",
      "Urgent neuroimaging once stabilised."],
     2,
     "Put the slow pulse, the high blood pressure and the unequal pupil together. What is happening inside the skull?",
     "This is a Cushing response with pupillary asymmetry. Which of the four options could precipitate herniation?",
     "Reduced consciousness, an unequal pupil and a Cushing response mean <b>raised intracranial pressure with possible herniation</b>. A lumbar puncture now is contraindicated. Antibiotics are given immediately after blood cultures &mdash; they never wait for CSF &mdash; with airway protection, head-up positioning and hyperosmolar therapy (Unit 13).",
     "<b>A</b> &mdash; correct and urgent: antibiotics do not wait. <b>B</b> &mdash; correct first steps for raised pressure. <b>D</b> &mdash; imaging is appropriate once the child is stable enough to travel.",
     "The LP can always be done tomorrow. The antibiotics cannot be given yesterday.",
     "section 4, ‘When is a lumbar puncture safe?’")]
)

# ------------------------------------------------------------------ UNIT 7
unit(7, "B", "Exposure and the metabolic milieu",
  "&ldquo;E&rdquo; is where the diagnosis often hides: the purpuric rash under the vest, the eschar in the axilla, the cigarette burn, the swollen scrotum, the glucose of 1.8.",
  [("e", "Perform a complete exposure survey while preventing heat loss, and say what must be looked for."),
   ("e", "Recognise and treat hypoglycaemia, and know when to take a critical sample first."),
   ("a", "Recognise and begin treatment of the electrolyte disturbances that kill quickly."),
   ("x", "Interpret a paediatric blood gas with the anion gap, and name the emergency behind it.")],
  [
   sec(1, "The exposure survey", '''
  <p>Undress fully, look everywhere, then cover and warm. What a hurried examiner misses:</p>
  <ul>
    <li><b>Rash.</b> A non-blanching purpuric rash is meningococcal sepsis until proven otherwise. Press with a glass. Look at soles, palms, conjunctivae and behind the ears.</li>
    <li><b>Eschar.</b> Scrub typhus. Axilla, groin, natal cleft, waistband, behind the ear. It is painless, so it is never reported.</li>
    <li><b>Genitalia and hernial orifices.</b> Torsion and incarcerated hernia. A vomiting, irritable infant needs the nappy off.</li>
    <li><b>Back and scalp.</b> Log-roll in trauma; look for injuries, a sacral dimple, lice and scabies.</li>
    <li><b>Bruises in unusual places</b> &mdash; torso, ears or neck in a child aged four or under; any bruise in an infant under four months who is not yet mobile; patterned bruises. Consider inflicted injury (Unit 20).</li>
    <li><b>Temperature.</b> Measure it. In a young infant or a malnourished child, a low temperature is as ominous as fever.</li>
    <li><b>Weight.</b> A real weight whenever possible &mdash; every dose depends on it.</li>
  </ul>'''),

   sec(2, "Glucose", table(
     ["", "What to do"],
     [["Threshold", "WHO: treat a blood glucose <b>below 2.5 mmol/L (45 mg/dL)</b>, or <b>below 3 mmol/L (54 mg/dL)</b> in a child with severe malnutrition. Many hospital protocols act at 3.0&ndash;3.3 mmol/L in a sick child. Neonates follow neonatal thresholds."],
      ["Treatment", "<b>10% glucose 5 mL/kg IV or IO</b> (0.5 g/kg), then a glucose-containing infusion, and recheck in 15&ndash;30 minutes. Never give 50% glucose to a child &mdash; dilute it."],
      ["Unconscious, no access", "Sugar solution or expressed breast milk by nasogastric tube, or sugar under the tongue, while access is obtained. Do not let the search for a vein delay glucose."],
      ["Critical sample", "If hypoglycaemia is unexplained or recurrent, take blood before treatment when you safely can: glucose, ketones (β-hydroxybutyrate), lactate, ammonia, insulin, cortisol, growth hormone, acylcarnitines; and the first urine after the event. It can save years of diagnostic uncertainty."]]) + pearl('''<p><b>Hypoglycaemia without ketones</b> means hyperinsulinism or a fatty-acid oxidation defect such as MCAD deficiency. Both are dangerous and both are treatable. Ketotic hypoglycaemia after a fast in a small toddler is far commoner and more benign &mdash; but only the critical sample tells them apart.</p>''')),

   sec(3, "Electrolytes that kill quickly", table(
     ["Disturbance", "Presentation", "Immediate action", "Trap"],
     [["<b>Hyponatraemia</b> (symptomatic, or Na &lt;125)", "Seizures, lethargy, vomiting, coma", "<b>3% saline 3&ndash;5 mL/kg over 10&ndash;20 min</b>, repeated until seizures stop", "After symptoms settle, limit the rise to about 8&ndash;10 mmol/L in 24 h. Hypotonic maintenance fluid is a leading cause: use isotonic maintenance in hospitalised children."],
      ["<b>Hypernatraemia</b> (Na &gt;150)", "Doughy skin, irritability then lethargy, high-pitched cry", "Resuscitate shock with isotonic fluid; then correct slowly, no faster than about 0.5 mmol/L per hour", "Rapid correction causes cerebral oedema and seizures."],
      ["<b>Hyperkalaemia</b> (K &gt;6.5 or ECG changes)", "Peaked T waves, then wide QRS, then arrest", "<b>10% calcium gluconate 0.5 mL/kg IV</b> (max 20 mL) to protect the heart; then insulin with glucose, nebulised salbutamol; then removal", "A haemolysed sample misleads &mdash; but never assume haemolysis in an anuric or crushed child. Get an ECG."],
      ["<b>Hypocalcaemia</b>", "Tetany, stridor from laryngospasm, seizures, long QT", "10% calcium gluconate 0.5&ndash;1 mL/kg IV slowly, diluted, with ECG monitoring", "Extravasation causes necrosis. Check magnesium: low magnesium makes low calcium refractory."]]) + '''
  <p class="dash-status">Verify infusion concentrations and maximum doses against your unit protocol and Appendix E before use.</p>''', lvl="a"),

   sec(4, "Reading the blood gas", algo("Five steps", ''' 1. pH           acidaemia (< 7.35) or alkalaemia (> 7.45)?
 2. PRIMARY      high PaCO2 with low pH   → respiratory acidosis
                 low HCO3  with low pH    → metabolic acidosis
 3. COMPENSATED? compensation is never complete. A normal pH with two
                 abnormal values suggests a MIXED disorder.
 4. ANION GAP    Na − (Cl + HCO3); normal about 8–12 mmol/L
                 RAISED gap:  Ketones (DKA, starvation) · Uraemia
                              Lactate (shock, sepsis, seizures, thiamine
                                       deficiency, inborn errors)
                              Toxins (salicylate, methanol, iron)
                 NORMAL gap:  diarrhoea · renal tubular acidosis ·
                              large volumes of 0.9% saline
 5. OXYGENATION  SpO2/FiO2 or PaO2/FiO2 — used in PARDS and Phoenix''') + '''
  <p>A raised-gap metabolic acidosis in a shocked child is usually lactate &mdash; but ask whether it is ketones (DKA presenting as &ldquo;gastroenteritis with fast breathing&rdquo;) or a toxin. A normal-gap acidosis after several litres of saline is the saline, and a reason the 2026 sepsis guideline prefers balanced crystalloids (Unit 8).</p>''', tier="good", lvl="x"),
  ],
  [Q("A 2-year-old admitted with gastroenteritis and given 0.18% saline with 5% glucose as maintenance has a generalised seizure on day two. Sodium is 118 mmol/L. What is the best immediate management?",
     ["Load with phenytoin and recheck the sodium in the morning.",
      "Restrict fluids and observe.",
      "Correct to a normal sodium within six hours using 0.9% saline.",
      "Give 3% saline 3&ndash;5 mL/kg over 10&ndash;20 minutes, repeated if the seizure persists, then correct slowly."],
     3,
     "Will an antiseizure drug stop a seizure caused by a low sodium?",
     "Symptomatic hyponatraemia needs a small, fast rise in sodium to stop the seizure &mdash; then a slow rise after that. Which option does both?",
     "Symptomatic hyponatraemia is a neurological emergency. <b>3% saline 3&ndash;5 mL/kg</b> produces the small, rapid rise (a few mmol/L) that usually stops the seizure. After that, correct slowly to avoid osmotic demyelination. The deeper lesson: hypotonic maintenance fluid caused this; isotonic maintenance is the standard for hospitalised children.",
     "<b>A</b> &mdash; antiseizure drugs will not work until the sodium rises, and the seizure is the emergency now. <b>B</b> &mdash; restriction is far too slow for a seizing child. <b>C</b> &mdash; normalising the sodium in six hours is dangerously fast.",
     "When a seizure will not stop, ask what is causing it before asking which drug is next.",
     "section 3, ‘Electrolytes that kill quickly’"),
   Q("A 9-year-old with 6 days of fever, headache and myalgia has been treated for typhoid without response. Platelets are 60,000/µL and ALT is 180 U/L. On exposure you find a painless 6 mm black-crusted lesion in the left axilla. What should you do?",
     ["Add doxycycline (or azithromycin) now for probable scrub typhus.",
      "Continue the typhoid treatment for another 5 days before changing anything.",
      "Diagnose dengue and stop all antibiotics.",
      "Send an IgM for scrub typhus and withhold treatment until it returns."],
     0,
     "What painless lesion, hidden in a skin fold, is never mentioned by the patient?",
     "An eschar plus fever, thrombocytopenia and raised transaminases is a classic cluster. Does a definite eschar need a serology result before treatment?",
     "A painless black eschar in a skin fold with fever, low platelets and transaminitis is <b>scrub typhus</b> until proven otherwise. Start <b>doxycycline</b> (or azithromycin) now; response is usually within 48 hours. Found only because the child was fully exposed.",
     "<b>B</b> &mdash; six days without response is itself a reason to rethink. <b>C</b> &mdash; dengue does not cause an eschar, and stopping all antibiotics would leave scrub typhus untreated. <b>D</b> &mdash; serology can be falsely negative early and should never delay treatment when the eschar is present.",
     "Undress the child. The diagnosis you need is often under the vest.",
     "section 1, ‘The exposure survey’")]
)
