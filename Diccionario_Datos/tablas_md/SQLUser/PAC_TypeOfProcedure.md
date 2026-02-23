# SQLUser.PAC_TypeOfProcedure

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TOP_RowId | bigint | PK |  | NO | - |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Score |
| Q11 | - |  |  | SI | Guidelines |
| Q13 | - |  |  | SI | The RichardsCampbell Sleep Questionnaire (RCSQ) wa... |
| Q14 | - |  |  | SI | The scale was originally developed as a self-repor... |
| Q15 | - |  |  | SI | Scoring Directions |
| Q16 | - |  |  | SI | 1. Scores may range from 0 (indicating the worst p... |
| Q17 | - |  |  | SI | 2. For verbal patients, ask the patient to give a ... |
| Q18 | - |  |  | SI | 3. For non-verbal patients, ask the patient to ind... |
| Q19 | - |  |  | SI | 4. The total sleep score is derived by adding the ... |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Copyright © Kathy Richards et al. |
| Q21 | - |  |  | SI | The Richards–Campbell Sleep Questionnaire (RCSQ) e... |
| Q4 | - |  |  | SI | The patient should answer each of these questions ... |
| Q5 | - |  |  | SI | Considering 100 as Deep sleep and 0 as Light sleep... |
| Q6 | - |  |  | SI | Considering 100 as Fell asleep almost immediately ... |
| Q7 | - |  |  | SI | Considering 100 as Awake very little and 0 as Awak... |
| Q8 | - |  |  | SI | Considering 100 as Got back to sleep immediately a... |
| Q9 | - |  |  | SI | Considering 100 as A good night's sleep and 0 as A... |
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
| TOP_Code | varchar |  |  | NO | Code |
| TOP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TOP_CreatedDate | date |  |  | SI | Created Date |
| TOP_CreatedTime | time |  |  | SI | Created Time |
| TOP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TOP_DateFrom | date |  |  | SI | Date From |
| TOP_DateTo | date |  |  | SI | Date To |
| TOP_Desc | varchar |  |  | NO | Description |
| TOP_Owner | varchar |  |  | SI | Owner |
| TOP_UpdatedDate | date |  |  | SI | Updated Date |
| TOP_UpdatedTime | time |  |  | SI | Updated Time |
| TOP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*