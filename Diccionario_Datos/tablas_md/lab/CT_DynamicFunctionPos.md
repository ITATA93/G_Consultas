# lab.CT_DynamicFunctionPos

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDFP_ParRef | varchar | PK |  | NO | CT_DynamicFunction Parent Reference |
| CTDFP_RowID | varchar |  |  | NO | - |
| CTDFP_Sequence | double |  |  | NO | Sequence |
| CTDFP_Time | double |  |  | SI | Time in hours from position 0 |
| CTDFP_TimeWindow | double |  |  | SI | Time Window |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*