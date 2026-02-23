# questionnaire.QTCSLUMS

> Saint Louis University Mental Status Examination (SLUMS)

**Schema:** questionnaire
**Columnas:** 115
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Saint Louis University Mental Status Examination (SLUMS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of examination |
| Q02 | time |  |  | SI | Time of examination |
| Q03 | varchar |  |  | SI | Patient's level of alertness |
| Q04 | varchar |  |  | SI | Level of education |
| Q05 | varchar |  |  | SI | 1. Does the patient know the correct day of the we... |
| Q06 | varchar |  |  | SI | 2. Does the patient know what the correct year is? |
| Q07 | varchar |  |  | SI | 3. Does the patient know what city / town / countr... |
| Q08 | varchar |  |  | SI | 4. Please remember these five objects. I will ask ... |
| Q09 | varchar |  |  | SI | Apple. Pen. Tie. House. Car |
| Q10 | varchar |  |  | SI | 5. You have $100 and you go to the store and buy a... |
| Q11 | varchar |  |  | SI | Does the patient know the correct answer to the qu... |
| Q12 | varchar |  |  | SI | Does the patient know the correct answer to the qu... |
| Q13 | varchar |  |  | SI | 6. Please name as many animals as you can in one m... |
| Q14 | varchar |  |  | SI | 7. How many objects from Question #4 does the pati... |
| Q15 | varchar |  |  | SI | 8. I am going to give you a series of numbers and ... |
| Q16 | varchar |  |  | SI | Does the patient know the backward number for '87'... |
| Q17 | varchar |  |  | SI | Does the patient know the backward number for '648... |
| Q18 | varchar |  |  | SI | Does the patient know the backward number for '853... |
| Q19 | varchar |  |  | SI | Please provide image to patient and document accor... |
| Q20 | varchar |  |  | SI | 9. This is a clock face image - Please put in the ... |
| Q21 | varchar |  |  | SI | Does the patient put the hours marker okay? |
| Q22 | varchar |  |  | SI | Does the patient put the time correct? |
| Q23 | varchar |  |  | SI | 10. Object image - Does the patient put an 'X' in ... |
| Q24 | varchar |  |  | SI | Object image - Does the patient know which of the ... |
| Q25 | varchar |  |  | SI | 11. I am going to tell you a story. Please listen ... |
| Q26 | varchar |  |  | SI | Jill was a very successful stockbroker. She made a... |
| Q27 | varchar |  |  | SI | She married him and had three children. They lived... |
| Q28 | varchar |  |  | SI | Does the patient know what the female's name was? |
| Q29 | varchar |  |  | SI | Does the patient know what work did she do? |
| Q30 | varchar |  |  | SI | Does the patient know when did she go back to work... |
| Q31 | varchar |  |  | SI | Does the patient know what state did she live in? |
| Q32 | varchar |  |  | SI | SLUMS form is used to screen individuals to look f... |
| Q33 | varchar |  |  | SI | Begin by asking the patient the following: “Do you... |
| Q34 | varchar |  |  | SI | is by asking you some questions.” You may need to ... |
| Q35 | varchar |  |  | SI | What this tool does is check the amount of memory ... |
| Q36 | varchar |  |  | SI | Read the questions aloud clearly and slowly to the... |
| Q37 | varchar |  |  | SI | Score the questions as indicated on the examinatio... |
| Q38 | varchar |  |  | SI | a. On question No. 4, read the statement as listed... |
| Q39 | varchar |  |  | SI | that the patient heard and understood what you sai... |
| Q40 | varchar |  |  | SI | b. On question  No. 5, make sure the patient is fo... |
| Q41 | varchar |  |  | SI | you have left?”).  Do not prompt or give hints, bu... |
| Q42 | varchar |  |  | SI | c. Redirect the patient’s attention if necessary b... |
| Q43 | varchar |  |  | SI | d. On question No. 8, state each number by its ind... |
| Q44 | varchar |  |  | SI | On question No. 9, either draw a large circle on t... |
| Q45 | varchar |  |  | SI | When scoring, give full credit for either all 12 n... |
| Q46 | varchar |  |  | SI | for full credit. When scoring the correct time, ma... |
| Q47 | varchar |  |  | SI | You may also provide a separate sheet with larger ... |
| Q48 | varchar |  |  | SI | be created by enlarging the figures on the examina... |
| Q49 | varchar |  |  | SI | Read question No. 11 as written, and provide ample... |
| Q50 | varchar |  |  | SI | read it to them. Do not prompt or give hints. The ... |
| Q51 | varchar |  |  | SI | Score |
| Q52 | varchar |  |  | SI | Classification |
| Q53 | varchar |  |  | SI | The answer of Chicago as the state she lives in ge... |
| Q54 | varchar |  |  | SI | High school education |
| Q55 | varchar |  |  | SI | 27 - 30 |
| Q56 | varchar |  |  | SI | 21 - 26 |
| Q57 | varchar |  |  | SI | 1 - 20 |
| Q58 | varchar |  |  | SI | Less than high school education |
| Q59 | varchar |  |  | SI | 25 - 30 |
| Q60 | varchar |  |  | SI | 20 - 24 |
| Q61 | varchar |  |  | SI | 1 - 19 |
| Q62 | varchar |  |  | SI | The Saint Louis University Mental Status exam is a... |
| Q63 | varchar |  |  | SI | . |
| Q64 | varchar |  |  | SI |      • |
| Q65 | varchar |  |  | SI | For example, if I say 42, you would say 24. |
| Q66 | varchar |  |  | SI | When they were teenagers, she went back to work. S... |
| Q67 | varchar |  |  | SI | The purpose of the form is to screen individuals t... |
| Q68 | varchar |  |  | SI |  :  |
| Q69 | varchar |  |  | SI | Normal |
| Q70 | varchar |  |  | SI | Mild Neurocognitive Disorder |
| Q71 | varchar |  |  | SI | Dementia |
| Q72 | varchar |  |  | SI | Normal |
| Q73 | varchar |  |  | SI | Mild Neurocognitive Disorder |
| Q74 | varchar |  |  | SI | Dementia |
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