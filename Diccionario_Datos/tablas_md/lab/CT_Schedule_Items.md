# lab.CT_Schedule_Items

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSHI_ParRef | varchar | PK |  | NO | CT_Schedule Parent Reference |
| CTSHI_Item_DR | varchar |  | FK | NO | Item DR |
| CTSHI_RowID | varchar |  |  | NO | - |
| CTSHI_in_LimitPerDay | double |  |  | SI | Inpatients Limit Per Day |
| CTSHI_in_LimitPerPeriod | double |  |  | SI | Inpatients Limit per Period |
| CTSHI_in_Period | double |  |  | SI | Inpatients Period |
| CTSHI_out_LimitPerDay | numeric |  |  | SI | Outpatients Limit per Day |
| CTSHI_out_LimitPerPeriod | numeric |  |  | SI | Outpatients Limit per Period |
| CTSHI_out_Period | numeric |  |  | SI | Outpatients Period |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*