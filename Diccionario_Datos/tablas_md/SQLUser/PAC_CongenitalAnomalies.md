# SQLUser.PAC_CongenitalAnomalies

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONGANOM_RowId | bigint | PK |  | NO | - |
| CONGANOM_Active | varchar |  |  | SI | Active |
| CONGANOM_AnomType | varchar |  |  | SI | Anomaly type |
| CONGANOM_Code | varchar |  |  | NO | Code |
| CONGANOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONGANOM_CreatedDate | date |  |  | SI | Created Date |
| CONGANOM_CreatedTime | time |  |  | SI | Created Time |
| CONGANOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONGANOM_DateFrom | date |  |  | SI | Date From |
| CONGANOM_DateTo | date |  |  | SI | DateTo |
| CONGANOM_Desc | varchar |  |  | NO | Description |
| CONGANOM_NationalCode | varchar |  |  | SI | National Code |
| CONGANOM_Owner | varchar |  |  | SI | Owner |
| CONGANOM_UpdatedDate | date |  |  | SI | Updated Date |
| CONGANOM_UpdatedTime | time |  |  | SI | Updated Time |
| CONGANOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ10DR | - |  |  | SI | Child Reference: Review of precautions |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Commencement date of precautions |
| Q04 | - |  |  | SI | Precautions required |
| Q05 | - |  |  | SI | Organism |
| Q06 | - |  |  | SI | Other organism |
| Q07 | - |  |  | SI | Infection site |
| Q08 | - |  |  | SI | Other infection site |
| Q09 | - |  |  | SI | Precaution notes |
| Q11 | - |  |  | SI | Date of clearance from precautions |
| Q12 | - |  |  | SI | Clearance notes |
| Q13 | - |  |  | SI | Cleared by |
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