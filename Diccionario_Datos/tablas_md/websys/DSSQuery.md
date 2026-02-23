# websys.DSSQuery

**Schema:** websys
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ClassName | varchar |  |  | SI | - |
| Code | varchar |  |  | SI | - |
| ColUnit | varchar |  |  | SI | Column Measurement Unit
i.e DAY,MONTH,YEAR |
| ColumnRuleDR | bigint |  | FK | SI | - |
| Description | varchar |  |  | SI | - |
| IndexClassName | varchar |  |  | SI | - |
| QueryText | varchar |  |  | SI | - |
| QueryValue | varchar |  |  | SI | - |
| RowFilter | varchar |  |  | SI | - |
| RowRuleDR | bigint |  | FK | SI | - |
| RowUnit | varchar |  |  | SI | Row Measurement Unit
i.e DAY,MONTH,YEAR |
| RowsPerPage | integer |  |  | SI | - |
| ViewDR | bigint |  | FK | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*