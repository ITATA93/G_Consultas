# SQLUser.CT_Religion

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTRLG_RowId | bigint | PK |  | NO | - |
| CTRLG_Code | varchar |  |  | NO | Religion Code |
| CTRLG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTRLG_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| CTRLG_CreatedDate | date |  |  | SI | Created Date |
| CTRLG_CreatedTime | time |  |  | SI | Created Time |
| CTRLG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTRLG_DateFrom | date |  |  | SI | Date From |
| CTRLG_DateTo | date |  |  | SI | Date to |
| CTRLG_Desc | varchar |  |  | NO | Religion Description |
| CTRLG_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| CTRLG_Owner | varchar |  |  | SI | Owner |
| CTRLG_UpdatedDate | date |  |  | SI | Updated Date |
| CTRLG_UpdatedTime | time |  |  | SI | Updated Time |
| CTRLG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Weight |
| Q03ObsDR | - |  |  | SI | Weight DR |
| Q04 | - |  |  | SI | kg |
| Q05 | - |  |  | SI | Height |
| Q05ObsDR | - |  |  | SI | Height DR |
| Q06 | - |  |  | SI | cm |
| Q07 | - |  |  | SI | BMI |
| Q08 | - |  |  | SI | AST |
| Q09 | - |  |  | SI | U/L |
| Q10 | - |  |  | SI | ALT |
| Q11 | - |  |  | SI | U/L |
| Q12 | - |  |  | SI | Diabetes mellitus |
| Q13 | - |  |  | SI | BARD Score |
| Q14 | - |  |  | SI | BARD Score Interpretation |
| Q15 | - |  |  | SI | High risk of advanced hepatic fibrosis (positive p... |
| Q16 | - |  |  | SI | Low risk of advanced hepatic fibrosis (negative pr... |
| Q17 | - |  |  | SI | Test performance will be affected by the prevalenc... |
| Q18 | - |  |  | SI | Score |
| Q19 | - |  |  | SI | Classification |
| Q20 | - |  |  | SI | 0 - 1 |
| Q21 | - |  |  | SI | Low risk of advanced hepatic fibrosis (negative pr... |
| Q22 | - |  |  | SI | 2 - 4 |
| Q23 | - |  |  | SI | High risk of advanced hepatic fibrosis (positive p... |
| Q24 | - |  |  | SI | 0 - 1: Low risk of advanced hepatic fibrosis (nega... |
| Q25 | - |  |  | SI | 2 - 4: High risk of advanced hepatic fibrosis (pos... |
| Q26 | - |  |  | SI | To identify patients with non-alcoholic fatty live... |
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