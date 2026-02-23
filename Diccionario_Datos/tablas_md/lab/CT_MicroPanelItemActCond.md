# lab.CT_MicroPanelItemActCond

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTMPB_ParRef | varchar | PK |  | NO | CT_MicroPanelItemsActions Parent Reference |
| CTMPB_AntibioticTherapy | varchar |  |  | SI | Antibiotic Therapy |
| CTMPB_Operand | varchar |  |  | SI | Operand |
| CTMPB_Order | double |  |  | NO | Order |
| CTMPB_RowID | varchar |  |  | NO | - |
| CTMPB_SensitivityResult_DR | varchar |  | FK | SI | Sensitivity Result |
| CTMPB_Table | varchar |  |  | SI | Table |
| CTMPB_TableField | varchar |  |  | SI | Table Field |
| CTMPB_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*