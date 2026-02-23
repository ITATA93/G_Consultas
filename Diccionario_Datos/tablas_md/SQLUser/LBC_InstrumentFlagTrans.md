# SQLUser.LBC_InstrumentFlagTrans

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINFT_ParRef | bigint | PK |  | NO | Parent instrument DR |
| CQ39 | - |  |  | SI | (null) |
| CQ67 | - |  |  | SI | (null) |
| CQ68 | - |  |  | SI | (null) |
| CQ70 | - |  |  | SI | (null) |
| CQ75 | - |  |  | SI | (null) |
| CQ76 | - |  |  | SI | (null) |
| CQ77 | - |  |  | SI | (null) |
| CQ78 | - |  |  | SI | (null) |
| CQ83 | - |  |  | SI | (null) |
| CQB13b | - |  |  | SI | (null) |
| CQB14 | - |  |  | SI | (null) |
| CQc | - |  |  | SI | (null) |
| LBCINFT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINFT_DateFrom | date |  |  | SI | Date From |
| LBCINFT_DateTo | date |  |  | SI | Date To |
| LBCINFT_Flag_DR | bigint |  | FK | SI | Internal flag |
| LBCINFT_InstrumentFlag | varchar |  |  | SI | Instrument flag |
| LBCINFT_RejectResult | varchar |  |  | SI | Reject result
Should a result flagged with this f... |
| LBCINFT_RowID | varchar |  |  | NO | - |
| Q001 | - |  |  | SI | Folio |
| Q012 | - |  |  | SI | Lugar de ocurrencia del Accidente |
| Q015 | - |  |  | SI | Fecha en que se registraron estos datos |
| Q020 | - |  |  | SI | Comuna Accidente |
| Q39 | - |  |  | SI | Tipo de Ingreso |
| Q62 | - |  |  | SI | Código del Caso |
| Q63 | - |  |  | SI | Número de Teléfono |
| Q64 | - |  |  | SI | Actividad Económica |
| Q65 | - |  |  | SI | Hombres |
| Q66 | - |  |  | SI | Mujeres |
| Q67 | - |  |  | SI | Propiedad de la Empresa |
| Q68 | - |  |  | SI | Tipo de Empresa |
| Q69 | - |  |  | SI | Actividad económica empresa principal |
| Q70 | - |  |  | SI | Tipo de Contrato |
| Q71 | - |  |  | SI | Hora de Ingreso al trabajo |
| Q72 | - |  |  | SI | Hora de salida del trabajo |
| Q73 | - |  |  | SI | Actividad antes del accidente |
| Q74 | - |  |  | SI | Trabajo Habitual |
| Q75 | - |  |  | SI | Al momento del accidente desarrollaba su trabajo h... |
| Q76 | - |  |  | SI | Clasificación del Accidente |
| Q77 | - |  |  | SI | Tipo de Accidente de Trayecto |
| Q78 | - |  |  | SI | Medio de Prueba |
| Q79 | - |  |  | SI | Detalle del Medio de Prueba |
| Q80 | - |  |  | SI | Nombre del Denunciante |
| Q81 | - |  |  | SI | RUN del Denunciante |
| Q82 | - |  |  | SI | Numero de Teléfono del Denunciante |
| Q83 | - |  |  | SI | Clasificación del Denunciante |
| QA1 | - |  |  | SI | Nombre o Razón Social |
| QA2 | - |  |  | SI | Rut Empleador |
| QA3 | - |  |  | SI | Comuna |
| QB13a | - |  |  | SI | Antiguedad en el trabajo en que se accidentó |
| QB13b | - |  |  | SI | Formato Antiguedad |
| QB14 | - |  |  | SI | Categoria Ocupacional del Accidentado |
| QC15c | - |  |  | SI | Calle y N° |
| QC16 | - |  |  | SI | Direccion del Accidente |
| QC17a | - |  |  | SI | Fecha del Accidente |
| QC17b | - |  |  | SI | Hora del Accidente |
| QC19a | - |  |  | SI | Circunstancias |
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
| Qc | - |  |  | SI | Tipo de accidente |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*