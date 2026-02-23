# questionnaire.QTCMPQ

> McGill Pain Questionnaire (MPQ)

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* McGill Pain Questionnaire (MPQ)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Sensory (S) |
| Q02 | varchar |  |  | SI | 1 |
| Q03 | varchar |  |  | SI | 2 |
| Q04 | varchar |  |  | SI | 3 |
| Q05 | varchar |  |  | SI | 4 |
| Q06 | varchar |  |  | SI | 5 |
| Q07 | varchar |  |  | SI | 6 |
| Q08 | varchar |  |  | SI | 7 |
| Q09 | varchar |  |  | SI | 8 |
| Q10 | varchar |  |  | SI | 9 |
| Q11 | varchar |  |  | SI | 10 |
| Q12 | varchar |  |  | SI | Affective (A) |
| Q13 | varchar |  |  | SI | 11 |
| Q14 | varchar |  |  | SI | 12 |
| Q15 | varchar |  |  | SI | 13 |
| Q16 | varchar |  |  | SI | 14 |
| Q17 | varchar |  |  | SI | 15 |
| Q18 | varchar |  |  | SI | Evaluative (E) |
| Q19 | varchar |  |  | SI | 16 |
| Q20 | varchar |  |  | SI | 17 |
| Q21 | varchar |  |  | SI | 18 |
| Q22 | varchar |  |  | SI | 19 |
| Q23 | varchar |  |  | SI | 20 |
| Q24 | varchar |  |  | SI | (S) Score |
| Q25 | varchar |  |  | SI | (A) Score |
| Q26 | varchar |  |  | SI | (E) Score |
| Q27 | varchar |  |  | SI | (M) Score |
| Q28 | varchar |  |  | SI | Score ranges from 0 (no pain) to 78 (severe pain) |
| Q29 | varchar |  |  | SI | Present Pain Intensity (PPI) |
| Q30 | varchar |  |  | SI | Comments |
| Q32 | varchar |  |  | SI | Repeat this section as many times as necessary |
| Q33 | varchar |  |  | SI | Accompanying symptoms |
| Q34 | varchar |  |  | SI | Comments |
| Q35 | varchar |  |  | SI | Sleep |
| Q36 | varchar |  |  | SI | Comments |
| Q37 | varchar |  |  | SI | Food intake |
| Q38 | varchar |  |  | SI | Comments |
| Q39 | varchar |  |  | SI | Activity |
| Q40 | varchar |  |  | SI | Comments |
| Q41 | varchar |  |  | SI | What Does Your Pain Feel Like? |
| Q42 | varchar |  |  | SI | Some of the words describe your present pain. Circ... |
| Q43 | varchar |  |  | SI | The McGill Pain Questionnaire (MPQ) can be used to... |
| Q44 | varchar |  |  | SI | Score Interpretation |
| Q45 | varchar |  |  | SI | Score ranges from 0 (no pain) to 78 (severe pain) |
| Q46 | varchar |  |  | SI | Score ranges from 0 (no pain) to 78 (severe pain) |
| Q47 | varchar |  |  | SI | Miscellaneous (M) |
| Q48 | date |  |  | SI | Date |
| Q49 | time |  |  | SI | Time |
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