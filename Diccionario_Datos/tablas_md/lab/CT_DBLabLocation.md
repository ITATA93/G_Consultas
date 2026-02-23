# lab.CT_DBLabLocation

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDBLO_ParRef | varchar | PK |  | NO | CT_DayBookLaboratory Parent Reference |
| CTDBLO_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTDBLO_Code | varchar |  |  | NO | Code |
| CTDBLO_Desc | varchar |  |  | SI | Description |
| CTDBLO_External | varchar |  |  | SI | External Flag |
| CTDBLO_RowID | varchar |  |  | NO | - |
| CTDBLO_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*