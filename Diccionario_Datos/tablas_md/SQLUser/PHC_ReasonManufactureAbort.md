# SQLUser.PHC_ReasonManufactureAbort

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REAMANAB_RowId | bigint | PK |  | NO | - |
| REAMANAB_Code | varchar |  |  | NO | Code |
| REAMANAB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REAMANAB_CreatedDate | date |  |  | SI | Created Date |
| REAMANAB_CreatedTime | time |  |  | SI | Created Time |
| REAMANAB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REAMANAB_DateFrom | date |  |  | SI | Date From |
| REAMANAB_DateTo | date |  |  | SI | Date To |
| REAMANAB_Desc | varchar |  |  | NO | Description |
| REAMANAB_Owner | varchar |  |  | SI | Owner |
| REAMANAB_UpdatedDate | date |  |  | SI | Updated Date |
| REAMANAB_UpdatedTime | time |  |  | SI | Updated Time |
| REAMANAB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*