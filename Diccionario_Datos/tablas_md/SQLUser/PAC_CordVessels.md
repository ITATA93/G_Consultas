# SQLUser.PAC_CordVessels

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLCVSLS_RowId | bigint | PK |  | NO | - |
| PLCVSLS_Active | varchar |  |  | SI | PLCVSLS_Active |
| PLCVSLS_Code | varchar |  |  | NO | Code |
| PLCVSLS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLCVSLS_CreatedDate | date |  |  | SI | Created Date |
| PLCVSLS_CreatedTime | time |  |  | SI | Created Time |
| PLCVSLS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLCVSLS_DateFrom | date |  |  | SI | Date From |
| PLCVSLS_DateTo | date |  |  | SI | Date To |
| PLCVSLS_Desc | varchar |  |  | NO | Description |
| PLCVSLS_NationalCode | varchar |  |  | SI | National code |
| PLCVSLS_Owner | varchar |  |  | SI | Owner |
| PLCVSLS_UpdatedDate | date |  |  | SI | Updated Date |
| PLCVSLS_UpdatedTime | time |  |  | SI | Updated Time |
| PLCVSLS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fertilization procedure |
| Q02 | - |  |  | SI | Cycle number |
| Q03 | - |  |  | SI | Sperm extraction method |
| Q04 | - |  |  | SI | Number of follicles aspirated (left ovary) |
| Q05 | - |  |  | SI | Number of follicles aspirated (right ovary) |
| Q06 | - |  |  | SI | Number of oocytes retrieved (left ovary) |
| Q07 | - |  |  | SI | Number of oocytes retrieved (right ovary) |
| Q08 | - |  |  | SI | Complications |
| Q09 | - |  |  | SI | Comments |
| Q10 | - |  |  | SI | Physician |
| Q11 | - |  |  | SI | Embryologist |
| Q12 | - |  |  | SI | Date |
| Q13 | - |  |  | SI | Time |
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