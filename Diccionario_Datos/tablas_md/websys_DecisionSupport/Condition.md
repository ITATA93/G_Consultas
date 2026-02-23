# websys_DecisionSupport.Condition

**Schema:** websys_DecisionSupport
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| BaseCube | varchar |  |  | SI | - |
| BooleanOperator | varchar |  |  | SI | - |
| ConditionClass | varchar |  |  | SI | - |
| ConditionClassQualifier | varchar |  |  | SI | Qualifiers
Used to reduce the number of rules tha... |
| Description | varchar |  |  | SI | - |
| DoNotTriggerOnClass | bit |  |  | SI | - |
| DoesNotExist | bit |  |  | SI | if true - we check for NO items that satisfy these... |
| Exists | bit |  |  | SI | this is not used now - it really is used just for ... |
| ID | varchar |  |  | NO | - |
| IsDisabled | bit |  |  | SI | - |
| IsLast | bit |  |  | SI | Property to indicate we ONLY consider the most rec... |
| IsPropertyActive | bit |  |  | SI | - |
| Sequence | integer |  |  | SI | - |
| TimeAmount | integer |  |  | SI | - |
| TimeField | varchar |  |  | SI | Time field to use for calculation, eg OEOrdItem->O... |
| TimeUnit | varchar |  |  | SI | - |
| ValuesToConsider | integer |  |  | SI | Number of historical values to consider.   zero (b... |
| WizardType | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*