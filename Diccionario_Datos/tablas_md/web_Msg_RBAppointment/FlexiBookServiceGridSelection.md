# web_Msg_RBAppointment.FlexiBookServiceGridSelection

**Schema:** web_Msg_RBAppointment
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Agenda de Citas (Web)**. Interfaz de agendamiento de consultas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ApptSchedDR | varchar |  | FK | SI | - |
| CellDate | date |  |  | SI | - |
| CellTime | time |  |  | SI | - |
| Day | numeric |  |  | SI | - |
| Generated | bit |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| NumberOfCells | numeric |  |  | SI | - |
| ParRef | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| ResourceDR | bigint |  | FK | SI | - |
| ServiceDR | bigint |  | FK | SI | - |
| ServiceDuration | numeric |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*