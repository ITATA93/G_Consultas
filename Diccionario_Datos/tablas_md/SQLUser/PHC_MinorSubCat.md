# SQLUser.PHC_MinorSubCat

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIN_ParRef | varchar | PK |  | NO | PHC_SubCat Parent Reference |
| MIN_Childsub | double |  |  | NO | Childsub |
| MIN_Code | varchar |  |  | NO | Code |
| MIN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MIN_CreatedDate | date |  |  | SI | Created Date |
| MIN_CreatedTime | time |  |  | SI | Created Time |
| MIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MIN_Desc | varchar |  |  | NO | Description |
| MIN_RowId | varchar |  |  | NO | - |
| MIN_UpdatedDate | date |  |  | SI | Updated Date |
| MIN_UpdatedTime | time |  |  | SI | Updated Time |
| MIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*