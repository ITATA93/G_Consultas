# SQLUser.PA_Problem

**Schema:** SQLUser
**Columnas:** 55
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROB_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| PROB_AutoCreated | varchar |  |  | SI | Problem Autocreated from Pregnancy  |
| PROB_Childsub | double |  |  | NO | Childsub |
| PROB_Comment | varchar |  |  | SI | Comment |
| PROB_CreateDate | date |  |  | SI | CreateDate |
| PROB_CreateTime | time |  |  | SI | CreateTime |
| PROB_Deleted | varchar |  |  | SI | Deleted |
| PROB_EndCalcDateAge | integer |  |  | SI | Calculated date "at the age of" |
| PROB_EndCalcDateAgeUnit | varchar |  |  | SI | Calculated date units "[num] [unit] ago/from" |
| PROB_EndCalcDateAgo | varchar |  |  | SI | Calculated date ago or from "[num] [unit] ago on/f... |
| PROB_EndCalcDateAgoNum | integer |  |  | SI | Calculated date number of units "[num] [unit] ago ... |
| PROB_EndCalcDateAgoUnit | varchar |  |  | SI | Calculated date units "[num] [unit] ago/from" |
| PROB_EndCalcDateBase | date |  |  | SI | date calculated date is based on |
| PROB_EndDate | date |  |  | SI | EndDate |
| PROB_EndTime | time |  |  | SI | EndTime |
| PROB_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| PROB_ErrorReason_DR | bigint |  | FK | SI | Des Ref - Error Reason |
| PROB_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| PROB_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| PROB_Laterality | varchar |  |  | SI | Laterality |
| PROB_MainEpisDiagnos | varchar |  |  | SI | MainEpisDiagnos |
| PROB_MasterVersion_DR | varchar |  | FK | SI | Des Ref PAProblem |
| PROB_Morphological_DR | bigint |  | FK | SI | Des Ref to MRCID for Morphological Code |
| PROB_Morphological_Date | date |  |  | SI | Discovery Date for Morphological Code |
| PROB_NCPProb_DR | bigint |  | FK | SI | Nursing Care Plan Problem |
| PROB_NoHistory | varchar |  |  | SI | No Known History Of |
| PROB_OnsetCalcDateAge | integer |  |  | SI | Calculated date "at the age of" |
| PROB_OnsetCalcDateAgeUnit | varchar |  |  | SI | Calculated date units "at the age of [num] [unit]  |
| PROB_OnsetCalcDateAgo | varchar |  |  | SI | Calculated date ago or from "[num] [unit] ago on/f... |
| PROB_OnsetCalcDateAgoNum | integer |  |  | SI | Calculated date number of units "[num] [unit] ago ... |
| PROB_OnsetCalcDateAgoUnit | varchar |  |  | SI | Calculated date units "[num] [unit] ago/from" |
| PROB_OnsetCalcDateBase | date |  |  | SI | date calculated date is based on |
| PROB_OnsetDate | date |  |  | SI | OnsetDate |
| PROB_OnsetTime | time |  |  | SI | OnsetTime |
| PROB_Pregnancy_DR | bigint |  | FK | SI | Pregnancy  |
| PROB_ProvisionalDiagnos | varchar |  |  | SI | ProvisionalDiagnos |
| PROB_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref - Reason For Correction |
| PROB_RefinedSiteSCTIDs | varchar |  |  | SI | RefinedSiteSCTIDs |
| PROB_RespCareProv_DR | varchar |  | FK | SI | Des Ref Responsible Careprovider |
| PROB_RespLocation_DR | bigint |  | FK | SI | Des Ref Responsible "Specialty" |
| PROB_RowId | varchar |  |  | NO | - |
| PROB_SeveritySnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| PROB_Severity_DR | bigint |  | FK | SI | Des Ref MRCSeverity |
| PROB_SiteSnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| PROB_SiteText | varchar |  |  | SI | SiteText |
| PROB_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| PROB_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| PROB_TerminologyCode | varchar |  |  | SI | Problem Terminology - if Terminology link was used... |
| PROB_TerminologyDesc | varchar |  |  | SI | Problem Terminology Description - if Terminology l... |
| PROB_TerminologySelected | varchar |  |  | SI | Selected Description - if Problem Terminology link... |
| PROB_TimeLineArchived | varchar |  |  | SI | TimeLineArchived |
| PROB_UpdateDate | date |  |  | SI | UpdateDate |
| PROB_UpdateTime | time |  |  | SI | UpdateTime |
| PROB_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| PROB_VersionChange | varchar |  |  | SI | List of versionchanges
only used when t |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*