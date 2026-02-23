# questionnaire.QTCIVFITBA

> Infertility Treatment Baseline Assessment

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Infertility Treatment Baseline Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Treatment |
| Q01A | numeric |  |  | SI | Number of Frozen Embryos |
| Q01B | date |  |  | SI | Date of Lupron Injection |
| Q01C | date |  |  | SI | Date of Baseline Ultrasound |
| Q01D | varchar |  |  | SI | Thawing Embryo Consent Signed |
| Q02 | varchar |  |  | SI | Last menstrual period |
| Q02A | varchar |  |  | SI | Type of Infertility |
| Q02B | varchar |  |  | SI | Cause of Infertility |
| Q02C | numeric |  |  | SI | Duration (years) |
| Q02D | varchar |  |  | SI | Protocol |
| Q02E | varchar |  |  | SI | Medications |
| Q02F | varchar |  |  | SI | IVF or ICSI |
| Q02G | date |  |  | SI | Date of Starting Protocol |
| Q02ObsDR | varchar |  | FK | SI | Last menstrual period DR |
| Q03 | numeric |  |  | SI | Cycle number |
| Q03A | varchar |  |  | SI | Type |
| Q03B | varchar |  |  | SI | Decapeptyl 0.1mg |
| Q03C | varchar |  |  | SI | Cetrorelix 0.25mg |
| Q04 | varchar |  |  | SI | Vital signs stable |
| Q05 | varchar |  |  | SI | Body Mass Index (BMI) - (kg/m2) |
| Q05H | varchar |  |  | SI | Height (cm) |
| Q05HObsDR | varchar |  | FK | SI | Height (cm) DR |
| Q05W | varchar |  |  | SI | Weight (kg) |
| Q05WObsDR | varchar |  | FK | SI | Weight (kg) DR |
| Q06 | varchar |  |  | SI | Educated about weight |
| Q07 | varchar |  |  | SI | Psychologic assessment |
| Q08 | varchar |  |  | SI | Education done |
| Q09 | varchar |  |  | SI | Medication instructions given |
| Q10 | varchar |  |  | SI | Comments |
| Q11 | varchar |  |  | SI | Other instructions given |
| Q28 | date |  |  | SI | Date |
| Q29 | time |  |  | SI | Time |
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