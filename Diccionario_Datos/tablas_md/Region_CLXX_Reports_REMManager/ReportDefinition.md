# Region_CLXX_Reports_REMManager.ReportDefinition

**Schema:** Region_CLXX_Reports_REMManager
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Reportes Regionales**. Informes y estadísticas locales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ImportedVersion | varchar |  |  | SI | - |
| LastUserUpdate | varchar |  |  | SI | - |
| NotUseSystemDate | bit |  |  | SI | - |
| ReportDataExt | bigint |  |  | SI | - |
| ReportProcess | bigint |  |  | SI | - |
| RptActive | integer |  |  | SI | - |
| RptActiveTimeFrom | time |  |  | SI | - |
| RptActiveTimeTo | time |  |  | SI | - |
| RptCode | varchar |  |  | NO | - |
| RptDataExt | bigint |  |  | SI | - |
| RptDesc | varchar |  |  | NO | - |
| RptFilterField | varchar |  |  | SI | - |
| RptFullCode | varchar |  |  | SI | - |
| RptGlobalFilter | varchar |  |  | SI | - |
| RptInternalDesc | varchar |  |  | SI | - |
| RptInternalVersion | varchar |  |  | SI | - |
| RptMinorCode | varchar |  |  | SI | - |
| RptNivel | varchar |  |  | SI | - |
| RptPivotSubGroupTitle | varchar |  |  | SI | - |
| RptPivotTitle | varchar |  |  | SI | - |
| RptProcess | bigint |  |  | SI | - |
| RptSubCode | varchar |  |  | SI | - |
| RptType | integer |  |  | NO | - |
| RptVersionCode | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*