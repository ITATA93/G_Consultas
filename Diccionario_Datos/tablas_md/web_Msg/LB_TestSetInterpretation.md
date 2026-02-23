# web_Msg.LB_TestSetInterpretation

**Schema:** web_Msg
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBTSINT_AppEventRule_DR | bigint |  | FK | SI | Interpretation App Event Rule |
| LBTSINT_Document_DR | bigint |  | FK | SI | Link to a websys.Document that stores the formated... |
| LBTSINT_Index | varchar |  |  | SI | Index of Interpretation within app event rule list... |
| LBTSINT_Interpretation_DR | bigint |  | FK | SI | Link to the interpretation |
| LBTSINT_ParRef | bigint |  |  | SI | Parent TestSet DR
Required by User.LBTestSetInter... |
| LBTSINT_Reportable | varchar |  |  | SI | Reportable flag |
| LBTSINT_RowID | varchar |  |  | SI | - |
| LBTSINT_SourceType | varchar |  |  | SI | Interpetation Source |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*