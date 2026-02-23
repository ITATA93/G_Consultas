# SQLUser.PAC_PregDiabTreatment

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACDIAB_RowID | bigint | PK |  | NO | - |
| ChildQ06DR | - |  |  | SI | Child Reference: Procedural final count |
| PACDIAB_Code | varchar |  |  | NO | Code |
| PACDIAB_CodeTableTags | varchar |  |  | SI | List of code table tags |
| PACDIAB_CreatedDate | date |  |  | SI | Created Date |
| PACDIAB_CreatedTime | time |  |  | SI | Created Time |
| PACDIAB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACDIAB_DateFrom | date |  |  | SI | Effective date for the record |
| PACDIAB_DateTo | date |  |  | SI | Last day the record is active |
| PACDIAB_Desc | varchar |  |  | NO | Description |
| PACDIAB_Owner | varchar |  |  | SI | Owner |
| PACDIAB_UpdatedDate | date |  |  | SI | Updated Date |
| PACDIAB_UpdatedTime | time |  |  | SI | Updated Time |
| PACDIAB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Are swabs, sharps and instruments correct? |
| Q02 | - |  |  | SI | Theatre scrub practitioner |
| Q03 | - |  |  | SI | Theatre circulator |
| Q04 | - |  |  | SI | Time |
| Q07 | - |  |  | SI | Are swabs, sharps and instruments correct? |
| Q08 | - |  |  | SI | Theatre scrub practitioner |
| Q09 | - |  |  | SI | Theatre circulator |
| Q10 | - |  |  | SI | Time |
| Q11 | - |  |  | SI | Object intentionally left in situ? |
| Q12 | - |  |  | SI | Planned removal? |
| Q13 | - |  |  | SI | Specify item(s) and plan |
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