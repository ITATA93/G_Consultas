# Tools_DataMover_Message.TrakEventNotifyRequest

**Schema:** Tools_DataMover_Message
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| EventData | varchar |  |  | SI | - |
| EventStatus | varchar |  |  | SI | - |
| IsErrorEventData | bit |  |  | SI | - |
| IsPatientEventStatus | bit |  |  | SI | - |
| LogIndex | integer |  |  | SI | - |
| NotifyCentralServer | bit |  |  | SI | - |
| NotifyTrakUI | bit |  |  | SI | - |
| RegistrationNumber | varchar |  |  | SI | - |
| TrakProcessGUID | varchar |  |  | SI | - |
| TrakSessionID | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*