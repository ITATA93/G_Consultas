# SQLUser.PAC_PathwayItemGoal

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPIG_ParRef | varchar | PK |  | NO | Parent Reference |
| PACPIC_NursingOutcome_DR | bigint |  | FK | SI | Condition - Nursing Outcome |
| PACPIG_Childsub | double |  |  | NO | Childsub |
| PACPIG_Code | varchar |  |  | SI | Code |
| PACPIG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACPIG_CreatedDate | date |  |  | SI | Created Date |
| PACPIG_CreatedTime | time |  |  | SI | Created Time |
| PACPIG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPIG_Desc | varchar |  |  | SI | Description |
| PACPIG_FreeText | varchar |  |  | SI | Condition - Free-text |
| PACPIG_NursingOutcomeMinValue | integer |  |  | SI | Condition - Nursing Outcome Minimum Value |
| PACPIG_PHFreq_DR | bigint |  | FK | SI | Frequency |
| PACPIG_Period | integer |  |  | SI | Period - Time from the beginning of the pathway by... |
| PACPIG_PeriodType | varchar |  |  | SI | Period duration type |
| PACPIG_RowId | varchar |  |  | NO | - |
| PACPIG_UpdatedDate | date |  |  | SI | Updated Date |
| PACPIG_UpdatedTime | time |  |  | SI | Updated Time |
| PACPIG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PACPIG_VisualRule_DR | bigint |  | FK | SI | Condition - Visual Rule |
| Q01 | - |  |  | SI | Primary tumor |
| Q02 | - |  |  | SI | Visceral metastases |
| Q03 | - |  |  | SI | Bone metastases (including spine) |
| Q04 | - |  |  | SI | Score : 2 - 3: Treatment & Surgical Strategy: Long... |
| Q05 | - |  |  | SI | Score : 4 - 5: Treatment & Surgical Strategy: Midd... |
| Q06 | - |  |  | SI | Score : 6 - 7: Treatment & Surgical Strategy: Shor... |
| Q07 | - |  |  | SI | Score : 8 - 10: Treatment & Surgical Strategy: Ter... |
| Q08 | - |  |  | SI | The Tomita score, is composed of 3 parameters base... |
| Q09 | - |  |  | SI | The score is used to formulate surgical strategy f... |
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