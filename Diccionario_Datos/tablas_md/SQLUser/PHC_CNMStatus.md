# SQLUser.PHC_CNMStatus

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CNMS_RowId | bigint | PK |  | NO | - |
| CNMS_Code | varchar |  |  | NO | Code |
| CNMS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CNMS_CreatedDate | date |  |  | SI | Created Date |
| CNMS_CreatedTime | time |  |  | SI | Created Time |
| CNMS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CNMS_DateFrom | date |  |  | SI | Date From |
| CNMS_DateTo | date |  |  | SI | Date To |
| CNMS_Desc | varchar |  |  | NO | Description |
| CNMS_Owner | varchar |  |  | SI | Owner |
| CNMS_UpdatedDate | date |  |  | SI | Updated Date |
| CNMS_UpdatedTime | time |  |  | SI | Updated Time |
| CNMS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*