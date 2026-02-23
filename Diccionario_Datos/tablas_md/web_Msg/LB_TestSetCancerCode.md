# web_Msg.LB_TestSetCancerCode

**Schema:** web_Msg
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AddedByTIComment_DR | varchar |  | FK | SI | Not stored in the User class, used to indicate whi... |
| ID | varchar |  |  | NO | - |
| LBTSCC_CancerCode_DR | bigint |  | FK | SI | - |
| LBTSCC_ParRef | bigint |  |  | SI | - |
| LBTSCC_RowID | varchar |  |  | SI | - |
| LBTSCC_Value | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*