# SQLUser.SS_ProfileDepartmentOrder

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSPDO_ParRef | bigint | PK |  | NO | Parent table |
| SSPDO_Department_DR | bigint |  | FK | SI | Lab Department  |
| SSPDO_RowID | varchar |  |  | NO | - |
| SSPDO_Sequence | double |  |  | SI | Sequence |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*