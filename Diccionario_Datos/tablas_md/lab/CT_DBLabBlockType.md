# lab.CT_DBLabBlockType

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDBA_ParRef | varchar | PK |  | NO | CT_DayBookLaboratory Parent Reference |
| CTDBA_Code | varchar |  |  | NO | Code |
| CTDBA_Desc | varchar |  |  | SI | Description |
| CTDBA_RowId | varchar |  |  | NO | - |
| CTDBA_Welcan_Minute | varchar |  |  | SI | Minute Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*