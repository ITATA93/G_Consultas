# lab.CT_HealthFundNumber

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTHFN_ParRef | varchar | PK |  | NO | CT_HealthFund Parent Reference |
| CTHFN_EndDate | date |  |  | SI | End Date |
| CTHFN_PatternOrFunction | varchar |  |  | SI | Pattern or Function |
| CTHFN_RowID | varchar |  |  | NO | - |
| CTHFN_Sequence | varchar |  |  | NO | Sequence |
| CTHFN_StartDate | date |  |  | SI | Start Date |
| CTHFN_Tooltip | varchar |  |  | SI | Tooltip |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*