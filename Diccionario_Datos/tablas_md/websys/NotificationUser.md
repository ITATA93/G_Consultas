# websys.NotificationUser

> Notification User

**Schema:** websys
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Notification User

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| Message | bigint | PK |  | NO | - |
| DateCreated | date |  |  | SI | - |
| Dismissed | bit |  |  | SI | - |
| DismissedAction | varchar |  |  | SI | Dismissal was actioned by user interaction or syst... |
| DismissedByUserDR | bigint |  | FK | SI | - |
| DismissedDate | date |  |  | SI | - |
| DismissedTime | time |  |  | SI | - |
| ForwardDR | varchar |  | FK | SI | - |
| ForwardedBy | bigint |  |  | SI | - |
| ForwardingMessage | varchar |  |  | SI | - |
| GeneralNotifType | varchar |  |  | SI | Notification Type
calculated by the parent's gene... |
| ID | varchar |  |  | NO | - |
| New | bit |  |  | SI | - |
| OriginDR | varchar |  | FK | SI | - |
| PatientDR | bigint |  | FK | SI | - |
| TimeCreated | time |  |  | SI | - |
| UserDR | bigint |  | FK | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*