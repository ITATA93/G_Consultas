# SQLUser.ORC_ReasonForOTBookChange

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REOTBC_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Assessment date |
| Q02 | - |  |  | SI | Assessment time |
| Q03 | - |  |  | SI | Seizure onset date |
| Q04 | - |  |  | SI | Seizure number |
| Q05 | - |  |  | SI | Seizure onset time |
| Q06 | - |  |  | SI | Seizure semiology |
| Q07 | - |  |  | SI | Pre-ictal (before seizure)(aura) |
| Q08 | - |  |  | SI | Warning sign |
| Q09 | - |  |  | SI | Description |
| Q10 | - |  |  | SI | Ictal stage (during seizure) |
| Q11 | - |  |  | SI | Description |
| Q12 | - |  |  | SI | Duration |
| Q13 | - |  |  | SI | Exact duration (minutes) |
| Q14 | - |  |  | SI | Preserve awareness |
| Q15 | - |  |  | SI | Seizure terminates spontaneously |
| Q16 | - |  |  | SI | Evaluation during seizure |
| Q17 | - |  |  | SI | Memory: ask the patient if he/she remembers |
| Q18 | - |  |  | SI | Number |
| Q19 | - |  |  | SI | Phrase |
| Q20 | - |  |  | SI | Language : |
| Q21 | - |  |  | SI | Ask patient about his/her name |
| Q22 | - |  |  | SI | Ask the patient to point to TV, window or any obje... |
| Q23 | - |  |  | SI | Post ictal evaluation (after seizure) |
| Q24 | - |  |  | SI | Memory |
| Q25 | - |  |  | SI | Patient able to recall given number and phrase |
| Q26 | - |  |  | SI | Vision, receptive, expressive language |
| Q27 | - |  |  | SI | Ask patient to name shown object (pen, watch...) |
| Q28 | - |  |  | SI | Ask patient to do a motor action on each side of t... |
| Q29 | - |  |  | SI | Point to ceiling, window, door.. |
| Q30 | - |  |  | SI | Trauma or injuries |
| Q31 | - |  |  | SI | Specify |
| Q32 | - |  |  | SI | Nurse name |
| Q33 | - |  |  | SI | Nurse ID number |
| Q34 | - |  |  | SI | Signature |
| Q34UDt | - |  |  | SI | Signature Last Updated Date |
| Q34UTm | - |  |  | SI | Signature Last Updated Time |
| Q35 | - |  |  | SI | Attending nurse actions |
| Q36 | - |  |  | SI | Exact duration (seconds) |
| Q37 | - |  |  | SI | Ictal Stage |
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
| REOTBC_Code | varchar |  |  | NO | Code |
| REOTBC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REOTBC_CreatedDate | date |  |  | SI | Created Date |
| REOTBC_CreatedTime | time |  |  | SI | Created Time |
| REOTBC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REOTBC_DateFrom | date |  |  | SI | Date From |
| REOTBC_DateTo | date |  |  | SI | Date To |
| REOTBC_Desc | varchar |  |  | NO | Description |
| REOTBC_Owner | varchar |  |  | SI | Owner |
| REOTBC_UpdatedDate | date |  |  | SI | Updated Date |
| REOTBC_UpdatedTime | time |  |  | SI | Updated Time |
| REOTBC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*