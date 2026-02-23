# SQLUser.SS_ElectronicMail

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EMAIL_RowID | bigint | PK |  | NO | - |
| EMAIL_DateSent | date |  |  | SI | Date the Message was sent |
| EMAIL_Location_DR | bigint |  | FK | SI | Hospital Location for the Message |
| EMAIL_Message | varchar |  |  | NO | Message text |
| EMAIL_Sent | varchar |  |  | SI | Has the Message been sent |
| EMAIL_Subject | varchar |  |  | NO | Subject of the Message |
| EMAIL_TimeSent | time |  |  | SI | Time the Message was sent |
| EMAIL_User_DR | bigint |  | FK | NO | User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*