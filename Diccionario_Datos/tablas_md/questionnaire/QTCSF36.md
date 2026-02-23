# questionnaire.QTCSF36

> 36-Item Short Form Survey (SF-36)

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* 36-Item Short Form Survey (SF-36)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | In general, would you say your health is |
| Q04 | varchar |  |  | SI | Compared to one year ago, how would you rate your ... |
| Q05 | varchar |  |  | SI | The following items are about activities you might... |
| Q06 | varchar |  |  | SI | Vigorous activities, such as running, lifting heav... |
| Q07 | varchar |  |  | SI | Moderate activities, such as moving a table, pushi... |
| Q08 | varchar |  |  | SI | Lifting or carrying groceries |
| Q09 | varchar |  |  | SI | Climbing several flights of stairs |
| Q10 | varchar |  |  | SI | Climbing one flight of stairs |
| Q11 | varchar |  |  | SI | Bending, kneeling, or stooping |
| Q12 | varchar |  |  | SI | Walking more than a mile |
| Q13 | varchar |  |  | SI | Walking several blocks |
| Q14 | varchar |  |  | SI | Walking one block |
| Q15 | varchar |  |  | SI | Bathing or dressing yourself |
| Q16 | varchar |  |  | SI | During the past 4 weeks, have you had any of the f... |
| Q17 | varchar |  |  | SI | Cut down the amount of time you spent on work or o... |
| Q18 | varchar |  |  | SI | Accomplished less than you would like |
| Q19 | varchar |  |  | SI | Were limited in the kind of work or other activiti... |
| Q20 | varchar |  |  | SI | Had difficulty performing the work or other activi... |
| Q21 | varchar |  |  | SI | During the past 4 weeks, have you had any of the f... |
| Q22 | varchar |  |  | SI | Cut down the amount of time you spent on work or o... |
| Q23 | varchar |  |  | SI | Accomplished less than you would like |
| Q24 | varchar |  |  | SI | Didn't do work or other activities as carefully as... |
| Q25 | varchar |  |  | SI | During the past 4 weeks, to what extent has your p... |
| Q26 | varchar |  |  | SI | How much bodily pain have you had during the past ... |
| Q27 | varchar |  |  | SI | During the past 4 weeks, how much did pain interfe... |
| Q28 | varchar |  |  | SI | These questions are about how you feel and how thi... |
| Q29 | varchar |  |  | SI | How much of the time during the past 4 weeks: |
| Q30 | varchar |  |  | SI | Did you feel full of pep? |
| Q31 | varchar |  |  | SI | Have you been a very nervous person? |
| Q32 | varchar |  |  | SI | Have you felt so down in the dumps that nothing co... |
| Q33 | varchar |  |  | SI | Have you felt calm and peaceful? |
| Q34 | varchar |  |  | SI | Did you have a lot of energy? |
| Q35 | varchar |  |  | SI | Have you felt downhearted and blue? |
| Q36 | varchar |  |  | SI |  Did you feel worn out? |
| Q37 | varchar |  |  | SI | Have you been a happy person? |
| Q38 | varchar |  |  | SI |  Did you feel tired? |
| Q39 | varchar |  |  | SI | During the past 4 weeks, how much of the time has ... |
| Q40 | varchar |  |  | SI | How TRUE or FALSE is each of the following stateme... |
| Q41 | varchar |  |  | SI | I seem to get sick a little easier than other peop... |
| Q42 | varchar |  |  | SI | I am as healthy as anybody I know |
| Q43 | varchar |  |  | SI | I expect my health to get worse |
| Q44 | varchar |  |  | SI | My health is excellent |
| Q45 | varchar |  |  | SI | Notes |
| Q46 | varchar |  |  | SI | Total score |
| Q47 | varchar |  |  | SI | Physical functioning |
| Q48 | varchar |  |  | SI | Role limitations due to physical health |
| Q49 | varchar |  |  | SI | Role limitations due to emotional problems |
| Q50 | varchar |  |  | SI | Energy / Fatigue |
| Q51 | varchar |  |  | SI | Emotional well-being |
| Q52 | varchar |  |  | SI | Social functioning |
| Q53 | varchar |  |  | SI | Pain |
| Q54 | varchar |  |  | SI | General health |
| Q55 | varchar |  |  | SI | Lower scores indicate more disability while higher... |
| Q56 | varchar |  |  | SI | Physical functioning, Bodily pain, Role limitation... |
| Q57 | varchar |  |  | SI | Emotional well-being, Social functioning, Energy F... |
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