# SQLUser.RBC_NationalClinicType

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NCT_RowId | bigint | PK |  | NO | - |
| NCT_Code | varchar |  |  | NO | Relationship ChildRBCEventSubType As RBCEventSubTy... |
| NCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NCT_CreatedDate | date |  |  | SI | Created Date |
| NCT_CreatedTime | time |  |  | SI | Created Time |
| NCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NCT_DateFrom | date |  |  | SI | DateFrom |
| NCT_DateTo | date |  |  | SI | DateTo |
| NCT_Desc | varchar |  |  | NO | Description |
| NCT_Owner | varchar |  |  | SI | Owner |
| NCT_UpdatedDate | date |  |  | SI | Updated Date |
| NCT_UpdatedTime | time |  |  | SI | Updated Time |
| NCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*