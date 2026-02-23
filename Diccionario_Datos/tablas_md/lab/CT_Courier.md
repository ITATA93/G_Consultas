# lab.CT_Courier

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCR_RowId | varchar | PK |  | NO | - |
| CTCR_Code | varchar |  |  | NO | Code |
| CTCR_Confidential | varchar |  |  | SI | Confidential |
| CTCR_DisplaySequence | double |  |  | SI | Display Sequence |
| CTCR_FaxTemplate | varchar |  |  | SI | Fax Template |
| CTCR_NonPrintable | varchar |  |  | SI | Non Printable |
| CTCR_PrinterType | varchar |  |  | SI | Printer Type |
| CTCR_RunDesc | varchar |  |  | SI | Run Description |
| CTCR_TimeSlot | numeric |  |  | SI | Time Slot |
| CTCR_UserSite_DR | varchar |  | FK | SI | User Site DR |
| CTCR_WordTemplate | varchar |  |  | SI | Word Template |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*