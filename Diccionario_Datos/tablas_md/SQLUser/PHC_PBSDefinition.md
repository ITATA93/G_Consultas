# SQLUser.PHC_PBSDefinition

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSDEF_RowId | bigint | PK |  | NO | - |
| PBSDEF_Code | varchar |  |  | NO | The PBS unique code for a definition |
| PBSDEF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSDEF_CreatedDate | date |  |  | SI | Created Date |
| PBSDEF_CreatedTime | time |  |  | SI | Created Time |
| PBSDEF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSDEF_DateFrom | date |  |  | SI | Date From |
| PBSDEF_DateTo | date |  |  | SI | Date To |
| PBSDEF_Desc | varchar |  |  | NO | The textual definition |
| PBSDEF_Owner | varchar |  |  | SI | Owner |
| PBSDEF_UpdatedDate | date |  |  | SI | Updated Date |
| PBSDEF_UpdatedTime | time |  |  | SI | Updated Time |
| PBSDEF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*