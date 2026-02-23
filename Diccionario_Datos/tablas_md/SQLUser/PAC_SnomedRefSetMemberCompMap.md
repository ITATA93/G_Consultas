# SQLUser.PAC_SnomedRefSetMemberCompMap

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNORFSCM_RowId | bigint | PK |  | NO | - |
| ChildQ09DR | - |  |  | SI | Child Reference: Add action(s) for postpartum haem... |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Obstetric emergency called at |
| Q04 | - |  |  | SI | Obstetric emergency called at |
| Q05 | - |  |  | SI | Type of emergency |
| Q06 | - |  |  | SI | Other type of emergency |
| Q07 | - |  |  | SI | Placenta birthed |
| Q13 | - |  |  | SI | Notes |
| Q14 | - |  |  | SI | Hauspurg A, Jeyabalan A. Postpartum preeclampsia o... |
| Q15 | - |  |  | SI | Available from: https://www.ajog.org/article/S0002... |
| Q16 | - |  |  | SI | Pacheco LD, Saade G, Hankins GDV, Clark SL. Amniot... |
| Q17 | - |  |  | SI | The following questionnaire is to be used to docum... |
| Q18 | - |  |  | SI | Call for help at |
| Q19 | - |  |  | SI | Call for help at |
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
| SNORFSCM_Correlation_DR | bigint |  | FK | SI | Correlation Id |
| SNORFSCM_CreatedDate | date |  |  | SI | Created Date |
| SNORFSCM_CreatedTime | time |  |  | SI | Created Time |
| SNORFSCM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNORFSCM_MapAdvice | varchar |  |  | SI | Map Advice |
| SNORFSCM_MapCategory_DR | bigint |  | FK | SI | Map Category Id |
| SNORFSCM_MapGroup | integer |  |  | SI | Map Group |
| SNORFSCM_MapPriority | integer |  |  | SI | Map Priority |
| SNORFSCM_MapRule | varchar |  |  | SI | Map Rule |
| SNORFSCM_MapTarget | varchar |  |  | SI | Map Target |
| SNORFSCM_RefSetMember_DR | bigint |  | FK | SI | Des Ref PACSnomedRefSetMember |
| SNORFSCM_UpdatedDate | date |  |  | SI | Updated Date |
| SNORFSCM_UpdatedTime | time |  |  | SI | Updated Time |
| SNORFSCM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*