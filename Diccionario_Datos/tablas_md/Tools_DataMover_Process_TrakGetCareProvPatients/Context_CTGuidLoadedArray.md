# Tools_DataMover_Process_TrakGetCareProvPatients.Context_CTGuidLoadedArray

**Schema:** Tools_DataMover_Process_TrakGetCareProvPatients
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Contexto**. Datos de contexto de sesión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| Context | bigint | PK |  | NO | Parent reference |
| CTGuidLoadedArray | varchar |  |  | SI | CTGuidLoadedArray |
| ID | varchar |  |  | NO | - |
| element_key | varchar |  |  | NO | CTGuidLoadedArray array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*