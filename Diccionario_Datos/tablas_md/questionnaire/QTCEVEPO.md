# questionnaire.QTCEVEPO

> Visita de Enfermería Pre-Operatoria

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Visita de Enfermería Pre-Operatoria

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Lugar de Realización de Visita de Enfermería Preop... |
| Q02 | date |  |  | SI | Fecha Realización Visita de Enfermería Preoperator... |
| Q03 | time |  |  | SI | Hora Realización Visita Enfermería Preoperatoria |
| Q04 | varchar |  |  | SI | Presentación y Recepción de EU |
| Q05 | varchar |  |  | SI | Revisión de Antecedentes Generales (Ingreso de EU,... |
| Q06 | varchar |  |  | SI | Nivel Compromiso de Conciencia |
| Q07 | varchar |  |  | SI | Limitaciones Sensitivo/ Motoras |
| Q08 | varchar |  |  | SI | Datos Generales de la Cirugía( monitorización, ind... |
| Q09 | numeric |  |  | SI | Recepción de Examenes e Imaginología (placas cd,et... |
| Q10 | numeric |  |  | SI | Recepción de Examenes e Imaginologia |
| Q11 | varchar |  |  | SI | Resuelve Consultas de Paciente y/o Familia |
| Q12 | varchar |  |  | SI | Procedencia del Paciente |
| Q13 | varchar |  |  | SI | Motivo de Atraso Preoperatorio (si corresponde) |
| Q14 | varchar |  |  | SI | Recepción de Examenes e Imagenología (placas cd,et... |
| Q15 | varchar |  |  | SI | Otros Procedencia |
| Q16 | varchar |  |  | SI | comentario uno |
| Q17 | varchar |  |  | SI | comentario dos |
| Q18 | varchar |  |  | SI | comentario tres |
| Q19 | varchar |  |  | SI | comentario cuatro |
| Q20 | varchar |  |  | SI | comentario cinco |
| Q21 | varchar |  |  | SI | El paciente refiere Alergias |
| Q22 | varchar |  |  | SI | Comentario |
| Q23 | varchar |  |  | SI | El paciente refiere Ayuno |
| Q24 | varchar |  |  | SI | Comentario |
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