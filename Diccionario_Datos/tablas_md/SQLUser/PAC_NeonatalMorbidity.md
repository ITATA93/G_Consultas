# SQLUser.PAC_NeonatalMorbidity

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NEOMORB_RowId | bigint | PK |  | NO | - |
| NEOMORB_Active | varchar |  |  | SI | Active flag |
| NEOMORB_Code | varchar |  |  | NO | Code |
| NEOMORB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NEOMORB_CreatedDate | date |  |  | SI | Created Date |
| NEOMORB_CreatedTime | time |  |  | SI | Created Time |
| NEOMORB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NEOMORB_DateFrom | date |  |  | SI | Date from |
| NEOMORB_DateTo | date |  |  | SI | Date To |
| NEOMORB_Desc | varchar |  |  | NO | Description |
| NEOMORB_NationalCode | varchar |  |  | SI | National Code |
| NEOMORB_Owner | varchar |  |  | SI | Owner |
| NEOMORB_UpdatedDate | date |  |  | SI | Updated Date |
| NEOMORB_UpdatedTime | time |  |  | SI | Updated Time |
| NEOMORB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Severity of symptoms |
| Q02 | - |  |  | SI | The Hoehn and Yahr scale is used to describe the s... |
| Q03 | - |  |  | SI | Higher stage indicates higher degree of disability |
| Q04 | - |  |  | SI | This rating system has been largely supplanted by ... |
| Q05 | - |  |  | SI | Higher stage indicates higher degree of disability |
| Q06 | - |  |  | SI | Score caption |
| Q07 | - |  |  | SI | Date |
| Q08 | - |  |  | SI | Time |
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