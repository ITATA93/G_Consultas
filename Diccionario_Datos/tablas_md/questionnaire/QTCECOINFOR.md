# questionnaire.QTCECOINFOR

> Consentimiento Informado para Examen Corporal

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Consentimiento Informado para Examen Corporal

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ004 | varchar |  |  | SI | - |
| CQ024 | varchar |  |  | SI | - |
| Q001 | date |  |  | SI | Fecha |
| Q002 | varchar |  |  | SI | Nombre Completo Acompañante |
| Q003 | varchar |  |  | SI | RUT Acompañante |
| Q004 | varchar |  |  | SI | Autorización para que se practiquen Exámenes Corpo... |
| Q005 | varchar |  |  | SI | Motivo de Negativa de Realización de Examen |
| Q006 | varchar |  |  | SI | Procedimiento |
| Q007 | date |  |  | SI | Fecha |
| Q008 | time |  |  | SI | Hora |
| Q009 | varchar |  |  | SI | Descripción de Especie |
| Q010 | varchar |  |  | SI | Unidad Policial |
| Q011 | varchar |  |  | SI | Levantada por |
| Q012 | varchar |  |  | SI | N° de paciente |
| Q013 | varchar |  |  | SI | RUT |
| Q014 | varchar |  |  | SI | Cargo |
| Q015 | varchar |  |  | SI | Observaciones Indicadas por el Fiscal |
| Q016 | varchar |  |  | SI | De |
| Q017 | date |  |  | SI | Fecha |
| Q018 | varchar |  |  | SI | Nombre (Grado) |
| Q019 | varchar |  |  | SI | RUT |
| Q020 | varchar |  |  | SI | Motivo de Traslado |
| Q021 | varchar |  |  | SI | Para (Estado Especie) |
| Q022 | varchar |  |  | SI | De (Estado Especie) |
| Q023 | time |  |  | SI | Hora (Estado Especie) |
| Q024 | varchar |  |  | SI | ¿Víctima es Menor de Edad? |
| Q025 | varchar |  |  | SI | Para 2 |
| Q026 | varchar |  |  | SI | De  |
| Q027 | time |  |  | SI | Hora 2 |
| Q028 | varchar |  |  | SI | Para 3 |
| Q029 | varchar |  |  | SI | De 3 |
| Q030 | time |  |  | SI | Hora 3 |
| Q031 | varchar |  |  | SI | De 4 |
| Q032 | varchar |  |  | SI | Para 4 |
| Q033 | time |  |  | SI | Hora 4 |
| Q034 | varchar |  |  | SI | De 5  |
| Q035 | varchar |  |  | SI | Para 5 |
| Q036 | time |  |  | SI | Hora 5 |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*