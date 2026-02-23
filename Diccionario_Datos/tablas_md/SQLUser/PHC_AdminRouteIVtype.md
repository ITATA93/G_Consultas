# SQLUser.PHC_AdminRouteIVtype

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IV_ParRef | bigint | PK |  | NO | Parent Reference |
| IV_Childsub | double |  |  | NO | Childsub |
| IV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| IV_CreatedDate | date |  |  | SI | Created Date |
| IV_CreatedTime | time |  |  | SI | Created Time |
| IV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IV_DateFrom | date |  |  | NO | Date From |
| IV_DateTo | date |  |  | SI | Date To |
| IV_Default | varchar |  |  | SI | Default |
| IV_IVType | varchar |  |  | SI | IVType |
| IV_OrderContext | varchar |  |  | SI | OrderContext |
| IV_RowId | varchar |  |  | NO | - |
| IV_UpdatedDate | date |  |  | SI | Updated Date |
| IV_UpdatedTime | time |  |  | SI | Updated Time |
| IV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*