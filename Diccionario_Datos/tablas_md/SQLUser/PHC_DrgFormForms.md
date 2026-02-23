# SQLUser.PHC_DrgFormForms

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FRM_ParRef | varchar | PK |  | NO | PHC_DrgForm Parent Reference |
| FRM_Childsub | double |  |  | NO | Childsub |
| FRM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FRM_CreatedDate | date |  |  | SI | Created Date |
| FRM_CreatedTime | time |  |  | SI | Created Time |
| FRM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FRM_DrgForm_DR | varchar |  | FK | SI | Des Ref DrgForm |
| FRM_RowId | varchar |  |  | NO | - |
| FRM_UpdatedDate | date |  |  | SI | Updated Date |
| FRM_UpdatedTime | time |  |  | SI | Updated Time |
| FRM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*