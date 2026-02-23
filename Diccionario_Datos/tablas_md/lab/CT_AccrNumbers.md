# lab.CT_AccrNumbers

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTACN_RowID | double | PK |  | NO | - |
| CTACN_AccreditationNo | varchar |  |  | SI | Accreditation Number |
| CTACN_Department_DR | varchar |  | FK | SI | Department DR |
| CTACN_EndDate | date |  |  | SI | End Date |
| CTACN_Sequence | double |  |  | NO | Sequence |
| CTACN_StartDate | date |  |  | SI | Start Date |
| CTACN_Usersite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*