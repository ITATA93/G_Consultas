# websys.ReportCSVColumn

> Report CSV extract column definition

**Schema:** websys
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Report CSV extract column definition

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | Reference to parent CSV report |
| ColumnName | varchar |  |  | SI | Name of the column according the query |
| DateFrom | date |  |  | SI | Date From column is active. CSV only extract activ... |
| DateTo | date |  |  | SI | Date To column is active. CSV only extract active ... |
| Description | varchar |  |  | SI | Description of the column for CSV extract |
| ID | varchar |  |  | NO | - |
| Sequence | integer |  |  | SI | Sequence of column in CSV . Columns with empty seq... |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*