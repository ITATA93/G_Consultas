# questionnaire.QTCEPARAS

> FORMULARIO GENERAL DE ENVÍO DE MUESTRAS CLÍNICAS PARA ESTUDIOS PARASITOLÓGICOS

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* FORMULARIO GENERAL DE ENVÍO DE MUESTRAS CLÍNICAS PARA ESTUDIOS PARASITOLÓGICOS

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | FECHA ENVIO  |
| Q02 | varchar |  |  | SI | APELLIDO PATERNO |
| Q03 | varchar |  |  | SI | APELLIDO MATERNO |
| Q04 | varchar |  |  | SI | NOMBRE |
| Q05 | varchar |  |  | SI | RUT |
| Q06 | varchar |  |  | SI | FECHA DE NACIMIENTO  |
| Q07 | varchar |  |  | SI | SEXO |
| Q08 | varchar |  |  | SI | PREVISIÓN |
| Q09 | varchar |  |  | SI | DIRECCIÓN |
| Q10 | varchar |  |  | SI | TELÉFONO |
| Q11 | varchar |  |  | SI | PROFESIONAL RESPONSABLE |
| Q12 | varchar |  |  | SI | ESTABLECIMIENTO |
| Q13 | varchar |  |  | SI | DIRECCIÓN |
| Q14 | varchar |  |  | SI | TELEFONO |
| Q15 | varchar |  |  | SI | FAX |
| Q16 | varchar |  |  | SI | MAIL |
| Q17 | varchar |  |  | SI | Con Eosinofilia |
| Q18 | varchar |  |  | SI | Sin Eosinofilia |
| Q19 | varchar |  |  | SI | Observación Microscópica |
| Q20 | varchar |  |  | SI | Tipo de Muestra |
| Q21 | date |  |  | SI | Fecha Toma Muestra |
| Q22 | time |  |  | SI | Hora Toma Muestra |
| Q23 | date |  |  | SI | Fecha de Eliminación  |
| Q24 | varchar |  |  | SI | Via de Eliminación |
| Q25 | varchar |  |  | SI | Viaje Reciente Extranjero |
| Q26 | varchar |  |  | SI | Lugar |
| Q27 | varchar |  |  | SI | Tiene Macotas |
| Q28 | varchar |  |  | SI | Especificar |
| Q29 | varchar |  |  | SI | Presenta Eosinofilia |
| Q30 | varchar |  |  | SI | N° |
| Q31 | varchar |  |  | SI | % de Eosinofilia |
| Q32 | varchar |  |  | SI | Consumo Carne Cruda |
| Q33 | varchar |  |  | SI | Tipo de Preparación |
| Q34 | varchar |  |  | SI | Lugar de Consumo |
| Q35 | varchar |  |  | SI | Servicio |
| Q36 | varchar |  |  | SI | Especificar |
| Q37 | varchar |  |  | SI | OTROS ANTECEDENTES |
| Q38 | time |  |  | SI | Hora Toma de Muestra |
| Q39 | varchar |  |  | SI | Edad |
| Q40 | varchar |  |  | SI | Ciudad |
| Q41 | varchar |  |  | SI | Otro |
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