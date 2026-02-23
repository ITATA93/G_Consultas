# SQLUser.PAC_AccessToService

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACCSER_RowId | bigint | PK |  | NO | - |
| ACCSER_Code | varchar |  |  | NO | Code |
| ACCSER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACCSER_CreatedDate | date |  |  | SI | Created Date |
| ACCSER_CreatedTime | time |  |  | SI | Created Time |
| ACCSER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACCSER_DateFrom | date |  |  | SI | DateFrom |
| ACCSER_DateTo | date |  |  | SI | DateTo |
| ACCSER_Desc | varchar |  |  | NO | Description |
| ACCSER_Owner | varchar |  |  | SI | Owner |
| ACCSER_UpdatedDate | date |  |  | SI | Updated Date |
| ACCSER_UpdatedTime | time |  |  | SI | Updated Time |
| ACCSER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Complete for all patients on admission only (best ... |
| Q04 | - |  |  | SI | Conduct malnutrition screening |
| Q05 | - |  |  | SI | Comprehensive initial skin inspection |
| Q06 | - |  |  | SI | Provide pressure injury prevention information and... |
| Q07 | - |  |  | SI | If pressure injury present, commence wound chart a... |
| Q08 | - |  |  | SI | If patient has had a previous pressure injury they... |
| Q09 | - |  |  | SI | If data such as serum albumin or haemoglobin is no... |
| Q10 | - |  |  | SI | Glamorgan Paediatric Pressure Ulcer Risk Assessmen... |
| Q11 | - |  |  | SI | Notes |
| Q12 | - |  |  | SI | Action taken |
| Q13 | - |  |  | SI | Action taken details |
| Q14 | - |  |  | SI | 1. Willock J, Baharestani MM, Anthony D. The devel... |
| Q15 | - |  |  | SI | 2. Willock J, Anthony D, Richardson J. Inter-rater... |
| Q16 | - |  |  | SI | AT RISK 10+ |
| Q17 | - |  |  | SI | (ALL NEONATAES ARE AT RISK I.E. RISK SCORE 10+) |
| Q18 | - |  |  | SI | • Inspect skin at least twice a day |
| Q19 | - |  |  | SI | • Relieve pressure by helping child to move at lea... |
| Q20 | - |  |  | SI | • Use age and weight appropriate pressure redistri... |
| Q21 | - |  |  | SI | Dummy1 |
| Q22 | - |  |  | SI | HIGH RISK 15+ |
| Q23 | - |  |  | SI | • Inspect skin with each positioning |
| Q24 | - |  |  | SI | • Reposition child / equipment / devices at least ... |
| Q25 | - |  |  | SI | • Relieve pressure before any skin redness develop... |
| Q26 | - |  |  | SI | • Use an age and weight appropriate pressure redis... |
| Q27 | - |  |  | SI | Dummy2 |
| Q28 | - |  |  | SI | Dummy3 |
| Q29 | - |  |  | SI | SEVERE RISK 20+ |
| Q30 | - |  |  | SI | Inspect skin at least hourly |
| Q31 | - |  |  | SI | Move or turn if possible, before skin becomes red |
| Q32 | - |  |  | SI | Ensure equipment / objects are not pressing on the... |
| Q33 | - |  |  | SI | Consider using specialised pressure relieving equi... |
| Q34 | - |  |  | SI | Dummy4 |
| Q35 | - |  |  | SI | Dummy5 |
| Q36 | - |  |  | SI | Dummy6 |
| Q37 | - |  |  | SI | Dummy7 |
| Q38 | - |  |  | SI | Glamorgan Paediatric Pressure Ulcer Risk Assessmen... |
| Q39 | - |  |  | SI | Children who are at risk of pressure ulcers need t... |
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