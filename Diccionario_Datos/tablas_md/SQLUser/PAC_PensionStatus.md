# SQLUser.PAC_PensionStatus

**Schema:** SQLUser
**Columnas:** 150
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PENST_RowId | bigint | PK |  | NO | - |
| PENST_Code | varchar |  |  | NO | Code |
| PENST_CreatedDate | date |  |  | SI | Created Date |
| PENST_CreatedTime | time |  |  | SI | Created Time |
| PENST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PENST_DateFrom | date |  |  | SI | DateFrom |
| PENST_DateTo | date |  |  | SI | DateTo |
| PENST_Desc | varchar |  |  | NO | Description |
| PENST_NationalCode | varchar |  |  | SI | National Code |
| PENST_UpdatedDate | date |  |  | SI | Updated Date |
| PENST_UpdatedTime | time |  |  | SI | Updated Time |
| PENST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Reason for completion |
| Q04 | - |  |  | SI | Did the patient present to hospital with a fall or... |
| Q05 | - |  |  | SI | If not, has the patient fallen within the last 2 m... |
| Q06 | - |  |  | SI | Is the patient confused (i.e. unable to make purpo... |
| Q07 | - |  |  | SI | Is the patient disorientated (i.e. lacking awarene... |
| Q08 | - |  |  | SI | Is the patient agitated (i.e. fearful affect, freq... |
| Q09 | - |  |  | SI | Is the answer YES to any of the above mental statu... |
| Q10 | - |  |  | SI | Does the patient require eyeglasses continually? |
| Q11 | - |  |  | SI | Does the patient report blurred vision? |
| Q12 | - |  |  | SI | Does the patient have glaucoma, cataracts or macul... |
| Q13 | - |  |  | SI | Is the answer YES to any of the above vision quest... |
| Q14 | - |  |  | SI | Are there any alterations in urination (i.e. frequ... |
| Q15 | - |  |  | SI | Transfer score (means from bed to chair and back) |
| Q16 | - |  |  | SI | Mobility score |
| Q17 | - |  |  | SI | Summarized transfer and mobility score |
| Q18 | - |  |  | SI | Instructions for scoring |
| Q19 | - |  |  | SI | 1. Complete the Falls Risk Screen questions in the... |
| Q20 | - |  |  | SI | 2. Add the Transfer Score (TS) and the Mobility Sc... |
| Q21 | - |  |  | SI | i. If value total between 0–3 then score = 0 |
| Q22 | - |  |  | SI | ii. If values total between 4-6 then score = 7 |
| Q23 | - |  |  | SI | iii. Total TS + MS to reach the total mobility sco... |
| Q24 | - |  |  | SI | 3. Total score provides risk level: as validated t... |
| Q25 | - |  |  | SI | Consider communication difficulties when completin... |
| Q26 | - |  |  | SI | Score |
| Q27 | - |  |  | SI | Classification |
| Q28 | - |  |  | SI | 1 - 8 |
| Q29 | - |  |  | SI | The patient is NOT at risk |
| Q30 | - |  |  | SI | 9 - 30 |
| Q31 | - |  |  | SI | The patient is at risk |
| Q32 | - |  |  | SI | 1 - 8: The patient is NOT at risk |
| Q33 | - |  |  | SI | 9 - 30: The patient is at risk |
| Q34 | - |  |  | SI | This tool is from a best practice guideline |
| Q35 | - |  |  | SI | If a patient scores <9, a clinician using clinical... |
| Q36 | - |  |  | SI | Falls risk score corrected |
| Q37 | - |  |  | SI | Reason for adjustment |
| Q38 | - |  |  | SI | If any fall risk factors are identified, complete ... |
| Q39 | - |  |  | SI | Is the patient on antipsychotics, antidepressants,... |
| Q40 | - |  |  | SI | Complete medication section on Falls Risk Assessme... |
| Q41 | - |  |  | SI | Provide patient / family / carers with information... |
| Q42 | - |  |  | SI | Provide patient / family / carers with information... |
| Q43 | - |  |  | SI | Care actions for all patients |
| Q44 | - |  |  | SI | These care actions are relevant for all patients a... |
| Q45 | - |  |  | SI | • Orientate patient to bed area, toilet and ward |
| Q46 | - |  |  | SI | • Educate patient and family, providing culturally... |
| Q47 | - |  |  | SI | • Instruct patient on the use of the call bell, en... |
| Q48 | - |  |  | SI | • Ensure frequently used items (including mobility... |
| Q49 | - |  |  | SI | • Ensure bed and chair are at appropriate height f... |
| Q50 | - |  |  | SI | • Ensure bed brakes are on at all times and chair ... |
| Q51 | - |  |  | SI | • Position over-bed-table on the non exit side of ... |
| Q52 | - |  |  | SI | • Place IV pole and all other devices / attachment... |
| Q53 | - |  |  | SI | • Ensure attachments (such as catheters, wound dra... |
| Q54 | - |  |  | SI | • Remove clutter and obstacles from room |
| Q55 | - |  |  | SI | • Ensure patient is using appropriate personal aid... |
| Q56 | - |  |  | SI | • Ensure patient wears appropriate footwear when a... |
| Q57 | - |  |  | SI | • Establish patient's level of personal care need |
| Q58 | - |  |  | SI | • Ensure adequate night lighting |
| Q59 | - |  |  | SI | Provide patient / family / carers with falls preve... |
| Q60 | - |  |  | SI | Clinical Excellence Commission Falls Prevention fl... |
| Q61 | - |  |  | SI | Reproduced with permission ©Clinical Excellence Co... |
| Q62 | - |  |  | SI | Patient actions |
| Q63 | - |  |  | SI | 1. Orientation to the bed area and ward facilities... |
| Q64 | - |  |  | SI | 2. Lower bed if possible. Ensure brakes are on. |
| Q65 | - |  |  | SI | 3. Place call bell and side table within reach, an... |
| Q66 | - |  |  | SI | 4. Ensure safe footwear when mobilising ie well-fi... |
| Q67 | - |  |  | SI | 5. Provide safe footwear brochure to patient and c... |
| Q68 | - |  |  | SI | 6. Clothing to fit well and of appropriate length. |
| Q69 | - |  |  | SI | 7. Clear area of hazards-spills, clutter, unstable... |
| Q70 | - |  |  | SI | 8. Fall prevention brochure provided to patient / ... |
| Q71 | - |  |  | SI | 9. Ensure patient has access to adequate nutrition... |
| Q72 | - |  |  | SI | 10. Medication review |
| Q73 | - |  |  | SI | 11. Bone protection medication review: consider vi... |
| Q74 | - |  |  | SI | 12. Ensure that patient has their glasses and hear... |
| Q75 | - |  |  | SI | 13. Falls identifiers used (sign & sticker). |
| Q76 | - |  |  | SI | 14. Supervise patient during mobilisation. |
| Q77 | - |  |  | SI | 15. Supervise patient during self care and toileti... |
| Q78 | - |  |  | SI | 16. Supervise patient with nutrition and hydration... |
| Q79 | - |  |  | SI | 17. Regular toileting regimen, and prior to settli... |
| Q80 | - |  |  | SI | 18. Use non-slip matting by the bed. |
| Q81 | - |  |  | SI | 19. Referral to physiotherapy and/or occupational ... |
| Q82 | - |  |  | SI | 20. Do not leave patient unattended during planned... |
| Q83 | - |  |  | SI | 21. Locate patient close to the nurses station. |
| Q84 | - |  |  | SI | 22. Ensure bed height is appropriate to the needs ... |
| Q85 | - |  |  | SI | 23. Consider constant observation - particularly i... |
| Q86 | - |  |  | SI | 24. Consider use of hip protectors |
| Q87 | - |  |  | SI | Low risk : 0 – 5 points |
| Q88 | - |  |  | SI | Medium risk : 6 – 16 points (all of the above plus... |
| Q89 | - |  |  | SI | High risk : 17 – 30 points (all of the above plus,... |
| Q90 | - |  |  | SI | Papaioannou A. et al. Prediction of falls using a ... |
| Q91 | - |  |  | SI | Best Practice Risk Assessment Adjustments (Clinica... |
| Q92 | - |  |  | SI | 1. Falls Guidelines Review Expert Advisory Group o... |
| Q93 | - |  |  | SI | Preventing Falls and Harm From Falls in Older Peop... |
| Q94 | - |  |  | SI | 2. Papaioannou A, Parkinson W, Cook R, Ferko N, Co... |
| Q95 | - |  |  | SI | 3. Oliver D, Britton M, Seed P, Martin FC, Hopper ... |
| Q96 | - |  |  | SI | Development and evaluation of evidence based risk ... |
| Q97 | - |  |  | SI | (1) published by the Australian Commission on Safe... |
| Q98 | - |  |  | SI | (2) Which is itself an adaptation of a British fal... |
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