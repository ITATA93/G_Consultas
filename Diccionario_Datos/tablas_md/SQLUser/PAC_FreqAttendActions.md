# SQLUser.PAC_FreqAttendActions

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FAA_RowId | bigint | PK |  | NO | - |
| FAA_Code | varchar |  |  | NO | Code |
| FAA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FAA_CommentsMandatory | varchar |  |  | SI | CommentsMandatory |
| FAA_CreatedDate | date |  |  | SI | Created Date |
| FAA_CreatedTime | time |  |  | SI | Created Time |
| FAA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FAA_DateFrom | date |  |  | SI | DateFrom |
| FAA_DateTo | date |  |  | SI | DateTo |
| FAA_Desc | varchar |  |  | NO | Description |
| FAA_Owner | varchar |  |  | SI | Owner |
| FAA_UpdatedDate | date |  |  | SI | Updated Date |
| FAA_UpdatedTime | time |  |  | SI | Updated Time |
| FAA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Imaging destination |
| Q04 | - |  |  | SI | Other imaging |
| Q05 | - |  |  | SI | Requirements Checklist |
| Q06 | - |  |  | SI | High risk patient screening completed |
| Q07 | - |  |  | SI | Escort required to remain with the patient |
| Q08 | - |  |  | SI | Type of escort required |
| Q09 | - |  |  | SI | Other escort type |
| Q10 | - |  |  | SI | Mobility status |
| Q11 | - |  |  | SI | Mobility aids |
| Q12 | - |  |  | SI | Other mobility aids |
| Q13 | - |  |  | SI | Dummy1 |
| Q14 | - |  |  | SI | Dummy2 |
| Q15 | - |  |  | SI | High Risk Critieria |
| Q16 | - |  |  | SI | Children (< 16yrs) unless accompanied by a family ... |
| Q17 | - |  |  | SI | Requiring cardiac monitoring |
| Q18 | - |  |  | SI | Requiring airway management |
| Q19 | - |  |  | SI | Dummy7 |
| Q20 | - |  |  | SI | Dummy8 |
| Q21 | - |  |  | SI | Dummy9 |
| Q22 | - |  |  | SI | Dummy10 |
| Q23 | - |  |  | SI | Dummy11 |
| Q24 | - |  |  | SI | Dummy12 |
| Q25 | - |  |  | SI | Dummy13 |
| Q26 | - |  |  | SI | Dummy14 |
| Q27 | - |  |  | SI | Dummy15 |
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