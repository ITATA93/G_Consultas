# epr.DoseFormulaConfigItem

**Schema:** epr
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Configuración del módulo.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| Code | varchar |  |  | SI | Internal Code
GFR and SerumC [Hard Coded] |
| Description | varchar |  |  | SI | Configurable Description |
| ID | varchar |  |  | NO | - |
| InputItem | varchar |  |  | SI | Actual Input Item Description: for instance: weigh... |
| InputItemCode | varchar |  |  | SI | Actual Input Item Code: for instance: WEIGHT, CR |
| InputSource | varchar |  |  | SI | Input Source: Either Observation Item or Lab Test ... |
| InputSourceCode | varchar |  |  | SI | Input Source Code: hard coded "OI" :Observation; h... |
| Item | varchar |  |  | SI | Internal Item for the internal code |
| MaxSupportedDays | integer |  |  | SI | Max Supported Days to find the actual value based ... |
| UOMDescExternal | varchar |  |  | SI | UOM Description if TrakCare Lab (or any other) but... |
| UOMExt | bigint |  |  | SI | Map To Units: Lab Enterprise UOM  |
| Units | varchar |  |  | SI | Formula Units: Internal Units |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*