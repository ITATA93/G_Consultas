# SQLUser.OEC_LabResultStatus

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LABRS_RowId | bigint | PK |  | NO | - |
| LABRS_Code | varchar |  |  | NO | Code |
| LABRS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LABRS_CreatedDate | date |  |  | SI | Created Date |
| LABRS_CreatedTime | time |  |  | SI | Created Time |
| LABRS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LABRS_Desc | varchar |  |  | NO | Description |
| LABRS_IconFilePath | varchar |  |  | SI | IconFilePath |
| LABRS_Owner | varchar |  |  | SI | Owner |
| LABRS_UpdatedDate | date |  |  | SI | Updated Date |
| LABRS_UpdatedTime | time |  |  | SI | Updated Time |
| LABRS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Eye |
| Q02 | - |  |  | SI | Refraction Type |
| Q03 | - |  |  | SI | Sphere |
| Q04 | - |  |  | SI | Cylinder |
| Q05 | - |  |  | SI | Axis |
| Q06 | - |  |  | SI | K1 |
| Q07 | - |  |  | SI | K2 |
| Q08 | - |  |  | SI | @ |
| Q09 | - |  |  | SI | @ |
| Q10 | - |  |  | SI | ACD (endo) |
| Q11 | - |  |  | SI | Pentacam topography |
| Q12 | - |  |  | SI | Pentacam topography text |
| Q13 | - |  |  | SI | By IOL master |
| Q14 | - |  |  | SI | By IOL text |
| Q15 | - |  |  | SI | Calculated IOL |
| Q16 | - |  |  | SI | Notes |
| Q17 | - |  |  | SI | Pachymetery |
| Q18 | - |  |  | SI | Calculated IOL |
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