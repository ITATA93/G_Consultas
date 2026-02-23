# lab.DF_DynamicFunctionReqPos

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DFRP_ParRef | varchar | PK |  | NO | DF_DynamicFunctionRequest Parent Reference |
| DFRP_RowID | varchar |  |  | NO | - |
| DFRP_Sequence | double |  |  | NO | Sequence |
| DFRP_SpecimenNumber | varchar |  |  | SI | Specimen Number |
| DFRP_vtsRID_DR | varchar |  | FK | SI | vtsRID DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*