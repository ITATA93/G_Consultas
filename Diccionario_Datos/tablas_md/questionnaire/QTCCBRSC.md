# questionnaire.QTCCBRSC

> CRUSADE Bleeding Risk Score

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* CRUSADE Bleeding Risk Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Baseline hematocrit (%) |
| Q04 | varchar |  |  | SI | Creatinine clearance (mL/min) |
| Q05 | varchar |  |  | SI | Heart rate (beats / minute) |
| Q06 | varchar |  |  | SI | Systolic BP (mmHg) |
| Q07 | varchar |  |  | SI | Sex |
| Q08 | varchar |  |  | SI | Signs of congestive heart failure at presentation |
| Q09 | varchar |  |  | SI | Prior vascular disease |
| Q10 | varchar |  |  | SI | Diabetes mellitus |
| Q11 | varchar |  |  | SI | In the original study: |
| Q12 | varchar |  |  | SI | Creatinine clearance was estimated using the Cockc... |
| Q13 | varchar |  |  | SI | Prior vascular disease was defined as history of p... |
| Q14 | varchar |  |  | SI | Score Interpretation: |
| Q15 | varchar |  |  | SI | The CRUSADE bleeding score (range 1–100 points) wa... |
| Q16 | varchar |  |  | SI | 3.1% very low risk (≤ 20) |
| Q17 | varchar |  |  | SI | 5.5% low risk (21 – 30) |
| Q18 | varchar |  |  | SI | 8.6% moderate risk (31 – 40) |
| Q19 | varchar |  |  | SI | 11.9% high risk (41 – 50) |
| Q20 | varchar |  |  | SI | and 19.5% very high risk (> 50) |
| Q21 | varchar |  |  | SI | Score |
| Q22 | varchar |  |  | SI | Classification |
| Q23 | varchar |  |  | SI | ≤ 20 |
| Q24 | varchar |  |  | SI | Very low risk |
| Q25 | varchar |  |  | SI | 21 - 30 |
| Q26 | varchar |  |  | SI | Low risk |
| Q27 | varchar |  |  | SI | 31 - 40 |
| Q28 | varchar |  |  | SI | Moderate risk |
| Q29 | varchar |  |  | SI | 41 - 50 |
| Q30 | varchar |  |  | SI | High risk |
| Q31 | varchar |  |  | SI | > 50 |
| Q32 | varchar |  |  | SI | Very high risk |
| Q33 | varchar |  |  | SI | ≤ 20: 3.1% very low risk |
| Q34 | varchar |  |  | SI | 21 - 30: 5.5% low risk |
| Q35 | varchar |  |  | SI | 31 - 40: 8.6% moderate risk |
| Q36 | varchar |  |  | SI | 41 - 50: 11.9% high risk |
| Q37 | varchar |  |  | SI | > 50: 19.5% very high risk |
| Q38 | varchar |  |  | SI | The CRUSADE bleeding score quantifies risk for in-... |
| Q39 | varchar |  |  | SI | Creatinine clearance (mL/min) |
| Q40 | varchar |  |  | SI | 1.Subherwal S, Bach RG, Chen AY, et al. Baseline R... |
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