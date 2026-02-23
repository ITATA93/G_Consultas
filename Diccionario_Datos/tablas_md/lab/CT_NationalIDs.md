# lab.CT_NationalIDs

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTNI_RowID | varchar | PK |  | NO | - |
| CTNI_Code | varchar |  |  | NO | Code |
| CTNI_Description | varchar |  |  | SI | Description |
| CTNI_PatternOrFunction | varchar |  |  | SI | Pattern or Function |
| CTNI_UpdateFlag | varchar |  |  | SI | Update Flag (For use by custom scripts) |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*