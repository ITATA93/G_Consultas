# SQLUser.CT_CurrencyDenomination

**Schema:** SQLUser
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CURRDOM_RowId | bigint | PK |  | NO | - |
| CURRDOM_Code | varchar |  |  | NO | Code |
| CURRDOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CURRDOM_CreatedDate | date |  |  | SI | Created Date |
| CURRDOM_CreatedTime | time |  |  | SI | Created Time |
| CURRDOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CURRDOM_DateFrom | date |  |  | SI | Date From |
| CURRDOM_DateTo | date |  |  | SI | Date To |
| CURRDOM_Desc | varchar |  |  | NO | Description |
| CURRDOM_DisplayOnly | varchar |  |  | SI | Process |
| CURRDOM_Factor | double |  |  | SI | Factor |
| CURRDOM_Owner | varchar |  |  | SI | Owner |
| CURRDOM_Sequence | double |  |  | SI | Sequence |
| CURRDOM_UpdatedDate | date |  |  | SI | Updated Date |
| CURRDOM_UpdatedTime | time |  |  | SI | Updated Time |
| CURRDOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Cirugía de alto riesgo (intervención intraperitone... |
| Q02 | - |  |  | SI | Cardiopatía isquémica (por cualquier criterio de d... |
| Q03 | - |  |  | SI | Antecedente de insuficiencia cardíaca congestiva |
| Q04 | - |  |  | SI | Antecedente de enfermedad cerebrovascular |
| Q05 | - |  |  | SI | Diabetes mellitus que precisa insulina |
| Q06 | - |  |  | SI | Creatinina > 2 mg/dl (176 µmol/l) |
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