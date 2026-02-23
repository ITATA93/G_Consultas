# SQLUser.CT_Modules

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MOD_RowId | bigint | PK |  | NO | - |
| MOD_Code | varchar |  |  | NO | Modules Code |
| MOD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MOD_CreatedDate | date |  |  | SI | Created Date |
| MOD_CreatedTime | time |  |  | SI | Created Time |
| MOD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MOD_Desc | varchar |  |  | NO | Modules Description |
| MOD_Owner | varchar |  |  | SI | Owner |
| MOD_UpdatedDate | date |  |  | SI | Updated Date |
| MOD_UpdatedTime | time |  |  | SI | Updated Time |
| MOD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | History of severe organ failure (heart failure cla... |
| Q02 | - |  |  | SI | Type of surgery |
| Q03 | - |  |  | SI | Age |
| Q04 | - |  |  | SI | Temperature, °C |
| Q05 | - |  |  | SI | Mean arterial pressure, mmHg |
| Q06 | - |  |  | SI | Heart rate, beats per minute |
| Q07 | - |  |  | SI | Respiratory rate, breaths per minute |
| Q08 | - |  |  | SI | Oxygenation (use PaO2 if FiO2 < 50%, otherwise use... |
| Q09 | - |  |  | SI | Arterial pH |
| Q10 | - |  |  | SI | Serum sodium, mmol/L |
| Q11 | - |  |  | SI | Serum potassium, mmol/L |
| Q12 | - |  |  | SI | Serum creatinine, mg/100 mL |
| Q13 | - |  |  | SI | Hematocrit, % |
| Q14 | - |  |  | SI | White blood count, total / cubic mm in 1000s |
| Q15 | - |  |  | SI | Glasgow Coma Scale (GCS) |
| Q16 | - |  |  | SI | Score |
| Q17 | - |  |  | SI | Classification |
| Q18 | - |  |  | SI | 0 - 4 |
| Q19 | - |  |  | SI | Nonoperative (4%) |
| Q20 | - |  |  | SI | 5 - 9 |
| Q21 | - |  |  | SI | Nonoperative (8%) |
| Q22 | - |  |  | SI | 10 - 14 |
| Q23 | - |  |  | SI | Nonoperative (15%) |
| Q24 | - |  |  | SI | 15 - 19 |
| Q25 | - |  |  | SI | Nonoperative (25%) |
| Q26 | - |  |  | SI | 20 - 24 |
| Q27 | - |  |  | SI | Nonoperative (40%) |
| Q28 | - |  |  | SI | 25 - 29 |
| Q29 | - |  |  | SI | Nonoperative (55%) |
| Q30 | - |  |  | SI | 30 - 34 |
| Q31 | - |  |  | SI | Nonoperative (73%) |
| Q32 | - |  |  | SI | > 34 |
| Q33 | - |  |  | SI | Nonoperative (85%) |
| Q34 | - |  |  | SI | 0 - 4: Nonoperative (4%) |
| Q35 | - |  |  | SI | 5 - 9:  Nonoperative (8%) |
| Q36 | - |  |  | SI | 10 - 14:  Nonoperative (15%) |
| Q37 | - |  |  | SI | 15 - 19: Nonoperative (25%) |
| Q38 | - |  |  | SI | 20 - 24: Nonoperative (40%) |
| Q39 | - |  |  | SI | 25 - 29: Nonoperative (55%) |
| Q40 | - |  |  | SI | 30 - 34: Nonoperative (73%) |
| Q41 | - |  |  | SI | > 34: Nonoperative (85%) |
| Q42 | - |  |  | SI | The APACHE II score was designed as a mortality pr... |
| Q43 | - |  |  | SI | Date |
| Q44 | - |  |  | SI | Time |
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