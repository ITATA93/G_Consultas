# Region_CLXX_Reports_REMManager.ReportHeader

**Schema:** Region_CLXX_Reports_REMManager
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Reportes Regionales**. Informes y estadísticas locales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HdrDef | bigint |  |  | SI | - |
| HeaderDef | bigint |  |  | SI | - |
| HeaderMinorSubGroup | varchar |  |  | SI | - |
| HeaderOrder | integer |  |  | SI | - |
| HeaderSubGroup | varchar |  |  | SI | - |
| ReportDef | bigint |  |  | SI | - |
| ReportParentHeader | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*