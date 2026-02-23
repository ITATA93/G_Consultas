# SQLUser.INC_POReference

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| POREF_RowId | bigint | PK |  | NO | - |
| ChildQ27DR | - |  |  | SI | Child Reference: Chest drain assessment |
| POREF_Code | varchar |  |  | NO | Code |
| POREF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| POREF_CreatedDate | date |  |  | SI | Created Date |
| POREF_CreatedTime | time |  |  | SI | Created Time |
| POREF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| POREF_Desc | varchar |  |  | NO | Description |
| POREF_Owner | varchar |  |  | SI | Owner |
| POREF_UpdatedDate | date |  |  | SI | Updated Date |
| POREF_UpdatedTime | time |  |  | SI | Updated Time |
| POREF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Pre-Procedure Checklist |
| Q04 | - |  |  | SI | Explained procedure to patient and verified consen... |
| Q05 | - |  |  | SI | Aseptic technique used |
| Q06 | - |  |  | SI | Skin disinfected with |
| Q07 | - |  |  | SI | Other skin disinfection |
| Q08 | - |  |  | SI | Local anaesthetic used |
| Q09 | - |  |  | SI | Pre-procedure notes |
| Q10 | - |  |  | SI | Insertion Details |
| Q11 | - |  |  | SI | Insertion reason |
| Q12 | - |  |  | SI | Other insertion reason |
| Q13 | - |  |  | SI | Insertion date |
| Q14 | - |  |  | SI | Insertion time |
| Q15 | - |  |  | SI | Drain identifier |
| Q16 | - |  |  | SI | Catheter type |
| Q17 | - |  |  | SI | Size of catheter (French) |
| Q18 | - |  |  | SI | Insertion site laterality |
| Q19 | - |  |  | SI | Insertion site |
| Q20 | - |  |  | SI | Other insertion site |
| Q21 | - |  |  | SI | Drainage unit type |
| Q22 | - |  |  | SI | Post-insertion checklist |
| Q23 | - |  |  | SI | Insertion notes |
| Q24 | - |  |  | SI | Inserted by |
| Q25 | - |  |  | SI | Assistant |
| Q26 | - |  |  | SI | Assessment |
| Q28 | - |  |  | SI | Removal Details |
| Q29 | - |  |  | SI | Removal date |
| Q30 | - |  |  | SI | Removal time |
| Q31 | - |  |  | SI | Removal reason |
| Q32 | - |  |  | SI | Other removal reason |
| Q33 | - |  |  | SI | Catheter tip sent for microbiology culture and sen... |
| Q34 | - |  |  | SI | Removal notes |
| Q35 | - |  |  | SI | Removed by 1 |
| Q36 | - |  |  | SI | Removed by 2 |
| Q37 | - |  |  | SI | Complications |
| Q38 | - |  |  | SI | Complications |
| Q39 | - |  |  | SI | Other complications |
| Q40 | - |  |  | SI | Complication notes |
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