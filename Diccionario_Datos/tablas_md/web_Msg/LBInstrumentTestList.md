# web_Msg.LBInstrumentTestList

**Schema:** web_Msg
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| HideQCValues | varchar |  |  | SI | - |
| HideUnlinkedResults | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LBCInstrument | bigint |  |  | SI | - |
| LBCInstrumentTestGroupID | varchar |  |  | SI | - |
| LabSite | bigint |  |  | SI | - |
| LastPage | bit |  |  | SI | - |
| PageNumber | varchar |  |  | SI | - |
| PageSize | integer |  |  | SI | - |
| PerformedOnInstrument | bigint |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| ReasonHeld | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| hiddenInstrumentFlagTypeList | varchar |  |  | SI | - |
| hiddenResultAbnormalFlagList | varchar |  |  | SI | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*