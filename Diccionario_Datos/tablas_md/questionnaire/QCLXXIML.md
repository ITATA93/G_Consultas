# questionnaire.QCLXXIML

> Informe Médico de Lesiones

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe Médico de Lesiones

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | N° |
| Q02 | date |  |  | SI | Fecha |
| Q03 | time |  |  | SI | Hora |
| Q04 | varchar |  |  | SI | Nombre Completo del Examinado |
| Q05 | varchar |  |  | SI | Apellido Paterno |
| Q06 | varchar |  |  | SI | Apellido Materno |
| Q07 | varchar |  |  | SI | RUT |
| Q08 | varchar |  |  | SI | Sexo |
| Q09 | varchar |  |  | SI | 1. Diagnóstico clínico de las lesiones y breve des... |
| Q10 | varchar |  |  | SI | 2. Método de Diagnóstico  |
| Q11 | varchar |  |  | SI | 3. Describir brevemente origen de la lesión |
| Q12 | varchar |  |  | SI | Según relato lesionado |
| Q13 | varchar |  |  | SI | Según apreciación clínica |
| Q14 | numeric |  |  | SI | 4. Lesiones que ocasionarán al lesionado enfermeda... |
| Q15 | varchar |  |  | SI | días |
| Q16 | varchar |  |  | SI | 5. Diagnóstico médico legal de las lesiones |
| Q17 | varchar |  |  | SI | 6. Identificación persona que acompaña al lesionad... |
| Q18 | varchar |  |  | SI | Acompañado |
| Q20 | varchar |  |  | SI | Médico |
| Q21 | varchar |  |  | SI | Nombre Completo |
| Q22 | varchar |  |  | SI | RUT |
| Q23 | varchar |  |  | SI | Centro Asistencial |
| Q24 | varchar |  |  | SI | DAU N° |
| Q25 | varchar |  |  | SI | Edad |
| Q26 | varchar |  |  | SI | Parentesco |
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