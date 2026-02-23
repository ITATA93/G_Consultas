# questionnaire.QGXXXOPH32

> Contact Lens Evaluation

**Schema:** questionnaire
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Contact Lens Evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Habitual Refractions |
| Q02 | date |  |  | SI | Date |
| Q03 | varchar |  |  | SI | Type / Brand |
| Q04 | varchar |  |  | SI | Right Eye |
| Q05 | varchar |  |  | SI | Left Eye |
| Q06 | varchar |  |  | SI | Both Eyes |
| Q07 | varchar |  |  | SI | Base curve |
| Q08 | varchar |  |  | SI | bc 2 |
| Q09 | varchar |  |  | SI | Sphere |
| Q10 | varchar |  |  | SI | Sph2 |
| Q11 | varchar |  |  | SI | Cylinder |
| Q12 | varchar |  |  | SI | Cyl 2 |
| Q13 | varchar |  |  | SI | Axis |
| Q14 | varchar |  |  | SI | axis 2 |
| Q15 | varchar |  |  | SI | Visual acuity - Distance |
| Q16 | varchar |  |  | SI | va-dt2 |
| Q17 | varchar |  |  | SI | va-dt3 |
| Q18 | varchar |  |  | SI | Visual acuity - Near |
| Q19 | varchar |  |  | SI | VA-nr2 |
| Q20 | varchar |  |  | SI | va-nr3 |
| Q21 | varchar |  |  | SI | Material |
| Q22 | varchar |  |  | SI | Material 2 |
| Q23 | varchar |  |  | SI | Diameter |
| Q24 | varchar |  |  | SI | dia 2 |
| Q25 | varchar |  |  | SI | Notes |
| Q26 | varchar |  |  | SI | Final Refractions |
| Q27 | date |  |  | SI | Date |
| Q28 | varchar |  |  | SI | Type / Brand |
| Q29 | varchar |  |  | SI | Right Eye |
| Q30 | varchar |  |  | SI | Left Eye |
| Q31 | varchar |  |  | SI | Both Eye |
| Q32 | varchar |  |  | SI | Base curve |
| Q33 | varchar |  |  | SI | bc2 |
| Q34 | varchar |  |  | SI | Sphere |
| Q35 | varchar |  |  | SI | Sph 2 |
| Q36 | varchar |  |  | SI | Cylinder |
| Q37 | varchar |  |  | SI | Cyl2 |
| Q38 | varchar |  |  | SI | Axis |
| Q39 | varchar |  |  | SI | Axis 2 |
| Q40 | varchar |  |  | SI | Add |
| Q41 | varchar |  |  | SI | Add 2 |
| Q42 | varchar |  |  | SI | Visual acuity - Distance |
| Q43 | varchar |  |  | SI | va-dt 2 |
| Q44 | varchar |  |  | SI | va-dt 3 |
| Q45 | varchar |  |  | SI | Visual acuity - Near |
| Q46 | varchar |  |  | SI | VA-Nr 2 |
| Q47 | varchar |  |  | SI | VA-Nr 3 |
| Q48 | varchar |  |  | SI | Material  |
| Q49 | varchar |  |  | SI | Material 2 |
| Q50 | varchar |  |  | SI | Diameter |
| Q51 | varchar |  |  | SI | Dia 2 |
| Q52 | varchar |  |  | SI | Notes |
| Q53 | varchar |  |  | SI | Add |
| Q54 | varchar |  |  | SI | add 2 |
| Q55 | varchar |  |  | SI | Contact Lens Image Annotation |
| Q56 | varchar |  |  | SI | Interpupillary Distance (IPD) |
| Q57 | varchar |  |  | SI | Distance |
| Q58 | varchar |  |  | SI | Near |
| Q59 | varchar |  |  | SI | Lens type |
| Q60 | varchar |  |  | SI | Lens specification |
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