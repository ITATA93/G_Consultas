# SQLUser.PAC_NameType

**Schema:** SQLUser
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NAMETYP_RowId | bigint | PK |  | NO | - |
| NAMETYP_Code | varchar |  |  | NO | Code |
| NAMETYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NAMETYP_CreatedDate | date |  |  | SI | Created Date |
| NAMETYP_CreatedTime | time |  |  | SI | Created Time |
| NAMETYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NAMETYP_DateFrom | date |  |  | SI | Date From |
| NAMETYP_DateTo | date |  |  | SI | Date To |
| NAMETYP_Desc | varchar |  |  | NO | Description |
| NAMETYP_Owner | varchar |  |  | SI | Owner |
| NAMETYP_UpdatedDate | date |  |  | SI | Updated Date |
| NAMETYP_UpdatedTime | time |  |  | SI | Updated Time |
| NAMETYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Signs / Symptoms |
| Q02 | - |  |  | SI | Please select one of the following |
| Q03 | - |  |  | SI | Grade I: Low risk of vasospasm (range 0-21%) |
| Q04 | - |  |  | SI | Grade II: Low risk of vasospasm (range 0-25%) |
| Q05 | - |  |  | SI | Grade III: Low to high risk of vasospasm (range 23... |
| Q06 | - |  |  | SI | Grade IV: Low to moderate risk of vasospasm (range... |
| Q07 | - |  |  | SI | Scale is used to predict the risk of cerebral vaso... |
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