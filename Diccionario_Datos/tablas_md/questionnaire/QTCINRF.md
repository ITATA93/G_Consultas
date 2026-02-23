# questionnaire.QTCINRF

> Interventional Nephrology Record - Fistula

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Interventional Nephrology Record - Fistula

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | date |  |  | SI | Date of procedure |
| Q04 | varchar |  |  | SI | Care provider 1 |
| Q05 | varchar |  |  | SI | Care provider 2 |
| Q06 | varchar |  |  | SI | Care provider 3 |
| Q07 | varchar |  |  | SI | Access requiring procedure |
| Q08 | varchar |  |  | SI | Laterality |
| Q09 | varchar |  |  | SI | Access location |
| Q10 | varchar |  |  | SI | Other access location |
| Q11 | varchar |  |  | SI | Procedure |
| Q12 | varchar |  |  | SI | Procedure code |
| Q13 | varchar |  |  | SI | Anaesthesia |
| Q14 | varchar |  |  | SI | Type of contrast used |
| Q15 | varchar |  |  | SI | Access to fistula |
| Q16 | varchar |  |  | SI | Sheath size |
| Q17 | varchar |  |  | SI | Fistulogram stenosis |
| Q18 | varchar |  |  | SI | Fistulogram - Anastomosis status |
| Q19 | varchar |  |  | SI | Fistulogram - Peripheral check |
| Q20 | varchar |  |  | SI | Fistulogram - Central check |
| Q21 | varchar |  |  | SI | Fistulogram notes |
| Q22 | varchar |  |  | SI | Flow |
| Q23 | varchar |  |  | SI | Stenting - Fistuloplasty |
| Q25 | varchar |  |  | SI | IV heparin dose required |
| Q26 | varchar |  |  | SI | Heparin comments |
| Q27 | varchar |  |  | SI | Procedure outcome |
| Q28 | varchar |  |  | SI | Complications |
| Q29 | varchar |  |  | SI | Procedure notes |
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