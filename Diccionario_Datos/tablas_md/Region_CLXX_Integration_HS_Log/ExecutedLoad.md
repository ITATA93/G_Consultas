# Region_CLXX_Integration_HS_Log.ExecutedLoad

**Schema:** Region_CLXX_Integration_HS_Log
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Integración Health Share**. Conexión con sistema de interoperabilidad.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ClassName | varchar |  |  | SI | - |
| CreatedBy | varchar |  |  | NO | - |
| CreationDate | timestamp |  |  | NO | - |
| ExecStatus | varchar |  |  | SI | - |
| ExecutedFrom | varchar |  |  | SI | - |
| FinishingDate | timestamp |  |  | SI | - |
| FromDate | timestamp |  |  | SI | - |
| JobID | integer |  |  | SI | - |
| ToDate | timestamp |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*