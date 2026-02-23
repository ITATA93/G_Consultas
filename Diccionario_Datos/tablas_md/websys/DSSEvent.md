# websys.DSSEvent

> "4-Mar-03 17:08 AW: need both a date from and a date to field. and the event should only be triggered if they are within todays date range.. they shouldn't be deleting an event, just giving it a date to

**Schema:** websys
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "4-Mar-03 17:08 AW: need both a date from and a date to field. and the event should only be triggered if they are within todays date range.. they shouldn't be deleting an event, just giving it a date to

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AuditActions | bit |  |  | SI | - |
| Class | varchar |  |  | SI | - |
| ClassTrigger | varchar |  |  | SI | ,OnBeforeInsert,OnAfterInsert,OnBeforeUpdate,OnAft... |
| Code | varchar |  |  | SI | - |
| Component | varchar |  |  | SI | - |
| ComponentTrigger | varchar |  |  | SI | ,OnBeforeSave,OnAfterSave,OnLoad |
| Description | varchar |  |  | SI | - |
| EndDate | date |  |  | SI | - |
| EventError | varchar |  |  | SI | - |
| EventStatus | varchar |  |  | SI | - |
| EventType | varchar |  |  | SI | C=component
L=class |
| LastGenDate | date |  |  | SI | - |
| LastGenTime | time |  |  | SI | - |
| StartDate | date |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*