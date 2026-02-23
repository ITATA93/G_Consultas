# SQLUser.LBC_Pathogen

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPA_RowID | bigint | PK |  | NO | - |
| LBCPA_AutoCommentsRules | varchar |  |  | SI | Auto Comments Rules |
| LBCPA_AutoCommentsSelection | varchar |  |  | SI | Auto Comments Selection |
| LBCPA_BinomialRepresentation | varchar |  |  | SI | Binomial Representation |
| LBCPA_Classification | varchar |  |  | SI | Classification |
| LBCPA_Code | varchar |  |  | SI | Code |
| LBCPA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPA_CreatedDate | date |  |  | SI | Created Date |
| LBCPA_CreatedTime | time |  |  | SI | Created Time |
| LBCPA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPA_DateFrom | date |  |  | SI | Effective date for the record |
| LBCPA_DateTo | date |  |  | SI | Last day the record is active  |
| LBCPA_Desc | varchar |  |  | SI | Description
HTMLTextBox |
| LBCPA_InfectionReport | varchar |  |  | SI | Infection Report |
| LBCPA_InfectionReportTime | time |  |  | SI | Infection Report Time |
| LBCPA_National_ID | varchar |  |  | SI | National ID |
| LBCPA_Owner | varchar |  |  | SI | Owner |
| LBCPA_PathogenGroup_DR | bigint |  | FK | SI | Pathogen group |
| LBCPA_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPA_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Diagnóstico principal |
| Q02 | - |  |  | SI | Diagnóstico secundario 1 |
| Q03 | - |  |  | SI | Diagnóstico secundario 2 |
| Q04 | - |  |  | SI | Diagnóstico secundario 3 |
| Q05 | - |  |  | SI | Diagnóstico secundario 4 |
| Q06 | - |  |  | SI | Diagnóstico secundario 5 |
| Q07 | - |  |  | SI | Diagnóstico secundario 6 |
| Q08 | - |  |  | SI | Diagnóstico secundario 7 |
| Q09 | - |  |  | SI | Diagnóstico secundario 8 |
| Q10 | - |  |  | SI | Diagnóstico secundario 9 |
| Q11 | - |  |  | SI | Causa externa Dg. principal |
| Q12 | - |  |  | SI | Estado de verificación |
| Q13 | - |  |  | SI | Notas |
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