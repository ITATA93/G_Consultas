# questionnaire.QTCPRWHE

> Patient Rated Wrist Hand Evaluation

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Rated Wrist Hand Evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | At rest |
| Q04 | varchar |  |  | SI | When doing a task with repeated wrist movement |
| Q05 | varchar |  |  | SI | When lifting a heavy object |
| Q06 | varchar |  |  | SI | When it is at its worst |
| Q07 | varchar |  |  | SI | How often do you have pain? |
| Q08 | varchar |  |  | SI | Fasten buttons on my shirt |
| Q09 | varchar |  |  | SI | Cut meat using a knife with my affected hand |
| Q10 | varchar |  |  | SI | Turn a door knob using my affected hand |
| Q11 | varchar |  |  | SI | Use my affected hand to push up from a chair |
| Q12 | varchar |  |  | SI | Carry a 10 lb (5 kg) object in my affected hand |
| Q13 | varchar |  |  | SI | Use bathroom tissue with my affected hand |
| Q14 | varchar |  |  | SI | Personal care activities (dressing, washing) |
| Q15 | varchar |  |  | SI | Household work (cleaning, maintenance) |
| Q16 | varchar |  |  | SI | Work (your job or usual everyday work) |
| Q17 | varchar |  |  | SI | Recreational activities |
| Q18 | varchar |  |  | SI | Pain score |
| Q19 | varchar |  |  | SI | Disability score |
| Q20 | varchar |  |  | SI | Total score |
| Q21 | varchar |  |  | SI | You will be describing your average wrist symptoms... |
| Q22 | varchar |  |  | SI | 0 - 100: Higher scores indicate more pain and func... |
| Q23 | varchar |  |  | SI | The Patient-Rated Wrist and Hand Evaluation (PRWHE... |
| Q24 | varchar |  |  | SI | All responses set to not evaluable |
| Q25 | varchar |  |  | SI | Guidelines |
| Q26 | varchar |  |  | SI | Rate the average amount of pain in your wrist over... |
| Q27 | varchar |  |  | SI | A zero (0) means that you did not have any pain an... |
| Q28 | varchar |  |  | SI | Rate the amount of difficulty you experienced perf... |
| Q29 | varchar |  |  | SI | A zero (0) means that you did not experience any d... |
| Q30 | varchar |  |  | SI | Rate the amount of difficulty you experienced perf... |
| Q31 | varchar |  |  | SI | By “usual activities”, we mean the activities you ... |
| Q32 | varchar |  |  | SI | The questions below will help us understand how mu... |
| Q33 | varchar |  |  | SI | Please provide an answer for ALL questions. |
| Q34 | varchar |  |  | SI | If you did not perform an activity, please ESTIMAT... |
| Q35 | varchar |  |  | SI | If you have never performed the activity, you may ... |
| Q36 | varchar |  |  | SI | A. Specific Activities |
| Q37 | varchar |  |  | SI | B. Usual Activities |
| Q38 | varchar |  |  | SI | A zero (0) means that you did not experience any d... |
| Q39 | varchar |  |  | SI | Appearance - Optional |
| Q40 | varchar |  |  | SI | How important is the appearance of your hand? |
| Q41 | varchar |  |  | SI | Rate how dissatisfied you were with the appearance... |
| Q42 | varchar |  |  | SI | Other comments |
| Q43 | varchar |  |  | SI | MacDermid JC, Turgeon T, Richards RS, Beadle M, Ro... |
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