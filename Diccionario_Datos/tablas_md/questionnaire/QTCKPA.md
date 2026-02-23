# questionnaire.QTCKPA

> Knee Progress Assessment

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Knee Progress Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Pain scale |
| Q03ObsDR | varchar |  | FK | SI | Pain scale DR |
| Q04 | varchar |  |  | SI | How does the patient feel? |
| Q05 | varchar |  |  | SI | Does the patient have nausea / vomiting? |
| Q06 | varchar |  |  | SI | Does the patient have nausea / vomiting? |
| Q07 | varchar |  |  | SI | Does the patient indicate any numbness in the leg? |
| Q08 | varchar |  |  | SI | Additional subjective information |
| Q09 | varchar |  |  | SI | Vital Signs |
| Q10 | varchar |  |  | SI | Temperature |
| Q10ObsDR | varchar |  | FK | SI | Temperature DR |
| Q11 | varchar |  |  | SI | RR |
| Q11ObsDR | varchar |  | FK | SI | RR DR |
| Q12 | varchar |  |  | SI | Pulse |
| Q12ObsDR | varchar |  | FK | SI | Pulse DR |
| Q13 | varchar |  |  | SI | Systolic BP |
| Q13ObsDR | varchar |  | FK | SI | Systolic BP DR |
| Q14 | varchar |  |  | SI | Diastolic BP |
| Q14ObsDR | varchar |  | FK | SI | Diastolic BP DR |
| Q15 | varchar |  |  | SI | Wound Details |
| Q16 | varchar |  |  | SI | Bleeding |
| Q17 | varchar |  |  | SI | Signs of infection |
| Q18 | varchar |  |  | SI | Swelling |
| Q19 | varchar |  |  | SI | Signs of DVT |
| Q20 | varchar |  |  | SI | Vacuum drain |
| Q21 | numeric |  |  | SI | Vacuum drain (ml) |
| Q22 | varchar |  |  | SI | ml |
| Q23 | varchar |  |  | SI | Additional wound information |
| Q24 | varchar |  |  | SI | Knee Range of Motion (ROM) |
| Q26 | varchar |  |  | SI | Neurovascular Status |
| Q27 | varchar |  |  | SI | Neurovascular status |
| Q28 | varchar |  |  | SI | Neurovascular details |
| Q29 | varchar |  |  | SI | Ambulation |
| Q30 | varchar |  |  | SI | Ambulation |
| Q31 | varchar |  |  | SI | Ambulation details |
| Q32 | varchar |  |  | SI | Post-op progress |
| Q33 | varchar |  |  | SI | Recovery as expected |
| Q34 | varchar |  |  | SI | Additional assessment information |
| Q35 | varchar |  |  | SI | Plan |
| Q36 | varchar |  |  | SI | Self physical therapy training program explained a... |
| Q37 | varchar |  |  | SI | Continue intravenous antibiotics |
| Q38 | varchar |  |  | SI | Additional discharge information |
| Q39 | varchar |  |  | SI |  °C |
| Q40 | varchar |  |  | SI |  br/min |
| Q41 | varchar |  |  | SI |  bt/min |
| Q42 | varchar |  |  | SI |  mmHg |
| Q43 | varchar |  |  | SI |  mmHg |
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