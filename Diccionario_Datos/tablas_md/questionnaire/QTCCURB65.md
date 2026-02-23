# questionnaire.QTCCURB65

> CURB-65 Score for Pneumonia Severity

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* CURB-65 Score for Pneumonia Severity

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Confusion |
| Q04 | varchar |  |  | SI | Blood Urea Nitrogen (BUN) > 19 mg/dL (> 7 mmol/L) |
| Q05 | varchar |  |  | SI | Respiratory rate ≥ 30 bpm |
| Q06 | varchar |  |  | SI | Systolic BP < 90 mmHg or Diastolic BP ≤ 60 mmHg |
| Q07 | varchar |  |  | SI | Age ≥ 65 years |
| Q08 | varchar |  |  | SI | Score |
| Q09 | varchar |  |  | SI | Classification |
| Q10 | varchar |  |  | SI | CURB-65 Score estimates mortality of community-acq... |
| Q11 | varchar |  |  | SI | 0 |
| Q12 | varchar |  |  | SI | Low risk groups: 0.6% 30-days mortality. Consider ... |
| Q13 | varchar |  |  | SI | 1 |
| Q14 | varchar |  |  | SI | Low risk groups: 2.7% 30-days mortality. Consider ... |
| Q15 | varchar |  |  | SI | 2 |
| Q16 | varchar |  |  | SI | Moderate risk groups: 6.8% 30-days mortality. Cons... |
| Q17 | varchar |  |  | SI | 3 |
| Q18 | varchar |  |  | SI | Moderate risk groups: 14% 30-days mortality. Consi... |
| Q19 | varchar |  |  | SI | 4 - 5 |
| Q20 | varchar |  |  | SI | Highest risk groups: 27.8% 30-days mortality. Cons... |
| Q21 | varchar |  |  | SI | 0: 	Low risk groups: 0.6% 30-days mortality. Consi... |
| Q22 | varchar |  |  | SI | 1: Low risk groups: 2.7% 30-days mortality. Consid... |
| Q23 | varchar |  |  | SI | 2: Moderate risk groups: 6.8% 30-days mortality. C... |
| Q24 | varchar |  |  | SI | 3:  Moderate risk groups: 14% 30-days mortality. C... |
| Q25 | varchar |  |  | SI | 4 - 5: Highest risk groups: 27.8% 30-days mortalit... |
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