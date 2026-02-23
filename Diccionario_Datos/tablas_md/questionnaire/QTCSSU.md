# questionnaire.QTCSSU

> Updated Schwartz Criteria For Long QT Syndrome (1993 - 2011)

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Updated Schwartz Criteria For Long QT Syndrome (1993 - 2011)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Long QT Syndrome (LQTS) Diagnostic Criteria (Updat... |
| Q04 | varchar |  |  | SI | A. Syncope (mutually exclusive) |
| Q05 | varchar |  |  | SI | A. QTc |
| Q06 | varchar |  |  | SI | Calculated by Bazett's formula where QTc = QT/√RR |
| Q07 | varchar |  |  | SI | B. QTc† 4th minute of recovery from exercise stres... |
| Q08 | varchar |  |  | SI | Calculated by Bazett's formula where QTc = QT/√RR |
| Q09 | varchar |  |  | SI | C. Torsades de Pointes (mutually exclusive) |
| Q10 | varchar |  |  | SI | D. T - wave alternans |
| Q11 | varchar |  |  | SI | D. T - wave alternans |
| Q12 | varchar |  |  | SI | E. Notched T wave in 3 leads |
| Q13 | varchar |  |  | SI | F. Low heart rate for age (resting heart rate belo... |
| Q14 | varchar |  |  | SI | B. Congenital deafness |
| Q15 | varchar |  |  | SI | For questions A and B in Family History, the same ... |
| Q16 | varchar |  |  | SI | A. Family members with definite LQTS |
| Q17 | varchar |  |  | SI | B. Unexplained sudden cardiac death below age 30 a... |
| Q18 | varchar |  |  | SI | Score |
| Q19 | varchar |  |  | SI | Classification |
| Q20 | varchar |  |  | SI | ≤ 1 |
| Q21 | varchar |  |  | SI | Low probability of Long QT Syndrome |
| Q22 | varchar |  |  | SI | 1.5 – 3 |
| Q23 | varchar |  |  | SI | Intermediate probability of Long QT Syndrome |
| Q24 | varchar |  |  | SI | ≥ 3.5 |
| Q25 | varchar |  |  | SI | High probability of Long QT Syndrome |
| Q26 | varchar |  |  | SI | <= 1: Low probability of Long QT Syndrome |
| Q27 | varchar |  |  | SI | 1.5 – 3: Intermediate probability of Long QT Syndr... |
| Q28 | varchar |  |  | SI | >= 3.5: High probability of Long QT Syndrome |
| Q29 | varchar |  |  | SI | A tool to assess the patient’s probability of Long... |
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