# web_Msg.OE_AdmixManufIngrAddnBatch

**Schema:** web_Msg
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| BAT_Childsub | double |  |  | SI | Childsub |
| BAT_ExtStkBatchID | varchar |  |  | SI | External Stock BatchID |
| BAT_ExtStkDetails | varchar |  |  | SI | External Stock Details |
| BAT_INCIRN_DR | varchar |  | FK | SI | Des Ref INCItmRegNo |
| BAT_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| BAT_ParRef | varchar |  |  | SI | OE_OrdAdmix Parent Reference
Required by User.OEA... |
| BAT_Quantity | double |  |  | SI | Quantity |
| BAT_RowId | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*