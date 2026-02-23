# lab.CT_PaymentCodeExcTestSets

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPCE_ParRef | varchar | PK |  | NO | CT_PaymentCode Parent Reference |
| CTPCE_Reject | varchar |  |  | SI | Reject |
| CTPCE_RowID | varchar |  |  | NO | - |
| CTPCE_TestSet_DR | varchar |  | FK | NO | Test Set DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*