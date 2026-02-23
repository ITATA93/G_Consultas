# SQLUser.LBC_AdditionalBloodGroupSystem

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCABGS_RowID | bigint | PK |  | NO | - |
| ChildQ11DR | - |  |  | SI | Child Reference: Consejería Familiar |
| LBCABGS_Code | varchar |  |  | NO | Code |
| LBCABGS_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCABGS_CreatedDate | date |  |  | SI | Created Date |
| LBCABGS_CreatedTime | time |  |  | SI | Created Time |
| LBCABGS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCABGS_DateFrom | date |  |  | SI | Effective date for the record |
| LBCABGS_DateTo | date |  |  | SI | Last day the record is active |
| LBCABGS_Desc | varchar |  |  | NO | Description |
| LBCABGS_Owner | varchar |  |  | SI | Owner |
| LBCABGS_UpdatedDate | date |  |  | SI | Updated Date |
| LBCABGS_UpdatedTime | time |  |  | SI | Updated Time |
| LBCABGS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Consejería Familiar |
| Q02 | - |  |  | SI | Con Riesgo Psicosocial |
| Q03 | - |  |  | SI | Con integrante de patología crónica |
| Q04 | - |  |  | SI | Con integrante con problema de salud mental |
| Q05 | - |  |  | SI | Con adulto mayor dependiente |
| Q06 | - |  |  | SI | Con adulto mayor con demencia |
| Q07 | - |  |  | SI | Con integrante con enfermedad terminal |
| Q08 | - |  |  | SI | Con integrante dependiente severo |
| Q09 | - |  |  | SI | Otras áreas de intervención |
| Q10 | - |  |  | SI | Temas Prioridad |
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