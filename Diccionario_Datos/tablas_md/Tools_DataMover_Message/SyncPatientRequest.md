# Tools_DataMover_Message.SyncPatientRequest

**Schema:** Tools_DataMover_Message
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| EpisodeNumber | varchar |  |  | SI | Episode based update |
| IncludeEpisodeTransactions | bit |  |  | SI | - |
| RegistrationNumber | varchar |  |  | SI | Patients number required to update |
| SyncUsername | varchar |  |  | SI | - |
| TrakProcessGUID | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*