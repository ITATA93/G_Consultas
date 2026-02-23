# questionnaire.QTCRATHUS

> The Rathus Assertiveness Schedule (RAS)

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* The Rathus Assertiveness Schedule (RAS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | 1. Most people seem to be more aggressive and asse... |
| Q04 | varchar |  |  | SI | 2. I have hesitated to make or accept dates becaus... |
| Q05 | varchar |  |  | SI | 3. When the food served at a restaurant is not don... |
| Q06 | varchar |  |  | SI | 4. I am careful to avoid hurting other people’s fe... |
| Q07 | varchar |  |  | SI | 5. If a salesperson has gone to considerable troub... |
| Q08 | varchar |  |  | SI | 6. When I am asked to do something, I insist upon ... |
| Q09 | varchar |  |  | SI | 7. There are times when I look for a good, vigorou... |
| Q10 | varchar |  |  | SI | 8. I strive to get ahead as well as most people in... |
| Q11 | varchar |  |  | SI | 9. To be honest, people often take advantage of me... |
| Q12 | varchar |  |  | SI | 10. I enjoy starting conversations with new acquai... |
| Q13 | varchar |  |  | SI | 11. I often don’t know what to say to people I fin... |
| Q14 | varchar |  |  | SI | 12. I will hesitate to make phone calls to busines... |
| Q15 | varchar |  |  | SI | 13. I would rather apply for a job or for admissio... |
| Q16 | varchar |  |  | SI | 14. I find it embarrassing to return merchandise. |
| Q17 | varchar |  |  | SI | 15. If a close and respected relative were annoyin... |
| Q18 | varchar |  |  | SI | 16. I have avoided asking questions for fear of so... |
| Q19 | varchar |  |  | SI | 17. During an argument, I am sometimes afraid that... |
| Q20 | varchar |  |  | SI | 17. During an argument, I am sometimes afraid that... |
| Q21 | varchar |  |  | SI | 18. If a famed and respected lecturer makes a comm... |
| Q22 | varchar |  |  | SI | 19. I avoid arguing over prices with clerks and sa... |
| Q23 | varchar |  |  | SI | 20. When I have done something important or worthw... |
| Q24 | varchar |  |  | SI | 21. I am open and frank about my feelings. |
| Q25 | varchar |  |  | SI | 22. If someone has been spreading false and bad st... |
| Q26 | varchar |  |  | SI | 23. I often have a hard time saying “No.” |
| Q27 | varchar |  |  | SI | 24. I tend to bottle up my emotions rather than ma... |
| Q28 | varchar |  |  | SI | 25. I complain about poor service in a restaurant ... |
| Q29 | varchar |  |  | SI | 26. When I am given a compliment, I sometimes just... |
| Q30 | varchar |  |  | SI | 27. If a couple near me in a theater or at a lectu... |
| Q31 | varchar |  |  | SI | 28. Anyone attempting to push ahead of me in a lin... |
| Q32 | varchar |  |  | SI | 29. I am quick to express an opinion. |
| Q33 | varchar |  |  | SI | 30. There are times when I just can’t say anything... |
| Q34 | varchar |  |  | SI | The Rathus Assertiveness Scale (RAS) was designed ... |
| Q35 | varchar |  |  | SI | Please refer to the Guidelines section. |
| Q36 | varchar |  |  | SI | The RAS provides a score and a percentile for inte... |
| Q37 | varchar |  |  | SI | -90 to 90: High positive scores indicate high asse... |
| Q38 | varchar |  |  | SI | -90 |
| Q39 | varchar |  |  | SI | Low assertiveness |
| Q40 | varchar |  |  | SI | 90 |
| Q41 | varchar |  |  | SI | High assertiveness |
| Q42 | varchar |  |  | SI | Score |
| Q43 | varchar |  |  | SI | Classification |
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