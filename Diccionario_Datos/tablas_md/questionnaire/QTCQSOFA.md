# questionnaire.QTCQSOFA

> Quick Sepsis Organ Failure Assessment

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Quick Sepsis Organ Failure Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q04 | varchar |  |  | SI | Altered mental status: GCS ≤ 15 |
| Q05 | varchar |  |  | SI | Respiratory rate ≥ 22 bpm |
| Q06 | varchar |  |  | SI | Systolic BP ≤ 100 mmHg |
| Q07 | varchar |  |  | SI | Score |
| Q08 | varchar |  |  | SI | Classification |
| Q09 | varchar |  |  | SI | 0 |
| Q10 | varchar |  |  | SI | Patient with suspected infection not in the intens... |
| Q11 | varchar |  |  | SI | 1 |
| Q12 | varchar |  |  | SI | Patient with suspected infection not in the intens... |
| Q13 | varchar |  |  | SI | 2 |
| Q14 | varchar |  |  | SI | Patient with suspected infection not in the intens... |
| Q15 | varchar |  |  | SI | 3 |
| Q16 | varchar |  |  | SI | Patient with suspected infection not in the intens... |
| Q17 | varchar |  |  | SI | 0: Patient with suspected infection not in the int... |
| Q18 | varchar |  |  | SI | 1: Patient with suspected infection not in the int... |
| Q19 | varchar |  |  | SI | 2: Patient with suspected infection not in the int... |
| Q20 | varchar |  |  | SI | 3: Patient with suspected infection not in the int... |
| Q21 | varchar |  |  | SI | The qSOFA score (also known as quickSOFA) is a bed... |
| Q22 | varchar |  |  | SI | 1% risk |
| Q23 | varchar |  |  | SI | of a bad outcome. |
| Q24 | varchar |  |  | SI | Sepsis considered |
| Q25 | varchar |  |  | SI | unlikely |
| Q26 | varchar |  |  | SI | 3% risk |
| Q27 | varchar |  |  | SI | of a bad outcome. Sepsis considered |
| Q28 | varchar |  |  | SI | possible. |
| Q29 | varchar |  |  | SI | 6% risk |
| Q30 | varchar |  |  | SI | of a bad outcome. Sepsis considered |
| Q31 | varchar |  |  | SI | likely. |
| Q32 | varchar |  |  | SI | 23% risk |
| Q33 | varchar |  |  | SI | of a bad outcome. Sepsis considered |
| Q34 | varchar |  |  | SI | very likely. |
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