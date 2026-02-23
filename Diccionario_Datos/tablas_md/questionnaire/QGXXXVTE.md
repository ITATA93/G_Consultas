# questionnaire.QGXXXVTE

> Venous Thromboembolism Risk Assessment (VTE)

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Venous Thromboembolism Risk Assessment (VTE)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Surgical VTE Risk |
| Q02 | varchar |  |  | SI | Recommended VTE prophylaxis |
| Q03 | varchar |  |  | SI | Recommended VTE prophylaxis Freetext 1 |
| Q04 | varchar |  |  | SI | Recommended VTE prophylaxis Freetext 2 |
| Q05 | varchar |  |  | SI | Recommended VTE prophylaxis Freetext 3 |
| Q06 | varchar |  |  | SI | Recommended VTE prophylaxis Freetext 4 |
| Q07 | varchar |  |  | SI | Recommended VTE prophylaxis Freetext 5 |
| Q08 | varchar |  |  | SI | Recommended VTE prophylaxis Freetext 6 |
| Q09 | varchar |  |  | SI | Recommended VTE prophylaxis Freetext 7 |
| Q10 | varchar |  |  | SI | Recommended VTE prophylaxis Freetext 8 |
| Q13 | varchar |  |  | SI | Medical VTE Risk |
| Q16 | varchar |  |  | SI | Are there any contraindications to chemical or mec... |
| Q17 | varchar |  |  | SI | Chemical  |
| Q19 | varchar |  |  | SI | Note |
| Q20 | varchar |  |  | SI | Prophylaxis required? |
| Q21 | varchar |  |  | SI | 0 - 3: Low risk |
| Q22 | varchar |  |  | SI | >= 5: High risk |
| Q23 | varchar |  |  | SI | The Venous Thromboembolism Risk Assessment assesse... |
| Q24 | date |  |  | SI | Date |
| Q25 | varchar |  |  | SI | HIGH |
| Q25a | bit |  |  | SI | Hip arthroplasty |
| Q25b | bit |  |  | SI | Knee arthroplasty  |
| Q25c | bit |  |  | SI | Major trauma  |
| Q25d | bit |  |  | SI | Hip fracture surgery  |
| Q25e | bit |  |  | SI | Other surgery with prior VTE and/or active cancer  |
| Q25f | bit |  |  | SI | Major surgery and age >40 yrs  |
| Q25g | varchar |  |  | SI | (Major surgery refers to intra-abdominal surgery a... |
| Q25h | bit |  |  | SI | Other risk (please state) |
| Q26 | varchar |  |  | SI | LOWER |
| Q26a | bit |  |  | SI | All other surgery |
| Q26b | bit |  |  | SI | All other surgery with additional VTE risk factors |
| Q27 | varchar |  |  | SI | HIGH |
| Q27a | bit |  |  | SI | Ischaemic stroke  |
| Q27b | bit |  |  | SI | History of VTE |
| Q27c | bit |  |  | SI | Active cancer  |
| Q27e | bit |  |  | SI | Decompensated heart failure  |
| Q27f | bit |  |  | SI | Acute or chronic lung disease |
| Q27g | bit |  |  | SI | Acute inflammatory disease  |
| Q27h | bit |  |  | SI | Age > 60 years  |
| Q27i | bit |  |  | SI | Other risk (please state) |
| Q28 | varchar |  |  | SI | LOW |
| Q28a | bit |  |  | SI | None of the above risk factors |
| Q43 | varchar |  |  | SI | Mechanical |
| Q44 | time |  |  | SI | Time |
| Q45 | varchar |  |  | SI | Score |
| Q46 | varchar |  |  | SI | Classification |
| Q47 | varchar |  |  | SI | 0 - 3 |
| Q48 | varchar |  |  | SI | Low risk |
| Q49 | varchar |  |  | SI | >= 5 |
| Q50 | varchar |  |  | SI | High risk |
| Q51 | varchar |  |  | SI | Comment |
| Q52 | varchar |  |  | SI | Comment |
| Q53 | varchar |  |  | SI | !!!These are examples and must be verified by a do... |
| Q54 | varchar |  |  | SI | Planned interventions |
| Q55 | varchar |  |  | SI | Score to be visualized and verified by the physici... |
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