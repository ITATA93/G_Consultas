# questionnaire.QTCPEWS

> Pediatric Early Warning Score (PEWS)

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pediatric Early Warning Score (PEWS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Behavior |
| Q02 | varchar |  |  | SI | Cardiovascular |
| Q03 | varchar |  |  | SI | Respiratory |
| Q04 | varchar |  |  | SI | Quarter hourly nebulizers (every 15 minutes) |
| Q05 | varchar |  |  | SI | Persistent vomiting following surgery |
| Q06 | varchar |  |  | SI | PEWS Escalation Protocol |
| Q07 | varchar |  |  | SI | Score 1-2: |
| Q08 | varchar |  |  | SI | Primary Nurse uses clinical judgement to inform th... |
| Q09 | varchar |  |  | SI | Based on clinical judgement Charge Nurse notifies ... |
| Q10 | varchar |  |  | SI | PEWS scoring must be repeated within 4 hours. |
| Q11 | varchar |  |  | SI | Score 3: |
| Q12 | varchar |  |  | SI | Primary Nurse to notify the Charge Nurse  |
| Q13 | varchar |  |  | SI | Charge Nurse notifies the Paediatrician on-site to... |
| Q14 | varchar |  |  | SI | If no response from Paediatrician on-site  within ... |
| Q15 | varchar |  |  | SI | Repeat PEWS within 2 hours or as ordered by the do... |
| Q16 | varchar |  |  | SI | Score 4-5: |
| Q17 | varchar |  |  | SI | Primary Nurse to notify the Charge Nurse STAT. |
| Q18 | varchar |  |  | SI | Charge Nurse calls the Paediatrician on-site STAT. |
| Q19 | varchar |  |  | SI | If no response from the Paediatrician on-site with... |
| Q20 | varchar |  |  | SI | Repeat PEWS and assessment no later than 30 minute... |
| Q21 | varchar |  |  | SI | 6 or a score of 3 from any category: |
| Q22 | varchar |  |  | SI | Primary Nurse to notify the Charge Nurse STAT and ... |
| Q23 | varchar |  |  | SI | Charge Nurse notifies the Paediatrician on-site wh... |
| Q24 | varchar |  |  | SI | If no response from the Physician on-site to call ... |
| Q25 | varchar |  |  | SI | If Paediatrician is not available and patient’s co... |
| Q26 | date |  |  | SI | Date |
| Q27 | time |  |  | SI | Time |
| Q28 | varchar |  |  | SI | The Pediatric Early Warning Score (PEWS) was devel... |
| Q29 | varchar |  |  | SI | Trust in the UK in order for nurses and junior med... |
| Q30 | varchar |  |  | SI | Score |
| Q31 | varchar |  |  | SI | Classification |
| Q32 | varchar |  |  | SI | 0 - 2 |
| Q33 | varchar |  |  | SI | Low risk |
| Q34 | varchar |  |  | SI | 3 - 4 |
| Q35 | varchar |  |  | SI | Intermediate risk |
| Q36 | varchar |  |  | SI | 5 - 14 |
| Q37 | varchar |  |  | SI | High risk |
| Q38 | varchar |  |  | SI | 0 - 2: Low risk |
| Q39 | varchar |  |  | SI | 3 - 4: Intermediate risk |
| Q40 | varchar |  |  | SI | 5 - 14: High risk |
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