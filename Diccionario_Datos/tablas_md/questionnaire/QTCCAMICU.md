# questionnaire.QTCCAMICU

> Confusion Assessment Method (CAM) for ICU

**Schema:** questionnaire
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Confusion Assessment Method (CAM) for ICU

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1A: Is the Patient different than his/her baseline... |
| Q02 | varchar |  |  | SI | 1B: Has the patient had any fluctuation in mental ... |
| Q03 | varchar |  |  | SI | (e.g Richmond Agitation and Sedation Scale (RASS))... |
| Q04 | varchar |  |  | SI | Acute Onset or fluctuating course (positive if  'Y... |
| Q05 | varchar |  |  | SI | Attempt the Attention Screening Examination (ASE) ... |
| Q06 | varchar |  |  | SI |  If patient is unable to perform this test or the ... |
| Q07 | varchar |  |  | SI | 2A: ASE Letters test ? |
| Q08 | varchar |  |  | SI | S A V E A H A A R T |
| Q09 | varchar |  |  | SI | Direction: Say to the patient 'I am going to read ... |
| Q10 | varchar |  |  | SI | Score for ASE Letters |
| Q11 | varchar |  |  | SI | 2B: ASE Pictures test? |
| Q12 | varchar |  |  | SI | Score for ASE Pictures |
| Q13 | varchar |  |  | SI | Confirm patient response for Feature 2 |
| Q14 | varchar |  |  | SI | 3A: Use either Set A or Set B,  alternate on conse... |
| Q15 | varchar |  |  | SI | Positive if combined score is less than 4	 |
| Q16 | varchar |  |  | SI | Set A: |
| Q17 | varchar |  |  | SI | 1. Will a stone float on water? |
| Q18 | varchar |  |  | SI | 2. Are there fish in the sea? |
| Q19 | varchar |  |  | SI | 3. Does one pound weigh more than two pounds? |
| Q20 | varchar |  |  | SI | 4. Can you use a hammer to pound a nail? |
| Q21 | varchar |  |  | SI | Set B: |
| Q22 | varchar |  |  | SI | 1. Will a leaf float on water? |
| Q23 | varchar |  |  | SI | 2. Are there Elephants in the sea? |
| Q24 | varchar |  |  | SI | 3. Do two pounds weigh more than one pound? |
| Q25 | varchar |  |  | SI | 4. Can you use a hammer to cut wood? |
| Q26 | varchar |  |  | SI | 3B: Command: Say to the patient ''Hold up this man... |
| Q27 | varchar |  |  | SI | Confirm name of set used |
| Q28 | varchar |  |  | SI | Label A	 |
| Q29 | varchar |  |  | SI |  Label B |
| Q30 | varchar |  |  | SI | Confirm score for set used 	 |
| Q31 | varchar |  |  | SI | Confirm score for command used	 |
| Q32 | varchar |  |  | SI | Total score for Set and  Command |
| Q33 | varchar |  |  | SI | Confirm patient's response for Feature 3	 |
| Q34 | varchar |  |  | SI | Please select Positive if the actual Richmond Agit... |
| Q35 | varchar |  |  | SI | Overall CAM-ICU  |
| Q36 | varchar |  |  | SI | Instructions for completing form: |
| Q37 | varchar |  |  | SI | Instructions for Feature 2 - Inattention:	 |
| Q38 | varchar |  |  | SI | Positive if either score for 2A or 2 B is less tha... |
| Q39 | varchar |  |  | SI | 2A: ASE Letters:	 |
| Q40 | varchar |  |  | SI | Read letters from the following letter list in a n... |
| Q41 | varchar |  |  | SI | S A V E A H A A R T	 |
| Q42 | varchar |  |  | SI | Scoring: Errors are counted when patient fails to ... |
| Q43 | varchar |  |  | SI | Score 1 point for each error |
| Q44 | varchar |  |  | SI | 2B: ASE Pictures:	 |
| Q45 | varchar |  |  | SI | Directions are included on the picture packets (pl... |
| Q46 | varchar |  |  | SI | Instructions for Feature 3 - Disorganised thinking... |
| Q47 | varchar |  |  | SI | 3B: Command:(examiner holds two fingers in front o... |
| Q48 | varchar |  |  | SI | **if the patient is unable to move both arms, for ... |
| Q49 | varchar |  |  | SI | Patient earns 1 point if able to successfully comp... |
| Q50 | varchar |  |  | SI | Overall CAM-ICU:(Feature 1 Plus 2 AND either 3 or ... |
| Q51 | varchar |  |  | SI | Confirm score for set used |
| Q52 | varchar |  |  | SI | Confirm score for command used	 |
| Q53 | varchar |  |  | SI | Or |
| Q54 | varchar |  |  | SI | Confirm patient's response for Feature 3	 |
| Q55 | date |  |  | SI | Date |
| Q56 | time |  |  | SI | Time |
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