# questionnaire.QTCALSFRSR

> Revised Amyotrophic Lateral Sclerosis Functional Rating Scale Revised (ALSFRS - R)

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Revised Amyotrophic Lateral Sclerosis Functional Rating Scale Revised (ALSFRS - R)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Speech |
| Q02 | varchar |  |  | SI | Salivation |
| Q03 | varchar |  |  | SI | Swallowing |
| Q04 | varchar |  |  | SI | Handwriting |
| Q05 | varchar |  |  | SI | Patients with gastrostomy and >50% daily nutrition... |
| Q06 | varchar |  |  | SI | Cutting food and handling utensils Patients withou... |
| Q07 | varchar |  |  | SI | Cutting food and handling utensils Patients with g... |
| Q08 | varchar |  |  | SI | Dressing and hygiene |
| Q09 | varchar |  |  | SI | Turning in bed and adjusting bed clothes |
| Q10 | varchar |  |  | SI | Walking |
| Q11 | varchar |  |  | SI | Climbing stairs |
| Q12 | varchar |  |  | SI | Dyspnea |
| Q13 | varchar |  |  | SI | Orthopnea |
| Q14 | varchar |  |  | SI | Respiratory insufficiency |
| Q15 | varchar |  |  | SI | Score |
| Q16 | varchar |  |  | SI | Classification |
| Q17 | varchar |  |  | SI | ≤15 |
| Q18 | varchar |  |  | SI | ≤25% 9-month survival |
| Q19 | varchar |  |  | SI | 16-20 |
| Q20 | varchar |  |  | SI | ~25-40% 9-month survival |
| Q21 | varchar |  |  | SI | 21-25 |
| Q22 | varchar |  |  | SI | ~40-60% 9-month survival |
| Q23 | varchar |  |  | SI | 26-30 |
| Q24 | varchar |  |  | SI | ~60-70% 9-month survival |
| Q25 | varchar |  |  | SI | 31-35 |
| Q26 | varchar |  |  | SI | ~70-80% 9-month survival |
| Q27 | varchar |  |  | SI | 36-40 |
| Q28 | varchar |  |  | SI | ~80-90% 9-month survival |
| Q29 | varchar |  |  | SI | ≥41 |
| Q30 | varchar |  |  | SI | >90% 9-month survival |
| Q31 | varchar |  |  | SI | <=15: <=25% 9-month survival |
| Q32 | varchar |  |  | SI | 16-20: ~25-40% 9-month survival |
| Q33 | varchar |  |  | SI | 21-25: ~25-40% 9-month survival |
| Q34 | varchar |  |  | SI | 26-30: ~60-70% 9-month survival |
| Q35 | varchar |  |  | SI | 31-35: ~70-80% 9-month survival |
| Q36 | varchar |  |  | SI | 36-40: ~80-90% 9-month survival |
| Q37 | varchar |  |  | SI | <=41: >90% 9-month survival |
| Q38 | varchar |  |  | SI | The Revised Amyotrophic Lateral Sclerosis Function... |
| Q39 | varchar |  |  | SI | for Patients with ALS (Amyotrophic Lateral Scleros... |
| Q40 | varchar |  |  | SI | Figures are approximate and estimated as per refer... |
| Q41 | varchar |  |  | SI | Cedarbaum JM, Stambler N. Performance of the Amyot... |
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