# TCBI_Cubes_SSSecurityOverride.Fact

**Schema:** TCBI_Cubes_SSSecurityOverride
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| DxCareProvider | bigint |  |  | SI | Dimension: DxCareProvider<br/>
Source: SECOVUserD... |
| DxOverrideTimeRange | bigint |  |  | SI | Dimension: DxOverrideTimeRange
Expression: %sourc... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: SECOVPatientD... |
| DxPatientNumber | bigint |  |  | SI | Dimension: DxPatientNumber<br/>
Source: SECOVPati... |
| DxSECOVDate | date |  |  | SI | Dimension: DxSECOVDate<br/>
Source: SECOVDate |
| DxSECOVDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxSECOVDateFxDayMonthYear<br/>
Source:... |
| DxSECOVDateFxMonthNumber | varchar |  |  | SI | Dimension: DxSECOVDateFxMonthNumber<br/>
Source: ... |
| DxSECOVDateFxMonthYear | varchar |  |  | SI | Dimension: DxSECOVDateFxMonthYear<br/>
Source: SE... |
| DxSECOVDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxSECOVDateFxQuarterNumber<br/>
Source... |
| DxSECOVDateFxQuarterYear | varchar |  |  | SI | Dimension: DxSECOVDateFxQuarterYear<br/>
Source: ... |
| DxSECOVDateFxYear | varchar |  |  | SI | Dimension: DxSECOVDateFxYear<br/>
Source: SECOVDa... |
| MxActualOverrides | double |  |  | SI | Measure: MxActualOverrides
Expression: %cube.GetO... |
| RxIDViaSECOVPatientDR | bigint |  | FK | SI | Relationship: RxIDViaSECOVPatientDR<br/>
Source: ... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*