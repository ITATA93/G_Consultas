# Tools_InfoLink_Telehealth_Entity.TelehealthMeeting

**Schema:** Tools_InfoLink_Telehealth_Entity
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| MeetingId | varchar |  |  | SI | unique meeting id  |
| MeetingUrl | varchar |  |  | SI | meeting url  |
| RBAppointmentDR | varchar |  | FK | NO | appointment row id  |
| RequestDR | bigint |  | FK | SI | relation to meeting request used to get the meetin... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*