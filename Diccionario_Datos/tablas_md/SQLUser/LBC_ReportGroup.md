# SQLUser.LBC_ReportGroup

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRG_RowID | bigint | PK |  | NO | - |
| LBCRG_Code | varchar |  |  | NO | Code |
| LBCRG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRG_CreatedDate | date |  |  | SI | Created Date |
| LBCRG_CreatedTime | time |  |  | SI | Created Time |
| LBCRG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCRG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCRG_DateTo | date |  |  | SI | Last day the record is active  |
| LBCRG_Desc | varchar |  |  | NO | Description |
| LBCRG_Owner | varchar |  |  | SI | Owner |
| LBCRG_ReportGroupTime | integer |  |  | SI | This property defines the age (in seconds) after A... |
| LBCRG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCRG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCRG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Bañarse |
| Q02 | - |  |  | SI | Vestirse |
| Q03 | - |  |  | SI | Usar el Inodoro |
| Q04 | - |  |  | SI | Trasladarse |
| Q05 | - |  |  | SI | Continencia |
| Q06 | - |  |  | SI | Alimentarse |
| Q07 | - |  |  | SI | Dependiente en las seis funciones (Todas) |
| Q08 | - |  |  | SI | Resultado Indice de Katz |
| Q08ObsDR | - |  |  | SI | Resultado Indice de Katz DR |
| Q09 | - |  |  | SI | Usar cuestionario sólo en pacientes dependientes. |
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