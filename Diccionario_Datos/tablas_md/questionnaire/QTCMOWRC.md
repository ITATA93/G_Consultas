# questionnaire.QTCMOWRC

> Medical Officer Ward Round Checklist - ICU

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Medical Officer Ward Round Checklist - ICU

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | date |  |  | SI | Date of current intensive care unit (ICU) admissio... |
| Q04 | numeric |  |  | SI | Days in ICU |
| Q05 | varchar |  |  | SI | Research trial information |
| Q06 | varchar |  |  | SI | Suitability to leave ICU |
| Q07 | date |  |  | SI | Decision date / time |
| Q08 | time |  |  | SI | Decision time |
| Q09 | varchar |  |  | SI | Discharge planning notes |
| Q10 | varchar |  |  | SI | Sedation |
| Q11 | varchar |  |  | SI | Sleep / Sleep pattern |
| Q12 | varchar |  |  | SI | Delirium |
| Q13 | varchar |  |  | SI | Adequate analgesia |
| Q14 | varchar |  |  | SI | Adequate glucose control |
| Q15 | varchar |  |  | SI | Feeing regimen |
| Q16 | varchar |  |  | SI | Lines - Dated / Removed / Changed |
| Q17 | varchar |  |  | SI | Antibiotics review |
| Q18 | varchar |  |  | SI | Venous Thromboembolism (VTE) prophylaxis |
| Q19 | varchar |  |  | SI | Stress ulcer prophylaxis |
| Q20 | varchar |  |  | SI | Resuscitation review / order |
| Q21 | varchar |  |  | SI | Need for family / relative discussion |
| Q22 | varchar |  |  | SI | Allied health referrals |
| Q23 | varchar |  |  | SI | Research |
| Q24 | varchar |  |  | SI | Patient diary |
| Q25 | varchar |  |  | SI | Bowels |
| Q26 | date |  |  | SI | Date bowels last opened |
| Q27 | varchar |  |  | SI | Notes |
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