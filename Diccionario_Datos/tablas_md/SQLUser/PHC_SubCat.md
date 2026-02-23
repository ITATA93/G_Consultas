# SQLUser.PHC_SubCat

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCSC_PHCC_ParRef | bigint | PK |  | NO | PHCC Parent Reference |
| PHCSC_ChildSub | double |  |  | NO | ChildSub (New Key) |
| PHCSC_Code | varchar |  |  | NO | Sub Category Code |
| PHCSC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCSC_CreatedDate | date |  |  | SI | Created Date |
| PHCSC_CreatedTime | time |  |  | SI | Created Time |
| PHCSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCSC_Desc | varchar |  |  | NO | Description |
| PHCSC_LookupDisplay | varchar |  |  | SI | Lookup Display |
| PHCSC_RowId | varchar |  |  | NO | - |
| PHCSC_UpdatedDate | date |  |  | SI | Updated Date |
| PHCSC_UpdatedTime | time |  |  | SI | Updated Time |
| PHCSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*