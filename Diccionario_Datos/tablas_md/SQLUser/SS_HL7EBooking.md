# SQLUser.SS_HL7EBooking

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EB_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| EB_AppointmentID | varchar |  |  | SI | Appointment ID |
| EB_ApptIDFormat | varchar |  |  | SI | ApptIDFormat |
| EB_Childsub | double |  |  | NO | Childsub |
| EB_DaysToSend | double |  |  | SI | DaysToSend |
| EB_OnRequestAppt | varchar |  |  | SI | OnRequestAppt |
| EB_PrimaryPatNum | varchar |  |  | SI | PrimaryPatientNumber |
| EB_RowId | varchar |  |  | NO | - |
| EB_SendAllSlots | varchar |  |  | SI | SendAllSlots |
| EB_WLPriority_DR | bigint |  | FK | SI | Des Ref WLPriority |
| EB_WLReasonForList_DR | bigint |  | FK | SI | Des Ref WLReasonForList |
| EB_WLType_DR | bigint |  | FK | SI | Des Ref WLType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*