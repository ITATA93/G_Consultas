# SQLUser.PHC_PBSAdministrativeAdvice

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSADM_RowId | bigint | PK |  | NO | - |
| PBSADM_Code | varchar |  |  | NO | The PBS unique code for a non-legally binding note... |
| PBSADM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSADM_CreatedDate | date |  |  | SI | Created Date |
| PBSADM_CreatedTime | time |  |  | SI | Created Time |
| PBSADM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSADM_DateFrom | date |  |  | SI | Date From |
| PBSADM_DateTo | date |  |  | SI | Date To |
| PBSADM_Desc | varchar |  |  | NO | Description of the administrative advice |
| PBSADM_Owner | varchar |  |  | SI | Owner |
| PBSADM_Text | varchar |  |  | NO | Textual representation of the administrative advic... |
| PBSADM_UpdatedDate | date |  |  | SI | Updated Date |
| PBSADM_UpdatedTime | time |  |  | SI | Updated Time |
| PBSADM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*