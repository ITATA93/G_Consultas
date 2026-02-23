# web_Msg.LB_Protocol

**Schema:** web_Msg
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBPT_Episode_DR | bigint |  | FK | SI | Episode |
| LBPT_Protocol_DR | bigint |  | FK | SI | Protocol |
| LBPT_RowID | varchar |  |  | SI | - |
| LBPT_SpecimenContainer_DR | bigint |  | FK | SI | Specimen Container |
| LBPT_Status | varchar |  |  | SI | Status |
| LBPT_TestSet_DR | bigint |  | FK | SI | Test Set |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*