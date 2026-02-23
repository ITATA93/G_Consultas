# SQLUser.PA_PathwayItemGoal

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Datos de Paciente**. Información demográfica y administrativa. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATHIG_ParRef | varchar | PK |  | NO | Parent Reference |
| PATHIG_Childsub | double |  |  | NO | Childsub |
| PATHIG_Desc | varchar |  |  | SI | Description |
| PATHIG_FreeText | varchar |  |  | SI | Condition - Free-text |
| PATHIG_FreeTextCondAchieved | bit |  |  | SI | Condition - Free-text |
| PATHIG_NursingOutcomeThreshold | integer |  |  | SI | Condition - Nursing Outcome Threshold from five-po... |
| PATHIG_NursingOutcome_DR | bigint |  | FK | SI | Condition - Nursing Outcome |
| PATHIG_PHFreq_DR | bigint |  | FK | SI | Frequency |
| PATHIG_Period | integer |  |  | SI | Period - Time from the beginning of the pathway by... |
| PATHIG_PeriodType | varchar |  |  | SI | Period duration type |
| PATHIG_ProtItemGoal_DR | varchar |  | FK | SI | Protocol Item that this is derived from |
| PATHIG_RowId | varchar |  |  | NO | - |
| PATHIG_VisualRule_DR | bigint |  | FK | SI | Condition - Visual Rule |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*