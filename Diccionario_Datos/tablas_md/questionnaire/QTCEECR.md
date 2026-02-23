# questionnaire.QTCEECR

> Emergencia Cardio - Respiratoria

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Emergencia Cardio - Respiratoria

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Emergencia |
| Q02 | time |  |  | SI | Hora Emergencia |
| Q03 | varchar |  |  | SI | Causa Presunta de la Emergencia |
| Q04 | varchar |  |  | SI | Lugar Donde Ocurre la Emergencia |
| Q05 | varchar |  |  | SI | Otro 01 |
| Q06 | varchar |  |  | SI | Tipo de Emergencia |
| Q07 | varchar |  |  | SI | Otra Emergencia |
| Q08 | numeric |  |  | SI | Tiempo Estimado Inicio Maniobra (min) |
| Q09 | varchar |  |  | SI | Tipo de Paro |
| Q10 | varchar |  |  | SI | Otro 02 |
| Q11 | numeric |  |  | SI | Inicio Ventilación Efectiva (min) |
| Q12 | varchar |  |  | SI | Método de Asistencia Ventilatoria |
| Q13 | varchar |  |  | SI | Otro 03 |
| Q14 | varchar |  |  | SI | Realización Masaje Cardiaco |
| Q15 | varchar |  |  | SI | Tipo de Masaje |
| Q16 | numeric |  |  | SI | Aparición de Pulso (min) |
| Q17 | varchar |  |  | SI | Medicamentos utilizados durante la Emergencia y/o ... |
| Q19 | numeric |  |  | SI | Duración de la Reanimación (min) |
| Q20 | varchar |  |  | SI | Reanimación |
| Q21 | varchar |  |  | SI | Vía Aérea |
| Q22 | varchar |  |  | SI | Otro 04 |
| Q23 | varchar |  |  | SI | Ventilación |
| Q24 | varchar |  |  | SI | Circulación (Pulso) |
| Q25 | varchar |  |  | SI | Otro 05 |
| Q26 | varchar |  |  | SI | Frecuencia Cardiaca (Ipm) |
| Q26ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca (Ipm) DR |
| Q27 | varchar |  |  | SI | Presión Arterial Sistólica (mmHg) |
| Q27ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica (mmHg) DR |
| Q28 | varchar |  |  | SI | Presión Arterial Diastólica (mmHg) |
| Q28ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica (mmHg) DR |
| Q29 | varchar |  |  | SI | Presión Arterial Media (mmHg) |
| Q29ObsDR | varchar |  | FK | SI | Presión Arterial Media (mmHg) DR |
| Q30 | varchar |  |  | SI | Frecuencia Respiratoria (rpm) |
| Q30ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria (rpm) DR |
| Q31 | varchar |  |  | SI | FiO2 (%) |
| Q31ObsDR | varchar |  | FK | SI | FiO2 (%) DR |
| Q32 | varchar |  |  | SI | Flujo de Oxígeno (Lt/min) |
| Q32ObsDR | varchar |  | FK | SI | Flujo de Oxígeno (Lt/min) DR |
| Q33 | varchar |  |  | SI | Oxigenoterapia |
| Q34 | varchar |  |  | SI | Saturación de O2 (%) |
| Q34ObsDR | varchar |  | FK | SI | Saturación de O2 (%) DR |
| Q35 | varchar |  |  | SI | Temperatura Axilar (°C) |
| Q35ObsDR | varchar |  | FK | SI | Temperatura Axilar (°C) DR |
| Q36 | varchar |  |  | SI | Temperatura Rectal (°C) |
| Q36ObsDR | varchar |  | FK | SI | Temperatura Rectal (°C) DR |
| Q37 | varchar |  |  | SI | HGT (mg/dl) |
| Q37ObsDR | varchar |  | FK | SI | HGT (mg/dl) DR |
| Q38 | varchar |  |  | SI | Evaluación Pupilar |
| Q39 | varchar |  |  | SI | Comentarios |
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