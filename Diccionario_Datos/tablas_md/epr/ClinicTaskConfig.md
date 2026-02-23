# epr.ClinicTaskConfig

**Schema:** epr
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Configuración del módulo.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TASKCF_RowId | bigint | PK |  | NO | - |
| TASKCF_ApplyConfig | varchar |  |  | SI | Apply the configuration Flag |
| TASKCF_BedCol | varchar |  |  | SI | Bed Column |
| TASKCF_GrpNum | double |  |  | SI | Max number of groups |
| TASKCF_IconProf | varchar |  |  | SI | Icon Profile Flag |
| TASKCF_NameCol | varchar |  |  | SI | Name Column |
| TASKCF_Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| TASKCF_TimeRange | double |  |  | SI | Time range |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*