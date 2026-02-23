# questionnaire.QTCEORDTRA

**Schema:** questionnaire
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CQ011 | varchar | PK |  | SI | - |
| CQ012 | varchar | PK |  | SI | - |
| CQ013 | varchar | PK |  | SI | - |
| CQ014 | varchar | PK |  | SI | - |
| CQ015 | varchar | PK |  | SI | - |
| CQ019 | varchar | PK |  | SI | - |
| CQ028 | varchar | PK |  | SI | - |
| CQ039 | varchar | PK |  | SI | - |
| CQ042 | varchar | PK |  | SI | - |
| CQ043 | varchar | PK |  | SI | - |
| CQ044 | varchar | PK |  | SI | - |
| CQ045 | varchar | PK |  | SI | - |
| CQ047 | varchar | PK |  | SI | - |
| CQTP | varchar | PK |  | SI | - |
| ID | bigint | PK |  | NO | - |
| Q001 | varchar | PK |  | SI | Nombre de Paciente |
| Q002 | varchar | PK |  | SI | RUT Paciente |
| Q003 | varchar | PK |  | SI | N° de Ficha Clínica |
| Q004 | varchar | PK |  | SI | Edad |
| Q004A | bit | PK |  | SI | Desfibrilador |
| Q004B | bit | PK |  | SI | DEA |
| Q004C | bit | PK |  | SI | Marcapaso Externo |
| Q004D | bit | PK |  | SI | Ventilación Mecánica |
| Q004E | bit | PK |  | SI | Monitor Multiparámetros |
| Q004F | bit | PK |  | SI | Oximetría de pulso pediatrico |
| Q004G | bit | PK |  | SI | Oximetria de pulso adulto |
| Q004H | bit | PK |  | SI | Capnógrafo |
| Q004J | bit | PK |  | SI | Bombas de Infusión |
| Q004K | bit | PK |  | SI | Otros |
| Q006 | varchar | PK |  | SI | Traslado a |
| Q007 | varchar | PK |  | SI | Desde |
| Q008 | date | PK |  | SI | Fecha |
| Q009 | time | PK |  | SI | Hora |
| Q010 | varchar | PK |  | SI | Diagnóstico |
| Q011 | varchar | PK |  | SI | Móvil |
| Q012 | varchar | PK |  | SI | Medio de Traslado |
| Q013 | varchar | PK |  | SI | Gases Clínicos |
| Q014 | varchar | PK |  | SI | Equipos |
| Q015 | varchar | PK |  | SI | Tipo de Bajada |
| Q016 | varchar | PK |  | SI | Otro tipo de Bajada |
| Q017 | varchar | PK |  | SI | ¿Cuantas? |
| Q018 | varchar | PK |  | SI | Otro Equipo |
| Q019 | varchar | PK |  | SI | Acompañantes |
| Q020 | date | PK |  | SI | Fecha Emisión de Orden |
| Q021 | time | PK |  | SI | Hora emisión de Orden |
| Q022 | varchar | PK |  | SI | Médico Derivador |
| Q023 | varchar | PK |  | SI | Médico Receptor |
| Q024 | varchar | PK |  | SI | Conductor |
| Q025 | varchar | PK |  | SI | Paramedico |
| Q026 | varchar | PK |  | SI | Reanimador |
| Q027 | varchar | PK |  | SI | Conductor (segundo) |
| Q028 | varchar | PK |  | SI | Tipo de Móvil |
| Q029 | varchar | PK |  | SI | Otros |
| Q030 | date | PK |  | SI | Fecha de Traslado Propuesta |
| Q031 | time | PK |  | SI | Hora de Traslado Propuesta |
| Q032 | varchar | PK |  | SI | TISS - 28 m:(N°) |
| Q033 | date | PK |  | SI | Fecha Salida Real |
| Q034 | time | PK |  | SI | Hora Salida Real |
| Q035 | date | PK |  | SI | Fecha entrega paciente |
| Q036 | time | PK |  | SI | Hora entrega paciente |
| Q037 | date | PK |  | SI | Fecha de Retorno |
| Q038 | time | PK |  | SI | Hora de retorno |
| Q039 | varchar | PK |  | SI | Retorno con Paciente |
| Q040 | date | PK |  | SI | Fecha Término Cometido |
| Q041 | time | PK |  | SI | Hora Término Cometido |
| Q042 | varchar | PK |  | SI | RRHH |
| Q043 | varchar | PK |  | SI | RRFF |
| Q044 | varchar | PK |  | SI | Administrativos |
| Q045 | varchar | PK |  | SI | Otros |
| Q046 | varchar | PK |  | SI | Comentarios |
| Q047 | varchar | PK |  | SI | Traslado No Realizado |
| Q048 | varchar | PK |  | SI | Gases Clínicos |
| Q049 | varchar | PK |  | SI | Aire Comprimido |
| QTP | varchar | PK |  | SI | Tipo de Paciente |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*