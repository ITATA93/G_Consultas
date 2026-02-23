# SQLUser.LBC_SpecimenSuitabilityCondition

**Schema:** SQLUser
**Columnas:** 59
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSSC_RowID | bigint | PK |  | NO | - |
| ChildQ01DR | - |  |  | SI | Child Reference: Via Venosa Periférica |
| LBCSSC_Active | varchar |  |  | SI | Active
Will be overwritten by LBCSSCAlwaysActive |
| LBCSSC_AlwaysActive | bit |  |  | SI | Always Active
Cannot be set via the UI |
| LBCSSC_Caption | varchar |  |  | SI | Caption |
| LBCSSC_Code | varchar |  |  | NO | Code |
| LBCSSC_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCSSC_CreatedDate | date |  |  | SI | Created Date |
| LBCSSC_CreatedTime | time |  |  | SI | Created Time |
| LBCSSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSSC_Desc | varchar |  |  | NO | Description |
| LBCSSC_Duration | integer |  |  | SI | Duration
In days |
| LBCSSC_DurationEnabled | bit |  |  | SI | Duration Enabled
Cannot be set via the UI |
| LBCSSC_IsCondition | bit |  |  | SI | Is a condition to be considered in the suitability... |
| LBCSSC_Sequence | numeric |  |  | SI | Display sequence |
| LBCSSC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSSC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q03 | - |  |  | SI | ANANO |
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