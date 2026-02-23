# questionnaire.QTCCWS

> Cannabis Withdrawal Scale

**Schema:** questionnaire
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cannabis Withdrawal Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Restlessness / agitation |
| Q02 | varchar |  |  | SI | Mood changes |
| Q03 | varchar |  |  | SI | Fear |
| Q04 | varchar |  |  | SI | Sleep |
| Q05 | varchar |  |  | SI | Hunger |
| Q06 | varchar |  |  | SI | Feelings of unreality |
| Q07 | varchar |  |  | SI | Racing thoughts |
| Q08 | varchar |  |  | SI | Drowsiness - observation |
| Q09 | varchar |  |  | SI | Appetite |
| Q10 | varchar |  |  | SI | Other symptoms |
| Q11 | varchar |  |  | SI | Temperature |
| Q11ObsDR | varchar |  | FK | SI | Temperature DR |
| Q12 | varchar |  |  | SI | Pulse |
| Q12ObsDR | varchar |  | FK | SI | Pulse DR |
| Q13 | varchar |  |  | SI | Respiration |
| Q13ObsDR | varchar |  | FK | SI | Respiration DR |
| Q14 | varchar |  |  | SI | Systolic BP |
| Q14ObsDR | varchar |  | FK | SI | Systolic BP DR |
| Q15 | varchar |  |  | SI | Diastolic BP |
| Q15ObsDR | varchar |  | FK | SI | Diastolic BP DR |
| Q16 | varchar |  |  | SI | Pupil size (L) |
| Q16ObsDR | varchar |  | FK | SI | Pupil size (L) DR |
| Q17 | varchar |  |  | SI | Pupil reaction (L) |
| Q17ObsDR | varchar |  | FK | SI | Pupil reaction (L) DR |
| Q18 | varchar |  |  | SI | Pupil size (R) |
| Q18ObsDR | varchar |  | FK | SI | Pupil size (R) DR |
| Q19 | varchar |  |  | SI | Pupil reaction (R) |
| Q19ObsDR | varchar |  | FK | SI | Pupil reaction (R) DR |
| Q20 | varchar |  |  | SI | Weight |
| Q20ObsDR | varchar |  | FK | SI | Weight DR |
| Q21 | varchar |  |  | SI | Symptom |
| Q22 | varchar |  |  | SI | Scoring |
| Q23 | varchar |  |  | SI | Questions |
| Q24 | varchar |  |  | SI | Do you feel more restless than you are normally? |
| Q25 | varchar |  |  | SI | Are your moods changing over a short period of tim... |
| Q26 | varchar |  |  | SI | Do you feel fearful? |
| Q27 | varchar |  |  | SI | How did you sleep last night? |
| Q28 | varchar |  |  | SI | Do you feel hungry? |
| Q29 | varchar |  |  | SI | Are your thoughts racing? |
| Q30 | varchar |  |  | SI | Do you feel sleepy or drowsy?	 |
| Q31 | varchar |  |  | SI | Have you noticed any changes in your appetite? |
| Q32 | varchar |  |  | SI | Do you feel that things around you are not real or... |
| Q33 | varchar |  |  | SI | Score |
| Q34 | varchar |  |  | SI | Classification |
| Q35 | varchar |  |  | SI | 0 - 63 |
| Q36 | varchar |  |  | SI | 0 is no withdrawal symptoms and 63 is the most sev... |
| Q37 | varchar |  |  | SI | 0 - 63: 0 is no withdrawal symptoms and 63 is the ... |
| Q38 | varchar |  |  | SI | 0 is no withdrawal symptoms and 63 is the most sev... |
| Q39 | varchar |  |  | SI | The Cannabis Withdrawal Scale is used to assess th... |
| Q40 | varchar |  |  | SI | The Cannabis Withdrawal Scale is used to assess th... |
| Q41 | date |  |  | SI | Date |
| Q42 | time |  |  | SI | Time |
| Q43 | varchar |  |  | SI | Restlessness / agitation |
| Q44 | varchar |  |  | SI | Mood changes |
| Q45 | varchar |  |  | SI | Fear |
| Q46 | varchar |  |  | SI | Sleep |
| Q47 | varchar |  |  | SI | Hunger |
| Q48 | varchar |  |  | SI | Feelings of unreality |
| Q49 | varchar |  |  | SI | Racing thoughts |
| Q50 | varchar |  |  | SI | Drowsiness - observation |
| Q51 | varchar |  |  | SI | Appetite |
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