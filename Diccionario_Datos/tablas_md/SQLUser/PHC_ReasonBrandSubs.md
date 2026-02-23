# SQLUser.PHC_ReasonBrandSubs

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REABS_RowId | bigint | PK |  | NO | - |
| REABS_Code | varchar |  |  | NO | Code |
| REABS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REABS_CreatedDate | date |  |  | SI | Created Date |
| REABS_CreatedTime | time |  |  | SI | Created Time |
| REABS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REABS_DateFrom | date |  |  | SI | Date From |
| REABS_DateTo | date |  |  | SI | Date To |
| REABS_Desc | varchar |  |  | NO | Description |
| REABS_Owner | varchar |  |  | SI | Owner |
| REABS_UpdatedDate | date |  |  | SI | Updated Date |
| REABS_UpdatedTime | time |  |  | SI | Updated Time |
| REABS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*