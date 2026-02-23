# SQLUser.PHC_GenericRtFormsInter

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INT_ParRef | varchar | PK |  | NO | PHC_GenericRtForms Parent Reference |
| INT_Childsub | double |  |  | NO | Childsub |
| INT_CreatedDate | date |  |  | SI | Created Date |
| INT_CreatedTime | time |  |  | SI | Created Time |
| INT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INT_GenRouteForm_DR | varchar |  | FK | SI | Des Ref GenRouteForm |
| INT_Monograph_DR | bigint |  | FK | SI | Des Ref Monograph |
| INT_RowId | varchar |  |  | NO | - |
| INT_Severity_DR | bigint |  | FK | SI | Des Ref Severity |
| INT_UpdatedDate | date |  |  | SI | Updated Date |
| INT_UpdatedTime | time |  |  | SI | Updated Time |
| INT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*