# websys.Notification

> Notifications

**Schema:** websys
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Notifications

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Acknowledged | bit |  |  | SI | - |
| AcknowledgedUserDR | bigint |  | FK | SI | - |
| DSSAuditDR | bigint |  | FK | SI | - |
| DateAcknowledged | date |  |  | SI | - |
| DateCreated | date |  |  | SI | - |
| GeneralItemDR | bigint |  | FK | SI | Notification message item for the notification (if... |
| OEAlertDR | varchar |  | FK | SI | - |
| TimeAcknowledged | time |  |  | SI | - |
| TimeCreated | time |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*