# TCDS_Cubes_MRProcedures_Version73.Fact

**Schema:** TCDS_Cubes_MRProcedures_Version73
**Columnas:** 16
**Actualizado:** 2026-01-30 15:31:15

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxDSSEpisodeID | bigint |  |  | SI | Dimension: DxDSSEpisodeID<br/>
Source: PROCParRef... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: PROCParRef... |
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
| DxProcedureCareProvider | bigint |  |  | SI | Dimension: DxProcedureCareProvider<br/>
Source: P... |
| DxProcedureDayOfWeek | bigint |  |  | SI | Dimension: DxProcedureDayOfWeek
Expression: "sour... |
| DxProcedureDescription | bigint |  |  | SI | Dimension: DxProcedureDescription<br/>
Source: PR... |
| DxProcedureStartTimeRange | bigint |  |  | SI | Dimension: DxProcedureStartTimeRange
Expression: ... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*