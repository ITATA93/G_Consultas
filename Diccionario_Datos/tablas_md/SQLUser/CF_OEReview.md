# SQLUser.CF_OEReview

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEREV_RowId | bigint | PK |  | NO | - |
| ChildQ81DR | - |  |  | SI | Child Reference: Programa de Salud MEUI |
| OEREV_AlertDueColor | varchar |  |  | SI | AlertDueColor  |
| OEREV_AlertDueTimeUnit | varchar |  |  | SI | AlertDueTimeUnit |
| OEREV_AlertDueTimeValue | double |  |  | SI | AlertDueTimeValue  |
| OEREV_DateFrom | date |  |  | SI | DateFrom |
| OEREV_DateTo | date |  |  | SI | DateTo |
| OEREV_EpisodeType | varchar |  |  | SI | EpisodeType |
| OEREV_ExDisPriority | varchar |  |  | SI | Exclude Discharge Priority |
| OEREV_GenFreqUnit | varchar |  |  | SI | GenFreqUnit |
| OEREV_GenFreqValue | double |  |  | SI | GenFreqValue  |
| OEREV_GenerationTime | time |  |  | SI | GenerationTime  |
| OEREV_OffsetTimeUnit | varchar |  |  | SI | OffsetTimeUnit |
| OEREV_OffsetTimeValue | double |  |  | SI | OffsetTimeValue  |
| OEREV_OverlapPeriodUnit | varchar |  |  | SI | OverlapPeriondUnit |
| OEREV_OverlapPeriodValue | double |  |  | SI | OverlapPeriondValue  |
| Q73Q1 | - |  |  | SI | Programa / Actividad |
| Q73Q2 | - |  |  | SI | Tipo Consulta |
| Q73Q3 | - |  |  | SI | ID Consultation |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*