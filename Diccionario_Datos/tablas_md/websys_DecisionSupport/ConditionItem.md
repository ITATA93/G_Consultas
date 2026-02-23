# websys_DecisionSupport.ConditionItem

**Schema:** websys_DecisionSupport
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | varchar | PK |  | NO | - |
| BooleanOperator | varchar |  |  | SI | - |
| ConditionBetweenValue | varchar |  |  | SI | - |
| ConditionOperator | varchar |  |  | SI | Use 'DSSConditionalOperator' standard Type |
| ConditionProperty | varchar |  |  | SI | - |
| ConditionValue | varchar |  |  | SI | - |
| ConditionValueList | bigint |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| MainProperty | varchar |  |  | SI | Use to define which one is the main property in th... |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*