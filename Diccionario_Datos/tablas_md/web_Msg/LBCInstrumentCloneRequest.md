# web_Msg.LBCInstrumentCloneRequest

**Schema:** web_Msg
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AlphaCounter | bit |  |  | SI | - |
| BaseCode | varchar |  |  | SI | - |
| CloneProduction | bit |  |  | SI | - |
| CounterStart | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| InboundRuleClassName | varchar |  |  | SI | - |
| NumClones | integer |  |  | SI | - |
| OutboundRuleClassName | varchar |  |  | SI | - |
| ProductionClassName | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SourceInstrumentDesc | bigint |  |  | SI | Instrument to be cloned |
| TransformReplyRuleClassName | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*