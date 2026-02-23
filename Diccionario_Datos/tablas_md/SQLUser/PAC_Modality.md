# SQLUser.PAC_Modality

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MODAL_RowId | bigint | PK |  | NO | - |
| MODAL_Code | varchar |  |  | NO | Code |
| MODAL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MODAL_CreatedDate | date |  |  | SI | Created Date |
| MODAL_CreatedTime | time |  |  | SI | Created Time |
| MODAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MODAL_Desc | varchar |  |  | NO | Description |
| MODAL_Owner | varchar |  |  | SI | Owner |
| MODAL_UpdatedDate | date |  |  | SI | Updated Date |
| MODAL_UpdatedTime | time |  |  | SI | Updated Time |
| MODAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Age |
| Q02 | - |  |  | SI | APACHE II |
| Q03 | - |  |  | SI | SOFA |
| Q04 | - |  |  | SI | Number of co-morbidities |
| Q05 | - |  |  | SI | Days from hospital to ICU admission |
| Q06 | - |  |  | SI | IL-6 |
| Q07 | - |  |  | SI | NUTRIC Score scoring system : if IL-6 available |
| Q08 | - |  |  | SI | 6 -10 : High Score |
| Q09 | - |  |  | SI | Associated with worse clinical outcomes (mortality... |
| Q10 | - |  |  | SI | 0 - 5 : Low Score |
| Q11 | - |  |  | SI | NUTRIC Score scoring system : if NO IL-6 available |
| Q12 | - |  |  | SI | 5 - 9 : High Score |
| Q13 | - |  |  | SI | Associated with worse clinical outcomes (mortality... |
| Q14 | - |  |  | SI | 0 - 4 : Low Score |
| Q15 | - |  |  | SI | These patients have a low malnutrition risk. |
| Q16 | - |  |  | SI | The NUTRIC score is designed to quantify the risk ... |
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