# lab.CT_TestCodeDelta

**Schema:** lab
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTCD_ParRef | varchar | PK |  | NO | CT_TestCode Parent Reference |
| CTTCD_Age | varchar |  |  | SI | Age |
| CTTCD_DeltaType | varchar |  |  | NO | Delta Type |
| CTTCD_DeltaValAbsolute | double |  |  | SI | Delta Value Absolute |
| CTTCD_DeltaValAbsoluteAsc | double |  |  | SI | Delta Value Absolute Asc |
| CTTCD_DeltaValAbsoluteDsc | double |  |  | SI | Delta Value Absolute Dsc |
| CTTCD_DeltaValPerc | double |  |  | SI | Delta Percantage |
| CTTCD_DeltaValPercAsc | double |  |  | SI | Delta Percantage Asc |
| CTTCD_DeltaValPercDsc | double |  |  | SI | Delta Percantage Dsc |
| CTTCD_DeltaValPercRate | double |  |  | SI | Delta Percantage Rate |
| CTTCD_DeltaValPercRateAsc | double |  |  | SI | Delta Percantage Rate Asc |
| CTTCD_DeltaValPercRateDsc | double |  |  | SI | Delta Percantage Rate Dsc |
| CTTCD_DeltaValRate | double |  |  | SI | Delta Value Rate |
| CTTCD_DeltaValRateAsc | double |  |  | SI | Delta Value Rate Asc |
| CTTCD_DeltaValRateDsc | double |  |  | SI | Delta Value Rate Dsc |
| CTTCD_Order | double |  |  | NO | Order |
| CTTCD_RowID | varchar |  |  | NO | - |
| CTTCD_Sex_DR | varchar |  | FK | SI | Sex |
| CTTCD_ValueHigh | double |  |  | SI | Value High |
| CTTCD_ValueLow | double |  |  | SI | Value Low |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*