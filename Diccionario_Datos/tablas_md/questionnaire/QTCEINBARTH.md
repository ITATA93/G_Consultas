# questionnaire.QTCEINBARTH

> Indice de Barthel

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Indice de Barthel

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ01 | varchar |  |  | SI | - |
| CQ02 | varchar |  |  | SI | - |
| CQ03 | varchar |  |  | SI | - |
| CQ04 | varchar |  |  | SI | - |
| CQ05 | varchar |  |  | SI | - |
| CQ06 | varchar |  |  | SI | - |
| CQ07 | varchar |  |  | SI | - |
| CQ08 | varchar |  |  | SI | - |
| CQ09 | varchar |  |  | SI | - |
| CQ10 | varchar |  |  | SI | - |
| Q01 | varchar |  |  | SI | Comer |
| Q02 | varchar |  |  | SI | Lavarse |
| Q03 | varchar |  |  | SI | Vestirse |
| Q04 | varchar |  |  | SI | Arreglarse |
| Q05 | varchar |  |  | SI | Deposiciones (Valorese la semana previa) |
| Q06 | varchar |  |  | SI | Micción (Valorese la semana previa) |
| Q07 | varchar |  |  | SI | Usar el Retrete |
| Q08 | varchar |  |  | SI | Trasladarse |
| Q09 | varchar |  |  | SI | Deambular |
| Q10 | varchar |  |  | SI | Escalones |
| Q11 | varchar |  |  | SI | Puntaje |
| Q13 | varchar |  |  | SI | Resultado Indice Barthel |
| Q13ObsDR | varchar |  | FK | SI | Resultado Indice Barthel DR |
| Q14 | date |  |  | SI | Fecha de Realización |
| Q15 | time |  |  | SI | Hora de Realización |
| Q16 | varchar |  |  | SI | Fecha/Hora de Realización |
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