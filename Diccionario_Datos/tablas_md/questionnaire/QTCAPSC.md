# questionnaire.QTCAPSC

> Acute Pain Service Chart

**Schema:** questionnaire
**Columnas:** 206
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Acute Pain Service Chart

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Method of analgesia |
| Q02 | varchar |  |  | SI | If any entry is selected (aside from Intravenous, ... |
| Q03 | date |  |  | SI | Date of insertion |
| Q04 | time |  |  | SI | Time of insertion |
| Q05 | varchar |  |  | SI | Insertion site |
| Q06 | varchar |  |  | SI | Insertion site details |
| Q07 | numeric |  |  | SI | Depth to space (cm) |
| Q08 | numeric |  |  | SI | Marking at skin (cm) |
| Q09 | varchar |  |  | SI | ASA status |
| Q10 | date |  |  | SI | Epidural removal date |
| Q100 | varchar |  |  | SI | • Hypotension – systolic BP < 90 |
| Q101 | varchar |  |  | SI | • Oxygen saturations < 90% |
| Q102 | varchar |  |  | SI | • Excessive sedation – score of ≥2 |
| Q103 | varchar |  |  | SI | • Temp > 38 |
| Q104 | varchar |  |  | SI | • Inadequate analgesia |
| Q105 | varchar |  |  | SI | • Excessive nausea / vomiting |
| Q106 | varchar |  |  | SI | • Dermatome above T4 (xiphisternum) |
| Q107 | varchar |  |  | SI | • Urinary retention (to home team) |
| Q108 | varchar |  |  | SI | • Bromage score > 1 |
| Q109 | varchar |  |  | SI | • Paraesthesia upper / lower limbs |
| Q11 | time |  |  | SI | Epidural removal time |
| Q110 | varchar |  |  | SI | SPECIAL INSTRUCTIONS |
| Q111 | varchar |  |  | SI | • 2/24 position changes |
| Q112 | varchar |  |  | SI | • 4/24 motor / sensation observations 24 hours pos... |
| Q113 | varchar |  |  | SI | Have available: |
| Q114 | varchar |  |  | SI | • Atropine 1.2 mgs |
| Q115 | varchar |  |  | SI | • Ephedrine 30 mgs |
| Q116 | varchar |  |  | SI | • Naloxone 0.4 mgs |
| Q117 | varchar |  |  | SI | • Oxygen & Airviva resuscitator bag |
| Q118 | varchar |  |  | SI | COMPLICATIONS & ACTIONS |
| Q119 | varchar |  |  | SI | LOCAL ANAESTHETIXC TOXICITY |
| Q12 | varchar |  |  | SI | Catheter tip intact |
| Q120 | varchar |  |  | SI | Patient reports of perioral tingling, tinnitus, me... |
| Q121 | varchar |  |  | SI | 1. Stop infusion. Call for help – MET call |
| Q122 | varchar |  |  | SI | 2. BLS regime - ABC and 100% O2 |
| Q123 | varchar |  |  | SI | 3. Confirm IV access |
| Q124 | varchar |  |  | SI | 4. BLS/ALS as necessary |
| Q125 | varchar |  |  | SI | 5. Benzodiazepines for convulsions |
| Q126 | varchar |  |  | SI | Obtain bottle Intralipid from either Operating The... |
| Q127 | varchar |  |  | SI | HYPOTENSION WITH EPIDURAL IN PROGRESS |
| Q128 | varchar |  |  | SI | Systolic BP < 90 mm Hg |
| Q129 | varchar |  |  | SI | 1. Stop infusion |
| Q13 | varchar |  |  | SI | If catheter tip not intact report to Acute Pain Se... |
| Q130 | varchar |  |  | SI | 2. Ensure oxygen is administered |
| Q131 | varchar |  |  | SI | 3. Elevate legs |
| Q132 | varchar |  |  | SI | 4. Turn obstetric patient to lateral position |
| Q133 | varchar |  |  | SI | 5. MET call |
| Q134 | varchar |  |  | SI | 6. Prepare to administer Hartmann’s solution |
| Q135 | varchar |  |  | SI | SEDATION SCORE 2 and RR ≥ 8 |
| Q136 | varchar |  |  | SI | 1. Remove PCA button if in in situ until patient i... |
| Q137 | varchar |  |  | SI | 2. Decrease PCA if in in situ |
| Q138 | varchar |  |  | SI | 3. Contact APS |
| Q139 | varchar |  |  | SI | SEDATION SCORE ≥ 2 and RR < 8 |
| Q14 | date |  |  | SI | Discharge from Acute Pain Service date	 |
| Q140 | varchar |  |  | SI | 1. MET call |
| Q141 | varchar |  |  | SI | 2. Remove PCA button |
| Q142 | varchar |  |  | SI | 3. Ensure O2 in situ |
| Q143 | varchar |  |  | SI | 4. Prepare to administer naloxone |
| Q144 | varchar |  |  | SI | 5. Notify APS |
| Q145 | varchar |  |  | SI | SEDATION SCORE 3 |
| Q146 | varchar |  |  | SI | 1. MET call & Notify APS |
| Q147 | varchar |  |  | SI | 2. Ensure Oxygen in situ |
| Q148 | varchar |  |  | SI | 3. Prepare to administer naloxone |
| Q149 | varchar |  |  | SI | For paediatrics: Stop infusion, administer 02 at 6... |
| Q15 | varchar |  |  | SI | 24 hours post Acute Pain Service discharge date ch... |
| Q150 | varchar |  |  | SI | FACES Scale |
| Q151 | varchar |  |  | SI | A higher score indicates a more severe pain |
| Q152 | varchar |  |  | SI | Face |
| Q153 | varchar |  |  | SI | Restlessness |
| Q154 | varchar |  |  | SI | Muscle Tone |
| Q155 | varchar |  |  | SI | Vocalisation |
| Q156 | varchar |  |  | SI | Consolability |
| Q157 | varchar |  |  | SI | Score |
| Q158 | varchar |  |  | SI | Score |
| Q159 | varchar |  |  | SI | Classification |
| Q16 | bit |  |  | SI | Back pain / site |
| Q160 | varchar |  |  | SI | The behavioural rating scale for pain is designed ... |
| Q161 | varchar |  |  | SI | 0 - 10 |
| Q162 | varchar |  |  | SI | 0 - 10 |
| Q163 | varchar |  |  | SI | A higher score indicates a more severe pain |
| Q164 | varchar |  |  | SI | 0 - 10: A higher score indicates a more severe pai... |
| Q165 | date |  |  | SI | Date |
| Q166 | time |  |  | SI | Time |
| Q17 | varchar |  |  | SI | Back pain / site comments |
| Q18 | bit |  |  | SI | Motor |
| Q19 | varchar |  |  | SI | Motor comments |
| Q20 | bit |  |  | SI | Sensory |
| Q21 | varchar |  |  | SI | Sensory comments |
| Q22 | bit |  |  | SI | Bladder / Bowel control |
| Q23 | varchar |  |  | SI | Bladder / Bowel control comments |
| Q24 | bit |  |  | SI | Discharge advice |
| Q25 | varchar |  |  | SI | Discharge advice comments |
| Q26 | bit |  |  | SI | Discharge card |
| Q27 | varchar |  |  | SI | Discharge card comments |
| Q28 | varchar |  |  | SI | Special follow up instructions (if any) |
| Q30 | varchar |  |  | SI | Face |
| Q31 | varchar |  |  | SI | Restlessness |
| Q32 | varchar |  |  | SI | Muscle tone |
| Q33 | varchar |  |  | SI | Vocalisation |
| Q34 | varchar |  |  | SI | Consolability |
| Q35 | varchar |  |  | SI | Score |
| Q36 | varchar |  |  | SI | Score |
| Q37 | varchar |  |  | SI | Classification |
| Q38 | varchar |  |  | SI | 0 |
| Q39 | varchar |  |  | SI | No hurt |
| Q40 | varchar |  |  | SI | 1 - 2 |
| Q41 | varchar |  |  | SI | Hurts little bit |
| Q42 | varchar |  |  | SI | 3 - 4 |
| Q43 | varchar |  |  | SI | Hurts little more |
| Q44 | varchar |  |  | SI | 5 - 6 |
| Q45 | varchar |  |  | SI | Hurts even more |
| Q46 | varchar |  |  | SI | 7 - 8 |
| Q47 | varchar |  |  | SI | Hurts whole lot |
| Q48 | varchar |  |  | SI | 9 - 10 |
| Q49 | varchar |  |  | SI | Hurts worst |
| Q50 | varchar |  |  | SI | The behavioural rating scale for pain is designed ... |
| Q51 | varchar |  |  | SI | 0: No hurt |
| Q52 | varchar |  |  | SI | 1 - 2: Hurts little bit |
| Q53 | varchar |  |  | SI | 3 - 4: Hurts little more |
| Q54 | varchar |  |  | SI | 5 - 6: Hurts even more |
| Q55 | varchar |  |  | SI | 7 - 8: Hurts whole lot |
| Q56 | varchar |  |  | SI | 9 - 10: Hurts worst |
| Q57 | varchar |  |  | SI | PAIN SCORE TOOLS |
| Q58 | varchar |  |  | SI | NRS - numerical rating scale (0-10) OR Wong-Baker ... |
| Q59 | varchar |  |  | SI | OR Verbal Pain Intensity Scale (Mild-Severe) OR Be... |
| Q60 | varchar |  |  | SI | AND Functional Activity Score ( A-C) |
| Q61 | varchar |  |  | SI | PARENTERAL NARCOTIC ADMINISTRATION |
| Q62 | varchar |  |  | SI | (infusion, PCA, S/C) |
| Q63 | varchar |  |  | SI | Initial and after bolus or increased rate: |
| Q64 | varchar |  |  | SI | • Respiratory rate – 1/24 x 12 then 2/24 |
| Q65 | varchar |  |  | SI | • Sedation score – 1/24 x 12 then 2/24 |
| Q66 | varchar |  |  | SI | • Pain score – when awake |
| Q67 | varchar |  |  | SI | o During observations, and if |
| Q68 | varchar |  |  | SI | o Clinical condition changes |
| Q69 | varchar |  |  | SI | • Pulse & BP – 4/24 unless clinically indicated |
| Q70 | varchar |  |  | SI | • Pulse oximetry – during observations |
| Q71 | varchar |  |  | SI | REPORTABLE OBSERVATIONS TO APS |
| Q72 | varchar |  |  | SI | • Excessive sedation – score of 2 |
| Q73 | varchar |  |  | SI | • Inadequate analgesia |
| Q74 | varchar |  |  | SI | • Excessive nausea / vomiting  |
| Q75 | varchar |  |  | SI | MET call & Notify APS |
| Q76 | varchar |  |  | SI | • Respiratory rate < 8 / minute (taken for a whole... |
| Q77 | varchar |  |  | SI | • Sedation score 3 |
| Q78 | varchar |  |  | SI | REGIONAL BLOCKS |
| Q79 | varchar |  |  | SI | (TAP block, extrapleural, nerve block) |
| Q80 | varchar |  |  | SI | • 4/24 vital signs after RPAO |
| Q81 | varchar |  |  | SI | • Awareness of local anaesthetic toxicity |
| Q82 | varchar |  |  | SI | • Site – check once per shift and if pain or leaki... |
| Q83 | varchar |  |  | SI | • Following bolus - BP and Pulse within 5 minutes ... |
| Q84 | varchar |  |  | SI | EPIDURAL ADMINISTRATION |
| Q85 | varchar |  |  | SI | (Local Anaesthetic +/- Narcotic) |
| Q86 | varchar |  |  | SI | Initial and after bolus or increased rate: |
| Q87 | varchar |  |  | SI | • Respiratory rate – 1/24 x 12 then 2/24 |
| Q88 | varchar |  |  | SI | • Pulse & BP – 5/60 x 4, then 4/24 after Routine P... |
| Q89 | varchar |  |  | SI | Anaesthetic Observations (RPAO) |
| Q90 | varchar |  |  | SI | • Sedation score – 1/24 x 12 then 2/24 |
| Q91 | varchar |  |  | SI | • Pain score – when awake |
| Q92 | varchar |  |  | SI | o During observations, and if |
| Q93 | varchar |  |  | SI | o Clinical condition changes |
| Q94 | varchar |  |  | SI | • Pulse oximetry – during observations |
| Q95 | varchar |  |  | SI | • Dermatome assessment – 8/24, if pain increases &... |
| Q96 | varchar |  |  | SI | • Bromage score (Motor function) – 4/24 |
| Q97 | varchar |  |  | SI | • Paraesthesia (Sensation) – 4/24 |
| Q98 | varchar |  |  | SI | REPORTABLE OBSERVATIONS TO APS |
| Q99 | varchar |  |  | SI | • Resp rate < 8 / minute (taken for a whole minute... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*