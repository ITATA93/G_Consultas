# lab.CT_Species

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Especialidades**. Especialidades médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSP_RowId | varchar | PK |  | NO | - |
| CTSP_Code | varchar |  |  | NO | Code |
| CTSP_Desc | varchar |  |  | SI | Description |
| CTSP_PromptForPregnant | varchar |  |  | SI | Prompt For Pregnant |
| CTSP_SpecimenClass_DR | varchar |  | FK | SI | Specimen Class DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*