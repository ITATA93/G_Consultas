# questionnaire.QTCOMSSS

> Ontario Modified STRATIFY (Sydney Scoring) - Falls Risk Assessment Tool

**Schema:** questionnaire
**Columnas:** 139
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ontario Modified STRATIFY (Sydney Scoring) - Falls Risk Assessment Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Reason for completion |
| Q04 | varchar |  |  | SI | Did the patient present to hospital with a fall or... |
| Q05 | varchar |  |  | SI | If not, has the patient fallen within the last 2 m... |
| Q06 | varchar |  |  | SI | Is the patient confused (i.e. unable to make purpo... |
| Q07 | varchar |  |  | SI | Is the patient disorientated (i.e. lacking awarene... |
| Q08 | varchar |  |  | SI | Is the patient agitated (i.e. fearful affect, freq... |
| Q09 | varchar |  |  | SI | Is the answer YES to any of the above mental statu... |
| Q10 | varchar |  |  | SI | Does the patient require eyeglasses continually? |
| Q11 | varchar |  |  | SI | Does the patient report blurred vision? |
| Q12 | varchar |  |  | SI | Does the patient have glaucoma, cataracts or macul... |
| Q13 | varchar |  |  | SI | Is the answer YES to any of the above vision quest... |
| Q14 | varchar |  |  | SI | Are there any alterations in urination (i.e. frequ... |
| Q15 | varchar |  |  | SI | Transfer score (means from bed to chair and back) |
| Q16 | varchar |  |  | SI | Mobility score |
| Q17 | varchar |  |  | SI | Summarized transfer and mobility score |
| Q18 | varchar |  |  | SI | Instructions for scoring |
| Q19 | varchar |  |  | SI | 1. Complete the Falls Risk Screen questions in the... |
| Q20 | varchar |  |  | SI | 2. Add the Transfer Score (TS) and the Mobility Sc... |
| Q21 | varchar |  |  | SI | i. If value total between 0–3 then score = 0 |
| Q22 | varchar |  |  | SI | ii. If values total between 4-6 then score = 7 |
| Q23 | varchar |  |  | SI | iii. Total TS + MS to reach the total mobility sco... |
| Q24 | varchar |  |  | SI | 3. Total score provides risk level: as validated t... |
| Q25 | varchar |  |  | SI | Consider communication difficulties when completin... |
| Q26 | varchar |  |  | SI | Score |
| Q27 | varchar |  |  | SI | Classification |
| Q28 | varchar |  |  | SI | 1 - 8 |
| Q29 | varchar |  |  | SI | The patient is NOT at risk |
| Q30 | varchar |  |  | SI | 9 - 30 |
| Q31 | varchar |  |  | SI | The patient is at risk |
| Q32 | varchar |  |  | SI | 1 - 8: The patient is NOT at risk |
| Q33 | varchar |  |  | SI | 9 - 30: The patient is at risk |
| Q34 | varchar |  |  | SI | This tool is from a best practice guideline |
| Q35 | varchar |  |  | SI | If a patient scores <9, a clinician using clinical... |
| Q36 | varchar |  |  | SI | Falls risk score corrected |
| Q37 | varchar |  |  | SI | Reason for adjustment |
| Q38 | varchar |  |  | SI | If any fall risk factors are identified, complete ... |
| Q39 | varchar |  |  | SI | Is the patient on antipsychotics, antidepressants,... |
| Q40 | varchar |  |  | SI | Complete medication section on Falls Risk Assessme... |
| Q41 | varchar |  |  | SI | Provide patient / family / carers with information... |
| Q42 | varchar |  |  | SI | Provide patient / family / carers with information... |
| Q43 | varchar |  |  | SI | Care actions for all patients |
| Q44 | varchar |  |  | SI | These care actions are relevant for all patients a... |
| Q45 | varchar |  |  | SI | • Orientate patient to bed area, toilet and ward |
| Q46 | varchar |  |  | SI | • Educate patient and family, providing culturally... |
| Q47 | varchar |  |  | SI | • Instruct patient on the use of the call bell, en... |
| Q48 | varchar |  |  | SI | • Ensure frequently used items (including mobility... |
| Q49 | varchar |  |  | SI | • Ensure bed and chair are at appropriate height f... |
| Q50 | varchar |  |  | SI | • Ensure bed brakes are on at all times and chair ... |
| Q51 | varchar |  |  | SI | • Position over-bed-table on the non exit side of ... |
| Q52 | varchar |  |  | SI | • Place IV pole and all other devices / attachment... |
| Q53 | varchar |  |  | SI | • Ensure attachments (such as catheters, wound dra... |
| Q54 | varchar |  |  | SI | • Remove clutter and obstacles from room |
| Q55 | varchar |  |  | SI | • Ensure patient is using appropriate personal aid... |
| Q56 | varchar |  |  | SI | • Ensure patient wears appropriate footwear when a... |
| Q57 | varchar |  |  | SI | • Establish patient's level of personal care need |
| Q58 | varchar |  |  | SI | • Ensure adequate night lighting |
| Q59 | varchar |  |  | SI | Provide patient / family / carers with falls preve... |
| Q60 | varchar |  |  | SI | Clinical Excellence Commission Falls Prevention fl... |
| Q61 | varchar |  |  | SI | Reproduced with permission ©Clinical Excellence Co... |
| Q62 | varchar |  |  | SI | Patient actions |
| Q63 | varchar |  |  | SI | 1. Orientation to the bed area and ward facilities... |
| Q64 | varchar |  |  | SI | 2. Lower bed if possible. Ensure brakes are on. |
| Q65 | varchar |  |  | SI | 3. Place call bell and side table within reach, an... |
| Q66 | varchar |  |  | SI | 4. Ensure safe footwear when mobilising ie well-fi... |
| Q67 | varchar |  |  | SI | 5. Provide safe footwear brochure to patient and c... |
| Q68 | varchar |  |  | SI | 6. Clothing to fit well and of appropriate length. |
| Q69 | varchar |  |  | SI | 7. Clear area of hazards-spills, clutter, unstable... |
| Q70 | varchar |  |  | SI | 8. Fall prevention brochure provided to patient / ... |
| Q71 | varchar |  |  | SI | 9. Ensure patient has access to adequate nutrition... |
| Q72 | varchar |  |  | SI | 10. Medication review |
| Q73 | varchar |  |  | SI | 11. Bone protection medication review: consider vi... |
| Q74 | varchar |  |  | SI | 12. Ensure that patient has their glasses and hear... |
| Q75 | varchar |  |  | SI | 13. Falls identifiers used (sign & sticker). |
| Q76 | varchar |  |  | SI | 14. Supervise patient during mobilisation. |
| Q77 | varchar |  |  | SI | 15. Supervise patient during self care and toileti... |
| Q78 | varchar |  |  | SI | 16. Supervise patient with nutrition and hydration... |
| Q79 | varchar |  |  | SI | 17. Regular toileting regimen, and prior to settli... |
| Q80 | varchar |  |  | SI | 18. Use non-slip matting by the bed. |
| Q81 | varchar |  |  | SI | 19. Referral to physiotherapy and/or occupational ... |
| Q82 | varchar |  |  | SI | 20. Do not leave patient unattended during planned... |
| Q83 | varchar |  |  | SI | 21. Locate patient close to the nurses station. |
| Q84 | varchar |  |  | SI | 22. Ensure bed height is appropriate to the needs ... |
| Q85 | varchar |  |  | SI | 23. Consider constant observation - particularly i... |
| Q86 | varchar |  |  | SI | 24. Consider use of hip protectors |
| Q87 | varchar |  |  | SI | Low risk : 0 – 5 points |
| Q88 | varchar |  |  | SI | Medium risk : 6 – 16 points (all of the above plus... |
| Q89 | varchar |  |  | SI | High risk : 17 – 30 points (all of the above plus,... |
| Q90 | varchar |  |  | SI | Papaioannou A. et al. Prediction of falls using a ... |
| Q91 | varchar |  |  | SI | Best Practice Risk Assessment Adjustments (Clinica... |
| Q92 | varchar |  |  | SI | 1. Falls Guidelines Review Expert Advisory Group o... |
| Q93 | varchar |  |  | SI | Preventing Falls and Harm From Falls in Older Peop... |
| Q94 | varchar |  |  | SI | 2. Papaioannou A, Parkinson W, Cook R, Ferko N, Co... |
| Q95 | varchar |  |  | SI | 3. Oliver D, Britton M, Seed P, Martin FC, Hopper ... |
| Q96 | varchar |  |  | SI | Development and evaluation of evidence based risk ... |
| Q97 | varchar |  |  | SI | (1) published by the Australian Commission on Safe... |
| Q98 | varchar |  |  | SI | (2) Which is itself an adaptation of a British fal... |
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