# websys.MonitorQuickSQLText

> "contains the text of SQL queries to avoid duplication large fields

**Schema:** websys
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "contains the text of SQL queries to avoid duplication large fields

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Hash | varchar |  |  | NO | Hash of query text |
| LastUsed | date |  |  | SI | the most recent day this query has been seen |
| QueryText | varchar |  |  | SI | query text for hash |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*