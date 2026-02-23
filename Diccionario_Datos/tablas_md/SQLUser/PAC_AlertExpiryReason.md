# SQLUser.PAC_AlertExpiryReason

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALEXP_RowId | bigint | PK |  | NO | - |
| ALEXP_Code | varchar |  |  | NO | Code |
| ALEXP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALEXP_CreatedDate | date |  |  | SI | Created Date |
| ALEXP_CreatedTime | time |  |  | SI | Created Time |
| ALEXP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALEXP_DateFrom | date |  |  | SI | Date From |
| ALEXP_DateTo | date |  |  | SI | Date To |
| ALEXP_Desc | varchar |  |  | NO | Description |
| ALEXP_Owner | varchar |  |  | SI | Owner |
| ALEXP_UpdatedDate | date |  |  | SI | Updated Date |
| ALEXP_UpdatedTime | time |  |  | SI | Updated Time |
| ALEXP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Respiratory diagnosis |
| Q04 | - |  |  | SI | Other diagnosis |
| Q05 | - |  |  | SI | Details of disability |
| Q06 | - |  |  | SI | Patient has stopped smoking for one month prior to... |
| Q07 | - |  |  | SI | Identification of need |
| Q08 | - |  |  | SI | Clinical criteria |
| Q09 | - |  |  | SI | At rest (l/min) |
| Q10 | - |  |  | SI | Exercise (l/min) |
| Q11 | - |  |  | SI | Sleep (l/min) |
| Q12 | - |  |  | SI | Hours per day oxygen is required |
| Q13 | - |  |  | SI | Physician ordering |
| Q14 | - |  |  | SI | Respiratory consultant |
| Q15 | - |  |  | SI | Provide further details as relevant |
| Q16 | - |  |  | SI | Considerations include lifestyle issues, clinical ... |
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