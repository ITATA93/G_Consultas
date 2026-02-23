# questionnaire.QTCNSZCQ

> Zurich Claudication Questionnaire

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Zurich Claudication Questionnaire

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | I. The pain you have had on the average, including... |
| Q02 | varchar |  |  | SI | II. How often have you had back, buttock, or leg p... |
| Q03 | varchar |  |  | SI | III. The pain in your back or buttocks? |
| Q04 | varchar |  |  | SI | IV. The pain in your legs or feet? |
| Q05 | varchar |  |  | SI | V. Numbness or tingling in your legs or feet? |
| Q06 | varchar |  |  | SI | VI. Weakness in your legs or feet? |
| Q07 | varchar |  |  | SI | VII. Problems with your balance? |
| Q08 | varchar |  |  | SI | VIII. How far have you been able to walk? |
| Q09 | varchar |  |  | SI | IX. Have you taken walks outdoors or around the sh... |
| Q10 | varchar |  |  | SI | X. Have you been shopping for groceries or other i... |
| Q11 | varchar |  |  | SI | XI. Have you walked around the different rooms in ... |
| Q12 | varchar |  |  | SI | XII. Have you walked from your bedroom to the bath... |
| Q13 | varchar |  |  | SI | XIII. The overall result of your back operation? |
| Q14 | varchar |  |  | SI | XIV. Relief of pain after your operation? |
| Q15 | varchar |  |  | SI | XV. The ability to walk after your operation? |
| Q16 | varchar |  |  | SI | XVI. Your ability to do housework, yardwork, or jo... |
| Q17 | varchar |  |  | SI | XVII. Your strength in your thighs, legs, and feet... |
| Q18 | varchar |  |  | SI | XVIII. Your balance, or steadiness, on your feet? |
| Q19 | varchar |  |  | SI | The Zurich Claudication Questionnaire quantifies s... |
| Q20 | varchar |  |  | SI | There are 12 questions for all patients, and a fur... |
| Q21 | varchar |  |  | SI | The The Zurich Claudication Questionnaire consists... |
| Q22 | varchar |  |  | SI | 1. Symptom severity scale  (questions I-VII) [furt... |
| Q23 | varchar |  |  | SI | 2. Physical function scale (questions VIII-XII): P... |
| Q24 | varchar |  |  | SI | 3. Patient's satisfaction with treatment scale (qu... |
| Q25 | varchar |  |  | SI | The score increases with worsening disability. |
| Q26 | varchar |  |  | SI | 0 = No Disability & 79 = Worsening Disability |
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