# lab.CT_ICD10RulesDefinition

**Schema:** lab
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTICDB_ParRef | varchar | PK |  | NO | CT_ICD10Rules Parent Reference |
| CTICDB_CTICD10High_DR | varchar |  | FK | SI | CT ICD10 High DR |
| CTICDB_CTICD10Low_DR | varchar |  | FK | SI | CT ICD10 Low DR |
| CTICDB_CTICD10Normal_DR | varchar |  | FK | SI | CT ICD10 Normal DR |
| CTICDB_CTICD10_DR | varchar |  | FK | SI | CT ICD10 DR |
| CTICDB_ConditionTestItemDR | varchar |  | FK | SI | Condition Test Item DR |
| CTICDB_ConditionType | varchar |  |  | SI | Condition Type |
| CTICDB_ConditionValue | varchar |  |  | SI | Condition Value |
| CTICDB_ElseCTICD10High_DR | varchar |  | FK | SI | Else ICD10 High DR |
| CTICDB_ElseCTICD10Low_DR | varchar |  | FK | SI | ICD10 Low DR |
| CTICDB_ElseCTICD10Normal_DR | varchar |  | FK | SI | ICD10 Normal DR |
| CTICDB_ElseCTICD10_DR | varchar |  | FK | SI | Else ICD10 DR |
| CTICDB_ElseRuleType | varchar |  |  | SI | Else Rule Type |
| CTICDB_ElseTestItemDR | varchar |  | FK | SI | Else Test Item DR |
| CTICDB_Order | double |  |  | NO | Order |
| CTICDB_RowID | varchar |  |  | NO | - |
| CTICDB_RuleType | varchar |  |  | SI | Rule Type |
| CTICDB_TestItem_DR | varchar |  | FK | SI | Test Item DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*