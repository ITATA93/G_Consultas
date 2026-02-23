# SQLUser.PA_Allergy

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALG_PAPMI_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| ALG_AllergyGrp_DR | bigint |  | FK | SI | Des Ref Allergy Group |
| ALG_CTPCP_DR | varchar |  | FK | SI | CTCP DR |
| ALG_Category_DR | bigint |  | FK | SI | Des Ref Category - Nature of Reaction |
| ALG_Certainty_DR | bigint |  | FK | SI | Des Ref Certainty |
| ALG_ChildSub | double |  |  | NO | Child Sub |
| ALG_Comments | varchar |  |  | SI | Comments |
| ALG_ConfirmedDate | date |  |  | SI | Connfirmed Date |
| ALG_ConfirmedTime | time |  |  | SI | Confirmed Time |
| ALG_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| ALG_Date | date |  |  | SI | Date |
| ALG_Desc | varchar |  |  | SI | Description |
| ALG_DrugSpecific | varchar |  |  | SI | DrugSpecific |
| ALG_DuratDays | double |  |  | SI | Duration in Days |
| ALG_DuratMonth | double |  |  | SI | Duration in Month |
| ALG_DuratYear | double |  |  | SI | Duration in Year |
| ALG_Entered | varchar |  |  | SI | Entered Allergy |
| ALG_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| ALG_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| ALG_ExpiryDate | date |  |  | SI | Expirey Date |
| ALG_ExternalID | varchar |  |  | SI | ExternalID |
| ALG_FreeTextAllergy | varchar |  |  | SI | FreeTextAllergy |
| ALG_InActive | varchar |  |  | SI | InActive |
| ALG_InactiveDate | date |  |  | SI | Inactive Date |
| ALG_InactiveFreeText | varchar |  |  | SI | Inactive Free Text |
| ALG_Ingred_DR | bigint |  | FK | SI | Des Ref Ingred |
| ALG_IsSensitivity | varchar |  |  | SI | Sensitivity Flag |
| ALG_LastUpdateDate | date |  |  | SI | Last Update Date |
| ALG_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| ALG_LastUpdateTime | time |  |  | SI | Last Update Time |
| ALG_MRCAllType_DR | bigint |  | FK | SI | Des Ref to MRC_AllType - Allergy Category |
| ALG_OnsetDate | date |  |  | SI | Onset Date |
| ALG_OnsetDateFreeText | varchar |  |  | SI | OnsetDateFreeText |
| ALG_OthAllergy | varchar |  |  | SI | Other Allergy |
| ALG_PHCDM_DR | bigint |  | FK | SI | Des Ref PHCDM |
| ALG_PHCDRGForm_DR | varchar |  | FK | SI | Des Ref PHCDRGForm |
| ALG_PHCGE_DR | bigint |  | FK | SI | PHCGE_DR |
| ALG_PHCSC_DR | varchar |  | FK | SI | PHCSC DR |
| ALG_Reaction | varchar |  |  | SI | Reaction To Allergy |
| ALG_ReasForChange_DR | bigint |  | FK | SI | Des Ref ReasForChange |
| ALG_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref Reason For Correction |
| ALG_ReasonNotCoded | varchar |  |  | SI | Reason Not Coded |
| ALG_RequireAssistanceMeal | varchar |  |  | SI | RequireAssistanceMeal |
| ALG_RequireAssistanceMenu | varchar |  |  | SI | RequireAssistanceMenu |
| ALG_RowID | varchar |  |  | NO | - |
| ALG_Severity_DR | bigint |  | FK | SI | Des Ref Severity |
| ALG_Sort | varchar |  |  | SI | Sort |
| ALG_Status | varchar |  |  | SI | Status |
| ALG_Time | time |  |  | SI | Time |
| ALG_Type_DR | bigint |  | FK | SI | Allergy |
| ALG_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| ALG_VerifiedDate | date |  |  | SI | Verified Date (Date signed as opposed to date conf... |
| ALG_VerifiedTime | time |  |  | SI | Verified Time |
| ChildQ16DR | - |  |  | SI | Child Reference: Daily Shift Assessment |
| Q01 | - |  |  | SI | Skin preparation |
| Q02 | - |  |  | SI | Checklist |
| Q03 | - |  |  | SI | Number of insertion attempts |
| Q04 | - |  |  | SI | Information |
| Q05 | - |  |  | SI | Date inserted |
| Q06 | - |  |  | SI | Time inserted |
| Q07 | - |  |  | SI | Date removed |
| Q08 | - |  |  | SI | Time removed |
| Q09 | - |  |  | SI | Date infection found |
| Q10 | - |  |  | SI | Time infection found |
| Q11 | - |  |  | SI | Date infection healed |
| Q12 | - |  |  | SI | Time infection healed |
| Q13 | - |  |  | SI | Type |
| Q13a | - |  |  | SI | Type |
| Q13aObsDR | - |  |  | SI | Type DR |
| Q14 | - |  |  | SI | Material |
| Q15 | - |  |  | SI | Catheter-Associated Urinary Track Infection type |
| Q17 | - |  |  | SI | Fixation Device |
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