# Region_CLXX_Reports_QueryManager.Query

**Schema:** Region_CLXX_Reports_QueryManager
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Reportes Regionales**. Informes y estadísticas locales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Description | varchar |  |  | SI | - |
| Document | bit |  |  | SI | - |
| EnabledOnDemand | integer |  |  | NO | - |
| EnabledOnDemandClient | integer |  |  | NO | - |
| EnabledQuery | integer |  |  | NO | - |
| Hospital | integer |  |  | SI | - |
| Name | varchar |  |  | SI | - |
| ParentQuery | bigint |  |  | SI | - |
| Perfilamiento | varchar |  |  | SI | - |
| Profiling | varchar |  |  | SI | - |
| SSGroup | varchar |  |  | SI | - |
| Source | varchar |  |  | NO | - |
| SqlQuery | varchar |  |  | SI | - |
| TimeParameter | integer |  |  | NO | - |
| UserType | integer |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*