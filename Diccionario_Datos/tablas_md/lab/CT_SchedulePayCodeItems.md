# lab.CT_SchedulePayCodeItems

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSHA_ParRef | varchar | PK |  | NO | CT_Schedule_PaymentCode Parent Reference |
| CTSHA_Amount | numeric |  |  | SI | Amount |
| CTSHA_Discount | double |  |  | SI | Discount |
| CTSHA_GSTAmount | double |  |  | SI | GST Amount |
| CTSHA_GSTexempt | varchar |  |  | SI | GST exempt |
| CTSHA_Item_DR | varchar |  | FK | NO | Item DR |
| CTSHA_ManualEntry | varchar |  |  | SI | Manual Entry |
| CTSHA_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*