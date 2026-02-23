# questionnaire.QTCRAESWT

> Risk Assessment Before Extracorporeal Shockwave Therapy (ESWT)

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Risk Assessment Before Extracorporeal Shockwave Therapy (ESWT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Have you had any corticosteroid injection within t... |
| Q02 | varchar |  |  | SI | Do you have any coagulation disorder or take any a... |
| Q03 | varchar |  |  | SI | Do you have thrombosis? |
| Q04 | varchar |  |  | SI | Do you suffer from epilepsy? |
| Q05 | varchar |  |  | SI | Do you have any acute inflammation? |
| Q06 | varchar |  |  | SI | Do you have any polyneuropathy? |
| Q07 | varchar |  |  | SI | Have you had any tumor or recent radiotherapy/chem... |
| Q08 | varchar |  |  | SI | Have you had ESWT treatment in the past 2 months? |
| Q09 | varchar |  |  | SI | Risks and Side Effects include: |
| Q10 | varchar |  |  | SI | Swelling, redness, haematoma and pain. |
| Q11 | varchar |  |  | SI | Symptoms should reduce within 2 to 5 days and prio... |
| Q12 | varchar |  |  | SI | I understand the treatment and have had the risks ... |
| Q13 | longvarbinary |  |  | SI | Patient signature |
| Q13UDt | date |  |  | SI | Patient signature Last Updated Date |
| Q13UTm | time |  |  | SI | Patient signature Last Updated Time |
| Q14 | date |  |  | SI | Date |
| Q15 | varchar |  |  | SI | I have asked these questions and explained the tre... |
| Q16 | longvarbinary |  |  | SI | Care giver signature |
| Q16UDt | date |  |  | SI | Care giver signature Last Updated Date |
| Q16UTm | time |  |  | SI | Care giver signature Last Updated Time |
| Q17 | date |  |  | SI | Date |
| Q18 | varchar |  |  | SI | Additional information |
| Q19 | varchar |  |  | SI | Additional information |
| Q20 | varchar |  |  | SI | Additional information |
| Q21 | varchar |  |  | SI | Additional information |
| Q22 | varchar |  |  | SI | Additional information |
| Q23 | varchar |  |  | SI | Additional information |
| Q24 | varchar |  |  | SI | Additional information |
| Q25 | varchar |  |  | SI | Additional information |
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