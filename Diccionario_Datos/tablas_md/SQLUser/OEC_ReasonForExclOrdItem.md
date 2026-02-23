# SQLUser.OEC_ReasonForExclOrdItem

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REAEXOI_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Sitting / lying down - assessment |
| Q02 | - |  |  | SI | Sitting / Lying down - Patient Ability |
| Q03 | - |  |  | SI | Sitting / Lying down - Equipment Required |
| Q04 | - |  |  | SI | Sitting / Lying down - Prior Assessment |
| Q05 | - |  |  | SI | Sitting / Lying down - Staff Required |
| Q06 | - |  |  | SI | Moving up the bed - Assessment |
| Q07 | - |  |  | SI | Moving up the bed - Patient Ability |
| Q08 | - |  |  | SI | Moving up the bed - Equipment Required |
| Q09 | - |  |  | SI | Moving up the bed - Prior Assessment |
| Q10 | - |  |  | SI | Moving up the bed - Staff Required |
| Q11 | - |  |  | SI | Turning in the bed - Assessment |
| Q12 | - |  |  | SI | Turning in the bed - Patient Ability |
| Q13 | - |  |  | SI | Turning in the bed - Equipment Required |
| Q14 | - |  |  | SI | Turning in the bed - Prior Assessment |
| Q15 | - |  |  | SI | Turning in the bed - Staff Required |
| Q16 | - |  |  | SI | Sitting on the side of bed - Assessment |
| Q17 | - |  |  | SI | Sitting on the side of bed - Patient Ability |
| Q18 | - |  |  | SI | Sitting on the side of bed - Equipment Required |
| Q19 | - |  |  | SI | Sitting on the side of bed - Prior Assessment |
| Q20 | - |  |  | SI | Sitting on the side of bed - Staff Required |
| Q21 | - |  |  | SI | Task |
| Q22 | - |  |  | SI | Assessment |
| Q23 | - |  |  | SI | Patient Ability |
| Q24 | - |  |  | SI | Equipment Required |
| Q25 | - |  |  | SI | Prior Assessment |
| Q26 | - |  |  | SI | Staff Required |
| Q27 | - |  |  | SI | Sitting / Lying down |
| Q28 | - |  |  | SI | Moving up the bed |
| Q29 | - |  |  | SI | Turning in the bed |
| Q30 | - |  |  | SI | Sitting on the side of bed |
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
| REAEXOI_Code | varchar |  |  | NO | Code |
| REAEXOI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REAEXOI_CreatedDate | date |  |  | SI | Created Date |
| REAEXOI_CreatedTime | time |  |  | SI | Created Time |
| REAEXOI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REAEXOI_DateFrom | date |  |  | SI | Date From |
| REAEXOI_DateTo | date |  |  | SI | Date To |
| REAEXOI_DefaultReason | varchar |  |  | SI | Default Reason |
| REAEXOI_Desc | varchar |  |  | NO | Description |
| REAEXOI_Owner | varchar |  |  | SI | Owner |
| REAEXOI_UpdatedDate | date |  |  | SI | Updated Date |
| REAEXOI_UpdatedTime | time |  |  | SI | Updated Time |
| REAEXOI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*