# Region_CLXX_Reports_REMManager.ReportExecution_Data

**Schema:** Region_CLXX_Reports_REMManager
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Reportes Regionales**. Informes y estadísticas locales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ReportExecution | bigint | PK |  | NO | Parent reference |
| Data | bigint |  |  | SI | Data |
| ID | varchar |  |  | NO | - |
| element_key | varchar |  |  | NO | Data array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*