# lab.CT_SpecimenTranslation

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Especialidades**. Especialidades médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSPF_ParRef | varchar | PK |  | NO | CT_Specimen Parent Reference |
| CTSPF_Description | varchar |  |  | SI | Description |
| CTSPF_Language_DR | bigint |  | FK | NO | Language DR |
| CTSPF_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*