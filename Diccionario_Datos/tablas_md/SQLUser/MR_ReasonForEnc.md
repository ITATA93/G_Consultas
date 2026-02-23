# SQLUser.MR_ReasonForEnc

**Schema:** SQLUser
**Columnas:** 41
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REAENC_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| ChildQ35DR | - |  |  | SI | Child Reference: Administration Record: |
| Q33Q1 | - |  |  | SI | BG (mmol/L): |
| Q33Q2 | - |  |  | SI | BG (mg/dL): |
| Q33Q3 | - |  |  | SI | Dose (Units): |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REAENC_Childsub | double |  |  | NO | Childsub |
| REAENC_Comment | varchar |  |  | SI | Comment |
| REAENC_CreateDate | date |  |  | SI | CreateDate |
| REAENC_CreateTime | time |  |  | SI | CreateTime |
| REAENC_Deleted | varchar |  |  | SI | Deleted |
| REAENC_Encounter_DR | bigint |  | FK | SI | MREncounter Reference |
| REAENC_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| REAENC_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| REAENC_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| REAENC_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| REAENC_Laterality | varchar |  |  | SI | Laterality |
| REAENC_MainRFE | varchar |  |  | SI | MainRFE |
| REAENC_MasterVersion_DR | varchar |  | FK | SI | Des Ref MRReasonForEnc |
| REAENC_OnsetCalcDateAge | integer |  |  | SI | Calculated date "at the age of" |
| REAENC_OnsetCalcDateAgeUnit | varchar |  |  | SI | Calculated date units "at the age of [num] [unit]  |
| REAENC_OnsetCalcDateAgo | varchar |  |  | SI | Calculated date ago or from "[num] [unit] ago on/f... |
| REAENC_OnsetCalcDateAgoNum | integer |  |  | SI | Calculated date number of units "[num] [unit] ago ... |
| REAENC_OnsetCalcDateAgoUnit | varchar |  |  | SI | Calculated date units "[num] [unit] ago/from" |
| REAENC_OnsetCalcDateBase | date |  |  | SI | date calculated date is based on |
| REAENC_OnsetDate | date |  |  | SI | OnsetDate |
| REAENC_OnsetTime | time |  |  | SI | OnsetTime |
| REAENC_ReasonForChange | varchar |  |  | SI | ReasonForChange |
| REAENC_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref Reason For Correction |
| REAENC_RefinedSiteSCTIDs | varchar |  |  | SI | RefinedSiteSCTIDs |
| REAENC_RowId | varchar |  |  | NO | - |
| REAENC_SeveritySnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| REAENC_Severity_DR | bigint |  | FK | SI | Des Ref MRCSeverity |
| REAENC_SiteSnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| REAENC_SiteText | varchar |  |  | SI | SiteText |
| REAENC_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| REAENC_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| REAENC_UpdateDate | date |  |  | SI | UpdateDate |
| REAENC_UpdateTime | time |  |  | SI | UpdateTime |
| REAENC_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| REAENC_VersionReason | varchar |  |  | SI | VersionReason |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*