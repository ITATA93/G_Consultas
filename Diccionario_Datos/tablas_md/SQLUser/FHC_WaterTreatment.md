# SQLUser.FHC_WaterTreatment

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Hogar/Familia**. Parámetros de entorno familiar.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FHCWT_RowId | bigint | PK |  | NO | - |
| FHCWT_Code | varchar |  |  | NO | Water Treatment Code |
| FHCWT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FHCWT_CreatedDate | date |  |  | SI | Created Date |
| FHCWT_CreatedTime | time |  |  | SI | Created Time |
| FHCWT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FHCWT_DateFrom | date |  |  | NO | Date From |
| FHCWT_DateTo | date |  |  | SI | Date To |
| FHCWT_Desc | varchar |  |  | NO | Water Treatment Description |
| FHCWT_NationalCode | varchar |  |  | SI | National Code |
| FHCWT_Owner | varchar |  |  | SI | Owner |
| FHCWT_UpdatedDate | date |  |  | SI | Updated Date |
| FHCWT_UpdatedTime | time |  |  | SI | Updated Time |
| FHCWT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Catheter urinary tract infection - Insertion bundl... |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Catheter insertion date |
| Q05 | - |  |  | SI | Have alternatives to urinary catheter placement be... |
| Q06 | - |  |  | SI | Aseptic procedure followed for urinary catheter in... |
| Q07 | - |  |  | SI | Was the smallest possible urinary catheter used? |
| Q08 | - |  |  | SI | Once the catheter has been inserted, has the ballo... |
| Q09 | - |  |  | SI | Was the urethral meatus cleaned and sterile single... |
| Q10 | - |  |  | SI | Has aseptic technique been maintained until the ur... |
| Q11 | - |  |  | SI | Has a sterile drainage system been used, equipped ... |
| Q12 | - |  |  | SI | Comments |
| Q13 | - |  |  | SI | Bundle compliance percentage |
| Q14 | - |  |  | SI | % |
| Q15 | - |  |  | SI | Guidelines |
| Q16 | - |  |  | SI | 0 - 100%:  higher percentages represent higher com... |
| Q17 | - |  |  | SI | 0 - 100 |
| Q18 | - |  |  | SI | higher percentages represent higher compliance to ... |
| Q19 | - |  |  | SI | Score |
| Q20 | - |  |  | SI | Classification |
| Q21 | - |  |  | SI | Catheter Associated Urinary Tract Infection - Inse... |
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