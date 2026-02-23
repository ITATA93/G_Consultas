# questionnaire.QGXXXCARD02

> Cardiac Exam

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac Exam

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Face-Skin Color and Texture |
| Q02 | varchar |  |  | SI | Eyes and Lids |
| Q04 | varchar |  |  | SI | Hands |
| Q05 | varchar |  |  | SI | Breathing patterns  |
| Q05ObsDR | varchar |  | FK | SI | Breathing patterns  DR |
| Q07 | varchar |  |  | SI | Cyanosis Type  |
| Q08 | varchar |  |  | SI | Precordium  |
| Q09 | varchar |  |  | SI | Rate Type |
| Q09ObsDR | varchar |  | FK | SI | Rate Type DR |
| Q10 | varchar |  |  | SI | Rate |
| Q10ObsDR | varchar |  | FK | SI | Rate DR |
| Q11 | varchar |  |  | SI | Rhythm |
| Q11ObsDR | varchar |  | FK | SI | Rhythm DR |
| Q12 | varchar |  |  | SI | Character |
| Q12ObsDR | varchar |  | FK | SI | Character DR |
| Q13 | varchar |  |  | SI | Carotid Pulse |
| Q13ObsDR | varchar |  | FK | SI | Carotid Pulse DR |
| Q14 | varchar |  |  | SI | Apex Beat |
| Q14ObsDR | varchar |  | FK | SI | Apex Beat DR |
| Q15 | varchar |  |  | SI | Jugular Vein |
| Q15ObsDR | varchar |  | FK | SI | Jugular Vein DR |
| Q16 | varchar |  |  | SI | JVP Abnormalities |
| Q17 | varchar |  |  | SI | Auscultation S1 |
| Q17ObsDR | varchar |  | FK | SI | Auscultation S1 DR |
| Q18 | varchar |  |  | SI | Auscultation S2 |
| Q18ObsDR | varchar |  | FK | SI | Auscultation S2 DR |
| Q19 | varchar |  |  | SI | Auscultation S3 |
| Q19ObsDR | varchar |  | FK | SI | Auscultation S3 DR |
| Q20 | varchar |  |  | SI | Auscultation S4 |
| Q20ObsDR | varchar |  | FK | SI | Auscultation S4 DR |
| Q21 | varchar |  |  | SI | Auscultation Findings |
| Q21ObsDR | varchar |  | FK | SI | Auscultation Findings DR |
| Q22 | varchar |  |  | SI | Cardiac Anatomy |
| Q23 | varchar |  |  | SI | Liver |
| Q24 | bit |  |  | SI | Ascites  |
| Q25 | bit |  |  | SI | Aneurysm of abdominal aorta  |
| Q26 | varchar |  |  | SI | Other Findings |
| Q27 | varchar |  |  | SI | Equality |
| Q28 | varchar |  |  | SI | femoral Pulse |
| Q28ObsDR | varchar |  | FK | SI | femoral Pulse DR |
| Q29 | varchar |  |  | SI | Poplteal Pulse |
| Q29ObsDR | varchar |  | FK | SI | Poplteal Pulse DR |
| Q30 | varchar |  |  | SI | Dorsalis Pedis Pulse |
| Q30ObsDR | varchar |  | FK | SI | Dorsalis Pedis Pulse DR |
| Q31 | varchar |  |  | SI | JVP |
| Q31ObsDR | varchar |  | FK | SI | JVP DR |
| Q32 | varchar |  |  | SI | Comment |
| Q33 | varchar |  |  | SI | Extremities |
| Q40 | varchar |  |  | SI | Arterial Pulses |
| Q41 | varchar |  |  | SI | Venous Pulses |
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