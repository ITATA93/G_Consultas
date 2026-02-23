# questionnaire.QTCHAMA

> Hamilton Anxiety Scale (HAM-A)

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hamilton Anxiety Scale (HAM-A)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Instructions - Read each of the symptoms below. Ra... |
| Q02 | varchar |  |  | SI | Anxious mood - worries, expecting the worst, fearf... |
| Q03 | varchar |  |  | SI | Tension - Feelings of tension, fatigability, start... |
| Q04 | varchar |  |  | SI | Fears -  Of dark, of strangers, of being left alon... |
| Q05 | varchar |  |  | SI | Insomnia - Difficulty in falling asleep, broken sl... |
| Q06 | varchar |  |  | SI | Depressed mood - Loss of interest, lack of interes... |
| Q07 | varchar |  |  | SI | Physical / Muscular - Constant pains and aches, tw... |
| Q08 | varchar |  |  | SI | Senses - Tinnitus, blurring of vision, hot and col... |
| Q09 | varchar |  |  | SI | Cardiovascular - Tachycardia, palpitations, pain i... |
| Q10 | varchar |  |  | SI | Respiratory - Pressure or constriction in chest, c... |
| Q11 | varchar |  |  | SI | Digestive - Difficulty in swallowing, wind abdomin... |
| Q12 | varchar |  |  | SI | Genitourinary - Frequency of micturition, urgency ... |
| Q13 | varchar |  |  | SI | Autonomic symptoms - Dry mouth, flushing, pallor, ... |
| Q14 | varchar |  |  | SI | Behaviour at interview - Fidgeting, restlessness o... |
| Q15 | varchar |  |  | SI | Interpretation of scores |
| Q16 | varchar |  |  | SI | 18 + = Mild |
| Q17 | varchar |  |  | SI | Each item is scored on a scale of 0 (not present) ... |
| Q18 | varchar |  |  | SI | Main purpose to assess the severity of symptoms of... |
| Q19 | varchar |  |  | SI | 25+ = Moderate Anxiety |
| Q20 | varchar |  |  | SI | 30+ = Severe Anxiety (Professional help required) |
| Q21 | varchar |  |  | SI | Intellectual - Difficulty in concentration, poor m... |
| Q23 | varchar |  |  | SI | Normal |
| Q24 | date |  |  | SI | Date |
| Q25 | time |  |  | SI | Time |
| Q26 | varchar |  |  | SI | Score |
| Q27 | varchar |  |  | SI | Classification |
| Q28 | varchar |  |  | SI | 1 - 17 |
| Q29 | varchar |  |  | SI | Mild anxiety severity |
| Q30 | varchar |  |  | SI | 18 - 24 |
| Q31 | varchar |  |  | SI | Mild to moderate anxiety severity |
| Q32 | varchar |  |  | SI | 25 - 30 |
| Q33 | varchar |  |  | SI | Moderate anxiety - Professional help required |
| Q34 | varchar |  |  | SI | 31 - 56 |
| Q35 | varchar |  |  | SI | Severe anxiety - Professional help required |
| Q36 | varchar |  |  | SI | 1 - 17: Mild anxiety severity |
| Q37 | varchar |  |  | SI | 18 - 24: Mild to moderate anxiety severity |
| Q38 | varchar |  |  | SI | 25 - 30: Moderate anxiety - Professional help requ... |
| Q39 | varchar |  |  | SI | 31 - 56: Severe anxiety - Professional help requir... |
| Q40 | varchar |  |  | SI | 0 |
| Q41 | varchar |  |  | SI | Not present |
| Q42 | varchar |  |  | SI | 0: Not present |
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