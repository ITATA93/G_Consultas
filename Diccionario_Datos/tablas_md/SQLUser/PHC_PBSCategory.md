# SQLUser.PHC_PBSCategory

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSCAT_RowId | bigint | PK |  | NO | - |
| PBSCAT_Code | varchar |  |  | NO | Code |
| PBSCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSCAT_CreatedDate | date |  |  | SI | Created Date |
| PBSCAT_CreatedTime | time |  |  | SI | Created Time |
| PBSCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSCAT_DateFrom | date |  |  | SI | Date From |
| PBSCAT_DateTo | date |  |  | SI | Date To |
| PBSCAT_Desc | varchar |  |  | NO | Description of the general category of Pharmaceuti... |
| PBSCAT_Owner | varchar |  |  | SI | Owner |
| PBSCAT_UpdatedDate | date |  |  | SI | Updated Date |
| PBSCAT_UpdatedTime | time |  |  | SI | Updated Time |
| PBSCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*