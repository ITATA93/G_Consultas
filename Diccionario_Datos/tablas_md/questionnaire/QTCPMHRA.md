# questionnaire.QTCPMHRA

> Manual Handling Risk Assessment

**Schema:** questionnaire
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Manual Handling Risk Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Does the patient require assistance |
| Q02 | varchar |  |  | SI | Risk Assessment |
| Q03 | varchar |  |  | SI | Rolling in bed |
| Q04 | numeric |  |  | SI | Number of staff required |
| Q05 | varchar |  |  | SI | Equipment required |
| Q06 | date |  |  | SI | Date transferred / reviewed |
| Q07 | varchar |  |  | SI | Movement up/down bed |
| Q08 | numeric |  |  | SI | Number of staff required |
| Q09 | varchar |  |  | SI | Equipment required |
| Q10 | date |  |  | SI | Date transferred / reviewed |
| Q11 | varchar |  |  | SI | Repositioning in bed |
| Q12 | numeric |  |  | SI | Number of staff required |
| Q13 | varchar |  |  | SI | Equipment required |
| Q14 | date |  |  | SI | Date transferred / reviewed |
| Q15 | varchar |  |  | SI | Supine to sitting |
| Q16 | numeric |  |  | SI | Number of staff required |
| Q17 | varchar |  |  | SI | Equipment required |
| Q18 | date |  |  | SI | Date transferred / reviewed |
| Q19 | varchar |  |  | SI | Sit to standing up |
| Q20 | numeric |  |  | SI | Number of staff required |
| Q21 | varchar |  |  | SI | Equipment required |
| Q22 | date |  |  | SI | Date transferred / reviewed |
| Q23 | varchar |  |  | SI | Mobilising |
| Q24 | numeric |  |  | SI | Number of staff required |
| Q25 | varchar |  |  | SI | Equipment required |
| Q26 | date |  |  | SI | Date transferred / reviewed |
| Q27 | varchar |  |  | SI | Transfers (bed to chair etc) |
| Q28 | numeric |  |  | SI | Number of staff required |
| Q29 | varchar |  |  | SI | Equipment required |
| Q30 | date |  |  | SI | Date transferred / reviewed |
| Q31 | varchar |  |  | SI | Bed to trolley / Lateral transfers or end to end |
| Q32 | numeric |  |  | SI | Number of staff required |
| Q33 | varchar |  |  | SI | Equipment required |
| Q34 | date |  |  | SI | Date transferred / reviewed |
| Q35 | varchar |  |  | SI | Actions taken |
| Q36 | varchar |  |  | SI | Additional comments |
| Q37 | varchar |  |  | SI | Using a bedpan |
| Q38 | numeric |  |  | SI | Number of staff required |
| Q39 | varchar |  |  | SI | Equipment required |
| Q40 | date |  |  | SI | Date transferred / reviewed |
| Q41 | varchar |  |  | SI | Bathing: getting in and out of shower |
| Q42 | numeric |  |  | SI | Number of staff required |
| Q43 | varchar |  |  | SI | Equipment required |
| Q44 | date |  |  | SI | Date transferred / reviewed |
| Q45 | date |  |  | SI | Date |
| Q46 | time |  |  | SI | Time |
| Q47 | varchar |  |  | SI | Patient Handling Chart |
| Q48 | varchar |  |  | SI | Lateral transfers (bed to trolley etc) |
| Q49 | varchar |  |  | SI | Other |
| Q50 | varchar |  |  | SI | Other |
| Q51 | varchar |  |  | SI | Other |
| Q52 | varchar |  |  | SI | Getting on/off toilet or commode |
| Q53 | varchar |  |  | SI | Other |
| Q54 | varchar |  |  | SI | Getting in/out of bath or shower |
| Q55 | varchar |  |  | SI | Other |
| Q56 | varchar |  |  | SI | Hoisting |
| Q57 | varchar |  |  | SI | Sling type |
| Q58 | varchar |  |  | SI | Other |
| Q59 | varchar |  |  | SI | Sling size |
| Q60 | varchar |  |  | SI | Other |
| Q61 | varchar |  |  | SI | Other |
| Q62 | varchar |  |  | SI | If none of the above, please state task and techni... |
| Q63 | varchar |  |  | SI | Please complete the patient handling chart in cons... |
| Q64 | varchar |  |  | SI | If this patient requires hoisting, please select |
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