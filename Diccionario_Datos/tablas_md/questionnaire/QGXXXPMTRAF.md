# questionnaire.QGXXXPMTRAF

> PMTRA (off bed task)

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* PMTRA (off bed task)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Bed to Chair - Assessment |
| Q02 | varchar |  |  | SI | Bed to Chair - Patient Ability |
| Q03 | varchar |  |  | SI | Bed to Chair - Equipment Required |
| Q04 | varchar |  |  | SI | Bed to Chair - Prior Assessment |
| Q05 | varchar |  |  | SI | Bed to Chair - Staff Required |
| Q06 | varchar |  |  | SI | Chair to bed - Assessment |
| Q07 | varchar |  |  | SI | Chair to bed - Patient Ability |
| Q08 | varchar |  |  | SI | Chair to bed - Equipment Required |
| Q09 | varchar |  |  | SI | Chair to bed - Prior Assessment |
| Q10 | varchar |  |  | SI | Chair to bed - Staff Required |
| Q11 | varchar |  |  | SI | Chair to Chair - Assessment |
| Q12 | varchar |  |  | SI | Chair to Chair - Patient Ability |
| Q13 | varchar |  |  | SI | Chair to Chair - Equipment Required |
| Q14 | varchar |  |  | SI | Chair to Chair - Prior Assessment |
| Q15 | varchar |  |  | SI | Chair to Chair - Staff Required |
| Q16 | varchar |  |  | SI | Bed to Trolley to Bed - Assessment |
| Q17 | varchar |  |  | SI | Bed to Trolley to Bed - Patient Ability |
| Q18 | varchar |  |  | SI | Bed to Trolley to Bed - Equipment Required |
| Q19 | varchar |  |  | SI | Bed to Trolley to Bed - Prior Assessment |
| Q20 | varchar |  |  | SI | Bed to Trolley to Bed - Staff Required |
| Q21 | varchar |  |  | SI | Task |
| Q22 | varchar |  |  | SI | Assessment |
| Q23 | varchar |  |  | SI | Patient Ability |
| Q24 | varchar |  |  | SI | Equipment Required |
| Q25 | varchar |  |  | SI | Prior Assessment |
| Q26 | varchar |  |  | SI | Staff Required |
| Q27 | varchar |  |  | SI | Bed to Chair |
| Q28 | varchar |  |  | SI | Chair to bed |
| Q29 | varchar |  |  | SI | Chair to Chair |
| Q30 | varchar |  |  | SI | Bed to Trolley to Bed |
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