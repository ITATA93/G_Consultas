# lab.CT_MPCalcResults

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTMPG_ParRef | varchar | PK |  | NO | CT_MPCalculations Parent Reference |
| CTMPG_Antibiotics_DR | varchar |  | FK | NO | Antibiotics DR |
| CTMPG_Result_DR | varchar |  | FK | SI | Result DR |
| CTMPG_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*