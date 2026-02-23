# SQLUser.OEC_DMOPlannedCallBackBy

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLANCALLB_RowId | bigint | PK |  | NO | - |
| PLANCALLB_Code | varchar |  |  | NO | Code |
| PLANCALLB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLANCALLB_CreatedDate | date |  |  | SI | Created Date |
| PLANCALLB_CreatedTime | time |  |  | SI | Created Time |
| PLANCALLB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLANCALLB_DateFrom | date |  |  | SI | DateFrom |
| PLANCALLB_DateTo | date |  |  | SI | DateTo |
| PLANCALLB_Desc | varchar |  |  | NO | Description |
| PLANCALLB_Owner | varchar |  |  | SI | Owner |
| PLANCALLB_UpdatedDate | date |  |  | SI | Updated Date |
| PLANCALLB_UpdatedTime | time |  |  | SI | Updated Time |
| PLANCALLB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Right Eye |
| Q02 | - |  |  | SI | Left Eye |
| Q03 | - |  |  | SI | Refractive error / Other |
| Q04 | - |  |  | SI | Refractive error / Other 2 |
| Q05 | - |  |  | SI | External / Lid / NLD |
| Q06 | - |  |  | SI | External  / Lid / NLD |
| Q07 | - |  |  | SI | Conjuctiva |
| Q08 | - |  |  | SI | Conjuctiva 2 |
| Q09 | - |  |  | SI | Cornea |
| Q10 | - |  |  | SI | Cornea 2 |
| Q11 | - |  |  | SI | Pupil |
| Q12 | - |  |  | SI | Pupil 2 |
| Q13 | - |  |  | SI | Pupil 2 |
| Q14 | - |  |  | SI | Glaucoma / AC |
| Q15 | - |  |  | SI | Glaucoma / AC 2 |
| Q16 | - |  |  | SI | Lens / Cataract |
| Q17 | - |  |  | SI | Lens / Cataract 2 |
| Q18 | - |  |  | SI | Vitreous / Retina / Optic nerve |
| Q19 | - |  |  | SI | Vitreous / Retina / Optic nerve 2 |
| Q20 | - |  |  | SI | Disposition |
| Q21 | - |  |  | SI | EOM / Strabinus / Ambyopia |
| Q22 | - |  |  | SI | EOM / Strabinus / Ambyopia 2 |
| Q23 | - |  |  | SI | Disposition |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | Time |
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