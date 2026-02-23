# web_Msg.LB_QCRun

**Schema:** web_Msg
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBQCR_InstrumentGroup_DR | bigint |  | FK | SI | Instrument Group |
| LBQCR_Instrument_DR | bigint |  | FK | SI | Instrument |
| LBQCR_Reagents | varchar |  |  | SI | Reagents used for this QC run |
| LBQCR_RowID | varchar |  |  | SI | - |
| LBQCR_SequenceNumber | numeric |  |  | SI | Run Number |
| LBQCR_StartDate | date |  |  | SI | Start Date |
| LBQCR_StartTime | time |  |  | SI | Start Time |
| LBQCR_Status | varchar |  |  | SI | Run Status
StandardType: LabQCRunStatus |
| LBQCR_WorksheetGroup_DR | bigint |  | FK | SI | Worksheet Group |
| LBQCR_Worksheet_DR | bigint |  | FK | SI | Worksheet |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*