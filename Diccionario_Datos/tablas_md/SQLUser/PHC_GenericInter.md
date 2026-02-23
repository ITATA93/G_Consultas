# SQLUser.PHC_GenericInter

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INT_ParRef | bigint | PK |  | NO | PHC_Generic Parent Reference |
| INT_Childsub | double |  |  | NO | Childsub |
| INT_CreatedDate | date |  |  | SI | Created Date |
| INT_CreatedTime | time |  |  | SI | Created Time |
| INT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INT_Generic_DR | bigint |  | FK | SI | Des Ref Generic |
| INT_Monograph_DR | bigint |  | FK | SI | Des Ref Monograph |
| INT_RowId | varchar |  |  | NO | - |
| INT_Severity_DR | bigint |  | FK | SI | Des Ref Severity |
| INT_UpdatedDate | date |  |  | SI | Updated Date |
| INT_UpdatedTime | time |  |  | SI | Updated Time |
| INT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*