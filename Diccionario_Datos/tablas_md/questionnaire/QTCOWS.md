# questionnaire.QTCOWS

> Clinical Opiate Withdrawal Scale (COWS)

**Schema:** questionnaire
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Clinical Opiate Withdrawal Scale (COWS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Sweating |
| Q02 | varchar |  |  | SI | Tremor |
| Q03 | varchar |  |  | SI | Yawning |
| Q04 | varchar |  |  | SI | Bone or joint aches |
| Q05 | varchar |  |  | SI | Gooseflesh skin |
| Q06 | varchar |  |  | SI | Pupil size	 |
| Q07 | varchar |  |  | SI | Restleness |
| Q08 | varchar |  |  | SI | GI upset |
| Q09 | varchar |  |  | SI | Anxiety or irritability |
| Q10 | varchar |  |  | SI | Runny nose or tearing	 |
| Q11 | varchar |  |  | SI | Resting&nbsp;heart&nbsp;rate |
| Q12 | varchar |  |  | SI | Pupil Size (L) mm	 |
| Q12ObsDR | varchar |  | FK | SI | Pupil Size (L) mm	 DR |
| Q13 | varchar |  |  | SI | Pupil Reaction (L) |
| Q13ObsDR | varchar |  | FK | SI | Pupil Reaction (L) DR |
| Q14 | varchar |  |  | SI | Pupil Size (R) mm	 |
| Q14ObsDR | varchar |  | FK | SI | Pupil Size (R) mm	 DR |
| Q15 | varchar |  |  | SI | Pupil Reaction (R) |
| Q15ObsDR | varchar |  | FK | SI | Pupil Reaction (R) DR |
| Q16 | varchar |  |  | SI | Temperature |
| Q16ObsDR | varchar |  | FK | SI | Temperature DR |
| Q17 | varchar |  |  | SI | Systolic BP |
| Q17ObsDR | varchar |  | FK | SI | Systolic BP DR |
| Q18 | varchar |  |  | SI | Diastolic BP |
| Q18ObsDR | varchar |  | FK | SI | Diastolic BP DR |
| Q19 | varchar |  |  | SI | Respiration |
| Q19ObsDR | varchar |  | FK | SI | Respiration DR |
| Q20 | varchar |  |  | SI | Heart rate |
| Q20ObsDR | varchar |  | FK | SI | Heart rate DR |
| Q21 | varchar |  |  | SI | SCORING  |
| Q22 | varchar |  |  | SI | SCORING |
| Q23 | varchar |  |  | SI | SYMPTOM |
| Q24 | varchar |  |  | SI | SYMPTOM |
| Q25 | varchar |  |  | SI | Score |
| Q26 | varchar |  |  | SI | Classification	 |
| Q27 | varchar |  |  | SI | 5 to12 |
| Q28 | varchar |  |  | SI | 13 to&nbsp;24 |
| Q29 | varchar |  |  | SI | 25 to&nbsp;36 |
| Q30 | varchar |  |  | SI | > 36 	 |
| Q31 | varchar |  |  | SI | Total scores are indicative of increasing or decre... |
| Q32 | varchar |  |  | SI | Clinical opiate withdrawal scale is used to assess... |
| Q33 | varchar |  |  | SI | 0 to&nbsp;4 |
| Q34 | varchar |  |  | SI | No significant signs of withdrawal |
| Q35 | varchar |  |  | SI | Mild withdrawal |
| Q36 | varchar |  |  | SI | Moderate withdrawal |
| Q37 | varchar |  |  | SI | Moderately severe withdrawal	 |
| Q38 | varchar |  |  | SI | Severe withdrawal |
| Q39 | date |  |  | SI | Date |
| Q40 | time |  |  | SI | Time |
| Q41 | varchar |  |  | SI | Vital signs observation chart is required when com... |
| Q42 | varchar |  |  | SI | Resting heart rate |
| Q43 | varchar |  |  | SI | Sweating: over past 1/2 hour not accounted for by ... |
| Q44 | varchar |  |  | SI | Restlessness: Observation during assessment |
| Q45 | varchar |  |  | SI | Pupil size |
| Q46 | varchar |  |  | SI | Bone or joint aches:&nbsp;if patient was having pa... |
| Q47 | varchar |  |  | SI | Runny nose or tearing: not accounted for by cold s... |
| Q48 | varchar |  |  | SI | GI upset: over last 1/2 hour |
| Q49 | varchar |  |  | SI | Tremor: observation of outstretched hands |
| Q50 | varchar |  |  | SI | Yawning: observation of outstretched hands |
| Q51 | varchar |  |  | SI | Anxiety or irritability |
| Q52 | varchar |  |  | SI | Gooseflesh skin |
| Q53 | varchar |  |  | SI | Wesson DR, Ling W. The Clinical Opiate Withdrawal ... |
| Q54 | varchar |  |  | SI | Restlessness |
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