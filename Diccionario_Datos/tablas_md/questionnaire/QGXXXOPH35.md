# questionnaire.QGXXXOPH35

> Visual Acuity

**Schema:** questionnaire
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Visual Acuity

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Visual Acuity - Uncorrected |
| Q02 | varchar |  |  | SI | Right eye |
| Q03 | varchar |  |  | SI | Left eye |
| Q04 | varchar |  |  | SI | Both eyes |
| Q05 | varchar |  |  | SI | VA-Dt |
| Q06 | varchar |  |  | SI | Va-dt2 |
| Q07 | varchar |  |  | SI | Va-dt3 |
| Q08 | varchar |  |  | SI | VA-PH |
| Q09 | varchar |  |  | SI | VA-ph2 |
| Q10 | varchar |  |  | SI | vA-Ph3 |
| Q11 | varchar |  |  | SI | VA-Nr |
| Q12 | varchar |  |  | SI | va-nr2 |
| Q13 | varchar |  |  | SI | va-nr3 |
| Q14 | varchar |  |  | SI | Notes |
| Q15 | varchar |  |  | SI | Visual Acuity - Corrected |
| Q16 | varchar |  |  | SI | Right eye |
| Q17 | varchar |  |  | SI | Left eye |
| Q18 | varchar |  |  | SI | Sph |
| Q19 | varchar |  |  | SI | sph2 |
| Q20 | varchar |  |  | SI | Cyl |
| Q21 | varchar |  |  | SI | Cyl2 |
| Q22 | varchar |  |  | SI | Axis |
| Q23 | varchar |  |  | SI | axis2 |
| Q24 | varchar |  |  | SI | Add |
| Q25 | varchar |  |  | SI | VA-Dt |
| Q26 | varchar |  |  | SI | VA-dt2 |
| Q27 | varchar |  |  | SI | Va-dt3 |
| Q28 | varchar |  |  | SI | Both eyes |
| Q29 | varchar |  |  | SI | VA-Nr |
| Q30 | varchar |  |  | SI | VA-Nr2 |
| Q31 | varchar |  |  | SI | VA-Nr3 |
| Q32 | varchar |  |  | SI | Notes |
| Q33 | varchar |  |  | SI | Eye dilated? |
| Q36 | varchar |  |  | SI | This shows the visual acuity recordings taken by n... |
| Q361 | varchar |  |  | SI | Pinhole test |
| Q37 | varchar |  |  | SI | Previous values are retained here, to create a new... |
| Q371 | varchar |  |  | SI | Distance |
| Q38 | varchar |  |  | SI | Distance |
| Q39 | varchar |  |  | SI | Near |
| Q40 | varchar |  |  | SI | Near |
| Q41 | varchar |  |  | SI | Near |
| Q42 | varchar |  |  | SI | Va-NR-ph1 |
| Q43 | varchar |  |  | SI | Va-NR-ph2 |
| Q44 | varchar |  |  | SI | Va-NR-ph3 |
| Q45 | varchar |  |  | SI | Notes |
| Q46 | varchar |  |  | SI | Distance |
| Q47 | varchar |  |  | SI | Right eye |
| Q48 | varchar |  |  | SI | Left eye |
| Q49 | varchar |  |  | SI | Both eyes |
| Q50 | date |  |  | SI | Date |
| Q51 | time |  |  | SI | Time |
| Q52 | varchar |  |  | SI | Distance |
| Q53 | varchar |  |  | SI | Distance |
| Q54 | varchar |  |  | SI | Distance |
| Q55 | varchar |  |  | SI | Distance |
| Q56 | varchar |  |  | SI | Distance |
| Q57 | varchar |  |  | SI | Distance |
| Q58 | varchar |  |  | SI | Distance |
| Q59 | varchar |  |  | SI | Distance |
| Q60 | varchar |  |  | SI | Distance |
| Q61 | varchar |  |  | SI | Near |
| Q62 | varchar |  |  | SI | Near |
| Q63 | varchar |  |  | SI | Near |
| Q64 | varchar |  |  | SI | Near |
| Q65 | varchar |  |  | SI | Near |
| Q66 | varchar |  |  | SI | Near |
| Q67 | varchar |  |  | SI | Near |
| Q68 | varchar |  |  | SI | Near |
| Q69 | varchar |  |  | SI | Near |
| Q70 | varchar |  |  | SI | Notes |
| Q71 | varchar |  |  | SI | Notes |
| Q72 | varchar |  |  | SI | Notes |
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