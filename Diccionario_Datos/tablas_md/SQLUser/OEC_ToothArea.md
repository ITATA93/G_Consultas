# SQLUser.OEC_ToothArea

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TOOTHA_RowId | bigint | PK |  | NO | - |
| TOOTHA_Code | varchar |  |  | NO | Code |
| TOOTHA_CreatedDate | date |  |  | SI | Created Date |
| TOOTHA_CreatedTime | time |  |  | SI | Created Time |
| TOOTHA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TOOTHA_Desc | varchar |  |  | NO | Description |
| TOOTHA_UpdatedDate | date |  |  | SI | Updated Date |
| TOOTHA_UpdatedTime | time |  |  | SI | Updated Time |
| TOOTHA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*