# web_Msg_DecisionSupport.Log

**Schema:** web_Msg_DecisionSupport
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ConditionDate | date |  |  | SI | - |
| ConditionID | varchar |  |  | SI | - |
| ConditionItemCaption | varchar |  |  | SI | - |
| ConditionItemError | varchar |  |  | SI | - |
| ConditionItemID | varchar |  |  | SI | - |
| ConditionStatus | varchar |  |  | SI | - |
| ConditionTime | time |  |  | SI | - |
| EventCode | varchar |  |  | SI | - |
| EventID | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| SessionId | varchar |  |  | SI | - |
| UpdatingClass | varchar |  |  | SI | - |
| UpdatingClassRowID | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*