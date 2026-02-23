# questionnaire.QCLXXINGPEM

> Ingreso Psicológico Evaluación Motivacional

**Schema:** questionnaire
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Psicológico Evaluación Motivacional

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Situacion Previa al Ingreso |
| Q02 | varchar |  |  | SI | Antecedentes Relevantes |
| Q03 | varchar |  |  | SI | Situación Socio Familiar |
| Q04 | varchar |  |  | SI | Dinámica Familiar |
| Q05 | varchar |  |  | SI | Situaciones de Crisis |
| Q06 | varchar |  |  | SI | Otras Situaciones |
| Q07 | varchar |  |  | SI | Área Socio-Emocional |
| Q08 | varchar |  |  | SI | Relaciones de Amistad |
| Q09 | varchar |  |  | SI | Relaciones Amorosas |
| Q10 | varchar |  |  | SI | Identidad Personal |
| Q11 | varchar |  |  | SI | Construcción identitaria en torno a la infracción ... |
| Q12 | varchar |  |  | SI | Otros Socio-Emocional |
| Q13 | varchar |  |  | SI | Eje Motivacional al Ingreso (drogodependencia) |
| Q14 | varchar |  |  | SI | Significación de proceso de hospitalización y expe... |
| Q15 | varchar |  |  | SI | Expectativas de Egreso (drogodependecia) |
| Q16 | date |  |  | SI | Fecha de Ingreso |
| Q17 | time |  |  | SI | Hora de Ingreso |
| Q18 | varchar |  |  | SI | Profesional Responsable |
| Q19 | varchar |  |  | SI | Autoestima |
| Q20 | varchar |  |  | SI | Hipótesis Diagnostica |
| Q21 | varchar |  |  | SI | Plan de Tratamiento  |
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