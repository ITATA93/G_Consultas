# SQLUser.PAC_ProgramFundingSource

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PFS_RowId | bigint | PK |  | NO | - |
| PFS_Code | varchar |  |  | NO | Code |
| PFS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PFS_CreatedDate | date |  |  | SI | Created Date |
| PFS_CreatedTime | time |  |  | SI | Created Time |
| PFS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PFS_DateFrom | date |  |  | SI | Date From |
| PFS_DateTo | date |  |  | SI | Date To |
| PFS_Default | varchar |  |  | SI | Default |
| PFS_Desc | varchar |  |  | NO | Description |
| PFS_NationCode | varchar |  |  | SI | National Code |
| PFS_Owner | varchar |  |  | SI | Owner |
| PFS_UpdatedDate | date |  |  | SI | Updated Date |
| PFS_UpdatedTime | time |  |  | SI | Updated Time |
| PFS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q18Q1 | - |  |  | SI | Size |
| Q18Q2 | - |  |  | SI | Site |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*