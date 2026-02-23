# SQLUser.PAC_ReferralReason

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFREA_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Cord appearance |
| Q04 | - |  |  | SI | Cord appearance notes |
| Q05 | - |  |  | SI | Total cord length (cm) |
| Q06 | - |  |  | SI | Presence of cord knots |
| Q07 | - |  |  | SI | Cord knots notes |
| Q08 | - |  |  | SI | Placental diameter (cm) |
| Q09 | - |  |  | SI | Placental weight (g) |
| Q10 | - |  |  | SI | Placenta odour |
| Q11 | - |  |  | SI | Maternal surface |
| Q12 | - |  |  | SI | Other maternal surface notes |
| Q13 | - |  |  | SI | Umbilical cord sample collected |
| Q14 | - |  |  | SI | Notes |
| Q15 | - |  |  | SI | Examine placenta using sterile gloves. |
| Q16 | - |  |  | SI | Prior to sending the placenta to pathology, collec... |
| Q17 | - |  |  | SI | Place in appropriate specimen container labelled w... |
| Q18 | - |  |  | SI | If there are any clinical indications of placental... |
| Q19 | - |  |  | SI | When sending placenta to pathology it is required ... |
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
| REFREA_Code | varchar |  |  | NO | Code |
| REFREA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFREA_CreatedDate | date |  |  | SI | Created Date |
| REFREA_CreatedTime | time |  |  | SI | Created Time |
| REFREA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFREA_DateFrom | date |  |  | SI | DateFrom |
| REFREA_DateTo | date |  |  | SI | DateTo |
| REFREA_Desc | varchar |  |  | NO | Description |
| REFREA_Owner | varchar |  |  | SI | Owner |
| REFREA_UpdatedDate | date |  |  | SI | Updated Date |
| REFREA_UpdatedTime | time |  |  | SI | Updated Time |
| REFREA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*