# questionnaire.QTCEPEROD

> Periodoncia

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Periodoncia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q02 | varchar |  |  | SI | Ferulización |
| Q03 | date |  |  | SI | Impresión |
| Q04 | date |  |  | SI | Prueba de cera  |
| Q05 | date |  |  | SI | Instalación de planos de alivio oclusal/alta |
| Q06 | date |  |  | SI | Controles 1  |
| Q07 | date |  |  | SI | Controles 2 |
| Q08 | date |  |  | SI | Controles 3 |
| Q09 | date |  |  | SI | Cirugia Periodontal |
| Q10 | date |  |  | SI | Destartraje supragingival y pulido coronario |
| Q11 | date |  |  | SI | Destartraje subgingival y pulido radicular |
| Q12 | varchar |  |  | SI | Pronostico |
| Q17 | varchar |  |  | SI | Observaciones |
| Q18 | bit |  |  | SI | Periodontal |
| Q19 | bit |  |  | SI | De Mantención |
| Q24 | varchar |  |  | SI | Destartraje |
| Q28 | varchar |  |  | SI | Categoria de la carta |
| Q29 | varchar |  |  | SI | Malo |
| Q30 | varchar |  |  | SI | Digitado Por |
| Q33 | varchar |  |  | SI | Estado de la Pieza |
| QPer | varchar |  |  | SI | Periodontograma |
| QRem1 | date |  |  | SI | Instalación / Alta |
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
| Qo1 | varchar |  |  | SI | Observación 1 |
| Qo2 | varchar |  |  | SI | Observación 2 |
| Qo3 | varchar |  |  | SI | Observación 3 |
| Qo4 | varchar |  |  | SI | Observación 4 |
| Qo5 | varchar |  |  | SI | Observación 5 |
| Qo6 | varchar |  |  | SI | Observación 6 |
| Qo7 | varchar |  |  | SI | Observación 7 |
| Qo8 | varchar |  |  | SI | Observación 8 |
| Qo9 | varchar |  |  | SI | Observación 9 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*