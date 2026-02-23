# lab.CT_DBLabProceduresStatus

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDBPS_ParRef | varchar | PK |  | NO | CT_DBLabProcedures Parent Reference |
| CTDBPS_RowID | varchar |  |  | NO | - |
| CTDBPS_Sequence | varchar |  |  | NO | Sequence |
| CTDBPS_Status_DR | varchar |  | FK | SI | Status DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*