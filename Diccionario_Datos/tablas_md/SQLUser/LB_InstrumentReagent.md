# SQLUser.LB_InstrumentReagent

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBIR_RowID | bigint | PK |  | NO | - |
| ChildQ162DR | - |  |  | SI | Child Reference: Otras evaluaciones del Nervio Ópt... |
| LBIR_Active | varchar |  |  | SI | Active |
| LBIR_InstrumentEvent_DR | bigint |  | FK | SI | Associated instrument event |
| LBIR_InstrumentReagent_DR | varchar |  | FK | SI | Intrument reagent |
| LBIR_Instrument_DR | bigint |  | FK | NO | Instrument |
| LBIR_ReagentBatch_DR | bigint |  | FK | SI | Reagent batch |
| Q160Q1 | - |  |  | SI | Ojos |
| Q160Q2 | - |  |  | SI | Evaluación |
| Q160Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*