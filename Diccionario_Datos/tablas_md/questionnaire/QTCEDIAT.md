# questionnaire.QTCEDIAT

> Declaración Individual de Accidente de Trabajo

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Declaración Individual de Accidente de Trabajo

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ39 | varchar |  |  | SI | - |
| CQ67 | varchar |  |  | SI | - |
| CQ68 | varchar |  |  | SI | - |
| CQ70 | varchar |  |  | SI | - |
| CQ75 | varchar |  |  | SI | - |
| CQ76 | varchar |  |  | SI | - |
| CQ77 | varchar |  |  | SI | - |
| CQ78 | varchar |  |  | SI | - |
| CQ83 | varchar |  |  | SI | - |
| CQB13b | varchar |  |  | SI | - |
| CQB14 | varchar |  |  | SI | - |
| CQc | varchar |  |  | SI | - |
| Q001 | varchar |  |  | SI | Folio |
| Q012 | varchar |  |  | SI | Lugar de ocurrencia del Accidente |
| Q015 | date |  |  | SI | Fecha en que se registraron estos datos |
| Q020 | varchar |  |  | SI | Comuna Accidente |
| Q39 | varchar |  |  | SI | Tipo de Ingreso |
| Q62 | varchar |  |  | SI | Código del Caso |
| Q63 | numeric |  |  | SI | Número de Teléfono |
| Q64 | varchar |  |  | SI | Actividad Económica |
| Q65 | numeric |  |  | SI | Hombres |
| Q66 | numeric |  |  | SI | Mujeres |
| Q67 | varchar |  |  | SI | Propiedad de la Empresa |
| Q68 | varchar |  |  | SI | Tipo de Empresa |
| Q69 | varchar |  |  | SI | Actividad económica empresa principal |
| Q70 | varchar |  |  | SI | Tipo de Contrato |
| Q71 | time |  |  | SI | Hora de Ingreso al trabajo |
| Q72 | time |  |  | SI | Hora de salida del trabajo |
| Q73 | varchar |  |  | SI | Actividad antes del accidente |
| Q74 | varchar |  |  | SI | Trabajo Habitual |
| Q75 | varchar |  |  | SI | Al momento del accidente desarrollaba su trabajo h... |
| Q76 | varchar |  |  | SI | Clasificación del Accidente |
| Q77 | varchar |  |  | SI | Tipo de Accidente de Trayecto |
| Q78 | varchar |  |  | SI | Medio de Prueba |
| Q79 | varchar |  |  | SI | Detalle del Medio de Prueba |
| Q80 | varchar |  |  | SI | Nombre del Denunciante |
| Q81 | varchar |  |  | SI | RUN del Denunciante |
| Q82 | numeric |  |  | SI | Numero de Teléfono del Denunciante |
| Q83 | varchar |  |  | SI | Clasificación del Denunciante |
| QA1 | varchar |  |  | SI | Nombre o Razón Social |
| QA2 | varchar |  |  | SI | Rut Empleador |
| QA3 | varchar |  |  | SI | Comuna |
| QB13a | varchar |  |  | SI | Antiguedad en el trabajo en que se accidentó |
| QB13b | varchar |  |  | SI | Formato Antiguedad |
| QB14 | varchar |  |  | SI | Categoria Ocupacional del Accidentado |
| QC15c | varchar |  |  | SI | Calle y N° |
| QC16 | varchar |  |  | SI | Direccion del Accidente |
| QC17a | date |  |  | SI | Fecha del Accidente |
| QC17b | time |  |  | SI | Hora del Accidente |
| QC19a | varchar |  |  | SI | Circunstancias |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |
| Qc | varchar |  |  | SI | Tipo de accidente |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*