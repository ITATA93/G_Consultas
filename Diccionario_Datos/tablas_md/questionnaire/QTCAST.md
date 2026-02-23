# questionnaire.QTCAST

> Acuity Scoring Tool

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Acuity Scoring Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Select the option for each that is most applicable... |
| Q04 | varchar |  |  | SI | Observations |
| Q05 | varchar |  |  | SI | Early warning score |
| Q06 | varchar |  |  | SI | Conscious state |
| Q07 | varchar |  |  | SI | Behaviour |
| Q08 | varchar |  |  | SI | Communication |
| Q09 | varchar |  |  | SI | Respiratory status |
| Q10 | varchar |  |  | SI | Pain management |
| Q11 | varchar |  |  | SI | Wound Care |
| Q12 | varchar |  |  | SI | Medication management |
| Q13 | varchar |  |  | SI | ADL's |
| Q14 | varchar |  |  | SI | Isolation |
| Q15 | varchar |  |  | SI | Safety |
| Q16 | varchar |  |  | SI | Complexity |
| Q17 | varchar |  |  | SI | Admission / Discharge / Transfer |
| Q18 | varchar |  |  | SI | Acuity remarks |
| Q19 | varchar |  |  | SI | Score |
| Q20 | varchar |  |  | SI | Classification |
| Q21 | varchar |  |  | SI | 0 |
| Q22 | varchar |  |  | SI | 1 - 7 |
| Q23 | varchar |  |  | SI | 8 - 14 |
| Q24 | varchar |  |  | SI | 15 - 28 |
| Q25 | varchar |  |  | SI | ≥ 29 |
| Q26 | varchar |  |  | SI | Level 0 - Minimal / Sub-Acute Care |
| Q27 | varchar |  |  | SI | Level 1 - Acute Care |
| Q28 | varchar |  |  | SI | Level 2 - Intermediate Acute Care |
| Q29 | varchar |  |  | SI | Level 3 - Complex / High - Dependency Care |
| Q30 | varchar |  |  | SI | Level 4 - Maximum Care |
| Q31 | varchar |  |  | SI | 0: Level 0 - Minimal / Sub-Acute Care |
| Q32 | varchar |  |  | SI | 1 - 7: Level 1 - Acute Care |
| Q33 | varchar |  |  | SI | 8 - 14: Level 2 - Intermediate Acute Care |
| Q34 | varchar |  |  | SI | 15 - 28: Level 3 - Complex / High - Dependency Car... |
| Q35 | varchar |  |  | SI | ≥ 29: Level 4 - Maximum Care |
| Q36 | varchar |  |  | SI | This scored questionnaire is a tool used to help n... |
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