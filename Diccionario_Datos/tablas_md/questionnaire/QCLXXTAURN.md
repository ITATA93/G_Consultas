# questionnaire.QCLXXTAURN

> Tamizaje Auditivo en Recién Nacido

**Schema:** questionnaire
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Tamizaje Auditivo en Recién Nacido

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Edad Corregida |
| Q02 | varchar |  |  | SI | Timpanometría (Derecha) |
| Q03 | varchar |  |  | SI | Timpanometría (Izquierda) |
| Q04 | varchar |  |  | SI | Emisiones Otoacústicas (OAEs) |
| Q05 | varchar |  |  | SI | Emisiones Otoacústicas Transitorias (TEOAE) |
| Q06 | varchar |  |  | SI | Derecho |
| Q07 | varchar |  |  | SI | Izquierdo |
| Q08 | varchar |  |  | SI | Emisiones Otoacústicas Producto de Distorsión (DPO... |
| Q09 | varchar |  |  | SI | Derecho |
| Q10 | varchar |  |  | SI | Izquierdo |
| Q11 | varchar |  |  | SI | Respuesta Auditiva en Estado Estable (ASSR) |
| Q12 | varchar |  |  | SI | Derecho |
| Q13 | varchar |  |  | SI | Izquierdo |
| Q14 | varchar |  |  | SI | Potencial Evocado Auditivo Automatizado del Tronco... |
| Q15 | varchar |  |  | SI | Derecho |
| Q16 | varchar |  |  | SI | Izquierdo |
| Q17 | varchar |  |  | SI | Respuesta Auditiva del Tronco Cerebral (ABR) |
| Q18 | varchar |  |  | SI | Derecho |
| Q19 | varchar |  |  | SI | Izquierdo |
| Q20 | varchar |  |  | SI | Comentarios |
| Q21 | varchar |  |  | SI | Recomendaciones |
| Q22 | varchar |  |  | SI | Presenta Factores de Riesgo |
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