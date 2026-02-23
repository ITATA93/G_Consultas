# web_Msg_RBAppointment.OPPlanner

**Schema:** web_Msg_RBAppointment
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Agenda de Citas (Web)**. Interfaz de agendamiento de consultas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| RBApptID | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SchedID | varchar |  |  | SI | - |
| ServiceDesc | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*