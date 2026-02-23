# SQLUser.PA_ProblemDefChar

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROBDC_ParRef | varchar | PK |  | NO | Parent table |
| PROBDC_Childsub | double |  |  | NO | Childsub |
| PROBDC_Desc | varchar |  |  | SI | Description |
| PROBDC_RelatedConcept_DR | varchar |  | FK | SI | DR to Code Table Related Concept |
| PROBDC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*