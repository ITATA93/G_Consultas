# web_Msg.MR_Diagnos

**Schema:** web_Msg
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Diagnósticos**. Códigos CIE-10 asociados al episodio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| MRDIA_AccidentDate | varchar |  |  | SI | AccidentDate |
| MRDIA_Active | varchar |  |  | SI | Active |
| MRDIA_AdditionalDignosis | varchar |  |  | SI | AdditionalDignosis |
| MRDIA_AdminCategory_DR | bigint |  | FK | SI | Des Ref AccountClass |
| MRDIA_AliasDiagText | varchar |  |  | SI | AliasDiagText |
| MRDIA_Approximate | varchar |  |  | SI | Approximate |
| MRDIA_AutoAssignedFlg | varchar |  |  | SI | Auto Assigned Flag |
| MRDIA_AuxInsType_DR | bigint |  | FK | SI | Des Ref to AuxInsType |
| MRDIA_BodySite_DR | bigint |  | FK | SI | Des Ref BodySite |
| MRDIA_Childsub | numeric |  |  | SI | MRDIA_Childsub
Required by User.MRDiagnos. |
| MRDIA_CommReportedDate | date |  |  | SI | Commissioning Reported Date |
| MRDIA_ComorbidCode | varchar |  |  | SI | Code - if Comorbid Condition Terminology link was ... |
| MRDIA_ComorbidDesc | varchar |  |  | SI | Description - if Comorbid Condition Terminology li... |
| MRDIA_ComorbidSelected | varchar |  |  | SI | Selected Description - if Comorbid Condition Termi... |
| MRDIA_ConditionAdmission_DR | bigint |  | FK | SI | Des Ref to MRCConditionAdmission |
| MRDIA_Consult_DR | varchar |  | FK | SI | Des Ref Consult |
| MRDIA_ContractFlag_DR | bigint |  | FK | SI | Des Ref ContractFlag |
| MRDIA_CopyToEpisode_DR | bigint |  | FK | SI | Des Ref to PAAdm - Copied To Linked Episode |
| MRDIA_CopyToHistory | varchar |  |  | SI | Copy To History - Used in web.Msg.MRDiagnos |
| MRDIA_Cosmetic | varchar |  |  | SI | Cosmetic Flag |
| MRDIA_DRGOrder | varchar |  |  | SI | DRG Order |
| MRDIA_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| MRDIA_DaggerAster | varchar |  |  | SI | Dagger Aster |
| MRDIA_Date | date |  |  | SI | Date |
| MRDIA_DateDetect | date |  |  | SI | Date Detected |
| MRDIA_DateDiagnosisIdentif | date |  |  | SI | DateDiagnosisIdentified |
| MRDIA_DeletionReason_DR | bigint |  | FK | SI | Des Ref DeletionReason |
| MRDIA_DiagStat_DR | bigint |  | FK | SI | Des Ref to MRC_DiagStat |
| MRDIA_DiagnosisGroup1_DR | bigint |  | FK | SI | Des Ref DiagnosisGroup1 |
| MRDIA_DiagnosisGroup2_DR | bigint |  | FK | SI | Des Ref DiagnosisGroup2 |
| MRDIA_DiagnosisID | varchar |  |  | SI | Diagnosis ID - Used in web.Msg.MRDiagnos |
| MRDIA_DiagnosisType_DR | bigint |  | FK | SI | Diagnosis Type - Used in web.Msg.MRDiagnos |
| MRDIA_DistalMet_DR | bigint |  | FK | SI | Des REf DistalMet |
| MRDIA_DocCode_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| MRDIA_DurationNum | varchar |  |  | SI | DurationNum |
| MRDIA_DurationUnit | varchar |  |  | SI | DurationUnit |
| MRDIA_EndDate | date |  |  | SI | EndDate |
| MRDIA_EndTime | time |  |  | SI | EndTime |
| MRDIA_EnteredAs | varchar |  |  | SI | Entered As - if Terminology link was used |
| MRDIA_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| MRDIA_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| MRDIA_ExcludeFromClaim | varchar |  |  | SI | Exclude from Claim |
| MRDIA_ExtCauseDateOccurrence | date |  |  | SI | External Cause Date of Occurrence |
| MRDIA_ExternalId | varchar |  |  | SI | A reference to external systems |
| MRDIA_FirstInset | varchar |  |  | SI | First Inset |
| MRDIA_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| MRDIA_ICDStatus_DR | bigint |  | FK | SI | Des Ref to MRCIS |
| MRDIA_ICDSup_DR | bigint |  | FK | SI | Des Ref to MRCSI |
| MRDIA_InsType_DR | bigint |  | FK | SI | Des Ref to InsType |
| MRDIA_IsActive | varchar |  |  | SI | Active CALCULATED Property - used for more conplex... |
| MRDIA_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| MRDIA_LinkedExternalId | varchar |  |  | SI | External Id of the linked diagnosis
Used by Healt... |
| MRDIA_LymphInvas_DR | bigint |  | FK | SI | Des Ref LymphInvas |
| MRDIA_LymphNode_DR | bigint |  | FK | SI | Des Ref LymphNode |
| MRDIA_MRADM_ParRef | bigint |  |  | SI | MR_AdmLink Parent Reference
Required by User.MRDi... |
| MRDIA_MRDIA_DR | varchar |  | FK | SI | Des Ref MRDIA |
| MRDIA_MalGrade_DR | bigint |  | FK | SI | Des Ref MalGrade |
| MRDIA_MappedICD_DR | bigint |  | FK | SI | Des Ref MappedICD |
| MRDIA_ORAnaOp_DR | varchar |  | FK | SI | Des Ref to ORAnaestOperation |
| MRDIA_OnsetDate | date |  |  | SI | OnsetDate |
| MRDIA_OnsetTime | time |  |  | SI | OnsetTime |
| MRDIA_OriginalDiagnos_DR | varchar |  | FK | SI | Des Ref to MRDiagnos |
| MRDIA_PayByResult | varchar |  |  | SI | Payment By Result |
| MRDIA_Prefix | varchar |  |  | SI | Prefix |
| MRDIA_PresentOnAdmission_DR | bigint |  | FK | SI | Des Ref to PACPresentOnAdmission |
| MRDIA_PrimaryTumourSite_DR | bigint |  | FK | SI | Des Ref PrimaryTumourSite |
| MRDIA_Principle | varchar |  |  | SI | Principle |
| MRDIA_Questionnaire | varchar |  |  | SI | Questionnaire |
| MRDIA_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref - Reason For Correction |
| MRDIA_ResTum_DR | bigint |  | FK | SI | Des Ref ResTum_DR |
| MRDIA_RiskEvaluation_DR | varchar |  | FK | SI | Des Ref RiskEvaluation |
| MRDIA_RowId | varchar |  |  | SI | - |
| MRDIA_Severity_DR | bigint |  | FK | SI | Des Ref Severity |
| MRDIA_SignSym_DR | bigint |  | FK | SI | Des Ref SignSym |
| MRDIA_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| MRDIA_StageClas_DR | bigint |  | FK | SI | Des Ref StageClas |
| MRDIA_Stages_DR | bigint |  | FK | SI | Des Ref Stages_DR |
| MRDIA_Suspicion | varchar |  |  | SI | Suspicion |
| MRDIA_TerminologyCode | varchar |  |  | SI | Code - if Terminology link was used (e.g. ECDS Cod... |
| MRDIA_TerminologyDesc | varchar |  |  | SI | Description - if Terminology link was used (e.g. E... |
| MRDIA_TerminologySelected | varchar |  |  | SI | Selected Description - if Diagnose Terminology lin... |
| MRDIA_Time | time |  |  | SI | Time |
| MRDIA_TimeDiagnosisIdentif | time |  |  | SI | TimeDiagnosisIdentif |
| MRDIA_TumourSize | varchar |  |  | SI | TumourSize |
| MRDIA_TumourUpdateDate | date |  |  | SI | TumourUpdateDate |
| MRDIA_TumourUpdateHospitalDR | bigint |  | FK | SI | Des Ref TumourUpdateHospitalDR |
| MRDIA_TumourUpdateTime | time |  |  | SI | TumourUpdateTime |
| MRDIA_TumourUpdateUser_DR | bigint |  | FK | SI | Des Ref TumourUpdateUser |
| MRDIA_Tumour_DR | bigint |  | FK | SI | Des Ref Tumour |
| MRDIA_UpdateDate | date |  |  | SI | UpdateDate |
| MRDIA_UpdateHospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| MRDIA_UpdateTime | time |  |  | SI | UpdateTime |
| MRDIA_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| MRDIA_UserCreated_DR | bigint |  | FK | SI | Des Ref UserCreated |
| MRDIA_VenInvasion_DR | bigint |  | FK | SI | Des Ref VenInvasion |
| MRDIA_WorkRelated | varchar |  |  | SI | Work Related |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*