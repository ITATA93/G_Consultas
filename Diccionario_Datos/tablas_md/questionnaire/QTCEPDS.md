# questionnaire.QTCEPDS

> Edinburgh Postnatal Depression Scale

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Edinburgh Postnatal Depression Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ27 | varchar |  |  | SI | - |
| Q01 | varchar |  |  | SI | I have been able to laugh and see the funny side o... |
| Q02 | varchar |  |  | SI | I have looked forward with enjoyment to things |
| Q03 | varchar |  |  | SI | I have blamed myself unnecessarily when things wen... |
| Q04 | varchar |  |  | SI | I have been anxious or worried for no good reason |
| Q05 | varchar |  |  | SI | I have felt scared or panicky for no very good rea... |
| Q06 | varchar |  |  | SI | Things have been getting on top of me |
| Q07 | varchar |  |  | SI | I have been so unhappy that I have had difficulty ... |
| Q08 | varchar |  |  | SI | I have felt sad or miserable |
| Q09 | varchar |  |  | SI | I have been so unhappy that I have been crying |
| Q10 | varchar |  |  | SI | The thought of harming myself has occurred to me |
| Q11 | varchar |  |  | SI | Enquire further and ensure safety |
| Q19 | varchar |  |  | SI | Score |
| Q20 | varchar |  |  | SI | Classification |
| Q21 | varchar |  |  | SI | Possible Depression |
| Q22 | varchar |  |  | SI | >=10: Possible Depression |
| Q23 | varchar |  |  | SI | 0 - 9: Normal |
| Q24 | varchar |  |  | SI | 30: Maximum score |
| Q25 | date |  |  | SI | Date |
| Q26 | time |  |  | SI | Time |
| Q27 | varchar |  |  | SI | Period |
| Q28 | numeric |  |  | SI | Gestation at time of assessment |
| Q29 | varchar |  |  | SI | weeks |
| Q30 | varchar |  |  | SI | + |
| Q31 | numeric |  |  | SI | Days of gestation |
| Q32 | varchar |  |  | SI | days |
| Q33 | numeric |  |  | SI | Period of time post birth |
| Q34 | varchar |  |  | SI | Time factor |
| Q35 | varchar |  |  | SI | Clinical judgement is integral to interpreting EPD... |
| Q36 | varchar |  |  | SI | For example, a woman may have a low score, even th... |
| Q37 | varchar |  |  | SI | A very high EPDS score could suggest a crisis, oth... |
| Q38 | varchar |  |  | SI | Scores may be influenced by several factors, inclu... |
| Q39 | varchar |  |  | SI | their fear of the consequences if depression is id... |
| Q40 | varchar |  |  | SI | Follow-Up Care |
| Q41 | varchar |  |  | SI | A total score of 13 or more is considered a flag f... |
| Q42 | varchar |  |  | SI | In the antenatal period, repeat the EPDS in 2-4 we... |
| Q43 | varchar |  |  | SI | If the second EPDS score is 13 or more, refer to a... |
| Q44 | varchar |  |  | SI | In the postnatal period, arrange referral or ongoi... |
| Q45 | varchar |  |  | SI | Follow-up may also be needed if scores on Question... |
| Q46 | varchar |  |  | SI | For scores of 1, 2 or 3 on Question 10, the safety... |
| Q47 | varchar |  |  | SI | Dummy 1 |
| Q48 | varchar |  |  | SI | Dummy 2 |
| Q49 | varchar |  |  | SI | Dummy 3 |
| QINS1 | varchar |  |  | SI | As you are pregnant or have recently had a baby, w... |
| QL12 | varchar |  |  | SI | Postpartum depression is the most common complicat... |
| QL13 | varchar |  |  | SI | The 10-question scale  is a valuable and efficient... |
| QL14 | varchar |  |  | SI | The EPDS is easy to administer and has proven to b... |
| QSCORE01 | varchar |  |  | SI | Maximum score: 30 |
| QSCORE02 | varchar |  |  | SI | Possible Depression: ≥10 |
| QSCORE03 | varchar |  |  | SI | Always look at item 10 (Suicidal thoughts) |
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