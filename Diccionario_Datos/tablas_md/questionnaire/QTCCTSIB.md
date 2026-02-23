# questionnaire.QTCCTSIB

> Clinical Test of Sensory Interaction and Balance (CTSIB)

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Clinical Test of Sensory Interaction and Balance (CTSIB)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of test |
| Q02 | time |  |  | SI | Time of test |
| Q03 | varchar |  |  | SI | Standing on a firm surface with eyes open time (se... |
| Q04 | numeric |  |  | SI | Attempt 1 |
| Q05 | numeric |  |  | SI | Attempt 2 |
| Q06 | numeric |  |  | SI | Attempt 3 |
| Q07 | varchar |  |  | SI | Result |
| Q08 | varchar |  |  | SI | Standing on a firm surface with eyes closed time (... |
| Q09 | numeric |  |  | SI | Attempt 1 |
| Q10 | numeric |  |  | SI | Attempt 2 |
| Q11 | numeric |  |  | SI | Attempt 3 |
| Q12 | varchar |  |  | SI | Result |
| Q13 | varchar |  |  | SI | Standing on a firm surface with visual conflict ti... |
| Q14 | numeric |  |  | SI | Attempt 1 |
| Q15 | numeric |  |  | SI | Attempt 2 |
| Q16 | numeric |  |  | SI | Attempt 3 |
| Q17 | varchar |  |  | SI | Result |
| Q18 | varchar |  |  | SI | Standing on an unstable surface with eyes open tim... |
| Q19 | numeric |  |  | SI | Attempt 1 |
| Q20 | numeric |  |  | SI | Attempt 2 |
| Q21 | numeric |  |  | SI | Attempt 3 |
| Q22 | varchar |  |  | SI | Result |
| Q23 | varchar |  |  | SI | Standing on an unstable surface with eyes closed t... |
| Q24 | numeric |  |  | SI | Attempt 1 |
| Q25 | numeric |  |  | SI | Attempt 2 |
| Q26 | numeric |  |  | SI | Attempt 3 |
| Q27 | varchar |  |  | SI | Result |
| Q28 | varchar |  |  | SI | Standing on an unstable surface with visual confli... |
| Q29 | numeric |  |  | SI | Attempt 1 |
| Q30 | numeric |  |  | SI | Attempt 2 |
| Q31 | numeric |  |  | SI | Attempt 3 |
| Q32 | varchar |  |  | SI | Result |
| Q33 | varchar |  |  | SI | Comments |
| Q34 | varchar |  |  | SI | General Information |
| Q35 | varchar |  |  | SI | 1. Patients stand with their hands at their sides,... |
| Q36 | varchar |  |  | SI | 2. Patient performance is timed for 30 seconds. |
| Q37 | varchar |  |  | SI | 3. The test is terminated when: |
| Q38 | varchar |  |  | SI | • 30 seconds elapses; |
| Q39 | varchar |  |  | SI | • A subject's arms or feet change position; |
| Q40 | varchar |  |  | SI | 4. If a patient is unable to maintain the position... |
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