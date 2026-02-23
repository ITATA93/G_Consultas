# web_Msg.ARBillingItemList

**Schema:** web_Msg
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ARCBillingScheduleRevisionTariffID | varchar |  |  | SI | - |
| DateOfService | date |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| InpatientBillingFlag | varchar |  |  | SI | - |
| LBEpisodeNo | varchar |  |  | SI | - |
| MRN | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| Status | varchar |  |  | SI | - |
| URN | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*