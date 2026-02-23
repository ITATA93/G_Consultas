# SQLUser.RB_ResEffDateSessServices

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SER_ParRef | varchar | PK |  | NO | RB_ResEffDateSession Parent Reference |
| SER_ARCIM_ARCOS | varchar |  |  | SI | ARCIM/ARCOS |
| SER_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| SER_Childsub | double |  |  | NO | Childsub |
| SER_DayOfWeek_DR | double |  | FK | SI | Des Ref Day Of Week |
| SER_Desc | varchar |  |  | SI | Desc |
| SER_EBookEntity | varchar |  |  | SI | E-Booker Entities |
| SER_EBookPriority | varchar |  |  | SI | E-Booker Priorities |
| SER_EBookingEnabled | varchar |  |  | SI | E-Booking Enabled |
| SER_EBookingSuspReas | varchar |  |  | SI | E-Booking Suspended Reason |
| SER_Minutes | double |  |  | SI | Minutes |
| SER_NoOfTimesBook | double |  |  | SI | No Of Times Book |
| SER_RBC_Service_DR | bigint |  | FK | SI | Des Ref RBC Service |
| SER_ReminderDays | double |  |  | SI | ReminderDays |
| SER_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| SER_RowId | varchar |  |  | NO | - |
| SER_SerMessage | varchar |  |  | SI | Service Message |
| SER_ServInfEB_DR | bigint |  | FK | SI | Des Ref ServInfEBooking |
| SER_StartTime | time |  |  | SI | Start Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*