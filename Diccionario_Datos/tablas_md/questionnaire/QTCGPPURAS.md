# questionnaire.QTCGPPURAS

> Glamorgan Paediatric Pressure Ulcer Risk Assessment Scale (2008 version)

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Glamorgan Paediatric Pressure Ulcer Risk Assessment Scale (2008 version)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Complete for all patients on admission only (best ... |
| Q04 | varchar |  |  | SI | Conduct malnutrition screening |
| Q05 | varchar |  |  | SI | Comprehensive initial skin inspection |
| Q06 | varchar |  |  | SI | Provide pressure injury prevention information and... |
| Q07 | varchar |  |  | SI | If pressure injury present, commence wound chart a... |
| Q08 | varchar |  |  | SI | If patient has had a previous pressure injury they... |
| Q09 | varchar |  |  | SI | If data such as serum albumin or haemoglobin is no... |
| Q10 | varchar |  |  | SI | Glamorgan Paediatric Pressure Ulcer Risk Assessmen... |
| Q11 | varchar |  |  | SI | Notes |
| Q12 | varchar |  |  | SI | Action taken |
| Q13 | varchar |  |  | SI | Action taken details |
| Q14 | varchar |  |  | SI | 1. Willock J, Baharestani MM, Anthony D. The devel... |
| Q15 | varchar |  |  | SI | 2. Willock J, Anthony D, Richardson J. Inter-rater... |
| Q16 | varchar |  |  | SI | AT RISK 10+ |
| Q17 | varchar |  |  | SI | (ALL NEONATAES ARE AT RISK I.E. RISK SCORE 10+) |
| Q18 | varchar |  |  | SI | • Inspect skin at least twice a day |
| Q19 | varchar |  |  | SI | • Relieve pressure by helping child to move at lea... |
| Q20 | varchar |  |  | SI | • Use age and weight appropriate pressure redistri... |
| Q21 | varchar |  |  | SI | Dummy1 |
| Q22 | varchar |  |  | SI | HIGH RISK 15+ |
| Q23 | varchar |  |  | SI | • Inspect skin with each positioning |
| Q24 | varchar |  |  | SI | • Reposition child / equipment / devices at least ... |
| Q25 | varchar |  |  | SI | • Relieve pressure before any skin redness develop... |
| Q26 | varchar |  |  | SI | • Use an age and weight appropriate pressure redis... |
| Q27 | varchar |  |  | SI | Dummy2 |
| Q28 | varchar |  |  | SI | Dummy3 |
| Q29 | varchar |  |  | SI | SEVERE RISK 20+ |
| Q30 | varchar |  |  | SI | Inspect skin at least hourly |
| Q31 | varchar |  |  | SI | Move or turn if possible, before skin becomes red |
| Q32 | varchar |  |  | SI | Ensure equipment / objects are not pressing on the... |
| Q33 | varchar |  |  | SI | Consider using specialised pressure relieving equi... |
| Q34 | varchar |  |  | SI | Dummy4 |
| Q35 | varchar |  |  | SI | Dummy5 |
| Q36 | varchar |  |  | SI | Dummy6 |
| Q37 | varchar |  |  | SI | Dummy7 |
| Q38 | varchar |  |  | SI | Glamorgan Paediatric Pressure Ulcer Risk Assessmen... |
| Q39 | varchar |  |  | SI | Children who are at risk of pressure ulcers need t... |
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