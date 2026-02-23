# SQLUser.PHC_PBSForeword

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSFOR_RowId | bigint | PK |  | NO | - |
| PBSFOR_Code | varchar |  |  | NO | The PBS unique code for a foreward |
| PBSFOR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSFOR_CreatedDate | date |  |  | SI | Created Date |
| PBSFOR_CreatedTime | time |  |  | SI | Created Time |
| PBSFOR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSFOR_DateFrom | date |  |  | SI | Date From |
| PBSFOR_DateTo | date |  |  | SI | Date To |
| PBSFOR_Desc | varchar |  |  | NO | Description of the foreward |
| PBSFOR_Owner | varchar |  |  | SI | Owner |
| PBSFOR_Text | varchar |  |  | NO | Textual representation of the foreward |
| PBSFOR_UpdatedDate | date |  |  | SI | Updated Date |
| PBSFOR_UpdatedTime | time |  |  | SI | Updated Time |
| PBSFOR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*