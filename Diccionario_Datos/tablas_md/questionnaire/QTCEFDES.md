# questionnaire.QTCEFDES

> Formulario de Envío Estudio Serológico

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Envío Estudio Serológico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | RUT |
| Q02 | varchar |  |  | SI | Nombres |
| Q03 | varchar |  |  | SI | Apellido Paterno |
| Q04 | varchar |  |  | SI | Apellido Materno |
| Q05 | varchar |  |  | SI | Sexo |
| Q06 | varchar |  |  | SI | Fecha de Nacimiento |
| Q07 | varchar |  |  | SI | Edad |
| Q08 | varchar |  |  | SI | Dirección |
| Q09 | varchar |  |  | SI | Región |
| Q10 | varchar |  |  | SI | Ciudad / Localidad |
| Q11 | varchar |  |  | SI | Comuna |
| Q12 | varchar |  |  | SI | Teléfono |
| Q13 | varchar |  |  | SI | Previsión |
| Q14 | varchar |  |  | SI | Establecimiento |
| Q15 | varchar |  |  | SI | Unidad |
| Q16 | varchar |  |  | SI | Dirección |
| Q17 | varchar |  |  | SI | Región |
| Q18 | varchar |  |  | SI | Ciudad / Localidad |
| Q19 | varchar |  |  | SI | Comuna |
| Q20 | varchar |  |  | SI | Profesional Responsable |
| Q21 | varchar |  |  | SI | Correo Laboratorio |
| Q22 | varchar |  |  | SI | Fono Laboratorio |
| Q23 | varchar |  |  | SI | Correo Laboratorio |
| Q24 | varchar |  |  | SI | Servicio de Salud |
| Q25 | varchar |  |  | SI | Dirección |
| Q26 | varchar |  |  | SI | Región |
| Q27 | varchar |  |  | SI | Ciudad / Localidad |
| Q28 | varchar |  |  | SI | Tipo Despacho |
| Q29 | varchar |  |  | SI | Comuna |
| Q30 | varchar |  |  | SI | Correo Laboratorio |
| Q31 | varchar |  |  | SI | Examen |
| Q32 | date |  |  | SI | Fecha de la Muestra |
| Q33 | time |  |  | SI | Hora de Obtención  |
| Q34 | varchar |  |  | SI | Tipo de Muestra |
| Q35 | varchar |  |  | SI | N° Muestra Original |
| Q36 | varchar |  |  | SI | N° Muestra |
| Q37 | date |  |  | SI | Fecha envío ISPCH |
| Q38 | varchar |  |  | SI | Observaciones |
| Q39 | varchar |  |  | SI | Diagnóstico Clínico |
| Q40 | date |  |  | SI | Fecha Inicio de Sintomas |
| Q41 | varchar |  |  | SI | Tratamiento Antibiótico |
| Q42 | date |  |  | SI | Fecha Inicio de Tratamiento |
| Q43 | varchar |  |  | SI | Fax Laboratorio |
| Q44 | varchar |  |  | SI | Fax Laboratorio |
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