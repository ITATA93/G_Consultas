# web_Msg.LBC_DynamicFunctionTestSlot

**Schema:** web_Msg
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCDFTS_ParRef | bigint |  |  | SI | Parent table
Required by User.LBCDynamicFunctionT... |
| LBCDFTS_RowID | varchar |  |  | SI | - |
| LBCDFTS_Sequence | double |  |  | SI | Slot sequence number within the dynamic function t... |
| LBCDFTS_TestItems | varchar |  |  | SI | Test items associated with this slot
List of poss... |
| LBCDFTS_TestSets | varchar |  |  | SI | Test sets associated with this slot
List of possi... |
| LBCDFTS_TimeOffset | integer |  |  | SI | Slot offset time 
for this slot from start/openin... |
| LBCDFTS_TimeWindow | integer |  |  | SI | Slot time window
for this slot. Tolerance interva... |
| LBCDFTS_UseTIRanges | varchar |  |  | SI | Use Test Item Ranges for this slot |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*