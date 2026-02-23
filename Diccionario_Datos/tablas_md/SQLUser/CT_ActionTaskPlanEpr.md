# SQLUser.CT_ActionTaskPlanEpr

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPR_ParRef | bigint | PK |  | NO | CT_ActionTaskPlan Parent Reference |
| EPR_Childsub | double |  |  | NO | Childsub |
| EPR_CreatedDate | date |  |  | SI | Created Date |
| EPR_CreatedTime | time |  |  | SI | Created Time |
| EPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EPR_NumberOfDays | double |  |  | SI | Number of days from the previous stage |
| EPR_RowId | varchar |  |  | NO | - |
| EPR_Sequence | double |  |  | SI | Sequence |
| EPR_Task_DR | bigint |  | FK | SI | Des Ref epr.Task |
| EPR_UpdatedDate | date |  |  | SI | Updated Date |
| EPR_UpdatedTime | time |  |  | SI | Updated Time |
| EPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Problema de Salud Ricarte Soto |
| Q02 | - |  |  | SI | Diagnóstico del Paciente Asociado a Ricarte Soto |
| Q03 | - |  |  | SI | Estado Problema de Salud Ricarte Soto |
| Q04 | - |  |  | SI | Fecha Sospecha Fundada |
| Q05 | - |  |  | SI | Comentario Sospecha Fundada |
| Q06 | - |  |  | SI | Hora Sospecha Fundada |
| Q07 | - |  |  | SI | Fecha Confirmación Diagnóstica |
| Q08 | - |  |  | SI | Etapa Clínica |
| Q09 | - |  |  | SI | Fecha Cierre de Caso |
| Q10 | - |  |  | SI | Motivo Cierre de Caso |
| Q11 | - |  |  | SI | Comentario Cierre de Caso |
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