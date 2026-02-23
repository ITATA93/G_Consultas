# questionnaire.QTCLUNSERS

> Liverpool University Neuroleptic Side Effect Rating Scale

**Schema:** questionnaire
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Liverpool University Neuroleptic Side Effect Rating Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Instructions: the following scale is intended to b... |
| Q04 | varchar |  |  | SI | Rash |
| Q05 | varchar |  |  | SI | Difficulty staying awake during the day |
| Q06 | varchar |  |  | SI | Runny nose |
| Q07 | varchar |  |  | SI | Increased dreaming |
| Q08 | varchar |  |  | SI | Headaches |
| Q09 | varchar |  |  | SI | Dry mouth |
| Q10 | varchar |  |  | SI | Swollen or tender chest |
| Q11 | varchar |  |  | SI | Chillblains |
| Q12 | varchar |  |  | SI | Difficulty in concentrating |
| Q13 | varchar |  |  | SI | Constipation |
| Q14 | varchar |  |  | SI | Hair loss |
| Q15 | varchar |  |  | SI | Urine darker than usual |
| Q16 | varchar |  |  | SI | Period pains |
| Q17 | varchar |  |  | SI | Tension |
| Q18 | varchar |  |  | SI | Dizziness |
| Q19 | varchar |  |  | SI | Feeling sick |
| Q20 | varchar |  |  | SI | Increased sex drive |
| Q21 | varchar |  |  | SI | Tiredness |
| Q22 | varchar |  |  | SI | Muscle stiffness |
| Q23 | varchar |  |  | SI | Palpitations |
| Q24 | varchar |  |  | SI | Difficulty in remembering things |
| Q25 | varchar |  |  | SI | Losing weight |
| Q26 | varchar |  |  | SI | Lack of emotions |
| Q27 | varchar |  |  | SI | Difficulty in achieving climax |
| Q28 | varchar |  |  | SI | Weak fingernails |
| Q29 | varchar |  |  | SI | Depression |
| Q30 | varchar |  |  | SI | Increased sweating |
| Q31 | varchar |  |  | SI | Mouth ulcers |
| Q32 | varchar |  |  | SI | Slowing of movements |
| Q33 | varchar |  |  | SI | Greasy skin |
| Q34 | varchar |  |  | SI | Sleeping too much |
| Q35 | varchar |  |  | SI | Difficulty passing water |
| Q36 | varchar |  |  | SI | Flushing of face |
| Q37 | varchar |  |  | SI | Muscle spasms |
| Q38 | varchar |  |  | SI | Sensitivity to sun |
| Q39 | varchar |  |  | SI | Diarrhoea |
| Q40 | varchar |  |  | SI | Over-wet or drooling mouth |
| Q41 | varchar |  |  | SI | Blurred vision |
| Q42 | varchar |  |  | SI | Putting on weight |
| Q43 | varchar |  |  | SI | Restlessness |
| Q44 | varchar |  |  | SI | Difficulty getting to sleep |
| Q45 | varchar |  |  | SI | Neck muscles aching |
| Q46 | varchar |  |  | SI | Shakiness |
| Q47 | varchar |  |  | SI | Pins and needles |
| Q48 | varchar |  |  | SI | Painful joints |
| Q49 | varchar |  |  | SI | Reduced sex drive |
| Q50 | varchar |  |  | SI | New or unusual skin marks |
| Q51 | varchar |  |  | SI | Parts of body moving on their own accord eg. foot ... |
| Q52 | varchar |  |  | SI | Itchy skin |
| Q53 | varchar |  |  | SI | Periods less frequent |
| Q54 | varchar |  |  | SI | Passing a lot of water |
| Q55 | varchar |  |  | SI | Results |
| Q56 | varchar |  |  | SI | Psychic side effects |
| Q57 | varchar |  |  | SI | Extra-pyramidal side effects |
| Q58 | varchar |  |  | SI | Hormonal side effects |
| Q59 | varchar |  |  | SI | Anti-cholinergic side effects |
| Q60 | varchar |  |  | SI | Miscellaneous side effects |
| Q61 | varchar |  |  | SI | Other autonomic side effects |
| Q62 | varchar |  |  | SI | Allergic reactions |
| Q63 | varchar |  |  | SI | Lunsers total score |
| Q64 | varchar |  |  | SI | Red herrings |
| Q65 | varchar |  |  | SI | Red Herring item score 0-1 = Low, 2-6 = Average, 5... |
| Q66 | varchar |  |  | SI | Final Lunsers Score |
| Q67 | varchar |  |  | SI | Final Lunsers Index: 0-20 = Low, 31-60 = Medium, 6... |
| Q68 | varchar |  |  | SI | LUNSERS is a fully validated and comprehensive sel... |
| Q69 | varchar |  |  | SI | Score caption |
| Q70 | varchar |  |  | SI | Red Herring Item Score |
| Q71 | varchar |  |  | SI | 0-1 = Low |
| Q72 | varchar |  |  | SI | 2-6 = Average |
| Q73 | varchar |  |  | SI | 5-15 = High |
| Q74 | varchar |  |  | SI | >15 = Very High |
| Q75 | varchar |  |  | SI | Final Lunsers Index |
| Q76 | varchar |  |  | SI | 0-20 = Low |
| Q77 | varchar |  |  | SI | 31-60 = Medium |
| Q78 | varchar |  |  | SI | 61-80 = High |
| Q79 | varchar |  |  | SI | >81 = Very High |
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