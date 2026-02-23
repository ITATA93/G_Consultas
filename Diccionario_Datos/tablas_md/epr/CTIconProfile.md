# epr.CTIconProfile

**Schema:** epr
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Code | varchar |  |  | NO | - |
| CodeTableIcons | bit |  |  | SI | - |
| Description | varchar |  |  | NO | - |
| FixedIconPositions | bit |  |  | SI | - |
| MonitorExtraInfo | bit |  |  | SI | include extra monitor stats if set |
| MultiEpisodes | bit |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| ShortDescription | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*