# web_Msg.LB_SecurityAccessRule

**Schema:** web_Msg
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBSAR_AccessConfidentialResult | bit |  |  | SI | - |
| LBSAR_AccessNonFinalResult | bit |  |  | SI | - |
| LBSAR_Department_DR | bigint |  | FK | SI | - |
| LBSAR_EditEpisode | bit |  |  | SI | - |
| LBSAR_EditStaffNote | bit |  |  | SI | - |
| LBSAR_EditTestSet | bit |  |  | SI | - |
| LBSAR_LabSite_DR | bigint |  | FK | SI | - |
| LBSAR_Sequence | numeric |  |  | SI | - |
| LBSAR_SubjectType_DR | bigint |  | FK | SI | - |
| LBSAR_ViewConfidentialEpisode | bit |  |  | SI | - |
| LBSAR_ViewConfidentialTestSet | bit |  |  | SI | - |
| LBSAR_ViewEpisode | bit |  |  | SI | - |
| LBSAR_ViewNonFinalTransferred | bit |  |  | SI | - |
| LBSAR_ViewStaffNote | bit |  |  | SI | - |
| LBSAR_ViewTestItemHistory | bit |  |  | SI | - |
| LBSAR_ViewTestSet | bit |  |  | SI | - |
| LBSAR_ViewTransferred | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*