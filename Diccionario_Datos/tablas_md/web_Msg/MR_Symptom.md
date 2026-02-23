# web_Msg.MR_Symptom

**Schema:** web_Msg
**Columnas:** 32
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SYM_Childsub | double |  |  | SI | Childsub |
| SYM_CreateDate | date |  |  | SI | CreateDate |
| SYM_CreateTime | time |  |  | SI | CreateTime |
| SYM_Deleted | varchar |  |  | SI | Deleted |
| SYM_Exists | bit |  |  | SI | SYMExists |
| SYM_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| SYM_ICPCCode_DR | bigint |  | FK | SI | Des Ref to MRCICPC2 |
| SYM_Laterality | varchar |  |  | SI | Laterality |
| SYM_MasterVersion_DR | varchar |  | FK | SI | Des Ref MRSymptom |
| SYM_NoSymptomOf | bit |  |  | SI | NoSymptomOf |
| SYM_OnsetDate | date |  |  | SI | OnsetDate |
| SYM_OnsetTime | time |  |  | SI | OnsetTime |
| SYM_ParRef | bigint |  |  | SI | MR_Adm Parent Reference
Required by User.MRSympto... |
| SYM_ROSSystem_DR | varchar |  | FK | SI | Des Ref MRCROSSystem
only used when symptom part ... |
| SYM_RefinedSiteSCTIDs | varchar |  |  | SI | RefinedSiteSCTIDs |
| SYM_ReviewOfSystems_DR | varchar |  | FK | SI | Des Ref MRReviewOfSystems
only used when symptom ... |
| SYM_RowId | varchar |  |  | SI | - |
| SYM_SeveritySnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| SYM_Severity_DR | bigint |  | FK | SI | Des Ref MRCSeverity |
| SYM_SiteSnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| SYM_SiteText | varchar |  |  | SI | SiteText |
| SYM_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| SYM_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| SYM_UpdateDate | date |  |  | SI | UpdateDate |
| SYM_UpdateTime | time |  |  | SI | UpdateTime |
| SYM_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*