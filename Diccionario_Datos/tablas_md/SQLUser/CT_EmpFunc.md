# SQLUser.CT_EmpFunc

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTEMF_RowID | bigint | PK |  | NO | - |
| CTEMF_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTEMF_Code | varchar |  |  | NO | Employee Function Code |
| CTEMF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTEMF_CreatedDate | date |  |  | SI | Created Date |
| CTEMF_CreatedTime | time |  |  | SI | Created Time |
| CTEMF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTEMF_Desc | varchar |  |  | NO | Employee Function Description |
| CTEMF_Owner | varchar |  |  | SI | Owner |
| CTEMF_UpdatedDate | date |  |  | SI | Updated Date |
| CTEMF_UpdatedTime | time |  |  | SI | Updated Time |
| CTEMF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q10 | - |  |  | SI | Do you drink alcohol? |
| Q11 | - |  |  | SI | Allows care providers to record answers to questio... |
| Q12 | - |  |  | SI | Date |
| Q13 | - |  |  | SI | Time |
| Q14 | - |  |  | SI | Bush K, Kivlahan DR, McDonell MB, Fihn SD, Bradley... |
| Q2 | - |  |  | SI | Complete Audit C |
| Q3 | - |  |  | SI | Audit C questions |
| Q4 | - |  |  | SI | How often did you have a drink containing alcohol ... |
| Q5 | - |  |  | SI | How many drinks did you have on a typical day when... |
| Q6 | - |  |  | SI | How often did you have 6 or more drinks on one occ... |
| Q7 | - |  |  | SI | Brief intervention given and patient information l... |
| Q8 | - |  |  | SI | Local Community Alcohol Service Information given |
| Q9 | - |  |  | SI | Has the patient been referred to specialist servic... |
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