# SQLUser.PAC_PathwayItemInfo

**Schema:** SQLUser
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPIIN_ParRef | varchar | PK |  | NO | Parent Reference |
| PACPIIN_COPYR_DR | bigint |  | FK | SI | Copyright |
| PACPIIN_Childsub | double |  |  | NO | Childsub |
| PACPIIN_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| PACPIIN_CreatedDate | date |  |  | SI | Created Date |
| PACPIIN_CreatedTime | time |  |  | SI | Created Time |
| PACPIIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPIIN_Desc | varchar |  |  | NO | Description |
| PACPIIN_FileName | varchar |  |  | SI | File Name |
| PACPIIN_RowId | varchar |  |  | NO | - |
| PACPIIN_StreamData | bigint |  |  | SI | epr.CTFile |
| PACPIIN_UpdatedDate | date |  |  | SI | Updated Date |
| PACPIIN_UpdatedTime | time |  |  | SI | Updated Time |
| PACPIIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Please select one of the following |
| Q02 | - |  |  | SI | Grade 1: 70% chance of survival |
| Q03 | - |  |  | SI | Grade 2: 60% chance of survival |
| Q04 | - |  |  | SI | Grade 3: 50% chance of survival |
| Q05 | - |  |  | SI | Grade 4: 20% chance of survival |
| Q06 | - |  |  | SI | Grade 5: 10% chance of survival |
| Q07 | - |  |  | SI | WFNS Scale  is intended to be a simple, reliable a... |
| Q08 | - |  |  | SI | This system offers  less interobserver variability... |
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