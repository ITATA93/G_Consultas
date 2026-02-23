# web_Msg.PA_GlobalDisp

**Schema:** web_Msg
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| GDSP_ADMINDateFrom | date |  |  | SI | ADMINDateFrom  |
| GDSP_ADMINDateTo | date |  |  | SI | ADMINDateTo |
| GDSP_ADMINTimeFrom | time |  |  | SI | ADMINTimeFrom  |
| GDSP_ADMINTimeTo | time |  |  | SI | ADMINTimeTo  |
| GDSP_AutoPickBatchID | varchar |  |  | SI | - |
| GDSP_Description | varchar |  |  | SI | Description  |
| GDSP_ExtraQty | double |  |  | SI | ExtraQty  |
| GDSP_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| GDSP_LastUpdateDate | date |  |  | SI | LastUpdateDate  |
| GDSP_LastUpdateHosp_DR | bigint |  | FK | SI | Des Ref CTHospital |
| GDSP_LastUpdateTime | time |  |  | SI | LastUpdateTime   |
| GDSP_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| GDSP_LocStockGlobDisp_DR | varchar |  | FK | SI | Des Ref CTLocStockGlobDisp  |
| GDSP_PharmStatus | varchar |  |  | SI | Pharmacy Status
Required by User.PAGlobalDisp. |
| GDSP_RecLoc_DR | bigint |  | FK | SI |  Receiving Location |
| GDSP_RowId | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*