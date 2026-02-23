# SQLUser.LBDR_CumulativeCommentsEpisode

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRCCE_ParRef | bigint | PK |  | NO | Parent Reference |
| ChildQ18DR | - |  |  | SI | Child Reference: Desfibrilación |
| LBDRCCE_Header | varchar |  |  | SI | The header for the Episode in the Cumulative Comme... |
| LBDRCCE_RowID | varchar |  |  | NO | - |
| LBDRCCE_Sequence | integer |  |  | SI | The Sequence of the Episode within the comments |
| Q01 | - |  |  | SI | Fecha Emergencia |
| Q02 | - |  |  | SI | Hora Emergencia |
| Q03 | - |  |  | SI | Causa Presunta de la Emergencia |
| Q04 | - |  |  | SI | Lugar Donde Ocurre la Emergencia |
| Q05 | - |  |  | SI | Otro 01 |
| Q06 | - |  |  | SI | Tipo de Emergencia |
| Q07 | - |  |  | SI | Otra Emergencia |
| Q08 | - |  |  | SI | Tiempo Estimado Inicio Maniobra (min) |
| Q09 | - |  |  | SI | Tipo de Paro |
| Q10 | - |  |  | SI | Otro 02 |
| Q11 | - |  |  | SI | Inicio Ventilación Efectiva (min) |
| Q12 | - |  |  | SI | Método de Asistencia Ventilatoria |
| Q13 | - |  |  | SI | Otro 03 |
| Q14 | - |  |  | SI | Realización Masaje Cardiaco |
| Q15 | - |  |  | SI | Tipo de Masaje |
| Q16 | - |  |  | SI | Aparición de Pulso (min) |
| Q17 | - |  |  | SI | Medicamentos utilizados durante la Emergencia y/o ... |
| Q19 | - |  |  | SI | Duración de la Reanimación (min) |
| Q20 | - |  |  | SI | Reanimación |
| Q21 | - |  |  | SI | Vía Aérea |
| Q22 | - |  |  | SI | Otro 04 |
| Q23 | - |  |  | SI | Ventilación |
| Q24 | - |  |  | SI | Circulación (Pulso) |
| Q25 | - |  |  | SI | Otro 05 |
| Q26 | - |  |  | SI | Frecuencia Cardiaca (Ipm) |
| Q26ObsDR | - |  |  | SI | Frecuencia Cardiaca (Ipm) DR |
| Q27 | - |  |  | SI | Presión Arterial Sistólica (mmHg) |
| Q27ObsDR | - |  |  | SI | Presión Arterial Sistólica (mmHg) DR |
| Q28 | - |  |  | SI | Presión Arterial Diastólica (mmHg) |
| Q28ObsDR | - |  |  | SI | Presión Arterial Diastólica (mmHg) DR |
| Q29 | - |  |  | SI | Presión Arterial Media (mmHg) |
| Q29ObsDR | - |  |  | SI | Presión Arterial Media (mmHg) DR |
| Q30 | - |  |  | SI | Frecuencia Respiratoria (rpm) |
| Q30ObsDR | - |  |  | SI | Frecuencia Respiratoria (rpm) DR |
| Q31 | - |  |  | SI | FiO2 (%) |
| Q31ObsDR | - |  |  | SI | FiO2 (%) DR |
| Q32 | - |  |  | SI | Flujo de Oxígeno (Lt/min) |
| Q32ObsDR | - |  |  | SI | Flujo de Oxígeno (Lt/min) DR |
| Q33 | - |  |  | SI | Oxigenoterapia |
| Q34 | - |  |  | SI | Saturación de O2 (%) |
| Q34ObsDR | - |  |  | SI | Saturación de O2 (%) DR |
| Q35 | - |  |  | SI | Temperatura Axilar (°C) |
| Q35ObsDR | - |  |  | SI | Temperatura Axilar (°C) DR |
| Q36 | - |  |  | SI | Temperatura Rectal (°C) |
| Q36ObsDR | - |  |  | SI | Temperatura Rectal (°C) DR |
| Q37 | - |  |  | SI | HGT (mg/dl) |
| Q37ObsDR | - |  |  | SI | HGT (mg/dl) DR |
| Q38 | - |  |  | SI | Evaluación Pupilar |
| Q39 | - |  |  | SI | Comentarios |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*