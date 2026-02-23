# SQLUser.PHC_PBSEpisodicity

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSEPS_RowId | bigint | PK |  | NO | - |
| PBSEPS_Code | varchar |  |  | NO | The PBS unique code for a frequency with which a c... |
| PBSEPS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSEPS_CreatedDate | date |  |  | SI | Created Date |
| PBSEPS_CreatedTime | time |  |  | SI | Created Time |
| PBSEPS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSEPS_DateFrom | date |  |  | SI | Date From |
| PBSEPS_DateTo | date |  |  | SI | Date To |
| PBSEPS_Desc | varchar |  |  | NO | The textual description of the frequency |
| PBSEPS_Owner | varchar |  |  | SI | Owner |
| PBSEPS_UpdatedDate | date |  |  | SI | Updated Date |
| PBSEPS_UpdatedTime | time |  |  | SI | Updated Time |
| PBSEPS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*