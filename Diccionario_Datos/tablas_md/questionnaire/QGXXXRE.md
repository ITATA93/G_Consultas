# questionnaire.QGXXXRE

> Respiratory Examination

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Respiratory Examination

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q03 | varchar |  |  | SI | Rhonchi |
| Q03N | varchar |  |  | SI | Note |
| Q03ObsDR | varchar |  | FK | SI | Rhonchi DR |
| Q05N | varchar |  |  | SI | Note |
| Q07 | varchar |  |  | SI | Other |
| Q08 | varchar |  |  | SI | Lung sound |
| Q08N | varchar |  |  | SI | Note |
| Q08ObsDR | varchar |  | FK | SI | Lung sound DR |
| Q10 | varchar |  |  | SI | Chest |
| Q10N | varchar |  |  | SI | Note |
| Q10ObsDR | varchar |  | FK | SI | Chest DR |
| Q12 | varchar |  |  | SI | Axilla |
| Q12N | varchar |  |  | SI | Note |
| Q12ObsDR | varchar |  | FK | SI | Axilla DR |
| Q13 | varchar |  |  | SI | Other |
| Q15 | varchar |  |  | SI | Stridor |
| Q15N | varchar |  |  | SI | Note |
| Q15ObsDR | varchar |  | FK | SI | Stridor DR |
| Q16 | varchar |  |  | SI | Rales |
| Q16N | varchar |  |  | SI | Note |
| Q16ObsDR | varchar |  | FK | SI | Rales DR |
| Q17 | varchar |  |  | SI | Chest percussion |
| Q17N | varchar |  |  | SI | Note |
| Q17ObsDR | varchar |  | FK | SI | Chest percussion DR |
| Q19 | varchar |  |  | SI | Chest appearance  |
| Q19N | varchar |  |  | SI | Note |
| Q19ObsDR | varchar |  | FK | SI | Chest appearance  DR |
| Q20 | varchar |  |  | SI | Wheezing |
| Q20ObsDR | varchar |  | FK | SI | Wheezing DR |
| Q21 | varchar |  |  | SI | Chest scars |
| Q21N | varchar |  |  | SI | Note |
| Q21ObsDR | varchar |  | FK | SI | Chest scars DR |
| Q22 | varchar |  |  | SI | Accessory muscle use |
| Q22N | varchar |  |  | SI | Note |
| Q22ObsDR | varchar |  | FK | SI | Accessory muscle use DR |
| Q23 | varchar |  |  | SI | Intercostal recession |
| Q23N | varchar |  |  | SI | Note |
| Q23ObsDR | varchar |  | FK | SI | Intercostal recession DR |
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