# questionnaire.QGXXXCARDAE

> Cardiac Arrest exam/findings

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac Arrest exam/findings

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Pulses |
| Q02 | varchar |  |  | SI | Spontaneous |
| Q03 | varchar |  |  | SI | With CPR only |
| Q04 | varchar |  |  | SI | By doppler |
| Q05 | varchar |  |  | SI | Measurable BP |
| Q06 | varchar |  |  | SI | Systolic |
| Q06ObsDR | varchar |  | FK | SI | Systolic DR |
| Q07 | varchar |  |  | SI | Diastolic |
| Q07ObsDR | varchar |  | FK | SI | Diastolic DR |
| Q08 | varchar |  |  | SI | Responsiveness |
| Q08N | varchar |  |  | SI | Note |
| Q10a | varchar |  |  | SI | Pupil reaction (L) |
| Q10aN | varchar |  |  | SI | Note |
| Q10aObsDR | varchar |  | FK | SI | Pupil reaction (L) DR |
| Q10b | varchar |  |  | SI | Pupil reaction (R) |
| Q10bN | varchar |  |  | SI | Note |
| Q10bObsDR | varchar |  | FK | SI | Pupil reaction (R) DR |
| Q12a | varchar |  |  | SI | Pupil size (L) |
| Q12aN | varchar |  |  | SI | Note |
| Q12aObsDR | varchar |  | FK | SI | Pupil size (L) DR |
| Q12b | varchar |  |  | SI | Pupil size (R) |
| Q12bN | varchar |  |  | SI | Note |
| Q12bObsDR | varchar |  | FK | SI | Pupil size (R) DR |
| Q15 | varchar |  |  | SI | Cardiac rhythm (initial) |
| Q15N | varchar |  |  | SI | Note |
| Q17 | varchar |  |  | SI | Heart sounds |
| Q17N | varchar |  |  | SI | Note |
| Q19 | varchar |  |  | SI | Cardioversion / Countershock |
| Q20 | varchar |  |  | SI | Response |
| Q20N | varchar |  |  | SI | Note |
| Q20SPN | bit |  |  | SI | See procedure notes |
| Q23 | varchar |  |  | SI | Respiratory effort |
| Q23N | varchar |  |  | SI | Note |
| Q25 | varchar |  |  | SI | Bag-mask ventilation |
| Q26 | varchar |  |  | SI | Endotracheal tube placed |
| Q27 | varchar |  |  | SI | Successful |
| Q28 | varchar |  |  | SI | Position verified |
| Q28CG | varchar |  |  | SI | If yes |
| Q28N | varchar |  |  | SI | Note |
| Q28SPN | bit |  |  | SI | See procedure notes |
| Q32 | varchar |  |  | SI | Lung sounds |
| Q32N | varchar |  |  | SI | Note |
| Q34 | varchar |  |  | SI | Patient deceased |
| Q36 | varchar |  |  | SI | Spontaneous circulation restored |
| Q37 | varchar |  |  | SI | Spontaneous respiration |
| Q38 | varchar |  |  | SI | On ventilator |
| Q39 | varchar |  |  | SI | Patient requires circulatory support |
| Q39CBG | varchar |  |  | SI | If yes |
| Q39N | varchar |  |  | SI | Note |
| Q42 | varchar |  |  | SI | Neurological status |
| Q42N | varchar |  |  | SI | Note |
| Q46 | varchar |  |  | SI | Cardiac rhythm (initial) |
| Q47 | varchar |  |  | SI | Heart sounds |
| Q48 | varchar |  |  | SI | Respiratory effort |
| Q49 | varchar |  |  | SI | Lung sounds |
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