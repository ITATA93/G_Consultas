# SQLUser.OEC_RouteAdmin

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADM_ParRef | bigint | PK |  | NO | OEC_Route Parent Reference |
| ADM_AdminRoute_DR | bigint |  | FK | SI | Des Ref AdminRoute |
| ADM_Childsub | double |  |  | NO | Childsub |
| ADM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADM_CreatedDate | date |  |  | SI | Created Date |
| ADM_CreatedTime | time |  |  | SI | Created Time |
| ADM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADM_RowId | varchar |  |  | NO | - |
| ADM_UpdatedDate | date |  |  | SI | Updated Date |
| ADM_UpdatedTime | time |  |  | SI | Updated Time |
| ADM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Shortness of breath / Dyspnoea |
| Q010 | - |  |  | SI | Note |
| Q011N | - |  |  | SI | Note |
| Q012N | - |  |  | SI | Note |
| Q01N | - |  |  | SI | Note |
| Q02 | - |  |  | SI | Shortness of breath / Dyspnoea status |
| Q03 | - |  |  | SI | Cough |
| Q03N | - |  |  | SI | Note |
| Q04 | - |  |  | SI | Cough status |
| Q05 | - |  |  | SI | Sputum |
| Q06 | - |  |  | SI | Sputum colour |
| Q07 | - |  |  | SI | Haemoptysis |
| Q07N | - |  |  | SI | Note |
| Q08 | - |  |  | SI | Haemoptysis status |
| Q09 | - |  |  | SI | Fever / Chills |
| Q09N | - |  |  | SI | Note |
| Q10 | - |  |  | SI | Asthma history |
| Q11 | - |  |  | SI | Asthma medications |
| Q12 | - |  |  | SI | Stridor |
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