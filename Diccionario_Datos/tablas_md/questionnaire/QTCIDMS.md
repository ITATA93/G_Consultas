# questionnaire.QTCIDMS

> Infectious Diseases Melioidosis Summary

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Infectious Diseases Melioidosis Summary

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Risk factor(s) |
| Q04 | varchar |  |  | SI | Other risk factor(s) |
| Q05 | numeric |  |  | SI | Number of admissions |
| Q06 | varchar |  |  | SI | Details of previous admissions |
| Q07 | date |  |  | SI | Diagnosis date |
| Q08 | date |  |  | SI | Discharge date |
| Q09 | varchar |  |  | SI | Disease status |
| Q10 | varchar |  |  | SI | Melioidosis history |
| Q11 | varchar |  |  | SI | Inoculation event |
| Q12 | varchar |  |  | SI | Melioidosis diagnosis (ensure patients diagnosis i... |
| Q13 | varchar |  |  | SI | Other clinical focus notes |
| Q14 | varchar |  |  | SI | Blood culture |
| Q15 | date |  |  | SI | Date blood culture completed |
| Q16 | varchar |  |  | SI | Sputum culture |
| Q17 | date |  |  | SI | Date sputum culture completed |
| Q18 | varchar |  |  | SI | Urine culture |
| Q19 | date |  |  | SI | Date urine culture completed |
| Q20 | varchar |  |  | SI | Pus cutlure |
| Q21 | date |  |  | SI | Date pus culture completed |
| Q22 | varchar |  |  | SI | Septic shock |
| Q23 | varchar |  |  | SI | Abscesses |
| Q24 | varchar |  |  | SI | Other location of abscess notes |
| Q25 | varchar |  |  | SI | Chest X-ray (CXR) |
| Q26 | date |  |  | SI | Date CXR completed |
| Q28 | varchar |  |  | SI | Intensive Care Unit (ICU) admission |
| Q29 | varchar |  |  | SI | During ICU admission, patient was |
| Q30 | varchar |  |  | SI | Antibiotic recommendations  |
| Q31 | varchar |  |  | SI | Compliance |
| Q32 | varchar |  |  | SI | Antibiotic recommendations  |
| Q33 | varchar |  |  | SI | Compliance |
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