# lab.CT_BugGroupCalcConditions

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBGO_ParRef | varchar | PK |  | NO | CT_Bugs_Group_Calculations Parent Reference |
| CTBGO_Antibiotics_DR | varchar |  | FK | NO | Des Ref Antibiotics |
| CTBGO_Result_DR | varchar |  | FK | SI | Des Ref Result |
| CTBGO_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*