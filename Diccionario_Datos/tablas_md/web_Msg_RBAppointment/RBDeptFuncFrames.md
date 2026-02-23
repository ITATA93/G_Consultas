# web_Msg_RBAppointment.RBDeptFuncFrames

**Schema:** web_Msg_RBAppointment
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Agenda de Citas (Web)**. Interfaz de agendamiento de consultas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| Date | date |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| ResourceID | varchar |  |  | SI | - |
| SessID | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*