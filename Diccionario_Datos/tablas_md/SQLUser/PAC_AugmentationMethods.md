# SQLUser.PAC_AugmentationMethods

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AUGMTH_RowId | bigint | PK |  | NO | - |
| AUGMTH_Arm | varchar |  |  | SI | ARM |
| AUGMTH_Code | varchar |  |  | NO | Code |
| AUGMTH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AUGMTH_CreatedDate | date |  |  | SI | Created Date |
| AUGMTH_CreatedTime | time |  |  | SI | Created Time |
| AUGMTH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AUGMTH_DateFrom | date |  |  | SI | Date From |
| AUGMTH_DateTo | date |  |  | SI | Date To |
| AUGMTH_Desc | varchar |  |  | NO | Description |
| AUGMTH_NationalCode | varchar |  |  | SI | National Code |
| AUGMTH_Owner | varchar |  |  | SI | Owner |
| AUGMTH_Oxytocics | varchar |  |  | SI | Oxytocics |
| AUGMTH_UpdatedDate | date |  |  | SI | Updated Date |
| AUGMTH_UpdatedTime | time |  |  | SI | Updated Time |
| AUGMTH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Altered level of consciousness |
| Q02 | - |  |  | SI | Inattention |
| Q03 | - |  |  | SI | Disorientation |
| Q04 | - |  |  | SI | Hallucination, delusion, or psychosis |
| Q05 | - |  |  | SI | Psychomotor agitation or retardation |
| Q06 | - |  |  | SI | Inappropriate speech or mood |
| Q07 | - |  |  | SI | Sleep-wake cycle disturbance |
| Q08 | - |  |  | SI | Symptom fluctuation (of any of the above symptoms ... |
| Q09 | - |  |  | SI | -1: The questionnaire cannot be completed when the... |
| Q10 | - |  |  | SI | 0: Normal |
| Q11 | - |  |  | SI | 1-3: Subsyndromal delirium |
| Q12 | - |  |  | SI | 4-8: Delirium |
| Q13 | - |  |  | SI | -1 |
| Q14 | - |  |  | SI | The questionnaire cannot be completed when the pat... |
| Q15 | - |  |  | SI | 0 |
| Q16 | - |  |  | SI | Normal |
| Q17 | - |  |  | SI | 1-3 |
| Q18 | - |  |  | SI | Subsyndromal delirium |
| Q19 | - |  |  | SI | 4-8 |
| Q20 | - |  |  | SI | Delirium |
| Q21 | - |  |  | SI | Altered level of consciousness:  A) No response or... |
| Q22 | - |  |  | SI | If there is a coma (A) or stupor (B), there is no ... |
| Q23 | - |  |  | SI | C) Drowsiness or requirement of a mild to moderate... |
| Q24 | - |  |  | SI | D) Wakefulness or sleeping that that could easily ... |
| Q25 | - |  |  | SI | E) Hypervigilance is rated as an abnormal level of... |
| Q26 | - |  |  | SI | Inattention: difficulty in following a conversatio... |
| Q27 | - |  |  | SI | Disorientation: Any obvious mistake in time, place... |
| Q28 | - |  |  | SI | Hallucination, delusion or psychosis: The unequivo... |
| Q29 | - |  |  | SI | as well as gross impairment in reality testing. An... |
| Q30 | - |  |  | SI | Psychomotor agitation or retardation: hyperactivit... |
| Q31 | - |  |  | SI | (e.g., pulling out IV lines, hitting staff), as we... |
| Q32 | - |  |  | SI | Inappropriate speech or mood: inappropriate, disor... |
| Q33 | - |  |  | SI | Sleep / wake cycle disturbance: sleeping less than... |
| Q34 | - |  |  | SI | Any of these scores 1 point. |
| Q35 | - |  |  | SI | Symptom fluctuation: fluctuation of the manifestat... |
| Q36 | - |  |  | SI | Score |
| Q37 | - |  |  | SI | Classification |
| Q38 | - |  |  | SI | The Intensive Care Delirium Screening Checklist (I... |
| Q39 | - |  |  | SI | 1. |
| Q40 | - |  |  | SI | 2. |
| Q41 | - |  |  | SI | 3. |
| Q42 | - |  |  | SI | 4. |
| Q43 | - |  |  | SI | 5. |
| Q44 | - |  |  | SI | 6. |
| Q45 | - |  |  | SI | 7. |
| Q46 | - |  |  | SI | 8. |
| Q47 | - |  |  | SI | Date |
| Q48 | - |  |  | SI | Time |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*