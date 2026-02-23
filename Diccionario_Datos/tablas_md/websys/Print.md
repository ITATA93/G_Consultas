# websys.Print

> "Control and manage print destinations and print Reports.<br>

**Schema:** websys
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Control and manage print destinations and print Reports.<br>

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Courier | bigint |  |  | SI | The Courier for whom the report was requested. |
| IP | varchar |  |  | SI | The ComputerName from which the report was request... |
| LocalPrinter | bit |  |  | SI | - |
| LocalPrinterDialog | bit |  |  | SI | - |
| Location | bigint |  |  | SI | The Location from which the report was requested. ... |
| PaperOrientation | varchar |  |  | SI | - |
| PaperSource | varchar |  |  | SI | - |
| PrintServer | integer |  |  | SI | Flag to trigger server printing |
| Printer | bigint |  |  | SI | The printer on which the report will be generated. |
| Report | bigint |  |  | SI | - |
| ReportGroup | bigint |  |  | SI | - |
| TempOverridePrinter | bigint |  |  | SI | The printer for temporary re-direction. |
| UserID | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*