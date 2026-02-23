# Tools_DataMover_Process.TrakSyncPendingPatients_MessagesReceived

**Schema:** Tools_DataMover_Process
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TrakSyncPendingPatients | bigint | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| MessagesReceived | varchar |  |  | SI | MessagesReceived |
| element_key | varchar |  |  | NO | %MessagesReceived array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*