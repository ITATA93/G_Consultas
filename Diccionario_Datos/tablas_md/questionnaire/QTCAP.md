# questionnaire.QTCAP

> Amniocentesis Procedure

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Amniocentesis Procedure

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | numeric |  |  | SI | Gestation |
| Q04 | varchar |  |  | SI | weeks |
| Q05 | numeric |  |  | SI | Gestation days |
| Q06 | varchar |  |  | SI | days |
| Q07 | varchar |  |  | SI | Indication for amniocentesis |
| Q08 | varchar |  |  | SI | Other indication for amniocentesis |
| Q09 | varchar |  |  | SI | Consent obtained |
| Q10 | varchar |  |  | SI | Serology checked |
| Q11 | varchar |  |  | SI | Rhesus status checked |
| Q12 | varchar |  |  | SI | Plurality |
| Q13 | varchar |  |  | SI | Fetal cardiac activity pre procedure |
| Q14 | numeric |  |  | SI | Fetal heart rate pre procedure (bpm) |
| Q15 | varchar |  |  | SI | Fetus 2 cardiac activity pre procedure |
| Q16 | numeric |  |  | SI | Fetus 2 heart rate pre procedure (bpm) |
| Q17 | varchar |  |  | SI | Fetus 3 cardiac activity pre procedure |
| Q18 | varchar |  |  | SI | Placenta traversed |
| Q19 | numeric |  |  | SI | Volume amniotic fluid obtained (mls) |
| Q20 | varchar |  |  | SI | Amniotic fluid aspect |
| Q21 | varchar |  |  | SI | Other amniotic fluid aspect |
| Q22 | numeric |  |  | SI | Number of attempts |
| Q23 | varchar |  |  | SI | Procedure notes |
| Q24 | varchar |  |  | SI | Fetal cardiac activity post procedure |
| Q24ObsDR | varchar |  | FK | SI | Fetal cardiac activity post procedure DR |
| Q25 | varchar |  |  | SI | Fetal heart rate post procedure (bpm) |
| Q25ObsDR | varchar |  | FK | SI | Fetal heart rate post procedure (bpm) DR |
| Q26 | varchar |  |  | SI | Fetus 2 cardiac activity post procedure |
| Q26ObsDR | varchar |  | FK | SI | Fetus 2 cardiac activity post procedure DR |
| Q27 | varchar |  |  | SI | Fetus 2 heart rate post procedure (bpm) |
| Q27ObsDR | varchar |  | FK | SI | Fetus 2 heart rate post procedure (bpm) DR |
| Q28 | varchar |  |  | SI | Fetus 3 cardiac activity post procedure |
| Q28ObsDR | varchar |  | FK | SI | Fetus 3 cardiac activity post procedure DR |
| Q29 | varchar |  |  | SI | Fetus 3 heart rate post procedure (bpm) |
| Q29ObsDR | varchar |  | FK | SI | Fetus 3 heart rate post procedure (bpm) DR |
| Q30 | varchar |  |  | SI | Management plan |
| Q31 | numeric |  |  | SI | Fetus 3 heart rate pre procedure (bpm) |
| Q32 | varchar |  |  | SI | Pre-Procedure |
| Q33 | varchar |  |  | SI | Procedure Details |
| Q34 | varchar |  |  | SI | Post-Procedure |
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