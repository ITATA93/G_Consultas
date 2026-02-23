# questionnaire.QTCTIMEDAMT

> TIME Delirium Assessment and Management Tool

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* TIME Delirium Assessment and Management Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Initiate |
| Q04 | varchar |  |  | SI | TIME |
| Q05 | varchar |  |  | SI |  within 2 hours |
| Q06 | varchar |  |  | SI | Review observations |
| Q07 | varchar |  |  | SI | Think sepsis |
| Q08 | varchar |  |  | SI | Blood glucose |
| Q09 | varchar |  |  | SI | Medication history |
| Q10 | varchar |  |  | SI | Identify new medications / change of dose / medica... |
| Q11 | varchar |  |  | SI | Pain review (Abbey pain scale) |
| Q12 | varchar |  |  | SI | Alcohol history |
| Q13 | varchar |  |  | SI | Consider withdrawal / intoxication |
| Q14 | varchar |  |  | SI | Assess for urinary retention |
| Q15 | varchar |  |  | SI | Assess for constipation |
| Q16 | varchar |  |  | SI | Notes |
| Q17 | varchar |  |  | SI | Assess hydration and start fluid balance chart |
| Q18 | varchar |  |  | SI | Bloods |
| Q19 | varchar |  |  | SI | Full blood count, urea and electrolytes, liver fun... |
| Q20 | varchar |  |  | SI | Look for symptoms / signs of infection and perform... |
| Q21 | varchar |  |  | SI | Consider signs and symptoms: skin, chest, urine, c... |
| Q22 | varchar |  |  | SI | Electrocardiogram |
| Q23 | varchar |  |  | SI | Consider Acute Coronary Syndrome |
| Q24 | varchar |  |  | SI | Notes |
| Q25 | varchar |  |  | SI | Initiate treatment of all underlying causes found ... |
| Q26 | varchar |  |  | SI | Notes |
| Q27 | varchar |  |  | SI | Complete within 2 hours or if family / carer not p... |
| Q28 | varchar |  |  | SI | Engage with patient / family / carer – explore if ... |
| Q29 | varchar |  |  | SI | Ask: How would you like to be involved? |
| Q30 | varchar |  |  | SI | Explain diagnoses of delirium to patient and famil... |
| Q31 | varchar |  |  | SI | Document diagnosis of delirium |
| Q32 | varchar |  |  | SI | Notes |
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