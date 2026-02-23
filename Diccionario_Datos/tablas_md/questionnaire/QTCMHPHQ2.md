# questionnaire.QTCMHPHQ2

> Patient Health Questionnaire-2 (PHQ-2)

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Health Questionnaire-2 (PHQ-2)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Over the past two weeks, how often have you been b... |
| Q02 | varchar |  |  | SI | Little interest or pleasure in doing things? |
| Q03 | varchar |  |  | SI | Feeling down, depressed, or hopeless? |
| Q04 | varchar |  |  | SI | The Patient Health Questionnaire PHQ-2, comprising... |
| Q05 | varchar |  |  | SI | Its purpose is not to establish final diagnosis or... |
| Q06 | varchar |  |  | SI | Score |
| Q07 | varchar |  |  | SI | Classification	 |
| Q08 | varchar |  |  | SI | Probability of Major Depressive Disorder (%)	 |
| Q09 | varchar |  |  | SI | Probability of Depressive Disorder (%) |
| Q10 | varchar |  |  | SI | 1 |
| Q11 | varchar |  |  | SI | 15.4 |
| Q12 | varchar |  |  | SI | 36.9 |
| Q13 | varchar |  |  | SI | 2 |
| Q14 | varchar |  |  | SI | 21.1 |
| Q15 | varchar |  |  | SI | 48.3 |
| Q16 | varchar |  |  | SI | 3 |
| Q17 | varchar |  |  | SI | 38.4 |
| Q18 | varchar |  |  | SI | 75.0 |
| Q19 | varchar |  |  | SI | 4 |
| Q20 | varchar |  |  | SI | 45.5 |
| Q21 | varchar |  |  | SI | 81.2 |
| Q22 | varchar |  |  | SI | 5 |
| Q23 | varchar |  |  | SI | 56.4 |
| Q24 | varchar |  |  | SI | 84.6 |
| Q25 | varchar |  |  | SI | 6 |
| Q26 | varchar |  |  | SI | 78.6 |
| Q27 | varchar |  |  | SI | 92.9 |
| Q28 | varchar |  |  | SI | The Patient Health Questionnaire PHQ-2, comprising... |
| Q29 | varchar |  |  | SI | Patients who screen positive should be further eva... |
| Q30 | varchar |  |  | SI | Negative |
| Q31 | varchar |  |  | SI | Positive.  Use PHQ-9 for further evaluation |
| Q32 | varchar |  |  | SI | 0-2 |
| Q33 | varchar |  |  | SI | 3-6 |
| Q34 | varchar |  |  | SI | Probability of Major Depressive Disorder (%)  |
| Q35 | varchar |  |  | SI | Probability of Depressive Disorder (%) |
| Q36 | date |  |  | SI | Date |
| Q37 | time |  |  | SI | Time |
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