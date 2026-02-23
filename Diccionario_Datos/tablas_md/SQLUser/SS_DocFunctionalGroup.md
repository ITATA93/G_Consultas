# SQLUser.SS_DocFunctionalGroup

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSDOCGRP_RowId | bigint | PK |  | NO | - |
| SSDOCGRP_Code | varchar |  |  | NO | Code |
| SSDOCGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSDOCGRP_CreatedDate | date |  |  | SI | Created Date |
| SSDOCGRP_CreatedTime | time |  |  | SI | Created Time |
| SSDOCGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SSDOCGRP_DateFrom | date |  |  | SI | Date From |
| SSDOCGRP_DateTo | date |  |  | SI | Date To |
| SSDOCGRP_Desc | varchar |  |  | NO | Description |
| SSDOCGRP_Owner | varchar |  |  | SI | Owner - changed to system only |
| SSDOCGRP_System | varchar |  |  | SI | System created |
| SSDOCGRP_UpdatedDate | date |  |  | SI | Updated Date |
| SSDOCGRP_UpdatedTime | time |  |  | SI | Updated Time |
| SSDOCGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*