# Region_CLXX_Reports_REMManager.Process

**Schema:** Region_CLXX_Reports_REMManager
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Reportes Regionales**. Informes y estadísticas locales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Active | integer |  |  | SI | - |
| BaseDataExtraction | bigint |  |  | SI | - |
| DayOfMonth | varchar |  |  | SI | - |
| DayOfWeek | varchar |  |  | SI | - |
| EndDate | timestamp |  |  | SI | - |
| ExecQMExtract | integer |  |  | SI | - |
| ExtractionPeriod | varchar |  |  | SI | - |
| Frecuency | varchar |  |  | SI | - |
| FrequencyString | varchar |  |  | SI | - |
| GenReports | integer |  |  | SI | - |
| InitDate | timestamp |  |  | NO | - |
| LastUserUpdate | varchar |  |  | SI | - |
| MaxOfSavedDates | integer |  |  | SI | - |
| Maxofsavedreports | integer |  |  | SI | - |
| NameSpace | varchar |  |  | SI | - |
| ProcessDataExt | bigint |  |  | SI | - |
| SqlTable | varchar |  |  | SI | - |
| Status | integer |  |  | SI | - |
| TaskID | varchar |  |  | SI | - |
| TimeExecution | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*