# SQLUser.ARC_ItemDietModifier

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DM_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| DM_Childsub | double |  |  | NO | Childsub |
| DM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DM_CreatedDate | date |  |  | SI | Created Date |
| DM_CreatedTime | time |  |  | SI | Created Time |
| DM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DM_DateFrom | date |  |  | SI | Date From |
| DM_DateTo | date |  |  | SI | Date To |
| DM_Default | varchar |  |  | SI | Default |
| DM_Modifier_DR | bigint |  | FK | SI | Des Ref Modifier |
| DM_RowId | varchar |  |  | NO | - |
| DM_UpdatedDate | date |  |  | SI | Updated Date |
| DM_UpdatedTime | time |  |  | SI | Updated Time |
| DM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Age |
| Q02 | - |  |  | SI | Blood pressure |
| Q03 | - |  |  | SI | Clinical feature of TIA |
| Q04 | - |  |  | SI | Duration |
| Q05 | - |  |  | SI | Diabetes |
| Q06 | - |  |  | SI | The ABCD score assesses a patient risk of short-te... |
| Q07 | - |  |  | SI | The score is optimized to predict the risk of stro... |
| Q08 | - |  |  | SI | A higher number is associated with a greater risk ... |
| Q09 | - |  |  | SI | 0 - 3: 1.0% of 2-day stroke risk |
| Q09a | - |  |  | SI | Hospital observation may be unnecessary without an... |
| Q11 | - |  |  | SI | 4 - 5: 4.1% of 2-day stroke risk |
| Q11a | - |  |  | SI | Hospital observation justified in most situations |
| Q13 | - |  |  | SI | 6 - 7: 8.1% of 2-day stroke risk |
| Q14 | - |  |  | SI | Hospital observation worthwhile |
| Q15 | - |  |  | SI | Score |
| Q16 | - |  |  | SI | Classification |
| Q17 | - |  |  | SI | 0 - 3 |
| Q18 | - |  |  | SI | 1.0% of 2-day stroke risk |
| Q19 | - |  |  | SI | 4 - 5 |
| Q20 | - |  |  | SI | 4.1% of 2-day stroke risk |
| Q21 | - |  |  | SI | 6 - 7 |
| Q22 | - |  |  | SI | 8.1% of 2-day stroke risk |
| Q23 | - |  |  | SI | Date |
| Q24 | - |  |  | SI | Tme |
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