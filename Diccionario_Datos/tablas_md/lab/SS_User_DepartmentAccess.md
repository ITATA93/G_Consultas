# lab.SS_User_DepartmentAccess

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUDEP_ParRef | varchar | PK |  | NO | SS_User Parent Reference |
| SUDEP_Department_DR | varchar |  | FK | NO | Des Ref Department |
| SUDEP_RowId | varchar |  |  | NO | - |
| SUDEP_ViewOnly | varchar |  |  | SI | View Only |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*