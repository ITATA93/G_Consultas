# SQLUser.PAC_ContractRole

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTROL_RowId | bigint | PK |  | NO | - |
| CONTROL_Code | varchar |  |  | SI | Code |
| CONTROL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTROL_ContractType | varchar |  |  | SI | ContractType |
| CONTROL_CreatedDate | date |  |  | SI | Created Date |
| CONTROL_CreatedTime | time |  |  | SI | Created Time |
| CONTROL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTROL_DateFrom | date |  |  | SI | Date From |
| CONTROL_DateTo | date |  |  | SI | Date To |
| CONTROL_Default | varchar |  |  | SI | Default |
| CONTROL_Desc | varchar |  |  | SI | Description |
| CONTROL_FundingArrang | varchar |  |  | SI | FundingArrang |
| CONTROL_NationCode | varchar |  |  | SI | Nation Code |
| CONTROL_Owner | varchar |  |  | SI | Owner |
| CONTROL_UpdatedDate | date |  |  | SI | Updated Date |
| CONTROL_UpdatedTime | time |  |  | SI | Updated Time |
| CONTROL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*