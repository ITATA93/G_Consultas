# questionnaire.QGXXXMTFCOL

> Colposcopy Report - Initial

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Colposcopy Report - Initial

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of Referral |
| Q02 | varchar |  |  | SI | Referring Physician |
| Q03 | varchar |  |  | SI | Referral |
| Q04 | varchar |  |  | SI | Symptoms |
| Q05 | varchar |  |  | SI | Smear (General) |
| Q06 | varchar |  |  | SI | Smear (Specific) |
| Q07 | varchar |  |  | SI | Smear (Specific) Other |
| Q08 | numeric |  |  | SI | Gravida |
| Q09 | numeric |  |  | SI | Para |
| Q10 | numeric |  |  | SI | Age 1st Pregnancy |
| Q11 | varchar |  |  | SI | Gross Appearance |
| Q12 | varchar |  |  | SI | Contraception |
| Q13 | varchar |  |  | SI | Contraception Other |
| Q14 | varchar |  |  | SI | Clinical Indications Comments |
| Q15 | date |  |  | SI | Date of Report |
| Q16 | varchar |  |  | SI | Cytology |
| Q17 | varchar |  |  | SI | Other Comments |
| Q18 | varchar |  |  | SI | Diagnosis |
| Q19 | varchar |  |  | SI | Abnormal Features |
| Q20 | varchar |  |  | SI | Colposcopy Diagram |
| Q21 | numeric |  |  | SI | Pregnant Months |
| Q22 | varchar |  |  | SI | Extent of Lesion |
| Q23 | varchar |  |  | SI | Recommended Treatment |
| Q24 | varchar |  |  | SI | Recommended Treatment Other |
| Q26 | varchar |  |  | SI | Treatment Comments |
| Q27 | date |  |  | SI | Treatment Date |
| Q28 | varchar |  |  | SI | Pregnancy History |
| Q29 | varchar |  |  | SI | Referral Details |
| Q30 | varchar |  |  | SI | Colposcopy |
| Q31 | varchar |  |  | SI | Directed Biopsy |
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