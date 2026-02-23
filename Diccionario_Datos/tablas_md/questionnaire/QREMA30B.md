# questionnaire.QREMA30B

> REM A30 B - Teleconsulta Médica En Establecimientos De Atención Secundaria De Urgencia

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* REM A30 B - Teleconsulta Médica En Establecimientos De Atención Secundaria De Urgencia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q02 | numeric |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q03 | numeric |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q04 | numeric |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q05 | numeric |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q06 | numeric |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q07 | numeric |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q08 | numeric |  |  | SI | MÉDICO - Hombres  - MENORES DE 15 AÑOS  -  TELECON... |
| Q12 | numeric |  |  | SI | CONSULTA URGENCIA OTROS |
| Q13 | numeric |  |  | SI | CONSULTA URGENCIA OTROS 1 |
| Q14 | numeric |  |  | SI | CONSULTA URGENCIA OTROS 2 |
| Q15 | numeric |  |  | SI | CONSULTA URGENCIA OTROS 3 |
| Q16 | numeric |  |  | SI | CONSULTA URGENCIA OTROS 4 |
| Q17 | numeric |  |  | SI | CONSULTA URGENCIA OTROS 5 |
| Q18 | numeric |  |  | SI | CONSULTA URGENCIA OTROS 6 |
| Q19 | numeric |  |  | SI | CONSULTA URGENCIA OTROS 7 |
| Q20 | numeric |  |  | SI | CONSULTA URGENCIA OTROS 8 |
| Q21 | numeric |  |  | SI | CONSULTA URGENCIA OTROS 9 |
| Q22 | numeric |  |  | SI | CONSULTA URGENCIA OTROS 10 |
| Q23 | numeric |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) |
| Q24 | numeric |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 1 |
| Q25 | numeric |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 2 |
| Q26 | numeric |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 3 |
| Q27 | numeric |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 4 |
| Q28 | numeric |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 5 |
| Q29 | numeric |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 6 |
| Q30 | numeric |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 7 |
| Q31 | numeric |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 8 |
| Q32 | numeric |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 9 |
| Q33 | numeric |  |  | SI | ACCIDENTE CEREBRO VASCULAR (ACV) 10 |
| Q34 | numeric |  |  | SI | QUEMADOS |
| Q35 | numeric |  |  | SI | QUEMADOS 1 |
| Q36 | numeric |  |  | SI | QUEMADOS 2 |
| Q37 | numeric |  |  | SI | QUEMADOS 3 |
| Q38 | numeric |  |  | SI | QUEMADOS 4 |
| Q39 | numeric |  |  | SI | QUEMADOS 5 |
| Q40 | numeric |  |  | SI | QUEMADOS 6 |
| Q41 | numeric |  |  | SI | QUEMADOS 7 |
| Q42 | numeric |  |  | SI | QUEMADOS 8 |
| Q43 | numeric |  |  | SI | QUEMADOS 9 |
| Q44 | numeric |  |  | SI | QUEMADOS 10 |
| QA | numeric |  |  | SI | Año |
| QHR | varchar |  |  | SI | Establecimiento |
| QM | varchar |  |  | SI | Mes |
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