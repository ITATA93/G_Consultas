# questionnaire.QTCAPC

> Anaesthetic Procedure Consent

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Anaesthetic Procedure Consent

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Anaesthetic type |
| Q04 | varchar |  |  | SI | Consent for |
| Q05 | varchar |  |  | SI | Complications of general anaesthetic / sedation  d... |
| Q06 | varchar |  |  | SI | Additional anaesthetic / sedation discussion notes |
| Q07 | varchar |  |  | SI | Complications of regional anaesthesia discussed |
| Q08 | varchar |  |  | SI | Additional regional anaesthesia discussion notes |
| Q09 | varchar |  |  | SI | Supplementary techniques |
| Q10 | varchar |  |  | SI | Complications of supplementary techniques discusse... |
| Q11 | varchar |  |  | SI | Exclusions |
| Q12 | varchar |  |  | SI | Exclusions details |
| Q13 | longvarbinary |  |  | SI | Patient signature |
| Q13UDt | date |  |  | SI | Patient signature Last Updated Date |
| Q13UTm | time |  |  | SI | Patient signature Last Updated Time |
| Q14 | varchar |  |  | SI | Guardian name (if applicable) |
| Q15 | longvarbinary |  |  | SI | Guardian signature (if applicable) |
| Q15UDt | date |  |  | SI | Guardian signature (if applicable) Last Updated Da... |
| Q15UTm | time |  |  | SI | Guardian signature (if applicable) Last Updated Ti... |
| Q16 | varchar |  |  | SI | Interpreter name (if applicable) |
| Q17 | longvarbinary |  |  | SI | Interpreter signature (if applicable) |
| Q17UDt | date |  |  | SI | Interpreter signature (if applicable) Last Updated... |
| Q17UTm | time |  |  | SI | Interpreter signature (if applicable) Last Updated... |
| Q18 | varchar |  |  | SI | Anaesthetist name |
| Q19 | longvarbinary |  |  | SI | Anaesthetist signature |
| Q19UDt | date |  |  | SI | Anaesthetist signature Last Updated Date |
| Q19UTm | time |  |  | SI | Anaesthetist signature Last Updated Time |
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