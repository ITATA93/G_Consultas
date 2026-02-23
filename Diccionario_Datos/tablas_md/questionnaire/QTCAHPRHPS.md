# questionnaire.QTCAHPRHPS

> Pelvic Symptoms

**Schema:** questionnaire
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pelvic Symptoms

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Urinary Symptoms |
| Q02 | numeric |  |  | SI | Frequency of Urination while awake |
| Q02A | varchar |  |  | SI | number of times per day |
| Q03 | numeric |  |  | SI | Frequency of Urination during sleep hours |
| Q03A | varchar |  |  | SI | number of times per night |
| Q04 | varchar |  |  | SI | When you have a normal urge to urinate, |
| Q04A | varchar |  |  | SI | How long can you delay? |
| Q05 | numeric |  |  | SI | Minutes |
| Q06 | numeric |  |  | SI | Hours |
| Q07 | bit |  |  | SI | Not at all |
| Q08 | varchar |  |  | SI | The usual amount of urine passed is |
| Q09 | varchar |  |  | SI | Typical position for emptying bladder & comments |
| Q11 | varchar |  |  | SI | Bowel Symptoms |
| Q12 | varchar |  |  | SI | Number of Bowel Symptoms |
| Q14 | numeric |  |  | SI | Per day |
| Q15 | numeric |  |  | SI | Per week |
| Q16 | varchar |  |  | SI | Other |
| Q17 | varchar |  |  | SI | The Bowel movements are typically |
| Q18 | varchar |  |  | SI | Typical position for emptying bowel & comments |
| Q19 | varchar |  |  | SI | If constipation is present describe management tec... |
| Q20 | varchar |  |  | SI | When you have an urge to have Bowel Movement, |
| Q20A | varchar |  |  | SI | How long can you delay before you have to go the t... |
| Q21 | numeric |  |  | SI | Minutes |
| Q22 | numeric |  |  | SI | Hours |
| Q23 | bit |  |  | SI | Not at all |
| Q24 | numeric |  |  | SI | Average Fluid intake (one glas is 8 oz or one cup) |
| Q24A | varchar |  |  | SI | glasses per day |
| Q25 | numeric |  |  | SI | Of this total, how many are caffeinated? |
| Q25A | varchar |  |  | SI | glasses per day |
| Q26 | varchar |  |  | SI | Rate a feeling of organ 'falling out' /prolapse or... |
| Q27 | bit |  |  | SI | None |
| Q28 | numeric |  |  | SI | Times per month |
| Q29 | varchar |  |  | SI | Record if related to activity or menstrual history |
| Q30 | numeric |  |  | SI | When standing after |
| Q31 | varchar |  |  | SI | Time Unit |
| Q32 | bit |  |  | SI | With exertion or straining |
| Q33 | varchar |  |  | SI | Other |
| Q34 | numeric |  |  | SI | Bladder leakage - number of episodes |
| Q35 | varchar |  |  | SI | Bladder leakage - how often |
| Q36 | varchar |  |  | SI | How much urine leaked? |
| Q37 | numeric |  |  | SI | Bowel Leakage - number of episodes |
| Q38 | varchar |  |  | SI | Bowel Leakage - how often |
| Q39 | varchar |  |  | SI | How much stool do you lose? |
| Q40 | numeric |  |  | SI | How many pad changes in 24 hours? |
| Q43 | varchar |  |  | SI | Protection |
| Q44 | varchar |  |  | SI | Leak and Protection comments |
| Q47 | varchar |  |  | SI | Further Evaluation |
| Q50 | varchar |  |  | SI | Urinary |
| Q53 | varchar |  |  | SI | Bowel |
| Q54 | varchar |  |  | SI | Fluid Intake |
| Q56 | date |  |  | SI | Date |
| Q57 | varchar |  |  | SI | Pelvic Pressure |
| Q58 | varchar |  |  | SI | Bladder Leakage |
| Q59 | varchar |  |  | SI | Bowel Leakage |
| Q60 | varchar |  |  | SI | Protection |
| Q61 | varchar |  |  | SI | This assessment form is designed to retain and dis... |
| Q62 | varchar |  |  | SI | Hours |
| Q63 | varchar |  |  | SI | Frequency per day |
| Q64 | varchar |  |  | SI | Frequencyper week |
| Q65 | time |  |  | SI | Time |
| Q66 | varchar |  |  | SI | Minutes |
| Q67 | varchar |  |  | SI | Frequency per day |
| Q68 | varchar |  |  | SI | Minutes |
| Q69 | varchar |  |  | SI | Average Fluid intake (one glas is 8 oz or one cup) |
| Q70 | varchar |  |  | SI | None |
| Q71 | varchar |  |  | SI | Times per month |
| Q72 | varchar |  |  | SI | Hours |
| Q73 | varchar |  |  | SI | With exertion or straining |
| Q74 | varchar |  |  | SI | Not at all |
| Q75 | varchar |  |  | SI | Not at all |
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