# web_Msg.LB_QCReview

**Schema:** web_Msg
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBQCRE_Comments | varchar |  |  | SI | Review comments |
| LBQCRE_CorrectiveAction_DR | bigint |  | FK | SI | Review Corrective Action |
| LBQCRE_Date | date |  |  | SI | Review Date |
| LBQCRE_RootCause_DR | bigint |  | FK | SI | Review Root Cause |
| LBQCRE_RowID | varchar |  |  | SI | - |
| LBQCRE_RunData | varchar |  |  | SI | List of run data included in review  |
| LBQCRE_Time | time |  |  | SI | Review Time |
| LBQCRE_Type_DR | bigint |  | FK | SI | Review Type |
| LBQCRE_User_DR | bigint |  | FK | SI | Review User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*