# lab.CT_Schedule_PaymentCode

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSHP_ParRef | varchar | PK |  | NO | CT_Schedule Parent Reference |
| CTSHP_Date | date |  |  | NO | Date |
| CTSHP_PaymentCode_DR | varchar |  | FK | NO | Payment Code DR |
| CTSHP_Percent | numeric |  |  | SI | Percent |
| CTSHP_RowID | varchar |  |  | NO | - |
| CTSHP_Type | varchar |  |  | SI | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*