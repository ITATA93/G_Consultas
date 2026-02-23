# SQLUser.ARC_SurchargeCode

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SURC_RowId | bigint | PK |  | NO | - |
| Q103Q1 | - |  |  | SI | N° |
| Q103Q2 | - |  |  | SI | NUE |
| Q103Q3 | - |  |  | SI | Destino |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SURC_Code | varchar |  |  | NO | Code |
| SURC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SURC_CreatedDate | date |  |  | SI | Created Date |
| SURC_CreatedTime | time |  |  | SI | Created Time |
| SURC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SURC_Desc | varchar |  |  | NO | Description |
| SURC_Extrinsic | varchar |  |  | SI | Name of Extrinsic |
| SURC_Fixed | double |  |  | SI | Fixed Amount |
| SURC_IncrementPrice | double |  |  | SI | Increment Price |
| SURC_IncrementTime | double |  |  | SI | Increment Time |
| SURC_OTOverride | varchar |  |  | SI | OTOverride |
| SURC_Owner | varchar |  |  | SI | Owner |
| SURC_Percentage | double |  |  | SI | Percentage Surcharge |
| SURC_TimeFrom | double |  |  | SI | Time From |
| SURC_TimeUntil | double |  |  | SI | Time Until |
| SURC_UpdatedDate | date |  |  | SI | Updated Date |
| SURC_UpdatedTime | time |  |  | SI | Updated Time |
| SURC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*