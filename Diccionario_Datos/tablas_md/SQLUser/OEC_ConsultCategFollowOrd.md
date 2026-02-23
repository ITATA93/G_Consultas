# SQLUser.OEC_ConsultCategFollowOrd

**Schema:** SQLUser
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FOL_ParRef | bigint | PK |  | NO | OEC_ConsultCateg Parent Reference |
| FOL_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| FOL_Childsub | double |  |  | NO | Childsub |
| FOL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FOL_CreatedDate | date |  |  | SI | Created Date |
| FOL_CreatedTime | time |  |  | SI | Created Time |
| FOL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FOL_Default | varchar |  |  | SI | Default |
| FOL_RowId | varchar |  |  | NO | - |
| FOL_UpdatedDate | date |  |  | SI | Updated Date |
| FOL_UpdatedTime | time |  |  | SI | Updated Time |
| FOL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Physical Condition |
| Q02 | - |  |  | SI | Mental Condition |
| Q03 | - |  |  | SI | Activity |
| Q04 | - |  |  | SI | Mobility |
| Q05 | - |  |  | SI | Incontinence |
| Q06 | - |  |  | SI | > 18: Low risk |
| Q07 | - |  |  | SI | 14 - 18: Medium risk |
| Q08 | - |  |  | SI | 10 - 14: High risk |
| Q09 | - |  |  | SI | < 10: Very high risk |
| Q10 | - |  |  | SI | The Norton scale assesses a patients risk of devel... |
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