# questionnaire.QTCEBRONCON

> Score Riesgo de Morir de Bronconeumonía

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Score Riesgo de Morir de Bronconeumonía

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQRMB1 | varchar |  |  | SI | - |
| CQRMB10 | varchar |  |  | SI | - |
| CQRMB2 | varchar |  |  | SI | - |
| CQRMB3 | varchar |  |  | SI | - |
| CQRMB4 | varchar |  |  | SI | - |
| CQRMB5 | varchar |  |  | SI | - |
| CQRMB6 | varchar |  |  | SI | - |
| CQRMB7 | varchar |  |  | SI | - |
| CQRMB8 | varchar |  |  | SI | - |
| QRBron | varchar |  |  | SI | Resultado de la Evaluación |
| QRBronObsDR | varchar |  | FK | SI | Resultado de la Evaluación DR |
| QRMB1 | varchar |  |  | SI | Malformaciones congénitas |
| QRMB10 | varchar |  |  | SI | Síndrome bronquial obstructivo recurrente (SBOR) |
| QRMB2 | varchar |  |  | SI | Tabaquismo materno |
| QRMB3 | varchar |  |  | SI | Hospitalización anterior |
| QRMB4 | varchar |  |  | SI | Desnutrición |
| QRMB5 | varchar |  |  | SI | Baja escolaridad materna |
| QRMB6 | varchar |  |  | SI | Bajo peso de nacimiento, < 2500 grs. |
| QRMB7 | varchar |  |  | SI | Lactancia materna insuficiente, < 4 meses |
| QRMB8 | varchar |  |  | SI | Madre adolescente (10 - 19 años) |
| QRRbron | varchar |  |  | SI | Resultado Evaluación |
| QRRbronObsDR | varchar |  | FK | SI | Resultado Evaluación DR |
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
| Qres | varchar |  |  | SI | Resultado Score Riesgo Morir Bronconeumonia |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*