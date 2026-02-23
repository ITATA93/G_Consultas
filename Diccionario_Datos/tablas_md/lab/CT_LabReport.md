# lab.CT_LabReport

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLR_RowID | varchar | PK |  | NO | - |
| CTLR_Code | varchar |  |  | NO | Code |
| CTLR_DBLaboratory_DR | varchar |  | FK | SI | DB Laboratory DR |
| CTLR_Description | varchar |  |  | SI | Description |
| CTLR_LastDate | date |  |  | SI | Last Date |
| CTLR_ReportType | varchar |  |  | SI | Report Type |
| CTLR_UserTestItem_DR | varchar |  | FK | SI | User Test Item DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*