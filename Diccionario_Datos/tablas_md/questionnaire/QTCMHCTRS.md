# questionnaire.QTCMHCTRS

> Crisis Triage Rating Scale

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Crisis Triage Rating Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Reliability of client (Choose one or more) |
| Q02 | varchar |  |  | SI | Crisis Triage Rating Scale (CTRS)	 |
| Q03 | varchar |  |  | SI | Rating A: DANGEROUSNESS |
| Q04 | varchar |  |  | SI | Rating B: SUPPORT SYSTEM |
| Q05 | varchar |  |  | SI | Rating C: ABILITY TO COOPERATE |
| Q06 | varchar |  |  | SI | The scale evaluates the person in crisis on a scal... |
| Q07 | varchar |  |  | SI | 1. Dangerousness |
| Q08 | varchar |  |  | SI | 2. Support System |
| Q09 | varchar |  |  | SI | 3. Ability to Cooperate |
| Q10 | varchar |  |  | SI | The lowest possible score is 3 and the highest pos... |
| Q11 | varchar |  |  | SI | THE TOTAL CTRS SCORE CALCULATED AND PROVIDED BASED... |
| Q12 | varchar |  |  | SI | CTRS: Urgency of Response |
| Q13 | varchar |  |  | SI | 1 – 9: Extreme Urgency – immediate response requir... |
| Q14 | varchar |  |  | SI | 10: High Urgency – present to emergency department... |
| Q15 | varchar |  |  | SI | 11 – 13: Medium to Low Urgency – see within 24 – 4... |
| Q16 | varchar |  |  | SI | 14 – 15: Non-urgent – Problem solve with individua... |
| Q17 | varchar |  |  | SI | CTRS Rating |
| Q18 | varchar |  |  | SI | Dangerousness |
| Q19 | varchar |  |  | SI | Support System |
| Q20 | varchar |  |  | SI | Ability to Cooperate	 |
| Q21 | varchar |  |  | SI | CTRS Total |
| Q22 | varchar |  |  | SI | URGENCY OF RESPONSE GUIDELINE |
| Q23 | varchar |  |  | SI | 3-9 |
| Q24 | varchar |  |  | SI | Extreme / Severe (Immediate Response Recommended) |
| Q25 | varchar |  |  | SI | 10 |
| Q26 | varchar |  |  | SI | High (See within 2 Hours) |
| Q27 | varchar |  |  | SI | 11 |
| Q28 | varchar |  |  | SI | Medium (See within 12 hours) |
| Q29 | varchar |  |  | SI | 12-13 |
| Q30 | varchar |  |  | SI | Low (See within 48 hours) |
| Q31 | varchar |  |  | SI | 14-15 |
| Q32 | varchar |  |  | SI | Non-Urgent (See within 2 weeks) |
| Q33 | varchar |  |  | SI | The Crisis Triage Rating Scale (CTRS) is intended ... |
| Q34 | varchar |  |  | SI | Score |
| Q35 | varchar |  |  | SI | Classification |
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