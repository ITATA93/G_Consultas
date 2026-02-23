# questionnaire.QTCFIQ

> FIQ

**Schema:** questionnaire
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(FIQ)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | For the past week were you able to: |
| Q02 | varchar |  |  | SI | Do shopping? |
| Q03 | varchar |  |  | SI | Do laundry with washer and dryer? |
| Q04 | varchar |  |  | SI | Prepare meals? |
| Q05 | varchar |  |  | SI | Wash dishes / cooking utensils by hand? |
| Q06 | varchar |  |  | SI | Vacuum a rug? |
| Q07 | varchar |  |  | SI | Make beds? |
| Q08 | varchar |  |  | SI | Walk several blocks? |
| Q09 | varchar |  |  | SI | Visit friends or relatives? |
| Q10 | varchar |  |  | SI | Do yard work? |
| Q11 | varchar |  |  | SI | Drive a car? |
| Q12 | varchar |  |  | SI | Climb stairs? |
| Q13 | varchar |  |  | SI | Of the 7 days in the past week, how many days did ... |
| Q14 | varchar |  |  | SI | How many days last week did you miss work, includi... |
| Q15 | varchar |  |  | SI | When you worked, how much did pain or other sympto... |
| Q16 | varchar |  |  | SI | No problem with work |
| Q17 | varchar |  |  | SI | Great difficulty with work |
| Q18 | varchar |  |  | SI | How bad has your pain been? |
| Q19 | varchar |  |  | SI | No pain |
| Q20 | varchar |  |  | SI | Very severe pain |
| Q21 | varchar |  |  | SI | How tired have you been? |
| Q22 | varchar |  |  | SI | No tiredness |
| Q23 | varchar |  |  | SI | Very tired |
| Q24 | varchar |  |  | SI | How have you felt when you get up in the morning? |
| Q25 | varchar |  |  | SI | Awoke well rested |
| Q26 | varchar |  |  | SI | Awoke very tired |
| Q27 | varchar |  |  | SI | How bad has your stiffness been? |
| Q28 | varchar |  |  | SI | No stiffness |
| Q29 | varchar |  |  | SI | Very stiff |
| Q30 | varchar |  |  | SI | How nervous or anxious have you felt? |
| Q31 | varchar |  |  | SI | Not anxious |
| Q32 | varchar |  |  | SI | Very anxious |
| Q33 | varchar |  |  | SI | How depressed or blue have you felt? |
| Q34 | varchar |  |  | SI | Not depressed |
| Q35 | varchar |  |  | SI | Very depressed |
| Q36 | varchar |  |  | SI | FIQ Score |
| Q37 | varchar |  |  | SI | 100 - Severe impact of the syndrome on the person ... |
| Q38 | varchar |  |  | SI | The higher the FIQ score the greater is the impact... |
| Q39 | varchar |  |  | SI | The FIQ (Fibromyalgia Impact Questionnaire) is an ... |
| Q40 | varchar |  |  | SI | Content |
| Q41 | varchar |  |  | SI | The FIQ is composed of 10 items. The first item co... |
| Q42 | varchar |  |  | SI | Items 2 and 3 ask the patient to mark the number o... |
| Q43 | varchar |  |  | SI | Items 4 through 10 are horizontal linear scales ma... |
| Q44 | varchar |  |  | SI | Administration |
| Q45 | varchar |  |  | SI | The FIQ is a self administered instrument that tak... |
| Q46 | varchar |  |  | SI | Scoring |
| Q47 | varchar |  |  | SI | The FIQ is scored in such a way that a higher scor... |
| Q48 | varchar |  |  | SI | Thus the maximum possible score is 100. The averag... |
| Q49 | varchar |  |  | SI | The questionnaire is scored in the following manne... |
| Q50 | varchar |  |  | SI | 1. The first item consists of 11 questions that ma... |
| Q51 | varchar |  |  | SI | Raw scores on each item can range from 0 (always) ... |
| Q52 | varchar |  |  | SI | Because some patients may not do some of the tasks... |
| Q53 | varchar |  |  | SI | In order to obtain a valid summed score for questi... |
| Q54 | varchar |  |  | SI | Finally, the result is normalized to a 0 - 10 scal... |
| Q55 | varchar |  |  | SI | 2. Item 2 is scored inversely - so that a higher n... |
| Q56 | varchar |  |  | SI | 3. Item 3 is scored directly (i.e. 7=7 and 0=0). T... |
| Q57 | varchar |  |  | SI | 4. Items 4 through 10 are scored in 10 increments.... |
| Q58 | date |  |  | SI | Date |
| Q59 | time |  |  | SI | Time |
| Q60 | varchar |  |  | SI | How bad has your pain been? |
| Q61 | varchar |  |  | SI | How tired have you been? |
| Q62 | varchar |  |  | SI | How have you felt when you get up in the morning? |
| Q63 | varchar |  |  | SI | How bad has your stiffness been? |
| Q64 | varchar |  |  | SI | How nervous or anxious have you felt? |
| Q65 | varchar |  |  | SI | How depressed or blue have you felt? |
| Q66 | varchar |  |  | SI | When you worked, how much did pain or other sympto... |
| Q67 | varchar |  |  | SI | How to answer |
| Q68 | varchar |  |  | SI | 0: No problem with work |
| Q69 | varchar |  |  | SI | 10: Great difficulty with work |
| Q70 | varchar |  |  | SI | 0: No pain |
| Q71 | varchar |  |  | SI | 10: Very severe pain |
| Q72 | varchar |  |  | SI | 0: No tiredness |
| Q73 | varchar |  |  | SI | 10: Very tired |
| Q74 | varchar |  |  | SI | 0: Awoke well rested |
| Q75 | varchar |  |  | SI | 10: Awoke very tired |
| Q76 | varchar |  |  | SI | 0: No stiffness |
| Q77 | varchar |  |  | SI | 10: Very stiff |
| Q78 | varchar |  |  | SI | 0: Not anxious |
| Q79 | varchar |  |  | SI | 10: Very anxious |
| Q80 | varchar |  |  | SI | 0: Not depressed |
| Q81 | varchar |  |  | SI | 10: Very depressed |
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