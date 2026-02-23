# questionnaire.QTCTBS

> Tuberculosis Score

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Tuberculosis Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Tuberculosis (TB) contact |
| Q04 | varchar |  |  | SI | Tuberculin skin test (Mantoux test) |
| Q05 | varchar |  |  | SI | Nutritional status |
| Q06 | varchar |  |  | SI | Body weight based on present body weight |
| Q07 | varchar |  |  | SI | Fever of unknown origin |
| Q08 | varchar |  |  | SI | Lymphadenopathy (Cervical, axillary, inguinal) |
| Q09 | varchar |  |  | SI | Joint swelling (Hip, knee, vertebral, phalangeal) |
| Q10 | varchar |  |  | SI | Chest X-ray |
| Q11 | varchar |  |  | SI | Chest X-ray is not considered to be a main diagnos... |
| Q12 | varchar |  |  | SI | 1. Positive tuberculosis diagnosis if total score ... |
| Q13 | varchar |  |  | SI | 2. Body weight based on present body weight |
| Q14 | varchar |  |  | SI | 3. Fever and cough relevant if no response to stan... |
| Q15 | varchar |  |  | SI | 4. Chest X-ray is not considered to be a main diag... |
| Q16 | varchar |  |  | SI | 5. Evaluated for accelerated Bacillus Calmette-Gue... |
| Q17 | varchar |  |  | SI | 6. Hospital referral to be made for children < 5 y... |
| Q18 | varchar |  |  | SI | 7. Isoniazid (INH) prophylaxis to be prescribed fo... |
| Q19 | varchar |  |  | SI | Score |
| Q20 | varchar |  |  | SI | Classification |
| Q21 | varchar |  |  | SI | 0 - 5 |
| Q22 | varchar |  |  | SI | Not indicative of a tuberculosis diagnosis |
| Q23 | varchar |  |  | SI | ≥ 6 |
| Q24 | varchar |  |  | SI | Positive tuberculosis diagnosis |
| Q25 | varchar |  |  | SI | Chronic cough |
| Q26 | varchar |  |  | SI | A tool to aid the diagnosis of tuberculosis create... |
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