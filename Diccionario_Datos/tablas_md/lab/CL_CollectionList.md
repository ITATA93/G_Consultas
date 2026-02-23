# lab.CL_CollectionList

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CL_RowID | varchar | PK |  | NO | - |
| CL_Code | varchar |  |  | NO | Code |
| CL_Description | varchar |  |  | SI | Description |
| CL_Labels | varchar |  |  | SI | Labels |
| CL_MaxNoOfPatients | numeric |  |  | SI | Max No Of Patients |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*