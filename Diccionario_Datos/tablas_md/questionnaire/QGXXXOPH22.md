# questionnaire.QGXXXOPH22

> Retina & Vitreous

**Schema:** questionnaire
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Retina & Vitreous

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Informed consent? |
| Q02 | date |  |  | SI | Date |
| Q03 | varchar |  |  | SI | Red Reflex abnormal |
| Q04 | varchar |  |  | SI | Right Eye |
| Q05 | varchar |  |  | SI | Left Eye |
| Q06 | varchar |  |  | SI | red |
| Q07 | varchar |  |  | SI | red2 |
| Q08 | varchar |  |  | SI | Notes |
| Q09 | varchar |  |  | SI | Notes |
| Q10 | varchar |  |  | SI | Vitrous abnormal |
| Q11 | varchar |  |  | SI | Right Eye |
| Q12 | varchar |  |  | SI | Left Eye |
| Q13 | varchar |  |  | SI | Vit |
| Q14 | varchar |  |  | SI | Vit2 |
| Q15 | varchar |  |  | SI | Notes |
| Q16 | varchar |  |  | SI | Notes  |
| Q17 | varchar |  |  | SI | Optic Nerve abnormal |
| Q18 | varchar |  |  | SI | Manula abnormal |
| Q19 | varchar |  |  | SI | Right eye |
| Q20 | varchar |  |  | SI | Left Eye |
| Q21 | varchar |  |  | SI | Macula |
| Q22 | varchar |  |  | SI | macula 2 |
| Q23 | varchar |  |  | SI | notes |
| Q24 | varchar |  |  | SI | notes 2 |
| Q25 | varchar |  |  | SI | Vessles abnormal |
| Q26 | varchar |  |  | SI | Vessles |
| Q27 | varchar |  |  | SI | Vessles 2 |
| Q28 | varchar |  |  | SI | notes |
| Q29 | varchar |  |  | SI | notes 2 |
| Q30 | varchar |  |  | SI | Periphery anormal |
| Q31 | varchar |  |  | SI | peri |
| Q32 | varchar |  |  | SI | Peri 2 |
| Q33 | varchar |  |  | SI | Notes |
| Q34 | varchar |  |  | SI | Notes 2 |
| Q35 | time |  |  | SI | Time |
| Q36 | varchar |  |  | SI | Retina |
| Q37 | varchar |  |  | SI | Retina 2 |
| Q40 | varchar |  |  | SI | Detachment Type |
| Q41 | varchar |  |  | SI | Detachment type 2 |
| Q42 | varchar |  |  | SI | PVR grading |
| Q43 | varchar |  |  | SI | PVR grading |
| Q44 | varchar |  |  | SI | Notes |
| Q441 | varchar |  |  | SI | Right Eye |
| Q45 | varchar |  |  | SI | Notes 2 |
| Q451 | varchar |  |  | SI | Left Eye |
| Q46 | varchar |  |  | SI | Optic Nerve |
| Q47 | varchar |  |  | SI | Optic Nerve 2 |
| Q48 | varchar |  |  | SI | Macula Abnormal |
| Q49 | varchar |  |  | SI | Vitreous Abnormal |
| Q50 | varchar |  |  | SI | Vitreous normal left |
| Q51 | varchar |  |  | SI | Optic nerve abnormal left |
| Q52 | varchar |  |  | SI | Retina abnormal 2 |
| Q53 | varchar |  |  | SI | Manula abnormal 2 |
| Q54 | varchar |  |  | SI | Vessles abnomal |
| Q55 | varchar |  |  | SI | Periphery abnormal |
| Q56 | varchar |  |  | SI | Periphery abnormal 2 |
| Q57 | varchar |  |  | SI | Red reflex abnorml 2 |
| Q58 | varchar |  |  | SI | Image Annotation |
| Q59 | varchar |  |  | SI | Image Link |
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