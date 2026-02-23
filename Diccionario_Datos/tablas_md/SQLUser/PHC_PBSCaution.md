# SQLUser.PHC_PBSCaution

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSCAU_RowId | bigint | PK |  | NO | - |
| PBSCAU_Code | varchar |  |  | NO | The PBS unique code for a caution |
| PBSCAU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSCAU_CreatedDate | date |  |  | SI | Created Date |
| PBSCAU_CreatedTime | time |  |  | SI | Created Time |
| PBSCAU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSCAU_DateFrom | date |  |  | SI | Date From |
| PBSCAU_DateTo | date |  |  | SI | Date To |
| PBSCAU_Desc | varchar |  |  | NO | The textual description of the caution |
| PBSCAU_Owner | varchar |  |  | SI | Owner |
| PBSCAU_Text | varchar |  |  | NO | Textual representation of the PBS Caution |
| PBSCAU_UpdatedDate | date |  |  | SI | Updated Date |
| PBSCAU_UpdatedTime | time |  |  | SI | Updated Time |
| PBSCAU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*