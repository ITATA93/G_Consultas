# questionnaire.QTCFSST

> Four Square Step Test (FSST)

**Schema:** questionnaire
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Four Square Step Test (FSST)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of test |
| Q02 | time |  |  | SI | Time of test |
| Q03 | varchar |  |  | SI | Gait aid(s) used |
| Q04 | varchar |  |  | SI | Time taken to complete test (in sec) |
| Q05 | varchar |  |  | SI | Comments |
| Q06 | varchar |  |  | SI | General Information |
| Q07 | varchar |  |  | SI | The subject is required to sequentially step over ... |
| Q08 | varchar |  |  | SI | At the start of the test, the subject stands in Sq... |
| Q09 | varchar |  |  | SI | The aim is to step as fast as possible into each s... |
| Q10 | varchar |  |  | SI | Test procedure may be demonstrated, one practice t... |
| Q11 | varchar |  |  | SI | Two trials are then performed, and the better time... |
| Q12 | varchar |  |  | SI | Timing starts when the first foot contacts the flo... |
| Q13 | varchar |  |  | SI | Instructions: |
| Q14 | varchar |  |  | SI | Repeat a trial if the subject: |
| Q15 | varchar |  |  | SI | Fails to complete the sequence successfully |
| Q16 | varchar |  |  | SI | Loses balance |
| Q17 | varchar |  |  | SI | Makes contact with the cane |
| Q18 | varchar |  |  | SI | Subjects who are unable to face forward during the... |
| Q19 | varchar |  |  | SI | Any assistive device used during the test are note... |
| Q20 | varchar |  |  | SI | Set up |
| Q21 | varchar |  |  | SI | Place 4 canes / rods in a + pattern on the floor. ... |
| Q22 | varchar |  |  | SI | Patient Instructions |
| Q23 | varchar |  |  | SI | “Try to complete the sequence as fast and as safel... |
| Q24 | varchar |  |  | SI | Score |
| Q25 | varchar |  |  | SI | Classification |
| Q26 | varchar |  |  | SI | Label the lower left square 1, and move clockwise ... |
| Q27 | varchar |  |  | SI | 0 |
| Q28 | varchar |  |  | SI | A score was not recorded |
| Q29 | varchar |  |  | SI | 5 - 14 |
| Q30 | varchar |  |  | SI | Patient is NOT at potential risk for falls |
| Q31 | varchar |  |  | SI | ≥ 15 |
| Q32 | varchar |  |  | SI | Patient is at potential risk for falls |
| Q33 | varchar |  |  | SI | 0: A score was not recorded |
| Q34 | varchar |  |  | SI | 5: ≤5 seconds  - Please review the interpretation ... |
| Q35 | varchar |  |  | SI | 6: 6 seconds  - Please review the interpretation o... |
| Q36 | varchar |  |  | SI | The Four Square Step Test (FSST) is used to assess... |
| Q37 | varchar |  |  | SI | 7: 7 seconds  - Please review the interpretation o... |
| Q38 | varchar |  |  | SI | 8: 8 seconds  - Please review the interpretation o... |
| Q39 | varchar |  |  | SI | 9: 9 seconds  - Please review the interpretation o... |
| Q40 | varchar |  |  | SI | 10: 10 seconds  - Please review the interpretation... |
| Q41 | varchar |  |  | SI | 11: 11 seconds  - Please review the interpretation... |
| Q42 | varchar |  |  | SI | 12: 12 seconds  - Please review the interpretation... |
| Q43 | varchar |  |  | SI | 13: 13 seconds  - Please review the interpretation... |
| Q44 | varchar |  |  | SI | 14: 14 seconds  - Please review the interpretation... |
| Q45 | varchar |  |  | SI | 15: 15 seconds  - Please review the interpretation... |
| Q46 | varchar |  |  | SI | 16: 16 seconds  - Please review the interpretation... |
| Q47 | varchar |  |  | SI | 17: 17 seconds  - Please review the interpretation... |
| Q48 | varchar |  |  | SI | 18: 18 seconds  - Please review the interpretation... |
| Q49 | varchar |  |  | SI | 19: 19 seconds  - Please review the interpretation... |
| Q50 | varchar |  |  | SI | 20: 20 seconds  - Please review the interpretation... |
| Q51 | varchar |  |  | SI | 21: 21 seconds  - Please review the interpretation... |
| Q52 | varchar |  |  | SI | 22: 22 seconds  - Please review the interpretation... |
| Q53 | varchar |  |  | SI | 23: 23 seconds  - Please review the interpretation... |
| Q54 | varchar |  |  | SI | 24: 24 seconds  - Please review the interpretation... |
| Q55 | varchar |  |  | SI | 25: ≥25 seconds - Please review the interpretation... |
| Q56 | varchar |  |  | SI | Population |
| Q57 | varchar |  |  | SI | Threshold indicating falls risk |
| Q58 | varchar |  |  | SI | Parkinson's disease |
| Q59 | varchar |  |  | SI | > 9.68 seconds |
| Q60 | varchar |  |  | SI | Acute stroke |
| Q61 | varchar |  |  | SI | > 15 seconds |
| Q62 | varchar |  |  | SI | Geriatric population |
| Q63 | varchar |  |  | SI | > 15 seconds |
| Q64 | varchar |  |  | SI | Lower extremity amputees |
| Q65 | varchar |  |  | SI | > 24 seconds |
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