# SQLUser.ARC_GuarantorGroup

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GUAGRP_RowId | bigint | PK |  | NO | - |
| ChildQ21DR | - |  |  | SI | Child Reference: Ojos Alterados |
| GUAGRP_Code | varchar |  |  | NO | Code |
| GUAGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GUAGRP_CreatedDate | date |  |  | SI | Created Date |
| GUAGRP_CreatedTime | time |  |  | SI | Created Time |
| GUAGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GUAGRP_DateFrom | date |  |  | SI | Date From |
| GUAGRP_DateTo | date |  |  | SI | Date To |
| GUAGRP_Desc | varchar |  |  | NO | Description |
| GUAGRP_Owner | varchar |  |  | SI | Owner |
| GUAGRP_UpdatedDate | date |  |  | SI | Updated Date |
| GUAGRP_UpdatedTime | time |  |  | SI | Updated Time |
| GUAGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q83Q1 | - |  |  | SI | Reflejos |
| Q83Q2 | - |  |  | SI | Estado |
| Q83Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*