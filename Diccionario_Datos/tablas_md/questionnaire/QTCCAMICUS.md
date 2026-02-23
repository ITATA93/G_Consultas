# questionnaire.QTCCAMICUS

> Confusion Assessment Method (CAM) for ICU Score

**Schema:** questionnaire
**Columnas:** 162
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Confusion Assessment Method (CAM) for ICU Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Sufficient level of consciousness to undertake ass... |
| Q04 | varchar |  |  | SI | Richmond Agitation-Sedation Scale (RASS) > -3, or ... |
| Q05 | varchar |  |  | SI | Patient is too sedated. Complete CAM-ICU at a late... |
| Q06 | varchar |  |  | SI | Is the patient different than their baseline menta... |
| Q07 | varchar |  |  | SI | Has the patient had any fluctuation in mental stat... |
| Q08 | varchar |  |  | SI | Attention test with >2 errors |
| Q09 | varchar |  |  | SI | Is the patient's actual RASS score is anything oth... |
| Q10 | varchar |  |  | SI | Combined number of errors to questions and command... |
| Q100 | bigint |  |  | SI | https://www.icudelirium.org/medical-professionals/... |
| Q100TxtOnly | bigint |  |  | SI | https://www.icudelirium.org/medical-professionals/... |
| Q101 | varchar |  |  | SI | A patient is considered CAM-ICU positive (i.e. del... |
| Q102 | varchar |  |  | SI | CAM-ICU Positive |
| Q103 | varchar |  |  | SI | • Reassess and manage pain |
| Q104 | varchar |  |  | SI | • Repeat CAM-ICU once per shift |
| Q105 | varchar |  |  | SI | • Proceed with delirium escalation |
| Q106 | varchar |  |  | SI | CAM-ICU Negative |
| Q107 | varchar |  |  | SI | • Continue delirium prevention bundle |
| Q108 | varchar |  |  | SI | • Repeat CAM-ICU once per shift |
| Q109 | varchar |  |  | SI | • Wean sedation as soon as possible |
| Q11 | varchar |  |  | SI | Feature 1 |
| Q110 | varchar |  |  | SI | Feature 1 not required |
| Q111 | varchar |  |  | SI | Feature 2 not required |
| Q112 | varchar |  |  | SI | Feature 2 not required |
| Q113 | varchar |  |  | SI | Feature 3 not required |
| Q114 | varchar |  |  | SI | Feature 3 not required |
| Q115 | varchar |  |  | SI | Feature 3 not required |
| Q116 | varchar |  |  | SI | Feature 4 not required |
| Q117 | varchar |  |  | SI | Feature 4 not required |
| Q118 | varchar |  |  | SI | Feature 4 not required |
| Q119 | varchar |  |  | SI | Feature 4 not required |
| Q12 | varchar |  |  | SI | Fluctuating Course of mental status is evidenced b... |
| Q120 | varchar |  |  | SI | Is the patient's actual RASS score is anything oth... |
| Q13 | varchar |  |  | SI | Feature 2: Letters |
| Q14 | varchar |  |  | SI | Directions: Say to the patient, ''I am going to re... |
| Q15 | varchar |  |  | SI | Read letters from one of the following letter list... |
| Q16 | varchar |  |  | SI | S A V E A H A A R T |
| Q17 | varchar |  |  | SI | C A S A B L A N C A |
| Q18 | varchar |  |  | SI | A B A D B A D A A Y |
| Q19 | varchar |  |  | SI | Errors are counted when patient fails to squeeze o... |
| Q20 | varchar |  |  | SI | Attempt letter assessment first. If the patient is... |
| Q21 | varchar |  |  | SI | If the patient is incapable of performing the Lett... |
| Q22 | varchar |  |  | SI | If both tests are performed, score based on pictur... |
| Q23 | varchar |  |  | SI | Feature 2: Pictures Step 1 |
| Q24 | varchar |  |  | SI | Directions: Say to the patient: ''I am going to sh... |
| Q25 | varchar |  |  | SI | Then show the pictures, naming each item and alter... |
| Q26 | varchar |  |  | SI | Show the first 5 pictures for 3 seconds each. |
| Q27 | varchar |  |  | SI | Step 1 Example Pictures |
| Q28 | varchar |  |  | SI | Feature 2: Pictures Step 2 |
| Q29 | varchar |  |  | SI | Directions: Say to the patient, ''Now I am going t... |
| Q30 | varchar |  |  | SI | Let me know whether or not you saw the picture bef... |
| Q31 | varchar |  |  | SI | Then show 10 pictures (5 new 5 repeat) for 3 secon... |
| Q32 | varchar |  |  | SI | Step 2 Example Pictures |
| Q33 | varchar |  |  | SI | Feature 2: Pictures Scoring |
| Q34 | varchar |  |  | SI | Scoring: Errors are counted with the patient incor... |
| Q35 | varchar |  |  | SI | In order to improve the visibility for elderly pat... |
| Q36 | varchar |  |  | SI | Note: If a patient wears glasses or hearing aids m... |
| Q37 | varchar |  |  | SI | Feature 3 |
| Q38 | varchar |  |  | SI | Feature 3 (Altered Level of Consciousness) evaluat... |
| Q39 | varchar |  |  | SI | The current level of consciousness as detected wit... |
| Q40 | varchar |  |  | SI | This is distinct from Feature 1 (Acute Change or F... |
| Q41 | varchar |  |  | SI | mental status baseline and whether there has been ... |
| Q42 | varchar |  |  | SI | A patient can have an alert/calm baseline, RASS fl... |
| Q43 | varchar |  |  | SI | Feature 1 is present due to fluctuations, but Feat... |
| Q44 | varchar |  |  | SI | Any validated sedation - agitation / level of cons... |
| Q45 | varchar |  |  | SI | The RASS is not the same as other sedation - agita... |
| Q46 | varchar |  |  | SI | For that reason, it is important to determine whic... |
| Q47 | varchar |  |  | SI | Feature 4 |
| Q48 | varchar |  |  | SI | Ask the patient the following yes/no questions and... |
| Q49 | varchar |  |  | SI | 1. Will a stone float on water? |
| Q50 | varchar |  |  | SI | 2. Are there fish in the sea? |
| Q51 | varchar |  |  | SI | 3. Does 1 pound weigh more than 2 pounds? |
| Q52 | varchar |  |  | SI | 4. Can you use a hammer to pound a nail? |
| Q53 | varchar |  |  | SI | Errors are counted when the patient incorrectly an... |
| Q54 | varchar |  |  | SI | Next, ask the patient to follow your commands: |
| Q55 | varchar |  |  | SI | a) ''Hold up this many fingers'' (hold up 2 finger... |
| Q56 | varchar |  |  | SI | b) ''Now do the same thing with the other hand'' (... |
| Q57 | varchar |  |  | SI | If unable to move both arms, for part ''b'' ask pa... |
| Q58 | varchar |  |  | SI | An error is counted if patient is unable to comple... |
| Q59 | varchar |  |  | SI | Score |
| Q60 | varchar |  |  | SI | Classification |
| Q61 | varchar |  |  | SI | 0 |
| Q62 | varchar |  |  | SI | CAM-ICU negative - delirium absent |
| Q63 | varchar |  |  | SI | 1 - 2 |
| Q64 | varchar |  |  | SI | CAM-ICU positive - delirium present |
| Q65 | varchar |  |  | SI | 99 |
| Q66 | varchar |  |  | SI | Patient too sedated to complete CAM-ICU |
| Q67 | varchar |  |  | SI | The Confusion Assessment Method ICU (CAM -ICU) sco... |
| Q68 | varchar |  |  | SI | Feature 1: Acute Onset or Fluctuating Course |
| Q69 | varchar |  |  | SI | Feature 2: Inattention |
| Q70 | varchar |  |  | SI | Feature 3: Altered Level of Consciousness |
| Q71 | varchar |  |  | SI | Feature 4: Disorganized Thinking |
| Q72 | varchar |  |  | SI | CAM-ICU negative - delirium absent |
| Q73 | varchar |  |  | SI | CAM-ICU positive - delirium present |
| Q74 | varchar |  |  | SI | Patient too sedated to complete CAM-ICU |
| Q75 | varchar |  |  | SI | Feature 1 not required |
| Q76 | varchar |  |  | SI | Feature 2 not required |
| Q77 | varchar |  |  | SI | Feature 3 not required |
| Q78 | varchar |  |  | SI | Feature 4 not required |
| Q79 | varchar |  |  | SI | Score based on |
| Q80 | varchar |  |  | SI | Directions: |
| Q81 | varchar |  |  | SI | Say to the patient, “I am going to read you a seri... |
| Q82 | varchar |  |  | SI | Read letters from one of the following letter list... |
| Q83 | varchar |  |  | SI | S A V E A H A A R T |
| Q84 | varchar |  |  | SI | C A S A B L A N C A |
| Q85 | varchar |  |  | SI | A B A D B A D A A Y |
| Q86 | varchar |  |  | SI | If unable to complete test with letters, use pictu... |
| Q87 | varchar |  |  | SI | If both tests performed, score based on pictures. |
| Q88 | varchar |  |  | SI | Directions: |
| Q89 | varchar |  |  | SI | Ask the patient the following yes/no questions and... |
| Q90 | varchar |  |  | SI | 1. Will a stone float on water? |
| Q91 | varchar |  |  | SI | 2. Are there fish in the sea? |
| Q92 | varchar |  |  | SI | 3. Does 1 pound weigh more than 2 pounds? |
| Q93 | varchar |  |  | SI | 4. Can you use a hammer to pound a nail? |
| Q94 | varchar |  |  | SI | Next, ask the patient to follow your commands: |
| Q95 | varchar |  |  | SI | a) “Hold up this many fingers” (hold up 2 fingers) |
| Q96 | varchar |  |  | SI | b) “Now do the same thing with the other hand” (do... |
| Q97 | varchar |  |  | SI | Copyright © 2002, E. Wesley Ely, MD, MPH and Vande... |
| Q98 | varchar |  |  | SI | For instructions on how to score, please open the ... |
| Q99 | varchar |  |  | SI | For details instructions on the CAM-ICU, please ac... |
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