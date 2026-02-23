# websys_DecisionSupport.Audit

**Schema:** websys_DecisionSupport
**Columnas:** 37
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ActionDate | date |  |  | SI | - |
| ActionEmailFrom | varchar |  |  | SI | - |
| ActionEmailSubject | varchar |  |  | SI | - |
| ActionEmailTo | varchar |  |  | SI | - |
| ActionEpisode | bigint |  |  | SI | - |
| ActionEvent | bigint |  |  | SI | - |
| ActionExecutionNote | varchar |  |  | SI | - |
| ActionHospital | bigint |  |  | SI | - |
| ActionID | varchar |  |  | SI | - |
| ActionItem | varchar |  |  | SI | - |
| ActionLBEpisode | bigint |  |  | SI | - |
| ActionLBSubject | bigint |  |  | SI | - |
| ActionMessage | varchar |  |  | SI | - |
| ActionMsgToGroups | bigint |  |  | SI | - |
| ActionMsgToUsers | varchar |  |  | SI | - |
| ActionObsEntry | varchar |  |  | SI | - |
| ActionPatient | bigint |  |  | SI | - |
| ActionResponse | varchar |  |  | SI | - |
| ActionResponseReason | bigint |  |  | SI | - |
| ActionResponseReasonTEXT | varchar |  |  | SI | - |
| ActionResponseUser | varchar |  |  | SI | - |
| ActionSeverity | varchar |  |  | SI | - |
| ActionTargetList | varchar |  |  | SI | - |
| ActionTime | time |  |  | SI | - |
| ActionTriggerClass | varchar |  |  | SI | - |
| ActionTriggerId | varchar |  |  | SI | - |
| ActionTriggerValues | varchar |  |  | SI | - |
| ActionType | varchar |  |  | SI | - |
| ActionUser | bigint |  |  | SI | - |
| AuditGUID | varchar |  |  | SI | - |
| MessageToCP | varchar |  |  | SI | - |
| PushStatus | varchar |  |  | SI | - |
| SMSStatus | varchar |  |  | SI | - |
| TaskARCIMDR | varchar |  | FK | SI | - |
| TaskARCOrdSetsDR | varchar |  | FK | SI | - |
| TaskItem | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*