# Report_JReport.ConfigurationLogiParameter

**Schema:** Report_JReport
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| DateFrom | date |  |  | SI | Date From column  |
| DateTo | date |  |  | SI | Date To column |
| ID | varchar |  |  | NO | - |
| Parameter | varchar |  |  | NO | Parameter according the std. type |
| Value | varchar |  |  | SI | Value of the parameter |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*