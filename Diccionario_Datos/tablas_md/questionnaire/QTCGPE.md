# questionnaire.QTCGPE

> Gynaecology Pelvic Examination

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Gynaecology Pelvic Examination

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Assessment Date |
| Q02 | time |  |  | SI | Assessment Time |
| Q03 | varchar |  |  | SI | Abdomen |
| Q03ObsDR | varchar |  | FK | SI | Abdomen DR |
| Q04 | varchar |  |  | SI | Note |
| Q05 | varchar |  |  | SI | Vulva |
| Q05ObsDR | varchar |  | FK | SI | Vulva DR |
| Q06 | varchar |  |  | SI | Note |
| Q07 | varchar |  |  | SI | Vagina |
| Q07ObsDR | varchar |  | FK | SI | Vagina DR |
| Q08 | varchar |  |  | SI | Note |
| Q09 | varchar |  |  | SI | Cervix |
| Q09ObsDR | varchar |  | FK | SI | Cervix DR |
| Q10 | varchar |  |  | SI | Note |
| Q11 | varchar |  |  | SI | Uterus position |
| Q11ObsDR | varchar |  | FK | SI | Uterus position DR |
| Q12 | varchar |  |  | SI | Note |
| Q13 | varchar |  |  | SI | Uterus size |
| Q13ObsDR | varchar |  | FK | SI | Uterus size DR |
| Q14 | varchar |  |  | SI | Note |
| Q15 | varchar |  |  | SI | Prolapse |
| Q15ObsDR | varchar |  | FK | SI | Prolapse DR |
| Q16 | varchar |  |  | SI | Note |
| Q17 | varchar |  |  | SI | Adnexa |
| Q17ObsDR | varchar |  | FK | SI | Adnexa DR |
| Q18 | varchar |  |  | SI | Note |
| Q19 | varchar |  |  | SI | Note (Other) |
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