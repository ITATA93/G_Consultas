# lab.CT_PaymentCodeTypes

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPCT_RowID | varchar | PK |  | NO | - |
| CTPCT_Code | varchar |  |  | NO | Code |
| CTPCT_Counter | varchar |  |  | SI | Counter |
| CTPCT_Description | varchar |  |  | SI | Description |
| CTPCT_PathToTransmissionIn | varchar |  |  | SI | Path To Transmission In |
| CTPCT_PathToTransmissionOut | varchar |  |  | SI | Path To Transmission Out |
| CTPCT_Transmission_ID | varchar |  |  | SI | Transmission ID |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*