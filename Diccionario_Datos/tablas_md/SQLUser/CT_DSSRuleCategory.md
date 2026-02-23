# SQLUser.CT_DSSRuleCategory

**Schema:** SQLUser
**Columnas:** 218
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DSSRULCAT_RowId | bigint | PK |  | NO | - |
| DSSRULCAT_Code | varchar |  |  | NO | Code |
| DSSRULCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DSSRULCAT_CreatedDate | date |  |  | SI | Created Date |
| DSSRULCAT_CreatedTime | time |  |  | SI | Created Time |
| DSSRULCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DSSRULCAT_DateFrom | date |  |  | SI | Date From |
| DSSRULCAT_DateTo | date |  |  | SI | Date To |
| DSSRULCAT_Desc | varchar |  |  | NO | Description |
| DSSRULCAT_Owner | varchar |  |  | SI | Owner |
| DSSRULCAT_UpdatedDate | date |  |  | SI | Updated Date |
| DSSRULCAT_UpdatedTime | time |  |  | SI | Updated Time |
| DSSRULCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Method of analgesia |
| Q02 | - |  |  | SI | If any entry is selected (aside from Intravenous, ... |
| Q03 | - |  |  | SI | Date of insertion |
| Q04 | - |  |  | SI | Time of insertion |
| Q05 | - |  |  | SI | Insertion site |
| Q06 | - |  |  | SI | Insertion site details |
| Q07 | - |  |  | SI | Depth to space (cm) |
| Q08 | - |  |  | SI | Marking at skin (cm) |
| Q09 | - |  |  | SI | ASA status |
| Q10 | - |  |  | SI | Epidural removal date |
| Q100 | - |  |  | SI | • Hypotension – systolic BP < 90 |
| Q101 | - |  |  | SI | • Oxygen saturations < 90% |
| Q102 | - |  |  | SI | • Excessive sedation – score of ≥2 |
| Q103 | - |  |  | SI | • Temp > 38 |
| Q104 | - |  |  | SI | • Inadequate analgesia |
| Q105 | - |  |  | SI | • Excessive nausea / vomiting |
| Q106 | - |  |  | SI | • Dermatome above T4 (xiphisternum) |
| Q107 | - |  |  | SI | • Urinary retention (to home team) |
| Q108 | - |  |  | SI | • Bromage score > 1 |
| Q109 | - |  |  | SI | • Paraesthesia upper / lower limbs |
| Q11 | - |  |  | SI | Epidural removal time |
| Q110 | - |  |  | SI | SPECIAL INSTRUCTIONS |
| Q111 | - |  |  | SI | • 2/24 position changes |
| Q112 | - |  |  | SI | • 4/24 motor / sensation observations 24 hours pos... |
| Q113 | - |  |  | SI | Have available: |
| Q114 | - |  |  | SI | • Atropine 1.2 mgs |
| Q115 | - |  |  | SI | • Ephedrine 30 mgs |
| Q116 | - |  |  | SI | • Naloxone 0.4 mgs |
| Q117 | - |  |  | SI | • Oxygen & Airviva resuscitator bag |
| Q118 | - |  |  | SI | COMPLICATIONS & ACTIONS |
| Q119 | - |  |  | SI | LOCAL ANAESTHETIXC TOXICITY |
| Q12 | - |  |  | SI | Catheter tip intact |
| Q120 | - |  |  | SI | Patient reports of perioral tingling, tinnitus, me... |
| Q121 | - |  |  | SI | 1. Stop infusion. Call for help – MET call |
| Q122 | - |  |  | SI | 2. BLS regime - ABC and 100% O2 |
| Q123 | - |  |  | SI | 3. Confirm IV access |
| Q124 | - |  |  | SI | 4. BLS/ALS as necessary |
| Q125 | - |  |  | SI | 5. Benzodiazepines for convulsions |
| Q126 | - |  |  | SI | Obtain bottle Intralipid from either Operating The... |
| Q127 | - |  |  | SI | HYPOTENSION WITH EPIDURAL IN PROGRESS |
| Q128 | - |  |  | SI | Systolic BP < 90 mm Hg |
| Q129 | - |  |  | SI | 1. Stop infusion |
| Q13 | - |  |  | SI | If catheter tip not intact report to Acute Pain Se... |
| Q130 | - |  |  | SI | 2. Ensure oxygen is administered |
| Q131 | - |  |  | SI | 3. Elevate legs |
| Q132 | - |  |  | SI | 4. Turn obstetric patient to lateral position |
| Q133 | - |  |  | SI | 5. MET call |
| Q134 | - |  |  | SI | 6. Prepare to administer Hartmann’s solution |
| Q135 | - |  |  | SI | SEDATION SCORE 2 and RR ≥ 8 |
| Q136 | - |  |  | SI | 1. Remove PCA button if in in situ until patient i... |
| Q137 | - |  |  | SI | 2. Decrease PCA if in in situ |
| Q138 | - |  |  | SI | 3. Contact APS |
| Q139 | - |  |  | SI | SEDATION SCORE ≥ 2 and RR < 8 |
| Q14 | - |  |  | SI | Discharge from Acute Pain Service date	 |
| Q140 | - |  |  | SI | 1. MET call |
| Q141 | - |  |  | SI | 2. Remove PCA button |
| Q142 | - |  |  | SI | 3. Ensure O2 in situ |
| Q143 | - |  |  | SI | 4. Prepare to administer naloxone |
| Q144 | - |  |  | SI | 5. Notify APS |
| Q145 | - |  |  | SI | SEDATION SCORE 3 |
| Q146 | - |  |  | SI | 1. MET call & Notify APS |
| Q147 | - |  |  | SI | 2. Ensure Oxygen in situ |
| Q148 | - |  |  | SI | 3. Prepare to administer naloxone |
| Q149 | - |  |  | SI | For paediatrics: Stop infusion, administer 02 at 6... |
| Q15 | - |  |  | SI | 24 hours post Acute Pain Service discharge date ch... |
| Q150 | - |  |  | SI | FACES Scale |
| Q151 | - |  |  | SI | A higher score indicates a more severe pain |
| Q152 | - |  |  | SI | Face |
| Q153 | - |  |  | SI | Restlessness |
| Q154 | - |  |  | SI | Muscle Tone |
| Q155 | - |  |  | SI | Vocalisation |
| Q156 | - |  |  | SI | Consolability |
| Q157 | - |  |  | SI | Score |
| Q158 | - |  |  | SI | Score |
| Q159 | - |  |  | SI | Classification |
| Q16 | - |  |  | SI | Back pain / site |
| Q160 | - |  |  | SI | The behavioural rating scale for pain is designed ... |
| Q161 | - |  |  | SI | 0 - 10 |
| Q162 | - |  |  | SI | 0 - 10 |
| Q163 | - |  |  | SI | A higher score indicates a more severe pain |
| Q164 | - |  |  | SI | 0 - 10: A higher score indicates a more severe pai... |
| Q165 | - |  |  | SI | Date |
| Q166 | - |  |  | SI | Time |
| Q17 | - |  |  | SI | Back pain / site comments |
| Q18 | - |  |  | SI | Motor |
| Q19 | - |  |  | SI | Motor comments |
| Q20 | - |  |  | SI | Sensory |
| Q21 | - |  |  | SI | Sensory comments |
| Q22 | - |  |  | SI | Bladder / Bowel control |
| Q23 | - |  |  | SI | Bladder / Bowel control comments |
| Q24 | - |  |  | SI | Discharge advice |
| Q25 | - |  |  | SI | Discharge advice comments |
| Q26 | - |  |  | SI | Discharge card |
| Q27 | - |  |  | SI | Discharge card comments |
| Q28 | - |  |  | SI | Special follow up instructions (if any) |
| Q30 | - |  |  | SI | Face |
| Q31 | - |  |  | SI | Restlessness |
| Q32 | - |  |  | SI | Muscle tone |
| Q33 | - |  |  | SI | Vocalisation |
| Q34 | - |  |  | SI | Consolability |
| Q35 | - |  |  | SI | Score |
| Q36 | - |  |  | SI | Score |
| Q37 | - |  |  | SI | Classification |
| Q38 | - |  |  | SI | 0 |
| Q39 | - |  |  | SI | No hurt |
| Q40 | - |  |  | SI | 1 - 2 |
| Q41 | - |  |  | SI | Hurts little bit |
| Q42 | - |  |  | SI | 3 - 4 |
| Q43 | - |  |  | SI | Hurts little more |
| Q44 | - |  |  | SI | 5 - 6 |
| Q45 | - |  |  | SI | Hurts even more |
| Q46 | - |  |  | SI | 7 - 8 |
| Q47 | - |  |  | SI | Hurts whole lot |
| Q48 | - |  |  | SI | 9 - 10 |
| Q49 | - |  |  | SI | Hurts worst |
| Q50 | - |  |  | SI | The behavioural rating scale for pain is designed ... |
| Q51 | - |  |  | SI | 0: No hurt |
| Q52 | - |  |  | SI | 1 - 2: Hurts little bit |
| Q53 | - |  |  | SI | 3 - 4: Hurts little more |
| Q54 | - |  |  | SI | 5 - 6: Hurts even more |
| Q55 | - |  |  | SI | 7 - 8: Hurts whole lot |
| Q56 | - |  |  | SI | 9 - 10: Hurts worst |
| Q57 | - |  |  | SI | PAIN SCORE TOOLS |
| Q58 | - |  |  | SI | NRS - numerical rating scale (0-10) OR Wong-Baker ... |
| Q59 | - |  |  | SI | OR Verbal Pain Intensity Scale (Mild-Severe) OR Be... |
| Q60 | - |  |  | SI | AND Functional Activity Score ( A-C) |
| Q61 | - |  |  | SI | PARENTERAL NARCOTIC ADMINISTRATION |
| Q62 | - |  |  | SI | (infusion, PCA, S/C) |
| Q63 | - |  |  | SI | Initial and after bolus or increased rate: |
| Q64 | - |  |  | SI | • Respiratory rate – 1/24 x 12 then 2/24 |
| Q65 | - |  |  | SI | • Sedation score – 1/24 x 12 then 2/24 |
| Q66 | - |  |  | SI | • Pain score – when awake |
| Q67 | - |  |  | SI | o During observations, and if |
| Q68 | - |  |  | SI | o Clinical condition changes |
| Q69 | - |  |  | SI | • Pulse & BP – 4/24 unless clinically indicated |
| Q70 | - |  |  | SI | • Pulse oximetry – during observations |
| Q71 | - |  |  | SI | REPORTABLE OBSERVATIONS TO APS |
| Q72 | - |  |  | SI | • Excessive sedation – score of 2 |
| Q73 | - |  |  | SI | • Inadequate analgesia |
| Q74 | - |  |  | SI | • Excessive nausea / vomiting |
| Q75 | - |  |  | SI | MET call & Notify APS |
| Q76 | - |  |  | SI | • Respiratory rate < 8 / minute (taken for a whole... |
| Q77 | - |  |  | SI | • Sedation score 3 |
| Q78 | - |  |  | SI | REGIONAL BLOCKS |
| Q79 | - |  |  | SI | (TAP block, extrapleural, nerve block) |
| Q80 | - |  |  | SI | • 4/24 vital signs after RPAO |
| Q81 | - |  |  | SI | • Awareness of local anaesthetic toxicity |
| Q82 | - |  |  | SI | • Site – check once per shift and if pain or leaki... |
| Q83 | - |  |  | SI | • Following bolus - BP and Pulse within 5 minutes ... |
| Q84 | - |  |  | SI | EPIDURAL ADMINISTRATION |
| Q85 | - |  |  | SI | (Local Anaesthetic +/- Narcotic) |
| Q86 | - |  |  | SI | Initial and after bolus or increased rate: |
| Q87 | - |  |  | SI | • Respiratory rate – 1/24 x 12 then 2/24 |
| Q88 | - |  |  | SI | • Pulse & BP – 5/60 x 4, then 4/24 after Routine P... |
| Q89 | - |  |  | SI | Anaesthetic Observations (RPAO) |
| Q90 | - |  |  | SI | • Sedation score – 1/24 x 12 then 2/24 |
| Q91 | - |  |  | SI | • Pain score – when awake |
| Q92 | - |  |  | SI | o During observations, and if |
| Q93 | - |  |  | SI | o Clinical condition changes |
| Q94 | - |  |  | SI | • Pulse oximetry – during observations |
| Q95 | - |  |  | SI | • Dermatome assessment – 8/24, if pain increases &... |
| Q96 | - |  |  | SI | • Bromage score (Motor function) – 4/24 |
| Q97 | - |  |  | SI | • Paraesthesia (Sensation) – 4/24 |
| Q98 | - |  |  | SI | REPORTABLE OBSERVATIONS TO APS |
| Q99 | - |  |  | SI | • Resp rate < 8 / minute (taken for a whole minute... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*