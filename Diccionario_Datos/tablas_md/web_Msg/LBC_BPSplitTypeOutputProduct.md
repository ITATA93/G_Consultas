# web_Msg.LBC_BPSplitTypeOutputProduct

**Schema:** web_Msg
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCBPSTOP_BloodProduct_DR | bigint |  | FK | SI | Blood Product
Required by User.LBCBPSplitTypeOutp... |
| LBCBPSTOP_ExpiryOffset | integer |  |  | SI | Default expiry offset of the newly created blood p... |
| LBCBPSTOP_ExpiryOffsetUnit | varchar |  |  | SI | Unit of the default expiry offset of the newly cre... |
| LBCBPSTOP_ParRef | bigint |  |  | SI | Parent Split Type |
| LBCBPSTOP_RowID | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*