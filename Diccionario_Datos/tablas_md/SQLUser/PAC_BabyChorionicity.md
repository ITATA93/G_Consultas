# SQLUser.PAC_BabyChorionicity

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CHOR_RowId | bigint | PK |  | NO | - |
| CHOR_Code | varchar |  |  | NO | Code |
| CHOR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CHOR_CreatedDate | date |  |  | SI | Created Date |
| CHOR_CreatedTime | time |  |  | SI | Created Time |
| CHOR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CHOR_DateFrom | date |  |  | SI | Date From |
| CHOR_DateTo | date |  |  | SI | Date To |
| CHOR_Desc | varchar |  |  | NO | Description |
| CHOR_Owner | varchar |  |  | SI | Owner |
| CHOR_UpdatedDate | date |  |  | SI | Updated Date |
| CHOR_UpdatedTime | time |  |  | SI | Updated Time |
| CHOR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ12DR | - |  |  | SI | Child Reference: Intracranial pressure catheter as... |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Insertion date |
| Q04 | - |  |  | SI | Insertion time |
| Q05 | - |  |  | SI | Insertion reason |
| Q06 | - |  |  | SI | Other insertion reason |
| Q07 | - |  |  | SI | Zero transducer (pre-insertion only) |
| Q08 | - |  |  | SI | Reference number |
| Q08ObsDR | - |  |  | SI | Reference number DR |
| Q09 | - |  |  | SI | Calibration |
| Q10 | - |  |  | SI | Insertion notes |
| Q11 | - |  |  | SI | Inserted by |
| Q13 | - |  |  | SI | Removal date |
| Q14 | - |  |  | SI | Removal time |
| Q15 | - |  |  | SI | Removal reason |
| Q16 | - |  |  | SI | Other removal reason |
| Q17 | - |  |  | SI | Removal notes |
| Q18 | - |  |  | SI | Catheter sent for microbiology culture and sensiti... |
| Q19 | - |  |  | SI | Removed by |
| Q20 | - |  |  | SI | Complications |
| Q21 | - |  |  | SI | Other complications |
| Q22 | - |  |  | SI | Complication notes |
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