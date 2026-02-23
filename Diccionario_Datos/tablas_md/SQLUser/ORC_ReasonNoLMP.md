# SQLUser.ORC_ReasonNoLMP

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RSNLMP_RowId | bigint | PK |  | NO | - |
| RSNLMP_Code | varchar |  |  | NO | Code |
| RSNLMP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RSNLMP_CreatedDate | date |  |  | SI | Created Date |
| RSNLMP_CreatedTime | time |  |  | SI | Created Time |
| RSNLMP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RSNLMP_DateFrom | date |  |  | SI | Date From |
| RSNLMP_DateTo | date |  |  | SI | Date To |
| RSNLMP_Desc | varchar |  |  | NO | Description |
| RSNLMP_Owner | varchar |  |  | SI | Owner |
| RSNLMP_UpdatedDate | date |  |  | SI | Updated Date |
| RSNLMP_UpdatedTime | time |  |  | SI | Updated Time |
| RSNLMP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*