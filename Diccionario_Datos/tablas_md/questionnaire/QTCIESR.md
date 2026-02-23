# questionnaire.QTCIESR

> Impact of Event Scale - Revised (IES-R)

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Impact of Event Scale - Revised (IES-R)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | date |  |  | SI | Date of event |
| Q04 | varchar |  |  | SI | Details of event |
| Q05 | varchar |  |  | SI | Instructions |
| Q06 | varchar |  |  | SI | Below is a list of difficulties people sometimes h... |
| Q07 | varchar |  |  | SI | Please read each item, and then indicate how distr... |
| Q08 | varchar |  |  | SI | How much have you been distressed or bothered by t... |
| Q09 | varchar |  |  | SI | 1. Any reminder brought back feelings about it |
| Q10 | varchar |  |  | SI | 2. I had trouble staying asleep |
| Q11 | varchar |  |  | SI | 3. Other things kept making me think about it |
| Q12 | varchar |  |  | SI | 4. I felt irritable and angry |
| Q13 | varchar |  |  | SI | 5. I avoided letting myself get upset when I thoug... |
| Q14 | varchar |  |  | SI | 6. I thought about it when I didn't mean to |
| Q15 | varchar |  |  | SI | 7. I felt as if it hadn't happened or wasn't real |
| Q16 | varchar |  |  | SI | 8. I stayed away from reminders of it |
| Q17 | varchar |  |  | SI | 9. Pictures about it popped into my mind |
| Q18 | varchar |  |  | SI | 10. I was jumpy and easily startled |
| Q19 | varchar |  |  | SI | 11. I tried not to think about it |
| Q20 | varchar |  |  | SI | 12. I was aware that I still had a lot of feelings... |
| Q21 | varchar |  |  | SI | 13. My feelings about it were kind of numb |
| Q22 | varchar |  |  | SI | 14. I found myself acting or feeling like I was ba... |
| Q23 | varchar |  |  | SI | 15. I had trouble falling asleep |
| Q24 | varchar |  |  | SI | 16. I had waves of strong feelings about it |
| Q25 | varchar |  |  | SI | 17. I tried to remove it from my memory |
| Q26 | varchar |  |  | SI | 18. I had trouble concentrating |
| Q27 | varchar |  |  | SI | 19. Reminders of it caused me to have physical rea... |
| Q28 | varchar |  |  | SI | 20. I had dreams about it |
| Q29 | varchar |  |  | SI | 21. I felt watchful and on guard |
| Q30 | varchar |  |  | SI | 22. I tried not to talk about it |
| Q31 | varchar |  |  | SI | Notes |
| Q32 | varchar |  |  | SI | Intrusion Subscore |
| Q33 | varchar |  |  | SI | Avoidance&nbsp;Subscore |
| Q34 | varchar |  |  | SI | Hyper-arousal&nbsp;Subscore |
| Q35 | varchar |  |  | SI | Total mean IES-R Score |
| Q36 | varchar |  |  | SI | Revised Impact of Event Scale (22 questions) |
| Q37 | varchar |  |  | SI | The revised version of the Impact of Event Scale (... |
| Q38 | varchar |  |  | SI | On this test, scores that exceed 24 can be quite m... |
| Q39 | varchar |  |  | SI | The IES-R is very helpful in measuring the affect ... |
| Q40 | varchar |  |  | SI | Sub Scale Questions |
| Q41 | varchar |  |  | SI | Avoidance Subscale = mean of items 5, 7, 8, 11, 12... |
| Q42 | varchar |  |  | SI | Intrusion Subscale = mean of items 1, 2, 3, 6, 9, ... |
| Q43 | varchar |  |  | SI | Hyper arousal Subscale = mean of items 4, 10, 14, ... |
| Q44 | varchar |  |  | SI | Total mean IES-R score = The mean of the Total IES... |
| Q45 | varchar |  |  | SI | Weiss D. The Impact of Event Scale - Revised. In: ... |
| Q46 | varchar |  |  | SI | Horowitz M, Wilner N, Alvarez W. Impact of Event S... |
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