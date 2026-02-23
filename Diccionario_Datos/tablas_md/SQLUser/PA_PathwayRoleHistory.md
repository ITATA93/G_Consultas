# SQLUser.PA_PathwayRoleHistory

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Datos de Paciente**. Información demográfica y administrativa. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATHRH_ParRef | varchar | PK |  | NO | Parent Reference |
| PATHRH_CareProv_DR | varchar |  | FK | SI | Care Provider |
| PATHRH_Childsub | double |  |  | NO | Childsub |
| PATHRH_DateFrom | date |  |  | SI | Date From |
| PATHRH_DateTo | date |  |  | SI | Date To |
| PATHRH_ReasonForVariance_DR | bigint |  | FK | SI | Pathway Item Role Reason For Variance DR  |
| PATHRH_RowId | varchar |  |  | NO | - |
| PATHRH_TimeFrom | time |  |  | SI | Time From |
| PATHRH_TimeTo | time |  |  | SI | Time To |
| PATHRH_UpdateUser_DR | bigint |  | FK | SI | Update User  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*