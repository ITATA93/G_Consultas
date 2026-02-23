# SQLUser.PA_Pathway

**Schema:** SQLUser
**Columnas:** 41
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Datos de Paciente**. Información demográfica y administrativa.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATH_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| PATH_BaseProtocol_DR | bigint |  | FK | SI | Based on Protocol DR |
| PATH_CPWType_DR | bigint |  | FK | SI | Pathway Type |
| PATH_Childsub | double |  |  | NO | Childsub |
| PATH_ClinicalTrialArm_DR | varchar |  | FK | SI | Clinical Trial Arm DR |
| PATH_Consent | bigint |  |  | SI | Patient Consent Document |
| PATH_ConsentDate | date |  |  | SI | Patient Consent Received Date |
| PATH_ConsentGiven | bit |  |  | SI | Patient Consent Received |
| PATH_ConsentTime | time |  |  | SI | Patient Consent Received Time |
| PATH_CreateDate | date |  |  | SI | CreateDate |
| PATH_CreateTime | time |  |  | SI | CreateTime |
| PATH_CreatedByCareProvider_DR | bigint |  | FK | SI | Care Provider that Initiated the Clinical Pathway |
| PATH_CreatedByWizard | bit |  |  | SI | Created by the Nursing Care Plan Wizard |
| PATH_Desc | varchar |  |  | SI | Pathway Description
Either Based on Protocol Desc... |
| PATH_DraftNCP | bit |  |  | SI | Draft of Nursing Care Plan |
| PATH_EndedDate | date |  |  | SI | Ended Date |
| PATH_EnrollingCareProvider_DR | varchar |  | FK | SI | Enrolling Care Provider |
| PATH_EnrollmentID | varchar |  |  | SI | Enrollment ID |
| PATH_ExitItem_DR | varchar |  | FK | SI | Exit item |
| PATH_InclusionNumber | varchar |  |  | SI | Inclusion Number |
| PATH_Intent | varchar |  |  | SI | Protocol Intent |
| PATH_MergeAcknowledge_DR | bigint |  | FK | SI | Patient Merge Acknowledge |
| PATH_MergePatient_DR | bigint |  | FK | SI | Patient Merge Info If Pathway has been copied due ... |
| PATH_NursingProblems | varchar |  |  | SI | Nursing Problems List |
| PATH_Outcome_DR | bigint |  | FK | SI | Pathway Outcome |
| PATH_PlannedStartDate | date |  |  | SI | Planned Start Date |
| PATH_Problem_DR | varchar |  | FK | SI | Patient Problem DR |
| PATH_ReasonScreenFailure_DR | bigint |  | FK | SI | Clinical Trial Reason For Screening Failure |
| PATH_RowId | varchar |  |  | NO | - |
| PATH_ScreeningConsentDate | date |  |  | SI | Screening Consent Date |
| PATH_ScreeningDate | date |  |  | SI | Screening Date |
| PATH_ScreeningNumber | varchar |  |  | SI | Screening Number |
| PATH_ScreeningOutcome | varchar |  |  | SI | Screening Outcome |
| PATH_Status | varchar |  |  | SI | Status |
| PATH_Trial_DR | bigint |  | FK | SI | Clinical Trial DR |
| PATH_UnmergedCopy | bit |  |  | SI | Boolean indicating whether the pathway is leftover... |
| PATH_UpdateDate | date |  |  | SI | UpdateDate |
| PATH_UpdateTime | time |  |  | SI | UpdateTime |
| PATH_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| PATH_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| PATH_WizardCompatible | bit |  |  | SI | Nursing Care Plan Wizard Compatible |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*