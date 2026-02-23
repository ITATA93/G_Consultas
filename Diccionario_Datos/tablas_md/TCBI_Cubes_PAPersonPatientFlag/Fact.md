# TCBI_Cubes_PAPersonPatientFlag.Fact

**Schema:** TCBI_Cubes_PAPersonPatientFlag
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1348174519 | varchar |  |  | SI | Dimension: Dx1348174519<br/>
Source: FLAGDateFrom |
| Dx356351631 | varchar |  |  | SI | Dimension: Dx356351631<br/>
Source: FLAGDateFrom |
| DxFLAGDateFrom | date |  |  | SI | Dimension: DxFLAGDateFrom<br/>
Source: FLAGDateFr... |
| DxFLAGDateFromFxMonthNumber | varchar |  |  | SI | Dimension: DxFLAGDateFromFxMonthNumber<br/>
Sourc... |
| DxFLAGDateFromFxMonthYear | varchar |  |  | SI | Dimension: DxFLAGDateFromFxMonthYear<br/>
Source:... |
| DxFLAGDateFromFxQuarterYear | varchar |  |  | SI | Dimension: DxFLAGDateFromFxQuarterYear<br/>
Sourc... |
| DxFLAGDateFromFxYear | varchar |  |  | SI | Dimension: DxFLAGDateFromFxYear<br/>
Source: FLAG... |
| DxFLAGDateTo | date |  |  | SI | Dimension: DxFLAGDateTo<br/>
Source: FLAGDateTo |
| DxFLAGDateToFxDayMonthYear | varchar |  |  | SI | Dimension: DxFLAGDateToFxDayMonthYear<br/>
Source... |
| DxFLAGDateToFxMonthNumber | varchar |  |  | SI | Dimension: DxFLAGDateToFxMonthNumber<br/>
Source:... |
| DxFLAGDateToFxMonthYear | varchar |  |  | SI | Dimension: DxFLAGDateToFxMonthYear<br/>
Source: F... |
| DxFLAGDateToFxQuarterNumber | varchar |  |  | SI | Dimension: DxFLAGDateToFxQuarterNumber<br/>
Sourc... |
| DxFLAGDateToFxQuarterYear | varchar |  |  | SI | Dimension: DxFLAGDateToFxQuarterYear<br/>
Source:... |
| DxFLAGDateToFxYear | varchar |  |  | SI | Dimension: DxFLAGDateToFxYear<br/>
Source: FLAGDa... |
| DxPatientFlagDescription | bigint |  |  | SI | Dimension: DxPatientFlagDescription
Expression: %... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: FLAGParRef.PA... |
| RxIDViaFLAGParRef | bigint |  |  | SI | Relationship: RxIDViaFLAGParRef<br/>
Source: FLAG... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*