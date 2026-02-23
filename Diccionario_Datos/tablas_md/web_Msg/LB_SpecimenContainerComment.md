# web_Msg.LB_SpecimenContainerComment

**Schema:** web_Msg
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Muestras de Laboratorio**. Gestión de especímenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBRSPCCRowID | varchar |  |  | SI | - |
| LBSPCC_ParRef | bigint |  |  | SI | Parent |
| LBSPCC_Reportable | varchar |  |  | SI | Reportable |
| LBSPCC_RowID | varchar |  |  | SI | - |
| LBSPCC_SpecimenComment_DR | bigint |  | FK | SI | Comment |
| LBSpecimenContainerMsg_DR | varchar |  | FK | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*