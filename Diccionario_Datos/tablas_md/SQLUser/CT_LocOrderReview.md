# SQLUser.CT_LocOrderReview

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEREV_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| OEREV_AlertDueColor | varchar |  |  | SI | AlertDueColor  |
| OEREV_AlertDueTimeUnit | varchar |  |  | SI | AlertDueTimeUnit |
| OEREV_AlertDueTimeValue | double |  |  | SI | AlertDueTimeValue  |
| OEREV_Childsub | double |  |  | NO | Childsub |
| OEREV_CreatedDate | date |  |  | SI | Created Date |
| OEREV_CreatedTime | time |  |  | SI | Created Time |
| OEREV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OEREV_DateFrom | date |  |  | SI | DateFrom |
| OEREV_DateTo | date |  |  | SI | DateTo |
| OEREV_EpisodeType | varchar |  |  | SI | EpisodeType |
| OEREV_GenFreqUnit | varchar |  |  | SI | GenFreqUnit |
| OEREV_GenFreqValue | double |  |  | SI | GenFreqValue  |
| OEREV_GenerationTime | time |  |  | SI | GenerationTime  |
| OEREV_OffsetTimeUnit | varchar |  |  | SI | OffsetTimeUnit |
| OEREV_OffsetTimeValue | double |  |  | SI | OffsetTimeValue  |
| OEREV_OverlapPeriodUnit | varchar |  |  | SI | OverlapPeriondUnit |
| OEREV_OverlapPeriodValue | double |  |  | SI | OverlapPeriondValue  |
| OEREV_RowId | varchar |  |  | NO | - |
| OEREV_UpdatedDate | date |  |  | SI | Updated Date |
| OEREV_UpdatedTime | time |  |  | SI | Updated Time |
| OEREV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q88Q1 | - |  |  | SI | Time |
| Q88Q2 | - |  |  | SI | mm/Hg |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*