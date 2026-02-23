# web_Msg.LB_BloodProductBulkEdit

**Schema:** web_Msg
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBBPBE_ConversionBPIdList | varchar |  |  | SI | Conversion Blood Product ID List |
| LBBPBE_PresumedTransfusionDate | date |  |  | SI | Presumed Transfusion Date |
| LBBPBE_PresumedTransfusionTime | time |  |  | SI | Presumed Transfusion Time |
| LBBPBE_Print | varchar |  |  | SI | Print |
| LBBPBE_isBPConversion | varchar |  |  | SI | Whether this message represents a Blood Product Co... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*