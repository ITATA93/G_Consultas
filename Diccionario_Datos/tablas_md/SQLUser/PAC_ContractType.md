# SQLUser.PAC_ContractType

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTRTYPE_RowId | bigint | PK |  | NO | - |
| CONTRTYPE_Code | varchar |  |  | NO | Code |
| CONTRTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTRTYPE_ContractRole | varchar |  |  | SI | ContractRole |
| CONTRTYPE_CreatedDate | date |  |  | SI | Created Date |
| CONTRTYPE_CreatedTime | time |  |  | SI | Created Time |
| CONTRTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTRTYPE_DateFrom | date |  |  | SI | Date From |
| CONTRTYPE_DateTo | date |  |  | SI | Date To |
| CONTRTYPE_Default | varchar |  |  | SI | Default |
| CONTRTYPE_Desc | varchar |  |  | NO | Description |
| CONTRTYPE_FundArangement | varchar |  |  | SI | FundArangement |
| CONTRTYPE_NationCode | varchar |  |  | SI | National Code |
| CONTRTYPE_Owner | varchar |  |  | SI | Owner |
| CONTRTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| CONTRTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| CONTRTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Treatment |
| Q01A | - |  |  | SI | Number of Frozen Embryos |
| Q01B | - |  |  | SI | Date of Lupron Injection |
| Q01C | - |  |  | SI | Date of Baseline Ultrasound |
| Q01D | - |  |  | SI | Thawing Embryo Consent Signed |
| Q02 | - |  |  | SI | Last menstrual period |
| Q02A | - |  |  | SI | Type of Infertility |
| Q02B | - |  |  | SI | Cause of Infertility |
| Q02C | - |  |  | SI | Duration (years) |
| Q02D | - |  |  | SI | Protocol |
| Q02E | - |  |  | SI | Medications |
| Q02F | - |  |  | SI | IVF or ICSI |
| Q02G | - |  |  | SI | Date of Starting Protocol |
| Q02ObsDR | - |  |  | SI | Last menstrual period DR |
| Q03 | - |  |  | SI | Cycle number |
| Q03A | - |  |  | SI | Type |
| Q03B | - |  |  | SI | Decapeptyl 0.1mg |
| Q03C | - |  |  | SI | Cetrorelix 0.25mg |
| Q04 | - |  |  | SI | Vital signs stable |
| Q05 | - |  |  | SI | Body Mass Index (BMI) - (kg/m2) |
| Q05H | - |  |  | SI | Height (cm) |
| Q05HObsDR | - |  |  | SI | Height (cm) DR |
| Q05W | - |  |  | SI | Weight (kg) |
| Q05WObsDR | - |  |  | SI | Weight (kg) DR |
| Q06 | - |  |  | SI | Educated about weight |
| Q07 | - |  |  | SI | Psychologic assessment |
| Q08 | - |  |  | SI | Education done |
| Q09 | - |  |  | SI | Medication instructions given |
| Q10 | - |  |  | SI | Comments |
| Q11 | - |  |  | SI | Other instructions given |
| Q28 | - |  |  | SI | Date |
| Q29 | - |  |  | SI | Time |
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