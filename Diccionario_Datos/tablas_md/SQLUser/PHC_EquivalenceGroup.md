# SQLUser.PHC_EquivalenceGroup

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EQGRP_RowId | bigint | PK |  | NO | - |
| EQGRP_Code | varchar |  |  | NO | Code |
| EQGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EQGRP_CreatedDate | date |  |  | SI | Created Date |
| EQGRP_CreatedTime | time |  |  | SI | Created Time |
| EQGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EQGRP_DateFrom | date |  |  | SI | Date From |
| EQGRP_DateTo | date |  |  | SI | Date To |
| EQGRP_Desc | varchar |  |  | NO | Description |
| EQGRP_LongDesc | varchar |  |  | SI | LongDescription |
| EQGRP_Owner | varchar |  |  | SI | Owner |
| EQGRP_UpdatedDate | date |  |  | SI | Updated Date |
| EQGRP_UpdatedTime | time |  |  | SI | Updated Time |
| EQGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*