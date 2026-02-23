# SQLUser.RBC_ServicePriority

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SERPR_RowId | bigint | PK |  | NO | - |
| SERPR_Code | varchar |  |  | NO | Code |
| SERPR_CreatedDate | date |  |  | SI | Created Date |
| SERPR_CreatedTime | time |  |  | SI | Created Time |
| SERPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SERPR_DateFrom | date |  |  | SI | DateFrom |
| SERPR_DateTo | date |  |  | SI | DateTo |
| SERPR_Desc | varchar |  |  | NO | Description |
| SERPR_NationalCode | varchar |  |  | SI | NationalCode |
| SERPR_UpdatedDate | date |  |  | SI | Updated Date |
| SERPR_UpdatedTime | time |  |  | SI | Updated Time |
| SERPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*