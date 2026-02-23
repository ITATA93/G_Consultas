# web_Msg.OE_AdmixManufIngrAllocAddnBatch

**Schema:** web_Msg
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AMIAAB_Childsub | double |  |  | SI | Childsub |
| AMIAAB_ExtStkBatchID | varchar |  |  | SI | External Stock BatchID |
| AMIAAB_ExtStkDetails | varchar |  |  | SI | External Stock Details |
| AMIAAB_INCIRN_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| AMIAAB_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| AMIAAB_ParRef | varchar |  |  | SI | OE_OrdAdmixAllocation Parent Reference
Required b... |
| AMIAAB_Quantity | double |  |  | SI | Quantity |
| AMIAAB_RowId | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*