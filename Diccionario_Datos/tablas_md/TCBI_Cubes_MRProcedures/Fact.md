# TCBI_Cubes_MRProcedures.Fact

**Schema:** TCBI_Cubes_MRProcedures
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxPROCDate | date |  |  | SI | Dimension: DxPROCDate<br/>
Source: PROCDate |
| DxPROCDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxPROCDateFxDayMonthYear<br/>
Source: ... |
| DxPROCDateFxMonthNumber | varchar |  |  | SI | Dimension: DxPROCDateFxMonthNumber<br/>
Source: P... |
| DxPROCDateFxMonthYear | varchar |  |  | SI | Dimension: DxPROCDateFxMonthYear<br/>
Source: PRO... |
| DxPROCDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxPROCDateFxQuarterNumber<br/>
Source:... |
| DxPROCDateFxQuarterYear | varchar |  |  | SI | Dimension: DxPROCDateFxQuarterYear<br/>
Source: P... |
| DxPROCDateFxYear | varchar |  |  | SI | Dimension: DxPROCDateFxYear<br/>
Source: PROCDate |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: PROCParRef.MR... |
| DxProcedureCareProvider | bigint |  |  | SI | Dimension: DxProcedureCareProvider<br/>
Source: P... |
| DxProcedureDayOfWeek | bigint |  |  | SI | Dimension: DxProcedureDayOfWeek
Expression: $syst... |
| DxProcedureDescription | bigint |  |  | SI | Dimension: DxProcedureDescription<br/>
Source: PR... |
| DxProcedureStartTimeRange | bigint |  |  | SI | Dimension: DxProcedureStartTimeRange
Expression: ... |
| Rx2623267417 | bigint |  |  | SI | Relationship: Rx2623267417<br/>
Source: PROCParRe... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*