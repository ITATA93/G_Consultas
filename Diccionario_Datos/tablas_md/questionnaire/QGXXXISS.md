# questionnaire.QGXXXISS

> Insulin Sliding Scale

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Insulin Sliding Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Insulin Type |
| Q02 | varchar |  |  | SI | Brand: |
| Q03 | varchar |  |  | SI | Brand: |
| Q04 | varchar |  |  | SI | Name: |
| Q05 | bit |  |  | SI | If Glucose Level is lower than 3.33 mmol/L (60 mg/... |
| Q06 | bit |  |  | SI | If Glucose Level is equal to or higher than 18.1 m... |
| Q07 | bit |  |  | SI | If potassium is lower than 3,5 mEq/L, Call M.D. |
| Q08 | varchar |  |  | SI | Frequency of cheking: |
| Q09 | varchar |  |  | SI | Type of Protocol: |
| Q10 | varchar |  |  | SI | BG (mmol/L) |
| Q11 | varchar |  |  | SI | Dose (Units) |
| Q12 | varchar |  |  | SI | 00.0 - 04.0 mmol/L |
| Q13 | varchar |  |  | SI | 04.1 - 06.9 mmol/L |
| Q14 | varchar |  |  | SI | 07.0 - 09.7 mmol/L |
| Q15 | varchar |  |  | SI | 09.8 - 12.4 mmol/L  |
| Q16 | varchar |  |  | SI | 12.5 - 15.3 mmol/L |
| Q17 | varchar |  |  | SI | 15.4 - 18.0 mmol/L |
| Q18 | varchar |  |  | SI | ≥ 18.1 mmol/L |
| Q19 | varchar |  |  | SI | 0 Units |
| Q20 | varchar |  |  | SI | 2 Units |
| Q21 | varchar |  |  | SI | 3 Units |
| Q22 | varchar |  |  | SI | 4 Units |
| Q23 | varchar |  |  | SI | 5 Units |
| Q24 | varchar |  |  | SI | 7 Units |
| Q25 | varchar |  |  | SI | Call M.D. |
| Q26 | varchar |  |  | SI | 00.0 - 04.0 mmol/L |
| Q27 | varchar |  |  | SI | 04.1 - 06.9 mmol/L |
| Q28 | varchar |  |  | SI | 07.0 - 09.7 mmol/L |
| Q29 | varchar |  |  | SI | 09.8 - 12.4 mmol/L |
| Q30 | varchar |  |  | SI | 12.5 - 15.3 mmol/L |
| Q31 | varchar |  |  | SI | 15.4 - 18.0 mmol/L |
| Q32 | varchar |  |  | SI | Frequency of Checking: Before Breakfast, Before Lu... |
| Q34 | varchar |  |  | SI | Notes: |
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