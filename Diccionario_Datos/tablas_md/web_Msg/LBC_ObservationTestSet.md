# web_Msg.LBC_ObservationTestSet

**Schema:** web_Msg
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCOTS_ParRef | bigint |  |  | SI | Parent table
Required by User.LBCObservationTestS... |
| LBCOTS_RowID | varchar |  |  | SI | - |
| LBCOTS_TestSet_DR | bigint |  | FK | SI | Lab test set associated with this cross reference |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*