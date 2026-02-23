# questionnaire.QGXXXMG

> Male urogenital examination

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Male urogenital examination

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Urethral meatus |
| Q01N | varchar |  |  | SI | Note |
| Q01ObsDR | varchar |  | FK | SI | Urethral meatus DR |
| Q03 | varchar |  |  | SI | Testis left |
| Q03N | varchar |  |  | SI | Note |
| Q03ObsDR | varchar |  | FK | SI | Testis left DR |
| Q05 | varchar |  |  | SI | Testis right |
| Q05N | varchar |  |  | SI | Note |
| Q05ObsDR | varchar |  | FK | SI | Testis right DR |
| Q07 | varchar |  |  | SI | Epididymis left |
| Q07N | varchar |  |  | SI | Note |
| Q07ObsDR | varchar |  | FK | SI | Epididymis left DR |
| Q09 | varchar |  |  | SI | Epididymis right |
| Q09N | varchar |  |  | SI | Note |
| Q09ObsDR | varchar |  | FK | SI | Epididymis right DR |
| Q11 | varchar |  |  | SI | Spermatic cord left |
| Q11N | varchar |  |  | SI | Note |
| Q11ObsDR | varchar |  | FK | SI | Spermatic cord left DR |
| Q13 | varchar |  |  | SI | Spermatic cord right |
| Q13N | varchar |  |  | SI | Note |
| Q13ObsDR | varchar |  | FK | SI | Spermatic cord right DR |
| Q15 | varchar |  |  | SI | Scrotum |
| Q15N | varchar |  |  | SI | Note |
| Q15ObsDR | varchar |  | FK | SI | Scrotum DR |
| Q17 | varchar |  |  | SI | Penis |
| Q17N | varchar |  |  | SI | Note |
| Q17ObsDR | varchar |  | FK | SI | Penis DR |
| Q19 | varchar |  |  | SI | Phimosis |
| Q19N | varchar |  |  | SI | Note |
| Q19ObsDR | varchar |  | FK | SI | Phimosis DR |
| Q21 | varchar |  |  | SI | Paraphimosis |
| Q21N | varchar |  |  | SI | Note |
| Q21ObsDR | varchar |  | FK | SI | Paraphimosis DR |
| Q23 | varchar |  |  | SI | Other |
| Q24 | varchar |  |  | SI | Hernia |
| Q24N | varchar |  |  | SI | Note |
| Q24ObsDR | varchar |  | FK | SI | Hernia DR |
| Q26 | varchar |  |  | SI | Inguinal lymphadenopathy |
| Q26N | varchar |  |  | SI | Note |
| Q26ObsDR | varchar |  | FK | SI | Inguinal lymphadenopathy DR |
| Q28 | varchar |  |  | SI | Rectal Examination Done |
| Q28N | varchar |  |  | SI | Note |
| Q30 | varchar |  |  | SI | Rectal Examination |
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