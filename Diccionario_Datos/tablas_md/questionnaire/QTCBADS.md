# questionnaire.QTCBADS

> Behavioural Activation for Depression Scale (BADS)

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Behavioural Activation for Depression Scale (BADS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Please read each statement carefully and then choo... |
| Q04 | varchar |  |  | SI | 0 = Not at all |
| Q05 | varchar |  |  | SI | 1 |
| Q06 | varchar |  |  | SI | 2 = A little |
| Q07 | varchar |  |  | SI | 3 |
| Q08 | varchar |  |  | SI | 4 = A lot |
| Q09 | varchar |  |  | SI | 5 |
| Q10 | varchar |  |  | SI | 6 = Completely |
| Q11 | varchar |  |  | SI | 1. I stay in bed for too long even though I had th... |
| Q12 | varchar |  |  | SI | 2. There were certain things I needed to do that I... |
| Q13 | varchar |  |  | SI | 3. I am content with the amount and types of thing... |
| Q14 | varchar |  |  | SI | 4. I engaged in a wide and diverse array of activi... |
| Q15 | varchar |  |  | SI | 5. I made good decisions about what type of activi... |
| Q16 | varchar |  |  | SI | 6. I was active, but did not accomplish any of my ... |
| Q17 | varchar |  |  | SI | 7. I was an active person and accomplished the goa... |
| Q18 | varchar |  |  | SI | 8. Most of what I did was to escape from or avoid ... |
| Q19 | varchar |  |  | SI | 9. I did things to avoid feeling sadness or other ... |
| Q20 | varchar |  |  | SI | 10. I tried not to think about certain things |
| Q21 | varchar |  |  | SI | 11. I did things even though they were hard becaus... |
| Q22 | varchar |  |  | SI | 12. I did something that was hard to do but it was... |
| Q23 | varchar |  |  | SI | 13. I spent a long time thinking over and over abo... |
| Q24 | varchar |  |  | SI | 14. I kept trying to think of ways to solve a prob... |
| Q25 | varchar |  |  | SI | 15. I frequently spent time thinking about my past... |
| Q26 | varchar |  |  | SI | 16. I did not see any of my friends |
| Q27 | varchar |  |  | SI | 17. I was withdrawn and quiet, even around people ... |
| Q28 | varchar |  |  | SI | 18. I was not social, even though I had opportunit... |
| Q29 | varchar |  |  | SI | 19. I pushed people away with my negativity |
| Q30 | varchar |  |  | SI | 20. I did things to cut myself off from other peop... |
| Q31 | varchar |  |  | SI | 21. I took time off of work / school simply becaus... |
| Q32 | varchar |  |  | SI | 22. My work / schoolwork / chores / responsibiliti... |
| Q33 | varchar |  |  | SI | 23. I structured my day's activities |
| Q34 | varchar |  |  | SI | 24. I only engaged in activities that would distra... |
| Q35 | varchar |  |  | SI | 25. I began to feel badly when others around me ex... |
| Q36 | varchar |  |  | SI | Notes |
| Q37 | varchar |  |  | SI | Activation subscale |
| Q38 | varchar |  |  | SI | Avoidance / Rumination subscale |
| Q39 | varchar |  |  | SI | Work / School Impairment subscale |
| Q40 | varchar |  |  | SI | Social Impairment subscale |
| Q41 | varchar |  |  | SI | Total BADS score |
| Q42 | varchar |  |  | SI | Kanter JW, Mulick PS, Busch AM, Berlin KS, Martell... |
| Q43 | varchar |  |  | SI | The behavioral activation for depression scale (BA... |
| Q44 | varchar |  |  | SI | The BADS has also been administered to a clinicall... |
| Q45 | varchar |  |  | SI | Kanter JW, Rusch LC, Busch AM, & Sedivy SK (2009).... |
| Q46 | varchar |  |  | SI | Journal of Psychopathology and Behavioral Assessme... |
| Q47 | varchar |  |  | SI | The scale is designed to be administered weekly to... |
| Q48 | varchar |  |  | SI | For all subscales, high scores are consistent with... |
| Q49 | varchar |  |  | SI | For all subscales, high scores are consistent with... |
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