# web_Msg.PA_ProblemCarePlan

**Schema:** web_Msg
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| PAPCP_Comments | varchar |  |  | SI | - |
| PAPCP_EndDate | date |  |  | SI | - |
| PAPCP_EndTime | time |  |  | SI | - |
| PAPCP_NRCProblem_DR | bigint |  | FK | SI | Des Ref to Problem |
| PAPCP_OnsetDate | date |  |  | SI | - |
| PAPCP_OnsetTime | time |  |  | SI | - |
| PAPCP_PatMas_DR | bigint |  | FK | SI | - |
| PAPCP_PathwayItem_DR | varchar |  | FK | SI | Des Ref to PAPathwayItem, pathway item |
| PAPCP_ProblemID | varchar |  |  | SI | - |
| PAPCP_RelatedConcepts_DR | varchar |  | FK | SI | DR to Code Table Related Concept - User.NRCProblem... |
| PAPCP_RowID | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*