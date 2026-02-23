# SQLUser.PHC_GenericAlrgXSens

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALXS_ParRef | bigint | PK |  | NO | PHC_Generic Parent Reference |
| ALG_AllergyGroup_DR | bigint |  | FK | SI | Des Ref AllergyGroup |
| ALXS_AllergyXSens_DR | bigint |  | FK | SI | Des Ref AllergyXSens |
| ALXS_Childsub | double |  |  | NO | Childsub |
| ALXS_CreatedDate | date |  |  | SI | Created Date |
| ALXS_CreatedTime | time |  |  | SI | Created Time |
| ALXS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALXS_RowId | varchar |  |  | NO | - |
| ALXS_UpdatedDate | date |  |  | SI | Updated Date |
| ALXS_UpdatedTime | time |  |  | SI | Updated Time |
| ALXS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*