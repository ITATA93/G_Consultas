# questionnaire.QTCICDSC

> Intensive Care Delirium Screening Checklist (ICDSC)

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intensive Care Delirium Screening Checklist (ICDSC)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Altered level of consciousness |
| Q02 | bit |  |  | SI | Inattention |
| Q03 | bit |  |  | SI | Disorientation |
| Q04 | bit |  |  | SI | Hallucination, delusion, or psychosis |
| Q05 | bit |  |  | SI | Psychomotor agitation or retardation |
| Q06 | bit |  |  | SI | Inappropriate speech or mood |
| Q07 | bit |  |  | SI | Sleep-wake cycle disturbance |
| Q08 | bit |  |  | SI | Symptom fluctuation (of any of the above symptoms ... |
| Q09 | varchar |  |  | SI | -1: The questionnaire cannot be completed when the... |
| Q10 | varchar |  |  | SI | 0: Normal; absence of delirium |
| Q11 | varchar |  |  | SI | 1-3: Subsyndromal delirium |
| Q12 | varchar |  |  | SI | 4-8: Delirium |
| Q13 | varchar |  |  | SI | -1 |
| Q14 | varchar |  |  | SI | The questionnaire cannot be completed when the pat... |
| Q15 | varchar |  |  | SI | 0 |
| Q16 | varchar |  |  | SI | Normal |
| Q17 | varchar |  |  | SI | 1-3 |
| Q18 | varchar |  |  | SI | Subsyndromal delirium |
| Q19 | varchar |  |  | SI | 4-8 |
| Q20 | varchar |  |  | SI | Delirium |
| Q21 | varchar |  |  | SI | Altered level of consciousness:  A) No response or... |
| Q22 | varchar |  |  | SI | If there is a coma (A) or stupor (B), there is no ... |
| Q23 | varchar |  |  | SI | C) Drowsiness or requirement of a mild to moderate... |
| Q24 | varchar |  |  | SI | D) Wakefulness or sleeping that that could easily ... |
| Q25 | varchar |  |  | SI | E) Hypervigilance is rated as an abnormal level of... |
| Q26 | varchar |  |  | SI | Inattention: difficulty in following a conversatio... |
| Q27 | varchar |  |  | SI | Disorientation: Any obvious mistake in time, place... |
| Q28 | varchar |  |  | SI | Hallucination, delusion or psychosis: The unequivo... |
| Q29 | varchar |  |  | SI | as well as gross impairment in reality testing. An... |
| Q30 | varchar |  |  | SI | Psychomotor agitation or retardation: hyperactivit... |
| Q31 | varchar |  |  | SI | (e.g., pulling out IV lines, hitting staff), as we... |
| Q32 | varchar |  |  | SI | Inappropriate speech or mood: inappropriate, disor... |
| Q33 | varchar |  |  | SI | Sleep / wake cycle disturbance: sleeping less than... |
| Q34 | varchar |  |  | SI | Any of these scores 1 point. |
| Q35 | varchar |  |  | SI | Symptom fluctuation: fluctuation of the manifestat... |
| Q36 | varchar |  |  | SI | Score |
| Q37 | varchar |  |  | SI | Classification |
| Q38 | varchar |  |  | SI | The Intensive Care Delirium Screening Checklist (I... |
| Q39 | varchar |  |  | SI | 1. |
| Q40 | varchar |  |  | SI | 2. |
| Q41 | varchar |  |  | SI | 3. |
| Q42 | varchar |  |  | SI | 4. |
| Q43 | varchar |  |  | SI | 5. |
| Q44 | varchar |  |  | SI | 6. |
| Q45 | varchar |  |  | SI | 7. |
| Q46 | varchar |  |  | SI | 8. |
| Q47 | date |  |  | SI | Date |
| Q48 | time |  |  | SI | Time |
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