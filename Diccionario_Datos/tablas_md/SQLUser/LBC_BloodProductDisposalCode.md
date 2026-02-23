# SQLUser.LBC_BloodProductDisposalCode

**Schema:** SQLUser
**Columnas:** 130
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPDC_RowID | bigint | PK |  | NO | - |
| LBCBPDC_BloodProduct_DR | bigint |  | FK | SI | Created Product Code |
| LBCBPDC_Code | varchar |  |  | NO | Code |
| LBCBPDC_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCBPDC_ConstitutesProductConversion | varchar |  |  | SI | Constitutes Product Conversion |
| LBCBPDC_CreatedDate | date |  |  | SI | Created Date |
| LBCBPDC_CreatedTime | time |  |  | SI | Created Time |
| LBCBPDC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCBPDC_DateFrom | date |  |  | SI | Effective date for the record |
| LBCBPDC_DateTo | date |  |  | SI | Last day the record is active |
| LBCBPDC_Desc | varchar |  |  | NO | Description |
| LBCBPDC_FateCategory | varchar |  |  | SI | Blood Product Fate Category |
| LBCBPDC_Owner | varchar |  |  | SI | Owner |
| LBCBPDC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCBPDC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCBPDC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Date form given |
| Q10 | - |  |  | SI | 03. I have felt I have someone to turn to for supp... |
| Q11 | - |  |  | SI | 04. I have felt OK about myself |
| Q12 | - |  |  | SI | 05. I have felt totally lacking in energy and enth... |
| Q13 | - |  |  | SI | 06. I have been physically violent to others |
| Q14 | - |  |  | SI | 07. I have felt able to cope when things go wrong |
| Q15 | - |  |  | SI | 08. I have been troubled by aches, pains, or other... |
| Q16 | - |  |  | SI | 09. I have thought of hurting myself |
| Q17 | - |  |  | SI | 10. Talking to people has felt too much for me |
| Q18 | - |  |  | SI | 11. Tension and anxiety have prevented me doing im... |
| Q19 | - |  |  | SI | 12. I have been happy with the things I have done |
| Q2 | - |  |  | SI | Stage completed |
| Q20 | - |  |  | SI | 13. I have been disturbed by unwanted thoughts and... |
| Q21 | - |  |  | SI | 14. I have felt like crying |
| Q22 | - |  |  | SI | 15. I have felt panic or terror |
| Q23 | - |  |  | SI | 16. I made plans to end my life |
| Q24 | - |  |  | SI | 17. I have felt overwhelmed by my problems |
| Q25 | - |  |  | SI | 18. I have had difficulty getting to sleep or stay... |
| Q26 | - |  |  | SI | 19. I have felt warmth or affection for someone |
| Q27 | - |  |  | SI | 20. My problems have been impossible to put to one... |
| Q28 | - |  |  | SI | 21. I have been able to do most things I needed to |
| Q29 | - |  |  | SI | 22. I have threatened or intimidated another perso... |
| Q3 | - |  |  | SI | IMPORTANT - PLEASE READ THIS FIRST |
| Q30 | - |  |  | SI | 23. I have felt despairing or hopeless |
| Q31 | - |  |  | SI | 24. I have thought it would be better if I were de... |
| Q32 | - |  |  | SI | 25. I have felt criticised by other people |
| Q33 | - |  |  | SI | 26. I have thought I have no friends |
| Q34 | - |  |  | SI | 27. I have felt unhappy |
| Q35 | - |  |  | SI | 28. Unwanted images or memories have been distress... |
| Q36 | - |  |  | SI | 29. I have been irritable when with other people |
| Q37 | - |  |  | SI | 30. I have thought I am to blame for my problems a... |
| Q38 | - |  |  | SI | 31. I have felt optimistic about my future |
| Q39 | - |  |  | SI | 32. I have achieved the things I wanted to |
| Q4 | - |  |  | SI | This form has 34 statements about how you have bee... |
| Q40 | - |  |  | SI | 33. I have felt humiliated or shamed by other peop... |
| Q41 | - |  |  | SI | 34. I have hurt myself physically or taken dangero... |
| Q42 | - |  |  | SI | For Clinicans Use Only |
| Q43 | - |  |  | SI | Subjective well-being total score |
| Q44 | - |  |  | SI | Subjective well-being mean score |
| Q45 | - |  |  | SI | Subjective well-being clinical score |
| Q46 | - |  |  | SI | Problems / symptoms total score |
| Q47 | - |  |  | SI | Problems / symptoms mean score |
| Q48 | - |  |  | SI | Problems / symptoms clinical score |
| Q49 | - |  |  | SI | Life functioning total score |
| Q5 | - |  |  | SI | Please read each statement and think how often you... |
| Q50 | - |  |  | SI | Life functioning mean score |
| Q51 | - |  |  | SI | Life functioning clinical score |
| Q52 | - |  |  | SI | Risk / harm total score |
| Q53 | - |  |  | SI | Risk / harm mean score |
| Q54 | - |  |  | SI | Risk / harm clinical score |
| Q55 | - |  |  | SI | All items total score |
| Q56 | - |  |  | SI | All items mean score |
| Q57 | - |  |  | SI | All items clinical score |
| Q58 | - |  |  | SI | All minus r total score |
| Q59 | - |  |  | SI | All minus r mean score |
| Q6 | - |  |  | SI | Then tick the box which is closest to this. |
| Q60 | - |  |  | SI | All minus r clinical score |
| Q61 | - |  |  | SI | Thank you for your time in completing this questio... |
| Q62 | - |  |  | SI | Over the last week ... |
| Q63 | - |  |  | SI | This instrument was originally developed by Evans ... |
| Q64 | - |  |  | SI | The CORE-OM assesses the efficacy and effectivenes... |
| Q65 | - |  |  | SI | Date |
| Q66 | - |  |  | SI | Time |
| Q67 | - |  |  | SI | 1. Evans C, Mellor-Clark J, Margison F, et al,. CO... |
| Q68 | - |  |  | SI | 2. Evans C, Mellor-Clark J, Margison F, et al,. CO... |
| Q69 | - |  |  | SI | The measure is problem-scored with higher scores i... |
| Q7 | - |  |  | SI | Over the last week ... |
| Q70 | - |  |  | SI | The overall maximum score is 136, with maximum sco... |
| Q71 | - |  |  | SI | TEST |
| Q72 | - |  |  | SI | This instrument was originally developed by Evans ... |
| Q73 | - |  |  | SI | 3. Mothersole G, Jordan T. Managing Therapy Outcom... |
| Q74 | - |  |  | SI | All items Total Clinical Score caption |
| Q8 | - |  |  | SI | 01. I have felt terribly alone and isolated |
| Q9 | - |  |  | SI | 02. I have felt tense, anxious or nervous |
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