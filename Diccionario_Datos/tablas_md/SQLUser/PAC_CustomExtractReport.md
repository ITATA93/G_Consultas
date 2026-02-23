# SQLUser.PAC_CustomExtractReport

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REP_ParRef | bigint | PK |  | NO | PAC_CustomExtract Parent Reference |
| Q01 | - |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q02 | - |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q03 | - |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q04 | - |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q05 | - |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q06 | - |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q07 | - |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q08 | - |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q09 | - |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q10 | - |  |  | SI | In the past 4 weeks, about how often did you feel ... |
| Q11 | - |  |  | SI | 10 - 19: Likely to be well |
| Q12 | - |  |  | SI | 20 - 24: Likely to have a mild disorder |
| Q13 | - |  |  | SI | 25 - 29: Likely to have a moderate disorder |
| Q14 | - |  |  | SI | 30 - 50: Likely to have a severe disorder |
| Q15 | - |  |  | SI | The Kessler Psychological Distress Scale (K10) is ... |
| Q16 | - |  |  | SI | 10 - 19: Likely to be well |
| Q17 | - |  |  | SI | 20 - 24: Likely to have a mild disorder |
| Q18 | - |  |  | SI | 25 - 29: Likely to have a moderate disorder |
| Q19 | - |  |  | SI | 30 - 50: Likely to have a severe disorder |
| Q20 | - |  |  | SI | Score |
| Q21 | - |  |  | SI | Classification |
| Q22 | - |  |  | SI | 10 - 19 |
| Q23 | - |  |  | SI | Likely to be well |
| Q24 | - |  |  | SI | 20 - 24 |
| Q25 | - |  |  | SI | Likely to have a mild disorder |
| Q26 | - |  |  | SI | 25 - 29 |
| Q27 | - |  |  | SI | Likely to have a moderate disorder |
| Q28 | - |  |  | SI | 30 - 50 |
| Q29 | - |  |  | SI | Likely to have a severe disorder |
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
| REP_Childsub | double |  |  | NO | Childsub |
| REP_Code | varchar |  |  | SI | Code |
| REP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REP_CreatedDate | date |  |  | SI | Created Date |
| REP_CreatedTime | time |  |  | SI | Created Time |
| REP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REP_DeleteScript | varchar |  |  | SI | DeleteScript |
| REP_Desc | varchar |  |  | SI | Description |
| REP_ExtractScript | varchar |  |  | SI | ExtractScript |
| REP_RowId | varchar |  |  | NO | - |
| REP_UpdatedDate | date |  |  | SI | Updated Date |
| REP_UpdatedTime | time |  |  | SI | Updated Time |
| REP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*