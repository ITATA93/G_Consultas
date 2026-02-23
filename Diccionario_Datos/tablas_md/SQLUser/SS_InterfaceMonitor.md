# SQLUser.SS_InterfaceMonitor

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INTMON_RowId | bigint | PK |  | NO | - |
| INTMON_Active | varchar |  |  | SI | Active |
| INTMON_CountMessages | double |  |  | SI | No Of Messages Received Since Started |
| INTMON_CountQueue | varchar |  |  | SI | No of Message in Outbound Queue |
| INTMON_DateLastMessage | date |  |  | SI | Date of Last Message |
| INTMON_DateLastRejection | date |  |  | SI | Date of Last Rejected Message |
| INTMON_DateStarted | date |  |  | SI | Date Interface Started |
| INTMON_Interface_DR | bigint |  | FK | NO | Des Ref SS_Interface |
| INTMON_NoUnAckRejections | varchar |  |  | SI | No of Un-Acked Rejections |
| INTMON_Status | varchar |  |  | SI | Connection Status |
| INTMON_TimeLastMessage | time |  |  | SI | Time of Last Message |
| INTMON_TimeLastRejection | time |  |  | SI | Time of Last Rejected Message |
| INTMON_TimeStarted | time |  |  | SI | Time Interface Started |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*