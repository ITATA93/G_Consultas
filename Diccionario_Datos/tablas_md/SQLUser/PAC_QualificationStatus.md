# SQLUser.PAC_QualificationStatus

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUAL_RowId | bigint | PK |  | NO | - |
| ChildQ02DR | - |  |  | SI | Child Reference: Skin preparation used |
| Q01 | - |  |  | SI | Procedure |
| QUAL_AdmReason | varchar |  |  | SI | AdmReason |
| QUAL_AgeFrom | double |  |  | SI | Age From |
| QUAL_AgeTo | double |  |  | SI | Age To |
| QUAL_AgeType | varchar |  |  | SI | Age Type |
| QUAL_Code | varchar |  |  | SI | Code |
| QUAL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QUAL_CreatedDate | date |  |  | SI | Created Date |
| QUAL_CreatedTime | time |  |  | SI | Created Time |
| QUAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QUAL_CriteriaForAdm | varchar |  |  | SI | Criteria for Admission codes |
| QUAL_DateFrom | date |  |  | SI | DateFrom |
| QUAL_DateTo | date |  |  | SI | DateTo |
| QUAL_Desc | varchar |  |  | SI | Description |
| QUAL_InPatAdmType | varchar |  |  | SI | InPat Admission Type codes |
| QUAL_NationalCode | varchar |  |  | SI | NationalCode |
| QUAL_Owner | varchar |  |  | SI | Owner |
| QUAL_QualifiedNewborn | varchar |  |  | SI | Qualified Newborn |
| QUAL_SourceOfAdmission | varchar |  |  | SI | Source of Admission codes |
| QUAL_UnqualifiedNewborn | varchar |  |  | SI | Unqualified Newborn |
| QUAL_UpdatedDate | date |  |  | SI | Updated Date |
| QUAL_UpdatedTime | time |  |  | SI | Updated Time |
| QUAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
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