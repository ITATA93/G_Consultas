# SQLUser.NRC_CarePlanGoal

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Enfermería**. Parámetros de enfermería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPGOAL_RowId | bigint | PK |  | NO | - |
| CPGOAL_Code | varchar |  |  | SI | Code |
| CPGOAL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CPGOAL_CreatedDate | date |  |  | SI | Created Date |
| CPGOAL_CreatedTime | time |  |  | SI | Created Time |
| CPGOAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CPGOAL_DateFrom | date |  |  | SI | Date From |
| CPGOAL_DateTo | date |  |  | SI | Date To |
| CPGOAL_Desc | varchar |  |  | SI | Description |
| CPGOAL_IssueGoal | varchar |  |  | SI | Issue Goal |
| CPGOAL_Owner | varchar |  |  | SI | Owner |
| CPGOAL_ProblemGoal | varchar |  |  | SI | Problem Goal |
| CPGOAL_UpdatedDate | date |  |  | SI | Updated Date |
| CPGOAL_UpdatedTime | time |  |  | SI | Updated Time |
| CPGOAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Difficulty or pain with urination |
| Q01N | - |  |  | SI | Note |
| Q02 | - |  |  | SI | Difficulty or pain with urination checkboxes |
| Q02N | - |  |  | SI | Note |
| Q03 | - |  |  | SI | Flank / CVA pain |
| Q03N | - |  |  | SI | Note |
| Q04 | - |  |  | SI | Penile discharge |
| Q04N | - |  |  | SI | Note |
| Q05 | - |  |  | SI | Penile pain |
| Q05N | - |  |  | SI | Note |
| Q06 | - |  |  | SI | Penile swelling |
| Q06N | - |  |  | SI | Note |
| Q07 | - |  |  | SI | Testicle pain |
| Q07N | - |  |  | SI | Note |
| Q08 | - |  |  | SI | Testicle swelling |
| Q08N | - |  |  | SI | Note |
| Q09 | - |  |  | SI | Injury |
| Q09N | - |  |  | SI | Note |
| Q10 | - |  |  | SI | Injury checkbox |
| Q10N | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Prior urological surgery |
| Q11N | - |  |  | SI | Note |
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