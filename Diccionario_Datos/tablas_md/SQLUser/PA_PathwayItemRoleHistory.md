# SQLUser.PA_PathwayItemRoleHistory

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Datos de Paciente**. Información demográfica y administrativa. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATHIRH_ParRef | varchar | PK |  | NO | Parent Reference |
| PATHIRH_CareProv_DR | varchar |  | FK | SI | Care Provider |
| PATHIRH_Childsub | double |  |  | NO | Childsub |
| PATHIRH_DateFrom | date |  |  | SI | Date From |
| PATHIRH_DateTo | date |  |  | SI | Date To |
| PATHIRH_ReasonForVariance_DR | bigint |  | FK | SI | Pathway Item Role Reason For Variance DR  |
| PATHIRH_RowId | varchar |  |  | NO | - |
| PATHIRH_TimeFrom | time |  |  | SI | Time From |
| PATHIRH_TimeTo | time |  |  | SI | Time To |
| PATHIRH_UpdateUser_DR | bigint |  | FK | SI | Update User  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*