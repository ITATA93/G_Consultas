# SQLUser.PHC_PBSCategoryProgram

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRO_ParRef | bigint | PK |  | NO | PHC_Category Parent Reference |
| PRO_Childsub | double |  |  | NO | Childsub |
| PRO_Code | varchar |  |  | SI | The PBS unique code for a group of drugs in a PBS ... |
| PRO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRO_CreatedDate | date |  |  | SI | Created Date |
| PRO_CreatedTime | time |  |  | SI | Created Time |
| PRO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRO_DateFrom | date |  |  | SI | DateFrom |
| PRO_DateTo | date |  |  | SI | DateTo |
| PRO_Desc | varchar |  |  | SI | The name of the PBS program |
| PRO_RowId | varchar |  |  | NO | - |
| PRO_UpdatedDate | date |  |  | SI | Updated Date |
| PRO_UpdatedTime | time |  |  | SI | Updated Time |
| PRO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*