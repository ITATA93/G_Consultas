# questionnaire.QTCEEVOPUE

> Evaluación Puerperio

**Schema:** questionnaire
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Puerperio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Frecuencia Cardiaca (lpm) |
| Q01ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca (lpm) DR |
| Q02 | varchar |  |  | SI | Presión Arterial Sistólica (mmHg) |
| Q02ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica (mmHg) DR |
| Q03 | varchar |  |  | SI | Presión Arterial Diastólica (mmHg) |
| Q03ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica (mmHg) DR |
| Q04 | varchar |  |  | SI | Frecuencia Respiratoria (rpm) |
| Q04ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria (rpm) DR |
| Q05 | varchar |  |  | SI | FiO2 % |
| Q05ObsDR | varchar |  | FK | SI | FiO2 % DR |
| Q06 | varchar |  |  | SI | Flujo de Oxígeno (Lt/min) |
| Q06ObsDR | varchar |  | FK | SI | Flujo de Oxígeno (Lt/min) DR |
| Q07 | varchar |  |  | SI | Oxigenoterapia |
| Q07ObsDR | varchar |  | FK | SI | Oxigenoterapia DR |
| Q08 | varchar |  |  | SI | Saturación O2 % |
| Q08ObsDR | varchar |  | FK | SI | Saturación O2 % DR |
| Q09 | varchar |  |  | SI | Temperatura Axilar (°C) |
| Q09ObsDR | varchar |  | FK | SI | Temperatura Axilar (°C) DR |
| Q10 | varchar |  |  | SI | Temperatura Rectal % |
| Q10ObsDR | varchar |  | FK | SI | Temperatura Rectal % DR |
| Q11 | varchar |  |  | SI | Hemoglucotest (mg/dl) |
| Q11ObsDR | varchar |  | FK | SI | Hemoglucotest (mg/dl) DR |
| Q12 | varchar |  |  | SI | comentario 01 |
| Q13 | varchar |  |  | SI | comentario 02 |
| Q14 | varchar |  |  | SI | comentario 03 |
| Q15 | varchar |  |  | SI | comentario 04 |
| Q16 | varchar |  |  | SI | comentario 05 |
| Q17 | varchar |  |  | SI | comentario 06 |
| Q18 | varchar |  |  | SI | comentario 07 |
| Q19 | varchar |  |  | SI | comentario 08 |
| Q20 | varchar |  |  | SI | comentario 09 |
| Q21 | varchar |  |  | SI | comentario 10 |
| Q22 | varchar |  |  | SI | comentario 11 |
| Q23 | varchar |  |  | SI | Tipo de Parto |
| Q23ObsDR | varchar |  | FK | SI | Tipo de Parto DR |
| Q24 | varchar |  |  | SI | Descripción Mamas |
| Q24ObsDR | varchar |  | FK | SI | Descripción Mamas DR |
| Q25 | varchar |  |  | SI | Descripción Pezones |
| Q25ObsDR | varchar |  | FK | SI | Descripción Pezones DR |
| Q26 | varchar |  |  | SI | Lactancia Materna Exclusiva |
| Q26ObsDR | varchar |  | FK | SI | Lactancia Materna Exclusiva DR |
| Q27 | varchar |  |  | SI | Útero |
| Q27ObsDR | varchar |  | FK | SI | Útero DR |
| Q28 | varchar |  |  | SI | Herida Operatoria |
| Q28ObsDR | varchar |  | FK | SI | Herida Operatoria DR |
| Q29 | varchar |  |  | SI | Episiotomía |
| Q29ObsDR | varchar |  | FK | SI | Episiotomía DR |
| Q30 | varchar |  |  | SI | Flujo Genital Puérpera |
| Q30ObsDR | varchar |  | FK | SI | Flujo Genital Puérpera DR |
| Q31 | varchar |  |  | SI | Cantidad Flujo Genital Puérpera |
| Q31ObsDR | varchar |  | FK | SI | Cantidad Flujo Genital Puérpera DR |
| Q32 | varchar |  |  | SI | Diuresis |
| Q32ObsDR | varchar |  | FK | SI | Diuresis DR |
| Q33 | varchar |  |  | SI | Deposiciones |
| Q33ObsDR | varchar |  | FK | SI | Deposiciones DR |
| Q34 | varchar |  |  | SI | Extremidades Inferiores |
| Q34ObsDR | varchar |  | FK | SI | Extremidades Inferiores DR |
| Q35 | varchar |  |  | SI | Edema |
| Q35ObsDR | varchar |  | FK | SI | Edema DR |
| Q36 | varchar |  |  | SI | Valoración del Dolor |
| Q37 | varchar |  |  | SI | Escala de Dolor |
| Q37ObsDR | varchar |  | FK | SI | Escala de Dolor DR |
| Q38 | varchar |  |  | SI | Ubicación del Dolor |
| Q39 | varchar |  |  | SI | Razones para no  Evaluar |
| Q40 | varchar |  |  | SI | Especifique Razón para no Evaluar |
| Q41 | varchar |  |  | SI | Abdomen |
| Q41ObsDR | varchar |  | FK | SI | Abdomen DR |
| Q42 | varchar |  |  | SI | comentario 12 |
| Q43 | varchar |  |  | SI | comentario 13 |
| Q44 | varchar |  |  | SI | comentario 14 |
| Q45 | varchar |  |  | SI | comentario 15 |
| Q46 | varchar |  |  | SI | comentario 16 |
| Q47 | varchar |  |  | SI | comentario 17 |
| Q48 | varchar |  |  | SI | comentario 18 |
| Q49 | varchar |  |  | SI | comentario 19 |
| Q50 | varchar |  |  | SI | comentario 20 |
| Q51 | varchar |  |  | SI | comentario 22 |
| Q52 | varchar |  |  | SI | comentario 23 |
| Q53 | varchar |  |  | SI | comentario 24 |
| Q54 | varchar |  |  | SI | comentario 25 |
| Q55 | varchar |  |  | SI | comentario 26 |
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