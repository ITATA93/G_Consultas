# SQLUser.PA_PersonConsultSetCons

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONS_ParRef | varchar | PK |  | NO | PA_PersonConsultSet Parent Reference |
| CONS_APPT_DR | varchar |  | FK | SI | Des Ref APPT |
| CONS_CTPCP_DR | varchar |  | FK | SI | Des Ref CTPCP |
| CONS_Childsub | double |  |  | NO | Childsub |
| CONS_EndDate | date |  |  | SI | EndDate |
| CONS_EndTime | time |  |  | SI | EndTime |
| CONS_FollowupOrder_DR | varchar |  | FK | SI | Des Ref FollowupOrder |
| CONS_Notes | varchar |  |  | SI | Notes |
| CONS_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| CONS_PreviousConsult_DR | varchar |  | FK | SI | Des Ref PreviousConsult |
| CONS_RowId | varchar |  |  | NO | - |
| CONS_Significant | varchar |  |  | SI | Significant |
| CONS_Status | varchar |  |  | SI | Status |
| CONS_VisitDate | date |  |  | SI | VisitDate |
| CONS_VisitTime | time |  |  | SI | VisitTime |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*