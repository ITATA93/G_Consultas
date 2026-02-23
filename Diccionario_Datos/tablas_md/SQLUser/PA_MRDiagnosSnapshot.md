# SQLUser.PA_MRDiagnosSnapshot

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAMRDIA_RowId | bigint | PK |  | NO | - |
| PAMRDIA_AccidentDate | varchar |  |  | SI | AccidentDate |
| PAMRDIA_Active | varchar |  |  | SI | Active |
| PAMRDIA_AdditionalDignosis | varchar |  |  | SI | AdditionalDignosis |
| PAMRDIA_AdminCategory_DR | bigint |  | FK | SI | Des Ref AccountClass |
| PAMRDIA_AliasDiagText | varchar |  |  | SI | AliasDiagText |
| PAMRDIA_Approximate | varchar |  |  | SI | Approximate |
| PAMRDIA_AutoAssignedFlg | varchar |  |  | SI | Auto Assigned Flag |
| PAMRDIA_AuxInsType_DR | bigint |  | FK | SI | Des Ref to AuxInsType |
| PAMRDIA_BodySite_DR | bigint |  | FK | SI | Des Ref BodySite |
| PAMRDIA_CommReportedDate | date |  |  | SI | Commissioning Reported Date |
| PAMRDIA_ComorbidCode | varchar |  |  | SI | Code - if Comorbid Condition Terminology link was ... |
| PAMRDIA_ComorbidDesc | varchar |  |  | SI | Description - if Comorbid Condition Terminology li... |
| PAMRDIA_ComorbidSelected | varchar |  |  | SI | Selected Description - if Comorbid Condition Termi... |
| PAMRDIA_Consult_DR | varchar |  | FK | SI | Des Ref Consult |
| PAMRDIA_ContractFlag_DR | bigint |  | FK | SI | Des Ref ContractFlag |
| PAMRDIA_CopyToEpisode_DR | bigint |  | FK | SI | Des Ref to PAAdm - Copied To Linked Episode |
| PAMRDIA_CopyToHistory | varchar |  |  | SI | Copy To History - Used in web.Msg.MRDiagnos |
| PAMRDIA_Cosmetic | varchar |  |  | SI | Cosmetic Flag |
| PAMRDIA_DRGOrder | varchar |  |  | SI | DRG Order |
| PAMRDIA_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| PAMRDIA_DaggerAster | varchar |  |  | SI | Dagger Aster |
| PAMRDIA_Date | date |  |  | SI | Date |
| PAMRDIA_DateDetect | date |  |  | SI | Date Detected |
| PAMRDIA_DateDiagnosisIdentif | date |  |  | SI | DateDiagnosisIdentified |
| PAMRDIA_DeletionReason_DR | bigint |  | FK | SI | Des Ref DeletionReason |
| PAMRDIA_Desc | varchar |  |  | SI | Description |
| PAMRDIA_DiagStat_DR | bigint |  | FK | SI | Des Ref to MRC_DiagStat |
| PAMRDIA_DiagnosisGroup1_DR | bigint |  | FK | SI | Des Ref DiagnosisGroup1 |
| PAMRDIA_DiagnosisGroup2_DR | bigint |  | FK | SI | Des Ref DiagnosisGroup2 |
| PAMRDIA_DiagnosisID | varchar |  |  | SI | Diagnosis ID - Used in web.Msg.MRDiagnos |
| PAMRDIA_DiagnosisType_DR | bigint |  | FK | SI | Diagnosis Type - Used in web.Msg.MRDiagnos |
| PAMRDIA_DistalMet_DR | bigint |  | FK | SI | Des REf DistalMet |
| PAMRDIA_DocCode_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| PAMRDIA_DurationNum | varchar |  |  | SI | DurationNum |
| PAMRDIA_DurationUnit | varchar |  |  | SI | DurationUnit |
| PAMRDIA_EndDate | date |  |  | SI | EndDate |
| PAMRDIA_EndTime | time |  |  | SI | EndTime |
| PAMRDIA_EnteredAs | varchar |  |  | SI | Entered As - if Terminology link was used |
| PAMRDIA_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| PAMRDIA_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| PAMRDIA_ExcludeFromClaim | varchar |  |  | SI | Exclude from Claim |
| PAMRDIA_ExternalId | varchar |  |  | SI | A reference to external systems |
| PAMRDIA_FirstInset | varchar |  |  | SI | First Inset |
| PAMRDIA_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| PAMRDIA_ICDStatus_DR | bigint |  | FK | SI | Des Ref to MRCIS |
| PAMRDIA_ICDSup_DR | bigint |  | FK | SI | Des Ref to MRCSI |
| PAMRDIA_InsType_DR | bigint |  | FK | SI | Des Ref to InsType |
| PAMRDIA_IsActive | varchar |  |  | SI | Active CALCULATED Property - used for more conplex... |
| PAMRDIA_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| PAMRDIA_LinkedExternalId | varchar |  |  | SI | External Id of the linked diagnosis
Used by Healt... |
| PAMRDIA_LymphInvas_DR | bigint |  | FK | SI | Des Ref LymphInvas |
| PAMRDIA_LymphNode_DR | bigint |  | FK | SI | Des Ref LymphNode |
| PAMRDIA_MRDIA_DR | bigint |  | FK | SI | Des Ref PAMRDIA |
| PAMRDIA_MalGrade_DR | bigint |  | FK | SI | Des Ref MalGrade |
| PAMRDIA_MappedICD_DR | bigint |  | FK | SI | Des Ref MappedICD |
| PAMRDIA_ORAnaOp_DR | varchar |  | FK | SI | Des Ref to ORAnaestOperation |
| PAMRDIA_OnsetDate | date |  |  | SI | OnsetDate |
| PAMRDIA_OnsetTime | time |  |  | SI | OnsetTime |
| PAMRDIA_OriginalDiagnos_DR | bigint |  | FK | SI | Des Ref to PAPAMRDIAgnosSnapshot |
| PAMRDIA_PayByResult | varchar |  |  | SI | Payment By Result |
| PAMRDIA_Prefix | varchar |  |  | SI | Prefix |
| PAMRDIA_PresentOnAdmission_DR | bigint |  | FK | SI | Des Ref to PACPresentOnAdmission |
| PAMRDIA_PrimaryTumourSite_DR | bigint |  | FK | SI | Des Ref PrimaryTumourSite |
| PAMRDIA_Principle | varchar |  |  | SI | Principle |
| PAMRDIA_Questionnaire | varchar |  |  | SI | Questionnaire |
| PAMRDIA_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref - Reason For Correction |
| PAMRDIA_ResTum_DR | bigint |  | FK | SI | Des Ref ResTum_DR |
| PAMRDIA_RiskEvaluation_DR | varchar |  | FK | SI | Des Ref RiskEvaluation |
| PAMRDIA_Severity_DR | bigint |  | FK | SI | Des Ref Severity |
| PAMRDIA_SignSym_DR | bigint |  | FK | SI | Des Ref SignSym |
| PAMRDIA_SnapshotDate | date |  |  | SI | Create Date |
| PAMRDIA_SnapshotTime | time |  |  | SI | Create Time |
| PAMRDIA_SnapshotUser_DR | bigint |  | FK | SI | Des Ref SSUSR |
| PAMRDIA_StageClas_DR | bigint |  | FK | SI | Des Ref StageClas |
| PAMRDIA_Stages_DR | bigint |  | FK | SI | Des Ref Stages_DR |
| PAMRDIA_Suspicion | varchar |  |  | SI | Suspicion |
| PAMRDIA_TerminologyCode | varchar |  |  | SI | Code - if Terminology link was used (e.g. ECDS Cod... |
| PAMRDIA_TerminologyDesc | varchar |  |  | SI | Description - if Terminology link was used (e.g. E... |
| PAMRDIA_TerminologySelected | varchar |  |  | SI | Selected Description - if Diagnose Terminology lin... |
| PAMRDIA_Time | time |  |  | SI | Time |
| PAMRDIA_TimeDiagnosisIdentif | time |  |  | SI | TimeDiagnosisIdentif |
| PAMRDIA_TumourNotes | varchar |  |  | SI | TumourNotes |
| PAMRDIA_TumourSize | varchar |  |  | SI | TumourSize |
| PAMRDIA_TumourUpdateDate | date |  |  | SI | TumourUpdateDate |
| PAMRDIA_TumourUpdateHospitalDR | bigint |  | FK | SI | Des Ref TumourUpdateHospitalDR |
| PAMRDIA_TumourUpdateTime | time |  |  | SI | TumourUpdateTime |
| PAMRDIA_TumourUpdateUser_DR | bigint |  | FK | SI | Des Ref TumourUpdateUser |
| PAMRDIA_Tumour_DR | bigint |  | FK | SI | Des Ref Tumour |
| PAMRDIA_UpdateDate | date |  |  | SI | UpdateDate |
| PAMRDIA_UpdateHospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| PAMRDIA_UpdateTime | time |  |  | SI | UpdateTime |
| PAMRDIA_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| PAMRDIA_UserCreated_DR | bigint |  | FK | SI | Des Ref UserCreated |
| PAMRDIA_VenInvasion_DR | bigint |  | FK | SI | Des Ref VenInvasion |
| PAMRDIA_WorkRelated | varchar |  |  | SI | Work Related |
| Q55Q1 | - |  |  | SI | Activity |
| Q55Q2 | - |  |  | SI | Change |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*