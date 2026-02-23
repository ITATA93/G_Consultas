# questionnaire.QGXXXBREAST

> Breast Examination

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Breast Examination

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q00 | varchar |  |  | SI | View |
| Q03 | varchar |  |  | SI | Neck |
| Q08N | varchar |  |  | SI | Note |
| Q14 | varchar |  |  | SI | Breast |
| Q15 | varchar |  |  | SI | Breast general appearance |
| Q15N | varchar |  |  | SI | Note |
| Q15ObsDR | varchar |  | FK | SI | Breast general appearance DR |
| Q17 | varchar |  |  | SI | Nipple secretion |
| Q17N | varchar |  |  | SI | Note |
| Q17ObsDR | varchar |  | FK | SI | Nipple secretion DR |
| Q18 | varchar |  |  | SI | Breast normal |
| Q18N | varchar |  |  | SI | Note |
| Q18ObsDR | varchar |  | FK | SI | Breast normal DR |
| Q19 | varchar |  |  | SI | Nipple retraction |
| Q19N | varchar |  |  | SI | Note |
| Q19ObsDR | varchar |  | FK | SI | Nipple retraction DR |
| Q20 | varchar |  |  | SI | Breast symmetry  |
| Q20N | varchar |  |  | SI | Note |
| Q20ObsDR | varchar |  | FK | SI | Breast symmetry  DR |
| Q21 | varchar |  |  | SI | Breast skin |
| Q21N | varchar |  |  | SI | Note |
| Q21ObsDR | varchar |  | FK | SI | Breast skin DR |
| Q23 | varchar |  |  | SI | Breast nodule |
| Q23N | varchar |  |  | SI | Localization |
| Q23ObsDR | varchar |  | FK | SI | Breast nodule DR |
| Q25 | varchar |  |  | SI | Lymph nodes palpable |
| Q25N | varchar |  |  | SI | Note |
| Q25ObsDR | varchar |  | FK | SI | Lymph nodes palpable DR |
| Q27 | varchar |  |  | SI | Other |
| Q30 | varchar |  |  | SI | Mastectomy |
| Q30N | varchar |  |  | SI | Note |
| Q30ObsDR | varchar |  | FK | SI | Mastectomy DR |
| Q31 | varchar |  |  | SI | Scars / prior surgery |
| Q31N | varchar |  |  | SI | Note |
| Q31ObsDR | varchar |  | FK | SI | Scars / prior surgery DR |
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