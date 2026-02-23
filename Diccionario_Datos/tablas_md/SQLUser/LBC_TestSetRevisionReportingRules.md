# SQLUser.LBC_TestSetRevisionReportingRules

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRRR_ParRef | bigint | PK |  | NO | Parent Reference to LBCTestSetRevision |
| ChildQ38DR | - |  |  | SI | Child Reference: Pulmonar Alterado |
| LBCTSRRR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRRR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRRR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRRR_FooterClass | varchar |  |  | SI | Test Set Footer Class |
| LBCTSRRR_HeaderClass | varchar |  |  | SI | Test Set Header Class |
| LBCTSRRR_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCTSRRR_RowID | varchar |  |  | NO | - |
| LBCTSRRR_SuppressMethod | varchar |  |  | SI | Suppress Test Method in Result Block |
| Q30Q1 | - |  |  | SI | Lesión |
| Q30Q2 | - |  |  | SI | Lateralidad |
| Q30Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*