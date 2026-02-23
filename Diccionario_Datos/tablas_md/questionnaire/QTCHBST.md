# questionnaire.QTCHBST

> Home Birth Screening Tool

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Home Birth Screening Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Gravida |
| Q04 | varchar |  |  | SI | Para |
| Q05 | numeric |  |  | SI | Gestation |
| Q06 | varchar |  |  | SI | weeks |
| Q07 | numeric |  |  | SI | Gestation (days) |
| Q08 | varchar |  |  | SI | days |
| Q09 | varchar |  |  | SI | Estimated birth due date |
| Q10 | varchar |  |  | SI | Age >18 and < 42 years |
| Q11 | varchar |  |  | SI | Body Mass Index (BMI) at booking (> 20 weeks) is >... |
| Q12 | varchar |  |  | SI | Has ambulance cover, or agrees to obtain it |
| Q13 | varchar |  |  | SI | Eligible for health insurance cover, or prepared t... |
| Q14 | varchar |  |  | SI | Lives within the acceptable defined boundary of th... |
| Q15 | varchar |  |  | SI | Access to clear running water |
| Q16 | varchar |  |  | SI | Access to electricity |
| Q17 | varchar |  |  | SI | Adequate heating |
| Q18 | varchar |  |  | SI | Adequate lighting |
| Q19 | varchar |  |  | SI | Home birth location is hygienic |
| Q20 | varchar |  |  | SI | Access to phone with signal |
| Q21 | varchar |  |  | SI | Adequate vehicle access to property |
| Q22 | varchar |  |  | SI | Patient agrees to the 'Homebirth Terms of Care Agr... |
| Q23 | varchar |  |  | SI | Screening notes |
| Q24 | varchar |  |  | SI | Previous Obstetric History Exclusions |
| Q25 | varchar |  |  | SI | History of caesarean section or uterine surgery / ... |
| Q26 | varchar |  |  | SI | History of postpartum haemorrhage (PPH) |
| Q27 | varchar |  |  | SI | History of shoulder dystocia requiring internal ma... |
| Q28 | varchar |  |  | SI | History of manual removal of placenta |
| Q29 | varchar |  |  | SI | History of perinatal death of a viable baby |
| Q30 | varchar |  |  | SI | Previous baby with Group B Streptococcus (GBS) neo... |
| Q31 | varchar |  |  | SI | Current Pregnancy Exclusions |
| Q32 | varchar |  |  | SI | Medical, obstetric, surgical or social history con... |
| Q33 | varchar |  |  | SI | Multiple pregnancy |
| Q34 | varchar |  |  | SI | Abnormalities of maternal serum screening associat... |
| Q35 | varchar |  |  | SI | Diabetes mellitus (type 1, 2  or gestational), hyp... |
| Q36 | varchar |  |  | SI | Antenatal risk factors that require continuous fet... |
| Q37 | varchar |  |  | SI | Uncorrected female genital mutilation |
| Q38 | varchar |  |  | SI | Social Determinants of Health Exclusions |
| Q39 | varchar |  |  | SI | Domestic or family violence |
| Q40 | varchar |  |  | SI | Alcohol and/or drug dependency of woman and/or a f... |
| Q41 | varchar |  |  | SI | Newborn or child at risk of harm |
| Q42 | varchar |  |  | SI | Eligible for a home birth |
| Q43 | varchar |  |  | SI | Patient has signed 'Homebirth Terms of Care Agreem... |
| Q44 | varchar |  |  | SI | Not eligible - rationale given and alternative opt... |
| Q45 | varchar |  |  | SI | Outcome notes |
| Q46 | varchar |  |  | SI | Actions |
| Q47 | varchar |  |  | SI | Actions taken |
| Q48 | varchar |  |  | SI | Other actions |
| Q49 | varchar |  |  | SI | Obstetrician Review |
| Q50 | varchar |  |  | SI | Specialist obstetrician comment |
| Q51 | varchar |  |  | SI | Obstetrician name |
| Q52 | varchar |  |  | SI | Medical, obstetric, surgical or social history con... |
| Q53 | varchar |  |  | SI | Abnormalities of maternal serum screening associat... |
| Q54 | varchar |  |  | SI | Dummy1 |
| Q55 | varchar |  |  | SI | Dummy2 |
| Q56 | varchar |  |  | SI | Dummy3 |
| Q57 | varchar |  |  | SI | Para |
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