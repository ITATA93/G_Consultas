# SQLUser.PAC_WLStatusList

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLSL_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Level of consciousness |
| Q04 | - |  |  | SI | Activity |
| Q05 | - |  |  | SI | Neuromuscular control |
| Q06 | - |  |  | SI | Muscle tone |
| Q07 | - |  |  | SI | Posture |
| Q08 | - |  |  | SI | Stretch reflexes |
| Q09 | - |  |  | SI | Complex / Primitive reflexes |
| Q10 | - |  |  | SI | Suck |
| Q11 | - |  |  | SI | Moro (startle) |
| Q12 | - |  |  | SI | Tonic neck |
| Q13 | - |  |  | SI | Pupils |
| Q14 | - |  |  | SI | Heart rate |
| Q15 | - |  |  | SI | Seizures |
| Q16 | - |  |  | SI | • The numeric scale relates to the stages of Hypox... |
| Q17 | - |  |  | SI | Stage 1 (Mild) |
| Q18 | - |  |  | SI | Stage 2 (Moderate) |
| Q19 | - |  |  | SI | Stage 3 (Severe) |
| Q20 | - |  |  | SI | • Severity |
| Q21 | - |  |  | SI | Autonomic Function |
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
| WLSL_Code | varchar |  |  | NO | Code |
| WLSL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLSL_CreatedDate | date |  |  | SI | Created Date |
| WLSL_CreatedTime | time |  |  | SI | Created Time |
| WLSL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLSL_Desc | varchar |  |  | NO | Description |
| WLSL_Owner | varchar |  |  | SI | Owner |
| WLSL_UpdatedDate | date |  |  | SI | Updated Date |
| WLSL_UpdatedTime | time |  |  | SI | Updated Time |
| WLSL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*