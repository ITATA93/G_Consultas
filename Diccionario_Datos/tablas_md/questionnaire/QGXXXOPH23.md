# questionnaire.QGXXXOPH23

> Uveitis Refractions

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Uveitis Refractions

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Visual Acuity - Uncorrected |
| Q02 | varchar |  |  | SI | VA-Dt |
| Q03 | varchar |  |  | SI | VA-Dt 2 |
| Q04 | varchar |  |  | SI | VA-Dt 3 |
| Q05 | varchar |  |  | SI | VA-Nr |
| Q06 | varchar |  |  | SI | VA-Nr 2 |
| Q07 | varchar |  |  | SI | VA-Nr 3 |
| Q08 | varchar |  |  | SI | Notes |
| Q09 | varchar |  |  | SI | Right Eye |
| Q10 | varchar |  |  | SI | Left Eye |
| Q11 | varchar |  |  | SI | Both Eye |
| Q12 | varchar |  |  | SI | Visual Acuity - Corrected (Glasses Refraction) |
| Q13 | varchar |  |  | SI | Right Eye |
| Q14 | varchar |  |  | SI | Left Eye |
| Q15 | varchar |  |  | SI | Sph |
| Q16 | varchar |  |  | SI | Sph 2 |
| Q17 | varchar |  |  | SI | Cyl |
| Q18 | varchar |  |  | SI | Cyl 2 |
| Q19 | varchar |  |  | SI | Axis |
| Q20 | varchar |  |  | SI | Axis 2 |
| Q21 | varchar |  |  | SI | Add |
| Q22 | varchar |  |  | SI | VA-Dt |
| Q23 | varchar |  |  | SI | VA-Dt 2 |
| Q24 | varchar |  |  | SI | VA-Dt 3 |
| Q25 | varchar |  |  | SI | VA-Nr |
| Q26 | varchar |  |  | SI | VA-Nr 2 |
| Q27 | varchar |  |  | SI | VA-Nr 3 |
| Q28 | varchar |  |  | SI | Notes |
| Q29 | varchar |  |  | SI | Add 2 |
| Q30 | varchar |  |  | SI | Final Prescription Refraction |
| Q31 | date |  |  | SI | Date |
| Q32 | numeric |  |  | SI | IPD |
| Q33 | varchar |  |  | SI | mm |
| Q34 | varchar |  |  | SI | Material |
| Q35 | varchar |  |  | SI | Right Eye |
| Q36 | varchar |  |  | SI | Left Eye |
| Q37 | varchar |  |  | SI | Sph |
| Q38 | varchar |  |  | SI | Sph2 |
| Q39 | varchar |  |  | SI | Both Eyes |
| Q40 | varchar |  |  | SI | Cyl |
| Q41 | varchar |  |  | SI | Cyl 2 |
| Q42 | varchar |  |  | SI | Axis |
| Q43 | varchar |  |  | SI | Axis 2 |
| Q44 | varchar |  |  | SI | Add |
| Q45 | varchar |  |  | SI | Add2 |
| Q46 | varchar |  |  | SI | VA-Dt |
| Q47 | varchar |  |  | SI | VA-Dt 2 |
| Q48 | varchar |  |  | SI | VA-Dt 3 |
| Q49 | varchar |  |  | SI | VA-Nr |
| Q50 | varchar |  |  | SI | VA-Nr 2 |
| Q51 | varchar |  |  | SI | VA-Nr 3 |
| Q52 | varchar |  |  | SI | Notes |
| Q53 | varchar |  |  | SI | Both Eyes |
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