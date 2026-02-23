# SQLUser.PHC_AdmixIngrInstruction

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADINST_RowId | bigint | PK |  | NO | - |
| ADINST_Code | varchar |  |  | NO | Code |
| ADINST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADINST_CreatedDate | date |  |  | SI | Created Date |
| ADINST_CreatedTime | time |  |  | SI | Created Time |
| ADINST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADINST_DateFrom | date |  |  | SI | Date From |
| ADINST_DateTo | date |  |  | SI | Date To |
| ADINST_Desc | varchar |  |  | NO | Description |
| ADINST_Owner | varchar |  |  | SI | Owner |
| ADINST_UpdatedDate | date |  |  | SI | Updated Date |
| ADINST_UpdatedTime | time |  |  | SI | Updated Time |
| ADINST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*