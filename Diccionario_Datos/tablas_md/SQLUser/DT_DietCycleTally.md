# SQLUser.DT_DietCycleTally

**Schema:** SQLUser
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Dieta**. Gestión de alimentación de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TALLY_RowId | bigint | PK |  | NO | - |
| ChildQ120DR | - |  |  | SI | Child Reference: Exercise Test Scale |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Summary of Cardiac Condition |
| Q04 | - |  |  | SI | Pre Existing Injuries Impacting on Exercise Progra... |
| Q05 | - |  |  | SI | Current Exercise |
| Q06 | - |  |  | SI | Occupation / Recreation / Leisure |
| Q07 | - |  |  | SI | Physical Activities / ADL´s |
| Q08 | - |  |  | SI | Goals for Physical Activity / Exercise |
| Q09 | - |  |  | SI | Exercise Plan for Discharge |
| Q10 | - |  |  | SI | Physical Assessment |
| Q100 | - |  |  | SI | Diastolic |
| Q100ObsDR | - |  |  | SI | Diastolic DR |
| Q101 | - |  |  | SI | Pulse |
| Q101ObsDR | - |  |  | SI | Pulse DR |
| Q102 | - |  |  | SI | Rating of Perceived Exertion |
| Q102ObsDR | - |  |  | SI | Rating of Perceived Exertion DR |
| Q103 | - |  |  | SI | Immediately Post Test |
| Q104 | - |  |  | SI | Respirations |
| Q104ObsDR | - |  |  | SI | Respirations DR |
| Q105 | - |  |  | SI | Rating of Perceived Exertion |
| Q105ObsDR | - |  |  | SI | Rating of Perceived Exertion DR |
| Q106 | - |  |  | SI | Auscultation |
| Q108 | - |  |  | SI | Further Monitoring |
| Q109 | - |  |  | SI | (where necessary) |
| Q110 | - |  |  | SI | 2 Minutes Post Test |
| Q111 | - |  |  | SI | Systolic |
| Q111ObsDR | - |  |  | SI | Systolic DR |
| Q112 | - |  |  | SI | Diastolic |
| Q112ObsDR | - |  |  | SI | Diastolic DR |
| Q113 | - |  |  | SI | Pulse |
| Q113ObsDR | - |  |  | SI | Pulse DR |
| Q114 | - |  |  | SI | Further Monitoring |
| Q115 | - |  |  | SI | (where necessary) |
| Q116 | - |  |  | SI | Reasons for Stopping the Test |
| Q117 | - |  |  | SI | Reason for stopping the Test |
| Q118 | - |  |  | SI | Other Comments |
| Q119 | - |  |  | SI | Bodymap |
| Q121 | - |  |  | SI | Burdon's Modified Borg Scale |
| Q121ObsDR | - |  |  | SI | Burdon's Modified Borg Scale DR |
| Q122 | - |  |  | SI | Burdon's Modified Borg Scale |
| Q122ObsDR | - |  |  | SI | Burdon's Modified Borg Scale DR |
| Q68 | - |  |  | SI | Baseline Values |
| Q69 | - |  |  | SI | Observation |
| Q70 | - |  |  | SI | Pulse |
| Q70ObsDR | - |  |  | SI | Pulse DR |
| Q71 | - |  |  | SI | Systolic |
| Q71ObsDR | - |  |  | SI | Systolic DR |
| Q72 | - |  |  | SI | Diastolic |
| Q72ObsDR | - |  |  | SI | Diastolic DR |
| Q73 | - |  |  | SI | Chest |
| Q74 | - |  |  | SI | Respirations |
| Q74ObsDR | - |  |  | SI | Respirations DR |
| Q75 | - |  |  | SI | Oxygen Saturation |
| Q75ObsDR | - |  |  | SI | Oxygen Saturation DR |
| Q76 | - |  |  | SI | Auscultation |
| Q77 | - |  |  | SI | Weight |
| Q77ObsDR | - |  |  | SI | Weight DR |
| Q78 | - |  |  | SI | Height |
| Q78ObsDR | - |  |  | SI | Height DR |
| Q79 | - |  |  | SI | Waist Circumference |
| Q79ObsDR | - |  |  | SI | Waist Circumference DR |
| Q80 | - |  |  | SI | Posture |
| Q81 | - |  |  | SI | Unloaded Range of Motion / Strength |
| Q82 | - |  |  | SI | (as required) |
| Q83 | - |  |  | SI | Angina / Cardiac Symptoms |
| Q84 | - |  |  | SI | Comment |
| Q85 | - |  |  | SI | Discussed Borg Scale |
| Q86 | - |  |  | SI | Comment |
| Q87 | - |  |  | SI | Exercise Test |
| Q88 | - |  |  | SI | Target HR Reserve |
| Q90 | - |  |  | SI | (Refer to Initial HR Range Guidelines) |
| Q91 | - |  |  | SI | B-Blocker |
| Q92 | - |  |  | SI | 50% |
| Q93 | - |  |  | SI | 60% |
| Q94 | - |  |  | SI | 70% |
| Q95 | - |  |  | SI | 75% |
| Q97 | - |  |  | SI | Score |
| Q98 | - |  |  | SI | Systolic |
| Q98ObsDR | - |  |  | SI | Systolic DR |
| Q99 | - |  |  | SI | (% of HR maximum) |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| TALLY_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| TALLY_Date | date |  |  | SI | Date |
| TALLY_DietCycle_DR | bigint |  | FK | SI | Des Ref DTC DietCycle |
| TALLY_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| TALLY_Tally | double |  |  | SI | Tally |
| TALLY_Time | time |  |  | SI | Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*