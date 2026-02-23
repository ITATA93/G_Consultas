# web_Msg.LBC_TestSetRevisionReportingRules

**Schema:** web_Msg
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTSRRR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRRR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRRR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRRR_FooterClass | varchar |  |  | SI | Test Set Footer Class |
| LBCTSRRR_HeaderClass | varchar |  |  | SI | Test Set Header Class |
| LBCTSRRR_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCTSRRR_ParRef | bigint |  |  | SI | Parent Reference to LBCTestSetRevision |
| LBCTSRRR_RowID | varchar |  |  | SI | - |
| LBCTSRRR_SuppressMethod | varchar |  |  | SI | Suppress Test Method in Result Block |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*