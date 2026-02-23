# SQLUser.OE_MicrofilmRollPosition

**Schema:** SQLUser
**Columnas:** 194
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| POS_ParRef | bigint | PK |  | NO | OE_MicrofilmRoll Parent Reference |
| POS_Childsub | double |  |  | NO | Childsub |
| POS_Comment | varchar |  |  | SI | Comment |
| POS_DateEntered | date |  |  | SI | Date Entered |
| POS_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| POS_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| POS_MRecordType_DR | bigint |  | FK | SI | Des Ref MRecordType |
| POS_Position | varchar |  |  | SI | Position |
| POS_RTMAS_DR | bigint |  | FK | SI | Des Ref RTMAS |
| POS_RowId | varchar |  |  | NO | - |
| POS_TimeEntered | time |  |  | SI | Time Entered |
| Q01 | - |  |  | SI | General Presentation |
| Q02 | - |  |  | SI | Alertness / Affect / Communication |
| Q03 | - |  |  | SI | Hearing |
| Q04 | - |  |  | SI | Vision (e.g. Aids used premorbidly & for assessmen... |
| Q05 | - |  |  | SI | Diagnosis |
| Q06 | - |  |  | SI | Date of onset |
| Q07 | - |  |  | SI | Assessment |
| Q08 | - |  |  | SI | Date |
| Q09 | - |  |  | SI | Occupational Therapist Name |
| Q10 | - |  |  | SI | General |
| Q100 | - |  |  | SI | points |
| Q101 | - |  |  | SI | points |
| Q102 | - |  |  | SI | points |
| Q103 | - |  |  | SI | points |
| Q104 | - |  |  | SI | points |
| Q105 | - |  |  | SI | points |
| Q107 | - |  |  | SI | points |
| Q108 | - |  |  | SI | Occupational therapist name |
| Q109 | - |  |  | SI | Date |
| Q11 | - |  |  | SI | Assessment (General) |
| Q110 | - |  |  | SI | Signature |
| Q110UDt | - |  |  | SI | Signature Last Updated Date |
| Q110UTm | - |  |  | SI | Signature Last Updated Time |
| Q111 | - |  |  | SI | Visual field deficit and visual inattention togeth... |
| Q112 | - |  |  | SI | Reading |
| Q113 | - |  |  | SI | Cognition |
| Q114 | - |  |  | SI | Insight |
| Q115 | - |  |  | SI | Language |
| Q115ObsDR | - |  |  | SI | Language  DR |
| Q116 | - |  |  | SI | What would you do if you woke up one minute before... |
| Q117 | - |  |  | SI | you had an important meeting / appointment in town... |
| Q118 | - |  |  | SI | Cognitive assessment completed |
| Q119 | - |  |  | SI | Externally documented cognitive assessments |
| Q12 | - |  |  | SI | Assessment date (General) |
| Q120 | - |  |  | SI | Tracking |
| Q121 | - |  |  | SI | Vision comments |
| Q122 | - |  |  | SI | Agnosia |
| Q123 | - |  |  | SI | Agnosia test |
| Q124 | - |  |  | SI | Agnosia result |
| Q125 | - |  |  | SI | Eye quadrants	 |
| Q126 | - |  |  | SI | Date |
| Q127 | - |  |  | SI | Time |
| Q128 | - |  |  | SI | Diagnosis relevant to assessment |
| Q129 | - |  |  | SI | Visual attention time held comments |
| Q13 | - |  |  | SI | Assessment therapist name (General) |
| Q130 | - |  |  | SI | Nystagmus comments |
| Q131 | - |  |  | SI | Homonymous hemianopia comments |
| Q132 | - |  |  | SI | Visual field deficit and visual inattention togeth... |
| Q133 | - |  |  | SI | Other reading |
| Q134 | - |  |  | SI | Reading comments |
| Q135 | - |  |  | SI | Neglect |
| Q136 | - |  |  | SI | Assessment (General) |
| Q137 | - |  |  | SI | Assessment (Vision) |
| Q138 | - |  |  | SI | Assessment (Cognition) |
| Q139 | - |  |  | SI | Assessment (MOCA V.1) |
| Q14 | - |  |  | SI | Vision |
| Q140 | - |  |  | SI | Assessment (Perception) |
| Q141 | - |  |  | SI | Assessment (Upper limb) |
| Q15 | - |  |  | SI | Assessment (Vision) |
| Q16 | - |  |  | SI | Assessment date (Vision) |
| Q17 | - |  |  | SI | Assessment therapist name (Vision) |
| Q18 | - |  |  | SI | Cognition |
| Q19 | - |  |  | SI | Assessment (Cognition) |
| Q20 | - |  |  | SI | Assessment date (Cognition) |
| Q21 | - |  |  | SI | Assessment therapist name (Cognition) |
| Q22 | - |  |  | SI | MOCA V.1 |
| Q23 | - |  |  | SI | Assessment (MOCA V.1) |
| Q24 | - |  |  | SI | Assessment date (MOCA V.1) |
| Q25 | - |  |  | SI | Assessment therapist name (MOCA V.1) |
| Q26 | - |  |  | SI | Perception |
| Q27 | - |  |  | SI | Assessment (Perception) |
| Q28 | - |  |  | SI | Assessment date (Perception) |
| Q29 | - |  |  | SI | Assessment therapist name (Perception) |
| Q30 | - |  |  | SI | Upper limb |
| Q31 | - |  |  | SI | Assessment (Upper limb) |
| Q32 | - |  |  | SI | Assessment date (Upper limb) |
| Q33 | - |  |  | SI | Assessment therapist name (Upper limb) |
| Q34 | - |  |  | SI | Comments (e.g. factors which may influence results... |
| Q35 | - |  |  | SI | Vision |
| Q36 | - |  |  | SI | Visual attention time held (up to 30 seconds) |
| Q37 | - |  |  | SI | Tracking |
| Q38 | - |  |  | SI | Nystagmus |
| Q39 | - |  |  | SI | Visual fields |
| Q40 | - |  |  | SI | Homonymous hemianopia |
| Q47 | - |  |  | SI | Impulsivity |
| Q48 | - |  |  | SI | Ability to follow commands |
| Q49 | - |  |  | SI | 3 Step = “Pick up the pen, place the pen in my han... |
| Q50 | - |  |  | SI | 2 Step = “Touch your nose then touch your shoulder |
| Q51 | - |  |  | SI | 1 Step = “Pick up the pen” |
| Q52 | - |  |  | SI | Problem Solving |
| Q53 | - |  |  | SI | What would you do if you woke up one minute before... |
| Q54 | - |  |  | SI | Observations (Cognition) |
| Q55 | - |  |  | SI | Montreal Cognitive Assessment (MOCA) |
| Q56 | - |  |  | SI | Visuospatial / Execute |
| Q56ObsDR | - |  |  | SI | Visuospatial / Execute DR |
| Q57 | - |  |  | SI | Naming |
| Q57ObsDR | - |  |  | SI | Naming DR |
| Q58 | - |  |  | SI | Memory |
| Q58ObsDR | - |  |  | SI | Memory DR |
| Q59 | - |  |  | SI | Attention |
| Q59ObsDR | - |  |  | SI | Attention DR |
| Q60 | - |  |  | SI | Abstraction |
| Q60ObsDR | - |  |  | SI | Abstraction DR |
| Q61 | - |  |  | SI | Delayed recall |
| Q61ObsDR | - |  |  | SI | Delayed recall DR |
| Q62 | - |  |  | SI | Orientation |
| Q62ObsDR | - |  |  | SI | Orientation DR |
| Q63 | - |  |  | SI | Sum |
| Q64 | - |  |  | SI | Total (MOCA) |
| Q65 | - |  |  | SI | Add 1 point if < 12 years education |
| Q66 | - |  |  | SI | Perception |
| Q67 | - |  |  | SI | Visual Perception |
| Q68 | - |  |  | SI | Right / Left discrimination |
| Q69 | - |  |  | SI | Form constancy |
| Q70 | - |  |  | SI | Depth perception |
| Q71 | - |  |  | SI | Figure - Ground |
| Q72 | - |  |  | SI | Position in space |
| Q73 | - |  |  | SI | Unilateral spatial neglect |
| Q75 | - |  |  | SI | Unilateral body neglect |
| Q76 | - |  |  | SI | Agnosia |
| Q77 | - |  |  | SI | Facial Praxis Task |
| Q78 | - |  |  | SI | Cough |
| Q79 | - |  |  | SI | Blow out a match |
| Q80 | - |  |  | SI | Puff out your cheeks |
| Q81 | - |  |  | SI | Limb Praxis Task |
| Q82 | - |  |  | SI | Wave goodbye (Right) |
| Q83 | - |  |  | SI | Wave goodbye (Left) |
| Q84 | - |  |  | SI | Scratch your head (Right) |
| Q85 | - |  |  | SI | Scratch your head (Left) |
| Q86 | - |  |  | SI | Brush your teeth (Right) |
| Q87 | - |  |  | SI | Brush your teeth (Left) |
| Q88 | - |  |  | SI | Dyspraxia |
| Q89 | - |  |  | SI | Ideational dyspraxia |
| Q90 | - |  |  | SI | Ideomotor dyspraxia |
| Q91 | - |  |  | SI | Right |
| Q92 | - |  |  | SI | Left |
| Q93 | - |  |  | SI | Wave goodbye |
| Q94 | - |  |  | SI | Scratch your head |
| Q95 | - |  |  | SI | Brush teeth |
| Q96 | - |  |  | SI | points |
| Q97 | - |  |  | SI | points |
| Q98 | - |  |  | SI | points |
| Q99 | - |  |  | SI | points |
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