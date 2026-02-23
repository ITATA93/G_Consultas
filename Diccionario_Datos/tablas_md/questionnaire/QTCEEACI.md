# questionnaire.QTCEEACI

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date | PK |  | SI | Fecha |
| Q02 | time | PK |  | SI | Hora Inicio |
| Q03 | numeric | PK |  | SI | Tiempo de Procedimiento |
| Q04 | varchar | PK |  | SI | Historia |
| Q05 | varchar | PK |  | SI | Descripción del Procedimiento |
| Q06 | varchar | PK |  | SI | Tronco Común  |
| Q07 | varchar | PK |  | SI | Angiografía |
| Q08 | varchar | PK |  | SI | Ventriculografía |
| Q09 | varchar | PK |  | SI | Procedimiento Intervencional |
| Q10 | varchar | PK |  | SI | Complicaciones |
| Q11 | varchar | PK |  | SI | Diagnóstico 1 |
| Q12 | varchar | PK |  | SI | Nota Diagnóstico old |
| Q13 | varchar | PK |  | SI | Procedimiento |
| Q14 | date | PK |  | SI | Hora Término |
| Q15 | date | PK |  | SI | Fecha de Término |
| Q16 | varchar | PK |  | SI | Diagnóstico 2 |
| Q17 | varchar | PK |  | SI | Diagnóstico 3 |
| Q18 | varchar | PK |  | SI | Procedimiento 1 |
| Q19 | varchar | PK |  | SI | Procedimiento 2 |
| Q20 | varchar | PK |  | SI | Procedimiento 3 |
| Q21 | varchar | PK |  | SI | Indicaciones |
| Q22 | time | PK |  | SI | Hora de Término |
| Q23 | varchar | PK |  | SI | Nota Diagnóstico |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*