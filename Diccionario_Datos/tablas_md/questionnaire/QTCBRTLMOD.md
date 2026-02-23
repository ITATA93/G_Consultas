# questionnaire.QTCBRTLMOD

> Barthel Index - modified version

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Barthel Index - modified version

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Completed at |
| Q04 | varchar |  |  | SI | Feeding |
| Q05 | varchar |  |  | SI | Bathing |
| Q06 | varchar |  |  | SI | Grooming |
| Q07 | varchar |  |  | SI | Dressing |
| Q08 | varchar |  |  | SI | Bowels |
| Q09 | varchar |  |  | SI | Bladder |
| Q10 | varchar |  |  | SI | Toilet use |
| Q11 | varchar |  |  | SI | Transfers (bed to chair and back) |
| Q12 | varchar |  |  | SI | Mobility (on level surfaces) |
| Q13 | varchar |  |  | SI | Stairs |
| Q14 | varchar |  |  | SI | Wheelchair |
| Q15 | varchar |  |  | SI | 0-24: Total dependency |
| Q16 | varchar |  |  | SI | 25-49: Severe dependency |
| Q17 | varchar |  |  | SI | 50-74: Moderate dependency |
| Q18 | varchar |  |  | SI | 75-90: Slight dependency |
| Q19 | varchar |  |  | SI | 91-99: Nearly independency |
| Q20 | varchar |  |  | SI | 100: Complete independency |
| Q21 | varchar |  |  | SI | The Barthel scale is a scale used to measure perfo... |
| Q22 | varchar |  |  | SI | General |
| Q23 | varchar |  |  | SI | • The Index should be used as a record of what a p... |
| Q24 | varchar |  |  | SI | • The main aim is to establish degree of independe... |
| Q25 | varchar |  |  | SI | • The need for supervision renders the patient not... |
| Q26 | varchar |  |  | SI | • A patient's performance should be established us... |
| Q27 | varchar |  |  | SI | friends / relatives, and nurses will be the usual ... |
| Q28 | varchar |  |  | SI | • Usually the performance over the preceding 24 – ... |
| Q29 | varchar |  |  | SI | • Unconscious patients should score '0' throughout... |
| Q30 | varchar |  |  | SI | • Middle categories imply that the patient supplie... |
| Q31 | varchar |  |  | SI | • Use of aids to be independent is allowed. |
| Q32 | varchar |  |  | SI | Wheelchair use must be scored only if mobility sco... |
| Q33 | varchar |  |  | SI | Score |
| Q34 | varchar |  |  | SI | Classification |
| Q35 | varchar |  |  | SI | 0-24 |
| Q36 | varchar |  |  | SI | Total dependency |
| Q37 | varchar |  |  | SI | 25-49 |
| Q38 | varchar |  |  | SI | Severe dependency |
| Q39 | varchar |  |  | SI | 50-74 |
| Q40 | varchar |  |  | SI | Moderate dependency |
| Q41 | varchar |  |  | SI | 75-90 |
| Q42 | varchar |  |  | SI | Slight dependency |
| Q43 | varchar |  |  | SI | 91-99 |
| Q44 | varchar |  |  | SI | Nearly independency	 |
| Q45 | varchar |  |  | SI | 100 |
| Q46 | varchar |  |  | SI | Complete independency |
| Q47 | varchar |  |  | SI | 0-25: Total dependency |
| Q48 | varchar |  |  | SI | 25-49: Severe dependency |
| Q49 | varchar |  |  | SI | 50-74: Moderate dependency |
| Q50 | varchar |  |  | SI | 75-90: Slight dependency |
| Q51 | varchar |  |  | SI | 91-99: Nearly independency |
| Q52 | varchar |  |  | SI | 100: Complete independency |
| Q53 | varchar |  |  | SI | The Barthel scale is a scale used to measure perfo... |
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