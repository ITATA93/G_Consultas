# SQLUser.PAC_ContraceptiveMethods

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONMET_RowId | bigint | PK |  | NO | - |
| CONMET_Code | varchar |  |  | NO | Code |
| CONMET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONMET_CreatedDate | date |  |  | SI | Created Date |
| CONMET_CreatedTime | time |  |  | SI | Created Time |
| CONMET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONMET_DateFrom | date |  |  | SI | DateFrom |
| CONMET_DateTo | date |  |  | SI | DateTo |
| CONMET_Desc | varchar |  |  | NO | Description |
| CONMET_Owner | varchar |  |  | SI | Owner |
| CONMET_UpdatedDate | date |  |  | SI | Updated Date |
| CONMET_UpdatedTime | time |  |  | SI | Updated Time |
| CONMET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ05DR | - |  |  | SI | Child Reference: Embryo transfer |
| Q01 | - |  |  | SI | Partner's name |
| Q02 | - |  |  | SI | Partner's age (years) |
| Q03 | - |  |  | SI | Total number of cumuluses |
| Q06 | - |  |  | SI | No. of embryos frozen |
| Q07 | - |  |  | SI | Date of freezing |
| Q08 | - |  |  | SI | Comments |
| Q09 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Time |
| Q11 | - |  |  | SI | ID labelling of pot verified with patient |
| Q12 | - |  |  | SI | Separation tube checked - Embryologist |
| Q13 | - |  |  | SI | Time produced |
| Q14 | - |  |  | SI | Time prep |
| Q15 | - |  |  | SI | Method of prep |
| Q16 | - |  |  | SI | Witness |
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