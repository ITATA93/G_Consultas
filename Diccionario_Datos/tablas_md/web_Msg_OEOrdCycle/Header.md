# web_Msg_OEOrdCycle.Header

**Schema:** web_Msg_OEOrdCycle
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AsProtocol | bit |  |  | SI | As Protocol |
| ChangeType | varchar |  |  | SI | "CYC"LE or "CAL"ENDAR |
| Changed | bit |  |  | SI | indicates that the cycle has changed.  Replaces wh... |
| DoseChanged | bit |  |  | SI | dose has changed |
| FrequencyChanged | bit |  |  | SI | freq has changed |
| ID | varchar |  |  | NO | - |
| OrderID | varchar |  |  | SI | Des Ref to OEOrdItem |
| OtherID | varchar |  |  | SI | string to store non-OrderID - for medhx, medrec, e... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SetCustomFreqCycle | bit |  |  | SI | Set Custom Freq Cycle |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*