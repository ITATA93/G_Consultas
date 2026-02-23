# questionnaire.QTCMTCOLPF

> Colposcopy Report - Follow up

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Colposcopy Report - Follow up

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Treatment date |
| Q03 | varchar |  |  | SI | Treatment type - old |
| Q07 | date |  |  | SI | Follow up date - old |
| Q08 | numeric |  |  | SI | Follow up no |
| Q09 | numeric |  |  | SI | Pregnant months |
| Q16 | varchar |  |  | SI | Cytology old |
| Q17 | varchar |  |  | SI | Other comments |
| Q18 | varchar |  |  | SI | Diagnosis |
| Q19 | varchar |  |  | SI | Abnormal features |
| Q20 | varchar |  |  | SI | Colposcopy diagram |
| Q21 | numeric |  |  | SI | Months |
| Q22 | varchar |  |  | SI | Extent of lesion |
| Q23 | bit |  |  | SI | Plan to review old |
| Q24 | varchar |  |  | SI | Plan for treatment details |
| Q25 | bit |  |  | SI | Plan for treatment |
| Q26 | varchar |  |  | SI | Treatment comments |
| Q27 | date |  |  | SI | Treatment date |
| Q28 | bit |  |  | SI | Plan to review |
| Q29 | varchar |  |  | SI | Treatment type |
| Q30 | varchar |  |  | SI | Colposcopy |
| Q31 | varchar |  |  | SI | Directed biopsy |
| Q32 | date |  |  | SI | Follow up date |
| Q33 | varchar |  |  | SI | Cytology |
| Q34 | varchar |  |  | SI | Cytology |
| Q35 | varchar |  |  | SI | Colposcopy |
| Q36 | date |  |  | SI | Date |
| Q37 | time |  |  | SI | Time |
| Q38 | varchar |  |  | SI | Plan to review |
| Q39 | varchar |  |  | SI | Plan for treatment |
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