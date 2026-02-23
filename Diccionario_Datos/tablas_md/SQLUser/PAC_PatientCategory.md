# SQLUser.PAC_PatientCategory

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PCAT_RowId | bigint | PK |  | NO | - |
| PCAT_Code | varchar |  |  | NO | Code |
| PCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PCAT_CreatedDate | date |  |  | SI | Created Date |
| PCAT_CreatedTime | time |  |  | SI | Created Time |
| PCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PCAT_DateFrom | date |  |  | SI | DateFrom |
| PCAT_DateTo | date |  |  | SI | DateTo |
| PCAT_Desc | varchar |  |  | NO | Description |
| PCAT_Owner | varchar |  |  | SI | Owner |
| PCAT_UpdatedDate | date |  |  | SI | Updated Date |
| PCAT_UpdatedTime | time |  |  | SI | Updated Time |
| PCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Clock time |
| Q11 | - |  |  | SI | Etiology / Event |
| Q12 | - |  |  | SI | Pathology deficits |
| Q13 | - |  |  | SI | Provenance details |
| Q14 | - |  |  | SI | Jackson WT, Novack TA, Dowler RN. Effective serial... |
| Q15 | - |  |  | SI | Guidelines |
| Q16 | - |  |  | SI | Incorrect responses should be followed by cuing at... |
| Q17 | - |  |  | SI | In the place domain, hospital in any context is su... |
| Q18 | - |  |  | SI | In the domain of time, month, date, year, and day ... |
| Q19 | - |  |  | SI | However, clock time can be correct to within 30 mi... |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Patients are allowed to look at a clock without pe... |
| Q21 | - |  |  | SI | For situation, the patient must be oriented to bot... |
| Q22 | - |  |  | SI | And pathology / deficits (e.g., what kind of injur... |
| Q23 | - |  |  | SI | Situational responses must demonstrate awareness o... |
| Q24 | - |  |  | SI | Add scores down each column and plot total. |
| Q25 | - |  |  | SI | The Orientation Log (O-Log) is designed to be a qu... |
| Q3 | - |  |  | SI | City |
| Q4 | - |  |  | SI | Kind of place |
| Q5 | - |  |  | SI | Name of hospital |
| Q6 | - |  |  | SI | Month |
| Q7 | - |  |  | SI | Date |
| Q8 | - |  |  | SI | Year |
| Q9 | - |  |  | SI | Day of week |
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