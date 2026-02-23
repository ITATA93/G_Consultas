# SQLUser.LB_SpecimenContainerAlternateNumber

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Muestras de Laboratorio**. Gestión de especímenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBSPCAN_ParRef | bigint | PK |  | NO | Patent |
| LBSPCAN_Department_DR | bigint |  | FK | SI | Department |
| LBSPCAN_Function | varchar |  |  | SI | Function
Indicates the purpose of the number and ... |
| LBSPCAN_LabSiteList | varchar |  |  | SI | Lab Site List |
| LBSPCAN_Number | varchar |  |  | NO | Number |
| LBSPCAN_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*