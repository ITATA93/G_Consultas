# questionnaire.QGXXXOPH15

> Neuro-Ophthalmology

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neuro-Ophthalmology

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Pupils |
| Q02 | varchar |  |  | SI | Right Eye |
| Q03 | varchar |  |  | SI | Left Eye |
| Q04 | varchar |  |  | SI | Dim |
| Q05 | varchar |  |  | SI | Dim 2 |
| Q06 | varchar |  |  | SI | Light |
| Q07 | varchar |  |  | SI | Light 2 |
| Q08 | varchar |  |  | SI | Near ` |
| Q09 | varchar |  |  | SI | Near 2 |
| Q10 | varchar |  |  | SI | APD |
| Q11 | varchar |  |  | SI | APD 2 |
| Q12 | varchar |  |  | SI | Adnexa |
| Q13 | varchar |  |  | SI | Ptosis |
| Q14 | varchar |  |  | SI | Right Eye |
| Q15 | varchar |  |  | SI | Left Eye |
| Q16 | varchar |  |  | SI | PF |
| Q17 | varchar |  |  | SI | PF 2 |
| Q18 | varchar |  |  | SI | LF |
| Q19 | varchar |  |  | SI | LF 2 |
| Q20 | varchar |  |  | SI | MRD  |
| Q21 | varchar |  |  | SI | MRD 2 |
| Q22 | varchar |  |  | SI | Orbicularis weakness |
| Q23 | varchar |  |  | SI | Fatigability |
| Q24 | varchar |  |  | SI | Proptosis |
| Q25 | varchar |  |  | SI | Exophthalmometer |
| Q26 | varchar |  |  | SI | Exophthalmometer 2 |
| Q27 | varchar |  |  | SI | Lid lag |
| Q28 | varchar |  |  | SI | Fundus |
| Q29 | varchar |  |  | SI | Neuro Exam |
| Q30 | varchar |  |  | SI | Orbicularis weakness |
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