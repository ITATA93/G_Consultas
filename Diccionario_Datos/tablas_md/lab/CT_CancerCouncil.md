# lab.CT_CancerCouncil

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCA_RowID | varchar | PK |  | NO | - |
| CTCA_Code | varchar |  |  | NO | Code |
| CTCA_Department_DR | varchar |  | FK | SI | Department DR |
| CTCA_Descr | varchar |  |  | SI | Description |
| CTCA_OrderNumber | numeric |  |  | SI | Order Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*