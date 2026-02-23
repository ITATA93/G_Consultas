# questionnaire.QGXXXPACUD

> PACU Discharge

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* PACU Discharge

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | PACU comments |
| Q02 | bit |  |  | SI | Discharge agreed by anaesthetist (only if discharg... |
| Q02a | varchar |  |  | SI | Discharge agreed by anaesthetist (only if discharg... |
| Q03 | bit |  |  | SI | Ward notified / Bed available |
| Q03a | varchar |  |  | SI | Ward notified / Bed available |
| Q04 | bit |  |  | SI | Lines checked and flushed |
| Q04a | varchar |  |  | SI | Lines checked and flushed |
| Q05 | bit |  |  | SI | Dressings checked |
| Q05a | varchar |  |  | SI | Dressings checked |
| Q06 | bit |  |  | SI | Drains checked |
| Q06a | varchar |  |  | SI | Drains checked |
| Q07 | bit |  |  | SI | Nursing discharge summary completed |
| Q07a | varchar |  |  | SI | Nursing discharge summary completed |
| Q08 | bit |  |  | SI | Clinical indicators completed if applicable |
| Q08a | varchar |  |  | SI | Clinical indicators completed if applicable |
| Q09 | bit |  |  | SI | Post operative medications charted |
| Q09a | varchar |  |  | SI | Post operative medications charted |
| Q11 | varchar |  |  | SI | Glasses |
| Q12 | varchar |  |  | SI | Dentures |
| Q13 | varchar |  |  | SI | Hearing aides |
| Q14 | varchar |  |  | SI | X-Rays |
| Q15 | bit |  |  | SI | Temperature > 36 degrees |
| Q15a | varchar |  |  | SI | Temperature > 36 degrees |
| Q16 | varchar |  |  | SI | Comments |
| Q17 | varchar |  |  | SI | Script sent to pharmacy |
| Q19 | bit |  |  | SI | Clinical indicators completed if applicable  |
| Q27 | varchar |  |  | SI | Personal belongings |
| Q28 | varchar |  |  | SI | Supplementary oxygen required |
| Q29 | varchar |  |  | SI | Lines removed |
| Q30 | varchar |  |  | SI | Lines removed comments |
| Q31 | varchar |  |  | SI | Return of body part / metalware |
| Q32 | varchar |  |  | SI | Patient care plan follows post op instructions |
| Q33 | varchar |  |  | SI | Handover received by |
| Q34 | date |  |  | SI | Handover date and time |
| Q35 | time |  |  | SI | Handover time |
| Q36 | varchar |  |  | SI | Other belongings |
| Q38 | date |  |  | SI | Date |
| Q39 | time |  |  | SI | Time |
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