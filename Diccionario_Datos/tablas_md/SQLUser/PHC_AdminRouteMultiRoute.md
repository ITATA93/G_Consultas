# SQLUser.PHC_AdminRouteMultiRoute

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MR_ParRef | bigint | PK |  | NO | Parent Reference |
| MR_AdminRoute_DR | bigint |  | FK | SI | Admin Route |
| MR_Childsub | double |  |  | NO | Childsub |
| MR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MR_CreatedDate | date |  |  | SI | Created Date |
| MR_CreatedTime | time |  |  | SI | Created Time |
| MR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MR_DateFrom | date |  |  | SI | Date From |
| MR_DateTo | date |  |  | SI | Date To |
| MR_RowId | varchar |  |  | NO | - |
| MR_UpdatedDate | date |  |  | SI | Updated Date |
| MR_UpdatedTime | time |  |  | SI | Updated Time |
| MR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*