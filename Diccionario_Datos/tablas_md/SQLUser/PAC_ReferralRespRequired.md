# SQLUser.PAC_ReferralRespRequired

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFRR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Age ≥ 50 years |
| Q04 | - |  |  | SI | HR ≥ 100 bpm |
| Q05 | - |  |  | SI | Oxygen saturation on room air < 95% |
| Q06 | - |  |  | SI | Unilateral leg swelling |
| Q07 | - |  |  | SI | Hemoptysis |
| Q08 | - |  |  | SI | Recent surgery or trauma |
| Q09 | - |  |  | SI | Prior pulmonary embolism or deep vein thrombosis |
| Q10 | - |  |  | SI | Hormone use |
| Q11 | - |  |  | SI | Defintions |
| Q12 | - |  |  | SI | Recent surgery or trauma: |
| Q13 | - |  |  | SI | Surgery or trauma ≤ 4 weeks ago requiring treatmen... |
| Q14 | - |  |  | SI | Hormone use: |
| Q15 | - |  |  | SI | Oral contraceptives, hormone replacement or estrog... |
| Q16 | - |  |  | SI | When to Use: |
| Q17 | - |  |  | SI | The PERC rule should only be considered for use wh... |
| Q18 | - |  |  | SI | it should not be applied to all patients in whom a... |
| Q19 | - |  |  | SI | If one or more criteria are positive, pulmonary em... |
| Q20 | - |  |  | SI | Score |
| Q21 | - |  |  | SI | Classification |
| Q22 | - |  |  | SI | 1 - 8 |
| Q23 | - |  |  | SI | One or more positive criteria. Pulmonary embolism ... |
| Q24 | - |  |  | SI | 1 - 8: One or more positive criteria. Pulmonary em... |
| Q25 | - |  |  | SI | The PERC rule is used to rule out pulmonary emboli... |
| Q26 | - |  |  | SI | Requirements for this questionnaire have been comp... |
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
| REFRR_Code | varchar |  |  | NO | Code |
| REFRR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFRR_CreatedDate | date |  |  | SI | Created Date |
| REFRR_CreatedTime | time |  |  | SI | Created Time |
| REFRR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFRR_DateFrom | date |  |  | SI | Date From |
| REFRR_DateTo | date |  |  | SI | Date To |
| REFRR_Desc | varchar |  |  | NO | Description |
| REFRR_Owner | varchar |  |  | SI | Owner |
| REFRR_UpdatedDate | date |  |  | SI | Updated Date |
| REFRR_UpdatedTime | time |  |  | SI | Updated Time |
| REFRR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*