# SQLUser.PAC_Pathway

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACP_RowId | bigint | PK |  | NO | - |
| PACP_AgeFrom | double |  |  | SI | Age From |
| PACP_AgeTo | double |  |  | SI | Age To |
| PACP_AgeUnits | varchar |  |  | SI | Age Units |
| PACP_CPWType_DR | bigint |  | FK | SI | Des Ref Pathway Type |
| PACP_ClinicalTrialArm_DR | varchar |  | FK | SI | Clinical Trial Arm |
| PACP_Code | varchar |  |  | NO | Code |
| PACP_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| PACP_Consent_DR | bigint |  | FK | SI | Patient Consent |
| PACP_CreatedDate | date |  |  | SI | Created Date |
| PACP_CreatedTime | time |  |  | SI | Created Time |
| PACP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACP_DateFrom | date |  |  | SI | Date From |
| PACP_DateTo | date |  |  | SI | Date To |
| PACP_Desc | varchar |  |  | NO | Description |
| PACP_ExitItem_DR | bigint |  | FK | SI | Des Ref Exit questionnaire |
| PACP_ExtCode | varchar |  |  | SI | ExternalProtocol Code |
| PACP_InfoLink | varchar |  |  | SI | Protocol Info Link |
| PACP_Intent | varchar |  |  | SI | Protocol Intent |
| PACP_IssueOrg | varchar |  |  | SI | Issuing Organisation  |
| PACP_OriginalProtocol_DR | bigint |  | FK | SI | Original Protocol Version |
| PACP_Owner | varchar |  |  | SI | Code Table Owner |
| PACP_Sex_DR | bigint |  | FK | SI | Des Ref to CTSEX |
| PACP_TherapeuticInd | varchar |  |  | SI | Therapeutic Indication |
| PACP_Trial_DR | bigint |  | FK | SI | Clinical Trials |
| PACP_TypicalDur | double |  |  | SI | Protocol Typical Duration |
| PACP_TypicalDurType | varchar |  |  | SI | Protocol Typical Duration Type |
| PACP_UpdatedDate | date |  |  | SI | Updated Date |
| PACP_UpdatedTime | time |  |  | SI | Updated Time |
| PACP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PACP_UsedFlag | bit |  |  | SI | Protocol Used Flag |
| PACP_Version | numeric |  |  | SI | Version |
| PACP_VersionSummary | varchar |  |  | SI | Protocol Version - Revision Summary |
| PACP_VisualRule_DR | bigint |  | FK | SI | Visual Rule |
| Q01 | - |  |  | SI | Please select one of the following |
| Q02 | - |  |  | SI | The Schwab and England ADL scale is a means of ass... |
| Q03 | - |  |  | SI | The rating can be 100% indicating total independen... |
| Q04 | - |  |  | SI | 100 percent represents complete independence |
| Q05 | - |  |  | SI | 0 percent complete dependence (bedridden) |
| Q06 | - |  |  | SI | Rated in 10% increments |
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