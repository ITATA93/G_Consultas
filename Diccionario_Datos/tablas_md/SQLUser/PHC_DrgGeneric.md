# SQLUser.PHC_DrgGeneric

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GEN_ParRef | bigint | PK |  | NO | PHC_DrgMast Parent Reference |
| GEN_Childsub | double |  |  | NO | Childsub |
| GEN_CreatedDate | date |  |  | SI | Created Date |
| GEN_CreatedTime | time |  |  | SI | Created Time |
| GEN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GEN_Generic_DR | bigint |  | FK | SI | Des Ref Generic |
| GEN_RowId | varchar |  |  | NO | - |
| GEN_UpdatedDate | date |  |  | SI | Updated Date |
| GEN_UpdatedTime | time |  |  | SI | Updated Time |
| GEN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*