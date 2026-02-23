# SQLUser.PAC_ReferralWaitListTypeLink

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFWLTL_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Behavior |
| Q02 | - |  |  | SI | Cardiovascular |
| Q03 | - |  |  | SI | Respiratory |
| Q04 | - |  |  | SI | Quarter hourly nebulizers (every 15 minutes) |
| Q05 | - |  |  | SI | Persistent vomiting following surgery |
| Q06 | - |  |  | SI | PEWS Escalation Protocol |
| Q07 | - |  |  | SI | Score 1-2: |
| Q08 | - |  |  | SI | Primary Nurse uses clinical judgement to inform th... |
| Q09 | - |  |  | SI | Based on clinical judgement Charge Nurse notifies ... |
| Q10 | - |  |  | SI | PEWS scoring must be repeated within 4 hours. |
| Q11 | - |  |  | SI | Score 3: |
| Q12 | - |  |  | SI | Primary Nurse to notify the Charge Nurse |
| Q13 | - |  |  | SI | Charge Nurse notifies the Paediatrician on-site to... |
| Q14 | - |  |  | SI | If no response from Paediatrician on-site  within ... |
| Q15 | - |  |  | SI | Repeat PEWS within 2 hours or as ordered by the do... |
| Q16 | - |  |  | SI | Score 4-5: |
| Q17 | - |  |  | SI | Primary Nurse to notify the Charge Nurse STAT. |
| Q18 | - |  |  | SI | Charge Nurse calls the Paediatrician on-site STAT. |
| Q19 | - |  |  | SI | If no response from the Paediatrician on-site with... |
| Q20 | - |  |  | SI | Repeat PEWS and assessment no later than 30 minute... |
| Q21 | - |  |  | SI | 6 or a score of 3 from any category: |
| Q22 | - |  |  | SI | Primary Nurse to notify the Charge Nurse STAT and ... |
| Q23 | - |  |  | SI | Charge Nurse notifies the Paediatrician on-site wh... |
| Q24 | - |  |  | SI | If no response from the Physician on-site to call ... |
| Q25 | - |  |  | SI | If Paediatrician is not available and patient’s co... |
| Q26 | - |  |  | SI | Date |
| Q27 | - |  |  | SI | Time |
| Q28 | - |  |  | SI | The Pediatric Early Warning Score (PEWS) was devel... |
| Q29 | - |  |  | SI | Trust in the UK in order for nurses and junior med... |
| Q30 | - |  |  | SI | Score |
| Q31 | - |  |  | SI | Classification |
| Q32 | - |  |  | SI | 0 - 2 |
| Q33 | - |  |  | SI | Low risk |
| Q34 | - |  |  | SI | 3 - 4 |
| Q35 | - |  |  | SI | Intermediate risk |
| Q36 | - |  |  | SI | 5 - 14 |
| Q37 | - |  |  | SI | High risk |
| Q38 | - |  |  | SI | 0 - 2: Low risk |
| Q39 | - |  |  | SI | 3 - 4: Intermediate risk |
| Q40 | - |  |  | SI | 5 - 14: High risk |
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
| REFWLTL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFWLTL_CreatedDate | date |  |  | SI | Created Date |
| REFWLTL_CreatedTime | time |  |  | SI | Created Time |
| REFWLTL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFWLTL_DateFrom | date |  |  | SI | Date From |
| REFWLTL_DateTo | date |  |  | SI | Date To |
| REFWLTL_GroupByPriority | varchar |  |  | SI | Grouped by Priority |
| REFWLTL_GroupByReferral | varchar |  |  | SI | Grouped by Referral  |
| REFWLTL_Owner | varchar |  |  | SI | Owner |
| REFWLTL_UpdatedDate | date |  |  | SI | Updated Date |
| REFWLTL_UpdatedTime | time |  |  | SI | Updated Time |
| REFWLTL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| REFWLTL_WaitListType1_DR | bigint |  | FK | SI | Des Ref PACWaitingListType |
| REFWLTL_WaitListType2_DR | bigint |  | FK | SI | Des Ref PACWaitingListType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*