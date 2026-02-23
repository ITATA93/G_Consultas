# web_Msg.LBC_TestSetRevisionMultipleRules

**Schema:** web_Msg
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTSRMR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRMR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRMR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRMR_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCTSRMR_ParRef | bigint |  |  | SI | Parent Reference LBCTestSetRevisionDR |
| LBCTSRMR_RowID | varchar |  |  | SI | - |
| LBCTSRMR_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCTSRMR_SortOrder | varchar |  |  | SI | Sort Order |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*