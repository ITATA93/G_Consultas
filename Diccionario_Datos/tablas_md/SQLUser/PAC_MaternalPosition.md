# SQLUser.PAC_MaternalPosition

**Schema:** SQLUser
**Columnas:** 141
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MPOS_RowId | bigint | PK |  | NO | - |
| MPOS_Code | varchar |  |  | NO | Code |
| MPOS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MPOS_CreatedDate | date |  |  | SI | Created Date |
| MPOS_CreatedTime | time |  |  | SI | Created Time |
| MPOS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MPOS_DateFrom | date |  |  | SI | Date From |
| MPOS_DateTo | date |  |  | SI | Date To |
| MPOS_Desc | varchar |  |  | NO | Description |
| MPOS_NationalCode | varchar |  |  | SI | National Code |
| MPOS_Owner | varchar |  |  | SI | Owner |
| MPOS_UpdatedDate | date |  |  | SI | Updated Date |
| MPOS_UpdatedTime | time |  |  | SI | Updated Time |
| MPOS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Energy Level (EL) |
| Q04 | - |  |  | SI | I'm tired all the time |
| Q05 | - |  |  | SI | Everything is an effort |
| Q06 | - |  |  | SI | I soon run out of energy |
| Q07 | - |  |  | SI | Pain (P) |
| Q08 | - |  |  | SI | I have pain at night |
| Q09 | - |  |  | SI | I have unbearable pain |
| Q10 | - |  |  | SI | I find it painful to change position |
| Q11 | - |  |  | SI | I'm in pain when I walk |
| Q12 | - |  |  | SI | I'm in pain when I'm standing |
| Q13 | - |  |  | SI | I'm in constant pain |
| Q14 | - |  |  | SI | I'm in pain when going up or down stairs |
| Q15 | - |  |  | SI | I'm in pain when I'm sitting |
| Q16 | - |  |  | SI | Emotional Reaction (ER) |
| Q17 | - |  |  | SI | Things are getting me down |
| Q18 | - |  |  | SI | I've forgotten what it's like to enjoy myself |
| Q19 | - |  |  | SI | I'm feeling on edge |
| Q20 | - |  |  | SI | The days seem to drag |
| Q21 | - |  |  | SI | I lose my temper easily these days |
| Q22 | - |  |  | SI | I feel as if I'm losing control |
| Q23 | - |  |  | SI | Worry is keeping me awake at night |
| Q24 | - |  |  | SI | I feel that life is not worth living |
| Q25 | - |  |  | SI | I wake up feeling depressed |
| Q26 | - |  |  | SI | Sleep (S) |
| Q27 | - |  |  | SI | I take pills to help me sleep |
| Q28 | - |  |  | SI | I'm waking up in the early hours of the morning |
| Q29 | - |  |  | SI | I lie awake for most of the night |
| Q30 | - |  |  | SI | It takes me a long time to get to sleep |
| Q31 | - |  |  | SI | I sleep badly at night |
| Q32 | - |  |  | SI | Social Isolation (SI) |
| Q33 | - |  |  | SI | I feel lonely |
| Q34 | - |  |  | SI | I'm finding it hard to make contact with people |
| Q35 | - |  |  | SI | I feel there is nobody that I am close to |
| Q36 | - |  |  | SI | I feel I am a burden to people |
| Q37 | - |  |  | SI | I'm finding it hard to get along with people |
| Q38 | - |  |  | SI | Physical Abilities (PA) |
| Q39 | - |  |  | SI | I can walk about only indoors |
| Q40 | - |  |  | SI | I find it hard to bend |
| Q41 | - |  |  | SI | I'm unable to walk at all |
| Q42 | - |  |  | SI | I have trouble getting up and down stairs and step... |
| Q43 | - |  |  | SI | I find it hard to reach for things |
| Q44 | - |  |  | SI | I find it hard to get dressed by myself |
| Q45 | - |  |  | SI | I find it hard to stand for long (e.g., at the kit... |
| Q46 | - |  |  | SI | I need help to walk about outside (e.g., a walking... |
| Q47 | - |  |  | SI | Is your present state of health causing problems w... |
| Q48 | - |  |  | SI | Work? |
| Q49 | - |  |  | SI | (that is, paid employment) |
| Q50 | - |  |  | SI | Looking after the home? |
| Q51 | - |  |  | SI | (cleaning & cooking, repairs, odd jobs around the ... |
| Q52 | - |  |  | SI | Social life? |
| Q53 | - |  |  | SI | (going out, seeing friends, going to the movies, e... |
| Q54 | - |  |  | SI | Home life? |
| Q55 | - |  |  | SI | (that is, relationships with other people in your ... |
| Q56 | - |  |  | SI | Sex life? |
| Q57 | - |  |  | SI | Interests and hobbies? |
| Q58 | - |  |  | SI | (sports, arts and crafts, do-it-yourself, etc.) |
| Q59 | - |  |  | SI | Vacations? |
| Q60 | - |  |  | SI | (summer or winter vacations, weekends away, etc.) |
| Q61 | - |  |  | SI | Energy Level Score |
| Q62 | - |  |  | SI | Pain Score |
| Q63 | - |  |  | SI | Emotional Reaction Score |
| Q64 | - |  |  | SI | Sleep Score |
| Q65 | - |  |  | SI | Social Isolation Score |
| Q66 | - |  |  | SI | Physical Abilities Score |
| Q67 | - |  |  | SI | Total Score |
| Q68 | - |  |  | SI | Part I: 38 questions in 6 subareas, with each ques... |
| Q69 | - |  |  | SI | Part II: 7 life areas affected. |
| Q70 | - |  |  | SI | NHP scores are calculated by averaging domain scor... |
| Q71 | - |  |  | SI | Score |
| Q72 | - |  |  | SI | Classification |
| Q73 | - |  |  | SI | 0 :No perceived distress |
| Q74 | - |  |  | SI | 100 :Maximum perceived distress |
| Q75 | - |  |  | SI | The Nottingham Health Profile is intended for prim... |
| Q76 | - |  |  | SI | The higher the score, the greater the number and s... |
| Q77 | - |  |  | SI | 0 |
| Q78 | - |  |  | SI | No perceived distress |
| Q79 | - |  |  | SI | 100 |
| Q80 | - |  |  | SI | Maximum perceived distress |
| Q81 | - |  |  | SI | Work? (that is, paid employment)	 |
| Q82 | - |  |  | SI | Looking after the home? (cleaning & cooking, repai... |
| Q83 | - |  |  | SI | Social life? (going out, seeing friends, going to ... |
| Q84 | - |  |  | SI | Home life? (that is, relationships with other peop... |
| Q85 | - |  |  | SI | Interests and hobbies? (sports, arts and crafts, d... |
| Q86 | - |  |  | SI | Vacations? (summer or winter vacations, weekends a... |
| Q87 | - |  |  | SI | Total Score Caption |
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