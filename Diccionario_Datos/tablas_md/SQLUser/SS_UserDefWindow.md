# SQLUser.SS_UserDefWindow

**Schema:** SQLUser
**Columnas:** 55
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WIN_RowId | bigint | PK |  | NO | - |
| WIN_APIFlag | varchar |  |  | SI | API Flag |
| WIN_Author_DR | bigint |  | FK | SI | Author Des Ref User |
| WIN_AuthorityText | varchar |  |  | SI | AuthorityText   |
| WIN_Authority_DR | bigint |  | FK | SI | Authority Des Ref User |
| WIN_Code | varchar |  |  | NO | Code  |
| WIN_CreateSecondSignature | varchar |  |  | SI | Create Second Signature |
| WIN_CreatedDate | date |  |  | SI | CreatedDate |
| WIN_CreatedTime | time |  |  | SI | CreatedTime |
| WIN_CumulViewCreationUser | varchar |  |  | SI | Cumulative View Creation User |
| WIN_CumulViewLastUpdateDate | varchar |  |  | SI | Cumulative View Last Update Date |
| WIN_CumulViewLastUpdateTime | varchar |  |  | SI | Cumulative View Last Update Time |
| WIN_CumulViewLastUpdateUser | varchar |  |  | SI | Cumulative View Last Update User |
| WIN_CumulViewReasonForCorrection | varchar |  |  | SI | Cumulative View Reason For Correction |
| WIN_CumulViewReasonForError | varchar |  |  | SI | Cumulative View Reason For Error |
| WIN_CumulViewScore | varchar |  |  | SI | Cumulative View Score |
| WIN_CumulViewStatus | varchar |  |  | SI | Cumulative View Status |
| WIN_DateFrom | date |  |  | SI | Date From |
| WIN_DateTo | date |  |  | SI | Date To |
| WIN_DaysOffsetForDefOfLastAns | double |  |  | SI | Days Offset For Default Of Last Answer |
| WIN_Deprecated | varchar |  |  | SI | Deprecated |
| WIN_Desc | varchar |  |  | NO | Description |
| WIN_DisplayTCUI | varchar |  |  | SI | Display in TrakCare UI frame |
| WIN_Document | varchar |  |  | SI | Document |
| WIN_EncSOAPICategory | varchar |  |  | SI | Encounter Record SOAPI Category |
| WIN_ExcludeAdvSOAPSecurity | varchar |  |  | SI | ExcludeAdvSOAPSecurity |
| WIN_GenerateDSCube | varchar |  |  | SI | Generate DeepSee Cube |
| WIN_GenerateError | varchar |  |  | SI | GenerateError |
| WIN_GenerateZENReport | varchar |  |  | SI | Generate ZEN Report |
| WIN_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| WIN_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| WIN_IgnoreRptFld | varchar |  |  | SI | Do not generate questionnaire class with T69 "CQ" ... |
| WIN_ImageRegularCount | varchar |  |  | SI | Number of  Regular Image Control Type |
| WIN_ImageTabularCount | varchar |  |  | SI | Number of  Tabular Image Control Type |
| WIN_Inactive | varchar |  |  | SI | [DEPRECATED]Functionality replaced by DateFrom and... |
| WIN_IndexNotUpToDate | varchar |  |  | SI | IndexNotUpToDate |
| WIN_LastGenDate | date |  |  | SI | LastGenDate |
| WIN_LastGenHospital_DR | bigint |  | FK | SI | Des Ref LastGenHospital |
| WIN_LastGenTime | time |  |  | SI | LastGenTime |
| WIN_LastGenUser_DR | bigint |  | FK | SI | Des Ref LastGenUser |
| WIN_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| WIN_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| WIN_LastUpdateUser_DR | bigint |  | FK | SI | LastUpdateUser |
| WIN_OldQuestionnaire | varchar |  |  | SI | OldQuestionnaire |
| WIN_OnlyDefAnsFromSameEp | varchar |  |  | SI | Only Default Answers From Same Episode  |
| WIN_Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| WIN_Purpose | varchar |  |  | SI | Purpose |
| WIN_ReasonDeprecated | varchar |  |  | SI | Deprecated Reason |
| WIN_ReviewDate | date |  |  | SI | ReviewDate |
| WIN_Score | varchar |  |  | SI | Score |
| WIN_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| WIN_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| WIN_UsedFlag | varchar |  |  | SI | UsedFlag |
| WIN_WebFlag | varchar |  |  | SI | WebFlag |
| WIN_WindowGroup_DR | bigint |  | FK | SI | [DEPRECATED]This property is replaced by the data ... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*