# lab.HOS_HospitalDataBase

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOS_RowID | varchar | PK |  | NO | - |
| HOS_Date | date |  |  | SI | Date of Last update |
| HOS_FileName | varchar |  |  | SI | File Name |
| HOS_HospitalCode_DR | varchar |  | FK | NO | Hospital Code |
| HOS_Time | time |  |  | SI | Time of Last update |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*