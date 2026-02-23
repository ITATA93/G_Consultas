# SQLUser.PA_Family

**Schema:** SQLUser
**Columnas:** 41
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FAM_PAPMI_ParRef | bigint | PK |  | NO | Des Ref to PAPMI |
| FAM_ApproxOnsetDate | varchar |  |  | SI | ApproxOnsetDate |
| FAM_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| FAM_ChildSub | double |  |  | NO | Family Childsub |
| FAM_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| FAM_Date | date |  |  | SI | Date |
| FAM_Desc | varchar |  |  | SI | Description |
| FAM_DuratDays | double |  |  | SI | Duration in Days |
| FAM_DuratMonth | double |  |  | SI | Duration in Month |
| FAM_DuratYear | double |  |  | SI | Duration in Year |
| FAM_Duration | varchar |  |  | SI | Duration |
| FAM_DurationDesc | varchar |  |  | SI | DurationDesc |
| FAM_EndDate | date |  |  | SI | EndDate |
| FAM_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| FAM_ExternalID | varchar |  |  | SI | ExternalID |
| FAM_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| FAM_InActive | varchar |  |  | SI | InActive |
| FAM_MRCBodSysProbSub_DR | varchar |  | FK | SI | MRCBodSysProbSub |
| FAM_MRCBodySysProb_DR | varchar |  | FK | SI | Des Ref MRCBodySysProb |
| FAM_MRCBodySys_DR | bigint |  | FK | SI | Des Ref MRCBodySys |
| FAM_MRCICD_DR | bigint |  | FK | SI | Des Ref to MRCICDDx |
| FAM_NoHistoryOf | varchar |  |  | SI | NoHistoryOf |
| FAM_OnsetDate | date |  |  | SI | Onset Date |
| FAM_PAPER_DR | bigint |  | FK | SI | Des Ref to PAPER |
| FAM_RcFlag | varchar |  |  | SI | Archived Flag |
| FAM_Relation_DR | bigint |  | FK | SI | Des Ref to CTRLT |
| FAM_RowId | varchar |  |  | NO | - |
| FAM_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| FAM_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| FAM_Time | time |  |  | SI | Time |
| FAM_UpdateDate | date |  |  | SI | UpdateDate |
| FAM_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| FAM_UpdateTime | time |  |  | SI | UpdateTime |
| FAM_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| Q26Q1 | - |  |  | SI | Date |
| Q26Q2 | - |  |  | SI | Time |
| Q26Q3 | - |  |  | SI | Peristomal skin care and stoma products |
| Q26Q4 | - |  |  | SI | Education provided to patient |
| Q26Q5 | - |  |  | SI | Notes |
| Q26Q6 | - |  |  | SI | Care provider |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*