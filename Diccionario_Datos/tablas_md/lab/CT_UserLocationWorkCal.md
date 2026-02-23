# lab.CT_UserLocationWorkCal

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTUSB_ParRef | varchar | PK |  | NO | CT_UserLocation Parent Reference |
| CTUSB_Date | date |  |  | NO | Date |
| CTUSB_EndTime | time |  |  | SI | End Time |
| CTUSB_RowID | varchar |  |  | NO | - |
| CTUSB_StartTime | time |  |  | SI | Start Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*