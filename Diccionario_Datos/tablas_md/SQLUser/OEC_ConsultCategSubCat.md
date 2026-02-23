# SQLUser.OEC_ConsultCategSubCat

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUB_ParRef | bigint | PK |  | NO | OEC_ConsultCateg Parent Reference |
| Q01 | - |  |  | SI | Cornea |
| Q02 | - |  |  | SI | Pupils |
| Q03 | - |  |  | SI | Notes |
| Q04 | - |  |  | SI | Notes |
| Q05 | - |  |  | SI | Right Eye |
| Q06 | - |  |  | SI | Left Eye |
| Q07 | - |  |  | SI | Notes |
| Q08 | - |  |  | SI | Anterior Chamber |
| Q09 | - |  |  | SI | Grading |
| Q10 | - |  |  | SI | Grading |
| Q11 | - |  |  | SI | Cells |
| Q12 | - |  |  | SI | Cells 2 |
| Q13 | - |  |  | SI | Flare |
| Q14 | - |  |  | SI | Flare 2 |
| Q15 | - |  |  | SI | Notes |
| Q16 | - |  |  | SI | Lens |
| Q17 | - |  |  | SI | Left Eye |
| Q18 | - |  |  | SI | Right Eye |
| Q19 | - |  |  | SI | Uveitis |
| Q20 | - |  |  | SI | (Describe and Draw using the image link above) |
| Q21 | - |  |  | SI | Notes |
| Q22 | - |  |  | SI | Haze |
| Q23 | - |  |  | SI | Haze 2 |
| Q24 | - |  |  | SI | Cells |
| Q25 | - |  |  | SI | Cells 2 |
| Q26 | - |  |  | SI | Right Eye |
| Q27 | - |  |  | SI | Left Eye |
| Q28 | - |  |  | SI | Notes |
| Q29 | - |  |  | SI | Notes |
| Q30 | - |  |  | SI | Exam Method |
| Q31 | - |  |  | SI | Type |
| Q32 | - |  |  | SI | Grading 2_1 |
| Q33 | - |  |  | SI | Grading 2_2 |
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
| SUB_Childsub | double |  |  | NO | Childsub |
| SUB_Code | varchar |  |  | SI | Code |
| SUB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUB_CreatedDate | date |  |  | SI | Created Date |
| SUB_CreatedTime | time |  |  | SI | Created Time |
| SUB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUB_Desc | varchar |  |  | SI | Description |
| SUB_RowId | varchar |  |  | NO | - |
| SUB_UpdatedDate | date |  |  | SI | Updated Date |
| SUB_UpdatedTime | time |  |  | SI | Updated Time |
| SUB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*