# questionnaire.QTCMITC

> Medical Imaging Transfer Checklist

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Medical Imaging Transfer Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Imaging destination |
| Q04 | varchar |  |  | SI | Other imaging |
| Q05 | varchar |  |  | SI | Requirements Checklist |
| Q06 | varchar |  |  | SI | High risk patient screening completed |
| Q07 | varchar |  |  | SI | Escort required to remain with the patient |
| Q08 | varchar |  |  | SI | Type of escort required |
| Q09 | varchar |  |  | SI | Other escort type |
| Q10 | varchar |  |  | SI | Mobility status |
| Q11 | varchar |  |  | SI | Mobility aids |
| Q12 | varchar |  |  | SI | Other mobility aids |
| Q13 | varchar |  |  | SI | Dummy1 |
| Q14 | varchar |  |  | SI | Dummy2 |
| Q15 | varchar |  |  | SI | High Risk Critieria |
| Q16 | varchar |  |  | SI | Children (< 16yrs) unless accompanied by a family ... |
| Q17 | varchar |  |  | SI | Requiring cardiac monitoring |
| Q18 | varchar |  |  | SI | Requiring airway management |
| Q19 | varchar |  |  | SI | Dummy7 |
| Q20 | varchar |  |  | SI | Dummy8 |
| Q21 | varchar |  |  | SI | Dummy9 |
| Q22 | varchar |  |  | SI | Dummy10 |
| Q23 | varchar |  |  | SI | Dummy11 |
| Q24 | varchar |  |  | SI | Dummy12 |
| Q25 | varchar |  |  | SI | Dummy13 |
| Q26 | varchar |  |  | SI | Dummy14 |
| Q27 | varchar |  |  | SI | Dummy15 |
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