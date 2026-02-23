# lab.RG_ReagentMaterialTC

**Schema:** lab
**Columnas:** 3
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RGMT_ParRef | varchar | PK |  | NO | RG_ReagentMaterial Parent Reference |
| RGMT_RowID | varchar |  |  | NO | - |
| RGMT_TestItem_DR | varchar |  | FK | NO | Test Item DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*