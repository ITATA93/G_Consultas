# SQLUser.RVC_ClaimFlag

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLFL_RowId | bigint | PK |  | NO | - |
| CLFL_Code | varchar |  |  | NO | Code |
| CLFL_CreatedDate | date |  |  | SI | Created Date |
| CLFL_CreatedTime | time |  |  | SI | Created Time |
| CLFL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLFL_Desc | varchar |  |  | NO | Description |
| CLFL_UpdatedDate | date |  |  | SI | Updated Date |
| CLFL_UpdatedTime | time |  |  | SI | Updated Time |
| CLFL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*