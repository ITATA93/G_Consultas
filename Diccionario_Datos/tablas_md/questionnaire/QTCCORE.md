# questionnaire.QTCCORE

> Core-Om

**Schema:** questionnaire
**Columnas:** 115
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(Core-Om)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date form given |
| Q10 | varchar |  |  | SI | 03. I have felt I have someone to turn to for supp... |
| Q11 | varchar |  |  | SI | 04. I have felt OK about myself |
| Q12 | varchar |  |  | SI | 05. I have felt totally lacking in energy and enth... |
| Q13 | varchar |  |  | SI | 06. I have been physically violent to others |
| Q14 | varchar |  |  | SI | 07. I have felt able to cope when things go wrong |
| Q15 | varchar |  |  | SI | 08. I have been troubled by aches, pains, or other... |
| Q16 | varchar |  |  | SI | 09. I have thought of hurting myself |
| Q17 | varchar |  |  | SI | 10. Talking to people has felt too much for me |
| Q18 | varchar |  |  | SI | 11. Tension and anxiety have prevented me doing im... |
| Q19 | varchar |  |  | SI | 12. I have been happy with the things I have done |
| Q2 | varchar |  |  | SI | Stage completed |
| Q20 | varchar |  |  | SI | 13. I have been disturbed by unwanted thoughts and... |
| Q21 | varchar |  |  | SI | 14. I have felt like crying |
| Q22 | varchar |  |  | SI | 15. I have felt panic or terror |
| Q23 | varchar |  |  | SI | 16. I made plans to end my life |
| Q24 | varchar |  |  | SI | 17. I have felt overwhelmed by my problems |
| Q25 | varchar |  |  | SI | 18. I have had difficulty getting to sleep or stay... |
| Q26 | varchar |  |  | SI | 19. I have felt warmth or affection for someone |
| Q27 | varchar |  |  | SI | 20. My problems have been impossible to put to one... |
| Q28 | varchar |  |  | SI | 21. I have been able to do most things I needed to |
| Q29 | varchar |  |  | SI | 22. I have threatened or intimidated another perso... |
| Q3 | varchar |  |  | SI | IMPORTANT - PLEASE READ THIS FIRST |
| Q30 | varchar |  |  | SI | 23. I have felt despairing or hopeless |
| Q31 | varchar |  |  | SI | 24. I have thought it would be better if I were de... |
| Q32 | varchar |  |  | SI | 25. I have felt criticised by other people |
| Q33 | varchar |  |  | SI | 26. I have thought I have no friends |
| Q34 | varchar |  |  | SI | 27. I have felt unhappy |
| Q35 | varchar |  |  | SI | 28. Unwanted images or memories have been distress... |
| Q36 | varchar |  |  | SI | 29. I have been irritable when with other people |
| Q37 | varchar |  |  | SI | 30. I have thought I am to blame for my problems a... |
| Q38 | varchar |  |  | SI | 31. I have felt optimistic about my future |
| Q39 | varchar |  |  | SI | 32. I have achieved the things I wanted to |
| Q4 | varchar |  |  | SI | This form has 34 statements about how you have bee... |
| Q40 | varchar |  |  | SI | 33. I have felt humiliated or shamed by other peop... |
| Q41 | varchar |  |  | SI | 34. I have hurt myself physically or taken dangero... |
| Q42 | varchar |  |  | SI | For Clinicans Use Only |
| Q43 | varchar |  |  | SI | Subjective well-being total score |
| Q44 | varchar |  |  | SI | Subjective well-being mean score |
| Q45 | varchar |  |  | SI | Subjective well-being clinical score |
| Q46 | varchar |  |  | SI | Problems / symptoms total score |
| Q47 | varchar |  |  | SI | Problems / symptoms mean score |
| Q48 | varchar |  |  | SI | Problems / symptoms clinical score |
| Q49 | varchar |  |  | SI | Life functioning total score |
| Q5 | varchar |  |  | SI | Please read each statement and think how often you... |
| Q50 | varchar |  |  | SI | Life functioning mean score |
| Q51 | varchar |  |  | SI | Life functioning clinical score |
| Q52 | varchar |  |  | SI | Risk / harm total score |
| Q53 | varchar |  |  | SI | Risk / harm mean score |
| Q54 | varchar |  |  | SI | Risk / harm clinical score |
| Q55 | varchar |  |  | SI | All items total score |
| Q56 | varchar |  |  | SI | All items mean score |
| Q57 | varchar |  |  | SI | All items clinical score |
| Q58 | varchar |  |  | SI | All minus r total score |
| Q59 | varchar |  |  | SI | All minus r mean score |
| Q6 | varchar |  |  | SI | Then tick the box which is closest to this. |
| Q60 | varchar |  |  | SI | All minus r clinical score |
| Q61 | varchar |  |  | SI | Thank you for your time in completing this questio... |
| Q62 | varchar |  |  | SI | Over the last week ... |
| Q63 | varchar |  |  | SI | This instrument was originally developed by Evans ... |
| Q64 | varchar |  |  | SI | The CORE-OM assesses the efficacy and effectivenes... |
| Q65 | date |  |  | SI | Date |
| Q66 | time |  |  | SI | Time |
| Q67 | varchar |  |  | SI | 1. Evans C, Mellor-Clark J, Margison F, et al,. CO... |
| Q68 | varchar |  |  | SI | 2. Evans C, Mellor-Clark J, Margison F, et al,. CO... |
| Q69 | varchar |  |  | SI | The measure is problem-scored with higher scores i... |
| Q7 | varchar |  |  | SI | Over the last week ... |
| Q70 | varchar |  |  | SI | The overall maximum score is 136, with maximum sco... |
| Q71 | varchar |  |  | SI | TEST |
| Q72 | varchar |  |  | SI | This instrument was originally developed by Evans ... |
| Q73 | varchar |  |  | SI | 3. Mothersole G, Jordan T. Managing Therapy Outcom... |
| Q74 | varchar |  |  | SI | All items Total Clinical Score caption |
| Q8 | varchar |  |  | SI | 01. I have felt terribly alone and isolated |
| Q9 | varchar |  |  | SI | 02. I have felt tense, anxious or nervous |
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