# SQLUser.PHC_Per

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCP_RowId | bigint | PK |  | NO | - |
| PHCP_Code | varchar |  |  | NO | Per Code |
| PHCP_CreatedDate | date |  |  | SI | Created Date |
| PHCP_CreatedTime | time |  |  | SI | Created Time |
| PHCP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCP_UpdatedDate | date |  |  | SI | Updated Date |
| PHCP_UpdatedTime | time |  |  | SI | Updated Time |
| PHCP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*