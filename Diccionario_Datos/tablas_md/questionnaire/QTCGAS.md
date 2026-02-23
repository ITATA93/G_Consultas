# questionnaire.QTCGAS

> Geriatric Anxiety Scale (GAS)

**Schema:** questionnaire
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Geriatric Anxiety Scale (GAS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Say to the patient: |
| Q04 | varchar |  |  | SI | Below is a list of common symptoms of anxiety or s... |
| Q05 | varchar |  |  | SI | Please read each item in the list carefully. |
| Q06 | varchar |  |  | SI | Indicate how often you have experienced each sympt... |
| Q07 | varchar |  |  | SI | 1.&nbsp;My heart raced or beat strongly |
| Q08 | varchar |  |  | SI | 2. My breath was short |
| Q09 | varchar |  |  | SI | 3. I had an upset stomach |
| Q10 | varchar |  |  | SI | 4. I felt like things were not real or like I was ... |
| Q11 | varchar |  |  | SI | 5. I felt like I was losing control |
| Q12 | varchar |  |  | SI | 6. I was afraid of being judged by others |
| Q13 | varchar |  |  | SI | 7. I was afraid of being humiliated or embarrassed |
| Q14 | varchar |  |  | SI | 8. I had difficulty falling asleep |
| Q15 | varchar |  |  | SI | 9. I had difficulty staying asleep |
| Q16 | varchar |  |  | SI | 10. I was irritable |
| Q17 | varchar |  |  | SI | 11. I had outbursts of anger |
| Q18 | varchar |  |  | SI | 12. I had difficulty concentrating |
| Q19 | varchar |  |  | SI | 13. I was easily startled or upset |
| Q20 | varchar |  |  | SI | 14. I was less interested in doing something I typ... |
| Q21 | varchar |  |  | SI | 15. I felt detached or isolated from others |
| Q22 | varchar |  |  | SI | 16. I felt like I was in a daze |
| Q23 | varchar |  |  | SI | 17. I had a hard time sitting still |
| Q24 | varchar |  |  | SI | 18. I worried too much |
| Q25 | varchar |  |  | SI | 19. I could not control my worry |
| Q26 | varchar |  |  | SI | 20. I felt restless, keyed up, or on edge |
| Q27 | varchar |  |  | SI | 21. I felt tired |
| Q28 | varchar |  |  | SI | 22. My muscles were tense |
| Q29 | varchar |  |  | SI | 23. I had back pain, neck pain, or muscle cramps |
| Q30 | varchar |  |  | SI | 24. I felt like I had no control over my life |
| Q31 | varchar |  |  | SI | 25. I felt like something terrible was going to ha... |
| Q32 | varchar |  |  | SI | 26. I was concerned about my finances |
| Q33 | varchar |  |  | SI | 27. I was concerned about my health |
| Q34 | varchar |  |  | SI | 28. I was concerned about my children |
| Q35 | varchar |  |  | SI | 29. I was afraid of dying |
| Q36 | varchar |  |  | SI | 30. I was afraid of becoming a burden to my family... |
| Q37 | varchar |  |  | SI | Total Score |
| Q38 | varchar |  |  | SI | Somatic Subscale Score |
| Q39 | varchar |  |  | SI | Cognitive Subscale Score |
| Q40 | varchar |  |  | SI | Affective Subscale Score |
| Q41 | varchar |  |  | SI | Scoring Instructions |
| Q42 | varchar |  |  | SI | Items 1 through 25 are scorable items. |
| Q43 | varchar |  |  | SI | Each item ranges from 0 to 3. |
| Q44 | varchar |  |  | SI | Each item loads on only one scale. |
| Q45 | varchar |  |  | SI | Items 26 through 30 are used to help clinicians id... |
| Q46 | varchar |  |  | SI | They are not used to calculate the total score of ... |
| Q47 | varchar |  |  | SI | Total Score = sum of items 1 through 25. |
| Q48 | varchar |  |  | SI | Somatic subscale (9 items) = sum of items 1, 2, 3,... |
| Q49 | varchar |  |  | SI | Cognitive subscale (8 items) = sum of items 4, 5, ... |
| Q50 | varchar |  |  | SI | Affective subscale (8 items) = sum of items 6, 7, ... |
| Q51 | varchar |  |  | SI | Segal DL, June A, Payne M, Coolidge FL, Yochim B. ... |
| Q52 | varchar |  |  | SI | Geriatric Anxiety Scale (GAS) © Daniel L. Segal, P... |
| Q53 | varchar |  |  | SI | 0 - 75 |
| Q54 | varchar |  |  | SI | Higher scores corresponding to higher levels of an... |
| Q55 | varchar |  |  | SI | The Geriatric Anxiety Scale (GAS) is an instrument... |
| Q56 | varchar |  |  | SI | The Geriatric Anxiety Scale (GAS; Segal et al.&nbs... |
| Q57 | varchar |  |  | SI | The Geriatric Anxiety Scale (GAS) is an instrument... |
| Q58 | varchar |  |  | SI | The total score may total between 0 and 75, with h... |
| Q59 | varchar |  |  | SI | The total score may total between 0 and 75, with h... |
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