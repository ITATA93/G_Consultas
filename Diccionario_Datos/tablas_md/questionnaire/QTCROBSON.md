# questionnaire.QTCROBSON

> Robson Classification

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Robson Classification

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Is this a multiple pregnancy? |
| Q04 | varchar |  |  | SI | Transverse or oblique lie? |
| Q05 | varchar |  |  | SI | Single cephalic pregnancy < 37 weeks gestation? |
| Q06 | varchar |  |  | SI | Is the woman nulliparous? |
| Q07 | varchar |  |  | SI | Is this a breech pregnancy? |
| Q08 | varchar |  |  | SI | Spontaneous labour? |
| Q09 | varchar |  |  | SI | Is this a breech pregnancy? |
| Q10 | varchar |  |  | SI | Previous uterine scars? |
| Q11 | varchar |  |  | SI | Spontaneous labour? |
| Q12 | varchar |  |  | SI | Score |
| Q13 | varchar |  |  | SI | Classification |
| Q14 | varchar |  |  | SI | 1 |
| Q15 | varchar |  |  | SI | Group 1 - Nulliparous women with a single cephalic... |
| Q16 | varchar |  |  | SI | 2 |
| Q17 | varchar |  |  | SI | Group 2 - Nulliparous women with a single cephalic... |
| Q18 | varchar |  |  | SI | 3 |
| Q19 | varchar |  |  | SI | Group 3 - Multiparous women without a previous CS,... |
| Q20 | varchar |  |  | SI | 4 |
| Q21 | varchar |  |  | SI | Group 4 - Multiparous women without a previous CS,... |
| Q22 | varchar |  |  | SI | 5 |
| Q23 | varchar |  |  | SI | Group 5 - All multiparous women with at least one ... |
| Q24 | varchar |  |  | SI | 6 |
| Q25 | varchar |  |  | SI | Group 6 - All nulliparous women with a single bree... |
| Q26 | varchar |  |  | SI | 7 |
| Q27 | varchar |  |  | SI | Group 7 - All multiparous women with a single bree... |
| Q28 | varchar |  |  | SI | 8 |
| Q29 | varchar |  |  | SI | Group 8 - All women with multiple pregnancies incl... |
| Q30 | varchar |  |  | SI | 9 |
| Q31 | varchar |  |  | SI | Group 9 - All women with a single pregnancy with a... |
| Q32 | varchar |  |  | SI | 10 |
| Q33 | varchar |  |  | SI | Group 10 - All women with a single cephalic pregna... |
| Q34 | varchar |  |  | SI | 1: Group 1 - Nulliparous women with a single cepha... |
| Q35 | varchar |  |  | SI | 2: Group 2 - Nulliparous women with a single cepha... |
| Q36 | varchar |  |  | SI | 3: Group 3 - Multiparous women without a previous ... |
| Q37 | varchar |  |  | SI | 4: Group 4 - Multiparous women without a previous ... |
| Q38 | varchar |  |  | SI | 5: Group 5 - All multiparous women with at least o... |
| Q39 | varchar |  |  | SI | 6: Group 6 - All nulliparous women with a single b... |
| Q40 | varchar |  |  | SI | 7: Group 7 - All multiparous women with a single b... |
| Q41 | varchar |  |  | SI | 8: Group 8 - All women with multiple pregnancies i... |
| Q42 | varchar |  |  | SI | 9: Group 9 - All women with a single pregnancy wit... |
| Q43 | varchar |  |  | SI | 10: Group 10 - All women with a single cephalic pr... |
| Q44 | varchar |  |  | SI | The system classifies all women into one of 10 cat... |
| Q45 | varchar |  |  | SI | The categories are based on 5 basic obstetric char... |
| Q46 | varchar |  |  | SI | (parity, number of foetuses, previous caesarean se... |
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