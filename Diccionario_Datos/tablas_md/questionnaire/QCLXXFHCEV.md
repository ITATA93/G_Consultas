# questionnaire.QCLXXFHCEV

> Ficha Clap Evolución

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha Clap Evolución

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Acompañante |
| Q02 | varchar |  |  | SI | Otro acompañante |
| Q03 | varchar |  |  | SI | Estudios |
| Q04 | numeric |  |  | SI | Grado Curso |
| Q05 | varchar |  |  | SI | Estado Civil |
| Q06 | varchar |  |  | SI | Peso |
| Q06ObsDR | varchar |  | FK | SI | Peso DR |
| Q07 | varchar |  |  | SI | Talla |
| Q07ObsDR | varchar |  | FK | SI | Talla DR |
| Q08 | varchar |  |  | SI | DE |
| Q09 | varchar |  |  | SI | Perímetro Cintura |
| Q09ObsDR | varchar |  | FK | SI | Perímetro Cintura DR |
| Q10 | varchar |  |  | SI | IMC |
| Q11 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q11ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q12 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q12ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q13 | date |  |  | SI | Fecha última menstruación  |
| Q14 | bit |  |  | SI | No contesta |
| Q15 | bit |  |  | SI | Tanner con Foto |
| Q16 | varchar |  |  | SI | Tanner Mamas |
| Q16ObsDR | varchar |  | FK | SI | Tanner Mamas DR |
| Q17 | varchar |  |  | SI | Tanner Genitales |
| Q17ObsDR | varchar |  | FK | SI | Tanner Genitales DR |
| Q20 | varchar |  |  | SI | Cambios Relevantes / Observaciones |
| Q21 | varchar |  |  | SI | Detección de riesgo |
| Q22 | varchar |  |  | SI | Diagnóstico Integral |
| Q23 | varchar |  |  | SI | Indicaciones e Interconsultas |
| Q24 | date |  |  | SI | Fecha próxima visita |
| Q25 | varchar |  |  | SI | DE (IMC) |
| Q26 | varchar |  |  | SI | Conoce fecha de última menstruación |
| Q27 | varchar |  |  | SI | Especificar otro Riesgo |
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