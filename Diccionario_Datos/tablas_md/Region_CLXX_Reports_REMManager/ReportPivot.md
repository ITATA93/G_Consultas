# Region_CLXX_Reports_REMManager.ReportPivot

**Schema:** Region_CLXX_Reports_REMManager
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Reportes Regionales**. Informes y estadísticas locales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| PivotDef | bigint |  |  | SI | - |
| PivotOrder | integer |  |  | SI | - |
| PivotSubGroup | varchar |  |  | SI | - |
| PvtDef | bigint |  |  | SI | - |
| ReportDef | bigint |  |  | SI | - |
| ReportParentPivot | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*