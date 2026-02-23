# questionnaire.QGXXXCOGAPE

> Cognitive and Perceptual

**Schema:** questionnaire
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cognitive and Perceptual

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | View |
| Q02 | varchar |  |  | SI | Blindness |
| Q02N | varchar |  |  | SI | Note |
| Q02ObsDR | varchar |  | FK | SI | Blindness DR |
| Q04 | varchar |  |  | SI | Blindness partial |
| Q04N | varchar |  |  | SI | Note |
| Q04ObsDR | varchar |  | FK | SI | Blindness partial DR |
| Q06 | varchar |  |  | SI | Ocular prothesis |
| Q06N | varchar |  |  | SI | Note |
| Q06ObsDR | varchar |  | FK | SI | Ocular prothesis DR |
| Q08 | varchar |  |  | SI | Glasses |
| Q08N | varchar |  |  | SI | Note |
| Q08ObsDR | varchar |  | FK | SI | Glasses DR |
| Q10 | varchar |  |  | SI | Contact Lenses |
| Q10N | varchar |  |  | SI | Note |
| Q10ObsDR | varchar |  | FK | SI | Contact Lenses DR |
| Q12 | varchar |  |  | SI | Ocular bandage |
| Q12N | varchar |  |  | SI | Note |
| Q12ObsDR | varchar |  | FK | SI | Ocular bandage DR |
| Q14 | varchar |  |  | SI | Hearing |
| Q15 | varchar |  |  | SI | Deafness |
| Q15N | varchar |  |  | SI | Note |
| Q15ObsDR | varchar |  | FK | SI | Deafness DR |
| Q17 | varchar |  |  | SI | Hearing loss |
| Q17N | varchar |  |  | SI | Note |
| Q17ObsDR | varchar |  | FK | SI | Hearing loss DR |
| Q19 | varchar |  |  | SI | Hearing aids |
| Q19N | varchar |  |  | SI | Note |
| Q19ObsDR | varchar |  | FK | SI | Hearing aids DR |
| Q21 | varchar |  |  | SI | Language |
| Q22 | varchar |  |  | SI | Aphasia |
| Q22N | varchar |  |  | SI | Note |
| Q22ObsDR | varchar |  | FK | SI | Aphasia DR |
| Q24 | varchar |  |  | SI | Dysarthria |
| Q24N | varchar |  |  | SI | Note |
| Q24ObsDR | varchar |  | FK | SI | Dysarthria DR |
| Q26 | varchar |  |  | SI | Stuttering |
| Q26N | varchar |  |  | SI | Note |
| Q26ObsDR | varchar |  | FK | SI | Stuttering DR |
| Q27 | varchar |  |  | SI | Inability to understand |
| Q27N | varchar |  |  | SI | Note |
| Q27ObsDR | varchar |  | FK | SI | Inability to understand DR |
| Q29 | varchar |  |  | SI | Failure of communication |
| Q29N | varchar |  |  | SI | Note |
| Q29ObsDR | varchar |  | FK | SI | Failure of communication DR |
| Q31 | varchar |  |  | SI | State of mind |
| Q32 | varchar |  |  | SI | State of mind |
| Q32N | varchar |  |  | SI | Note |
| Q32ObsDR | varchar |  | FK | SI | State of mind DR |
| Q34 | varchar |  |  | SI | Oriented |
| Q34N | varchar |  |  | SI | Note |
| Q34ObsDR | varchar |  | FK | SI | Oriented DR |
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