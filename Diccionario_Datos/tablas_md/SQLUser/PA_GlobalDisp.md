# SQLUser.PA_GlobalDisp

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GDSP_RowId | bigint | PK |  | NO | - |
| GDSP_ADMINDateFrom | date |  |  | SI | ADMINDateFrom  |
| GDSP_ADMINDateTo | date |  |  | SI | ADMINDateTo |
| GDSP_ADMINTimeFrom | time |  |  | SI | ADMINTimeFrom  |
| GDSP_ADMINTimeTo | time |  |  | SI | ADMINTimeTo  |
| GDSP_Description | varchar |  |  | SI | Description  |
| GDSP_ExtraQty | double |  |  | SI | ExtraQty  |
| GDSP_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| GDSP_LastUpdateDate | date |  |  | SI | LastUpdateDate  |
| GDSP_LastUpdateHosp_DR | bigint |  | FK | SI | Des Ref CTHospital |
| GDSP_LastUpdateTime | time |  |  | SI | LastUpdateTime   |
| GDSP_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| GDSP_LocStockGlobDisp_DR | varchar |  | FK | SI | Des Ref CTLocStockGlobDisp  |
| GDSP_PharmStatus | varchar |  |  | NO | Pharmacy Status |
| GDSP_RecLoc_DR | bigint |  | FK | SI |  Receiving Location |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*