# SQLUser.LBC_ReagentCondition

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCREC_RowID | bigint | PK |  | NO | - |
| LBCREC_Code | varchar |  |  | SI | Code |
| LBCREC_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCREC_CreatedDate | date |  |  | SI | Created Date |
| LBCREC_CreatedTime | time |  |  | SI | Created Time |
| LBCREC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCREC_DateFrom | date |  |  | SI | Date From |
| LBCREC_DateTo | date |  |  | SI | Date To |
| LBCREC_Desc | varchar |  |  | SI | Description |
| LBCREC_Owner | varchar |  |  | SI | Owner |
| LBCREC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCREC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCREC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Sedantes |
| Q02 | - |  |  | SI | Antieméticos |
| Q03 | - |  |  | SI | Exanguinación |
| Q04 | - |  |  | SI | Tiempo de Insuflación |
| Q05 | - |  |  | SI | Observaciones |
| Q06 | - |  |  | SI | Ubicación |
| Q07 | - |  |  | SI | Número (#) |
| Q08 | - |  |  | SI | Descriptión |
| Q09 | - |  |  | SI | Observaciones |
| Q10 | - |  |  | SI | ANANO |
| Q11 | - |  |  | SI | Presión de Insuflación |
| Q12 | - |  |  | SI | Ubicación (T) |
| Q13 | - |  |  | SI | Hora de inicio de Isquemia |
| Q13ObsDR | - |  |  | SI | Hora de inicio de Isquemia DR |
| Q14 | - |  |  | SI | Hora de término de Isquemia |
| Q14ObsDR | - |  |  | SI | Hora de término de Isquemia DR |
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