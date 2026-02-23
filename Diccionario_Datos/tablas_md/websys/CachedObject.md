# websys.CachedObject

> Class to store temporary cached episode-based data

**Schema:** websys
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Class to store temporary cached episode-based data

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Data | varchar |  |  | SI | - |
| EpisodeID | bigint |  |  | NO | - |
| ObjectID | varchar |  |  | NO | - |
| ObjectType | varchar |  |  | NO | - |
| PatientID | bigint |  |  | NO | - |
| PrefContext | varchar |  |  | SI | - |
| PrefLevel | varchar |  |  | SI | - |
| PrefValue | varchar |  |  | SI | - |
| TimeCreated | varchar |  |  | SI | - |
| UserCreated | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*