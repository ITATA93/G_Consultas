# SQLUser.PAC_AdmCancelReason

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMCR_RowId | bigint | PK |  | NO | - |
| ADMCR_AllowShowResultsEPR | varchar |  |  | SI | Allow to Show Results in EPR |
| ADMCR_AllowShowResultsEncounterRecord | varchar |  |  | SI | Allow to Show Results in Encounter Record |
| ADMCR_Code | varchar |  |  | NO | Code |
| ADMCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMCR_CreatedDate | date |  |  | SI | Created Date |
| ADMCR_CreatedTime | time |  |  | SI | Created Time |
| ADMCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMCR_DateFrom | date |  |  | SI | Date From |
| ADMCR_DateTo | date |  |  | SI | Date To |
| ADMCR_DefaultForAutoCancel | varchar |  |  | SI | DefaultForAutoCancel |
| ADMCR_Desc | varchar |  |  | NO | Description |
| ADMCR_DisplayQuestionEPR | varchar |  |  | SI | Allow Display of Questionnaire on EPR |
| ADMCR_Owner | varchar |  |  | SI | Owner |
| ADMCR_UpdatedDate | date |  |  | SI | Updated Date |
| ADMCR_UpdatedTime | time |  |  | SI | Updated Time |
| ADMCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Following the steps described in the Guidelines. O... |
| Q04 | - |  |  | SI | Get Up and Go Test result |
| Q05 | - |  |  | SI | Normal indicates that the patient gave no evidence... |
| Q06 | - |  |  | SI | Severely abnormal indicates that the patient appea... |
| Q07 | - |  |  | SI | Intermediate grades reflect the presence of any of... |
| Q08 | - |  |  | SI | Instructions |
| Q09 | - |  |  | SI | Ask the patient to perform the following series of... |
| Q10 | - |  |  | SI | 1. Sit comfortably in a straight-backed chair. |
| Q11 | - |  |  | SI | 2. Rise from the chair. |
| Q12 | - |  |  | SI | 3. Stand still momentarily. |
| Q13 | - |  |  | SI | 4. Walk a short distance (approximately 3 meters). |
| Q14 | - |  |  | SI | 6. Walk back to the chair. |
| Q15 | - |  |  | SI | 7. Turn around. |
| Q16 | - |  |  | SI | 8. Sit down in the chair |
| Q17 | - |  |  | SI | Scoring |
| Q18 | - |  |  | SI | Normal indicates that the patient gave no evidence... |
| Q19 | - |  |  | SI | Severely abnormal indicates that the patient appea... |
| Q20 | - |  |  | SI | Intermediate grades reflect the presence of any of... |
| Q21 | - |  |  | SI | Result |
| Q22 | - |  |  | SI | A patient with a score of 3 or more on the Get-up ... |
| Q23 | - |  |  | SI | The Get Up and Go Test is used to measure balance ... |
| Q24 | - |  |  | SI | 5. Turn around. |
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