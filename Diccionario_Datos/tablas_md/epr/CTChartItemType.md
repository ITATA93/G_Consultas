# epr.CTChartItemType

**Schema:** epr
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CITClass | varchar |  |  | SI | - |
| CITCode | varchar |  |  | NO | - |
| CITDesc | varchar |  |  | SI | - |
| CITEPRPrintCustomReportDR | bigint |  | FK | SI | - |
| CITEditEPRComponentDR | bigint |  | FK | SI | - |
| CITListEPRComponentDR | bigint |  | FK | SI | - |
| CITListProfileComponentDR | bigint |  | FK | SI | - |
| CITURL | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*