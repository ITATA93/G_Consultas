# SQLUser.ARC_ItemDepartOverride

**Schema:** SQLUser
**Columnas:** 137
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOV_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| DOV_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DOV_Childsub | double |  |  | NO | Childsub |
| DOV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DOV_CreatedDate | date |  |  | SI | Created Date |
| DOV_CreatedTime | time |  |  | SI | Created Time |
| DOV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOV_DateFrom | date |  |  | SI | Date From |
| DOV_DateTo | date |  |  | SI | Date To |
| DOV_Days | double |  |  | SI | Days |
| DOV_Hours | double |  |  | SI | Hours |
| DOV_RowId | varchar |  |  | NO | - |
| DOV_UpdatedDate | date |  |  | SI | Updated Date |
| DOV_UpdatedTime | time |  |  | SI | Updated Time |
| DOV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date of injury |
| Q04 | - |  |  | SI | Time of injury |
| Q05 | - |  |  | SI | Abbreviated Westmead Post-Traumatic Amnesia Scale ... |
| Q07 | - |  |  | SI | Oriented** |
| Q08 | - |  |  | SI | **Patient must have all 5 orientation questions co... |
| Q09 | - |  |  | SI | Picture 1 |
| Q10 | - |  |  | SI | Picture 2 |
| Q11 | - |  |  | SI | Picture 3 |
| Q12 | - |  |  | SI | A-WPTAS Score |
| Q13 | - |  |  | SI | Pupils |
| Q14 | - |  |  | SI | Right |
| Q15 | - |  |  | SI | Left |
| Q16 | - |  |  | SI | Size |
| Q17 | - |  |  | SI | Reaction |
| Q18 | - |  |  | SI | Pupil size - Right |
| Q19 | - |  |  | SI | Pupil size - Left |
| Q20 | - |  |  | SI | Pupil reaction - Right |
| Q21 | - |  |  | SI | Pupil reaction - Left |
| Q22 | - |  |  | SI | Notes |
| Q23 | - |  |  | SI | Administration guidelines |
| Q24 | - |  |  | SI | Orientation questions |
| Q25 | - |  |  | SI | Question 1: WHAT IS YOUR NAME? |
| Q26 | - |  |  | SI | • The patient must provide their full name. |
| Q27 | - |  |  | SI | Question 2: WHAT IS THE NAME OF THIS PLACE? |
| Q28 | - |  |  | SI | • The patient has to be able to give the name of t... |
| Q29 | - |  |  | SI | • If the patient can not name the hospital, give t... |
| Q30 | - |  |  | SI | In Westmead Hospital’s case the 3 choices are ‘Nep... |
| Q31 | - |  |  | SI | Question 3: WHY ARE YOU HERE? |
| Q32 | - |  |  | SI | • The patient must know why they were brought into... |
| Q33 | - |  |  | SI | • If the patient does not know, give them three op... |
| Q34 | - |  |  | SI | Question 4: WHAT MONTH ARE WE IN? |
| Q35 | - |  |  | SI | • For emphasis the examiner can ask what month are... |
| Q36 | - |  |  | SI | • For example, if the patient answers ‘the 6th mon... |
| Q37 | - |  |  | SI | Question 5: WHAT YEAR ARE WE IN? |
| Q38 | - |  |  | SI | • It is considered correct for patients to answer ... |
| Q39 | - |  |  | SI | Picture recognition |
| Q40 | - |  |  | SI | • Straight after administering the GCS (standardis... |
| Q41 | - |  |  | SI | • Picture cards the first time - T1 : Show patient... |
| Q42 | - |  |  | SI | • Tell the patient to remember the pictures for th... |
| Q43 | - |  |  | SI | Scoring |
| Q44 | - |  |  | SI | • For patients who free recall all 3 pictures corr... |
| Q45 | - |  |  | SI | Present the 3 target pictures again and re-test in... |
| Q46 | - |  |  | SI | • For patients who can not free recall, or only pa... |
| Q47 | - |  |  | SI | If patient can recognise any correctly, score 1 pe... |
| Q48 | - |  |  | SI | • For patients who neither remember any pictures b... |
| Q49 | - |  |  | SI | Test 1 |
| Q50 | - |  |  | SI | Show the patient the target set of 3 pictures (Cup... |
| Q51 | - |  |  | SI | Tell the patient to remember the pictures for re-t... |
| Q52 | - |  |  | SI | Tests 2 to Test 5 |
| Q53 | - |  |  | SI | Ask the patient - “What were the three pictures th... |
| Q54 | - |  |  | SI | Assign a score of 1 for each picture that is recal... |
| Q55 | - |  |  | SI | • If the patient is unable to recall all 3 picture... |
| Q56 | - |  |  | SI | Assign a score of 1 for each target picture that i... |
| Q57 | - |  |  | SI | • If the patient is not able to correctly recognis... |
| Q58 | - |  |  | SI | Re-test the patient in 1 hour |
| Q59 | - |  |  | SI | Use of A-WPTAS and GCS for patients with mild trau... |
| Q60 | - |  |  | SI | The A-WPTAS combined with a standardised GCS asses... |
| Q61 | - |  |  | SI | Only for patients with current GCS of 13-15 (<24hr... |
| Q62 | - |  |  | SI | Administer both tests at hourly intervals to gauge... |
| Q63 | - |  |  | SI | Also, note the following: poor motivation, depress... |
| Q64 | - |  |  | SI | NB: This is a screening device, so exercise clinic... |
| Q65 | - |  |  | SI | Admission and Discharge Criteria |
| Q66 | - |  |  | SI | A patient is considered to be out of PTA when they... |
| Q67 | - |  |  | SI | Both the GCS and A-WPTAS should be used in conjunc... |
| Q68 | - |  |  | SI | Patients scoring 18/18 can be considered for disch... |
| Q69 | - |  |  | SI | For patients who do not obtain 18/18 re-assess aft... |
| Q70 | - |  |  | SI | Patients with persistent score <18/18 at 4 hours p... |
| Q71 | - |  |  | SI | Clinical judgement and consideration of pre-existi... |
| Q72 | - |  |  | SI | Referral to GP on discharge if abnormal PTA was pr... |
| Q73 | - |  |  | SI | The Westmead Post-Traumatic Amnesia Scale (WPTAS) ... |
| Q74 | - |  |  | SI | This form is based on the author's version (4). |
| Q75 | - |  |  | SI | 1. Shores EA, Marosszeky JE, Sandanam J, Batchelor... |
| Q76 | - |  |  | SI | 2. Shores EA, Lammél A, Hullick C, et al,. |
| Q77 | - |  |  | SI | The diagnostic accuracy of the Revised Westmead PT... |
| Q78 | - |  |  | SI | J Neurology Neurosurg Psychiatry 2008 |
| Q79 | - |  |  | SI | 3. Meares S, Shores EA, Taylor AJ, Lammél A, Batch... |
| Q80 | - |  |  | SI | A brief measure to identify acute cognitive impair... |
| Q81 | - |  |  | SI | 4.  Shores EA. Glasgow Coma Scale (GCS) and Abbrev... |
| Q82 | - |  |  | SI | https://www.mq.edu.au/about/about-the-university/o... |
| Q83 | - |  |  | SI | The Abbreviated-Westmead Post-Traumatic Amnesia Sc... |
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