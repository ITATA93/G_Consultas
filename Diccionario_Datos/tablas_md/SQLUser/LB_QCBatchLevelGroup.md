# SQLUser.LB_QCBatchLevelGroup

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBQCBLG_ParRef | varchar | PK |  | NO | Parent Batch Level |
| ChildQ15DR | - |  |  | SI | Child Reference: Nombre de quienes realizan la vis... |
| LBQCBLG_AllLevelsRequired | varchar |  |  | SI | QC from all levels must pass for this test item to... |
| LBQCBLG_Comments | varchar |  |  | SI | Comments |
| LBQCBLG_GroupType | varchar |  |  | SI | Value Group Type
StandardType: LabQCValueGroupTyp... |
| LBQCBLG_InstrumentGroup_DR | bigint |  | FK | SI | Instrument Group |
| LBQCBLG_Instrument_DR | bigint |  | FK | SI | Instrument |
| LBQCBLG_RowID | varchar |  |  | NO | - |
| LBQCBLG_WorksheetGroup_DR | bigint |  | FK | SI | Worksheet Group |
| LBQCBLG_Worksheet_DR | bigint |  | FK | SI | Worksheet  |
| Q01 | - |  |  | SI | ¿Se concreta la visita? |
| Q02 | - |  |  | SI | Domicilio no corresponde |
| Q03 | - |  |  | SI | No hay nadie en la vivienda |
| Q04 | - |  |  | SI | No acepta la visita |
| Q05 | - |  |  | SI | Otro Motivo |
| Q06 | - |  |  | SI | Fecha de la visita |
| Q07 | - |  |  | SI | Nombre de quienes realizan la visita |
| Q08 | - |  |  | SI | Apellidos |
| Q09 | - |  |  | SI | Nombre |
| Q10 | - |  |  | SI | Profesión |
| Q11 | - |  |  | SI | ¿Se confirma situación de riesgo Psicosocial? |
| Q12 | - |  |  | SI | Se detecta riesgo en las siguientes áreas |
| Q13 | - |  |  | SI | Especificar cuál |
| Q14 | - |  |  | SI | Observaciones |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*