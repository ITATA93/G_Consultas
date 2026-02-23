# TCBI_Cubes_MRObservations.Fact

**Schema:** TCBI_Cubes_MRObservations
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
| Dx1400653051 | bigint |  |  | SI | Dimension: Dx1400653051<br/>
Source: OBSEntryDR.O... |
| Dx3989971789 | bigint |  |  | SI | Dimension: Dx3989971789<br/>
Source: OBSEntryDR.O... |
| DxEarlyWarningSignScore | bigint |  |  | SI | Dimension: DxEarlyWarningSignScore<br/>
Source: O... |
| DxOBSDate | date |  |  | SI | Dimension: DxOBSDate<br/>
Source: OBSDate |
| DxOBSDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxOBSDateFxDayMonthYear<br/>
Source: O... |
| DxOBSDateFxMonthNumber | varchar |  |  | SI | Dimension: DxOBSDateFxMonthNumber<br/>
Source: OB... |
| DxOBSDateFxMonthYear | varchar |  |  | SI | Dimension: DxOBSDateFxMonthYear<br/>
Source: OBSD... |
| DxOBSDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxOBSDateFxQuarterNumber<br/>
Source: ... |
| DxOBSDateFxQuarterYear | varchar |  |  | SI | Dimension: DxOBSDateFxQuarterYear<br/>
Source: OB... |
| DxOBSDateFxYear | varchar |  |  | SI | Dimension: DxOBSDateFxYear<br/>
Source: OBSDate |
| DxObservationCode | bigint |  |  | SI | Dimension: DxObservationCode<br/>
Source: OBSItem... |
| DxObservationDescription | bigint |  |  | SI | Dimension: DxObservationDescription<br/>
Source: ... |
| DxObservationStatus | bigint |  |  | SI | Dimension: DxObservationStatus<br/>
Source: OBSOB... |
| DxObservationUnitOfMeasure | bigint |  |  | SI | Dimension: DxObservationUnitOfMeasure<br/>
Source... |
| DxObservationValue | bigint |  |  | SI | Dimension: DxObservationValue
Expression: %expres... |
| DxObservationValueNumber | bigint |  |  | SI | Dimension: DxObservationValueNumber
Expression: %... |
| Rx2564711593 | bigint |  |  | SI | Relationship: Rx2564711593<br/>
Source: OBSParRef... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*