# SQLUser.PAC_TypeOfAntenatalCare

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TOAC_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient primary treating unit - HOME unit |
| Q04 | - |  |  | SI | Preferred unit (location closest to home or accomm... |
| Q05 | - |  |  | SI | Other (specify) |
| Q06 | - |  |  | SI | Consented to dialysis and transplant survey regist... |
| Q07 | - |  |  | SI | Dummy1 |
| Q08 | - |  |  | SI | Modality |
| Q09 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Access used at first haemodialysis |
| Q11 | - |  |  | SI | Orientation to unit completed |
| Q12 | - |  |  | SI | Unit expectations discussed |
| Q13 | - |  |  | SI | Transport options and service discussed |
| Q14 | - |  |  | SI | Mode of transport |
| Q15 | - |  |  | SI | Other transport |
| Q16 | - |  |  | SI | Self care options discussed |
| Q17 | - |  |  | SI | Dialysis schedule discussed |
| Q18 | - |  |  | SI | Clinic appointments and reviews discussed |
| Q19 | - |  |  | SI | Home therapies model |
| Q20 | - |  |  | SI | Home therapies training status |
| Q21 | - |  |  | SI | Notes |
| Q22 | - |  |  | SI | Date training completed |
| Q23 | - |  |  | SI | Date patient transferred to home therapy |
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
| TOAC_Code | varchar |  |  | NO | Code |
| TOAC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TOAC_CreatedDate | date |  |  | SI | Created Date |
| TOAC_CreatedTime | time |  |  | SI | Created Time |
| TOAC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TOAC_DateFrom | date |  |  | SI | Date From |
| TOAC_DateTo | date |  |  | SI | Date To |
| TOAC_Desc | varchar |  |  | NO | Description |
| TOAC_NationalCode | varchar |  |  | SI | National Code |
| TOAC_Owner | varchar |  |  | SI | Owner |
| TOAC_UpdatedDate | date |  |  | SI | Updated Date |
| TOAC_UpdatedTime | time |  |  | SI | Updated Time |
| TOAC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*