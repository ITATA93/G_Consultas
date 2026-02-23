# web_Msg.OE_AdmixManufIngr

**Schema:** web_Msg
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| INGR_AdjustedAmount | double |  |  | SI | Adjusted Amount |
| INGR_AdmixAdditive_DR | varchar |  | FK | SI | Des Ref OEAdmixAdditive |
| INGR_Admix_DR | bigint |  | FK | SI | Des Ref OEAdmix |
| INGR_Childsub | double |  |  | SI | Childsub |
| INGR_ExtDispenseID | varchar |  |  | SI | External DispenseID |
| INGR_ExtStkBatchID | varchar |  |  | SI | External Stock BatchID |
| INGR_ExtStkDetails | varchar |  |  | SI | External Stock Details |
| INGR_INCIRN_DR | varchar |  | FK | SI | Des Ref INCItmRegNo |
| INGR_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| INGR_ParRef | varchar |  |  | SI | OE_AdmixManuf Parent Reference
Required by User.O... |
| INGR_Quantity | double |  |  | SI | Quantity |
| INGR_ReqQuantity | double |  |  | SI | Required Quantity |
| INGR_RowId | varchar |  |  | SI | - |
| INGR_WardDispense | varchar |  |  | SI | Ward Dispense |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*