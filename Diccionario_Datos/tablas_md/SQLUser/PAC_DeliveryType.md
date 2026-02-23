# SQLUser.PAC_DeliveryType

**Schema:** SQLUser
**Columnas:** 154
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DELT_RowId | bigint | PK |  | NO | - |
| DELT_Code | varchar |  |  | NO | Code |
| DELT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DELT_CreatedDate | date |  |  | SI | Created Date |
| DELT_CreatedTime | time |  |  | SI | Created Time |
| DELT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DELT_DateFrom | date |  |  | SI | Date From |
| DELT_DateTo | date |  |  | SI | Date To |
| DELT_Desc | varchar |  |  | NO | Description |
| DELT_Owner | varchar |  |  | SI | Owner |
| DELT_UpdatedDate | date |  |  | SI | Updated Date |
| DELT_UpdatedTime | time |  |  | SI | Updated Time |
| DELT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Side of symptomatic knee |
| Q04 | - |  |  | SI | If both knees have been operated on, please use a ... |
| Q05 | - |  |  | SI | Ethnicity |
| Q06 | - |  |  | SI | Please indicate the date and surgeon for your knee... |
| Q07 | - |  |  | SI | Date of operation |
| Q08 | - |  |  | SI | Surgeon |
| Q09 | - |  |  | SI | Was this a primary or revision knee replacement |
| Q10 | - |  |  | SI | Charnley functional classification |
| Q100 | - |  |  | SI | Patient Expectations Interpretation |
| Q101 | - |  |  | SI | Functional Score Interpretation |
| Q11 | - |  |  | SI | Alignment |
| Q12 | - |  |  | SI | Alignment: measured on anteroposterior (AP) standi... |
| Q13 | - |  |  | SI | Instability |
| Q14 | - |  |  | SI | Medial / Lateral instability: measured in full ext... |
| Q15 | - |  |  | SI | Anterior / Posterior instability: measured at 90 d... |
| Q16 | - |  |  | SI | Joint Motion |
| Q17 | - |  |  | SI | Range of motion (1 point for each 5 degrees) |
| Q18 | - |  |  | SI | Deductions |
| Q19 | - |  |  | SI | Flexion contracture (minus points) |
| Q20 | - |  |  | SI | Extensor lag (minus points) |
| Q21 | - |  |  | SI | Symptoms |
| Q22 | - |  |  | SI | Pain with level walking (0: none, 10: severe) |
| Q23 | - |  |  | SI | Pain with stairs or inclines (0: none, 10: severe) |
| Q24 | - |  |  | SI | Does this knee feel normal to you? |
| Q25 | - |  |  | SI | Currently, how satisfied are you with the pain lev... |
| Q26 | - |  |  | SI | Currently, how satisfied are you with the pain lev... |
| Q27 | - |  |  | SI | Currently, how satisfied are you with your knee fu... |
| Q28 | - |  |  | SI | Currently, how satisfied are you with your knee fu... |
| Q29 | - |  |  | SI | Currently, how satisfied are you with your knee fu... |
| Q30 | - |  |  | SI | Compared to what you expected before your knee rep... |
| Q31 | - |  |  | SI | My expectations for pain relief were |
| Q32 | - |  |  | SI | My expectations for being able to do my normal act... |
| Q33 | - |  |  | SI | My expectations for being able to do my leisure, r... |
| Q34 | - |  |  | SI | Walking and standing |
| Q35 | - |  |  | SI | Can you walk without any aids (such as a cane, cru... |
| Q36 | - |  |  | SI | Which of the following aid(s) do you use? |
| Q37 | - |  |  | SI | Other aid(s) |
| Q38 | - |  |  | SI | Aid(s) Score - please assign up to -10 points for ... |
| Q39 | - |  |  | SI | Do you use these aid(s) because of your knees? |
| Q40 | - |  |  | SI | For how long can you stand (with or without aid) b... |
| Q41 | - |  |  | SI | For how long can you walk (with or without aid) be... |
| Q42 | - |  |  | SI | Standard activities |
| Q43 | - |  |  | SI | How much does your knee bother you during each of ... |
| Q44 | - |  |  | SI | Walking on an uneven surface |
| Q45 | - |  |  | SI | Turning or pivoting on your leg |
| Q46 | - |  |  | SI | Climbing up or down a flight of stairs |
| Q47 | - |  |  | SI | Getting up from a low couch or a chair without arm... |
| Q48 | - |  |  | SI | Getting into or out of a car |
| Q49 | - |  |  | SI | Moving laterally (stepping to the side) |
| Q50 | - |  |  | SI | Advanced activities |
| Q51 | - |  |  | SI | Climbing a ladder or step stool |
| Q52 | - |  |  | SI | Carrying a shopping bag for a block |
| Q53 | - |  |  | SI | Squatting |
| Q54 | - |  |  | SI | Kneeling |
| Q55 | - |  |  | SI | Running |
| Q56 | - |  |  | SI | Discretionary knee activities |
| Q57 | - |  |  | SI | Please select the activities that you consider mos... |
| Q58 | - |  |  | SI | Activity 1 |
| Q59 | - |  |  | SI | How much does your knee bother you during the acti... |
| Q60 | - |  |  | SI | Activity 2 |
| Q61 | - |  |  | SI | How much does your knee bother you during the acti... |
| Q62 | - |  |  | SI | Activity 3 |
| Q63 | - |  |  | SI | How much does your knee bother you during the acti... |
| Q64 | - |  |  | SI | Objective Knee Score |
| Q65 | - |  |  | SI | Higher scores indicate better knee conditions |
| Q66 | - |  |  | SI | Patient Satisfaction |
| Q67 | - |  |  | SI | 0 - 40: Higher scores indicate a greater satisfact... |
| Q68 | - |  |  | SI | Patient Expectations |
| Q69 | - |  |  | SI | 3 - 15: Higher scores indicate a better match betw... |
| Q70 | - |  |  | SI | Functional Score |
| Q71 | - |  |  | SI | -10 - 100: Higher scores indicate better outcome |
| Q72 | - |  |  | SI | © by The Knee Society. All rights reserved. Reprod... |
| Q73 | - |  |  | SI | For additional information please use |
| Q74 | - |  |  | SI | http://kneesociety.org/the-knee-society-score/ |
| Q75 | - |  |  | SI | Score |
| Q76 | - |  |  | SI | Classification |
| Q77 | - |  |  | SI | Objective Knee Score |
| Q78 | - |  |  | SI | - |
| Q79 | - |  |  | SI | Higher scores indicate better knee conditions |
| Q80 | - |  |  | SI | Patient Satisfaction |
| Q81 | - |  |  | SI | 0 - 40 |
| Q82 | - |  |  | SI | Higher scores indicate a greater satisfaction |
| Q83 | - |  |  | SI | Patient Expectations |
| Q84 | - |  |  | SI | 3 - 15 |
| Q85 | - |  |  | SI | Higher scores indicate a better match between expe... |
| Q86 | - |  |  | SI | Functional Score |
| Q87 | - |  |  | SI | -10 - 100 |
| Q88 | - |  |  | SI | Higher scores indicate better outcome |
| Q89 | - |  |  | SI | The Knee Society Score was designed to provide a s... |
| Q90 | - |  |  | SI | Score |
| Q91 | - |  |  | SI | Classification |
| Q92 | - |  |  | SI | Score |
| Q93 | - |  |  | SI | Classification |
| Q94 | - |  |  | SI | Score |
| Q95 | - |  |  | SI | Classification |
| Q96 | - |  |  | SI | Score |
| Q97 | - |  |  | SI | Classification |
| Q98 | - |  |  | SI | Objective Knee Score Interpretation |
| Q99 | - |  |  | SI | Patient Satisfaction Interpretation |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*