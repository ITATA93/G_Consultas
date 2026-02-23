# SQLUser.LBC_Courier

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCC_RowID | bigint | PK |  | NO | - |
| LBCC_Code | varchar |  |  | NO | Code |
| LBCC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCC_Confidential | varchar |  |  | SI | Confidential |
| LBCC_ConfidentialLabSite_DR | bigint |  | FK | SI | Confidential Site
The LabSite for which the couri... |
| LBCC_CourierBatch_DR | bigint |  | FK | SI | Courier Batch
The Batch definition (type C) to us... |
| LBCC_CreatedDate | date |  |  | SI | Created Date |
| LBCC_CreatedTime | time |  |  | SI | Created Time |
| LBCC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCC_DateFrom | date |  |  | SI | Effective date for the record |
| LBCC_DateTo | date |  |  | SI | Last day the record is active  |
| LBCC_Desc | varchar |  |  | NO | Description |
| LBCC_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCC_Owner | varchar |  |  | SI | Owner |
| LBCC_QuickPrintBatch_DR | bigint |  | FK | SI | QuickPrint Batch
The QuickPrint Batch definition ... |
| LBCC_SinglePatientBatch_DR | bigint |  | FK | SI | SinglePatient Batch
The Single-Patient Batch defi... |
| LBCC_Timeslot | integer |  |  | SI | The Timeslot interval for creating Doctors Reports... |
| LBCC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Risk factors |
| Q04 | - |  |  | SI | Other risk factor details |
| Q05 | - |  |  | SI | Clinical presentation |
| Q06 | - |  |  | SI | Other symptoms |
| Q07 | - |  |  | SI | Papilloedema |
| Q08 | - |  |  | SI | Clinical exam details |
| Q09 | - |  |  | SI | Drug choice intensive phase |
| Q10 | - |  |  | SI | Intensive phase start date |
| Q11 | - |  |  | SI | Intensive phase stop date |
| Q12 | - |  |  | SI | Drug choice consolidation phase |
| Q13 | - |  |  | SI | Consolidation phase |
| Q14 | - |  |  | SI | Cryptococcal immune reconstitution inflammatory sy... |
| Q15 | - |  |  | SI | Treatment required |
| Q16 | - |  |  | SI | Treatment details |
| Q17 | - |  |  | SI | Drug toxicities |
| Q18 | - |  |  | SI | Repeat lumbar puncture date |
| Q19 | - |  |  | SI | Relevant culture results |
| Q20 | - |  |  | SI | Repeat chest X-ray date |
| Q21 | - |  |  | SI | Relevant chest X-ray findings |
| Q22 | - |  |  | SI | Surgical management is required due to Central Ner... |
| Q23 | - |  |  | SI | Surgical management for CNS details |
| Q24 | - |  |  | SI | Surgical management required for pulmonary disease |
| Q25 | - |  |  | SI | Surgical management for pulmonary details |
| Q26 | - |  |  | SI | Planned further management |
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