# SQLUser.PHC_MedRecClassifMethod

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RCM_RowId | bigint | PK |  | NO | - |
| RCM_Code | varchar |  |  | NO | Code |
| RCM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RCM_CreatedDate | date |  |  | SI | Created Date |
| RCM_CreatedTime | time |  |  | SI | Created Time |
| RCM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RCM_DateFrom | date |  |  | SI | Date From |
| RCM_DateTo | date |  |  | SI | Date To |
| RCM_Desc | varchar |  |  | NO | Description |
| RCM_Owner | varchar |  |  | SI | Owner |
| RCM_UpdatedDate | date |  |  | SI | Updated Date |
| RCM_UpdatedTime | time |  |  | SI | Updated Time |
| RCM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*