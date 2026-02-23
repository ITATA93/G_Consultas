# SQLUser.PAC_VisitorStatus

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISST_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Symptom Assessment |
| Q04 | - |  |  | SI | Cough |
| Q05 | - |  |  | SI | Other cough notes |
| Q06 | - |  |  | SI | Sputum |
| Q07 | - |  |  | SI | Other sputum notes |
| Q08 | - |  |  | SI | Sputum amount |
| Q09 | - |  |  | SI | Shortness of Breath (SOB) |
| Q10 | - |  |  | SI | Other SOB notes |
| Q11 | - |  |  | SI | Client able to walk |
| Q12 | - |  |  | SI | Dyspnoea Severity (Modified Medical Research Counc... |
| Q12ObsDR | - |  |  | SI | Dyspnoea Severity (Modified Medical Research Counc... |
| Q13 | - |  |  | SI | Sleeping |
| Q14 | - |  |  | SI | Other sleeping notes |
| Q15 | - |  |  | SI | Symptom assessment notes |
| Q16 | - |  |  | SI | Medications / Medication Devices |
| Q17 | - |  |  | SI | Observe inhaler / device technique at each visit |
| Q18 | - |  |  | SI | Review of current inhalers conducted |
| Q19 | - |  |  | SI | Inhaler observation and review notes |
| Q20 | - |  |  | SI | Distance walked |
| Q21 | - |  |  | SI | Information / Education and Support |
| Q22 | - |  |  | SI | Topics covered |
| Q23 | - |  |  | SI | Other topics covered |
| Q24 | - |  |  | SI | Support network |
| Q25 | - |  |  | SI | Other support |
| Q26 | - |  |  | SI | Information / Education and support notes |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| VISST_Code | varchar |  |  | NO | Code |
| VISST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VISST_CreatedDate | date |  |  | SI | Created Date |
| VISST_CreatedTime | time |  |  | SI | Created Time |
| VISST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VISST_DateFrom | date |  |  | SI | Date From |
| VISST_DateTo | date |  |  | SI | Date To |
| VISST_Desc | varchar |  |  | NO | Description |
| VISST_Owner | varchar |  |  | SI | Owner |
| VISST_UpdatedDate | date |  |  | SI | Updated Date |
| VISST_UpdatedTime | time |  |  | SI | Updated Time |
| VISST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*