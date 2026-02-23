# questionnaire.QTCNSPPSSA

> Pre/Post Spinal Surgery Assessment

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pre/Post Spinal Surgery Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Type of Assessment |
| Q02 | varchar |  |  | SI | Does patient have any red flags? |
| Q03 | varchar |  |  | SI | Level of Procedure |
| Q04 | varchar |  |  | SI | Type of Procedure |
| Q05 | varchar |  |  | SI | Special Precautions / Indications |
| Q06 | varchar |  |  | SI | Recommended Spinal Support |
| Q07 | varchar |  |  | SI | Prior Level of Function |
| Q08 | varchar |  |  | SI | Home / Office Setup |
| Q09 | varchar |  |  | SI | Has the patient attended regular physiotherapy ses... |
| Q10 | varchar |  |  | SI | Kind Of Physiotherapy Treatment |
| Q11 | varchar |  |  | SI | Indicate the Areas on Diagram (Surgery Site, Pain,... |
| Q11A | varchar |  |  | SI | Indicate the Areas on Diagram (Surgery Site, Pain,... |
| Q12 | varchar |  |  | SI | Pain Score |
| Q12ObsDR | varchar |  | FK | SI | Pain Score DR |
| Q13 | varchar |  |  | SI | Type of Pain |
| Q13ObsDR | varchar |  | FK | SI | Type of Pain DR |
| Q14 | varchar |  |  | SI | Do any other affected areas (other than Surgical) ... |
| Q14A | varchar |  |  | SI | Area |
| Q15 | varchar |  |  | SI | Drain placed on surgery site? |
| Q16 | varchar |  |  | SI | Complain of Intraoperative Position? |
| Q17 | varchar |  |  | SI | Area |
| Q19 | varchar |  |  | SI | Sensory Testing |
| Q20 | varchar |  |  | SI | Type of Sensory Test |
| Q21 | varchar |  |  | SI | Comparison left to right in %= ? |
| Q22 | varchar |  |  | SI | Mark Affected Dermatomes |
| Q22A | varchar |  |  | SI | Mark Affected Dermatomes |
| Q23 | varchar |  |  | SI | Any Anal Sensation |
| Q23ObsDR | varchar |  | FK | SI | Any Anal Sensation DR |
| Q25 | varchar |  |  | SI | Plan of Intervention |
| Q26 | varchar |  |  | SI | Referral to |
| Q27 | varchar |  |  | SI | Checklist |
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