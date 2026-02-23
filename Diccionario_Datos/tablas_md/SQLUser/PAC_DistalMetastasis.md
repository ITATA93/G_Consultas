# SQLUser.PAC_DistalMetastasis

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISM_RowId | bigint | PK |  | NO | - |
| DISM_Code | varchar |  |  | NO | Code |
| DISM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DISM_CreatedDate | date |  |  | SI | Created Date |
| DISM_CreatedTime | time |  |  | SI | Created Time |
| DISM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DISM_Desc | varchar |  |  | NO | Description |
| DISM_Owner | varchar |  |  | SI | Owner |
| DISM_UpdatedDate | date |  |  | SI | Updated Date |
| DISM_UpdatedTime | time |  |  | SI | Updated Time |
| DISM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Activity level |
| Q04 | - |  |  | SI | Respiration |
| Q05 | - |  |  | SI | Circulation (systolic blood pressure) |
| Q06 | - |  |  | SI | Consciousness |
| Q07 | - |  |  | SI | Oxygen saturation |
| Q08 | - |  |  | SI | 1 - 8 |
| Q09 | - |  |  | SI | Patient should NOT be discharged |
| Q10 | - |  |  | SI | 9 - 10 |
| Q11 | - |  |  | SI | Patient can be discharged |
| Q12 | - |  |  | SI | 1 - 8: Patient should NOT be discharged |
| Q13 | - |  |  | SI | 9 - 10: Patient can be discharged |
| Q14 | - |  |  | SI | The Modified Aldrete score is used to evaluate pat... |
| Q15 | - |  |  | SI | The score considers consciousness, mobility, breat... |
| Q16 | - |  |  | SI | Score |
| Q17 | - |  |  | SI | Classification |
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