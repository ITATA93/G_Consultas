# SQLUser.PA_PastHistCondition

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHIST_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| PHIST_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| PHIST_Childsub | double |  |  | NO | Childsub |
| PHIST_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| PHIST_Date | date |  |  | SI | Date |
| PHIST_Desc | varchar |  |  | SI | Description |
| PHIST_DuratDays | double |  |  | SI | Duration in Days |
| PHIST_DuratMonth | double |  |  | SI | Duration in Month |
| PHIST_DuratYear | double |  |  | SI | Duration in Year |
| PHIST_EndDate | date |  |  | SI | EndDate |
| PHIST_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| PHIST_ExternalId | varchar |  |  | SI | A reference to external systems |
| PHIST_InActive | varchar |  |  | SI | InActive |
| PHIST_OnsetDate | date |  |  | SI | Onset Date |
| PHIST_PastHistCateg_DR | varchar |  | FK | SI | Des Ref PastHistConCateg |
| PHIST_PastHist_DR | bigint |  | FK | SI | Des Ref PastHist |
| PHIST_RowId | varchar |  |  | NO | - |
| PHIST_Time | time |  |  | SI | Time |
| PHIST_UpdateDate | date |  |  | SI | UpdateDate |
| PHIST_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| PHIST_UpdateTime | time |  |  | SI | UpdateTime |
| PHIST_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| PHIST_VerifiedDate | date |  |  | SI | Verified Date |
| PHIST_VerifiedTime | time |  |  | SI | Verified Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*