# SQLUser.PAC_ComplaintPriority

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COMPRI_RowId | bigint | PK |  | NO | - |
| COMPRI_Code | varchar |  |  | NO | Code |
| COMPRI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COMPRI_Color | varchar |  |  | SI | Color |
| COMPRI_CreatedDate | date |  |  | SI | Created Date |
| COMPRI_CreatedTime | time |  |  | SI | Created Time |
| COMPRI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COMPRI_DateFrom | date |  |  | SI | Date From |
| COMPRI_DateTo | date |  |  | SI | Date To |
| COMPRI_Desc | varchar |  |  | NO | Description |
| COMPRI_Owner | varchar |  |  | SI | Owner |
| COMPRI_UpdatedDate | date |  |  | SI | Updated Date |
| COMPRI_UpdatedTime | time |  |  | SI | Updated Time |
| COMPRI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | In the past month |
| Q02 | - |  |  | SI | How often have you had the sensation of not emptyi... |
| Q03 | - |  |  | SI | How often have you had to urinate less than every ... |
| Q04 | - |  |  | SI | How often have you found you stopped and started a... |
| Q05 | - |  |  | SI | How often have you found it difficult to postpone ... |
| Q06 | - |  |  | SI | How often have you had a weak urinary stream? |
| Q07 | - |  |  | SI | How often have you had to strain to start urinatio... |
| Q08 | - |  |  | SI | How many times did you typically get up at night t... |
| Q09 | - |  |  | SI | If you were to spend the rest of your life with yo... |
| Q10 | - |  |  | SI | The International Prostate Symptom Score (I-PSS) q... |
| Q11 | - |  |  | SI | Score |
| Q12 | - |  |  | SI | Classification |
| Q13 | - |  |  | SI | 0 |
| Q14 | - |  |  | SI | No symptoms |
| Q15 | - |  |  | SI | 1 - 7 |
| Q16 | - |  |  | SI | Mild |
| Q17 | - |  |  | SI | 8 - 19 |
| Q18 | - |  |  | SI | Moderate |
| Q19 | - |  |  | SI | 20 - 35 |
| Q20 | - |  |  | SI | Severe |
| Q21 | - |  |  | SI | 0: No symptoms |
| Q22 | - |  |  | SI | 1 - 7: Mild |
| Q23 | - |  |  | SI | 8 - 19: Moderate |
| Q24 | - |  |  | SI | 20 - 35: Severe |
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