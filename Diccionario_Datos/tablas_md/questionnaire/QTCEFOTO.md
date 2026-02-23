# questionnaire.QTCEFOTO

> Ingreso a Fototerapia

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso a Fototerapia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombre del Paciente |
| Q02 | varchar |  |  | SI | Apellido Paterno  |
| Q03 | varchar |  |  | SI | Apellido Materno |
| Q04 | varchar |  |  | SI | Grupo y RH de la Madre |
| Q05 | varchar |  |  | SI | Apgar 1 Minuto |
| Q06 | varchar |  |  | SI | Apgar 5 Minutos |
| Q07 | varchar |  |  | SI | Grupo y Rh del Recien Nacido |
| Q08 | varchar |  |  | SI | Antecedentes Morbidos de la Madre |
| Q09 | varchar |  |  | SI | Antecedentes Quirurgicos de la Madre |
| Q10 | varchar |  |  | SI | Antecedentes Sociales/Habitos de la Madre |
| Q11 | date |  |  | SI | Fecha de Ingreso |
| Q12 | varchar |  |  | SI | N° Ficha Clinica |
| Q13 | varchar |  |  | SI | Anamnesis |
| Q14 | varchar |  |  | SI | Peso Ingreso |
| Q14ObsDR | varchar |  | FK | SI | Peso Ingreso DR |
| Q15 | varchar |  |  | SI | Peso al Nacer |
| Q15ObsDR | varchar |  | FK | SI | Peso al Nacer DR |
| Q16 | varchar |  |  | SI | Talla al Nacer |
| Q16ObsDR | varchar |  | FK | SI | Talla al Nacer DR |
| Q17 | varchar |  |  | SI | Circunferencia Craneana (cm) |
| Q17ObsDR | varchar |  | FK | SI | Circunferencia Craneana (cm) DR |
| Q18 | varchar |  |  | SI | Antecedentes Morbidos del Hijo |
| Q19 | varchar |  |  | SI | Ingresa con Billirubinemia de: |
| Q19ObsDR | varchar |  | FK | SI | Ingresa con Billirubinemia de: DR |
| Q20 | varchar |  |  | SI | Nivel de Foto es: |
| Q20ObsDR | varchar |  | FK | SI | Nivel de Foto es: DR |
| Q21 | time |  |  | SI | Presenta Ictericia desde las: |
| Q22 | varchar |  |  | SI | Examen Fisico |
| Q23 | varchar |  |  | SI | Diagnósticos de Ingreso |
| Q24 | varchar |  |  | SI | Plan |
| Q25 | varchar |  |  | SI | Profesional de salud |
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