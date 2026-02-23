# SQLUser.SS_UserDefWinContResp

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESP_ParRef | varchar | PK |  | NO | SS_UserDefWindowControls Parent Reference |
| RESP_Childsub | double |  |  | NO | Childsub |
| RESP_ClinPathway_DR | bigint |  | FK | SI | Des Ref ClinPathway |
| RESP_Code | varchar |  |  | SI | Code |
| RESP_ControlGroupExtraValue | varchar |  |  | SI | Control Group Extra Value |
| RESP_ControlGroupValue | varchar |  |  | SI | Control Group Value |
| RESP_DateFrom | date |  |  | SI | DateFrom |
| RESP_DateTo | date |  |  | SI | DateTo |
| RESP_Desc | varchar |  |  | SI | Description |
| RESP_Generated | varchar |  |  | SI | Generated |
| RESP_RowId | varchar |  |  | NO | - |
| RESP_Score | varchar |  |  | SI | Score |
| RESP_Sequence | double |  |  | SI | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*