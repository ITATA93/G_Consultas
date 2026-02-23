# lab.CT_ICD10Group

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTICDG_RowID | varchar | PK |  | NO | - |
| CTICDG_Code | varchar |  |  | NO | Code |
| CTICDG_Description | varchar |  |  | SI | Description |
| CTICDG_ICD10Chapter_DR | varchar |  | FK | SI | ICD10 Chapter DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*