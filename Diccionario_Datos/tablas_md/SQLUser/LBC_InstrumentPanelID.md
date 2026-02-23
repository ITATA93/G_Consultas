# SQLUser.LBC_InstrumentPanelID

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINPI_ParRef | bigint | PK |  | NO | Parent instrument test group DR |
| LBCINPI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINPI_OutboundInstrumentPanelIDs | varchar |  |  | SI | Outbound Instrument Panel IDs |
| LBCINPI_RowID | varchar |  |  | NO | - |
| LBCINPI_TestSet_DR | bigint |  | FK | SI | Test Set |
| Q59Q1 | - |  |  | SI | Date |
| Q59Q2 | - |  |  | SI | Time |
| Q59Q3 | - |  |  | SI | Done by |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*