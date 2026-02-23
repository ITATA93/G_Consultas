# questionnaire.QTCCAUTICIV

> Catheter Associated Urinary Tract Infection Care - Insertion Bundle - Italian version

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Catheter Associated Urinary Tract Infection Care - Insertion Bundle - Italian version

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Catheter placement and management |
| Q04 | date |  |  | SI | Date of prescription |
| Q05 | date |  |  | SI | Catheter insertion date |
| Q06 | varchar |  |  | SI | Doctor name |
| Q07 | varchar |  |  | SI | Nurse / midwife name |
| Q08 | varchar |  |  | SI | Have alternatives to urinary catheter placement be... |
| Q09 | varchar |  |  | SI | Aseptic procedure followed for urinary catheter in... |
| Q10 | varchar |  |  | SI | Was the smallest possible urinary catheter used an... |
| Q11 | varchar |  |  | SI | Was the urethral meatus cleaned and sterile single... |
| Q12 | varchar |  |  | SI | Has aseptic technique been maintained until the ur... |
| Q13 | varchar |  |  | SI | Has a sterile drainage system been used, equipped ... |
| Q14 | varchar |  |  | SI | Was hand hygiene carried out before any procedure ... |
| Q15 | varchar |  |  | SI | Has the need to keep the urinary catheter in place... |
| Q16 | varchar |  |  | SI | Was the hygiene of the urethral meatus performed d... |
| Q17 | varchar |  |  | SI | Has the urinary catheter been kept continuously co... |
| Q18 | varchar |  |  | SI | Has the drainage bag been emptied when an aseptic,... |
| Q19 | varchar |  |  | SI | Has the drainage bag been placed lower than the bl... |
| Q20 | varchar |  |  | SI | Comments |
| Q21 | varchar |  |  | SI | Bundle Compliance Percentage |
| Q22 | varchar |  |  | SI | % |
| Q23 | varchar |  |  | SI | Score |
| Q24 | varchar |  |  | SI | Classification |
| Q25 | varchar |  |  | SI | 0 - 100 |
| Q26 | varchar |  |  | SI | Higher percentages represent higher compliance to ... |
| Q27 | varchar |  |  | SI | 0 - 100: Higher percentages represent higher compl... |
| Q28 | varchar |  |  | SI | Catheter Associated Urinary Tract Infection Care -... |
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