# SQLUser.LB_QCBracketResult

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBQCBRE_ParRef | bigint | PK |  | NO | - |
| LBQCBRE_InstrumentResult_DR | varchar |  | FK | SI | Instrument Test Item Result |
| LBQCBRE_RowID | varchar |  |  | NO | - |
| LBQCBRE_TestSetItems | varchar |  |  | SI | List of test sets items for this bracket |
| LBQCBRE_TestSets | varchar |  |  | SI | List of test sets for this bracket - derived from ... |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*