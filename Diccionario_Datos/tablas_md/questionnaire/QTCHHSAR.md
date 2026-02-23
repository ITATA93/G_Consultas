# questionnaire.QTCHHSAR

> Home Haemodialysis Suitability Assessment - Residence

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Home Haemodialysis Suitability Assessment - Residence

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Accommodation |
| Q04 | varchar |  |  | SI | Accommodation type |
| Q05 | varchar |  |  | SI | Other accommodation type |
| Q06 | numeric |  |  | SI | Number of bedrooms |
| Q07 | numeric |  |  | SI | Number of adults living in the house |
| Q08 | numeric |  |  | SI | Number of children in the house |
| Q09 | numeric |  |  | SI | Number of pets in the house |
| Q10 | varchar |  |  | SI | Accommodation suitable for haemodialysis notes |
| Q11 | varchar |  |  | SI | Haemodialysis Space Assessment |
| Q12 | varchar |  |  | SI | 3x3 meter space available |
| Q13 | varchar |  |  | SI | Space notes |
| Q14 | varchar |  |  | SI | Describe access to home |
| Q15 | varchar |  |  | SI | Consider narrow doorway / passage / stairs / entry... |
| Q16 | varchar |  |  | SI | Entry doorways width confirmed to allow dialysis c... |
| Q17 | varchar |  |  | SI | Potential dialysis space room flooring type |
| Q18 | varchar |  |  | SI | Access to water pipe/ tap and sewerage close to pr... |
| Q19 | varchar |  |  | SI | Electricity outlet available with minimum requirem... |
| Q20 | varchar |  |  | SI | Photos taken of |
| Q21 | varchar |  |  | SI | Any additional work required to utilise existing p... |
| Q22 | varchar |  |  | SI | Additional work required |
| Q23 | varchar |  |  | SI | Outcome / Plan |
| Q24 | varchar |  |  | SI | Outcome of home haemodialysis suitability assessme... |
| Q25 | varchar |  |  | SI | Space suitable for haemodialysis |
| Q26 | varchar |  |  | SI | Outcome |
| Q27 | varchar |  |  | SI | Plan |
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