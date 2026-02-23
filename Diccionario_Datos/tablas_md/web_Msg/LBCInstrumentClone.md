# web_Msg.LBCInstrumentClone

**Schema:** web_Msg
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ArchiveDirectory | varchar |  |  | SI | - |
| ArchiveDirectoryOut | varchar |  |  | SI | - |
| CloneProduction | bit |  |  | SI | - |
| Code | varchar |  |  | SI | New Instrument Code |
| ControlledByInstrument | bigint |  |  | SI | - |
| Department | bigint |  |  | SI | - |
| Description | varchar |  |  | SI | New Instrument Description |
| Directory | varchar |  |  | SI | - |
| DirectoryOut | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| IPAddress | varchar |  |  | SI | - |
| InboundRuleClassName | varchar |  |  | SI | - |
| InstrumentGroup | bigint |  |  | SI | - |
| InstrumentType | varchar |  |  | SI | - |
| LabSiteDR | bigint |  | FK | SI | New Instrument Lab Site (Location) |
| MiddlewareInstrumentID | varchar |  |  | SI | - |
| OldCode | varchar |  |  | SI | Old Instrument Code |
| OutboundRuleClassName | varchar |  |  | SI | - |
| Port | varchar |  |  | SI | - |
| ProdConfigType | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SourceInstrumentDR | bigint |  | FK | SI | - |
| Suffix | varchar |  |  | SI | - |
| TransformReplyRuleClassName | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*