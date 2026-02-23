# Region_CLXX_Reports_QueryManager.Process

**Schema:** Region_CLXX_Reports_QueryManager
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Reportes Regionales**. Informes y estadísticas locales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Active | integer |  |  | SI | - |
| DayOfMonth | varchar |  |  | SI | - |
| DayOfWeek | varchar |  |  | SI | - |
| ExtractionPeriod | varchar |  |  | NO | - |
| Frecuency | varchar |  |  | SI | - |
| FrequencyString | varchar |  |  | SI | - |
| InternalExecution | varchar |  |  | NO | - |
| LastEnd | timestamp |  |  | SI | - |
| LastInit | timestamp |  |  | SI | - |
| Maxofsavedfiles | integer |  |  | SI | - |
| NameSpace | varchar |  |  | SI | - |
| Query | bigint |  |  | SI | - |
| TaskID | varchar |  |  | SI | - |
| TimeExecution | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*