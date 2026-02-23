# TCBI_Cubes_PAAdmCoding.Fact

**Schema:** TCBI_Cubes_PAAdmCoding
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx2980991542 | varchar |  |  | SI | Dimension: Dx2980991542<br/>
Source: CODStartDate |
| Dx313743057 | varchar |  |  | SI | Dimension: Dx313743057<br/>
Source: CODStartDate |
| DxCODEndDate | date |  |  | SI | Dimension: DxCODEndDate<br/>
Source: CODEndDate |
| DxCODEndDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxCODEndDateFxDayMonthYear<br/>
Source... |
| DxCODEndDateFxMonthNumber | varchar |  |  | SI | Dimension: DxCODEndDateFxMonthNumber<br/>
Source:... |
| DxCODEndDateFxMonthYear | varchar |  |  | SI | Dimension: DxCODEndDateFxMonthYear<br/>
Source: C... |
| DxCODEndDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxCODEndDateFxQuarterNumber<br/>
Sourc... |
| DxCODEndDateFxQuarterYear | varchar |  |  | SI | Dimension: DxCODEndDateFxQuarterYear<br/>
Source:... |
| DxCODEndDateFxYear | varchar |  |  | SI | Dimension: DxCODEndDateFxYear<br/>
Source: CODEnd... |
| DxCODStartDate | date |  |  | SI | Dimension: DxCODStartDate<br/>
Source: CODStartDa... |
| DxCODStartDateFxMonthNumber | varchar |  |  | SI | Dimension: DxCODStartDateFxMonthNumber<br/>
Sourc... |
| DxCODStartDateFxMonthYear | varchar |  |  | SI | Dimension: DxCODStartDateFxMonthYear<br/>
Source:... |
| DxCODStartDateFxQuarterYear | varchar |  |  | SI | Dimension: DxCODStartDateFxQuarterYear<br/>
Sourc... |
| DxCODStartDateFxYear | varchar |  |  | SI | Dimension: DxCODStartDateFxYear<br/>
Source: CODS... |
| DxCareProvider | bigint |  |  | SI | Dimension: DxCareProvider<br/>
Source: CODCarePro... |
| DxCodingStatus | bigint |  |  | SI | Dimension: DxCodingStatus
Expression: %cube.GetCo... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: CODCTLOCDR.CTL... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: CODParRef.PAA... |
| DxValidationStatus | bigint |  |  | SI | Dimension: DxValidationStatus
Expression: %cube.G... |
| DxWard | bigint |  |  | SI | Dimension: DxWard<br/>
Source: CODWardDR.WARDDesc |
| RxIDViaCODParRef | bigint |  |  | SI | Relationship: RxIDViaCODParRef<br/>
Source: CODPa... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*