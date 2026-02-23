# web_Msg_RBAppointment.FlexiBookServiceSlot

**Schema:** web_Msg_RBAppointment
**Columnas:** 32
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Agenda de Citas (Web)**. Interfaz de agendamiento de consultas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ApptSchedDR | varchar |  | FK | SI | - |
| CustomFlag1 | varchar |  |  | SI | - |
| CustomFlag2 | varchar |  |  | SI | - |
| CustomFlag3 | varchar |  |  | SI | - |
| Date | date |  |  | SI | - |
| Duration | numeric |  |  | SI | - |
| EndTime | time |  |  | SI | - |
| Equipment | bigint |  |  | SI | - |
| GroupAppts | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| InterpreterDR | bigint |  | FK | SI | - |
| LockedAppointment | varchar |  |  | SI | - |
| OPDRoom | bigint |  |  | SI | - |
| Overbooked | bit |  |  | SI | - |
| ParRef | varchar |  |  | SI | - |
| Price | numeric |  |  | SI | - |
| REDSDR | varchar |  | FK | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SMSConsent | varchar |  |  | SI | - |
| SeqRange | varchar |  |  | SI | - |
| ServiceDR | bigint |  | FK | SI | - |
| ServiceMessage | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| StartDate | date |  |  | SI | - |
| StartTime | time |  |  | SI | - |
| Technician | varchar |  |  | SI | - |
| TransportDR | bigint |  | FK | SI | - |
| childsub | bigint |  |  | NO | - |
| chkInterpreterRequired | varchar |  |  | SI | - |
| chkTransportRequired | varchar |  |  | SI | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*