# SQLUser.PA_AlertMsg

**Schema:** SQLUser
**Columnas:** 142
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALM_PAPMI_ParRef | bigint | PK |  | NO | Des Ref to PAPMI |
| ALM_ActionTaken | varchar |  |  | SI | Action |
| ALM_AlertCategory_DR | bigint |  | FK | SI | Des Ref AlertCategory |
| ALM_Alert_DR | bigint |  | FK | SI | Des Ref Alert |
| ALM_ChildSub | double |  |  | NO | Alert Message ChildSub |
| ALM_ClosedDate | date |  |  | SI | Closed Date |
| ALM_ClosedFlag | varchar |  |  | SI | Closed Flag |
| ALM_ClosedTime | time |  |  | SI | Closed Time |
| ALM_CreateDate | date |  |  | SI | Date Created |
| ALM_CreateTime | time |  |  | SI | Time Created |
| ALM_CreateUser | bigint |  |  | SI | User Created |
| ALM_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| ALM_DisplayAlert | varchar |  |  | SI | DisplayAlert |
| ALM_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| ALM_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| ALM_ExpiryDate | date |  |  | SI | Expiry Date |
| ALM_ExpiryReason_DR | bigint |  | FK | SI | Des Ref ExpiryReason |
| ALM_ExternalID | varchar |  |  | SI | ExternalID |
| ALM_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| ALM_Mess_1 | varchar |  |  | SI | Message 1st line |
| ALM_Message | varchar |  |  | SI | Patient Message |
| ALM_OnsetDate | date |  |  | SI | Onset Date |
| ALM_OnsetTime | time |  |  | SI | Onset Time |
| ALM_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref - Reason For Correction |
| ALM_ReviewDate | date |  |  | SI | Review Date |
| ALM_RowId | varchar |  |  | NO | - |
| ALM_SourceOfAlert_DR | bigint |  | FK | SI | Des Ref SourceOfAlert |
| ALM_Status | varchar |  |  | SI | Status |
| ALM_ViewDate | date |  |  | SI | Date Viewed |
| ALM_ViewTime | time |  |  | SI | Time Viewed |
| ALM_ViewUserId | bigint |  |  | SI | User ID View |
| Q01 | - |  |  | SI | Date of test |
| Q02 | - |  |  | SI | Time of test |
| Q03 | - |  |  | SI | Gait aid |
| Q04 | - |  |  | SI | Time taken to complete test (in secs) |
| Q05 | - |  |  | SI | Stopped to rest? |
| Q06 | - |  |  | SI | Comments |
| Q07 | - |  |  | SI | General Information |
| Q08 | - |  |  | SI | • The patient starts in a seated position. |
| Q09 | - |  |  | SI | • The patient stands up upon therapist’s command: ... |
| Q10 | - |  |  | SI | • The time starts on the word GO and stops when th... |
| Q11 | - |  |  | SI | • The subject is allowed to use an assistive devic... |
| Q12 | - |  |  | SI | • They may stop and rest (but not sit down) if the... |
| Q13 | - |  |  | SI | • A practice trial should be completed before the ... |
| Q14 | - |  |  | SI | Set up |
| Q15 | - |  |  | SI | • Place a piece of tape or other marker on the flo... |
| Q16 | - |  |  | SI | Patient Instructions |
| Q17 | - |  |  | SI | • 'My commands for this test are going to be ‘read... |
| Q18 | - |  |  | SI | • Once you are up, you may take any path you like,... |
| Q19 | - |  |  | SI | • Turn around and walk back to the chair. I will s... |
| Q20 | - |  |  | SI | Population |
| Q21 | - |  |  | SI | Threshold indicating falls risk |
| Q22 | - |  |  | SI | Hip osteoarthritis |
| Q23 | - |  |  | SI | > 10 seconds |
| Q24 | - |  |  | SI | Older stroke patients |
| Q25 | - |  |  | SI | > 14 seconds |
| Q26 | - |  |  | SI | Community-dwelling elderly |
| Q27 | - |  |  | SI | > 13.5 seconds |
| Q28 | - |  |  | SI | Lower extremity amputees |
| Q29 | - |  |  | SI | > 19 seconds |
| Q30 | - |  |  | SI | 0: No score was recorded |
| Q31 | - |  |  | SI | 5: ≤5 seconds  - Please review the interpretation ... |
| Q32 | - |  |  | SI | 6: 6 seconds  - Please review the interpretation o... |
| Q33 | - |  |  | SI | 7: 7 seconds  - Please review the interpretation o... |
| Q34 | - |  |  | SI | 8: 8 seconds  - Please review the interpretation o... |
| Q35 | - |  |  | SI | 9: 9 seconds  - Please review the interpretation o... |
| Q36 | - |  |  | SI | 10: 10 seconds  - Please review the interpretation... |
| Q37 | - |  |  | SI | 11: 11 seconds  - Please review the interpretation... |
| Q38 | - |  |  | SI | 12: 12 seconds  - Please review the interpretation... |
| Q39 | - |  |  | SI | 13: 13 seconds  - Please review the interpretation... |
| Q40 | - |  |  | SI | 14: 14 seconds  - Please review the interpretation... |
| Q41 | - |  |  | SI | 15: 15 seconds  - Please review the interpretation... |
| Q42 | - |  |  | SI | 16: 16 seconds  - Please review the interpretation... |
| Q43 | - |  |  | SI | 17: 17 seconds  - Please review the interpretation... |
| Q44 | - |  |  | SI | 18: 18 seconds  - Please review the interpretation... |
| Q45 | - |  |  | SI | 19: 19 seconds  - Please review the interpretation... |
| Q46 | - |  |  | SI | 20: ≥20 seconds - Please review the interpretation... |
| Q47 | - |  |  | SI | The Timed Up and Go Test (TUGT) is used to determi... |
| Q48 | - |  |  | SI | Test outcome |
| Q49 | - |  |  | SI | Time taken to complete test (in seconds) |
| Q50 | - |  |  | SI | Date |
| Q51 | - |  |  | SI | Time |
| Q52 | - |  |  | SI | Time taken to complete test (in seconds) |
| Q53 | - |  |  | SI | If other,&nbsp |
| Q54 | - |  |  | SI | The timed Up and Go test was described Podsiadlo a... |
| Q55 | - |  |  | SI | 1. Podsiadlo D, Richardson S. The Timed “Up &amp |
| Q56 | - |  |  | SI | 2. Mathias S, Nayak US, Isaacs B. Balance in elder... |
| Q57 | - |  |  | SI | 3. Dite W, Connor HJ, Curtis HC. Clinical Identifi... |
| Q58 | - |  |  | SI | 4. Shumway-Cook A, Brauer S, Woollacott M. Predict... |
| Q59 | - |  |  | SI | 5. Arnold CM, Faulkner RA. The history of falls an... |
| Q60 | - |  |  | SI | 6. Andersson Å, Kamwendo K, Seiger Å, Appelros P. ... |
| Q61 | - |  |  | SI | Population |
| Q62 | - |  |  | SI | Threshold TUG test for patients at risk of falling |
| Q63 | - |  |  | SI | Unilateral trans-tibial amputation |
| Q64 | - |  |  | SI | ≥19 seconds |
| Q65 | - |  |  | SI | Community-dwelling older adults |
| Q66 | - |  |  | SI | ≥13.5 seconds |
| Q67 | - |  |  | SI | Older adults with hip osteoarthritis |
| Q68 | - |  |  | SI | ≥10 seconds (falls and near falls) |
| Q69 | - |  |  | SI | Patients following a cerebrovascular accident |
| Q70 | - |  |  | SI | ≥14 seconds |
| Q71 | - |  |  | SI | older adults with hip osteoarthritis(5), and patie... |
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