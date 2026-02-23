# SQLUser.ORC_Intub_Grade

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INGRA_RowId | bigint | PK |  | NO | - |
| INGRA_Code | varchar |  |  | NO | INGRA Code |
| INGRA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INGRA_CreatedDate | date |  |  | SI | Created Date |
| INGRA_CreatedTime | time |  |  | SI | Created Time |
| INGRA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INGRA_DateFrom | date |  |  | SI | DateFrom |
| INGRA_DateTo | date |  |  | SI | DateTo |
| INGRA_Desc | varchar |  |  | NO | INGRA Description |
| INGRA_IntubationGrade | varchar |  |  | SI | Intubation Grade |
| INGRA_MallampatiScore | varchar |  |  | SI | Mallampati Score |
| INGRA_Owner | varchar |  |  | SI | Owner |
| INGRA_UpdatedDate | date |  |  | SI | Updated Date |
| INGRA_UpdatedTime | time |  |  | SI | Updated Time |
| INGRA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Family history |
| Q02 | - |  |  | SI | Clinical history |
| Q03 | - |  |  | SI | Physical examination |
| Q04 | - |  |  | SI | Investigation - LDL-cholesterol (mmol/L) |
| Q05 | - |  |  | SI | NB. This is the untreated LDL-cholesterol concentr... |
| Q06 | - |  |  | SI | Definite FH:  >8 |
| Q07 | - |  |  | SI | Probable FH: 6-8 |
| Q08 | - |  |  | SI | Possible FH: 3-5 |
| Q09 | - |  |  | SI | Unlikely FH: <3 |
| Q10 | - |  |  | SI | The DLCNS is a validated set of criteria based on ... |
| Q11 | - |  |  | SI | signs such as the presence of tendon xanthomata or... |
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