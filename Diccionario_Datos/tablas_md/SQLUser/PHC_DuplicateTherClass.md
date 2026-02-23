# SQLUser.PHC_DuplicateTherClass

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DTC_RowId | bigint | PK |  | NO | - |
| DTC_Code | varchar |  |  | NO | Code |
| DTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DTC_CreatedDate | date |  |  | SI | Created Date |
| DTC_CreatedTime | time |  |  | SI | Created Time |
| DTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DTC_Desc | varchar |  |  | NO | Description |
| DTC_NumberAllowed | double |  |  | SI | NumberAllowed |
| DTC_Owner | varchar |  |  | SI | Owner |
| DTC_UpdatedDate | date |  |  | SI | Updated Date |
| DTC_UpdatedTime | time |  |  | SI | Updated Time |
| DTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*