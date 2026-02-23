# SQLUser.ORC_NeonateAutopsy

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NEOAUT_RowId | bigint | PK |  | NO | - |
| NEOAUT_Code | varchar |  |  | NO | Code |
| NEOAUT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NEOAUT_CreatedDate | date |  |  | SI | Created Date |
| NEOAUT_CreatedTime | time |  |  | SI | Created Time |
| NEOAUT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NEOAUT_DateFrom | date |  |  | SI | Date From |
| NEOAUT_DateTo | date |  |  | SI | Date To |
| NEOAUT_Desc | varchar |  |  | NO | Description |
| NEOAUT_Owner | varchar |  |  | SI | Owner |
| NEOAUT_UpdatedDate | date |  |  | SI | Updated Date |
| NEOAUT_UpdatedTime | time |  |  | SI | Updated Time |
| NEOAUT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | If a response of 'Yes' is chosen for any of the fo... |
| Q04 | - |  |  | SI | If a response of 'Yes' is chosen for any of the fo... |
| Q05 | - |  |  | SI | Does the patient have a disability or other health... |
| Q06 | - |  |  | SI | Specify |
| Q07 | - |  |  | SI | Does patient live alone |
| Q08 | - |  |  | SI | Discharge location |
| Q09 | - |  |  | SI | Is the patient the main carer for someone else or ... |
| Q10 | - |  |  | SI | If yes, consider referral to social work |
| Q11 | - |  |  | SI | Does the patient already receive community support... |
| Q12 | - |  |  | SI | Is there evidence of functional decline or not cop... |
| Q13 | - |  |  | SI | Does the patient / carer / next of kin have concer... |
| Q14 | - |  |  | SI | Is the patient or their family members concerned a... |
| Q15 | - |  |  | SI | Are clinicians concerned about the patient returni... |
| Q16 | - |  |  | SI | Notes |
| Q17 | - |  |  | SI | Other location |
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