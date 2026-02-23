# SQLUser.RBC_EquipmentGroup

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GRP_RowId | bigint | PK |  | NO | - |
| GRP_Code | varchar |  |  | NO | Code |
| GRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GRP_CreatedDate | date |  |  | SI | Created Date |
| GRP_CreatedTime | time |  |  | SI | Created Time |
| GRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GRP_DateFrom | date |  |  | SI | Date From |
| GRP_DateTo | date |  |  | SI | Date To |
| GRP_Desc | varchar |  |  | NO | Description |
| GRP_Owner | varchar |  |  | SI | Owner |
| GRP_UpdatedDate | date |  |  | SI | Updated Date |
| GRP_UpdatedTime | time |  |  | SI | Updated Time |
| GRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*