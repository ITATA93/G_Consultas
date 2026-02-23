# questionnaire.QTCERPAP

> Resultado PAP

**Schema:** questionnaire
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Resultado PAP

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Resultado PAP |
| Q02 | varchar |  |  | SI | Diagnóstico Principal PAP |
| Q02ObsDR | varchar |  | FK | SI | Diagnóstico Principal PAP DR |
| Q03 | varchar |  |  | SI | Otros Diagnósticos PAP |
| Q03ObsDR | varchar |  | FK | SI | Otros Diagnósticos PAP DR |
| Q04 | varchar |  |  | SI | Otros Diagnósticos PAP (S) |
| Q04ObsDR | varchar |  | FK | SI | Otros Diagnósticos PAP (S) DR |
| Q05 | varchar |  |  | SI | Descripción de sugerencias |
| Q05ObsDR | varchar |  | FK | SI | Descripción de sugerencias DR |
| Q06 | varchar |  |  | SI | Fecha Próximo Exámen |
| Q06ObsDR | varchar |  | FK | SI | Fecha Próximo Exámen DR |
| Q07 | date |  |  | SI | Fecha de Vencimiento |
| Q08 | date |  |  | SI | Fecha Toma de PAP |
| Q09 | varchar |  |  | SI | Diagnósticos Primarios |
| Q09ObsDR | varchar |  | FK | SI | Diagnósticos Primarios DR |
| Q10 | varchar |  |  | SI | Descripción de la Calidad de la Muestra  |
| Q10ObsDR | varchar |  | FK | SI | Descripción de la Calidad de la Muestra  DR |
| Q11 | varchar |  |  | SI | Diagnósticos Secundarios  |
| Q11ObsDR | varchar |  | FK | SI | Diagnósticos Secundarios  DR |
| Q12 | varchar |  |  | SI | Fecha de Ingreso PAP  |
| Q12ObsDR | varchar |  | FK | SI | Fecha de Ingreso PAP  DR |
| Q13 | varchar |  |  | SI | Lugar Realización Examen |
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