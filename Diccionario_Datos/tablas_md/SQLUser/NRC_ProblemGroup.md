# SQLUser.NRC_ProblemGroup

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Enfermería**. Parámetros de enfermería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NRCPG_RowID | bigint | PK |  | NO | - |
| NRCPG_Code | varchar |  |  | SI | Code |
| NRCPG_CodeTableTags | varchar |  |  | SI | List of code table tags |
| NRCPG_CreatedDate | date |  |  | SI | Created Date |
| NRCPG_CreatedTime | time |  |  | SI | Created Time |
| NRCPG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NRCPG_DateFrom | date |  |  | SI | Date From |
| NRCPG_DateTo | date |  |  | SI | Date To |
| NRCPG_Desc | varchar |  |  | SI | Description |
| NRCPG_Owner | varchar |  |  | SI | Owner |
| NRCPG_UpdatedDate | date |  |  | SI | Updated Date |
| NRCPG_UpdatedTime | time |  |  | SI | Updated Time |
| NRCPG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Reason for admission |
| Q02 | - |  |  | SI | IV cannula required |
| Q02ObsDR | - |  |  | SI | IV cannula required DR |
| Q03 | - |  |  | SI | IV cannula sited |
| Q03ObsDR | - |  |  | SI | IV cannula sited DR |
| Q04 | - |  |  | SI | IV fluids required |
| Q04ObsDR | - |  |  | SI | IV fluids required DR |
| Q05 | - |  |  | SI | IV fluids prescribed |
| Q05ObsDR | - |  |  | SI | IV fluids prescribed DR |
| Q06 | - |  |  | SI | Medicines required |
| Q06ObsDR | - |  |  | SI | Medicines required DR |
| Q07 | - |  |  | SI | Medicines prescribed |
| Q07ObsDR | - |  |  | SI | Medicines prescribed DR |
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