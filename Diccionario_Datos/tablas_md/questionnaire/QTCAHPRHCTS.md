# questionnaire.QTCAHPRHCTS

> The Clinical Test of Sensory Interaction of Balance

**Schema:** questionnaire
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* The Clinical Test of Sensory Interaction of Balance

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Functional Reach Left |
| Q02 | varchar |  |  | SI | Functional Reach Right |
| Q03 | varchar |  |  | SI | Step Test (15 secs) Left Up |
| Q04 | varchar |  |  | SI | Step Test (15 secs) Right Up |
| Q05 | varchar |  |  | SI | Smart Balance Master Assessment |
| Q06 | varchar |  |  | SI | Composite Score (SOT) |
| Q07 | varchar |  |  | SI | Test |
| Q08 | varchar |  |  | SI | Position |
| Q09 | varchar |  |  | SI | (score time up to 30 sec) |
| Q10 | varchar |  |  | SI | Surface |
| Q11 | varchar |  |  | SI | Eyes |
| Q12 | varchar |  |  | SI | FA |
| Q13 | varchar |  |  | SI | FT |
| Q14 | varchar |  |  | SI | Tandem Left |
| Q15 | varchar |  |  | SI | Tandem Right |
| Q16 | varchar |  |  | SI | SLS Left |
| Q17 | varchar |  |  | SI | SLS Right |
| Q18 | varchar |  |  | SI | Firm |
| Q19 | varchar |  |  | SI | Open |
| Q20 | varchar |  |  | SI | Firm Surface, Open Eyes, FA |
| Q21 | varchar |  |  | SI | Firm Surface, Open Eyes, FT |
| Q22 | varchar |  |  | SI | Firm Surface, Open Eyes, Tandem Left |
| Q23 | varchar |  |  | SI | Firm Surface, Open Eyes, Tandem Right |
| Q24 | varchar |  |  | SI | Firm Surface, Open Eyes, SLS Left |
| Q25 | varchar |  |  | SI | Firm Surface, Open Eyes, SLS Right |
| Q26 | varchar |  |  | SI | Firm |
| Q27 | varchar |  |  | SI | Closed |
| Q28 | varchar |  |  | SI | Firm Surface, Closed Eyes, FA |
| Q29 | varchar |  |  | SI | Firm Surface, Closed Eyes, FT |
| Q30 | varchar |  |  | SI | Firm Surface, Closed Eyes, Tandem Left |
| Q31 | varchar |  |  | SI | Firm Surface, Closed Eyes, Tandem Right |
| Q32 | varchar |  |  | SI | Firm Surface, Closed Eyes, SLS Left |
| Q33 | varchar |  |  | SI | Firm Surface, Closed Eyes, SLS Right |
| Q34 | varchar |  |  | SI | Foam / Soft |
| Q35 | varchar |  |  | SI | Open |
| Q36 | varchar |  |  | SI | Foam/Soft Surface, Open Eyes, FA |
| Q37 | varchar |  |  | SI | Foam/Soft Surface, Open Eyes, FT |
| Q38 | varchar |  |  | SI | Foam/Soft Surface, Open Eyes, Tandem Left |
| Q39 | varchar |  |  | SI | Foam/Soft Surface, Open Eyes, Tandem Right |
| Q40 | varchar |  |  | SI | Foam/Soft Surface, Open Eyes, SLS Left |
| Q41 | varchar |  |  | SI | Foam/Soft Surface, Open Eyes, SLS Right |
| Q42 | varchar |  |  | SI | Foam / Soft |
| Q43 | varchar |  |  | SI | Closed |
| Q44 | varchar |  |  | SI | Foam/Soft Surface, Closed Eyes, FA |
| Q45 | varchar |  |  | SI | Foam/Soft Surface, Closed Eyes, FT |
| Q46 | varchar |  |  | SI | Foam/Soft Surface, Closed Eyes, Tandem Left |
| Q47 | varchar |  |  | SI | Foam/Soft Surface, Closed Eyes, Tandem Right |
| Q48 | varchar |  |  | SI | Foam/Soft Surface, Closed Eyes, SLS Left |
| Q49 | varchar |  |  | SI | Foam/Soft Surface, Closed Eyes, SLS Right |
| Q50 | varchar |  |  | SI | Comments |
| Q51 | varchar |  |  | SI | Limits of Stability (Internal / External Perturbat... |
| Q52 | varchar |  |  | SI | Ankle Strategy |
| Q53 | varchar |  |  | SI | Hip Strategy |
| Q54 | varchar |  |  | SI | Step Strategy |
| Q55 | varchar |  |  | SI | The Clinical Test of Sensory Interaction of Balanc... |
| Q56 | varchar |  |  | SI | Balance Measures |
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