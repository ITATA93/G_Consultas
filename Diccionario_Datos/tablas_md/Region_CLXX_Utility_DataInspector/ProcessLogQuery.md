# Region_CLXX_Utility_DataInspector.ProcessLogQuery

**Schema:** Region_CLXX_Utility_DataInspector
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| IntProcess | bigint |  |  | SI | - |
| SchemaQuery | varchar |  |  | SI | - |
| SqlSchemaName | varchar |  |  | SI | - |
| TableQuery | varchar |  |  | SI | - |
| TableToSearch | varchar |  |  | SI | - |
| TableToSearchRowId | varchar |  |  | SI | - |
| ValueToSelect | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*