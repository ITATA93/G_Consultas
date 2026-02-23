# SQLUser.BLC_ReasonForRefund

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RFR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Objetivo General |
| Q04 | - |  |  | SI | Objetivo Individual |
| Q05 | - |  |  | SI | Meta Individual |
| Q06 | - |  |  | SI | Actividad Individual |
| Q07 | - |  |  | SI | Objetivo Familiar |
| Q08 | - |  |  | SI | Meta Familiar |
| Q09 | - |  |  | SI | Actividad Familiar |
| Q10 | - |  |  | SI | Objetivo Comunitario |
| Q11 | - |  |  | SI | Meta Comunitario |
| Q12 | - |  |  | SI | Actividad Comunitario |
| Q13 | - |  |  | SI | Cumplimiento Individual |
| Q14 | - |  |  | SI | Cumplimiento Familiar |
| Q15 | - |  |  | SI | Cumplimiento Comunitario |
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
| RFR_Code | varchar |  |  | NO | Code |
| RFR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RFR_CreatedDate | date |  |  | SI | Created Date |
| RFR_CreatedTime | time |  |  | SI | Created Time |
| RFR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RFR_DateFrom | date |  |  | SI | Date From |
| RFR_DateTo | date |  |  | SI | Date To |
| RFR_Desc | varchar |  |  | NO | Description |
| RFR_Owner | varchar |  |  | SI | Owner |
| RFR_UpdatedDate | date |  |  | SI | Updated Date |
| RFR_UpdatedTime | time |  |  | SI | Updated Time |
| RFR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*