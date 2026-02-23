# SQLUser.PAC_AltWorkTypeCode

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AWTC_RowId | bigint | PK |  | NO | - |
| AWTC_Code | varchar |  |  | NO | Code |
| AWTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AWTC_CreatedDate | date |  |  | SI | Created Date |
| AWTC_CreatedTime | time |  |  | SI | Created Time |
| AWTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AWTC_DateFrom | date |  |  | SI | Date From |
| AWTC_DateTo | date |  |  | SI | Date To |
| AWTC_Desc | varchar |  |  | NO | Description |
| AWTC_Owner | varchar |  |  | SI | Owner |
| AWTC_UpdatedDate | date |  |  | SI | Updated Date |
| AWTC_UpdatedTime | time |  |  | SI | Updated Time |
| AWTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | How soon after you wake do you smoke your first ci... |
| Q04 | - |  |  | SI | How many cigarettes do you typically smoke per day... |
| Q05 | - |  |  | SI | Score |
| Q06 | - |  |  | SI | Classification |
| Q07 | - |  |  | SI | 0 - 2 |
| Q08 | - |  |  | SI | Low Nicotine Dependence |
| Q09 | - |  |  | SI | 3 - 4 |
| Q10 | - |  |  | SI | Medium Nicotine Dependence |
| Q11 | - |  |  | SI | 5 - 6 |
| Q12 | - |  |  | SI | High Nicotine Dependence |
| Q13 | - |  |  | SI | The Heaviness of Smoking Index (HSI) was developed... |
| Q14 | - |  |  | SI | 0 - 2: Low Nicotine Dependence |
| Q15 | - |  |  | SI | 3 - 4: Medium Nicotine Dependence |
| Q16 | - |  |  | SI | 5 - 6: High Nicotine Dependence |
| Q17 | - |  |  | SI | Guidelines |
| Q18 | - |  |  | SI | The Heaviness of Smoking Index (HSI) is a subset o... |
| Q19 | - |  |  | SI | The two-question HSI may be used in situations whe... |
| Q20 | - |  |  | SI | Dummy 1 |
| Q21 | - |  |  | SI | Dummy 2 |
| Q22 | - |  |  | SI | Dummy 3 |
| Q23 | - |  |  | SI | Heatherton TF |
| Q24 | - |  |  | SI | Using self-reported time to the first cigarette of... |
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