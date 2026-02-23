# lab.CT_LabReportGroupItemsRes

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLRB_ParRef | varchar | PK |  | NO | CT_LabReportGroupItems Parent Reference |
| CTLRB_Procedure | varchar |  |  | SI | Procedure |
| CTLRB_Result | varchar |  |  | SI | Result |
| CTLRB_RowID | varchar |  |  | NO | - |
| CTLRB_Sequence | numeric |  |  | NO | Sequence |
| CTLRB_Stain | varchar |  |  | SI | Stain |
| CTLRB_TestItem_DR | varchar |  | FK | SI | Test Item DR |
| CTLRB_TestSet_DR | varchar |  | FK | SI | Test Set DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*