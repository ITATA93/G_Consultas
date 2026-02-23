# lab.CT_ClientsReportsSchedule

**Schema:** lab
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCLA_ParRef | varchar | PK |  | NO | CT_ClientsReports Parent Reference |
| CTCLA_Interval | varchar |  |  | SI | Interval |
| CTCLA_IntervalDate | varchar |  |  | SI | Interval Date |
| CTCLA_IntervalTime | time |  |  | SI | Interval Time |
| CTCLA_Parameters | varchar |  |  | SI | Parameters |
| CTCLA_PrintFinishedDate | date |  |  | SI | Print Finished Date |
| CTCLA_PrintFinishedTime | time |  |  | SI | Print Finished Time |
| CTCLA_PrintStartedDate | date |  |  | SI | Print Started Date |
| CTCLA_PrintStartedTime | time |  |  | SI | Print Started Time |
| CTCLA_RowID | varchar |  |  | NO | - |
| CTCLA_Sequence | numeric |  |  | NO | Sequence |
| CTCLA_TimeFinish | time |  |  | SI | Time Finish |
| CTCLA_TimeStart | time |  |  | SI | Time Start |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*