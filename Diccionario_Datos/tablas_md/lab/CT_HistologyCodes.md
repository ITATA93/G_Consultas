# lab.CT_HistologyCodes

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTHIS_RowId | varchar | PK |  | NO | - |
| CTHIS_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTHIS_Code | varchar |  |  | NO | Code |
| CTHIS_Desc | varchar |  |  | SI | Description |
| CTHIS_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTHIS_Formatted | varchar |  |  | SI | Formatted |
| CTHIS_ReportCategory_DR | varchar |  | FK | SI | Report Category DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*