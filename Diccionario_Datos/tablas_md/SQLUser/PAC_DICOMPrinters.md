# SQLUser.PAC_DICOMPrinters

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DCPR_RowId | bigint | PK |  | NO | - |
| DCPR_Code | varchar |  |  | NO | Code |
| DCPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DCPR_CreatedDate | date |  |  | SI | Created Date |
| DCPR_CreatedTime | time |  |  | SI | Created Time |
| DCPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DCPR_Desc | varchar |  |  | NO | Description |
| DCPR_IPAddress | varchar |  |  | SI | IP Address |
| DCPR_Owner | varchar |  |  | SI | Owner |
| DCPR_PortNo | varchar |  |  | SI | Port No |
| DCPR_UpdatedDate | date |  |  | SI | Updated Date |
| DCPR_UpdatedTime | time |  |  | SI | Updated Time |
| DCPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Bathing |
| Q04 | - |  |  | SI | Dressing |
| Q05 | - |  |  | SI | Toileting |
| Q06 | - |  |  | SI | Transferring |
| Q07 | - |  |  | SI | Continence |
| Q08 | - |  |  | SI | Feeding |
| Q09 | - |  |  | SI | BATHING |
| Q10 | - |  |  | SI | DRESSING |
| Q11 | - |  |  | SI | TOILETING |
| Q12 | - |  |  | SI | TRANSFERRING |
| Q13 | - |  |  | SI | CONTINENCE |
| Q14 | - |  |  | SI | FEEDING |
| Q15 | - |  |  | SI | 6: High (patient independent) |
| Q16 | - |  |  | SI | 0: Low (patient very dependent) |
| Q17 | - |  |  | SI | Katz Index of Activities of Daily Living (Modified... |
| Q18 | - |  |  | SI | Katz Index of Activities of Daily Living (Modified... |
| Q19 | - |  |  | SI | Provenance |
| Q20 | - |  |  | SI | 1. Katz S, Ford AB, Moskowitz RW, Jackson BA, Jaff... |
| Q21 | - |  |  | SI | 2. Wallace M, Shelkey M, Nursing HI for G. Katz In... |
| Q22 | - |  |  | SI | References |
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