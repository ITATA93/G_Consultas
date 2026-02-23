# SQLUser.CT_HospitalPlan

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLAN_ParRef | bigint | PK |  | NO | CT_Hospital Parent Reference |
| PLAN_AuxIns_DR | bigint |  | FK | SI | Des Ref AuxIns |
| PLAN_Childsub | double |  |  | NO | Childsub |
| PLAN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLAN_CreatedDate | date |  |  | SI | Created Date |
| PLAN_CreatedTime | time |  |  | SI | Created Time |
| PLAN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLAN_DateFrom | date |  |  | SI | Date From |
| PLAN_DateTo | date |  |  | SI | Date To |
| PLAN_RowId | varchar |  |  | NO | - |
| PLAN_UpdatedDate | date |  |  | SI | Updated Date |
| PLAN_UpdatedTime | time |  |  | SI | Updated Time |
| PLAN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q81Q1 | - |  |  | SI | Time |
| Q81Q2 | - |  |  | SI | Strategy |
| Q81Q3 | - |  |  | SI | Sway |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*