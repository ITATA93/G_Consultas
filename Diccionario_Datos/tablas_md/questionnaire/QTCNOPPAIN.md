# questionnaire.QTCNOPPAIN

> Non-Communicative Patient's Pain Assessment Instrument (NOPPAIN)

**Schema:** questionnaire
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Non-Communicative Patient's Pain Assessment Instrument (NOPPAIN)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Activity Chart Check List |
| Q02 | varchar |  |  | SI | 1. Put resident in bed OR saw resident lying down |
| Q03 | varchar |  |  | SI | Did you do this? |
| Q04 | varchar |  |  | SI | Did you see pain when you did this? |
| Q05 | varchar |  |  | SI | 2. Turned resident in bed |
| Q06 | varchar |  |  | SI | Did you do this? |
| Q07 | varchar |  |  | SI | Did you see pain when you did this? |
| Q08 | varchar |  |  | SI | 3. Transferred resident (bed to chair, chair to be... |
| Q09 | varchar |  |  | SI | Did you do this? |
| Q10 | varchar |  |  | SI | Did you see pain when you did this? |
| Q11 | varchar |  |  | SI | 4. Sat resident up (bed or chair) OR saw resident ... |
| Q12 | varchar |  |  | SI | Did you do this? |
| Q13 | varchar |  |  | SI | Did you see pain when you did this? |
| Q14 | varchar |  |  | SI | 5. Dressed resident |
| Q15 | varchar |  |  | SI | Did you do this? |
| Q16 | varchar |  |  | SI | Did you see pain when you did this? |
| Q17 | varchar |  |  | SI | 6. Fed resident |
| Q18 | varchar |  |  | SI | Did you do this? |
| Q19 | varchar |  |  | SI | Did you see pain when you did this? |
| Q20 | varchar |  |  | SI | 7. Helped resident stand OR saw resident stand |
| Q21 | varchar |  |  | SI | Did you do this? |
| Q22 | varchar |  |  | SI | Did you see pain when you did this? |
| Q23 | varchar |  |  | SI | 8. Helped resident walk OR saw resident walk |
| Q24 | varchar |  |  | SI | Did you do this? |
| Q25 | varchar |  |  | SI | Did you see pain when you did this? |
| Q26 | varchar |  |  | SI | 9. Bathed resident OR gave resident sponge bath |
| Q27 | varchar |  |  | SI | Did you do this? |
| Q28 | varchar |  |  | SI | Did you see pain when you did this? |
| Q29 | varchar |  |  | SI | REMEMBER: Make sure to ASK THE PATIENT if he/she i... |
| Q30 | varchar |  |  | SI | Pain Response / Responsibility (What did you see a... |
| Q31 | varchar |  |  | SI | Pain words? (That hurts!, Ouch!, Cursing, Stop tha... |
| Q32 | varchar |  |  | SI | How intense were the pain words? |
| Q33 | varchar |  |  | SI | Pain faces? (grimaces, winces, furrowed brow) |
| Q34 | varchar |  |  | SI | How intense were the pain faces? |
| Q35 | varchar |  |  | SI | Bracing? (rigidity, holding, guarding, especially ... |
| Q36 | varchar |  |  | SI | How intense was the bracing? |
| Q37 | varchar |  |  | SI | Pain noises? (moans, groans, grunts, cries, gasps,... |
| Q38 | varchar |  |  | SI | How intense were the pain noises? |
| Q39 | varchar |  |  | SI | Rubbing? (massaging affected area) |
| Q40 | varchar |  |  | SI | How intense was the rubbing? |
| Q41 | varchar |  |  | SI | Restlessness? (frequent shifting, rocking, inabili... |
| Q42 | varchar |  |  | SI | How intense was the restlessness? |
| Q43 | varchar |  |  | SI | Level of pain |
| Q44 | varchar |  |  | SI | Level of pain |
| Q44ObsDR | varchar |  | FK | SI | Level of pain DR |
| Q45 | varchar |  |  | SI | Guidelines |
| Q46 | varchar |  |  | SI | • Nursing assistant should complete at least 5 min... |
| Q47 | varchar |  |  | SI | • This form should be completed immediately follow... |
| Q48 | date |  |  | SI | Date |
| Q49 | time |  |  | SI | Time |
| Q50 | varchar |  |  | SI | The Non-Communicative Patient's Pain Assessment In... |
| Q51 | varchar |  |  | SI | Score |
| Q52 | varchar |  |  | SI | Score Interpretation |
| Q53 | date |  |  | SI | Date |
| Q54 | time |  |  | SI | Time |
| Q55 | varchar |  |  | SI | 0 - 3 |
| Q56 | varchar |  |  | SI | No more action required |
| Q57 | varchar |  |  | SI | 0 - 3: No more action required |
| Q58 | varchar |  |  | SI | 4 - 55 |
| Q59 | varchar |  |  | SI | Nursing intervention and pain assessment required |
| Q60 | varchar |  |  | SI | 4 - 55: Nursing intervention and pain assessment r... |
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