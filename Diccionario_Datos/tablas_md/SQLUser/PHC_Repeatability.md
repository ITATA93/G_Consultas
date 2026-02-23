# SQLUser.PHC_Repeatability

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REPEAT_RowId | bigint | PK |  | NO | - |
| REPEAT_Code | varchar |  |  | NO | Code |
| REPEAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REPEAT_CreatedDate | date |  |  | SI | Created Date |
| REPEAT_CreatedTime | time |  |  | SI | Created Time |
| REPEAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REPEAT_DateFrom | date |  |  | SI | Date From |
| REPEAT_DateTo | date |  |  | SI | Date To |
| REPEAT_Desc | varchar |  |  | NO | Description |
| REPEAT_ExternalCode | varchar |  |  | SI | External Code |
| REPEAT_Owner | varchar |  |  | SI | Owner |
| REPEAT_Repeatable | varchar |  |  | SI | Repeatable  |
| REPEAT_UpdatedDate | date |  |  | SI | Updated Date |
| REPEAT_UpdatedTime | time |  |  | SI | Updated Time |
| REPEAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*