# SQLUser.FHC_TypeOfArea

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FHCTOA_RowId | bigint | PK |  | NO | - |
| FHCTOA_Code | varchar |  |  | NO | TypeOfArea Code |
| FHCTOA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FHCTOA_CreatedDate | date |  |  | SI | Created Date |
| FHCTOA_CreatedTime | time |  |  | SI | Created Time |
| FHCTOA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FHCTOA_DateFrom | date |  |  | NO | Date From |
| FHCTOA_DateTo | date |  |  | SI | Date To |
| FHCTOA_Desc | varchar |  |  | NO | TypeOfArea Description |
| FHCTOA_NationalCode | varchar |  |  | SI | National Code |
| FHCTOA_Owner | varchar |  |  | SI | Owner |
| FHCTOA_UpdatedDate | date |  |  | SI | Updated Date |
| FHCTOA_UpdatedTime | time |  |  | SI | Updated Time |
| FHCTOA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Catheter placement and management |
| Q04 | - |  |  | SI | Date of prescription |
| Q05 | - |  |  | SI | Catheter insertion date |
| Q06 | - |  |  | SI | Doctor name |
| Q07 | - |  |  | SI | Nurse / midwife name |
| Q08 | - |  |  | SI | Have alternatives to urinary catheter placement be... |
| Q09 | - |  |  | SI | Aseptic procedure followed for urinary catheter in... |
| Q10 | - |  |  | SI | Was the smallest possible urinary catheter used an... |
| Q11 | - |  |  | SI | Was the urethral meatus cleaned and sterile single... |
| Q12 | - |  |  | SI | Has aseptic technique been maintained until the ur... |
| Q13 | - |  |  | SI | Has a sterile drainage system been used, equipped ... |
| Q14 | - |  |  | SI | Was hand hygiene carried out before any procedure ... |
| Q15 | - |  |  | SI | Has the need to keep the urinary catheter in place... |
| Q16 | - |  |  | SI | Was the hygiene of the urethral meatus performed d... |
| Q17 | - |  |  | SI | Has the urinary catheter been kept continuously co... |
| Q18 | - |  |  | SI | Has the drainage bag been emptied when an aseptic,... |
| Q19 | - |  |  | SI | Has the drainage bag been placed lower than the bl... |
| Q20 | - |  |  | SI | Comments |
| Q21 | - |  |  | SI | Bundle Compliance Percentage |
| Q22 | - |  |  | SI | % |
| Q23 | - |  |  | SI | Score |
| Q24 | - |  |  | SI | Classification |
| Q25 | - |  |  | SI | 0 - 100 |
| Q26 | - |  |  | SI | Higher percentages represent higher compliance to ... |
| Q27 | - |  |  | SI | 0 - 100: Higher percentages represent higher compl... |
| Q28 | - |  |  | SI | Catheter Associated Urinary Tract Infection Care -... |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*