# SQLUser.PHC_GenericAlrgGroup

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALG_ParRef | bigint | PK |  | NO | PHC_Generic Parent Reference |
| ALG_AllergyGroup_DR | bigint |  | FK | SI | Des Ref AllergyGroup |
| ALG_Childsub | double |  |  | NO | Childsub |
| ALG_CreatedDate | date |  |  | SI | Created Date |
| ALG_CreatedTime | time |  |  | SI | Created Time |
| ALG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALG_RowId | varchar |  |  | NO | - |
| ALG_UpdatedDate | date |  |  | SI | Updated Date |
| ALG_UpdatedTime | time |  |  | SI | Updated Time |
| ALG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*