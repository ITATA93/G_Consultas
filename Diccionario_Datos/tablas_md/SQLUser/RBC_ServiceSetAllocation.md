# SQLUser.RBC_ServiceSetAllocation

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SETALL_RowId | bigint | PK |  | NO | - |
| SETALL_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| SETALL_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| SETALL_CreatedDate | date |  |  | SI | Created Date |
| SETALL_CreatedTime | time |  |  | SI | Created Time |
| SETALL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SETALL_Equip_DR | bigint |  | FK | SI | Des Ref Equip |
| SETALL_ServiceSet_DR | bigint |  | FK | SI | Des Ref RBCServiceSet |
| SETALL_UpdatedDate | date |  |  | SI | Updated Date |
| SETALL_UpdatedTime | time |  |  | SI | Updated Time |
| SETALL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*