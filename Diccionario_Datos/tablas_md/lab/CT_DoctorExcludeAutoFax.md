# lab.CT_DoctorExcludeAutoFax

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDRC_ParRef | varchar | PK |  | NO | CT_Doctor Parent Reference |
| CTDRC_RowId | varchar |  |  | NO | - |
| CTDRC_TestSet_DR | varchar |  | FK | NO | Test Set |
| CTDRC_xxx | varchar |  |  | SI | Exclude Auto Fax |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*