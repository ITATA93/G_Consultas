# questionnaire.QTCRSI

> Índice RSI Síntomas de Reflujo

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Índice RSI Síntomas de Reflujo

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha |
| Q02 | time |  |  | SI | Hora |
| Q03 | varchar |  |  | SI | Durante el mes pasado, ¿cómo le afectaron los sigu... |
| Q04 | varchar |  |  | SI | 0 = Sin Problema |
| Q05 | varchar |  |  | SI | 5 = Problema Severo |
| Q06 | varchar |  |  | SI | Disfonía u otro problema con su voz |
| Q07 | varchar |  |  | SI | Carraspera |
| Q08 | varchar |  |  | SI | Presencia de moco excesivo en su garganta o goteo ... |
| Q09 | varchar |  |  | SI | Dificultad para deglutir alimentos líquidos o past... |
| Q10 | varchar |  |  | SI | Tos después de comer o acostarse |
| Q11 | varchar |  |  | SI | Sensación de ahogo o atrancamiento |
| Q12 | varchar |  |  | SI | Tos ocasional o en accesos |
| Q13 | varchar |  |  | SI | Sensación de taco o una aguja en su garganta |
| Q14 | varchar |  |  | SI | Quemadura retroesternal, dolor en el pecho, indige... |
| Q15 | varchar |  |  | SI | Score |
| Q16 | varchar |  |  | SI | Classification |
| Q17 | varchar |  |  | SI | Score is not indicative of laryngopharyngeal reflu... |
| Q18 | varchar |  |  | SI | 0 - 13 |
| Q19 | varchar |  |  | SI | 14 - 45 |
| Q20 | varchar |  |  | SI | Score is indicative of laryngopharyngeal reflux  |
| Q21 | varchar |  |  | SI | 0 - 13: Indicative of laryngopharyngeal reflux |
| Q22 | varchar |  |  | SI | 14 - 45: Indicative of laryngopharyngeal reflux |
| Q23 | varchar |  |  | SI | The Reflux Symptom Index (RSI) is a self-administe... |
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