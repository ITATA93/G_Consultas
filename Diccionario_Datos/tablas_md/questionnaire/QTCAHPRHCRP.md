# questionnaire.QTCAHPRHCRP

> Cardiac Rehabilitation Physiotherapy Assessment

**Schema:** questionnaire
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac Rehabilitation Physiotherapy Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Summary of Cardiac Condition |
| Q04 | varchar |  |  | SI | Pre Existing Injuries Impacting on Exercise Progra... |
| Q05 | varchar |  |  | SI | Current Exercise |
| Q06 | varchar |  |  | SI | Occupation / Recreation / Leisure |
| Q07 | varchar |  |  | SI | Physical Activities / ADL´s |
| Q08 | varchar |  |  | SI | Goals for Physical Activity / Exercise |
| Q09 | varchar |  |  | SI | Exercise Plan for Discharge |
| Q10 | varchar |  |  | SI | Physical Assessment |
| Q100 | varchar |  |  | SI | Diastolic |
| Q100ObsDR | varchar |  | FK | SI | Diastolic DR |
| Q101 | varchar |  |  | SI | Pulse |
| Q101ObsDR | varchar |  | FK | SI | Pulse DR |
| Q102 | varchar |  |  | SI | Rating of Perceived Exertion |
| Q102ObsDR | varchar |  | FK | SI | Rating of Perceived Exertion DR |
| Q103 | varchar |  |  | SI | Immediately Post Test |
| Q104 | varchar |  |  | SI | Respirations |
| Q104ObsDR | varchar |  | FK | SI | Respirations DR |
| Q105 | varchar |  |  | SI | Rating of Perceived Exertion |
| Q105ObsDR | varchar |  | FK | SI | Rating of Perceived Exertion DR |
| Q106 | varchar |  |  | SI | Auscultation |
| Q108 | varchar |  |  | SI | Further Monitoring  |
| Q109 | varchar |  |  | SI | (where necessary) |
| Q110 | varchar |  |  | SI | 2 Minutes Post Test |
| Q111 | varchar |  |  | SI | Systolic |
| Q111ObsDR | varchar |  | FK | SI | Systolic DR |
| Q112 | varchar |  |  | SI | Diastolic |
| Q112ObsDR | varchar |  | FK | SI | Diastolic DR |
| Q113 | varchar |  |  | SI | Pulse |
| Q113ObsDR | varchar |  | FK | SI | Pulse DR |
| Q114 | varchar |  |  | SI | Further Monitoring |
| Q115 | varchar |  |  | SI | (where necessary) |
| Q116 | varchar |  |  | SI | Reasons for Stopping the Test |
| Q117 | varchar |  |  | SI | Reason for stopping the Test |
| Q118 | varchar |  |  | SI | Other Comments |
| Q119 | varchar |  |  | SI | Bodymap |
| Q121 | varchar |  |  | SI | Burdon's Modified Borg Scale |
| Q121ObsDR | varchar |  | FK | SI | Burdon's Modified Borg Scale DR |
| Q122 | varchar |  |  | SI | Burdon's Modified Borg Scale |
| Q122ObsDR | varchar |  | FK | SI | Burdon's Modified Borg Scale DR |
| Q68 | varchar |  |  | SI | Baseline Values |
| Q69 | varchar |  |  | SI | Observation |
| Q70 | varchar |  |  | SI | Pulse |
| Q70ObsDR | varchar |  | FK | SI | Pulse DR |
| Q71 | varchar |  |  | SI | Systolic |
| Q71ObsDR | varchar |  | FK | SI | Systolic DR |
| Q72 | varchar |  |  | SI | Diastolic |
| Q72ObsDR | varchar |  | FK | SI | Diastolic DR |
| Q73 | varchar |  |  | SI | Chest |
| Q74 | varchar |  |  | SI | Respirations |
| Q74ObsDR | varchar |  | FK | SI | Respirations DR |
| Q75 | varchar |  |  | SI | Oxygen Saturation |
| Q75ObsDR | varchar |  | FK | SI | Oxygen Saturation DR |
| Q76 | varchar |  |  | SI | Auscultation |
| Q77 | varchar |  |  | SI | Weight |
| Q77ObsDR | varchar |  | FK | SI | Weight DR |
| Q78 | varchar |  |  | SI | Height |
| Q78ObsDR | varchar |  | FK | SI | Height DR |
| Q79 | varchar |  |  | SI | Waist Circumference |
| Q79ObsDR | varchar |  | FK | SI | Waist Circumference DR |
| Q80 | varchar |  |  | SI | Posture |
| Q81 | varchar |  |  | SI | Unloaded Range of Motion / Strength |
| Q82 | varchar |  |  | SI | (as required) |
| Q83 | varchar |  |  | SI | Angina / Cardiac Symptoms |
| Q84 | varchar |  |  | SI | Comment |
| Q85 | varchar |  |  | SI | Discussed Borg Scale |
| Q86 | varchar |  |  | SI | Comment |
| Q87 | varchar |  |  | SI | Exercise Test |
| Q88 | varchar |  |  | SI | Target HR Reserve |
| Q90 | varchar |  |  | SI | (Refer to Initial HR Range Guidelines) |
| Q91 | bit |  |  | SI | B-Blocker |
| Q92 | numeric |  |  | SI | 50% |
| Q93 | numeric |  |  | SI | 60% |
| Q94 | numeric |  |  | SI | 70% |
| Q95 | numeric |  |  | SI | 75% |
| Q97 | varchar |  |  | SI | Score |
| Q98 | varchar |  |  | SI | Systolic |
| Q98ObsDR | varchar |  | FK | SI | Systolic DR |
| Q99 | varchar |  |  | SI | (% of HR maximum)  |
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