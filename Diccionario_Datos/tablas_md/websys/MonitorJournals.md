# websys.MonitorJournals

> "Capture, Store and report journal size.<br/>

**Schema:** websys
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Capture, Store and report journal size.<br/>

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CreationTime | varchar |  |  | SI | - |
| Name | varchar |  |  | SI | - |
| Reason | varchar |  |  | SI | - |
| RunDate | date |  |  | SI | Date this run was started
RunDate and RunTime uni... |
| RunTime | time |  |  | SI | Time this run was started
RunDate and RunTime uni... |
| Size | integer |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*