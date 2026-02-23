# SQLUser.PA_ProblemRiskFactor

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROBRISKF_ParRef | varchar | PK |  | NO | Parent table |
| PROBRISKF_Childsub | double |  |  | NO | Childsub |
| PROBRISKF_Desc | varchar |  |  | SI | Description |
| PROBRISKF_RelatedConcept_DR | varchar |  | FK | SI | DR to Code Table Related Concept |
| PROBRISKF_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*