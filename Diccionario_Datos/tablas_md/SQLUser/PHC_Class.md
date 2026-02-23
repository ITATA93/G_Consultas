# SQLUser.PHC_Class

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCCL_RowId | bigint | PK |  | NO | - |
| PHCCL_Code | varchar |  |  | NO | Code |
| PHCCL_CreatedDate | date |  |  | SI | Created Date |
| PHCCL_CreatedTime | time |  |  | SI | Created Time |
| PHCCL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCCL_Desc | varchar |  |  | NO | Description |
| PHCCL_UpdatedDate | date |  |  | SI | Updated Date |
| PHCCL_UpdatedTime | time |  |  | SI | Updated Time |
| PHCCL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*