# SQLUser.PAC_AdmReadmRehab

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARR_RowId | bigint | PK |  | NO | - |
| ARR_Code | varchar |  |  | NO | Code |
| ARR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARR_CreatedDate | date |  |  | SI | Created Date |
| ARR_CreatedTime | time |  |  | SI | Created Time |
| ARR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARR_DateFrom | date |  |  | SI | Date From |
| ARR_DateTo | date |  |  | SI | Date To |
| ARR_Default | varchar |  |  | SI | Default |
| ARR_Desc | varchar |  |  | NO | Description |
| ARR_Owner | varchar |  |  | SI | Owner |
| ARR_UpdatedDate | date |  |  | SI | Updated Date |
| ARR_UpdatedTime | time |  |  | SI | Updated Time |
| ARR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | General well-being: for the previous day, as repor... |
| Q04 | - |  |  | SI | Abdominal pain: for the previous day, as reported ... |
| Q05 | - |  |  | SI | Number of liquid / soft stools for the previous da... |
| Q06 | - |  |  | SI | Exact number of liquid / soft stools |
| Q07 | - |  |  | SI | Abdominal mass |
| Q08 | - |  |  | SI | Complications |
| Q09 | - |  |  | SI | Arthralgia |
| Q10 | - |  |  | SI | Uveitis |
| Q11 | - |  |  | SI | Erithema nodosum |
| Q12 | - |  |  | SI | Aphthous ulcers |
| Q13 | - |  |  | SI | Pyoderma gangrenosum |
| Q14 | - |  |  | SI | Anal fissures |
| Q15 | - |  |  | SI | New fistula |
| Q16 | - |  |  | SI | Abscess |
| Q17 | - |  |  | SI | Score |
| Q18 | - |  |  | SI | Classification |
| Q19 | - |  |  | SI | < 5 |
| Q20 | - |  |  | SI | Remission |
| Q21 | - |  |  | SI | 5 - 7 |
| Q22 | - |  |  | SI | Mild disease |
| Q23 | - |  |  | SI | 8 - 16 |
| Q24 | - |  |  | SI | Moderate disease |
| Q25 | - |  |  | SI | > 16 |
| Q26 | - |  |  | SI | Severe disease |
| Q27 | - |  |  | SI | < 5: Remission |
| Q28 | - |  |  | SI | 5 - 7: Mild disease |
| Q29 | - |  |  | SI | 8 - 16: Moderate disease |
| Q30 | - |  |  | SI | > 16: Severe disease |
| Q31 | - |  |  | SI | The Harvey Bradshaw Index (HBI) is a stratificatio... |
| Q32 | - |  |  | SI | Number of liquid / soft stools for the previous da... |
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