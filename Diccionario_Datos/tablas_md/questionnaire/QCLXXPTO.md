# questionnaire.QCLXXPTO

> Prueba de Tolerancia Ortostática (PTO)

**Schema:** questionnaire
**Columnas:** 118
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Prueba de Tolerancia Ortostática (PTO)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q02 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q03 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q04 | varchar |  |  | SI | % Saturación O2 |
| Q05 | varchar |  |  | SI | Síntomas |
| Q06 | varchar |  |  | SI | (mareo, debilidad, visión borrosa, síncope) |
| Q07 | varchar |  |  | SI | En decúbito supino |
| Q08 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q08ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q09 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q09ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q10 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q10ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q11 | varchar |  |  | SI | Saturación O2 |
| Q11ObsDR | varchar |  | FK | SI | Saturación O2 DR |
| Q12 | varchar |  |  | SI | Síntomas |
| Q13 | varchar |  |  | SI | 1er minuto en sedente borde cama |
| Q14 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q14ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q15 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q15ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q16 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q16ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q17 | varchar |  |  | SI | Saturación O2 |
| Q17ObsDR | varchar |  | FK | SI | Saturación O2 DR |
| Q18 | varchar |  |  | SI | Síntomas |
| Q19 | varchar |  |  | SI | 3er minuto en sedente borde cama |
| Q20 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q20ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q21 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q21ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q22 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q22ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q23 | varchar |  |  | SI | Saturación O2 |
| Q23ObsDR | varchar |  | FK | SI | Saturación O2 DR |
| Q24 | varchar |  |  | SI | Síntomas |
| Q25 | varchar |  |  | SI | 5to minuto en sedente borde cama |
| Q26 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q26ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q27 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q27ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q28 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q28ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q29 | varchar |  |  | SI | Saturación O2 |
| Q29ObsDR | varchar |  | FK | SI | Saturación O2 DR |
| Q30 | varchar |  |  | SI | Síntomas |
| Q31 | varchar |  |  | SI | 1er minuto en bípedo |
| Q32 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q32ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q33 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q33ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q34 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q34ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q35 | varchar |  |  | SI | Saturación O2 |
| Q35ObsDR | varchar |  | FK | SI | Saturación O2 DR |
| Q36 | varchar |  |  | SI | Síntomas |
| Q37 | varchar |  |  | SI | 3er minuto en bípedo |
| Q38 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q38ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q39 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q39ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q40 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q40ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q41 | varchar |  |  | SI | Saturación O2 |
| Q41ObsDR | varchar |  | FK | SI | Saturación O2 DR |
| Q42 | varchar |  |  | SI | Síntomas |
| Q43 | varchar |  |  | SI | 5to minuto en bípedo |
| Q44 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q44ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q45 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q45ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q46 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q46ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q47 | varchar |  |  | SI | Saturación O2 |
| Q47ObsDR | varchar |  | FK | SI | Saturación O2 DR |
| Q48 | varchar |  |  | SI | Síntomas |
| Q49 | varchar |  |  | SI | Evaluación de la prueba |
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