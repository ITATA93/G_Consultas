# SQLUser.PAC_ACPDisposal

**Schema:** SQLUser
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACPDSP_RowId | bigint | PK |  | NO | - |
| ACPDSP_Code | varchar |  |  | NO | Code |
| ACPDSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACPDSP_CreatedDate | date |  |  | SI | Created Date |
| ACPDSP_CreatedTime | time |  |  | SI | Created Time |
| ACPDSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACPDSP_DateFrom | date |  |  | SI | Date From |
| ACPDSP_DateTo | date |  |  | SI | Date To |
| ACPDSP_Desc | varchar |  |  | NO | Description |
| ACPDSP_NationalCode | varchar |  |  | SI | National Code |
| ACPDSP_Owner | varchar |  |  | SI | Owner |
| ACPDSP_UpdatedDate | date |  |  | SI | Updated Date |
| ACPDSP_UpdatedTime | time |  |  | SI | Updated Time |
| ACPDSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Say to the patient: |
| Q04 | - |  |  | SI | Below is a list of common symptoms of anxiety or s... |
| Q05 | - |  |  | SI | Please read each item in the list carefully. |
| Q06 | - |  |  | SI | Indicate how often you have experienced each sympt... |
| Q07 | - |  |  | SI | 1.&nbsp |
| Q08 | - |  |  | SI | 2. My breath was short |
| Q09 | - |  |  | SI | 3. I had an upset stomach |
| Q10 | - |  |  | SI | 4. I felt like things were not real or like I was ... |
| Q11 | - |  |  | SI | 5. I felt like I was losing control |
| Q12 | - |  |  | SI | 6. I was afraid of being judged by others |
| Q13 | - |  |  | SI | 7. I was afraid of being humiliated or embarrassed |
| Q14 | - |  |  | SI | 8. I had difficulty falling asleep |
| Q15 | - |  |  | SI | 9. I had difficulty staying asleep |
| Q16 | - |  |  | SI | 10. I was irritable |
| Q17 | - |  |  | SI | 11. I had outbursts of anger |
| Q18 | - |  |  | SI | 12. I had difficulty concentrating |
| Q19 | - |  |  | SI | 13. I was easily startled or upset |
| Q20 | - |  |  | SI | 14. I was less interested in doing something I typ... |
| Q21 | - |  |  | SI | 15. I felt detached or isolated from others |
| Q22 | - |  |  | SI | 16. I felt like I was in a daze |
| Q23 | - |  |  | SI | 17. I had a hard time sitting still |
| Q24 | - |  |  | SI | 18. I worried too much |
| Q25 | - |  |  | SI | 19. I could not control my worry |
| Q26 | - |  |  | SI | 20. I felt restless, keyed up, or on edge |
| Q27 | - |  |  | SI | 21. I felt tired |
| Q28 | - |  |  | SI | 22. My muscles were tense |
| Q29 | - |  |  | SI | 23. I had back pain, neck pain, or muscle cramps |
| Q30 | - |  |  | SI | 24. I felt like I had no control over my life |
| Q31 | - |  |  | SI | 25. I felt like something terrible was going to ha... |
| Q32 | - |  |  | SI | 26. I was concerned about my finances |
| Q33 | - |  |  | SI | 27. I was concerned about my health |
| Q34 | - |  |  | SI | 28. I was concerned about my children |
| Q35 | - |  |  | SI | 29. I was afraid of dying |
| Q36 | - |  |  | SI | 30. I was afraid of becoming a burden to my family... |
| Q37 | - |  |  | SI | Total Score |
| Q38 | - |  |  | SI | Somatic Subscale Score |
| Q39 | - |  |  | SI | Cognitive Subscale Score |
| Q40 | - |  |  | SI | Affective Subscale Score |
| Q41 | - |  |  | SI | Scoring Instructions |
| Q42 | - |  |  | SI | Items 1 through 25 are scorable items. |
| Q43 | - |  |  | SI | Each item ranges from 0 to 3. |
| Q44 | - |  |  | SI | Each item loads on only one scale. |
| Q45 | - |  |  | SI | Items 26 through 30 are used to help clinicians id... |
| Q46 | - |  |  | SI | They are not used to calculate the total score of ... |
| Q47 | - |  |  | SI | Total Score = sum of items 1 through 25. |
| Q48 | - |  |  | SI | Somatic subscale (9 items) = sum of items 1, 2, 3,... |
| Q49 | - |  |  | SI | Cognitive subscale (8 items) = sum of items 4, 5, ... |
| Q50 | - |  |  | SI | Affective subscale (8 items) = sum of items 6, 7, ... |
| Q51 | - |  |  | SI | Segal DL, June A, Payne M, Coolidge FL, Yochim B. ... |
| Q52 | - |  |  | SI | Geriatric Anxiety Scale (GAS) © Daniel L. Segal, P... |
| Q53 | - |  |  | SI | 0 - 75 |
| Q54 | - |  |  | SI | Higher scores corresponding to higher levels of an... |
| Q55 | - |  |  | SI | The Geriatric Anxiety Scale (GAS) is an instrument... |
| Q56 | - |  |  | SI | The Geriatric Anxiety Scale (GAS |
| Q57 | - |  |  | SI | The Geriatric Anxiety Scale (GAS) is an instrument... |
| Q58 | - |  |  | SI | The total score may total between 0 and 75, with h... |
| Q59 | - |  |  | SI | The total score may total between 0 and 75, with h... |
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