# lab.CT_SpecimenLabBlock

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Especialidades**. Especialidades médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSPB_ParRef | varchar | PK |  | NO | CT_SpecimenLab Parent Reference |
| CTSPB_AnatomicalSite_DR | varchar |  | FK | SI | Anatomical Site DR |
| CTSPB_BlockCode | varchar |  |  | SI | Block Code |
| CTSPB_Description | varchar |  |  | SI | Block description |
| CTSPB_Order | varchar |  |  | NO | Order number |
| CTSPB_RowId | varchar |  |  | NO | - |
| CTSPB_Sequence | double |  |  | SI | Sequence |
| CTSPB_TestSet_DR | varchar |  | FK | SI | Test Set DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*