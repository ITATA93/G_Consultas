# lab.RG_ReagentMaterialProcedure

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RGMP_ParRef | varchar | PK |  | NO | RG_ReagentMaterial Parent Reference |
| RGMP_Laboratory_DR | varchar |  | FK | NO | DB Laboratory DR |
| RGMP_Procedure | varchar |  |  | NO | Procedure DR |
| RGMP_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*