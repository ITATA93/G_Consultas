# questionnaire.QTCNSASPECT

> Alberta Stroke Program Early CT Score (ASPECTS)

**Schema:** questionnaire
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Alberta Stroke Program Early CT Score (ASPECTS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | (C) Caudate  |
| Q02 | varchar |  |  | SI | (I) Insular Ribbon |
| Q03 | varchar |  |  | SI | (IC) Internal Capsule  |
| Q04 | varchar |  |  | SI | (L) Lentiform nucleus  |
| Q05 | varchar |  |  | SI | (MCA1) Anterior MCA cortex  |
| Q06 | varchar |  |  | SI | (MCA2) MCA cortex lateral to the insular ribbon  |
| Q07 | varchar |  |  | SI | (MCA3) Posterior MCA cortex  |
| Q08 | varchar |  |  | SI | (MCA4) Anterior cortex immediately rostal to M1  |
| Q09 | varchar |  |  | SI | (MCA5) Lateral cortex immediately rostal to M3  |
| Q10 | varchar |  |  | SI | (MCA6) Posterior cortex immediately rostal to M3  |
| Q11 | varchar |  |  | SI | 95% prob of survial if ASPECTS >7 |
| Q12 | varchar |  |  | SI | 90% prob of poor outcome if ASPECTS <7 |
| Q13 | varchar |  |  | SI | 95% probability of survival  |
| Q14 | varchar |  |  | SI | 99% probability of no SICH |
| Q15 | varchar |  |  | SI | Score 0 - 7 |
| Q16 | varchar |  |  | SI | Score 8 - 10 |
| Q17 | varchar |  |  | SI | 90% probability of poor outcome |
| Q18 | varchar |  |  | SI | Subcortical Structures |
| Q19 | varchar |  |  | SI | MCA Cortex |
| Q20 | varchar |  |  | SI | ASPECTS  is a 10-point quantitative topographic CT... |
| Q21 | varchar |  |  | SI | Segmental assessment of the MCA vascular territory... |
| Q22 | varchar |  |  | SI | No ischaemia in the MCA territory would score 10 &... |
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