# questionnaire.QTCNHP

> Nottingham Health Profile

**Schema:** questionnaire
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nottingham Health Profile

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Energy Level (EL) |
| Q04 | varchar |  |  | SI | I'm tired all the time |
| Q05 | varchar |  |  | SI | Everything is an effort |
| Q06 | varchar |  |  | SI | I soon run out of energy |
| Q07 | varchar |  |  | SI | Pain (P) |
| Q08 | varchar |  |  | SI | I have pain at night |
| Q09 | varchar |  |  | SI | I have unbearable pain |
| Q10 | varchar |  |  | SI | I find it painful to change position |
| Q11 | varchar |  |  | SI | I'm in pain when I walk |
| Q12 | varchar |  |  | SI | I'm in pain when I'm standing |
| Q13 | varchar |  |  | SI | I'm in constant pain |
| Q14 | varchar |  |  | SI | I'm in pain when going up or down stairs |
| Q15 | varchar |  |  | SI | I'm in pain when I'm sitting |
| Q16 | varchar |  |  | SI | Emotional Reaction (ER) |
| Q17 | varchar |  |  | SI | Things are getting me down |
| Q18 | varchar |  |  | SI | I've forgotten what it's like to enjoy myself |
| Q19 | varchar |  |  | SI | I'm feeling on edge |
| Q20 | varchar |  |  | SI | The days seem to drag |
| Q21 | varchar |  |  | SI | I lose my temper easily these days |
| Q22 | varchar |  |  | SI | I feel as if I'm losing control |
| Q23 | varchar |  |  | SI | Worry is keeping me awake at night |
| Q24 | varchar |  |  | SI | I feel that life is not worth living |
| Q25 | varchar |  |  | SI | I wake up feeling depressed |
| Q26 | varchar |  |  | SI | Sleep (S) |
| Q27 | varchar |  |  | SI | I take pills to help me sleep |
| Q28 | varchar |  |  | SI | I'm waking up in the early hours of the morning |
| Q29 | varchar |  |  | SI | I lie awake for most of the night |
| Q30 | varchar |  |  | SI | It takes me a long time to get to sleep |
| Q31 | varchar |  |  | SI | I sleep badly at night |
| Q32 | varchar |  |  | SI | Social Isolation (SI) |
| Q33 | varchar |  |  | SI | I feel lonely |
| Q34 | varchar |  |  | SI | I'm finding it hard to make contact with people |
| Q35 | varchar |  |  | SI | I feel there is nobody that I am close to |
| Q36 | varchar |  |  | SI | I feel I am a burden to people |
| Q37 | varchar |  |  | SI | I'm finding it hard to get along with people |
| Q38 | varchar |  |  | SI | Physical Abilities (PA) |
| Q39 | varchar |  |  | SI | I can walk about only indoors |
| Q40 | varchar |  |  | SI | I find it hard to bend |
| Q41 | varchar |  |  | SI | I'm unable to walk at all |
| Q42 | varchar |  |  | SI | I have trouble getting up and down stairs and step... |
| Q43 | varchar |  |  | SI | I find it hard to reach for things |
| Q44 | varchar |  |  | SI | I find it hard to get dressed by myself |
| Q45 | varchar |  |  | SI | I find it hard to stand for long (e.g., at the kit... |
| Q46 | varchar |  |  | SI | I need help to walk about outside (e.g., a walking... |
| Q47 | varchar |  |  | SI | Is your present state of health causing problems w... |
| Q48 | varchar |  |  | SI | Work? |
| Q49 | varchar |  |  | SI | (that is, paid employment) |
| Q50 | varchar |  |  | SI | Looking after the home? |
| Q51 | varchar |  |  | SI | (cleaning & cooking, repairs, odd jobs around the ... |
| Q52 | varchar |  |  | SI | Social life? |
| Q53 | varchar |  |  | SI | (going out, seeing friends, going to the movies, e... |
| Q54 | varchar |  |  | SI | Home life? |
| Q55 | varchar |  |  | SI | (that is, relationships with other people in your ... |
| Q56 | varchar |  |  | SI | Sex life? |
| Q57 | varchar |  |  | SI | Interests and hobbies? |
| Q58 | varchar |  |  | SI | (sports, arts and crafts, do-it-yourself, etc.) |
| Q59 | varchar |  |  | SI | Vacations? |
| Q60 | varchar |  |  | SI | (summer or winter vacations, weekends away, etc.) |
| Q61 | varchar |  |  | SI | Energy Level Score |
| Q62 | varchar |  |  | SI | Pain Score |
| Q63 | varchar |  |  | SI | Emotional Reaction Score |
| Q64 | varchar |  |  | SI | Sleep Score |
| Q65 | varchar |  |  | SI | Social Isolation Score |
| Q66 | varchar |  |  | SI | Physical Abilities Score |
| Q67 | varchar |  |  | SI | Total Score |
| Q68 | varchar |  |  | SI | Part I: 38 questions in 6 subareas, with each ques... |
| Q69 | varchar |  |  | SI | Part II: 7 life areas affected. |
| Q70 | varchar |  |  | SI | NHP scores are calculated by averaging domain scor... |
| Q71 | varchar |  |  | SI | Score |
| Q72 | varchar |  |  | SI | Classification |
| Q73 | varchar |  |  | SI | 0 :No perceived distress |
| Q74 | varchar |  |  | SI | 100 :Maximum perceived distress |
| Q75 | varchar |  |  | SI | The Nottingham Health Profile is intended for prim... |
| Q76 | varchar |  |  | SI | The higher the score, the greater the number and s... |
| Q77 | varchar |  |  | SI | 0 |
| Q78 | varchar |  |  | SI | No perceived distress |
| Q79 | varchar |  |  | SI | 100 |
| Q80 | varchar |  |  | SI | Maximum perceived distress |
| Q81 | varchar |  |  | SI | Work? (that is, paid employment)	 |
| Q82 | varchar |  |  | SI | Looking after the home? (cleaning & cooking, repai... |
| Q83 | varchar |  |  | SI | Social life? (going out, seeing friends, going to ... |
| Q84 | varchar |  |  | SI | Home life? (that is, relationships with other peop... |
| Q85 | varchar |  |  | SI | Interests and hobbies? (sports, arts and crafts, d... |
| Q86 | varchar |  |  | SI | Vacations? (summer or winter vacations, weekends a... |
| Q87 | varchar |  |  | SI | Total Score Caption |
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