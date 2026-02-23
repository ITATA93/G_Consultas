# questionnaire.QTCCAUTIINS

> Catheter Associated Urinary Tract Infection - Insertion Procedure

**Schema:** questionnaire
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Catheter Associated Urinary Tract Infection - Insertion Procedure

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Catheter urinary tract infection - Insertion bundl... |
| Q02 | date |  |  | SI | Date |
| Q03 | time |  |  | SI | Time |
| Q04 | date |  |  | SI | Catheter insertion date |
| Q05 | varchar |  |  | SI | Have alternatives to urinary catheter placement be... |
| Q06 | varchar |  |  | SI | Aseptic procedure followed for urinary catheter in... |
| Q07 | varchar |  |  | SI | Was the smallest possible urinary catheter used? |
| Q08 | varchar |  |  | SI | Once the catheter has been inserted, has the ballo... |
| Q09 | varchar |  |  | SI | Was the urethral meatus cleaned and sterile single... |
| Q10 | varchar |  |  | SI | Has aseptic technique been maintained until the ur... |
| Q11 | varchar |  |  | SI | Has a sterile drainage system been used, equipped ... |
| Q12 | varchar |  |  | SI | Comments |
| Q13 | varchar |  |  | SI | Bundle compliance percentage |
| Q14 | varchar |  |  | SI | % |
| Q15 | varchar |  |  | SI | Guidelines |
| Q16 | varchar |  |  | SI | 0 - 100%:  higher percentages represent higher com... |
| Q17 | varchar |  |  | SI | 0 - 100 |
| Q18 | varchar |  |  | SI | higher percentages represent higher compliance to ... |
| Q19 | varchar |  |  | SI | Score |
| Q20 | varchar |  |  | SI | Classification |
| Q21 | varchar |  |  | SI | Catheter Associated Urinary Tract Infection - Inse... |
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