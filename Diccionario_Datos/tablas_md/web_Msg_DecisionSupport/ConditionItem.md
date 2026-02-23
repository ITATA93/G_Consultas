# web_Msg_DecisionSupport.ConditionItem

**Schema:** web_Msg_DecisionSupport
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| BooleanOperator | varchar |  |  | SI | - |
| ConditionBetweenValue | varchar |  |  | SI | - |
| ConditionOperator | varchar |  |  | SI | Use 'DSSConditionalOperator' standard Type |
| ConditionProperty | varchar |  |  | SI | - |
| ConditionValue | varchar |  |  | SI | - |
| ConditionValueList | bigint |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| MainProperty | varchar |  |  | SI | Use to define which one is the main property in th... |
| MarkForDelete | bit |  |  | SI | - |
| MsgParRef | varchar |  |  | SI | - |
| ParRef | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| RowID | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*