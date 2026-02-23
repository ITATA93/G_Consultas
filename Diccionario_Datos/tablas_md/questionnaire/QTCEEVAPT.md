# questionnaire.QTCEEVAPT

> Evaluacion de Puestos de Trabajo N

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluacion de Puestos de Trabajo N

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
| CQ11 | varchar |  |  | SI | - |
| CQ12 | varchar |  |  | SI | - |
| CQ13 | varchar |  |  | SI | - |
| CQ14 | varchar |  |  | SI | - |
| CQ15 | varchar |  |  | SI | - |
| CQ16 | varchar |  |  | SI | - |
| CQ17 | varchar |  |  | SI | - |
| Q01 | varchar |  |  | SI | Demandas de tiempo |
| Q02 | varchar |  |  | SI | Demandas de las tareas |
| Q03 | varchar |  |  | SI | Atraccion por las tareas laborales |
| Q04 | varchar |  |  | SI | Horario de trabajo |
| Q05 | varchar |  |  | SI | Interaccion entre compañeros de trabajo |
| Q06 | varchar |  |  | SI | Pertenencia a un grupo de trabajo |
| Q07 | varchar |  |  | SI | Interaccion con el supervisor |
| Q08 | varchar |  |  | SI | Estandares del rol laboral |
| Q09 | varchar |  |  | SI | Estilo del rol laboral |
| Q10 | varchar |  |  | SI | Interaccion con otros |
| Q11 | varchar |  |  | SI | Gratificaciones |
| Q12 | varchar |  |  | SI | Cualidades sensoriales ambientales |
| Q13 | varchar |  |  | SI | Arquitectura/ disposicion fisica del ambiente |
| Q14 | varchar |  |  | SI | Ambiente: Clima/Humor |
| Q15 | varchar |  |  | SI | Propiedades de los objetos |
| Q16 | varchar |  |  | SI | Lugares complementarios |
| Q17 | varchar |  |  | SI | Significado o sentido de los objetos o productos |
| QC1 | varchar |  |  | SI | Comentario1 |
| QC10 | varchar |  |  | SI | Comentario10 |
| QC11 | varchar |  |  | SI | Comentario11 |
| QC12 | varchar |  |  | SI | Comentario12 |
| QC13 | varchar |  |  | SI | Comentario13 |
| QC14 | varchar |  |  | SI | Comentario14 |
| QC15 | varchar |  |  | SI | Comentario15 |
| QC16 | varchar |  |  | SI | Comentario16 |
| QC17 | varchar |  |  | SI | Comentario17 |
| QC2 | varchar |  |  | SI | Comentario2 |
| QC3 | varchar |  |  | SI | Comentario3 |
| QC4 | varchar |  |  | SI | Comentario4 |
| QC5 | varchar |  |  | SI | Comentario5 |
| QC6 | varchar |  |  | SI | Comentario6 |
| QC7 | varchar |  |  | SI | Comentario7 |
| QC8 | varchar |  |  | SI | Comentario8 |
| QC9 | varchar |  |  | SI | Comentario9 |
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