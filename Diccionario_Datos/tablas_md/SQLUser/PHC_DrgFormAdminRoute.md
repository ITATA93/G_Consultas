# SQLUser.PHC_DrgFormAdminRoute

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMR_ParRef | varchar | PK |  | NO | PHC_DrgForm Parent Reference |
| ADMR_AdminRoute_DR | bigint |  | FK | SI | Des Ref AdminRoute |
| ADMR_Childsub | double |  |  | NO | Childsub |
| ADMR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMR_CreatedDate | date |  |  | SI | Created Date |
| ADMR_CreatedTime | time |  |  | SI | Created Time |
| ADMR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMR_DateFrom | date |  |  | SI | Date From |
| ADMR_DateTo | date |  |  | SI | Date To |
| ADMR_Default | varchar |  |  | SI | Default |
| ADMR_RowId | varchar |  |  | NO | - |
| ADMR_Sequence | integer |  |  | SI | Sequence |
| ADMR_UpdatedDate | date |  |  | SI | Updated Date |
| ADMR_UpdatedTime | time |  |  | SI | Updated Time |
| ADMR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*