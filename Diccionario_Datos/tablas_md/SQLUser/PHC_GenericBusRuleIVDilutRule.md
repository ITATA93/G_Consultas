# SQLUser.PHC_GenericBusRuleIVDilutRule

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DILUT_ParRef | varchar | PK |  | NO | PHC_GenericBusinessRule Parent Reference |
| DILUT_CalcMaxConc | double |  |  | SI | Calculated Max Concentration |
| DILUT_CalcMinConc | double |  |  | SI | Calculated Min Concentration |
| DILUT_Childsub | double |  |  | NO | Childsub |
| DILUT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DILUT_CreatedDate | date |  |  | SI | Created Date |
| DILUT_CreatedTime | time |  |  | SI | Created Time |
| DILUT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DILUT_DoseFrom | double |  |  | SI | Dose From |
| DILUT_DoseTo | double |  |  | SI | Dose To |
| DILUT_DoseUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| DILUT_RowId | varchar |  |  | NO | - |
| DILUT_UpdatedDate | date |  |  | SI | Updated Date |
| DILUT_UpdatedTime | time |  |  | SI | Updated Time |
| DILUT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DILUT_Volume | double |  |  | SI | Volume |
| DILUT_VolumeUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*