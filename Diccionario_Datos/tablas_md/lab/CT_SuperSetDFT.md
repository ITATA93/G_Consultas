# lab.CT_SuperSetDFT

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSSD_ParRef | varchar | PK |  | NO | CT_SuperSet Parent Reference |
| CTSSD_RowID | varchar |  |  | NO | - |
| CTSSD_SamplePrefix | varchar |  |  | SI | Sample Prefix |
| CTSSD_SampleSuffix | varchar |  |  | SI | Sample Suffix |
| CTSSD_Sequence | double |  |  | NO | Sequence |
| CTSSD_TestSet_DR | varchar |  | FK | SI | Test Set DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*