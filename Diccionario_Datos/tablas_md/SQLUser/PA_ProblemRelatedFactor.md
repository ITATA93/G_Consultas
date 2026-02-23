# SQLUser.PA_ProblemRelatedFactor

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROBRF_ParRef | varchar | PK |  | NO | Parent table |
| PROBRF_Childsub | double |  |  | NO | Childsub |
| PROBRF_Desc | varchar |  |  | SI | Description |
| PROBRF_RelatedConcept_DR | varchar |  | FK | SI | DR to Code Table Related Concept |
| PROBRF_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*