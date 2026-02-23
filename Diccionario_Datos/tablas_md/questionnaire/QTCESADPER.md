# questionnaire.QTCESADPER

> Evaluación a Usuario con Intento Suicida

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación a Usuario con Intento Suicida

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombre del Paciente |
| Q02 | varchar |  |  | SI | Rut |
| Q03 | varchar |  |  | SI | Edad |
| Q04 | date |  |  | SI | Fecha |
| Q05 | varchar |  |  | SI | S: Sexo Masculino |
| Q06 | varchar |  |  | SI | A: Edad < 20 ó >45 años. |
| Q07 | varchar |  |  | SI | D: Depresión |
| Q08 | varchar |  |  | SI | P: Tentativa Suicida Previa |
| Q09 | varchar |  |  | SI | E: Abuso de Alcohol |
| Q10 | varchar |  |  | SI | R: Falta de Pensamiento Racional (psicosis o trast... |
| Q11 | varchar |  |  | SI | S. Carencia de Apoyo Social |
| Q12 | varchar |  |  | SI | O: Plan Organizado de Suicidio |
| Q13 | varchar |  |  | SI | N: Sin Pareja o Cónyuge |
| Q14 | varchar |  |  | SI | S: Enfermedad Somática |
| Q15 | varchar |  |  | SI | Ideación Suicida Activa y/o Persistente |
| Q16 | varchar |  |  | SI | Falta de Enjuiciamiento del Intento Suicida |
| Q17 | varchar |  |  | SI | Ausencia de Planes o Proyectos de Futuro |
| Q18 | varchar |  |  | SI | Resultado SAD Persons |
| Q18ObsDR | varchar |  | FK | SI | Resultado SAD Persons DR |
| Q19 | varchar |  |  | SI | Hospitalización |
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