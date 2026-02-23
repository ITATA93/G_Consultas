# websys.NotificationItem

> The Message Item of the Notification

**Schema:** websys
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

*Descripción original:* The Message Item of the Notification

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| NOTIActionTaskDR | bigint |  | FK | SI | Task Item to Action the Notification |
| NOTIActionWorkFlowDR | bigint |  | FK | SI | WorkFlow to Action the Notification |
| NOTIActionWorkFlowInMainWin | bit |  |  | SI | Send the WorkFlow to Action the Notification insid... |
| NOTIFromUserDR | bigint |  | FK | SI | User that triggered the notification |
| NOTIFromUserGroupDR | bigint |  | FK | SI | User's Security that triggered the notification |
| NOTIFromUserProfileDR | bigint |  | FK | SI | User's Access Profile that triggered the notificat... |
| NOTIFromWorkFlowDR | bigint |  | FK | SI | WorkFlow that triggered the notification |
| NOTIMessage | varchar |  |  | SI | Message String |
| NOTIOEOrdItemDR | varchar |  | FK | SI | OEOrdItem Reference |
| NOTIPAADMDR | bigint |  | FK | SI | Episode Reference |
| NOTIPAPMIDR | bigint |  | FK | SI | Patient Reference |
| NOTIPriority | varchar |  |  | SI | Priority of message |
| NOTIType | varchar |  |  | SI | Type of notification
used to action extra type sp... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*