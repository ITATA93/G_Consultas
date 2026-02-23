# lab.CB_CollectorBooking

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CB_RowID | varchar | PK |  | NO | - |
| CB_BookingDate | date |  |  | NO | Booking Date |
| CB_BookingTime | varchar |  |  | NO | Booking Time |
| CB_Collector_DR | varchar |  | FK | NO | Collector DR |
| CB_Episode_DR | varchar |  | FK | SI | Episode DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*