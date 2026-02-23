# questionnaire.QGXXXBARTHE

> Barthel Index

**Schema:** questionnaire
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Barthel Index

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | varchar |  |  | SI | Feeding |
| Q03 | varchar |  |  | SI | Bathing |
| Q04 | varchar |  |  | SI | Grooming |
| Q05 | varchar |  |  | SI | Dressing |
| Q06 | varchar |  |  | SI | Bowels |
| Q07 | varchar |  |  | SI | Bladder |
| Q08 | varchar |  |  | SI | Toilet use |
| Q09 | varchar |  |  | SI | Transfers (bed to chair and back) |
| Q10 | varchar |  |  | SI | Mobility (on level surfaces) |
| Q11 | varchar |  |  | SI | Stairs |
| Q12 | varchar |  |  | SI | 0 - 20: Total dependency |
| Q13 | varchar |  |  | SI | 21 - 60: Severe dependency |
| Q14 | varchar |  |  | SI | 61 - 90: Moderate dependency |
| Q15 | varchar |  |  | SI | 91 - 99: Slight dependency |
| Q16 | varchar |  |  | SI | The Barthel scale is a scale used to measure perfo... |
| Q17 | varchar |  |  | SI | General |
| Q18 | varchar |  |  | SI | • The Index should be used as a record of what a p... |
| Q19 | varchar |  |  | SI | • The main aim is to establish degree of independe... |
| Q20 | varchar |  |  | SI | • The need for supervision renders the patient not... |
| Q21 | varchar |  |  | SI | • A patient's performance should be established us... |
| Q22 | varchar |  |  | SI | friends / relatives, and nurses will be the usual ... |
| Q23 | varchar |  |  | SI | • Usually the performance over the preceding 24 – ... |
| Q24 | varchar |  |  | SI | • Unconscious patients should score '0' throughout... |
| Q25 | varchar |  |  | SI | • Middle categories imply that the patient supplie... |
| Q26 | varchar |  |  | SI | • Use of aids to be independent is allowed. |
| Q27 | varchar |  |  | SI | Bowels (preceding week)  |
| Q28 | varchar |  |  | SI | • If needs enema from nurse, then 'incontinent'. |
| Q29 | varchar |  |  | SI | • 'Occasional' = once a week. |
| Q30 | varchar |  |  | SI | Bladder (preceding week)  |
| Q31 | varchar |  |  | SI | • 'Occasional' = less than once a day. |
| Q32 | varchar |  |  | SI | • A catheterized patient who can completely manage... |
| Q33 | varchar |  |  | SI | Grooming (preceding 24 – 48 hours) |
| Q34 | varchar |  |  | SI | • Refers to personal hygiene: doing teeth, fitting... |
| Q35 | varchar |  |  | SI | Toilet use |
| Q36 | varchar |  |  | SI | • Should be able to reach toilet / commode, undres... |
| Q37 | varchar |  |  | SI | • 'With help' = can wipe self and do some other of... |
| Q38 | varchar |  |  | SI | Feeding |
| Q39 | varchar |  |  | SI | • Able to eat any normal food (not only soft food)... |
| Q40 | varchar |  |  | SI | • 'Help' = food cut up, patient feeds self. |
| Q41 | varchar |  |  | SI | Transfer |
| Q42 | varchar |  |  | SI | • From bed to chair and back. |
| Q43 | varchar |  |  | SI | • 'Dependent' = NO sitting balance (unable to sit)... |
| Q44 | varchar |  |  | SI | • 'Major help' = one strong / skilled, or two norm... |
| Q45 | varchar |  |  | SI | • 'Minor help' = one person easily, OR needs any s... |
| Q46 | varchar |  |  | SI | Mobility |
| Q47 | varchar |  |  | SI | • Refers to mobility about house or ward, indoors.... |
| Q48 | varchar |  |  | SI | • 'Help' = by one untrained person, including supe... |
| Q49 | varchar |  |  | SI | • 'Help' = by one untrained person, including supe... |
| Q50 | varchar |  |  | SI | Dressing |
| Q51 | varchar |  |  | SI | • Should be able to select and put on all clothes,... |
| Q52 | varchar |  |  | SI | • Should be able to select and put on all clothes,... |
| Q53 | varchar |  |  | SI | • 'Half' = help with buttons, zips, etc., but can ... |
| Q54 | varchar |  |  | SI | Stairs |
| Q55 | varchar |  |  | SI | • Must carry any walking aid used to be independen... |
| Q56 | varchar |  |  | SI | Bathing |
| Q57 | varchar |  |  | SI | • Usually the most difficult activity. |
| Q58 | varchar |  |  | SI | • Must get in and out unsupervised, and wash self. |
| Q59 | varchar |  |  | SI | • Independent in shower = 'independent' if unsuper... |
| Q60 | time |  |  | SI | Time |
| Q61 | varchar |  |  | SI | 0 - 20 |
| Q62 | varchar |  |  | SI | Total dependency |
| Q63 | varchar |  |  | SI | 21 - 60 |
| Q64 | varchar |  |  | SI | Severe dependency |
| Q65 | varchar |  |  | SI | 61 - 90 |
| Q66 | varchar |  |  | SI | Moderate dependency |
| Q67 | varchar |  |  | SI | 91 - 99 |
| Q68 | varchar |  |  | SI | Slight dependency |
| Q69 | varchar |  |  | SI | Score |
| Q70 | varchar |  |  | SI | Classification |
| Q71 | varchar |  |  | SI | 100: Complete independency |
| Q72 | varchar |  |  | SI | 100 |
| Q73 | varchar |  |  | SI | Complete independency |
| Q74 | varchar |  |  | SI | Comment |
| Q75 | varchar |  |  | SI | Mahoney FI, Barthel DW. Barthel index. Maryland st... |
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