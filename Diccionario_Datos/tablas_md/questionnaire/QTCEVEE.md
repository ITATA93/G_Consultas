# questionnaire.QTCEVEE

> VE Eliminacion

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* VE Eliminacion

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Objetivo Registro |
| Q02 | bit |  |  | SI | Autonomo |
| Q03 | bit |  |  | SI | Total |
| Q04 | bit |  |  | SI | Parcial |
| Q05 | varchar |  |  | SI | Detalle |
| Q06 | varchar |  |  | SI | Orina |
| Q07 | bit |  |  | SI | Anuria |
| Q08 | bit |  |  | SI | Incontinencia |
| Q09 | bit |  |  | SI | Ocasional |
| Q10 | bit |  |  | SI | Permanente |
| Q11 | bit |  |  | SI | Retencion |
| Q12 | bit |  |  | SI | Disuria |
| Q13 | bit |  |  | SI | Dispositivo |
| Q14 | varchar |  |  | SI | Tipo |
| Q15 | date |  |  | SI | Fecha Colocacion |
| Q16 | varchar |  |  | SI | Heces |
| Q17 | bit |  |  | SI | Estreñimiento |
| Q18 | bit |  |  | SI | Laxantes |
| Q19 | bit |  |  | SI | Diarrea |
| Q20 | bit |  |  | SI | Incontinencia Fecal |
| Q21 | bit |  |  | SI | Ocacional |
| Q22 | bit |  |  | SI | Permanente |
| Q23 | bit |  |  | SI | Ostomia |
| Q24 | bit |  |  | SI | Drenajes |
| Q25 | varchar |  |  | SI | Detalle |
| Q26 | bit |  |  | SI | Asp. Gastrica |
| Q27 | bit |  |  | SI | Pañal |
| Q28 | varchar |  |  | SI | Diagnóstico 1 |
| Q29 | varchar |  |  | SI | Diagnóstico 2 |
| Q30 | varchar |  |  | SI | Conclusión |
| Q31 | varchar |  |  | SI | Eliminación |
| Q32 | varchar |  |  | SI | Descripción Parcial |
| Q33 | varchar |  |  | SI | Detalle Aps.Gástrica |
| Q34 | varchar |  |  | SI | Detalle Pañal |
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