# SQLUser.PAC_AdmLabourStatus

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMLS_RowId | bigint | PK |  | NO | - |
| ADMLS_Code | varchar |  |  | NO | Code |
| ADMLS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMLS_CreatedDate | date |  |  | SI | Created Date |
| ADMLS_CreatedTime | time |  |  | SI | Created Time |
| ADMLS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMLS_DateFrom | date |  |  | SI | Date From |
| ADMLS_DateTo | date |  |  | SI | Date To |
| ADMLS_Desc | varchar |  |  | NO | Desciption |
| ADMLS_Owner | varchar |  |  | SI | Owner |
| ADMLS_UpdatedDate | date |  |  | SI | Updated Date |
| ADMLS_UpdatedTime | time |  |  | SI | Updated Time |
| ADMLS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Instructions - Read each of the symptoms below. Ra... |
| Q02 | - |  |  | SI | Anxious mood - worries, expecting the worst, fearf... |
| Q03 | - |  |  | SI | Tension - Feelings of tension, fatigability, start... |
| Q04 | - |  |  | SI | Fears -  Of dark, of strangers, of being left alon... |
| Q05 | - |  |  | SI | Insomnia - Difficulty in falling asleep, broken sl... |
| Q06 | - |  |  | SI | Depressed mood - Loss of interest, lack of interes... |
| Q07 | - |  |  | SI | Physical / Muscular - Constant pains and aches, tw... |
| Q08 | - |  |  | SI | Senses - Tinnitus, blurring of vision, hot and col... |
| Q09 | - |  |  | SI | Cardiovascular - Tachycardia, palpitations, pain i... |
| Q10 | - |  |  | SI | Respiratory - Pressure or constriction in chest, c... |
| Q11 | - |  |  | SI | Digestive - Difficulty in swallowing, wind abdomin... |
| Q12 | - |  |  | SI | Genitourinary - Frequency of micturition, urgency ... |
| Q13 | - |  |  | SI | Autonomic symptoms - Dry mouth, flushing, pallor, ... |
| Q14 | - |  |  | SI | Behaviour at interview - Fidgeting, restlessness o... |
| Q15 | - |  |  | SI | Interpretation of scores |
| Q16 | - |  |  | SI | 18 + = Mild |
| Q17 | - |  |  | SI | Each item is scored on a scale of 0 (not present) ... |
| Q18 | - |  |  | SI | Main purpose to assess the severity of symptoms of... |
| Q19 | - |  |  | SI | 25+ = Moderate Anxiety |
| Q20 | - |  |  | SI | 30+ = Severe Anxiety (Professional help required) |
| Q21 | - |  |  | SI | Intellectual - Difficulty in concentration, poor m... |
| Q23 | - |  |  | SI | Normal |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | Time |
| Q26 | - |  |  | SI | Score |
| Q27 | - |  |  | SI | Classification |
| Q28 | - |  |  | SI | 1 - 17 |
| Q29 | - |  |  | SI | Mild anxiety severity |
| Q30 | - |  |  | SI | 18 - 24 |
| Q31 | - |  |  | SI | Mild to moderate anxiety severity |
| Q32 | - |  |  | SI | 25 - 30 |
| Q33 | - |  |  | SI | Moderate anxiety - Professional help required |
| Q34 | - |  |  | SI | 31 - 56 |
| Q35 | - |  |  | SI | Severe anxiety - Professional help required |
| Q36 | - |  |  | SI | 1 - 17: Mild anxiety severity |
| Q37 | - |  |  | SI | 18 - 24: Mild to moderate anxiety severity |
| Q38 | - |  |  | SI | 25 - 30: Moderate anxiety - Professional help requ... |
| Q39 | - |  |  | SI | 31 - 56: Severe anxiety - Professional help requir... |
| Q40 | - |  |  | SI | 0 |
| Q41 | - |  |  | SI | Not present |
| Q42 | - |  |  | SI | 0: Not present |
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