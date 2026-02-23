# questionnaire.QGXXXHP

> Home and Prevention

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Home and Prevention

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Lives at home |
| Q01N | varchar |  |  | SI | Note |
| Q01ObsDR | varchar |  | FK | SI | Lives at home DR |
| Q03 | varchar |  |  | SI | Activation care |
| Q03N | varchar |  |  | SI | Note |
| Q03ObsDR | varchar |  | FK | SI | Activation care DR |
| Q05 | varchar |  |  | SI | Intensive short observation |
| Q05N | varchar |  |  | SI | Note |
| Q05ObsDR | varchar |  | FK | SI | Intensive short observation DR |
| Q07 | varchar |  |  | SI | Emergency room |
| Q07N | varchar |  |  | SI | Note |
| Q07ObsDR | varchar |  | FK | SI | Emergency room DR |
| Q09 | varchar |  |  | SI | Another hospital |
| Q09N | varchar |  |  | SI | Note |
| Q09ObsDR | varchar |  | FK | SI | Another hospital DR |
| Q11 | varchar |  |  | SI | Other department |
| Q11N | varchar |  |  | SI | Note |
| Q11ObsDR | varchar |  | FK | SI | Other department DR |
| Q13 | varchar |  |  | SI | Nursing home |
| Q13N | varchar |  |  | SI | Note |
| Q13ObsDR | varchar |  | FK | SI | Nursing home DR |
| Q15 | varchar |  |  | SI | Via contact |
| Q15ObsDR | varchar |  | FK | SI | Via contact DR |
| Q16N | varchar |  |  | SI | Note |
| Q17 | varchar |  |  | SI | Via airway |
| Q17N | varchar |  |  | SI | Note |
| Q17ObsDR | varchar |  | FK | SI | Via airway DR |
| Q19 | varchar |  |  | SI | Via blood-borne |
| Q19N | varchar |  |  | SI | Note |
| Q19ObsDR | varchar |  | FK | SI | Via blood-borne DR |
| Q21 | varchar |  |  | SI | Via droplets |
| Q21N | varchar |  |  | SI | Note |
| Q21ObsDR | varchar |  | FK | SI | Via droplets DR |
| Q23 | bigint |  |  | SI | Other |
| Q23TxtOnly | bigint |  |  | SI | Other Plain Text Only |
| Q25 | varchar |  |  | SI | Management of home care |
| Q25N | varchar |  |  | SI | Note |
| Q25ObsDR | varchar |  | FK | SI | Management of home care DR |
| Q27 | varchar |  |  | SI | Management of their own health |
| Q27N | varchar |  |  | SI | Note |
| Q27ObsDR | varchar |  | FK | SI | Management of their own health DR |
| Q29 | varchar |  |  | SI | Hygienic conditions |
| Q29N | varchar |  |  | SI | Note |
| Q29ObsDR | varchar |  | FK | SI | Hygienic conditions DR |
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