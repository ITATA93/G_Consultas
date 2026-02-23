# questionnaire.QTCTUGT

> Timed Up and Go Test (TUGT)

**Schema:** questionnaire
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Timed Up and Go Test (TUGT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of test |
| Q02 | time |  |  | SI | Time of test |
| Q03 | varchar |  |  | SI | Gait aid |
| Q04 | varchar |  |  | SI | Time taken to complete test (in secs) |
| Q05 | varchar |  |  | SI | Stopped to rest? |
| Q06 | varchar |  |  | SI | Comments |
| Q07 | varchar |  |  | SI | General Information |
| Q08 | varchar |  |  | SI | • The patient starts in a seated position. |
| Q09 | varchar |  |  | SI | • The patient stands up upon therapist’s command: ... |
| Q10 | varchar |  |  | SI | • The time starts on the word GO and stops when th... |
| Q11 | varchar |  |  | SI | • The subject is allowed to use an assistive devic... |
| Q12 | varchar |  |  | SI | • They may stop and rest (but not sit down) if the... |
| Q13 | varchar |  |  | SI | • A practice trial should be completed before the ... |
| Q14 | varchar |  |  | SI | Set up |
| Q15 | varchar |  |  | SI | • Place a piece of tape or other marker on the flo... |
| Q16 | varchar |  |  | SI | Patient Instructions |
| Q17 | varchar |  |  | SI | • 'My commands for this test are going to be ‘read... |
| Q18 | varchar |  |  | SI | • Once you are up, you may take any path you like,... |
| Q19 | varchar |  |  | SI | • Turn around and walk back to the chair. I will s... |
| Q20 | varchar |  |  | SI | Population |
| Q21 | varchar |  |  | SI | Threshold indicating falls risk |
| Q22 | varchar |  |  | SI | Hip osteoarthritis |
| Q23 | varchar |  |  | SI | > 10 seconds |
| Q24 | varchar |  |  | SI | Older stroke patients |
| Q25 | varchar |  |  | SI | > 14 seconds |
| Q26 | varchar |  |  | SI | Community-dwelling elderly |
| Q27 | varchar |  |  | SI | > 13.5 seconds |
| Q28 | varchar |  |  | SI | Lower extremity amputees |
| Q29 | varchar |  |  | SI | > 19 seconds |
| Q30 | varchar |  |  | SI | 0: No score was recorded |
| Q31 | varchar |  |  | SI | 5: ≤5 seconds  - Please review the interpretation ... |
| Q32 | varchar |  |  | SI | 6: 6 seconds  - Please review the interpretation o... |
| Q33 | varchar |  |  | SI | 7: 7 seconds  - Please review the interpretation o... |
| Q34 | varchar |  |  | SI | 8: 8 seconds  - Please review the interpretation o... |
| Q35 | varchar |  |  | SI | 9: 9 seconds  - Please review the interpretation o... |
| Q36 | varchar |  |  | SI | 10: 10 seconds  - Please review the interpretation... |
| Q37 | varchar |  |  | SI | 11: 11 seconds  - Please review the interpretation... |
| Q38 | varchar |  |  | SI | 12: 12 seconds  - Please review the interpretation... |
| Q39 | varchar |  |  | SI | 13: 13 seconds  - Please review the interpretation... |
| Q40 | varchar |  |  | SI | 14: 14 seconds  - Please review the interpretation... |
| Q41 | varchar |  |  | SI | 15: 15 seconds  - Please review the interpretation... |
| Q42 | varchar |  |  | SI | 16: 16 seconds  - Please review the interpretation... |
| Q43 | varchar |  |  | SI | 17: 17 seconds  - Please review the interpretation... |
| Q44 | varchar |  |  | SI | 18: 18 seconds  - Please review the interpretation... |
| Q45 | varchar |  |  | SI | 19: 19 seconds  - Please review the interpretation... |
| Q46 | varchar |  |  | SI | 20: ≥20 seconds - Please review the interpretation... |
| Q47 | varchar |  |  | SI | The Timed Up and Go Test (TUGT) is used to determi... |
| Q48 | varchar |  |  | SI | Test outcome |
| Q49 | numeric |  |  | SI | Time taken to complete test (in seconds) |
| Q50 | date |  |  | SI | Date |
| Q51 | time |  |  | SI | Time |
| Q52 | numeric |  |  | SI | Time taken to complete test (in seconds) |
| Q53 | varchar |  |  | SI | If other,&nbsp;Gait aid |
| Q54 | varchar |  |  | SI | The timed Up and Go test was described Podsiadlo a... |
| Q55 | varchar |  |  | SI | 1. Podsiadlo D, Richardson S. The Timed “Up &amp; ... |
| Q56 | varchar |  |  | SI | 2. Mathias S, Nayak US, Isaacs B. Balance in elder... |
| Q57 | varchar |  |  | SI | 3. Dite W, Connor HJ, Curtis HC. Clinical Identifi... |
| Q58 | varchar |  |  | SI | 4. Shumway-Cook A, Brauer S, Woollacott M. Predict... |
| Q59 | varchar |  |  | SI | 5. Arnold CM, Faulkner RA. The history of falls an... |
| Q60 | varchar |  |  | SI | 6. Andersson Å, Kamwendo K, Seiger Å, Appelros P. ... |
| Q61 | varchar |  |  | SI | Population |
| Q62 | varchar |  |  | SI | Threshold TUG test for patients at risk of falling |
| Q63 | varchar |  |  | SI | Unilateral trans-tibial amputation |
| Q64 | varchar |  |  | SI | ≥19 seconds |
| Q65 | varchar |  |  | SI | Community-dwelling older adults |
| Q66 | varchar |  |  | SI | ≥13.5 seconds |
| Q67 | varchar |  |  | SI | Older adults with hip osteoarthritis |
| Q68 | varchar |  |  | SI | ≥10 seconds (falls and near falls) |
| Q69 | varchar |  |  | SI | Patients following a cerebrovascular accident |
| Q70 | varchar |  |  | SI | ≥14 seconds |
| Q71 | varchar |  |  | SI | older adults with hip osteoarthritis(5), and patie... |
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