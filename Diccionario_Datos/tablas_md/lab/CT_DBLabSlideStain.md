# lab.CT_DBLabSlideStain

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDBS_ParRef | varchar | PK |  | NO | CT_DayBookLaboratory Parent Reference |
| CTDBS_ActiveFlag | varchar |  |  | SI | Active |
| CTDBS_BillingItem_DR | varchar |  | FK | SI | Billing Item DR |
| CTDBS_Code | varchar |  |  | NO | Code |
| CTDBS_Desc | varchar |  |  | SI | Description |
| CTDBS_PrintLabels | varchar |  |  | SI | Print Labels |
| CTDBS_RowId | varchar |  |  | NO | - |
| CTDBS_Welcan_Minute | varchar |  |  | SI | Minute Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*