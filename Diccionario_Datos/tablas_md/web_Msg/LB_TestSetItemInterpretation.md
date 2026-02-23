# web_Msg.LB_TestSetItemInterpretation

**Schema:** web_Msg
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBTSII_AppEventRule_DR | bigint |  | FK | SI | Interpretation App Event Rule |
| LBTSII_Document_DR | bigint |  | FK | SI | Link to a websys.Document that stores the formated... |
| LBTSII_Index | varchar |  |  | SI | Index of Interpretation within app event rule list... |
| LBTSII_Interpretation_DR | bigint |  | FK | SI | Link to the interpretation |
| LBTSII_ParRef | varchar |  |  | SI | Parent TestSet DR
Required by User.LBTestSetItemI... |
| LBTSII_Reportable | varchar |  |  | SI | Reportable flag |
| LBTSII_RowID | varchar |  |  | SI | - |
| LBTSII_SourceType | varchar |  |  | SI | Interpetation Source |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*