# SQLUser.RBC_ClinicGroup

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLGRP_RowId | bigint | PK |  | NO | - |
| CLGRP_Code | varchar |  |  | NO | Code |
| CLGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CLGRP_CreatedDate | date |  |  | SI | Created Date |
| CLGRP_CreatedTime | time |  |  | SI | Created Time |
| CLGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLGRP_DateFrom | date |  |  | SI | Date From |
| CLGRP_DateTo | date |  |  | SI | Date To |
| CLGRP_Desc | varchar |  |  | NO | Description |
| CLGRP_Owner | varchar |  |  | SI | Owner |
| CLGRP_UpdatedDate | date |  |  | SI | Updated Date |
| CLGRP_UpdatedTime | time |  |  | SI | Updated Time |
| CLGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*