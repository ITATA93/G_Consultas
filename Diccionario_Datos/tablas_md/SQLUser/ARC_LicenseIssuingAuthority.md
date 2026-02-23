# SQLUser.ARC_LicenseIssuingAuthority

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LICIAU_RowId | bigint | PK |  | NO | - |
| LICIAU_Code | varchar |  |  | NO | Code |
| LICIAU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LICIAU_CreatedDate | date |  |  | SI | Created Date |
| LICIAU_CreatedTime | time |  |  | SI | Created Time |
| LICIAU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LICIAU_DateFrom | date |  |  | SI | Date From |
| LICIAU_DateTo | date |  |  | SI | Date To |
| LICIAU_Desc | varchar |  |  | NO | Description |
| LICIAU_Owner | varchar |  |  | SI | Owner |
| LICIAU_UpdatedDate | date |  |  | SI | Updated Date |
| LICIAU_UpdatedTime | time |  |  | SI | Updated Time |
| LICIAU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Tipo de Evaluación |
| Q02 | - |  |  | SI | 15 seg |
| Q03 | - |  |  | SI | 30 seg |
| Q04 | - |  |  | SI | 45 seg |
| Q05 | - |  |  | SI | 1 min |
| Q06 | - |  |  | SI | 1 min 15 seg |
| Q07 | - |  |  | SI | 1 min 30 seg |
| Q08 | - |  |  | SI | 1 min 45 seg |
| Q09 | - |  |  | SI | 2 min |
| Q10 | - |  |  | SI | 2 min 15 seg |
| Q11 | - |  |  | SI | 2 min 30 seg |
| Q12 | - |  |  | SI | 2 min 45 seg |
| Q13 | - |  |  | SI | 3 min |
| Q14 | - |  |  | SI | 3 min 15 seg |
| Q15 | - |  |  | SI | 3 min 30 seg |
| Q16 | - |  |  | SI | 3 min 45 seg |
| Q17 | - |  |  | SI | 4 min |
| Q18 | - |  |  | SI | 4 min 15 seg |
| Q19 | - |  |  | SI | 4 min 30 seg |
| Q20 | - |  |  | SI | 4 min 45 seg |
| Q21 | - |  |  | SI | 5 min |
| Q22 | - |  |  | SI | Cociente de Salivación |
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