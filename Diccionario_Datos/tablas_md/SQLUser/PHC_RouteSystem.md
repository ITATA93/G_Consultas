# SQLUser.PHC_RouteSystem

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROUTESYS_RowId | bigint | PK |  | NO | - |
| ROUTESYS_Code | varchar |  |  | NO | Code |
| ROUTESYS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ROUTESYS_CreatedDate | date |  |  | SI | Created Date |
| ROUTESYS_CreatedTime | time |  |  | SI | Created Time |
| ROUTESYS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROUTESYS_DateFrom | date |  |  | SI | Date From |
| ROUTESYS_DateTo | date |  |  | SI | Date To |
| ROUTESYS_Desc | varchar |  |  | NO | Description |
| ROUTESYS_Owner | varchar |  |  | SI | Owner |
| ROUTESYS_UpdatedDate | date |  |  | SI | Updated Date |
| ROUTESYS_UpdatedTime | time |  |  | SI | Updated Time |
| ROUTESYS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*