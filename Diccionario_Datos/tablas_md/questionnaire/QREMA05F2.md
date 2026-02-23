# questionnaire.QREMA05F2

> Ingresos y Egresos a Servicio Itinerante y Atención Domiciliaria

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingresos y Egresos a Servicio Itinerante y Atención Domiciliaria

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Mes |
| Q02 | numeric |  |  | SI | Año |
| Q03 | numeric |  |  | SI | Normal con rezago |
| Q04 | numeric |  |  | SI | Normal con rezago 1 |
| Q05 | numeric |  |  | SI | Normal con rezago 2 |
| Q06 | numeric |  |  | SI | Normal con rezago 3 |
| Q07 | numeric |  |  | SI | Normal con rezago 4 |
| Q08 | numeric |  |  | SI | Normal con rezago 5 |
| Q09 | numeric |  |  | SI | Normal con rezago 6 |
| Q10 | numeric |  |  | SI | Normal con rezago 7 |
| Q11 | numeric |  |  | SI | Normal con rezago 8 |
| Q12 | numeric |  |  | SI | Riesgo |
| Q13 | numeric |  |  | SI | Riesgo 1 |
| Q14 | numeric |  |  | SI | Riesgo 2 |
| Q15 | numeric |  |  | SI | Riesgo 3 |
| Q16 | numeric |  |  | SI | Riesgo 4 |
| Q17 | numeric |  |  | SI | Riesgo 5 |
| Q18 | numeric |  |  | SI | Riesgo 6 |
| Q19 | numeric |  |  | SI | Riesgo 7 |
| Q20 | numeric |  |  | SI | Riesgo 8 |
| Q21 | numeric |  |  | SI | Retraso |
| Q22 | numeric |  |  | SI | Retraso 1 |
| Q23 | numeric |  |  | SI | Retraso 2 |
| Q24 | numeric |  |  | SI | Retraso 3 |
| Q25 | numeric |  |  | SI | Retraso 4 |
| Q26 | numeric |  |  | SI | Retraso 5 |
| Q27 | numeric |  |  | SI | Retraso 6 |
| Q28 | numeric |  |  | SI | Retraso 7 |
| Q29 | numeric |  |  | SI | Retraso 8 |
| Q30 | numeric |  |  | SI | Otra vulnerabilidad |
| Q31 | numeric |  |  | SI | Otra vulnerabilidad 1 |
| Q32 | numeric |  |  | SI | Otra vulnerabilidad 2 |
| Q33 | numeric |  |  | SI | Otra vulnerabilidad 3 |
| Q34 | numeric |  |  | SI | Otra vulnerabilidad 4 |
| Q35 | numeric |  |  | SI | Otra vulnerabilidad 5 |
| Q36 | numeric |  |  | SI | Otra vulnerabilidad 6 |
| Q37 | numeric |  |  | SI | Otra vulnerabilidad 7 |
| Q38 | numeric |  |  | SI | Otra vulnerabilidad 8 |
| QHR | varchar |  |  | SI | Establecimiento |
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