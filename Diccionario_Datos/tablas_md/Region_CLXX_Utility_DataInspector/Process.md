# Region_CLXX_Utility_DataInspector.Process

**Schema:** Region_CLXX_Utility_DataInspector
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Impresión/Reportes**. Generación de documentos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CSVDirectory | varchar |  |  | SI | - |
| DeleteOrCancelRelatedRecords | varchar |  |  | NO | - |
| EndDate | timestamp |  |  | SI | - |
| ForceDictionaryRegeneration | varchar |  |  | NO | - |
| InitDate | timestamp |  |  | NO | - |
| InspectGlobals | varchar |  |  | NO | - |
| JobPID | integer |  |  | SI | - |
| JobStatus | integer |  |  | SI | - |
| ProcessType | varchar |  |  | SI | - |
| SqlFieldName | varchar |  |  | SI | - |
| SqlSchemaName | varchar |  |  | SI | - |
| SqlTableExcludeList | varchar |  |  | SI | - |
| SqlTableName | varchar |  |  | SI | - |
| State | varchar |  |  | NO | - |
| TotalRecordsDeleted | integer |  |  | SI | - |
| TotalRecordsFound | integer |  |  | SI | - |
| TotalRecordsUpdated | integer |  |  | SI | - |
| ValueCriteria | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*