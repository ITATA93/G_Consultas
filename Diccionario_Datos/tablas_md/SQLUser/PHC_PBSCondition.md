# SQLUser.PHC_PBSCondition

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSCON_RowId | bigint | PK |  | NO | - |
| PBSCON_Code | varchar |  |  | NO | The PBS unique code for a condition the patient is... |
| PBSCON_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSCON_CreatedDate | date |  |  | SI | Created Date |
| PBSCON_CreatedTime | time |  |  | SI | Created Time |
| PBSCON_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSCON_DateFrom | date |  |  | SI | Date From |
| PBSCON_DateTo | date |  |  | SI | Date To |
| PBSCON_Desc | varchar |  |  | NO | The textual description of the condition |
| PBSCON_Owner | varchar |  |  | SI | Owner |
| PBSCON_UpdatedDate | date |  |  | SI | Updated Date |
| PBSCON_UpdatedTime | time |  |  | SI | Updated Time |
| PBSCON_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*