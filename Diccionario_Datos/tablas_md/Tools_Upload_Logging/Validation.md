# Tools_Upload_Logging.Validation

**Schema:** Tools_Upload_Logging
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RunDetailParRef | bigint | PK |  | NO | - |
| ErrorMessage | varchar |  |  | SI | - |
| FailedColumn | varchar |  |  | SI | - |
| FailedContent | varchar |  |  | SI | - |
| FailedRow | integer |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LogType | varchar |  |  | SI | ERR    for Validation Errors
CNT    for Line/Save... |
| LoggingDate | date |  |  | SI | - |
| LoggingTime | time |  |  | SI | - |
| Message | varchar |  |  | SI | - |
| Solved | varchar |  |  | SI | - |
| ValidationColumn | varchar |  |  | SI | - |
| ValidationRow | integer |  |  | SI | - |
| ValidationType | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*