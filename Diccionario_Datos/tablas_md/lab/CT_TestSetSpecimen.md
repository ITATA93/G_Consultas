# lab.CT_TestSetSpecimen

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSS_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSS_DefaultCode | varchar |  |  | SI | Default Code |
| CTTSS_RowId | varchar |  |  | NO | - |
| CTTSS_Specimen_DR | varchar |  | FK | NO | Des Ref Specimen |
| CTTSS_xxx | varchar |  |  | SI | Containers |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*