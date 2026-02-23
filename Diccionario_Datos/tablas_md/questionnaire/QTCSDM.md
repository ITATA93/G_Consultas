# questionnaire.QTCSDM

> Shoulder Dystocia Management

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Shoulder Dystocia Management

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Fetus number |
| Q04 | varchar |  |  | SI | Maternal position when shoulder dystocia identifie... |
| Q05 | varchar |  |  | SI | If other, please specify |
| Q06 | time |  |  | SI | Call for help time |
| Q07 | time |  |  | SI | Obstetric emergency called time |
| Q08 | varchar |  |  | SI | (this is different from initial call for help) |
| Q09 | time |  |  | SI | Neonatologist / Paediatrician called time |
| Q11 | varchar |  |  | SI | Slow advancement of fetal head |
| Q12 | varchar |  |  | SI | Difficult delivery of fetal face |
| Q13 | varchar |  |  | SI | Slow or no restitution of fetal head |
| Q14 | varchar |  |  | SI | Turtle sign / Fetal chin retraction onto perineum |
| Q15 | varchar |  |  | SI | Other signs of shoulder dystocia |
| Q16 | varchar |  |  | SI | If other, please specify |
| Q17 | time |  |  | SI | Time of birth of fetal head |
| Q18 | varchar |  |  | SI | Birth of head mode |
| Q19 | varchar |  |  | SI | Fetal position during dystocia |
| Q20 | varchar |  |  | SI | Episiotomy for manoeuvres |
| Q22 | varchar |  |  | SI | Overall comments |
| Q23 | time |  |  | SI | Time of shoulder dystocia resolution (birth of bab... |
| Q24 | numeric |  |  | SI | Head to body delivery interval (mins) |
| Q25 | varchar |  |  | SI | Shoulder dystocia explained to parents |
| Q26 | varchar |  |  | SI | Explained by |
| Q27 | varchar |  |  | SI | Leaflet given |
| Q28 | varchar |  |  | SI | Incident number |
| Q29 | varchar |  |  | SI | Signature |
| Q30 | varchar |  |  | SI | Counter signature |
| Q31 | numeric |  |  | SI | Head to body delivery interval (mins) |
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