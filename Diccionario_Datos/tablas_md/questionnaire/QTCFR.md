# questionnaire.QTCFR

> Fibroscan Referral

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fibroscan Referral

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Indication |
| Q04 | varchar |  |  | SI | Other indication |
| Q05 | varchar |  |  | SI | Known cirrhosis |
| Q06 | varchar |  |  | SI | Ascites |
| Q07 | varchar |  |  | SI | Currently pregnant |
| Q08 | varchar |  |  | SI | Mass liver lesion |
| Q09 | varchar |  |  | SI | Exclusion Criteria - Do not proceed with the Fibro... |
| Q10 | varchar |  |  | SI | Previous fibroscan |
| Q11 | date |  |  | SI | Date |
| Q12 | varchar |  |  | SI | Previous liver biopsy |
| Q13 | date |  |  | SI | Date |
| Q14 | varchar |  |  | SI | Recent liver ultrasound |
| Q15 | varchar |  |  | SI | Exclusion Criteria - Do not proceed with the Fibro... |
| Q16 | varchar |  |  | SI | Exclusion Criteria - Do not proceed with the Fibro... |
| Q17 | varchar |  |  | SI | Exclusion Criteria - Do not proceed with the Fibro... |
| Q18 | varchar |  |  | SI | Exclusion Criteria - Do not proceed with the Fibro... |
| Q19 | varchar |  |  | SI | Exclusion Criteria |
| Q20 | varchar |  |  | SI | Meets exclusion criteria - Do not proceed with fib... |
| Q21 | varchar |  |  | SI | Has 'Yes' been selected as an answer, to any of th... |
| Q22 | varchar |  |  | SI | Meets exclusion criteria - Do not proceed with fib... |
| Q23 | varchar |  |  | SI | Other tests |
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