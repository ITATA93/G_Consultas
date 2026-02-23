# SQLUser.IN_Trans

**Schema:** SQLUser
**Columnas:** 181
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INTR_RowId | bigint | PK |  | NO | - |
| INTR_Amount | double |  |  | SI | Amount |
| INTR_AveragePrice | double |  |  | SI | Average Price |
| INTR_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| INTR_CTUOM_DR | bigint |  | FK | SI | Des Ref to CTUOM (Unit of Measurement) |
| INTR_Date | date |  |  | SI | Transaction Date |
| INTR_DrugRegisterNo | varchar |  |  | SI | Drug Register Number |
| INTR_GLBatch_DR | bigint |  | FK | SI | GL Batch |
| INTR_HospAveragePrice | double |  |  | SI | Hospital Average Price |
| INTR_INCI_DR | bigint |  | FK | SI | Des Ref INCI |
| INTR_INCLB_DR | varchar |  | FK | SI | Des Ref to INCLB |
| INTR_No | varchar |  |  | SI | Transaction Number |
| INTR_Pointer | varchar |  |  | SI | Pointer to other table |
| INTR_Qty | double |  |  | SI | Quantity |
| INTR_SSUSR_DR | bigint |  | FK | SI | Des ref to SSUSR |
| INTR_StorageBin_DR | varchar |  | FK | SI | Des Ref CTLocStorageBin |
| INTR_Time | time |  |  | SI | Transaction Time |
| INTR_Type | varchar |  |  | SI | Stock Transaction Type |
| INTR_UpdBalFlag | varchar |  |  | SI | Update Balance Flag |
| INTR_UpdFlag | varchar |  |  | SI | Update Inventory Flag |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Sufficient level of consciousness to undertake ass... |
| Q04 | - |  |  | SI | Richmond Agitation-Sedation Scale (RASS) > -3, or ... |
| Q05 | - |  |  | SI | Patient is too sedated. Complete CAM-ICU at a late... |
| Q06 | - |  |  | SI | Is the patient different than their baseline menta... |
| Q07 | - |  |  | SI | Has the patient had any fluctuation in mental stat... |
| Q08 | - |  |  | SI | Attention test with >2 errors |
| Q09 | - |  |  | SI | Is the patient's actual RASS score is anything oth... |
| Q10 | - |  |  | SI | Combined number of errors to questions and command... |
| Q100 | - |  |  | SI | https://www.icudelirium.org/medical-professionals/... |
| Q100TxtOnly | - |  |  | SI | https://www.icudelirium.org/medical-professionals/... |
| Q101 | - |  |  | SI | A patient is considered CAM-ICU positive (i.e. del... |
| Q102 | - |  |  | SI | CAM-ICU Positive |
| Q103 | - |  |  | SI | • Reassess and manage pain |
| Q104 | - |  |  | SI | • Repeat CAM-ICU once per shift |
| Q105 | - |  |  | SI | • Proceed with delirium escalation |
| Q106 | - |  |  | SI | CAM-ICU Negative |
| Q107 | - |  |  | SI | • Continue delirium prevention bundle |
| Q108 | - |  |  | SI | • Repeat CAM-ICU once per shift |
| Q109 | - |  |  | SI | • Wean sedation as soon as possible |
| Q11 | - |  |  | SI | Feature 1 |
| Q110 | - |  |  | SI | Feature 1 not required |
| Q111 | - |  |  | SI | Feature 2 not required |
| Q112 | - |  |  | SI | Feature 2 not required |
| Q113 | - |  |  | SI | Feature 3 not required |
| Q114 | - |  |  | SI | Feature 3 not required |
| Q115 | - |  |  | SI | Feature 3 not required |
| Q116 | - |  |  | SI | Feature 4 not required |
| Q117 | - |  |  | SI | Feature 4 not required |
| Q118 | - |  |  | SI | Feature 4 not required |
| Q119 | - |  |  | SI | Feature 4 not required |
| Q12 | - |  |  | SI | Fluctuating Course of mental status is evidenced b... |
| Q120 | - |  |  | SI | Is the patient's actual RASS score is anything oth... |
| Q13 | - |  |  | SI | Feature 2: Letters |
| Q14 | - |  |  | SI | Directions: Say to the patient, ''I am going to re... |
| Q15 | - |  |  | SI | Read letters from one of the following letter list... |
| Q16 | - |  |  | SI | S A V E A H A A R T |
| Q17 | - |  |  | SI | C A S A B L A N C A |
| Q18 | - |  |  | SI | A B A D B A D A A Y |
| Q19 | - |  |  | SI | Errors are counted when patient fails to squeeze o... |
| Q20 | - |  |  | SI | Attempt letter assessment first. If the patient is... |
| Q21 | - |  |  | SI | If the patient is incapable of performing the Lett... |
| Q22 | - |  |  | SI | If both tests are performed, score based on pictur... |
| Q23 | - |  |  | SI | Feature 2: Pictures Step 1 |
| Q24 | - |  |  | SI | Directions: Say to the patient: ''I am going to sh... |
| Q25 | - |  |  | SI | Then show the pictures, naming each item and alter... |
| Q26 | - |  |  | SI | Show the first 5 pictures for 3 seconds each. |
| Q27 | - |  |  | SI | Step 1 Example Pictures |
| Q28 | - |  |  | SI | Feature 2: Pictures Step 2 |
| Q29 | - |  |  | SI | Directions: Say to the patient, ''Now I am going t... |
| Q30 | - |  |  | SI | Let me know whether or not you saw the picture bef... |
| Q31 | - |  |  | SI | Then show 10 pictures (5 new 5 repeat) for 3 secon... |
| Q32 | - |  |  | SI | Step 2 Example Pictures |
| Q33 | - |  |  | SI | Feature 2: Pictures Scoring |
| Q34 | - |  |  | SI | Scoring: Errors are counted with the patient incor... |
| Q35 | - |  |  | SI | In order to improve the visibility for elderly pat... |
| Q36 | - |  |  | SI | Note: If a patient wears glasses or hearing aids m... |
| Q37 | - |  |  | SI | Feature 3 |
| Q38 | - |  |  | SI | Feature 3 (Altered Level of Consciousness) evaluat... |
| Q39 | - |  |  | SI | The current level of consciousness as detected wit... |
| Q40 | - |  |  | SI | This is distinct from Feature 1 (Acute Change or F... |
| Q41 | - |  |  | SI | mental status baseline and whether there has been ... |
| Q42 | - |  |  | SI | A patient can have an alert/calm baseline, RASS fl... |
| Q43 | - |  |  | SI | Feature 1 is present due to fluctuations, but Feat... |
| Q44 | - |  |  | SI | Any validated sedation - agitation / level of cons... |
| Q45 | - |  |  | SI | The RASS is not the same as other sedation - agita... |
| Q46 | - |  |  | SI | For that reason, it is important to determine whic... |
| Q47 | - |  |  | SI | Feature 4 |
| Q48 | - |  |  | SI | Ask the patient the following yes/no questions and... |
| Q49 | - |  |  | SI | 1. Will a stone float on water? |
| Q50 | - |  |  | SI | 2. Are there fish in the sea? |
| Q51 | - |  |  | SI | 3. Does 1 pound weigh more than 2 pounds? |
| Q52 | - |  |  | SI | 4. Can you use a hammer to pound a nail? |
| Q53 | - |  |  | SI | Errors are counted when the patient incorrectly an... |
| Q54 | - |  |  | SI | Next, ask the patient to follow your commands: |
| Q55 | - |  |  | SI | a) ''Hold up this many fingers'' (hold up 2 finger... |
| Q56 | - |  |  | SI | b) ''Now do the same thing with the other hand'' (... |
| Q57 | - |  |  | SI | If unable to move both arms, for part ''b'' ask pa... |
| Q58 | - |  |  | SI | An error is counted if patient is unable to comple... |
| Q59 | - |  |  | SI | Score |
| Q60 | - |  |  | SI | Classification |
| Q61 | - |  |  | SI | 0 |
| Q62 | - |  |  | SI | CAM-ICU negative - delirium absent |
| Q63 | - |  |  | SI | 1 - 2 |
| Q64 | - |  |  | SI | CAM-ICU positive - delirium present |
| Q65 | - |  |  | SI | 99 |
| Q66 | - |  |  | SI | Patient too sedated to complete CAM-ICU |
| Q67 | - |  |  | SI | The Confusion Assessment Method ICU (CAM -ICU) sco... |
| Q68 | - |  |  | SI | Feature 1: Acute Onset or Fluctuating Course |
| Q69 | - |  |  | SI | Feature 2: Inattention |
| Q70 | - |  |  | SI | Feature 3: Altered Level of Consciousness |
| Q71 | - |  |  | SI | Feature 4: Disorganized Thinking |
| Q72 | - |  |  | SI | CAM-ICU negative - delirium absent |
| Q73 | - |  |  | SI | CAM-ICU positive - delirium present |
| Q74 | - |  |  | SI | Patient too sedated to complete CAM-ICU |
| Q75 | - |  |  | SI | Feature 1 not required |
| Q76 | - |  |  | SI | Feature 2 not required |
| Q77 | - |  |  | SI | Feature 3 not required |
| Q78 | - |  |  | SI | Feature 4 not required |
| Q79 | - |  |  | SI | Score based on |
| Q80 | - |  |  | SI | Directions: |
| Q81 | - |  |  | SI | Say to the patient, “I am going to read you a seri... |
| Q82 | - |  |  | SI | Read letters from one of the following letter list... |
| Q83 | - |  |  | SI | S A V E A H A A R T |
| Q84 | - |  |  | SI | C A S A B L A N C A |
| Q85 | - |  |  | SI | A B A D B A D A A Y |
| Q86 | - |  |  | SI | If unable to complete test with letters, use pictu... |
| Q87 | - |  |  | SI | If both tests performed, score based on pictures. |
| Q88 | - |  |  | SI | Directions: |
| Q89 | - |  |  | SI | Ask the patient the following yes/no questions and... |
| Q90 | - |  |  | SI | 1. Will a stone float on water? |
| Q91 | - |  |  | SI | 2. Are there fish in the sea? |
| Q92 | - |  |  | SI | 3. Does 1 pound weigh more than 2 pounds? |
| Q93 | - |  |  | SI | 4. Can you use a hammer to pound a nail? |
| Q94 | - |  |  | SI | Next, ask the patient to follow your commands: |
| Q95 | - |  |  | SI | a) “Hold up this many fingers” (hold up 2 fingers) |
| Q96 | - |  |  | SI | b) “Now do the same thing with the other hand” (do... |
| Q97 | - |  |  | SI | Copyright © 2002, E. Wesley Ely, MD, MPH and Vande... |
| Q98 | - |  |  | SI | For instructions on how to score, please open the ... |
| Q99 | - |  |  | SI | For details instructions on the CAM-ICU, please ac... |
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