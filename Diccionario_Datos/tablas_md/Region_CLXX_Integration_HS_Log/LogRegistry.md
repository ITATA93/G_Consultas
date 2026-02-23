# Region_CLXX_Integration_HS_Log.LogRegistry

**Schema:** Region_CLXX_Integration_HS_Log
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DocumentId | varchar |  |  | SI | - |
| DocumentType | varchar |  |  | SI | - |
| EndGenDate | timestamp |  |  | SI | - |
| ErrorText | varchar |  |  | SI | - |
| IsError | bit |  |  | SI | - |
| PriorityQueueCode | varchar |  |  | SI | - |
| QueuePosition | integer |  |  | SI | - |
| Remarks | varchar |  |  | SI | - |
| SendingDate | timestamp |  |  | SI | - |
| Size | integer |  |  | SI | - |
| StartGenDate | timestamp |  |  | SI | - |
| StreamQueuePosition | integer |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*