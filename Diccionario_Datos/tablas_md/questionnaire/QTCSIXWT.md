# questionnaire.QTCSIXWT

> 6 Minute Walk Test

**Schema:** questionnaire
**Columnas:** 221
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* 6 Minute Walk Test

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Height |
| Q03ObsDR | varchar |  | FK | SI | Height DR |
| Q04 | varchar |  |  | SI | Weight |
| Q04ObsDR | varchar |  | FK | SI | Weight DR |
| Q05 | varchar |  |  | SI | Medications taken before test |
| Q06 | varchar |  |  | SI | Gait aid |
| Q07 | varchar |  |  | SI | O2 Flow rate |
| Q07ObsDR | varchar |  | FK | SI | O2 Flow rate DR |
| Q08 | varchar |  |  | SI | O2 Delivery mode |
| Q08ObsDR | varchar |  | FK | SI | O2 Delivery mode DR |
| Q09 | varchar |  |  | SI | Delivery method |
| Q10 | varchar |  |  | SI | O2 Trolley |
| Q100 | varchar |  |  | SI | • Read the following instructions to the participa... |
| Q101 | varchar |  |  | SI | “The object of this test is to walk as far as poss... |
| Q102 | varchar |  |  | SI | You will probably get out of breath or become exha... |
| Q103 | varchar |  |  | SI |  You will be walking back and forth around the con... |
| Q104 | varchar |  |  | SI | Please watch the way I turn without hesitation.” |
| Q105 | varchar |  |  | SI | • Demonstrate by walking one lap yourself. Walk an... |
| Q106 | varchar |  |  | SI | • Record completed and partial laps on the lap cou... |
| Q107 | varchar |  |  | SI | • Say to the participant: |
| Q108 | varchar |  |  | SI | “Are you ready to do that? I am going to use this ... |
| Q109 | varchar |  |  | SI | Remember that the object is to walk AS FAR AS POSS... |
| Q11 | varchar |  |  | SI | Baseline  (pre test after 10 min of rest) |
| Q110 | varchar |  |  | SI | DURING TEST |
| Q111 | varchar |  |  | SI | • Standardised Encouragement read in a steady voic... |
| Q112 | varchar |  |  | SI | • After the 1st minute: |
| Q113 | varchar |  |  | SI | “You are doing well. You have 5 minutes to go.” |
| Q114 | varchar |  |  | SI | • When the timer shows 4 minutes remaining: |
| Q115 | varchar |  |  | SI | “Keep up the good work. You have 4 minutes to go.” |
| Q116 | varchar |  |  | SI | • When the timer shows 3 minutes remaining: |
| Q117 | varchar |  |  | SI | “You are doing well. You are halfway done.'' |
| Q118 | varchar |  |  | SI | • When the timer shows 2 minutes remaining: |
| Q119 | varchar |  |  | SI | “Keep up the good work. You have only 2 minutes le... |
| Q12 | varchar |  |  | SI | End of Test (EOT) |
| Q120 | varchar |  |  | SI | • When the timer shows 1 minute remaining: |
| Q121 | varchar |  |  | SI | “You are doing well. You only have 1 minute to go.... |
| Q122 | varchar |  |  | SI | • With 15 seconds to go: |
| Q123 | varchar |  |  | SI | “In a moment I’m going to tell you to stop. When I... |
| Q124 | varchar |  |  | SI | • At 6 minutes: |
| Q125 | varchar |  |  | SI | “Stop” |
| Q126 | varchar |  |  | SI | • If the participant stops at any time prior, you ... |
| Q127 | varchar |  |  | SI | “You can lean against the wall if you would like; ... |
| Q128 | varchar |  |  | SI | • Do not use other words of encouragement (or body... |
| Q129 | varchar |  |  | SI | • If available record the distance at which the ox... |
| Q13 | varchar |  |  | SI | EOT + 2 min |
| Q130 | varchar |  |  | SI | The test should be immediately stopped if: |
| Q131 | varchar |  |  | SI | • SpO2 falls below 80% |
| Q132 | varchar |  |  | SI | • The participant asks to stop the test |
| Q133 | varchar |  |  | SI | • The participant experiences chest pain |
| Q134 | varchar |  |  | SI | • Intolerable dyspnoea |
| Q135 | varchar |  |  | SI | • Leg cramps |
| Q136 | varchar |  |  | SI | • Leg cramps |
| Q137 | varchar |  |  | SI | • Staggering |
| Q138 | varchar |  |  | SI | • Diaphoresis |
| Q139 | varchar |  |  | SI | • Pale or ashen appearance |
| Q14 | varchar |  |  | SI | EOT + 5 min |
| Q140 | varchar |  |  | SI | Parameter |
| Q141 | varchar |  |  | SI | HR (per min) |
| Q142 | varchar |  |  | SI | HR (per min) |
| Q143 | varchar |  |  | SI | HR (per min) |
| Q144 | varchar |  |  | SI | HR (per min) |
| Q145 | varchar |  |  | SI | HR (per min) |
| Q146 | varchar |  |  | SI | HR (per min) |
| Q147 | varchar |  |  | SI | HR (per min) |
| Q148 | varchar |  |  | SI | HR (per min) |
| Q149 | varchar |  |  | SI | HR (per min) |
| Q15 | varchar |  |  | SI | BP (mmHg) |
| Q150 | varchar |  |  | SI | SpO2 (%) |
| Q151 | varchar |  |  | SI | SpO2 (%) |
| Q152 | varchar |  |  | SI | SpO2 (%) |
| Q153 | varchar |  |  | SI | SpO2 (%) |
| Q154 | varchar |  |  | SI | SpO2 (%) |
| Q155 | varchar |  |  | SI | SpO2 (%) |
| Q156 | varchar |  |  | SI | SpO2 (%) |
| Q157 | varchar |  |  | SI | SpO2 (%) |
| Q158 | varchar |  |  | SI | SpO2 (%) |
| Q159 | varchar |  |  | SI | RR (per min) |
| Q16 | varchar |  |  | SI | HR (per min) |
| Q160 | varchar |  |  | SI | RR (per min) |
| Q161 | varchar |  |  | SI | RR (per min) |
| Q162 | varchar |  |  | SI | RR (per min) |
| Q163 | varchar |  |  | SI | BP (mmHg) |
| Q164 | varchar |  |  | SI | BP (mmHg) |
| Q165 | varchar |  |  | SI | BP (mmHg) |
| Q166 | varchar |  |  | SI | BP (mmHg) |
| Q167 | varchar |  |  | SI | Dyspnoea (Burdon's Modified Borg Scale) |
| Q168 | varchar |  |  | SI | Dyspnoea (Burdon's Modified Borg Scale) |
| Q169 | varchar |  |  | SI | Dyspnoea (Burdon's Modified Borg Scale) |
| Q17 | varchar |  |  | SI | RR (per min) |
| Q170 | varchar |  |  | SI | Dyspnoea (Burdon's Modified Borg Scale) |
| Q171 | varchar |  |  | SI | Fatigue (Borg CR10 Scale®) |
| Q172 | varchar |  |  | SI | Fatigue (Borg CR10 Scale®) |
| Q173 | varchar |  |  | SI | Fatigue (Borg CR10 Scale®) |
| Q174 | varchar |  |  | SI | Fatigue (Borg CR10 Scale®) |
| Q175 | numeric |  |  | SI | Total time stopped (seconds) |
| Q18 | varchar |  |  | SI | SpO2 (%) |
| Q19 | varchar |  |  | SI | Dyspnoea (BORG 10) |
| Q20 | varchar |  |  | SI | Fatigue (BORG 20) |
| Q21 | varchar |  |  | SI | Baseline BP |
| Q22 | numeric |  |  | SI | Baseline HR |
| Q23 | numeric |  |  | SI | Baseline RR |
| Q24 | numeric |  |  | SI | Baseline SpO2 |
| Q25 | numeric |  |  | SI | Dyspnoea, Baseline (Burdon's Modified Borg Scale) |
| Q26 | numeric |  |  | SI | Fatigue, Baseline (Borg CR10 Scale®) |
| Q27 | varchar |  |  | SI | EOT BP |
| Q28 | numeric |  |  | SI | EOT HR |
| Q29 | numeric |  |  | SI | EOT RR |
| Q30 | numeric |  |  | SI | EOT SpO2 |
| Q31 | numeric |  |  | SI | Dyspnoea, EOT (Burdon's Modified Borg Scale) |
| Q32 | numeric |  |  | SI | Fatigue, EOT (Borg CR10 Scale®) |
| Q33 | varchar |  |  | SI | EOT + 2 min BP |
| Q34 | numeric |  |  | SI | EOT + 2 min HR |
| Q35 | numeric |  |  | SI | EOT + 2 min RR |
| Q36 | numeric |  |  | SI | EOT + 2 min SpO2 |
| Q37 | numeric |  |  | SI | Dyspnoea, EOT + 2 min (Burdon's Modified Borg Scal... |
| Q38 | numeric |  |  | SI | Fatigue, EOT + 2 min (Borg CR10 Scale®) |
| Q39 | varchar |  |  | SI | EOT + 5 min BP |
| Q40 | numeric |  |  | SI | EOT + 5 min HR |
| Q41 | numeric |  |  | SI | EOT + 5 min RR |
| Q42 | numeric |  |  | SI | EOT + 5 min SpO2 |
| Q43 | numeric |  |  | SI | Dyspnoea, EOT + 5 min (Burdon's Modified Borg Scal... |
| Q44 | numeric |  |  | SI | Fatigue, EOT + 5 min (Borg CR10 Scale®) |
| Q45 | varchar |  |  | SI | Symptoms  comment |
| Q46 | numeric |  |  | SI | Distance in meters |
| Q47 | varchar |  |  | SI | Lowest SpO2 |
| Q48 | numeric |  |  | SI | Number of stops |
| Q49 | varchar |  |  | SI | Total time stopped |
| Q50 | varchar |  |  | SI | Comments |
| Q51 | varchar |  |  | SI | Has a resting electrocardiogram taken in the previ... |
| Q52 | varchar |  |  | SI | Do not proceed with test if: |
| Q53 | varchar |  |  | SI | • Systolic BP is greater than 200 mmHg |
| Q54 | varchar |  |  | SI | • Systolic BP less than 60 mmHg |
| Q55 | varchar |  |  | SI | • Diastolic BP is greater than 110 mmHg |
| Q56 | varchar |  |  | SI | • SpO2 is less than 80% |
| Q57 | varchar |  |  | SI | • Resting heart rate (HR) is greater than 120 beat... |
| Q58 | varchar |  |  | SI | • Resting HR is less than 50 beats per minute |
| Q59 | varchar |  |  | SI | Reason test not undertaken |
| Q60 | varchar |  |  | SI | Supplemental oxygen for test |
| Q61 | varchar |  |  | SI | Continuous pulse oximetry recorded |
| Q62 | time |  |  | SI | Time of baseline observations |
| Q63 | varchar |  |  | SI | Blood pressure must be recorded no more than 4 hou... |
| Q64 | time |  |  | SI | Time test started |
| Q65 | varchar |  |  | SI | 1 min |
| Q66 | varchar |  |  | SI | 2 min |
| Q67 | varchar |  |  | SI | 3 min |
| Q68 | varchar |  |  | SI | 4 min |
| Q69 | varchar |  |  | SI | 5 min |
| Q70 | varchar |  |  | SI | HR (per min) |
| Q71 | varchar |  |  | SI | SpO2 (%) |
| Q72 | varchar |  |  | SI | RR (per min) |
| Q73 | varchar |  |  | SI | BP (mmHg) |
| Q74 | varchar |  |  | SI | Dyspnoea (Burdon's Modified Borg Scale) |
| Q75 | varchar |  |  | SI | Fatigue (Borg CR10 Scale®) |
| Q76 | numeric |  |  | SI | 1 min HR |
| Q77 | numeric |  |  | SI | 1 min SpO2 |
| Q78 | numeric |  |  | SI | 2 min HR |
| Q79 | numeric |  |  | SI | 2 min SpO2 |
| Q80 | numeric |  |  | SI | 3 min HR |
| Q81 | numeric |  |  | SI | 3 min SpO2 |
| Q82 | numeric |  |  | SI | 4 min HR |
| Q83 | numeric |  |  | SI | 4 min SpO2 |
| Q84 | numeric |  |  | SI | 5 min HR |
| Q85 | numeric |  |  | SI | 5 min SpO2 |
| Q86 | varchar |  |  | SI | Type of course |
| Q87 | numeric |  |  | SI | Distance of one lap (meters) |
| Q88 | numeric |  |  | SI | Record the number of completed laps |
| Q89 | numeric |  |  | SI | Distance walked of the final partial lap (meters) |
| Q90 | varchar |  |  | SI | Calculated total distance walked (meters) |
| Q91 | varchar |  |  | SI | Total distance walked (meters) |
| Q91ObsDR | varchar |  | FK | SI | Total distance walked (meters) DR |
| Q92 | varchar |  |  | SI | Symptoms during test |
| Q93 | varchar |  |  | SI | Reason for stopping |
| Q94 | varchar |  |  | SI | Patient's subjective reason for not walking farthe... |
| Q95 | varchar |  |  | SI | Falls |
| Q96 | varchar |  |  | SI | Reason for stopping - additional detail |
| Q97 | varchar |  |  | SI | BEFORE TEST |
| Q98 | varchar |  |  | SI | • Explain the use of the modified Borg scale (0-10... |
| Q99 | varchar |  |  | SI | • Explain the use of the Borg rating of perceived ... |
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