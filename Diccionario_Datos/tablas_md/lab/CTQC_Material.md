# lab.CTQC_Material

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTQCM_RowId | varchar | PK |  | NO | - |
| CTQCM_Code | varchar |  |  | NO | Material Code |
| CTQCM_Comments | varchar |  |  | SI | Comments |
| CTQCM_Description | varchar |  |  | SI | Material Description |
| CTQCM_Levels | double |  |  | SI | Number of Levels |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*