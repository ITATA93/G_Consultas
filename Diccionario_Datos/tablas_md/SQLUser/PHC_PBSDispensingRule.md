# SQLUser.PHC_PBSDispensingRule

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSDPR_RowId | bigint | PK |  | NO | - |
| PBSDPR_Code | varchar |  |  | NO | The PBS unique code for a dispensing rule which de... |
| PBSDPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSDPR_CreatedDate | date |  |  | SI | Created Date |
| PBSDPR_CreatedTime | time |  |  | SI | Created Time |
| PBSDPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSDPR_DateFrom | date |  |  | SI | Date From |
| PBSDPR_DateTo | date |  |  | SI | Date To |
| PBSDPR_Desc | varchar |  |  | NO | The title of the dispensing rule |
| PBSDPR_Owner | varchar |  |  | SI | Owner |
| PBSDPR_UpdatedDate | date |  |  | SI | Updated Date |
| PBSDPR_UpdatedTime | time |  |  | SI | Updated Time |
| PBSDPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*