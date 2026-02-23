# Region_CLXX_Reports_REMManager.ReportExecutionData

**Schema:** Region_CLXX_Reports_REMManager
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Reportes Regionales**. Informes y estadísticas locales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| GlobalRefs | numeric |  |  | SI | - |
| Header | bigint |  |  | SI | - |
| Pivot | bigint |  |  | SI | - |
| PivotData | varchar |  |  | SI | - |
| PivotSubGroup | varchar |  |  | SI | - |
| ReportExecutionID | bigint |  |  | SI | - |
| SqlDetail | varchar |  |  | SI | - |
| TimeElapsed | numeric |  |  | SI | - |
| Value | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*