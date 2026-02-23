# SQLUser.PAC_BedTypeOrderSet

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OS_ParRef | bigint | PK |  | NO | PAC_BedType Parent Reference |
| OS_Childsub | double |  |  | NO | Childsub |
| OS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OS_CreatedDate | date |  |  | SI | Created Date |
| OS_CreatedTime | time |  |  | SI | Created Time |
| OS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OS_Deceased | varchar |  |  | SI | Deceased |
| OS_OrdSet_DR | varchar |  | FK | SI | Des Ref ARCOrdSets |
| OS_OverMidnight | varchar |  |  | SI | Over Midnight |
| OS_RowId | varchar |  |  | NO | - |
| OS_TimeFrom | double |  |  | SI | TimeFrom |
| OS_TimeTo | double |  |  | SI | TimeTo |
| OS_UpdatedDate | date |  |  | SI | Updated Date |
| OS_UpdatedTime | time |  |  | SI | Updated Time |
| OS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date of event |
| Q04 | - |  |  | SI | Details of event |
| Q05 | - |  |  | SI | Instructions |
| Q06 | - |  |  | SI | Below is a list of difficulties people sometimes h... |
| Q07 | - |  |  | SI | Please read each item, and then indicate how distr... |
| Q08 | - |  |  | SI | How much have you been distressed or bothered by t... |
| Q09 | - |  |  | SI | 1. Any reminder brought back feelings about it |
| Q10 | - |  |  | SI | 2. I had trouble staying asleep |
| Q11 | - |  |  | SI | 3. Other things kept making me think about it |
| Q12 | - |  |  | SI | 4. I felt irritable and angry |
| Q13 | - |  |  | SI | 5. I avoided letting myself get upset when I thoug... |
| Q14 | - |  |  | SI | 6. I thought about it when I didn't mean to |
| Q15 | - |  |  | SI | 7. I felt as if it hadn't happened or wasn't real |
| Q16 | - |  |  | SI | 8. I stayed away from reminders of it |
| Q17 | - |  |  | SI | 9. Pictures about it popped into my mind |
| Q18 | - |  |  | SI | 10. I was jumpy and easily startled |
| Q19 | - |  |  | SI | 11. I tried not to think about it |
| Q20 | - |  |  | SI | 12. I was aware that I still had a lot of feelings... |
| Q21 | - |  |  | SI | 13. My feelings about it were kind of numb |
| Q22 | - |  |  | SI | 14. I found myself acting or feeling like I was ba... |
| Q23 | - |  |  | SI | 15. I had trouble falling asleep |
| Q24 | - |  |  | SI | 16. I had waves of strong feelings about it |
| Q25 | - |  |  | SI | 17. I tried to remove it from my memory |
| Q26 | - |  |  | SI | 18. I had trouble concentrating |
| Q27 | - |  |  | SI | 19. Reminders of it caused me to have physical rea... |
| Q28 | - |  |  | SI | 20. I had dreams about it |
| Q29 | - |  |  | SI | 21. I felt watchful and on guard |
| Q30 | - |  |  | SI | 22. I tried not to talk about it |
| Q31 | - |  |  | SI | Notes |
| Q32 | - |  |  | SI | Intrusion Subscore |
| Q33 | - |  |  | SI | Avoidance&nbsp |
| Q34 | - |  |  | SI | Hyper-arousal&nbsp |
| Q35 | - |  |  | SI | Total mean IES-R Score |
| Q36 | - |  |  | SI | Revised Impact of Event Scale (22 questions) |
| Q37 | - |  |  | SI | The revised version of the Impact of Event Scale (... |
| Q38 | - |  |  | SI | On this test, scores that exceed 24 can be quite m... |
| Q39 | - |  |  | SI | The IES-R is very helpful in measuring the affect ... |
| Q40 | - |  |  | SI | Sub Scale Questions |
| Q41 | - |  |  | SI | Avoidance Subscale = mean of items 5, 7, 8, 11, 12... |
| Q42 | - |  |  | SI | Intrusion Subscale = mean of items 1, 2, 3, 6, 9, ... |
| Q43 | - |  |  | SI | Hyper arousal Subscale = mean of items 4, 10, 14, ... |
| Q44 | - |  |  | SI | Total mean IES-R score = The mean of the Total IES... |
| Q45 | - |  |  | SI | Weiss D. The Impact of Event Scale - Revised. In: ... |
| Q46 | - |  |  | SI | Horowitz M, Wilner N, Alvarez W. Impact of Event S... |
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