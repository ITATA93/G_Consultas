# questionnaire.QTCHASBLED

> HAS-BLED Score for Major Bleeding Risk

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* HAS-BLED Score for Major Bleeding Risk

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Hypertension (uncontrolled, >160 mmHg systolic) |
| Q02 | varchar |  |  | SI | Renal disease (dialysis, transplant, Creatinine >2... |
| Q03 | varchar |  |  | SI | Liver disease (cirrhosis or bilirubin >2x normal w... |
| Q04 | varchar |  |  | SI | Stroke history	 |
| Q05 | varchar |  |  | SI | Prior major bleeding or predisposition to bleeding... |
| Q06 | varchar |  |  | SI | Labile International Normalized Ratio (INR) (unsta... |
| Q07 | varchar |  |  | SI | Age > 65 years |
| Q08 | varchar |  |  | SI | Medication usage predisposing to bleeding |
| Q09 | varchar |  |  | SI | (e.g. Aspirin, Clopidogrel, Non-steroidal anti-inf... |
| Q10 | varchar |  |  | SI | Alcohol use (≥ 8 drinks/week) |
| Q11 | varchar |  |  | SI | 1. Maximum Total Score: 9 |
| Q12 | varchar |  |  | SI | 2. The score estimates the risk of major bleeding ... |
| Q13 | varchar |  |  | SI | Score |
| Q14 | varchar |  |  | SI | Classification	 |
| Q15 | varchar |  |  | SI | 0 points: Major bleeding risk 1% per year |
| Q16 | varchar |  |  | SI | 1 points: Major bleeding risk 3.4% per year |
| Q17 | varchar |  |  | SI | 2 points: Major bleeding risk 4.1% per year |
| Q18 | varchar |  |  | SI | 3 points: Major bleeding risk 5.8% per year |
| Q19 | varchar |  |  | SI | 4 points: Major bleeding risk 8.9% per year |
| Q20 | varchar |  |  | SI | 5 points: Major bleeding risk 9.1% per year |
| Q21 | varchar |  |  | SI | > 5 points: Major bleeding risk 12-15% per year |
| Q22 | varchar |  |  | SI | HAS-BLED Score is a tool to potentially guide the ... |
| Q23 | varchar |  |  | SI | The HAS-BLED Score was developed as a practical ri... |
| Q24 | date |  |  | SI | Date |
| Q25 | time |  |  | SI | Time |
| Q26 | date |  |  | SI | Date |
| Q27 | time |  |  | SI | Time |
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