# SQLUser.RBC_ReasonOverBook

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROB_RowId | bigint | PK |  | NO | - |
| ROB_Code | varchar |  |  | NO | Code |
| ROB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ROB_CreatedDate | date |  |  | SI | Created Date |
| ROB_CreatedTime | time |  |  | SI | Created Time |
| ROB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROB_DateFrom | date |  |  | SI | Date From |
| ROB_DateTo | date |  |  | SI | Date To |
| ROB_Desc | varchar |  |  | NO | Description |
| ROB_Owner | varchar |  |  | SI | Owner |
| ROB_UpdatedDate | date |  |  | SI | Updated Date |
| ROB_UpdatedTime | time |  |  | SI | Updated Time |
| ROB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*