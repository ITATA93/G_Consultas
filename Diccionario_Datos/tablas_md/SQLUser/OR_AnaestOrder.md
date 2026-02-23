# SQLUser.OR_AnaestOrder

**Schema:** SQLUser
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAORD_ParRef | varchar | PK |  | NO | Parent Reference |
| ANAORD_Childsub | double |  |  | NO | Childsub |
| ANAORD_OEORI_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| ANAORD_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | For the past week were you able to: |
| Q02 | - |  |  | SI | Do shopping? |
| Q03 | - |  |  | SI | Do laundry with washer and dryer? |
| Q04 | - |  |  | SI | Prepare meals? |
| Q05 | - |  |  | SI | Wash dishes / cooking utensils by hand? |
| Q06 | - |  |  | SI | Vacuum a rug? |
| Q07 | - |  |  | SI | Make beds? |
| Q08 | - |  |  | SI | Walk several blocks? |
| Q09 | - |  |  | SI | Visit friends or relatives? |
| Q10 | - |  |  | SI | Do yard work? |
| Q11 | - |  |  | SI | Drive a car? |
| Q12 | - |  |  | SI | Climb stairs? |
| Q13 | - |  |  | SI | Of the 7 days in the past week, how many days did ... |
| Q14 | - |  |  | SI | How many days last week did you miss work, includi... |
| Q15 | - |  |  | SI | When you worked, how much did pain or other sympto... |
| Q16 | - |  |  | SI | No problem with work |
| Q17 | - |  |  | SI | Great difficulty with work |
| Q18 | - |  |  | SI | How bad has your pain been? |
| Q19 | - |  |  | SI | No pain |
| Q20 | - |  |  | SI | Very severe pain |
| Q21 | - |  |  | SI | How tired have you been? |
| Q22 | - |  |  | SI | No tiredness |
| Q23 | - |  |  | SI | Very tired |
| Q24 | - |  |  | SI | How have you felt when you get up in the morning? |
| Q25 | - |  |  | SI | Awoke well rested |
| Q26 | - |  |  | SI | Awoke very tired |
| Q27 | - |  |  | SI | How bad has your stiffness been? |
| Q28 | - |  |  | SI | No stiffness |
| Q29 | - |  |  | SI | Very stiff |
| Q30 | - |  |  | SI | How nervous or anxious have you felt? |
| Q31 | - |  |  | SI | Not anxious |
| Q32 | - |  |  | SI | Very anxious |
| Q33 | - |  |  | SI | How depressed or blue have you felt? |
| Q34 | - |  |  | SI | Not depressed |
| Q35 | - |  |  | SI | Very depressed |
| Q36 | - |  |  | SI | FIQ Score |
| Q37 | - |  |  | SI | 100 - Severe impact of the syndrome on the person ... |
| Q38 | - |  |  | SI | The higher the FIQ score the greater is the impact... |
| Q39 | - |  |  | SI | The FIQ (Fibromyalgia Impact Questionnaire) is an ... |
| Q40 | - |  |  | SI | Content |
| Q41 | - |  |  | SI | The FIQ is composed of 10 items. The first item co... |
| Q42 | - |  |  | SI | Items 2 and 3 ask the patient to mark the number o... |
| Q43 | - |  |  | SI | Items 4 through 10 are horizontal linear scales ma... |
| Q44 | - |  |  | SI | Administration |
| Q45 | - |  |  | SI | The FIQ is a self administered instrument that tak... |
| Q46 | - |  |  | SI | Scoring |
| Q47 | - |  |  | SI | The FIQ is scored in such a way that a higher scor... |
| Q48 | - |  |  | SI | Thus the maximum possible score is 100. The averag... |
| Q49 | - |  |  | SI | The questionnaire is scored in the following manne... |
| Q50 | - |  |  | SI | 1. The first item consists of 11 questions that ma... |
| Q51 | - |  |  | SI | Raw scores on each item can range from 0 (always) ... |
| Q52 | - |  |  | SI | Because some patients may not do some of the tasks... |
| Q53 | - |  |  | SI | In order to obtain a valid summed score for questi... |
| Q54 | - |  |  | SI | Finally, the result is normalized to a 0 - 10 scal... |
| Q55 | - |  |  | SI | 2. Item 2 is scored inversely - so that a higher n... |
| Q56 | - |  |  | SI | 3. Item 3 is scored directly (i.e. 7=7 and 0=0). T... |
| Q57 | - |  |  | SI | 4. Items 4 through 10 are scored in 10 increments.... |
| Q58 | - |  |  | SI | Date |
| Q59 | - |  |  | SI | Time |
| Q60 | - |  |  | SI | How bad has your pain been? |
| Q61 | - |  |  | SI | How tired have you been? |
| Q62 | - |  |  | SI | How have you felt when you get up in the morning? |
| Q63 | - |  |  | SI | How bad has your stiffness been? |
| Q64 | - |  |  | SI | How nervous or anxious have you felt? |
| Q65 | - |  |  | SI | How depressed or blue have you felt? |
| Q66 | - |  |  | SI | When you worked, how much did pain or other sympto... |
| Q67 | - |  |  | SI | How to answer |
| Q68 | - |  |  | SI | 0: No problem with work |
| Q69 | - |  |  | SI | 10: Great difficulty with work |
| Q70 | - |  |  | SI | 0: No pain |
| Q71 | - |  |  | SI | 10: Very severe pain |
| Q72 | - |  |  | SI | 0: No tiredness |
| Q73 | - |  |  | SI | 10: Very tired |
| Q74 | - |  |  | SI | 0: Awoke well rested |
| Q75 | - |  |  | SI | 10: Awoke very tired |
| Q76 | - |  |  | SI | 0: No stiffness |
| Q77 | - |  |  | SI | 10: Very stiff |
| Q78 | - |  |  | SI | 0: Not anxious |
| Q79 | - |  |  | SI | 10: Very anxious |
| Q80 | - |  |  | SI | 0: Not depressed |
| Q81 | - |  |  | SI | 10: Very depressed |
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