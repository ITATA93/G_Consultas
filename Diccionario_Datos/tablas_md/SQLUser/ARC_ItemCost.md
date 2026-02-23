# SQLUser.ARC_ItemCost

**Schema:** SQLUser
**Columnas:** 235
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITCOST_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| ITCOST_Childsub | double |  |  | NO | Childsub |
| ITCOST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITCOST_Cost | double |  |  | NO | Cost |
| ITCOST_CreatedDate | date |  |  | SI | Created Date |
| ITCOST_CreatedTime | time |  |  | SI | Created Time |
| ITCOST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITCOST_DateFrom | date |  |  | NO | Date From |
| ITCOST_DateTo | date |  |  | SI | Date To |
| ITCOST_DoctorPerc | double |  |  | SI | Doctor % |
| ITCOST_Hospital_DR | bigint |  | FK | SI | Hospital |
| ITCOST_RowId | varchar |  |  | NO | - |
| ITCOST_UpdatedDate | date |  |  | SI | Updated Date |
| ITCOST_UpdatedTime | time |  |  | SI | Updated Time |
| ITCOST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Height |
| Q03ObsDR | - |  |  | SI | Height DR |
| Q04 | - |  |  | SI | Weight |
| Q04ObsDR | - |  |  | SI | Weight DR |
| Q05 | - |  |  | SI | Medications taken before test |
| Q06 | - |  |  | SI | Gait aid |
| Q07 | - |  |  | SI | O2 Flow rate |
| Q07ObsDR | - |  |  | SI | O2 Flow rate DR |
| Q08 | - |  |  | SI | O2 Delivery mode |
| Q08ObsDR | - |  |  | SI | O2 Delivery mode DR |
| Q09 | - |  |  | SI | Delivery method |
| Q10 | - |  |  | SI | O2 Trolley |
| Q100 | - |  |  | SI | • Read the following instructions to the participa... |
| Q101 | - |  |  | SI | “The object of this test is to walk as far as poss... |
| Q102 | - |  |  | SI | You will probably get out of breath or become exha... |
| Q103 | - |  |  | SI | You will be walking back and forth around the cone... |
| Q104 | - |  |  | SI | Please watch the way I turn without hesitation.” |
| Q105 | - |  |  | SI | • Demonstrate by walking one lap yourself. Walk an... |
| Q106 | - |  |  | SI | • Record completed and partial laps on the lap cou... |
| Q107 | - |  |  | SI | • Say to the participant: |
| Q108 | - |  |  | SI | “Are you ready to do that? I am going to use this ... |
| Q109 | - |  |  | SI | Remember that the object is to walk AS FAR AS POSS... |
| Q11 | - |  |  | SI | Baseline  (pre test after 10 min of rest) |
| Q110 | - |  |  | SI | DURING TEST |
| Q111 | - |  |  | SI | • Standardised Encouragement read in a steady voic... |
| Q112 | - |  |  | SI | • After the 1st minute: |
| Q113 | - |  |  | SI | “You are doing well. You have 5 minutes to go.” |
| Q114 | - |  |  | SI | • When the timer shows 4 minutes remaining: |
| Q115 | - |  |  | SI | “Keep up the good work. You have 4 minutes to go.” |
| Q116 | - |  |  | SI | • When the timer shows 3 minutes remaining: |
| Q117 | - |  |  | SI | “You are doing well. You are halfway done. |
| Q118 | - |  |  | SI | • When the timer shows 2 minutes remaining: |
| Q119 | - |  |  | SI | “Keep up the good work. You have only 2 minutes le... |
| Q12 | - |  |  | SI | End of Test (EOT) |
| Q120 | - |  |  | SI | • When the timer shows 1 minute remaining: |
| Q121 | - |  |  | SI | “You are doing well. You only have 1 minute to go. |
| Q122 | - |  |  | SI | • With 15 seconds to go: |
| Q123 | - |  |  | SI | “In a moment I’m going to tell you to stop. When I... |
| Q124 | - |  |  | SI | • At 6 minutes: |
| Q125 | - |  |  | SI | “Stop” |
| Q126 | - |  |  | SI | • If the participant stops at any time prior, you ... |
| Q127 | - |  |  | SI | “You can lean against the wall if you would like |
| Q128 | - |  |  | SI | • Do not use other words of encouragement (or body... |
| Q129 | - |  |  | SI | • If available record the distance at which the ox... |
| Q13 | - |  |  | SI | EOT + 2 min |
| Q130 | - |  |  | SI | The test should be immediately stopped if: |
| Q131 | - |  |  | SI | • SpO2 falls below 80% |
| Q132 | - |  |  | SI | • The participant asks to stop the test |
| Q133 | - |  |  | SI | • The participant experiences chest pain |
| Q134 | - |  |  | SI | • Intolerable dyspnoea |
| Q135 | - |  |  | SI | • Leg cramps |
| Q136 | - |  |  | SI | • Leg cramps |
| Q137 | - |  |  | SI | • Staggering |
| Q138 | - |  |  | SI | • Diaphoresis |
| Q139 | - |  |  | SI | • Pale or ashen appearance |
| Q14 | - |  |  | SI | EOT + 5 min |
| Q140 | - |  |  | SI | Parameter |
| Q141 | - |  |  | SI | HR (per min) |
| Q142 | - |  |  | SI | HR (per min) |
| Q143 | - |  |  | SI | HR (per min) |
| Q144 | - |  |  | SI | HR (per min) |
| Q145 | - |  |  | SI | HR (per min) |
| Q146 | - |  |  | SI | HR (per min) |
| Q147 | - |  |  | SI | HR (per min) |
| Q148 | - |  |  | SI | HR (per min) |
| Q149 | - |  |  | SI | HR (per min) |
| Q15 | - |  |  | SI | BP (mmHg) |
| Q150 | - |  |  | SI | SpO2 (%) |
| Q151 | - |  |  | SI | SpO2 (%) |
| Q152 | - |  |  | SI | SpO2 (%) |
| Q153 | - |  |  | SI | SpO2 (%) |
| Q154 | - |  |  | SI | SpO2 (%) |
| Q155 | - |  |  | SI | SpO2 (%) |
| Q156 | - |  |  | SI | SpO2 (%) |
| Q157 | - |  |  | SI | SpO2 (%) |
| Q158 | - |  |  | SI | SpO2 (%) |
| Q159 | - |  |  | SI | RR (per min) |
| Q16 | - |  |  | SI | HR (per min) |
| Q160 | - |  |  | SI | RR (per min) |
| Q161 | - |  |  | SI | RR (per min) |
| Q162 | - |  |  | SI | RR (per min) |
| Q163 | - |  |  | SI | BP (mmHg) |
| Q164 | - |  |  | SI | BP (mmHg) |
| Q165 | - |  |  | SI | BP (mmHg) |
| Q166 | - |  |  | SI | BP (mmHg) |
| Q167 | - |  |  | SI | Dyspnoea (Burdon's Modified Borg Scale) |
| Q168 | - |  |  | SI | Dyspnoea (Burdon's Modified Borg Scale) |
| Q169 | - |  |  | SI | Dyspnoea (Burdon's Modified Borg Scale) |
| Q17 | - |  |  | SI | RR (per min) |
| Q170 | - |  |  | SI | Dyspnoea (Burdon's Modified Borg Scale) |
| Q171 | - |  |  | SI | Fatigue (Borg CR10 Scale®) |
| Q172 | - |  |  | SI | Fatigue (Borg CR10 Scale®) |
| Q173 | - |  |  | SI | Fatigue (Borg CR10 Scale®) |
| Q174 | - |  |  | SI | Fatigue (Borg CR10 Scale®) |
| Q175 | - |  |  | SI | Total time stopped (seconds) |
| Q18 | - |  |  | SI | SpO2 (%) |
| Q19 | - |  |  | SI | Dyspnoea (BORG 10) |
| Q20 | - |  |  | SI | Fatigue (BORG 20) |
| Q21 | - |  |  | SI | Baseline BP |
| Q22 | - |  |  | SI | Baseline HR |
| Q23 | - |  |  | SI | Baseline RR |
| Q24 | - |  |  | SI | Baseline SpO2 |
| Q25 | - |  |  | SI | Dyspnoea, Baseline (Burdon's Modified Borg Scale) |
| Q26 | - |  |  | SI | Fatigue, Baseline (Borg CR10 Scale®) |
| Q27 | - |  |  | SI | EOT BP |
| Q28 | - |  |  | SI | EOT HR |
| Q29 | - |  |  | SI | EOT RR |
| Q30 | - |  |  | SI | EOT SpO2 |
| Q31 | - |  |  | SI | Dyspnoea, EOT (Burdon's Modified Borg Scale) |
| Q32 | - |  |  | SI | Fatigue, EOT (Borg CR10 Scale®) |
| Q33 | - |  |  | SI | EOT + 2 min BP |
| Q34 | - |  |  | SI | EOT + 2 min HR |
| Q35 | - |  |  | SI | EOT + 2 min RR |
| Q36 | - |  |  | SI | EOT + 2 min SpO2 |
| Q37 | - |  |  | SI | Dyspnoea, EOT + 2 min (Burdon's Modified Borg Scal... |
| Q38 | - |  |  | SI | Fatigue, EOT + 2 min (Borg CR10 Scale®) |
| Q39 | - |  |  | SI | EOT + 5 min BP |
| Q40 | - |  |  | SI | EOT + 5 min HR |
| Q41 | - |  |  | SI | EOT + 5 min RR |
| Q42 | - |  |  | SI | EOT + 5 min SpO2 |
| Q43 | - |  |  | SI | Dyspnoea, EOT + 5 min (Burdon's Modified Borg Scal... |
| Q44 | - |  |  | SI | Fatigue, EOT + 5 min (Borg CR10 Scale®) |
| Q45 | - |  |  | SI | Symptoms  comment |
| Q46 | - |  |  | SI | Distance in meters |
| Q47 | - |  |  | SI | Lowest SpO2 |
| Q48 | - |  |  | SI | Number of stops |
| Q49 | - |  |  | SI | Total time stopped |
| Q50 | - |  |  | SI | Comments |
| Q51 | - |  |  | SI | Has a resting electrocardiogram taken in the previ... |
| Q52 | - |  |  | SI | Do not proceed with test if: |
| Q53 | - |  |  | SI | • Systolic BP is greater than 200 mmHg |
| Q54 | - |  |  | SI | • Systolic BP less than 60 mmHg |
| Q55 | - |  |  | SI | • Diastolic BP is greater than 110 mmHg |
| Q56 | - |  |  | SI | • SpO2 is less than 80% |
| Q57 | - |  |  | SI | • Resting heart rate (HR) is greater than 120 beat... |
| Q58 | - |  |  | SI | • Resting HR is less than 50 beats per minute |
| Q59 | - |  |  | SI | Reason test not undertaken |
| Q60 | - |  |  | SI | Supplemental oxygen for test |
| Q61 | - |  |  | SI | Continuous pulse oximetry recorded |
| Q62 | - |  |  | SI | Time of baseline observations |
| Q63 | - |  |  | SI | Blood pressure must be recorded no more than 4 hou... |
| Q64 | - |  |  | SI | Time test started |
| Q65 | - |  |  | SI | 1 min |
| Q66 | - |  |  | SI | 2 min |
| Q67 | - |  |  | SI | 3 min |
| Q68 | - |  |  | SI | 4 min |
| Q69 | - |  |  | SI | 5 min |
| Q70 | - |  |  | SI | HR (per min) |
| Q71 | - |  |  | SI | SpO2 (%) |
| Q72 | - |  |  | SI | RR (per min) |
| Q73 | - |  |  | SI | BP (mmHg) |
| Q74 | - |  |  | SI | Dyspnoea (Burdon's Modified Borg Scale) |
| Q75 | - |  |  | SI | Fatigue (Borg CR10 Scale®) |
| Q76 | - |  |  | SI | 1 min HR |
| Q77 | - |  |  | SI | 1 min SpO2 |
| Q78 | - |  |  | SI | 2 min HR |
| Q79 | - |  |  | SI | 2 min SpO2 |
| Q80 | - |  |  | SI | 3 min HR |
| Q81 | - |  |  | SI | 3 min SpO2 |
| Q82 | - |  |  | SI | 4 min HR |
| Q83 | - |  |  | SI | 4 min SpO2 |
| Q84 | - |  |  | SI | 5 min HR |
| Q85 | - |  |  | SI | 5 min SpO2 |
| Q86 | - |  |  | SI | Type of course |
| Q87 | - |  |  | SI | Distance of one lap (meters) |
| Q88 | - |  |  | SI | Record the number of completed laps |
| Q89 | - |  |  | SI | Distance walked of the final partial lap (meters) |
| Q90 | - |  |  | SI | Calculated total distance walked (meters) |
| Q91 | - |  |  | SI | Total distance walked (meters) |
| Q91ObsDR | - |  |  | SI | Total distance walked (meters) DR |
| Q92 | - |  |  | SI | Symptoms during test |
| Q93 | - |  |  | SI | Reason for stopping |
| Q94 | - |  |  | SI | Patient's subjective reason for not walking farthe... |
| Q95 | - |  |  | SI | Falls |
| Q96 | - |  |  | SI | Reason for stopping - additional detail |
| Q97 | - |  |  | SI | BEFORE TEST |
| Q98 | - |  |  | SI | • Explain the use of the modified Borg scale (0-10... |
| Q99 | - |  |  | SI | • Explain the use of the Borg rating of perceived ... |
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