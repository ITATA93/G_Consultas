# lab.CT_BugsCalcConditions

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBCC_ParRef | varchar | PK |  | NO | CT_BugsCalculations Parent Reference |
| CTBCC_Antibiotic_DR | varchar |  | FK | NO | Antibiotic DR |
| CTBCC_Result_DR | varchar |  | FK | SI | Result DR |
| CTBCC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*