# questionnaire.QTCPASIS

> Psoriasis Area Severity Index (PASI)

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Psoriasis Area Severity Index (PASI)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Percentage of head and neck affected |
| Q04 | varchar |  |  | SI | Erythema (redness) |
| Q05 | varchar |  |  | SI | Induration (thickness) |
| Q06 | varchar |  |  | SI | Desquamation (scaling) |
| Q07 | varchar |  |  | SI | Percentage of arms affected |
| Q08 | varchar |  |  | SI | Erythema (redness) |
| Q09 | varchar |  |  | SI | Induration (thickness) |
| Q10 | varchar |  |  | SI | Desquamation (scaling) |
| Q11 | varchar |  |  | SI | Percentage of trunk affected |
| Q12 | varchar |  |  | SI | Erythema (redness) |
| Q13 | varchar |  |  | SI | Induration (thickness) |
| Q14 | varchar |  |  | SI | Desquamation (scaling) |
| Q15 | varchar |  |  | SI | Percentage of legs affected |
| Q16 | varchar |  |  | SI | Erythema (redness) |
| Q17 | varchar |  |  | SI | Induration (thickness) |
| Q18 | varchar |  |  | SI | Desquamation (scaling) |
| Q19 | varchar |  |  | SI | Total head score |
| Q20 | varchar |  |  | SI | Total trunk score |
| Q21 | varchar |  |  | SI | Total leg score |
| Q22 | varchar |  |  | SI | PASI Score |
| Q23 | varchar |  |  | SI | To use Psoriasis Area and Severity Index (PASI), t... |
| Q24 | varchar |  |  | SI | • Head -  10% of body surface area |
| Q25 | varchar |  |  | SI | • Trunk - 20% of body surface area |
| Q26 | varchar |  |  | SI | • Upper extremities - 30% of body surface area |
| Q27 | varchar |  |  | SI | • Lower extremities  - 40% of body surface area |
| Q28 | varchar |  |  | SI | The extent of psoriatic involvement of these four ... |
| Q29 | varchar |  |  | SI | 0 = No involvement |
| Q30 | varchar |  |  | SI | 1 = < 10 % |
| Q31 | varchar |  |  | SI | 2 = > 10 %, but < 30 % |
| Q32 | varchar |  |  | SI | 3 = > 30 %, but < 50 % |
| Q33 | varchar |  |  | SI | 4 = > 50 %, but < 70 % |
| Q34 | varchar |  |  | SI | 5 = > 70 %, but < 90 % |
| Q35 | varchar |  |  | SI | 6 = 90 – 100 % |
| Q36 | varchar |  |  | SI | The lesion severity is determined by assessing thr... |
| Q37 | varchar |  |  | SI | 0 = None |
| Q38 | varchar |  |  | SI | 1 = Slight |
| Q39 | varchar |  |  | SI | 2 = Moderate |
| Q40 | varchar |  |  | SI | 3 = Severe |
| Q41 | varchar |  |  | SI | 4 = Very severe |
| Q42 | varchar |  |  | SI | Total PASI = addition of PASI for each body region... |
| Q43 | varchar |  |  | SI | PASI for each body region = lesion severity x perc... |
| Q44 | varchar |  |  | SI | Lesion severity for each body region = erythema + ... |
| Q45 | varchar |  |  | SI | Psoriasis Area and Severity Index (PASI) is a wide... |
| Q46 | varchar |  |  | SI | PASI combines the assessment of the severity of le... |
| Q47 | varchar |  |  | SI | Higher the score, the more severe the disease |
| Q48 | varchar |  |  | SI | Total arm score |
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