# SQLUser.PHC_GenericBusinessRule

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GBR_ParRef | bigint | PK |  | NO | PHC_Generic Parent Reference |
| GBR_AdminRoute_DR | bigint |  | FK | NO | Des Ref AdminRoute |
| GBR_BrandRequired | varchar |  |  | SI | Brand Required |
| GBR_Childsub | double |  |  | NO | Childsub |
| GBR_CreatedDate | date |  |  | SI | Created Date |
| GBR_CreatedTime | time |  |  | SI | Created Time |
| GBR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GBR_FormRequired | varchar |  |  | SI | Form Required |
| GBR_MassUOM_DR | bigint |  | FK | SI | Mass Unit |
| GBR_MaxConcentration | double |  |  | SI | Maximum Concentration |
| GBR_MinConcentration | double |  |  | SI | Minimum Concentration |
| GBR_RowId | varchar |  |  | NO | - |
| GBR_StrengthRequired | varchar |  |  | SI | Strength Required |
| GBR_UpdatedDate | date |  |  | SI | Updated Date |
| GBR_UpdatedTime | time |  |  | SI | Updated Time |
| GBR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| GBR_VolumeUOM_DR | bigint |  | FK | SI | Volume Unit |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*