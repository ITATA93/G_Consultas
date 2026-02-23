# questionnaire.QGXXXACEX

> Activity and Exercise

**Schema:** questionnaire
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Activity and Exercise

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Systolic BP |
| Q01N | varchar |  |  | SI | Note |
| Q01ObsDR | varchar |  | FK | SI | Systolic BP DR |
| Q03 | varchar |  |  | SI | Diastolic BP |
| Q03ObsDR | varchar |  | FK | SI | Diastolic BP DR |
| Q04 | varchar |  |  | SI | Temperature |
| Q04ObsDR | varchar |  | FK | SI | Temperature DR |
| Q05 | varchar |  |  | SI | Pulse |
| Q05N | varchar |  |  | SI | Note |
| Q05ObsDR | varchar |  | FK | SI | Pulse DR |
| Q05Q | varchar |  |  | SI | Pulse quality |
| Q05QObsDR | varchar |  | FK | SI | Pulse quality DR |
| Q05R | varchar |  |  | SI | Pulse rhythm |
| Q05RObsDR | varchar |  | FK | SI | Pulse rhythm DR |
| Q06 | varchar |  |  | SI | Respiration |
| Q06ObsDR | varchar |  | FK | SI | Respiration DR |
| Q07 | varchar |  |  | SI | Mean Arterial Pressure |
| Q08 | varchar |  |  | SI | Pain cardio |
| Q08ObsDR | varchar |  | FK | SI | Pain cardio DR |
| Q12 | varchar |  |  | SI | Pacemaker |
| Q12N | varchar |  |  | SI | Note |
| Q12ObsDR | varchar |  | FK | SI | Pacemaker DR |
| Q14 | varchar |  |  | SI | Oxygen Saturation |
| Q14ObsDR | varchar |  | FK | SI | Oxygen Saturation DR |
| Q15 | varchar |  |  | SI | Oxygen l/min |
| Q15N | varchar |  |  | SI | Note |
| Q15ObsDR | varchar |  | FK | SI | Oxygen l/min DR |
| Q17 | varchar |  |  | SI | Dyspnoea |
| Q17N | varchar |  |  | SI | Note |
| Q17ObsDR | varchar |  | FK | SI | Dyspnoea DR |
| Q19 | varchar |  |  | SI | Superficial |
| Q19N | varchar |  |  | SI | Note |
| Q19ObsDR | varchar |  | FK | SI | Superficial DR |
| Q21 | varchar |  |  | SI | Rapid |
| Q21N | varchar |  |  | SI | Note |
| Q21ObsDR | varchar |  | FK | SI | Rapid DR |
| Q23 | varchar |  |  | SI | Cough |
| Q23N | varchar |  |  | SI | Note |
| Q23ObsDR | varchar |  | FK | SI | Cough DR |
| Q25 | varchar |  |  | SI | Oxygene at home |
| Q25N | varchar |  |  | SI | Note |
| Q25ObsDR | varchar |  | FK | SI | Oxygene at home DR |
| Q27 | varchar |  |  | SI | Tracheotomy |
| Q27N | varchar |  |  | SI | Note |
| Q27ObsDR | varchar |  | FK | SI | Tracheotomy DR |
| Q29 | varchar |  |  | SI | Paralysis |
| Q29N | varchar |  |  | SI | Note |
| Q29ObsDR | varchar |  | FK | SI | Paralysis DR |
| Q31 | varchar |  |  | SI | Amputation |
| Q31N | varchar |  |  | SI | Note |
| Q31ObsDR | varchar |  | FK | SI | Amputation DR |
| Q33 | varchar |  |  | SI | Mobilization at home |
| Q33N | varchar |  |  | SI | Note |
| Q33ObsDR | varchar |  | FK | SI | Mobilization at home DR |
| Q35 | varchar |  |  | SI | Mobilization |
| Q35N | varchar |  |  | SI | Note |
| Q35ObsDR | varchar |  | FK | SI | Mobilization DR |
| Q37 | varchar |  |  | SI | Mobilization limited |
| Q37N | varchar |  |  | SI | Note |
| Q37ObsDR | varchar |  | FK | SI | Mobilization limited DR |
| Q8N | varchar |  |  | SI | Note |
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