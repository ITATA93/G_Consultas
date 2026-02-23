# web_Msg.RB_ResEffDateCurrSession

**Schema:** web_Msg
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| RBCSApptListDate | date |  |  | SI | Active Date for the appointment List |
| RBCSApptListRBSessionID | varchar |  |  | SI | Active Appt List RBResource Session ID |
| RBCSApptListResourceID | varchar |  |  | SI | Active RBResource Session ID for the appointment L... |
| RBCSClinicListRBSessionID | varchar |  |  | SI | Active SessionID for the clinic List |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*