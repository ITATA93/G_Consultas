# questionnaire.QTCAHPAUAP

> Audiology - Pediatrics

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Audiology - Pediatrics

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Type of Session |
| Q02 | varchar |  |  | SI | Referral Source |
| Q03 | varchar |  |  | SI | Referral Source Comment |
| Q04 | varchar |  |  | SI | Remarkable |
| Q05 | varchar |  |  | SI | Family History of Hearing Loss |
| Q06 | varchar |  |  | SI | Recurrent Ear Infections |
| Q07 | varchar |  |  | SI | Parental Concerns |
| Q08 | varchar |  |  | SI | Comment |
| Q09 | varchar |  |  | SI | Presence of Hearing Loss |
| Q10 | varchar |  |  | SI | Onset of Hearing Loss |
| Q11 | varchar |  |  | SI | Hearing Aid Use |
| Q12 | varchar |  |  | SI | Previous Audiological Assessment |
| Q13 | varchar |  |  | SI | Results of Previous Assessment |
| Q14 | varchar |  |  | SI | Fever |
| Q15 | varchar |  |  | SI | Otoscopy Test Result |
| Q16 | varchar |  |  | SI | Otoscopy Comment |
| Q17 | varchar |  |  | SI | Tympanometry (Right) |
| Q18 | varchar |  |  | SI | Tympanometry (Left) |
| Q19 | varchar |  |  | SI | Distortion Product Otoacoustic Emission (DPOAE) |
| Q20 | varchar |  |  | SI | Right Ear |
| Q21 | varchar |  |  | SI | Left Ear |
| Q22 | varchar |  |  | SI | Transient Evoked Otoacoustic Emission (TEOAE) |
| Q23 | varchar |  |  | SI | Right Ear |
| Q24 | varchar |  |  | SI | Left Ear |
| Q25 | varchar |  |  | SI | Behavioral Hearing Test Performed |
| Q26 | varchar |  |  | SI | Reliability |
| Q27 | varchar |  |  | SI | Final Outcome |
| Q28 | varchar |  |  | SI | Final Outcome Comment |
| Q29 | varchar |  |  | SI | Recommendations |
| Q30 | varchar |  |  | SI | Recommendations Comment |
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