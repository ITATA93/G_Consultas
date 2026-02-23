# questionnaire.QCLXXAPACHE

> APACHE II (Evaluación Fisiológica de Salud Aguda y Crónica)

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* APACHE II (Evaluación Fisiológica de Salud Aguda y Crónica)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q02 | varchar |  |  | SI | Pje. Glasgow (Adultos) |
| Q02ObsDR | varchar |  | FK | SI | Pje. Glasgow (Adultos) DR |
| Q05 | varchar |  |  | SI | Temperatura Axilar |
| Q05ObsDR | varchar |  | FK | SI | Temperatura Axilar DR |
| Q07 | varchar |  |  | SI | Presión Arterial Media |
| Q07ObsDR | varchar |  | FK | SI | Presión Arterial Media DR |
| Q08 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q08ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q09 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q09ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q10 | varchar |  |  | SI | FiO2 |
| Q10ObsDR | varchar |  | FK | SI | FiO2 DR |
| Q11 | varchar |  |  | SI | PaO2 |
| Q11ObsDR | varchar |  | FK | SI | PaO2 DR |
| Q12 | varchar |  |  | SI | PaCO2 |
| Q12ObsDR | varchar |  | FK | SI | PaCO2 DR |
| Q13 | varchar |  |  | SI | Presión Atmosférica |
| Q13ObsDR | varchar |  | FK | SI | Presión Atmosférica DR |
| Q14 | varchar |  |  | SI | Ph Arterial |
| Q14ObsDR | varchar |  | FK | SI | Ph Arterial DR |
| Q15 | varchar |  |  | SI | Sodio Sérico |
| Q15ObsDR | varchar |  | FK | SI | Sodio Sérico DR |
| Q16 | varchar |  |  | SI | Potasio Sérico |
| Q16ObsDR | varchar |  | FK | SI | Potasio Sérico DR |
| Q17 | varchar |  |  | SI | Creatinina Sérica |
| Q17ObsDR | varchar |  | FK | SI | Creatinina Sérica DR |
| Q18 | varchar |  |  | SI | Falla Renal Aguida |
| Q19 | varchar |  |  | SI | Hematocrito |
| Q19ObsDR | varchar |  | FK | SI | Hematocrito DR |
| Q20 | varchar |  |  | SI | Recuento de Leucocitos |
| Q20ObsDR | varchar |  | FK | SI | Recuento de Leucocitos DR |
| Q22 | varchar |  |  | SI | Clasificación de la Admisión |
| Q23 | varchar |  |  | SI | Puntaje APACHE II |
| Q23ObsDR | varchar |  | FK | SI | Puntaje APACHE II DR |
| Q24 | varchar |  |  | SI | Conversión a Mortalidad |
| Q24ObsDR | varchar |  | FK | SI | Conversión a Mortalidad DR |
| Q26 | varchar |  |  | SI | Categoría de Diagnóstico de Admisión UCI (No Opera... |
| Q27 | varchar |  |  | SI | Categoría de Diagnóstico de Admisión UCI (Operator... |
| Q28 | varchar |  |  | SI | Paciente Requirió Cirugía de Emergencia |
| Q29 | varchar |  |  | SI | Edad (Años) |
| Q30 | varchar |  |  | SI | Insuficiencia Orgánica Sistémica Severa o Paciente... |
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