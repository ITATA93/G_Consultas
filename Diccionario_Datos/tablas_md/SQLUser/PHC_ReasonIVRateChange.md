# SQLUser.PHC_ReasonIVRateChange

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RIVRATE_RowId | bigint | PK |  | NO | - |
| RIVRATE_Code | varchar |  |  | NO | Code |
| RIVRATE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RIVRATE_CreatedDate | date |  |  | SI | Created Date |
| RIVRATE_CreatedTime | time |  |  | SI | Created Time |
| RIVRATE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RIVRATE_DateFrom | date |  |  | SI | Date From |
| RIVRATE_DateTo | date |  |  | SI | Date To |
| RIVRATE_Desc | varchar |  |  | NO | Description |
| RIVRATE_Owner | varchar |  |  | SI | Owner |
| RIVRATE_UpdatedDate | date |  |  | SI | Updated Date |
| RIVRATE_UpdatedTime | time |  |  | SI | Updated Time |
| RIVRATE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*