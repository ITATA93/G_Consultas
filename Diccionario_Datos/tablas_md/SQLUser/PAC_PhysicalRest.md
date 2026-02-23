# SQLUser.PAC_PhysicalRest

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHYR_RowId | bigint | PK |  | NO | - |
| PHYR_Code | varchar |  |  | NO | Code |
| PHYR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHYR_CreatedDate | date |  |  | SI | Created Date |
| PHYR_CreatedTime | time |  |  | SI | Created Time |
| PHYR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHYR_DateFrom | date |  |  | SI | Date From |
| PHYR_DateTo | date |  |  | SI | Date To |
| PHYR_Desc | varchar |  |  | NO | Description |
| PHYR_Owner | varchar |  |  | SI | Owner |
| PHYR_UpdatedDate | date |  |  | SI | Updated Date |
| PHYR_UpdatedTime | time |  |  | SI | Updated Time |
| PHYR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | The following is an indication of the predicted ti... |
| Q02 | - |  |  | SI | Length of stay |
| Q03 | - |  |  | SI | Days |
| Q04 | - |  |  | SI | Sick leave |
| Q05 | - |  |  | SI | Days |
| Q06 | - |  |  | SI | Follow up |
| Q07 | - |  |  | SI | Days |
| Q08 | - |  |  | SI | Fit to fly |
| Q09 | - |  |  | SI | Days |
| Q10 | - |  |  | SI | Stitches removed |
| Q11 | - |  |  | SI | Days |
| Q12 | - |  |  | SI | Full recovery |
| Q13 | - |  |  | SI | Days |
| Q14 | - |  |  | SI | Estimated cost |
| Q15 | - |  |  | SI | Currency |
| Q16 | - |  |  | SI | Date |
| Q17 | - |  |  | SI | Time |
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