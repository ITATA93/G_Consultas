# SQLUser.PAC_ContractGroup

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTGRP_RowId | bigint | PK |  | NO | - |
| CONTGRP_Code | varchar |  |  | NO | Code |
| CONTGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTGRP_CreatedDate | date |  |  | SI | Created Date |
| CONTGRP_CreatedTime | time |  |  | SI | Created Time |
| CONTGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTGRP_Desc | varchar |  |  | NO | Description |
| CONTGRP_Owner | varchar |  |  | SI | Owner |
| CONTGRP_UpdatedDate | date |  |  | SI | Updated Date |
| CONTGRP_UpdatedTime | time |  |  | SI | Updated Time |
| CONTGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ17DR | - |  |  | SI | Child Reference: Embryology summary sheet |
| Q05Q1 | - |  |  | SI | Date of embryo transfer |
| Q05Q2 | - |  |  | SI | No. transfered |
| Q05Q3 | - |  |  | SI | No. frozen |
| Q05Q4 | - |  |  | SI | No. discarded |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*