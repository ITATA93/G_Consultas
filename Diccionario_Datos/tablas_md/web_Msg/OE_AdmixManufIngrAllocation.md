# web_Msg.OE_AdmixManufIngrAllocation

**Schema:** web_Msg
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AMIA_AdmixAdditiveAllocation_DR | varchar |  | FK | SI | Des Ref OEAdmix |
| AMIA_Childsub | double |  |  | SI | Childsub |
| AMIA_ExtStkBatchID | varchar |  |  | SI | External Stock BatchID |
| AMIA_ExtStkDetails | varchar |  |  | SI | External Stock Details |
| AMIA_INCIRN_DR | varchar |  | FK | SI | Des Ref INCItmRegNo |
| AMIA_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| AMIA_ParRef | varchar |  |  | SI | OE_AdmixManufIngr Parent Reference
Required by Us... |
| AMIA_Quantity | double |  |  | SI | Quantity |
| AMIA_RowId | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*