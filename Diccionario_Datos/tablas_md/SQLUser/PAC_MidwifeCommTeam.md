# SQLUser.PAC_MidwifeCommTeam

**Schema:** SQLUser
**Columnas:** 115
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIDCOMM_RowId | bigint | PK |  | NO | - |
| MIDCOMM_Code | varchar |  |  | NO | Code |
| MIDCOMM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MIDCOMM_CreatedDate | date |  |  | SI | Created Date |
| MIDCOMM_CreatedTime | time |  |  | SI | Created Time |
| MIDCOMM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MIDCOMM_DateFrom | date |  |  | SI | Date From |
| MIDCOMM_DateTo | date |  |  | SI | Date To |
| MIDCOMM_Desc | varchar |  |  | NO | Description |
| MIDCOMM_NationalCode | varchar |  |  | SI | National Code |
| MIDCOMM_Owner | varchar |  |  | SI | Owner |
| MIDCOMM_UpdatedDate | date |  |  | SI | Updated Date |
| MIDCOMM_UpdatedTime | time |  |  | SI | Updated Time |
| MIDCOMM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Activity Chart Check List |
| Q02 | - |  |  | SI | 1. Put resident in bed OR saw resident lying down |
| Q03 | - |  |  | SI | Did you do this? |
| Q04 | - |  |  | SI | Did you see pain when you did this? |
| Q05 | - |  |  | SI | 2. Turned resident in bed |
| Q06 | - |  |  | SI | Did you do this? |
| Q07 | - |  |  | SI | Did you see pain when you did this? |
| Q08 | - |  |  | SI | 3. Transferred resident (bed to chair, chair to be... |
| Q09 | - |  |  | SI | Did you do this? |
| Q10 | - |  |  | SI | Did you see pain when you did this? |
| Q11 | - |  |  | SI | 4. Sat resident up (bed or chair) OR saw resident ... |
| Q12 | - |  |  | SI | Did you do this? |
| Q13 | - |  |  | SI | Did you see pain when you did this? |
| Q14 | - |  |  | SI | 5. Dressed resident |
| Q15 | - |  |  | SI | Did you do this? |
| Q16 | - |  |  | SI | Did you see pain when you did this? |
| Q17 | - |  |  | SI | 6. Fed resident |
| Q18 | - |  |  | SI | Did you do this? |
| Q19 | - |  |  | SI | Did you see pain when you did this? |
| Q20 | - |  |  | SI | 7. Helped resident stand OR saw resident stand |
| Q21 | - |  |  | SI | Did you do this? |
| Q22 | - |  |  | SI | Did you see pain when you did this? |
| Q23 | - |  |  | SI | 8. Helped resident walk OR saw resident walk |
| Q24 | - |  |  | SI | Did you do this? |
| Q25 | - |  |  | SI | Did you see pain when you did this? |
| Q26 | - |  |  | SI | 9. Bathed resident OR gave resident sponge bath |
| Q27 | - |  |  | SI | Did you do this? |
| Q28 | - |  |  | SI | Did you see pain when you did this? |
| Q29 | - |  |  | SI | REMEMBER: Make sure to ASK THE PATIENT if he/she i... |
| Q30 | - |  |  | SI | Pain Response / Responsibility (What did you see a... |
| Q31 | - |  |  | SI | Pain words? (That hurts!, Ouch!, Cursing, Stop tha... |
| Q32 | - |  |  | SI | How intense were the pain words? |
| Q33 | - |  |  | SI | Pain faces? (grimaces, winces, furrowed brow) |
| Q34 | - |  |  | SI | How intense were the pain faces? |
| Q35 | - |  |  | SI | Bracing? (rigidity, holding, guarding, especially ... |
| Q36 | - |  |  | SI | How intense was the bracing? |
| Q37 | - |  |  | SI | Pain noises? (moans, groans, grunts, cries, gasps,... |
| Q38 | - |  |  | SI | How intense were the pain noises? |
| Q39 | - |  |  | SI | Rubbing? (massaging affected area) |
| Q40 | - |  |  | SI | How intense was the rubbing? |
| Q41 | - |  |  | SI | Restlessness? (frequent shifting, rocking, inabili... |
| Q42 | - |  |  | SI | How intense was the restlessness? |
| Q43 | - |  |  | SI | Level of pain |
| Q44 | - |  |  | SI | Level of pain |
| Q44ObsDR | - |  |  | SI | Level of pain DR |
| Q45 | - |  |  | SI | Guidelines |
| Q46 | - |  |  | SI | • Nursing assistant should complete at least 5 min... |
| Q47 | - |  |  | SI | • This form should be completed immediately follow... |
| Q48 | - |  |  | SI | Date |
| Q49 | - |  |  | SI | Time |
| Q50 | - |  |  | SI | The Non-Communicative Patient's Pain Assessment In... |
| Q51 | - |  |  | SI | Score |
| Q52 | - |  |  | SI | Score Interpretation |
| Q53 | - |  |  | SI | Date |
| Q54 | - |  |  | SI | Time |
| Q55 | - |  |  | SI | 0 - 3 |
| Q56 | - |  |  | SI | No more action required |
| Q57 | - |  |  | SI | 0 - 3: No more action required |
| Q58 | - |  |  | SI | 4 - 55 |
| Q59 | - |  |  | SI | Nursing intervention and pain assessment required |
| Q60 | - |  |  | SI | 4 - 55: Nursing intervention and pain assessment r... |
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