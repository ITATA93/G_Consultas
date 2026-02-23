# lab.CT_QCAGroupRules

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTQCAGR_ParRef | varchar | PK |  | NO | QC_Group Parent Reference |
| CTQCAGR_Colour | varchar |  |  | SI | Colour |
| CTQCAGR_Comments | varchar |  |  | SI | Comments |
| CTQCAGR_OrderNumber | varchar |  |  | SI | Order Number |
| CTQCAGR_RowID | varchar |  |  | NO | - |
| CTQCAGR_RulesDR | varchar |  | FK | NO | Rules DR |
| CTQCAGR_Status | varchar |  |  | SI | Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*