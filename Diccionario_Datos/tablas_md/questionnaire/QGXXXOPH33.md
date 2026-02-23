# questionnaire.QGXXXOPH33

> Contact Lens Diagnosis

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Contact Lens Diagnosis

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Diagnosis Contact Lens |
| Q02 | date |  |  | SI | Date |
| Q03 | varchar |  |  | SI | Type / Brand |
| Q04 | varchar |  |  | SI | Right Eye |
| Q05 | varchar |  |  | SI | Left Eye |
| Q07 | varchar |  |  | SI | BC |
| Q08 | varchar |  |  | SI | bc 2 |
| Q09 | varchar |  |  | SI | Power |
| Q10 | varchar |  |  | SI | Power 2 |
| Q11 | varchar |  |  | SI | Diameter |
| Q12 | varchar |  |  | SI | Diameter 2 |
| Q13 | varchar |  |  | SI | Optic zone |
| Q14 | varchar |  |  | SI | Optic zone 2 |
| Q15 | varchar |  |  | SI | Design |
| Q16 | varchar |  |  | SI | design 2 |
| Q17 | varchar |  |  | SI | Tint |
| Q18 | varchar |  |  | SI | tint 2 |
| Q200 | varchar |  |  | SI | Notes |
| Q201 | varchar |  |  | SI | Notes |
| Q202 | varchar |  |  | SI | Contact Lens image |
| Q21 | varchar |  |  | SI | Material |
| Q22 | varchar |  |  | SI | Material 2 |
| Q25 | varchar |  |  | SI | Notes |
| Q26 | varchar |  |  | SI | Final Contact Lens Prescription |
| Q27 | date |  |  | SI | Date |
| Q28 | varchar |  |  | SI | Type / Brand |
| Q29 | varchar |  |  | SI | Right Eye |
| Q30 | varchar |  |  | SI | Left Eye |
| Q32 | varchar |  |  | SI | BC |
| Q33 | varchar |  |  | SI | bc2 |
| Q34 | varchar |  |  | SI | Power |
| Q35 | varchar |  |  | SI | power 2 |
| Q36 | varchar |  |  | SI | Diameter |
| Q37 | varchar |  |  | SI | diaeter 2 |
| Q38 | varchar |  |  | SI | Optic zone |
| Q39 | varchar |  |  | SI | optic zone 2 |
| Q40 | varchar |  |  | SI | Design |
| Q41 | varchar |  |  | SI | design 2 |
| Q42 | varchar |  |  | SI | Tint  |
| Q43 | varchar |  |  | SI | tint 2 |
| Q44 | varchar |  |  | SI | Cosmetic Contact Lens |
| Q45 | varchar |  |  | SI | Iris colour |
| Q46 | varchar |  |  | SI | Iris diameter |
| Q47 | varchar |  |  | SI | VA-Nr 3 |
| Q48 | varchar |  |  | SI | Material  |
| Q49 | varchar |  |  | SI | Material 2 |
| Q50 | varchar |  |  | SI | Opaque |
| Q51 | varchar |  |  | SI | Pupil |
| Q52 | varchar |  |  | SI | Pupil size |
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