# SQLUser.PHC_ReasonNoSubstitutes

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REANOSUB_RowId | bigint | PK |  | NO | - |
| REANOSUB_Code | varchar |  |  | NO | Code |
| REANOSUB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REANOSUB_CreatedDate | date |  |  | SI | Created Date |
| REANOSUB_CreatedTime | time |  |  | SI | Created Time |
| REANOSUB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REANOSUB_DateFrom | date |  |  | SI | Date From |
| REANOSUB_DateTo | date |  |  | SI | Date To |
| REANOSUB_Desc | varchar |  |  | NO | Description |
| REANOSUB_Owner | varchar |  |  | SI | Owner |
| REANOSUB_UpdatedDate | date |  |  | SI | Updated Date |
| REANOSUB_UpdatedTime | time |  |  | SI | Updated Time |
| REANOSUB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*