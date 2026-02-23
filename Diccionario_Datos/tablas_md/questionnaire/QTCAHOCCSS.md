# questionnaire.QTCAHOCCSS

> Stroke Screen (Allied Health)

**Schema:** questionnaire
**Columnas:** 184
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Stroke Screen (Allied Health)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | General Presentation |
| Q02 | varchar |  |  | SI | Alertness / Affect / Communication |
| Q03 | varchar |  |  | SI | Hearing |
| Q04 | varchar |  |  | SI | Vision (e.g. Aids used premorbidly & for assessmen... |
| Q05 | varchar |  |  | SI | Diagnosis |
| Q06 | date |  |  | SI | Date of onset |
| Q07 | varchar |  |  | SI | Assessment |
| Q08 | varchar |  |  | SI | Date |
| Q09 | varchar |  |  | SI | Occupational Therapist Name |
| Q10 | varchar |  |  | SI | General |
| Q100 | varchar |  |  | SI | points |
| Q101 | varchar |  |  | SI | points |
| Q102 | varchar |  |  | SI | points |
| Q103 | varchar |  |  | SI | points |
| Q104 | varchar |  |  | SI | points |
| Q105 | varchar |  |  | SI | points |
| Q107 | varchar |  |  | SI | points |
| Q108 | varchar |  |  | SI | Occupational therapist name |
| Q109 | date |  |  | SI | Date |
| Q11 | bit |  |  | SI | Assessment (General) |
| Q110 | longvarbinary |  |  | SI | Signature |
| Q110UDt | date |  |  | SI | Signature Last Updated Date |
| Q110UTm | time |  |  | SI | Signature Last Updated Time |
| Q111 | varchar |  |  | SI | Visual field deficit and visual inattention togeth... |
| Q112 | varchar |  |  | SI | Reading |
| Q113 | varchar |  |  | SI | Cognition |
| Q114 | varchar |  |  | SI | Insight |
| Q115 | varchar |  |  | SI | Language  |
| Q115ObsDR | varchar |  | FK | SI | Language  DR |
| Q116 | varchar |  |  | SI | What would you do if you woke up one minute before... |
| Q117 | varchar |  |  | SI | you had an important meeting / appointment in town... |
| Q118 | varchar |  |  | SI | Cognitive assessment completed |
| Q119 | varchar |  |  | SI | Externally documented cognitive assessments |
| Q12 | date |  |  | SI | Assessment date (General) |
| Q120 | varchar |  |  | SI | Tracking |
| Q121 | varchar |  |  | SI | Vision comments |
| Q122 | varchar |  |  | SI | Agnosia |
| Q123 | varchar |  |  | SI | Agnosia test |
| Q124 | varchar |  |  | SI | Agnosia result |
| Q125 | varchar |  |  | SI | Eye quadrants	 |
| Q126 | date |  |  | SI | Date |
| Q127 | time |  |  | SI | Time |
| Q128 | varchar |  |  | SI | Diagnosis relevant to assessment |
| Q129 | varchar |  |  | SI | Visual attention time held comments |
| Q13 | varchar |  |  | SI | Assessment therapist name (General) |
| Q130 | varchar |  |  | SI | Nystagmus comments |
| Q131 | varchar |  |  | SI | Homonymous hemianopia comments |
| Q132 | varchar |  |  | SI | Visual field deficit and visual inattention togeth... |
| Q133 | varchar |  |  | SI | Other reading |
| Q134 | varchar |  |  | SI | Reading comments |
| Q135 | varchar |  |  | SI | Neglect |
| Q136 | varchar |  |  | SI | Assessment (General) |
| Q137 | varchar |  |  | SI | Assessment (Vision) |
| Q138 | varchar |  |  | SI | Assessment (Cognition) |
| Q139 | varchar |  |  | SI | Assessment (MOCA V.1) |
| Q14 | varchar |  |  | SI | Vision |
| Q140 | varchar |  |  | SI | Assessment (Perception) |
| Q141 | varchar |  |  | SI | Assessment (Upper limb) |
| Q15 | bit |  |  | SI | Assessment (Vision) |
| Q16 | date |  |  | SI | Assessment date (Vision) |
| Q17 | varchar |  |  | SI | Assessment therapist name (Vision) |
| Q18 | varchar |  |  | SI | Cognition |
| Q19 | bit |  |  | SI | Assessment (Cognition) |
| Q20 | date |  |  | SI | Assessment date (Cognition) |
| Q21 | varchar |  |  | SI | Assessment therapist name (Cognition) |
| Q22 | varchar |  |  | SI | MOCA V.1 |
| Q23 | bit |  |  | SI | Assessment (MOCA V.1) |
| Q24 | date |  |  | SI | Assessment date (MOCA V.1) |
| Q25 | varchar |  |  | SI | Assessment therapist name (MOCA V.1) |
| Q26 | varchar |  |  | SI | Perception |
| Q27 | bit |  |  | SI | Assessment (Perception) |
| Q28 | date |  |  | SI | Assessment date (Perception) |
| Q29 | varchar |  |  | SI | Assessment therapist name (Perception) |
| Q30 | varchar |  |  | SI | Upper limb |
| Q31 | bit |  |  | SI | Assessment (Upper limb) |
| Q32 | date |  |  | SI | Assessment date (Upper limb)  |
| Q33 | varchar |  |  | SI | Assessment therapist name (Upper limb)  |
| Q34 | varchar |  |  | SI | Comments (e.g. factors which may influence results... |
| Q35 | varchar |  |  | SI | Vision |
| Q36 | varchar |  |  | SI | Visual attention time held (up to 30 seconds) |
| Q37 | varchar |  |  | SI | Tracking |
| Q38 | varchar |  |  | SI | Nystagmus |
| Q39 | varchar |  |  | SI | Visual fields |
| Q40 | varchar |  |  | SI | Homonymous hemianopia |
| Q47 | varchar |  |  | SI | Impulsivity |
| Q48 | varchar |  |  | SI | Ability to follow commands |
| Q49 | varchar |  |  | SI | 3 Step = “Pick up the pen, place the pen in my han... |
| Q50 | varchar |  |  | SI | 2 Step = “Touch your nose then touch your shoulder |
| Q51 | varchar |  |  | SI | 1 Step = “Pick up the pen” |
| Q52 | varchar |  |  | SI | Problem Solving |
| Q53 | varchar |  |  | SI | What would you do if you woke up one minute before... |
| Q54 | varchar |  |  | SI | Observations (Cognition) |
| Q55 | varchar |  |  | SI | Montreal Cognitive Assessment (MOCA) |
| Q56 | varchar |  |  | SI | Visuospatial / Execute |
| Q56ObsDR | varchar |  | FK | SI | Visuospatial / Execute DR |
| Q57 | varchar |  |  | SI | Naming |
| Q57ObsDR | varchar |  | FK | SI | Naming DR |
| Q58 | varchar |  |  | SI | Memory |
| Q58ObsDR | varchar |  | FK | SI | Memory DR |
| Q59 | varchar |  |  | SI | Attention |
| Q59ObsDR | varchar |  | FK | SI | Attention DR |
| Q60 | varchar |  |  | SI | Abstraction |
| Q60ObsDR | varchar |  | FK | SI | Abstraction DR |
| Q61 | varchar |  |  | SI | Delayed recall |
| Q61ObsDR | varchar |  | FK | SI | Delayed recall DR |
| Q62 | varchar |  |  | SI | Orientation |
| Q62ObsDR | varchar |  | FK | SI | Orientation DR |
| Q63 | varchar |  |  | SI | Sum |
| Q64 | numeric |  |  | SI | Total (MOCA) |
| Q65 | varchar |  |  | SI | Add 1 point if < 12 years education |
| Q66 | varchar |  |  | SI | Perception |
| Q67 | varchar |  |  | SI | Visual Perception |
| Q68 | varchar |  |  | SI | Right / Left discrimination |
| Q69 | varchar |  |  | SI | Form constancy |
| Q70 | varchar |  |  | SI | Depth perception |
| Q71 | varchar |  |  | SI | Figure - Ground |
| Q72 | varchar |  |  | SI | Position in space |
| Q73 | varchar |  |  | SI | Unilateral spatial neglect |
| Q75 | varchar |  |  | SI | Unilateral body neglect |
| Q76 | varchar |  |  | SI | Agnosia |
| Q77 | varchar |  |  | SI | Facial Praxis Task |
| Q78 | varchar |  |  | SI | Cough |
| Q79 | varchar |  |  | SI | Blow out a match |
| Q80 | varchar |  |  | SI | Puff out your cheeks |
| Q81 | varchar |  |  | SI | Limb Praxis Task |
| Q82 | varchar |  |  | SI | Wave goodbye (Right) |
| Q83 | varchar |  |  | SI | Wave goodbye (Left) |
| Q84 | varchar |  |  | SI | Scratch your head (Right) |
| Q85 | varchar |  |  | SI | Scratch your head (Left) |
| Q86 | varchar |  |  | SI | Brush your teeth (Right) |
| Q87 | varchar |  |  | SI | Brush your teeth (Left) |
| Q88 | varchar |  |  | SI | Dyspraxia |
| Q89 | varchar |  |  | SI | Ideational dyspraxia |
| Q90 | varchar |  |  | SI | Ideomotor dyspraxia |
| Q91 | varchar |  |  | SI | Right |
| Q92 | varchar |  |  | SI | Left |
| Q93 | varchar |  |  | SI | Wave goodbye |
| Q94 | varchar |  |  | SI | Scratch your head |
| Q95 | varchar |  |  | SI | Brush teeth |
| Q96 | varchar |  |  | SI | points |
| Q97 | varchar |  |  | SI | points |
| Q98 | varchar |  |  | SI | points |
| Q99 | varchar |  |  | SI | points |
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