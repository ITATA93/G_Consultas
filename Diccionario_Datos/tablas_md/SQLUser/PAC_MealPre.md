# SQLUser.PAC_MealPre

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MP_RowID | bigint | PK |  | NO | - |
| MP_Code | varchar |  |  | NO | Code |
| MP_CreatedDate | date |  |  | SI | Created Date |
| MP_CreatedTime | time |  |  | SI | Created Time |
| MP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MP_Description | varchar |  |  | SI | Description |
| MP_UpdatedDate | date |  |  | SI | Updated Date |
| MP_UpdatedTime | time |  |  | SI | Updated Time |
| MP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Recommended for children less than 1 year old |
| Q02 | - |  |  | SI | Facial Expression |
| Q03 | - |  |  | SI | Cry |
| Q04 | - |  |  | SI | Breathing Pattern |
| Q05 | - |  |  | SI | Arms |
| Q06 | - |  |  | SI | Legs |
| Q07 | - |  |  | SI | State of Arousal |
| Q08 | - |  |  | SI | 0-2 = mild to no pain |
| Q09 | - |  |  | SI | 3-4 = mild to moderate pain |
| Q10 | - |  |  | SI | >4 = severe pain |
| Q11 | - |  |  | SI | Intervention |
| Q12 | - |  |  | SI | None |
| Q13 | - |  |  | SI | Non-pharmacological intervention with a reassessme... |
| Q14 | - |  |  | SI | Non-pharmacological intervention and possibly a ph... |
| Q15 | - |  |  | SI | Total pain scores range from 0-7. The suggested in... |
| Q16 | - |  |  | SI | and agitation, however, the non-pharmacological in... |
| Q17 | - |  |  | SI | (i.e. changing the wet diaper, feeding the infant,... |
| Q18 | - |  |  | SI | 0-2 = mild to no pain |
| Q19 | - |  |  | SI | 3-4 = mild to moderate pain |
| Q20 | - |  |  | SI | >4 = severe pain |
| Q21 | - |  |  | SI | Date |
| Q22 | - |  |  | SI | Time |
| Q23 | - |  |  | SI | Type of assessment |
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