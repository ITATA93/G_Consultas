# lab.CT_StorageContainers

**Schema:** lab
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSTC_RowId | varchar | PK |  | NO | - |
| CTSTC_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTSTC_AlphaColumns | varchar |  |  | SI | Alpha Columns |
| CTSTC_AlphaRows | varchar |  |  | SI | Alpha Rows |
| CTSTC_AutoPurge | varchar |  |  | SI | Auto Purge |
| CTSTC_Code | varchar |  |  | NO | Code |
| CTSTC_ColumnWidth | double |  |  | SI | Column width |
| CTSTC_Columns | double |  |  | SI | Columns |
| CTSTC_Description | varchar |  |  | SI | Description |
| CTSTC_FrozenBT | varchar |  |  | SI | Frozen BT |
| CTSTC_LongTerm | varchar |  |  | SI | Long Term |
| CTSTC_NumberOfPositions | double |  |  | SI | Number Of Positions |
| CTSTC_RefreshTime | double |  |  | SI | Refresh Time |
| CTSTC_Rows | double |  |  | SI | Rows |
| CTSTC_Specimen_DR | varchar |  | FK | SI | Specimen DR |
| CTSTC_StorageTime | double |  |  | SI | Storage Time (days) |
| CTSTC_StorageTimeCalc | varchar |  |  | SI | Storage Time Calculation |
| CTSTC_UserSite_DR | varchar |  | FK | SI | User Site DR |
| CTSTC_Warnings | varchar |  |  | SI | Warnings |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*