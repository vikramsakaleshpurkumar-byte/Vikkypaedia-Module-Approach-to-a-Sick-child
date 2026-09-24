from gen import *

part("A", "Foundations: how to think before you act", "Units 1&ndash;3 · ~5 hours",
     "Every protocol in the next four Parts is an answer to three questions asked here: why do children die, how do you see it coming in sixty seconds, and why does a child's physiology hide the danger until late. Part A is open from the first minute.")

# ------------------------------------------------------------------ UNIT 1
unit(1, "A", "Why children die, and where this module fits",
  "A child who dies in hospital usually does so within the first day, from a short list of physiological end-points, after a period in which someone could have noticed. This module exists because of that sentence.",
  [("e", "State the leading causes of death in children under five, globally and in India, and explain why most are preventable at first contact."),
   ("e", "Describe the deterioration continuum &mdash; well, compensated, decompensated, arrest &mdash; and name the two final common pathways to paediatric cardiac arrest."),
   ("a", "Distinguish recognition failure, diagnostic error and execution failure, and match each to the fix that actually addresses it."),
   ("x", "Critique the evidence for structured recognition systems (ETAT, PEWS), including the negative EPOCH trial, and read it across the resource gradient.")],
  [
   sec(1, "The mortality picture", '''
  <p>Under-five mortality has fallen steeply over three decades, but the deaths that remain concentrate into a short list. Beyond the neonatal period the largest contributors are <b>pneumonia, diarrhoea, malaria, injuries</b> and <b>infection in a malnourished child</b>. Within the neonatal period, <b>prematurity, intrapartum-related events and neonatal infection</b> dominate.</p>
  <p>Two facts should shape how you read the rest of this module:</p>
  <ol>
    <li><b>Death clusters early.</b> A large share of in-hospital paediatric deaths happen within 24 hours of arrival &mdash; many within the first few hours. The window in which recognition changes the outcome is measured in minutes to hours, not days.</li>
    <li><b>The pathway is respiratory or circulatory, not primarily cardiac.</b> Children rarely have a primary arrhythmic arrest. Paediatric cardiac arrest is usually the end of progressive respiratory failure or shock. That is good news: there is a long, visible, interruptible runway before arrest.</li>
  </ol>
  ''' + india('''<p>India's neonatal period now accounts for the majority of under-five deaths, which is why Unit 17 (the sick young infant) is core, not optional. First contact for a sick child is frequently not a paediatrician: it is an ASHA, an ANM, a PHC medical officer, a general practitioner or a private clinic. IMNCI and F-IMNCI exist precisely to push structured recognition down to that level. A module that teaches only PICU-grade assessment teaches the wrong end of the pathway &mdash; recognition at first contact and safe referral save far more lives than any single ICU intervention.</p>
  <p class="dash-status">Mortality figures change every year. Quote current Sample Registration System (SRS) bulletins and national cause-of-death estimates, not a number remembered from a lecture.</p>''')),

   sec(2, "The deterioration continuum", algo("The runway to arrest", '''  WELL
    │   insult: infection · dehydration · obstruction · toxin · trauma · metabolic
    ▼
  COMPENSATED   tachycardia · tachypnoea · cool peripheries · CRT > 2 s
    │           anxious, clingy or quiet · NORMAL blood pressure
    │           ▸ this is where you win
    ▼
  DECOMPENSATED hypotension · altered sensorium · mottling
    │           weak central pulses · falling respiratory effort
    │           ▸ hours of physiological credit already spent
    ▼
  PERI-ARREST   bradycardia · gasping · unresponsive
    ▼
  ARREST        usually asystole or PEA · survival poor''') + '''
  <p>The clinically decisive point is that <b>a child's blood pressure is a late and treacherous sign</b>. Children hold their blood pressure with vigorous tachycardia and vasoconstriction until compensation fails &mdash; abruptly. A normal blood pressure in a tachycardic, cold, unwell child is not reassurance. It is a compensating child, and compensation is a countdown.</p>
  ''' + pitfall('''<p>&ldquo;BP was 96/60, so I wasn't worried.&rdquo; Hypotension in a child is a pre-terminal sign; in haemorrhage it may not appear until roughly a third of the circulating volume is gone. Treat the heart rate, the capillary refill, the skin temperature and the sensorium &mdash; not the number on the cuff.</p>''')),

   sec(3, "Three different failures, three different fixes", table(
     ["Failure", "What happened", "What fixes it"],
     [["<b>Recognition failure</b>", "The abnormal physiology was present and recordable, but nobody registered it as abnormal &mdash; or registered it and did not escalate.", "Structured assessment (PAT, ETAT), track-and-trigger charts, mandated escalation, and permission for nurses and parents to escalate."],
      ["<b>Diagnostic error</b>", "The physiology was noticed; the cause was misattributed &mdash; DKA called gastroenteritis, myocarditis called bronchiolitis.", "Illness scripts, a forced alternative diagnosis, a diagnostic time-out, follow-up loops."],
      ["<b>Execution failure</b>", "Recognised and diagnosed, but the treatment was late, wrongly dosed or unavailable.", "Pre-calculated dose charts, checklists, simulation, and oxygen and drug supply chains."]]) + '''
  <p>Parts A and B of this module attack recognition failure. Parts C and D attack diagnostic and execution error for the conditions that kill most often. Part E attacks the systems around them. Deciding which of the three is your own department's real problem is a worthwhile first act of quality improvement.</p>''', tier="good", lvl="a"),

   sec(4, "Does structured recognition work? Read the negative trial too", evidence('''<p><b>ETAT in low-resource hospitals.</b> Introducing structured emergency triage, with training and supervision, has been associated with substantial falls in early in-hospital paediatric mortality in several African and Asian hospitals. The mechanism is simple: a queue is replaced by a triage decision.</p>
  <p><b>PEWS in well-resourced hospitals.</b> The EPOCH cluster-randomised trial (Parshuram et al., <i>JAMA</i> 2018; 21 hospitals in 7 countries, over 144,000 admissions) found that the Bedside Paediatric Early Warning System did not reduce all-cause hospital mortality compared with usual care.</p>
  <p><b>How to reconcile them.</b> A track-and-trigger tool adds value in proportion to the surveillance gap it fills. On a tertiary ward with 1:2 nursing and a rapid response team the marginal gain is small. On a 60-bed district ward with two night nurses and no triage, the same tool can be transformative. <b>Do not carry a negative trial's conclusion across a resource gradient</b> &mdash; in either direction. It is a habit of appraisal you will need again for FEAST in Unit 8.</p>'''), tier="nice", lvl="x"),
  ],
  [Q("A 3-year-old has had fever and poor feeding for three days. Heart rate 168/min, respiratory rate 46/min, BP 98/62 mmHg, capillary refill 4 seconds, cool knees; irritable but consolable. Which statement is most accurate?",
     ["The normal blood pressure shows the child is haemodynamically stable; treat the fever and review in four hours.",
      "The child is in compensated shock and needs immediate intervention, even though the blood pressure is normal.",
      "The tachycardia is explained by the fever; antipyretics and a repeat heart rate will settle the question.",
      "Shock cannot be diagnosed until a serum lactate is available."],
     1,
     "Which of the findings here does the body sacrifice first, and which does it protect to the very end?",
     "Look at the perfusion findings &mdash; capillary refill, skin temperature, behaviour &mdash; separately from the blood pressure. If they are abnormal while the pressure is normal, what word describes that state?",
     "Tachycardia plus delayed capillary refill plus cool peripheries plus altered behaviour is inadequate tissue perfusion, with blood pressure still held up by compensation. That is <b>compensated shock</b>, and it is the stage at which treatment works best.",
     "<b>A</b> &mdash; the classic error: blood pressure is the last thing to fall in a child, so a normal value cannot exclude shock. <b>C</b> &mdash; fever raises the heart rate by roughly 10 beats/min per &deg;C; it does not produce a capillary refill of 4 seconds and cold knees. <b>D</b> &mdash; lactate supports the diagnosis and tracks the response, but shock is a clinical diagnosis. Waiting for a laboratory value spends the child's reserve.",
     "Say it aloud at handover: &ldquo;normal pressure, poor perfusion.&rdquo; Naming the state is often what gets the fluid decision made.",
     "section 2, ‘The deterioration continuum’"),
   Q("A registrar reviewing ward deaths finds that in three of five cases the observation charts showed rising heart and respiratory rates for six to ten hours before the arrest call, but no one was called. The correct diagnoses were made at the arrest. What is the principal failure, and the fix most likely to prevent the next one?",
     ["Diagnostic error; teach illness scripts for the conditions involved.",
      "Execution failure; buy a second defibrillator and pre-fill resuscitation drugs.",
      "A staffing problem only; nothing can be done until nurse numbers rise.",
      "Recognition failure; an observation chart with printed age-specific trigger thresholds and a mandated escalation response."],
     3,
     "The physiology was on paper for hours. The diagnosis was right. So where did the chain break?",
     "Sort the failure into one of three bins: not <i>seeing</i> the danger, <i>misnaming</i> it, or <i>acting</i> on it too slowly. Here the numbers were seen and recorded &mdash; were they <i>registered</i> as abnormal and escalated?",
     "The abnormal physiology was recorded and not acted on: that is <b>recognition failure</b>. The fix is to make abnormality impossible to miss and escalation automatic &mdash; age-specific thresholds printed on the chart, and a defined response when one is crossed.",
     "<b>A</b> &mdash; the diagnoses were correct at the arrest, so the reasoning was not the problem. <b>B</b> &mdash; equipment at the arrest cannot fix the six hours before it. <b>C</b> &mdash; staffing matters, but trigger thresholds and a mandated response are cheap, work with the staff you have, and address exactly this pattern.",
     "Most &ldquo;unexpected&rdquo; ward arrests in children were expected by the chart. The chart just had no way to shout.",
     "section 3, ‘Three different failures, three different fixes’")]
)

# ------------------------------------------------------------------ UNIT 2
unit(2, "A", "The sixty-second assessment",
  "Before you touch the child, before the thermometer, before the history, you look and listen from the doorway. Done properly it takes under a minute, needs no equipment, and decides the next hour.",
  [("e", "Perform a Paediatric Assessment Triangle and convert the result into a physiological category and a first move."),
   ("e", "Apply WHO ETAT to sort any arriving child into emergency, priority or queue, and name every emergency sign from memory."),
   ("e", "Use age-specific normal ranges for heart rate, respiratory rate and systolic blood pressure, and the formula for hypotension in children aged 1&ndash;10 years."),
   ("x", "Choose and defend a track-and-trigger tool for a given ward, including its escalation response and a carer-concern trigger.")],
  [
   sec(1, "The Paediatric Assessment Triangle", '''
  <p>The PAT is purely observational and hands-off. Its three sides are <b>Appearance</b>, <b>Work of breathing</b> and <b>Circulation to skin</b>. It answers two questions &mdash; <i>how sick?</i> and <i>which system?</i> &mdash; before any history or investigation.</p>''' + table(
     ["Side", "What you look for"],
     [["<b>Appearance</b> (TICLS)", "<b>T</b>one &mdash; limp or resisting · <b>I</b>nteractivity &mdash; reaches, plays, tracks · <b>C</b>onsolability &mdash; settles with the carer · <b>L</b>ook/gaze &mdash; fixes on you, or stares blankly · <b>S</b>peech/cry &mdash; strong, weak, high-pitched or absent"],
      ["<b>Work of breathing</b>", "Noises without a stethoscope (stridor, grunting, wheeze) · abnormal position (tripod, sniffing, refusing to lie flat) · recession (subcostal, intercostal, suprasternal) · nasal flaring · head bobbing in infants"],
      ["<b>Circulation to skin</b>", "Pallor · mottling · cyanosis"]]) + table(
     ["Appearance", "Breathing", "Circulation", "Category", "First move"],
     [["Normal", "Normal", "Normal", "Stable", "History and examination"],
      ["Normal", "Abnormal", "Normal", "Respiratory distress", "Oxygen, position of comfort, find the cause"],
      ["Abnormal", "Abnormal", "Normal", "Respiratory failure", "Support ventilation now"],
      ["Normal", "Normal", "Abnormal", "Compensated shock", "Access, fluid decision, find the cause"],
      ["Abnormal", "Normal", "Abnormal", "Decompensated shock", "Resuscitate immediately"],
      ["Abnormal", "Normal", "Normal", "Primary brain or metabolic problem", "Glucose, seizures, toxins, infection, raised pressure"],
      ["Abnormal", "Abnormal", "Abnormal", "Cardiopulmonary failure", "Full resuscitation; arrest is imminent"]]) + pearl('''<p>The row most often missed on wards is <b>abnormal appearance with normal breathing and normal circulation</b>. That child has a brain or metabolic problem &mdash; hypoglycaemia, meningitis or encephalitis, poisoning, non-convulsive seizures, intussusception with lethargy, or an inborn error decompensating. Check a glucose before anything else.</p>''')),

   sec(2, "WHO ETAT: emergency, priority, queue", '''
  <p>ETAT is WHO's triage system for facilities where children arrive in numbers and wait. Its strength is that a trained nurse or health worker can perform it at the door, without investigations, in under a minute.</p>''' + fig("etat", "ETAT at the door", '''EMERGENCY SIGNS  ▸ treat NOW, do not queue
  A  Airway      obstructed or absent breathing
  B  Breathing   severe respiratory distress · central cyanosis
  C  Circulation cold hands WITH capillary refill > 3 s
                 AND a weak, fast pulse
  C  Coma        unconscious (AVPU: responds only to pain, or not at all)
  C  Convulsing  now
  D  Dehydration severe, in a child with diarrhoea: any two of
                 lethargy · sunken eyes · very slow skin pinch
                 (Check for severe malnutrition before giving IV fluid)

PRIORITY SIGNS ("3 TPR MOB")  ▸ front of the queue, assess quickly
  Tiny baby (under 2 months) · Temperature (very high)
  Trauma or urgent surgical condition · Pallor (severe)
  Poisoning · Pain (severe) · Respiratory distress
  Restless, irritable or lethargic · Referral (urgent)
  Malnutrition (visible severe wasting) · Oedema of both feet
  Burns (major)

NON-URGENT  ▸ queue and see in turn''') + evidence('''<p>WHO's <i>Paediatric emergency triage, assessment and treatment: care of critically-ill children</i> (2016) updated the ETAT materials and the Pocket Book, with recommendations on oxygen, fluids for shock, and anticonvulsants. Where it has been implemented <b>with training and supervision</b>, ETAT has repeatedly been associated with lower early in-hospital mortality. Note the qualifier: a triage poster on a wall is not a triage system.</p>''')),

   sec(3, "Vital signs you must know cold", '''
  <p>Charts are safer than memory, but at 3 a.m. with a crashing child you need approximate ranges instantly. Learn the bands, then check the chart.</p>''' + table(
     ["Age", "Heart rate, awake (/min)", "Respiratory rate (/min)", "Hypotension: systolic below"],
     [["Under 1 month", "100&ndash;205", "30&ndash;60", "60 mmHg"],
      ["1&ndash;12 months", "100&ndash;190", "30&ndash;53", "70 mmHg"],
      ["1&ndash;2 years", "98&ndash;140", "22&ndash;37", "70 + (2 &times; age in years) mmHg"],
      ["3&ndash;5 years", "80&ndash;120", "20&ndash;28", "70 + (2 &times; age in years) mmHg"],
      ["6&ndash;10 years", "75&ndash;118", "18&ndash;25", "70 + (2 &times; age in years) mmHg"],
      ["Over 10 years", "60&ndash;100", "12&ndash;20", "90 mmHg"]]) + '''
  <p>Two things to carry without a chart: <b>hypotension in a child aged 1&ndash;10 years is a systolic pressure below 70 + (2 &times; age in years) mmHg</b>, and the IMNCI fast-breathing thresholds: <b>&ge;60/min under 2 months, &ge;50/min at 2&ndash;11 months, &ge;40/min at 1&ndash;5 years.</b></p>
  ''' + pitfall('''<p>Counting a screaming toddler's respiratory rate. Count over a full 60 seconds in a calm child &mdash; a rate counted for 15 seconds and multiplied by four is unreliable in infants, who breathe periodically. If the child settles on a parent's shoulder, count then.</p>''', "The crying child")),

   sec(4, "Track-and-trigger charts: what makes them work", '''
  <p>Paediatric Early Warning Scores turn repeated observations into an escalation trigger. Whichever tool you use, three design features matter more than the score itself:</p>
  <ul>
    <li><b>A mandated response, not just a number.</b> A given score must bring a named level of skill within a named time.</li>
    <li><b>A carer and nurse override.</b> &ldquo;I am worried about this child&rdquo; must be a legitimate trigger on its own. Parental concern independently predicts deterioration.</li>
    <li><b>A feedback loop.</b> Every arrest and unplanned PICU transfer is reviewed against the preceding twelve hours of observations.</li>
  </ul>''' + tracks(
     ["An electronic PEWS with automatic alerts to a rapid response team", "Continuous monitoring on high-dependency beds; scores recalculated with every observation set", "Audit of trigger-to-review time reported monthly"],
     ["ETAT triage at the door by a trained nurse", "A paper observation chart with age-specific abnormal thresholds printed in colour", "A written escalation ladder at the nursing station, and a standing instruction that any emergency sign means a doctor now", "A &ldquo;worried&rdquo; box on the chart that any nurse or parent can tick"]) + india('''<p>A full electronic PEWS is unrealistic in most district hospitals. The defensible minimum &mdash; ETAT at the door, a colour-banded chart and a written escalation ladder &mdash; costs almost nothing and attacks the recognition gap directly. Several state programmes and the F-IMNCI facility package already expect triage at the point of entry; a chart makes it continue after admission.</p>'''), tier="good", lvl="a"),
  ],
  [Q("At the door of a busy district-hospital OPD, a 14-month-old with four days of diarrhoea is lethargic, has sunken eyes and a very slow skin pinch. Hands are warm and capillary refill is 2 seconds. There is no visible severe wasting. What is the correct ETAT category?",
     ["Emergency &mdash; severe dehydration is an ETAT emergency sign.",
      "Priority &mdash; dehydration is only a priority sign when perfusion is normal.",
      "Non-urgent &mdash; warm hands and normal capillary refill exclude shock.",
      "Emergency &mdash; but only because the child is under two years old."],
     0,
     "ETAT's &ldquo;D&rdquo; is its own emergency sign, separate from &ldquo;C&rdquo;. What does it require?",
     "Severe dehydration in a child with diarrhoea needs any two of three signs: lethargy or unconsciousness, sunken eyes, very slow skin pinch. Count how many this child has.",
     "This child has all three signs of <b>severe dehydration</b>, which is an ETAT <b>emergency</b> sign in its own right. The child is treated now, not queued.",
     "<b>B</b> &mdash; severe dehydration is not downgraded by normal perfusion; the category is set by the dehydration signs themselves. <b>C</b> &mdash; warm hands exclude shock, not severe dehydration; this child is on the way to hypovolaemic shock. <b>D</b> &mdash; age under two months (&ldquo;tiny baby&rdquo;) is a priority sign, but it is not why this child is an emergency.",
     "Before starting IV fluid in severe dehydration, look for severe malnutrition: the fluid plan changes completely (Unit 16).",
     "section 2, ‘WHO ETAT’"),
   Q("A 4-year-old sits upright on her mother's lap refusing to lie down. She has audible inspiratory stridor and suprasternal recession, is alert and watching you, and her skin colour is normal. What is her PAT category, and your first move?",
     ["Respiratory failure; lay her flat and prepare for bag-mask ventilation.",
      "Cardiopulmonary failure; start full resuscitation.",
      "Respiratory distress with an upper-airway cause; keep her on her mother's lap, give oxygen without upsetting her, and call airway help.",
      "Primary brain or metabolic problem; check the blood glucose first."],
     2,
     "Which side of the triangle tells you the brain is still getting enough oxygen?",
     "Appearance is normal, work of breathing is abnormal, circulation is normal. Match that to the table &mdash; then ask what could make an upper-airway problem suddenly worse.",
     "Normal appearance with increased work of breathing is <b>respiratory distress</b>: she is compensating. With stridor, the priority is not to precipitate complete obstruction &mdash; position of comfort, oxygen she will tolerate, and senior airway help before any upsetting intervention.",
     "<b>A</b> &mdash; she is not in failure (her appearance is normal), and laying a child with upper-airway obstruction flat can turn partial obstruction into complete obstruction. <b>B</b> &mdash; appearance and circulation are both normal. <b>D</b> &mdash; that row requires abnormal appearance; hers is normal.",
     "In upper-airway obstruction, a calm child is a safer child. Every procedure you add is a chance to make her cry.",
     "section 1, ‘The Paediatric Assessment Triangle’")]
)

# ------------------------------------------------------------------ UNIT 3
unit(3, "A", "Why children crash late and fast",
  "Every difference between adult and paediatric emergency practice traces back to a handful of anatomical and physiological facts. Learn the facts and the protocols stop needing to be memorised.",
  [("e", "Explain from first principles why airway obstruction, hypoxia, hypoglycaemia and hypothermia develop faster in small children."),
   ("e", "Explain why infant cardiac output is rate-dependent and why bradycardia in a sick infant is an emergency."),
   ("a", "Recognise the tiring child &mdash; the falling respiratory rate that means exhaustion, not recovery."),
   ("x", "Apply named forcing strategies against anchoring, premature closure and attribution in a paediatric emergency.")],
  [
   sec(1, "Airway", '''
  <ul>
    <li><b>Large occiput.</b> Lying supine flexes an infant's neck and obstructs the airway. Aim for a neutral position in infants (a small roll under the shoulders) and a sniffing position in older children.</li>
    <li><b>Relatively large tongue, small jaw.</b> The tongue falling back is the commonest cause of airway obstruction in an obtunded child &mdash; and a jaw thrust often fixes it completely.</li>
    <li><b>Narrow airways.</b> Resistance to laminar flow rises with the <i>fourth power</i> of the fall in radius. In a 4 mm infant trachea, 1 mm of circumferential swelling halves the radius and multiplies resistance about sixteen-fold. The same swelling in an adult trachea is trivial. That one relationship explains croup, bronchiolitis and why a crying child with an inflamed airway can decompensate in seconds.</li>
    <li><b>Nose-breathing in young infants.</b> Nasal blockage alone can cause real distress and feeding failure. Saline drops and gentle suction are genuine therapy.</li>
  </ul>'''),

   sec(2, "Breathing", '''
  <ul>
    <li><b>High oxygen consumption, small reserve.</b> Infants consume roughly twice as much oxygen per kilogram as adults, with a proportionally smaller functional residual capacity. They desaturate on apnoea dramatically faster; pre-oxygenation buys seconds, not minutes.</li>
    <li><b>Compliant chest wall, diaphragm-dependent breathing.</b> Recession is prominent and ventilation inefficient. A distended stomach splints the diaphragm &mdash; which is why gastric decompression matters during bag-mask ventilation.</li>
    <li><b>A diaphragm that tires.</b> Sustained high work of breathing ends in exhaustion.</li>
  </ul>''' + danger('''<p><b>A tiring child looks calmer.</b> Recession lessens, the respiratory rate falls, the child goes quiet and drowsy, and inexperienced observers relax. In a child who was working hard, a falling rate with a falling level of consciousness is <b>pre-arrest</b>. Reassess &mdash; do not relax. Get a blood gas and senior help.</p>''', "The most dangerous sign in paediatrics")),

   sec(3, "Circulation", '''
  <ul>
    <li><b>Cardiac output = stroke volume &times; heart rate.</b> The infant heart has limited ability to raise stroke volume, so output depends largely on rate. <b>Bradycardia in a sick infant is functionally an arrest state, and its commonest cause is hypoxia.</b> Treat it with oxygen and ventilation first; atropine is for vagally mediated bradycardia or primary heart block, not the hypoxic kind.</li>
    <li><b>Vigorous vasoconstriction.</b> Blood pressure is defended at the expense of the skin and gut: cold peripheries, delayed capillary refill and a narrow pulse pressure appear long before hypotension.</li>
    <li><b>Small absolute blood volume</b> &mdash; about 80 mL/kg in infants and 70 mL/kg in children. A 10 kg child has roughly 800 mL of blood. Modest-looking bleeding or third-spacing is proportionally large; so is repeated blood sampling in a small infant.</li>
  </ul>'''),

   sec(4, "Everything else that scales with size", table(
     ["Property", "Paediatric difference", "What it means at the bedside"],
     [["Surface area to mass", "Much higher, especially in neonates", "Rapid heat and water loss. Hypothermia during resuscitation and transport is common, and it worsens acidosis and coagulopathy. Cover the head."],
      ["Glycogen stores", "Small, with high glucose demand", "Hypoglycaemia within hours of poor intake or any critical illness. Check glucose in every sick child."],
      ["Renal concentrating ability", "Immature in infants", "Poor tolerance of both fluid restriction and solute load; dehydration develops fast."],
      ["Immunity", "Immature, especially under 3 months", "Serious bacterial infection presents non-specifically; fever may be absent or replaced by a low temperature."],
      ["Skeleton", "Pliable, incompletely ossified", "Serious chest or abdominal injury without fractures. Rib fractures in an infant imply major force or abuse."],
      ["Communication", "Pre-verbal or limited", "Behaviour is the symptom. A parent saying &ldquo;he is not himself&rdquo; carries diagnostic weight."]]), tier="good"),

   sec(5, "How the sick child fools you", '''
  <p>Emergency paediatrics runs on fast, pattern-based reasoning &mdash; mostly right, and where the errors live. Telling yourself to &ldquo;be less biased&rdquo; does not work. Structural forcing strategies do.</p>''' + table(
     ["Bias", "How it looks in a sick child", "Forcing strategy"],
     [["Anchoring, premature closure", "Referred as &ldquo;bronchiolitis&rdquo;: the 4-month-old's wheeze and big liver turn out to be myocarditis or a VSD in failure.", "Ask aloud: &ldquo;If this is not X, what else fits every finding?&rdquo; Name one alternative before acting."],
      ["Search satisficing", "A fracture found on the trauma series; the splenic injury missed.", "Finish the systematic survey even after the first abnormality."],
      ["Availability", "A dengue outbreak: every fever with low platelets becomes dengue, and enteric fever, malaria and rickettsial illness are missed.", "&ldquo;What else is in season, and what is the one I must not miss?&rdquo;"],
      ["Triage cueing", "A &ldquo;non-urgent&rdquo; label at the door reduces the effort of every later examination.", "Re-triage at every contact; the child at 8 p.m. is not the child at 6 p.m."],
      ["Attribution", "A child with cerebral palsy: new signs attributed to the known condition.", "Assume a new symptom has a new cause until proven otherwise."]]) + pearl('''<p><b>The diagnostic time-out.</b> Before leaving any sick child, ask: What is my diagnosis? What does not fit? What is the worst thing this could be, and have I excluded it? What must happen if the child worsens, and who will do it? Thirty seconds. It catches more errors than any checklist you will be given.</p>'''), tier="nice", lvl="x"),
  ],
  [Q("A 6-month-old with bronchiolitis has had severe recession for six hours. On review the recession is less marked, the respiratory rate has fallen from 70 to 34/min, and the infant is sleepy and not feeding. SpO₂ is 92% on oxygen. What is the most appropriate interpretation?",
     ["Improving &mdash; wean the oxygen and reassess in four hours.",
      "A normal sleep pattern for age; document and continue observations.",
      "Impending respiratory failure from fatigue &mdash; escalate now.",
      "A response to bronchodilator therapy; continue nebulisation."],
     2,
     "What does a falling respiratory rate mean when the level of consciousness is falling with it?",
     "Put the three changes together: less recession, a much slower rate, and a sleepier infant who will not feed. Does a recovering infant become <i>less</i> interested in feeding?",
     "In an infant who has been working hard for hours, <b>less effort plus a falling rate plus a falling level of consciousness is exhaustion</b> &mdash; decompensation. An SpO₂ of 92% <i>on oxygen</i> is not reassuring: it means the oxygen is barely keeping up. This infant needs respiratory support, a blood gas and senior review now.",
     "<b>A</b> &mdash; recovery brings a calmer infant who feeds; this one is less able to feed. <b>B</b> &mdash; attributing a change to sleep is exactly the error this unit warns about. <b>D</b> &mdash; bronchodilators have little role in bronchiolitis, and a response to them would not produce drowsiness and refusal to feed.",
     "&ldquo;Settling&rdquo; is a word to distrust in a child who was struggling. Ask what made them settle.",
     "section 2, ‘Breathing’"),
   Q("A 2-month-old brought in with a week of cough and poor feeding has a heart rate of 54/min, is mottled and barely responsive. SpO₂ does not register. What is the first intervention?",
     ["Open the airway and give effective bag-mask ventilation with oxygen.",
      "IV atropine 0.02 mg/kg.",
      "Transcutaneous pacing.",
      "IV adenosine 0.1 mg/kg."],
     0,
     "In infants, what is the commonest cause of a slow heart?",
     "Infant cardiac output is rate-dependent, and bradycardia in a sick infant is usually hypoxic. Which option treats the cause rather than the number?",
     "Bradycardia with poor perfusion in an infant is <b>hypoxic until proven otherwise</b>, and because infant output depends on rate it is functionally an arrest state. <b>Oxygenate and ventilate first.</b> If the heart rate stays below 60/min with poor perfusion despite effective ventilation, start chest compressions and give epinephrine (PALS 2025).",
     "<b>B</b> &mdash; atropine is for vagally mediated bradycardia or primary AV block; it does not fix hypoxia. <b>C</b> &mdash; pacing is for specific conduction problems, not asphyxial bradycardia. <b>D</b> &mdash; adenosine treats supraventricular tachycardia; given here it would worsen things.",
     "In paediatrics, the answer to a slow heart is almost always the airway.",
     "section 3, ‘Circulation’")]
)
