# SQLUser.ARC_ItemFoodTextureMod

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITFTM_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| ITFTM_Childsub | double |  |  | NO | Childsub |
| ITFTM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITFTM_CreatedDate | date |  |  | SI | Created Date |
| ITFTM_CreatedTime | time |  |  | SI | Created Time |
| ITFTM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITFTM_DefaultFlag | varchar |  |  | SI | Default Flag |
| ITFTM_FoodTextureMod_DR | bigint |  | FK | SI | Des Ref DTCFoodTextureMod |
| ITFTM_RowId | varchar |  |  | NO | - |
| ITFTM_UpdatedDate | date |  |  | SI | Updated Date |
| ITFTM_UpdatedTime | time |  |  | SI | Updated Time |
| ITFTM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Shower / Bathing premorbid |
| Q04 | - |  |  | SI | Shower / Bathing current |
| Q05 | - |  |  | SI | Dressing premorbid |
| Q06 | - |  |  | SI | Dressing current |
| Q07 | - |  |  | SI | Grooming premorbid |
| Q08 | - |  |  | SI | Grooming current |
| Q09 | - |  |  | SI | Toileting premorbid |
| Q10 | - |  |  | SI | Toileting current |
| Q11 | - |  |  | SI | Eating premorbid |
| Q12 | - |  |  | SI | Eating current |
| Q13 | - |  |  | SI | Mobility premorbid |
| Q14 | - |  |  | SI | Mobility current |
| Q15 | - |  |  | SI | Referrals required |
| Q16 | - |  |  | SI | Shower / Bathing |
| Q17 | - |  |  | SI | Dressing |
| Q18 | - |  |  | SI | Grooming |
| Q19 | - |  |  | SI | Toileting |
| Q20 | - |  |  | SI | Eating |
| Q21 | - |  |  | SI | Mobility |
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