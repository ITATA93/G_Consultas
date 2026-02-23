# SQLUser.ORC_PrenatalScreenTestsDone

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRSCTE_RowId | bigint | PK |  | NO | - |
| PRSCTE_Code | varchar |  |  | NO | Code |
| PRSCTE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRSCTE_CreatedDate | date |  |  | SI | Created Date |
| PRSCTE_CreatedTime | time |  |  | SI | Created Time |
| PRSCTE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRSCTE_DateFrom | date |  |  | SI | Date From |
| PRSCTE_DateTo | date |  |  | SI | Date To |
| PRSCTE_Desc | varchar |  |  | NO | Description |
| PRSCTE_Owner | varchar |  |  | SI | Owner |
| PRSCTE_UpdatedDate | date |  |  | SI | Updated Date |
| PRSCTE_UpdatedTime | time |  |  | SI | Updated Time |
| PRSCTE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Indication for EEG |
| Q04 | - |  |  | SI | Date of EEG |
| Q05 | - |  |  | SI | EEG number |
| Q06 | - |  |  | SI | Type of EEG |
| Q07 | - |  |  | SI | Other type of EEG |
| Q08 | - |  |  | SI | Relevant clinical history |
| Q09 | - |  |  | SI | Drugs taken by the patient that may affect EEG res... |
| Q10 | - |  |  | SI | Other relevant drugs |
| Q11 | - |  |  | SI | Technical difficulties encountered during the test |
| Q12 | - |  |  | SI | Report summary |
| Q13 | - |  |  | SI | Conclusion / Impression |
| Q14 | - |  |  | SI | Referring consultant |
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