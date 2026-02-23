# questionnaire.QGXXXALCOHO

> Alcohol Assessment

**Schema:** questionnaire
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Alcohol Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Personal questions concerning alcohol consumption |
| Q02 | varchar |  |  | SI | Answer these questions to find out how much alcoho... |
| Q03 | varchar |  |  | SI | Mark the response which is closest to your own sit... |
| Q04 | varchar |  |  | SI | How often do you have a drink containing alcohol? |
| Q05 | varchar |  |  | SI | How many drinks do you have on a typical day when ... |
| Q06 | varchar |  |  | SI | How often do you have six or more drinks on one oc... |
| Q07 | varchar |  |  | SI | During the last year how often have you found that... |
| Q08 | varchar |  |  | SI | During the last year how often have you failed to ... |
| Q09 | varchar |  |  | SI | During the last year how often have you needed a f... |
| Q10 | varchar |  |  | SI | During the last year how often have you been unabl... |
| Q11 | varchar |  |  | SI | Have you or has someone else been injured as a res... |
| Q12 | varchar |  |  | SI | Has a relative, a friend, a doctor or other health... |
| Q13 | varchar |  |  | SI |  0 -  7: Low |
| Q14 | varchar |  |  | SI |  8 - 10: Slightly increased |
| Q15 | varchar |  |  | SI | 11 - 14: Noticeably increased |
| Q16 | varchar |  |  | SI | 15 - 19: High |
| Q17 | varchar |  |  | SI | 20 - 40: Very high |
| Q18 | varchar |  |  | SI | Is it time to make a change? If your risks are ele... |
| Q19 | varchar |  |  | SI | Take a moment to think about how you could change ... |
| Q20 | varchar |  |  | SI | Are you alarmed by your test results? Remember tha... |
| Q21 | varchar |  |  | SI | If you decide to moderate your drinking or quit al... |
| Q22 | varchar |  |  | SI | Consult an expert – you have a right to know! Espe... |
| Q23 | varchar |  |  | SI | Find out how alcohol is affecting you and your hea... |
| Q24 | varchar |  |  | SI | One bottle |
| Q25 | varchar |  |  | SI | One standard drink: |
| Q26 | varchar |  |  | SI | (33 cl) of medium beer or cider (max 4.7% vol.) |
| Q27 | varchar |  |  | SI | One glass |
| Q28 | varchar |  |  | SI | (12 cl) of table wine (12% vol.) |
| Q29 | varchar |  |  | SI | One small glass |
| Q30 | varchar |  |  | SI | (8 cl) of fortified wine (16-22% vol.) |
| Q31 | varchar |  |  | SI | One restaurant measure |
| Q32 | varchar |  |  | SI | (4 cl) of spirits (35-40% vol.) |
| Q33 | varchar |  |  | SI | Examples |
| Q34 | varchar |  |  | SI | 0.5 l of medium beer cider equals: 1.5	units (max ... |
| Q35 | varchar |  |  | SI | 0.5 l of strong beer or cider equals: 2 units (5-8... |
| Q36 | varchar |  |  | SI | 0.75 l bottle of table wine equals: 6 units (12% v... |
| Q37 | varchar |  |  | SI | 0.5 l bottle of spirits equals: 13 units (35-40% v... |
| Q38 | varchar |  |  | SI | How much? |
| Q39 | varchar |  |  | SI | Did you overdo it? |
| Q40 | varchar |  |  | SI | Work left undone? |
| Q41 | varchar |  |  | SI | Do you have to jump-start your day? |
| Q42 | varchar |  |  | SI | Did you feel bad in the morning? |
| Q43 | varchar |  |  | SI | Blackout? |
| Q44 | varchar |  |  | SI | Did you hurt yourself or others? |
| Q45 | varchar |  |  | SI | Has anyone said anything about your drinking? |
| Q46 | date |  |  | SI | Date |
| Q47 | varchar |  |  | SI | During the last year how often have you had a feel... |
| Q48 | varchar |  |  | SI | Score |
| Q49 | varchar |  |  | SI | Is the attendance/admission directly due to alcoho... |
| Q50 | varchar |  |  | SI | Does patient give consent to answer the assessment... |
| Q51 | varchar |  |  | SI | Brief advice given, and patient informed of follow... |
| Q52 | varchar |  |  | SI | Has the patient refused further follow-up from Alc... |
| Q53 | varchar |  |  | SI | 0 - 7 |
| Q54 | varchar |  |  | SI | Low |
| Q55 | varchar |  |  | SI | 8 - 10 |
| Q56 | varchar |  |  | SI | Slightly increased |
| Q57 | varchar |  |  | SI | 11 - 14 |
| Q58 | varchar |  |  | SI | Noticeably increased |
| Q59 | varchar |  |  | SI | 15 - 19 |
| Q60 | varchar |  |  | SI | High |
| Q61 | varchar |  |  | SI | 20 - 40 |
| Q62 | varchar |  |  | SI | Very high |
| Q63 | varchar |  |  | SI | Score |
| Q64 | varchar |  |  | SI | Classification |
| Q65 | time |  |  | SI | Time |
| Q66 | varchar |  |  | SI | Table with Standards drinks |
| Q67 | varchar |  |  | SI | Time to make a change |
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