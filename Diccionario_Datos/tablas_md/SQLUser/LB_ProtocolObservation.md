# SQLUser.LB_ProtocolObservation

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBPTO_ParRef | bigint | PK |  | NO | Parent Reference |
| LBPTO_AddOnBy_DR | bigint |  | FK | SI | User who add unplanned |
| LBPTO_AddOnDate | date |  |  | SI | Add-on Date
Date when procedure was added unplann... |
| LBPTO_AddOnTime | time |  |  | SI | Add-on Time
Time when procedure was added unplann... |
| LBPTO_CompletedBy_DR | bigint |  | FK | SI | User who completed |
| LBPTO_CompletedDate | date |  |  | SI | Completed Date
Date when observation was complete... |
| LBPTO_CompletedTime | time |  |  | SI | Completed Time
Time when observation was complete... |
| LBPTO_Note | longvarchar |  |  | SI | Standard Note against this observation
HTMLRichTe... |
| LBPTO_Observation_DR | bigint |  | FK | SI | Observation |
| LBPTO_Planned | bit |  |  | SI | Planned
Is this material part of the configured p... |
| LBPTO_RowID | varchar |  |  | NO | - |
| LBPTO_Source_DR | varchar |  | FK | SI | Source Material |
| LBPTO_Status | varchar |  |  | SI | Status |
| LBPTO_TestSetItem_DR | varchar |  | FK | SI | Linked test set item 
Links a test set item and i... |
| ProtocolSequence | numeric |  |  | SI | - |
| Q01Q1 | - |  |  | SI | Factores de Riesgo Alto de Daño Familiar y/o Indiv... |
| Q01Q2 | - |  |  | SI | Factores de Riesgo Intermedio de Daño Familiar y/o... |
| Q01Q3 | - |  |  | SI | Factores de Riesgo Bajo de Daño Familiar y/o Indiv... |
| Q01Q4 | - |  |  | SI | Comentarios |
| Q01Q5 | - |  |  | SI | Fecha |
| Q01Q6 | - |  |  | SI | Hora |
| Q01Q7 | - |  |  | SI | Profesional |
| Q01Q8 | - |  |  | SI | CESFAM |
| Q01Q9 | - |  |  | SI | Riego Familiar Evaluado |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*