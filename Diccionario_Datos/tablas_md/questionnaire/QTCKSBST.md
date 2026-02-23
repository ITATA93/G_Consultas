# questionnaire.QTCKSBST

> The Keele STarT Back Screening Tool

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* The Keele STarT Back Screening Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Thinking about the last 2 weeks tick your response... |
| Q04 | varchar |  |  | SI | 1- My back pain has spread down my leg(s) at some ... |
| Q05 | varchar |  |  | SI | 2- I have had pain in the shoulder or neck at some... |
| Q06 | varchar |  |  | SI | 3- I have only walked short distances because of m... |
| Q07 | varchar |  |  | SI | 4- In the last 2 weeks, I have dressed more slowly... |
| Q08 | varchar |  |  | SI | 5- It's not really safe for a person with a condit... |
| Q09 | varchar |  |  | SI | 6- Worrying thoughts have been going through my mi... |
| Q10 | varchar |  |  | SI | 7- I feel that my back pain is terrible and it's n... |
| Q11 | varchar |  |  | SI | 8- In general I have not enjoyed all the things I ... |
| Q12 | varchar |  |  | SI | 9- Overall, how bothersome has your back pain been... |
| Q13 | varchar |  |  | SI | Sub score (Q5-9) |
| Q14 | varchar |  |  | SI | Total score |
| Q15 | varchar |  |  | SI | Classification |
| Q16 | varchar |  |  | SI | ≤ 3 |
| Q17 | varchar |  |  | SI | Low risk |
| Q18 | varchar |  |  | SI | ≥ 4 |
| Q19 | varchar |  |  | SI | ≤ 3 |
| Q20 | varchar |  |  | SI | Medium risk |
| Q21 | varchar |  |  | SI | ≥ 4 |
| Q22 | varchar |  |  | SI |  ≥ 4 |
| Q23 | varchar |  |  | SI | High risk |
| Q24 | varchar |  |  | SI | Sub score (Q5-9) |
| Q25 | varchar |  |  | SI | The Keele STarT Back Screening Tool (9-item versio... |
| Q26 | varchar |  |  | SI | Total Score ≤ 3: Low risk |
| Q27 | varchar |  |  | SI | Total score ≥ 4 and Sub score (Q5-9) ≤ 3: Medium r... |
| Q28 | varchar |  |  | SI | Total score ≥ 4 and Sub score (Q5-9) ≥ 4: High ris... |
| Q29 | varchar |  |  | SI | Total score |
| Q30 | varchar |  |  | SI | designed to screen primary care patients with low ... |
| Q31 | varchar |  |  | SI | Sub score (Q5-9) calculated |
| Q32 | varchar |  |  | SI | Sub score (Q5-9) |
| Q33 | varchar |  |  | SI | Total score |
| Q34 | varchar |  |  | SI | Total score |
| Q35 | varchar |  |  | SI | Total score |
| Q36 | varchar |  |  | SI | Sub score (Q5-9) |
| Q37 | varchar |  |  | SI | Sub score (Q5-9) |
| Q38 | varchar |  |  | SI | Classification |
| Q39 | varchar |  |  | SI | Classification |
| Q40 | varchar |  |  | SI | Classification |
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