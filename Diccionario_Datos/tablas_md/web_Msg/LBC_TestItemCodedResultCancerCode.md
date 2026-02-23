# web_Msg.LBC_TestItemCodedResultCancerCode

**Schema:** web_Msg
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTICRCC_CancerCode_DR | bigint |  | FK | SI | - |
| LBCTICRCC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTICRCC_DefaultValue | varchar |  |  | SI | - |
| LBCTICRCC_ParRef | varchar |  |  | SI | - |
| LBCTICRCC_RowID | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*