# questionnaire.QCLXXEFGEN

> Examen Físico General

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico General

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Descripción Examen Físico General |
| Q02 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q02ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q03 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q03ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q04 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q04ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q05 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q05ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q06 | varchar |  |  | SI | Temperatura Axilar |
| Q06ObsDR | varchar |  | FK | SI | Temperatura Axilar DR |
| Q07 | varchar |  |  | SI | Saturación O2 |
| Q07ObsDR | varchar |  | FK | SI | Saturación O2 DR |
| Q08 | varchar |  |  | SI | FiO2 |
| Q08ObsDR | varchar |  | FK | SI | FiO2 DR |
| Q09 | varchar |  |  | SI | Escala del Dolor (EVA) |
| Q09ObsDR | varchar |  | FK | SI | Escala del Dolor (EVA) DR |
| Q10 | varchar |  |  | SI | Anamnesis Próxima |
| Q11 | varchar |  |  | SI | Ocupación |
| Q12 | varchar |  |  | SI | Descripción (SNOMED) |
| Q13 | varchar |  |  | SI | Motivo de consulta |
| Q14 | varchar |  |  | SI | Anamnesis Remota |
| Q15 | varchar |  |  | SI | Flujo |
| Q16 | varchar |  |  | SI | Peso (kg) |
| Q16ObsDR | varchar |  | FK | SI | Peso (kg) DR |
| Q17 | varchar |  |  | SI | Talla (cm) |
| Q17ObsDR | varchar |  | FK | SI | Talla (cm) DR |
| Q18 | varchar |  |  | SI | Circunferencia Craneana (cm) |
| Q18ObsDR | varchar |  | FK | SI | Circunferencia Craneana (cm) DR |
| Q19 | varchar |  |  | SI | Circunferencia Torácica (cm) |
| Q19ObsDR | varchar |  | FK | SI | Circunferencia Torácica (cm) DR |
| Q20 | varchar |  |  | SI | Circunferencia Abdominal (cm) |
| Q20ObsDR | varchar |  | FK | SI | Circunferencia Abdominal (cm) DR |
| Q21 | varchar |  |  | SI | Estado Nutricional |
| Q21ObsDR | varchar |  | FK | SI | Estado Nutricional DR |
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