# questionnaire.QCLXXMRCSUM

> Escala MRC-SUM

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala MRC-SUM

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Extremidad Superior Derecha (ESD) |
| Q02 | varchar |  |  | SI | Abducción de Hombro ESD |
| Q02ObsDR | varchar |  | FK | SI | Abducción de Hombro ESD DR |
| Q03 | varchar |  |  | SI | Flexión de Codo ESD |
| Q03ObsDR | varchar |  | FK | SI | Flexión de Codo ESD DR |
| Q04 | varchar |  |  | SI | Extensión de Muñeca ESD |
| Q04ObsDR | varchar |  | FK | SI | Extensión de Muñeca ESD DR |
| Q05 | varchar |  |  | SI | Total ESD |
| Q06 | varchar |  |  | SI | Extremidad Superior Izquierda (ESI) |
| Q07 | varchar |  |  | SI | Abducción de Hombro ESI |
| Q07ObsDR | varchar |  | FK | SI | Abducción de Hombro ESI DR |
| Q08 | varchar |  |  | SI | Flexión de Codo ESI |
| Q08ObsDR | varchar |  | FK | SI | Flexión de Codo ESI DR |
| Q09 | varchar |  |  | SI | Extensión de Muñeca ESI |
| Q09ObsDR | varchar |  | FK | SI | Extensión de Muñeca ESI DR |
| Q10 | varchar |  |  | SI | Extremidad Inferior Derecha (EID) |
| Q11 | varchar |  |  | SI | Flexión de Cadera EID |
| Q11ObsDR | varchar |  | FK | SI | Flexión de Cadera EID DR |
| Q12 | varchar |  |  | SI | Extensión de Rodilla EID |
| Q12ObsDR | varchar |  | FK | SI | Extensión de Rodilla EID DR |
| Q13 | varchar |  |  | SI | Dorsiflexión de Tobillo (Rodilla a 0°) EID |
| Q13ObsDR | varchar |  | FK | SI | Dorsiflexión de Tobillo (Rodilla a 0°) EID DR |
| Q14 | varchar |  |  | SI | Extremidad Inferior Izquierda (EII) |
| Q15 | varchar |  |  | SI | Flexión de Cadera EII |
| Q15ObsDR | varchar |  | FK | SI | Flexión de Cadera EII DR |
| Q16 | varchar |  |  | SI | Extensión de Rodilla EII |
| Q16ObsDR | varchar |  | FK | SI | Extensión de Rodilla EII DR |
| Q17 | varchar |  |  | SI | Dorsiflexión de Tobillo (Rodilla a 0°) EII |
| Q17ObsDR | varchar |  | FK | SI | Dorsiflexión de Tobillo (Rodilla a 0°) EII DR |
| Q18 | varchar |  |  | SI | Total ESI |
| Q19 | varchar |  |  | SI | Total EID |
| Q20 | varchar |  |  | SI | Total EII |
| Q21 | varchar |  |  | SI | Total Puntaje MRC |
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