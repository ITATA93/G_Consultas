# lab.CT_SpeciesTranslation

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Especialidades**. Especialidades médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSPT_ParRef | varchar | PK |  | NO | CT_Species Parent Reference |
| CTSPT_Description | varchar |  |  | SI | Description |
| CTSPT_Language_DR | bigint |  | FK | NO | Language DR |
| CTSPT_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*