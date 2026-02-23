# questionnaire.QTCROBSON17

> Robson classification (WHO, 2017)

**Schema:** questionnaire
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Robson classification (WHO, 2017)

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
| Q12 | varchar |  |  | SI | Classification |
| Q13 | varchar |  |  | SI | Group 1 - Nulliparous women with a single cephalic... |
| Q14 | varchar |  |  | SI | Group 2 - Nulliparous women with a single cephalic... |
| Q15 | varchar |  |  | SI | Group 2a - Nulliparous women with a single cephali... |
| Q16 | varchar |  |  | SI | Group 2b - Nulliparous women with a single cephali... |
| Q17 | varchar |  |  | SI | Group 3 - Multiparous women without a previous cae... |
| Q18 | varchar |  |  | SI | Group 4 - Multiparous women without a previous cae... |
| Q19 | varchar |  |  | SI | Group 4a - Multiparous women without a previous ca... |
| Q20 | varchar |  |  | SI | Group 4b - Multiparous women without a previous ca... |
| Q21 | varchar |  |  | SI | Group 5 - All multiparous women with at least one ... |
| Q22 | varchar |  |  | SI | Group 5.1 - All multiparous women with one previou... |
| Q23 | varchar |  |  | SI | Group 5.2 - All multiparous women with two or more... |
| Q24 | varchar |  |  | SI | Group 6 - All nulliparous women with a single bree... |
| Q25 | varchar |  |  | SI | Group 7 - All multiparous women with a single bree... |
| Q26 | varchar |  |  | SI | Group 8 - All women with multiple pregnancies incl... |
| Q27 | varchar |  |  | SI | Group 9 - All women with a single pregnancy with a... |
| Q28 | varchar |  |  | SI | Group 10 - All women with a single cephalic pregna... |
| Q29 | varchar |  |  | SI | WHO proposes the Robson Classification system as a... |
| Q30 | varchar |  |  | SI | The Robson Classification should be considered as ... |
| Q31 | varchar |  |  | SI | Please find details on each group category in the ... |
| Q32 | varchar |  |  | SI | Score 1 |
| Q33 | varchar |  |  | SI | Group 1 - Nulliparous women with a single cephalic... |
| Q34 | varchar |  |  | SI | Score 2 |
| Q35 | varchar |  |  | SI | Group 2 - Nulliparous women with a single cephalic... |
| Q36 | varchar |  |  | SI | Score 3 |
| Q37 | varchar |  |  | SI | Group 3 - Multiparous women without a previous cae... |
| Q38 | varchar |  |  | SI | Score 4 |
| Q39 | varchar |  |  | SI | Group 4 - Multiparous women without a previous cae... |
| Q40 | varchar |  |  | SI | Score 5 |
| Q41 | varchar |  |  | SI | Group 5 - All multiparous women with at least one ... |
| Q42 | varchar |  |  | SI | Score 6 |
| Q43 | varchar |  |  | SI | Group 6 - All nulliparous women with a single bree... |
| Q44 | varchar |  |  | SI | Score 7 |
| Q45 | varchar |  |  | SI | Group 7 - All multiparous women with a single bree... |
| Q46 | varchar |  |  | SI | Score 8 |
| Q47 | varchar |  |  | SI | Group 8 - All women with multiple pregnancies incl... |
| Q48 | varchar |  |  | SI | Score 9 |
| Q49 | varchar |  |  | SI | Group 9 - All women with a single pregnancy with a... |
| Q50 | varchar |  |  | SI | Score 10 |
| Q51 | varchar |  |  | SI | Group 10 - All women with a single cephalic pregna... |
| Q52 | varchar |  |  | SI | Score 21 |
| Q53 | varchar |  |  | SI | Group 2a - Nulliparous women with a single cephali... |
| Q54 | varchar |  |  | SI | Score 22 |
| Q55 | varchar |  |  | SI | Group 2b - Nulliparous women with a single cephali... |
| Q56 | varchar |  |  | SI | Score 41 |
| Q57 | varchar |  |  | SI | Group 4a - Multiparous women without a previous ca... |
| Q58 | varchar |  |  | SI | Score 42 |
| Q59 | varchar |  |  | SI | Group 4b - Multiparous women without a previous ca... |
| Q60 | varchar |  |  | SI | Score 51 |
| Q61 | varchar |  |  | SI | Group 5.1 - All multiparous women with one previou... |
| Q62 | varchar |  |  | SI | Score 52 |
| Q63 | varchar |  |  | SI | Group 5.2 - All multiparous women with two or more... |
| Q64 | varchar |  |  | SI | ≥37 weeks gestation who had labour induced or were... |
| Q65 | varchar |  |  | SI | ≥37 weeks gestation in spontaneous labour |
| Q66 | varchar |  |  | SI | ≥37 weeks gestation who had labour induced or were... |
| Q67 | varchar |  |  | SI | ≥37 weeks gestation who had labour induced |
| Q68 | varchar |  |  | SI | ≥37 weeks gestation who were delivered by caesarea... |
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