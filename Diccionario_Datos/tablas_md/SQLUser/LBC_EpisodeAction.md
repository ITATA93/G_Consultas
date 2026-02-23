# SQLUser.LBC_EpisodeAction

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCEA_RowID | bigint | PK |  | NO | - |
| LBCEA_Code | varchar |  |  | NO | Code |
| LBCEA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCEA_Comments | varchar |  |  | SI | Comments |
| LBCEA_CreatedDate | date |  |  | SI | Created Date |
| LBCEA_CreatedTime | time |  |  | SI | Created Time |
| LBCEA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCEA_DateFrom | date |  |  | SI | Effective date for the record |
| LBCEA_DateTo | date |  |  | SI | Last day the record is active  |
| LBCEA_Desc | varchar |  |  | NO | Description |
| LBCEA_InterimRegistration | varchar |  |  | SI | Interim Registration |
| LBCEA_Owner | varchar |  |  | SI | Owner |
| LBCEA_SuppressBilling | varchar |  |  | SI | Suppress Billing |
| LBCEA_SuppressReports | varchar |  |  | SI | Suppress Doctors Reports |
| LBCEA_UpdatedDate | date |  |  | SI | Updated Date |
| LBCEA_UpdatedTime | time |  |  | SI | Updated Time |
| LBCEA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02 | - |  |  | SI | Blood glucose concentration |
| Q02ObsDR | - |  |  | SI | Blood glucose concentration DR |
| Q03 | - |  |  | SI | If hypoglycaemic, treat and reassess |
| Q04 | - |  |  | SI | Other sudden symptoms |
| Q05 | - |  |  | SI | Use the below guide when carrying out a FAST scree... |
| Q06 | - |  |  | SI | Facial Movements |
| Q07 | - |  |  | SI | Ask patient to smile or show teeth |
| Q08 | - |  |  | SI | Look for NEW lack of symmetry |
| Q09 | - |  |  | SI | Arm Movements |
| Q10 | - |  |  | SI | Lift the patient's arms together (90 degrees if si... |
| Q11 | - |  |  | SI | Look for one arm drifting down or falling rapidly. |
| Q12 | - |  |  | SI | Speech |
| Q13 | - |  |  | SI | If the patient attempts a conversation: |
| Q14 | - |  |  | SI | Look for NEW disturbance of speech |
| Q15 | - |  |  | SI | Check with companion |
| Q16 | - |  |  | SI | Look for slurred speech |
| Q17 | - |  |  | SI | Look for word-finding difficulties. This can be co... |
| Q18 | - |  |  | SI | If there is a severe visual disturbance, place an ... |
| Q19 | - |  |  | SI | Action to be taken if stroke onset within a certai... |
| Q20 | - |  |  | SI | Emergency Department: If suspected stroke and symp... |
| Q21 | - |  |  | SI | Label for own instructions 1 |
| Q22 | - |  |  | SI | Label for own instructions 2 |
| Q23 | - |  |  | SI | Date |
| Q24 | - |  |  | SI | Time |
| Q25 | - |  |  | SI | mmol/L |
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