# TCBI_Cubes_PAProblem.Fact

**Schema:** TCBI_Cubes_PAProblem
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1666313982 | varchar |  |  | SI | Dimension: Dx1666313982<br/>
Source: PROBEndDate |
| Dx2336153956 | varchar |  |  | SI | Dimension: Dx2336153956<br/>
Source: PROBOnsetDat... |
| Dx3574198514 | varchar |  |  | SI | Dimension: Dx3574198514<br/>
Source: PROBOnsetDat... |
| Dx928107184 | varchar |  |  | SI | Dimension: Dx928107184<br/>
Source: PROBOnsetDate |
| Dx970986145 | varchar |  |  | SI | Dimension: Dx970986145<br/>
Source: PROBOnsetDate |
| DxCareProvider | bigint |  |  | SI | Dimension: DxCareProvider<br/>
Source: PROBRespCP... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: PROBRespLocDR.... |
| DxPROBEndDate | date |  |  | SI | Dimension: DxPROBEndDate<br/>
Source: PROBEndDate |
| DxPROBEndDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxPROBEndDateFxDayMonthYear<br/>
Sourc... |
| DxPROBEndDateFxMonthNumber | varchar |  |  | SI | Dimension: DxPROBEndDateFxMonthNumber<br/>
Source... |
| DxPROBEndDateFxMonthYear | varchar |  |  | SI | Dimension: DxPROBEndDateFxMonthYear<br/>
Source: ... |
| DxPROBEndDateFxQuarterYear | varchar |  |  | SI | Dimension: DxPROBEndDateFxQuarterYear<br/>
Source... |
| DxPROBEndDateFxYear | varchar |  |  | SI | Dimension: DxPROBEndDateFxYear<br/>
Source: PROBE... |
| DxPROBOnsetDate | date |  |  | SI | Dimension: DxPROBOnsetDate<br/>
Source: PROBOnset... |
| DxPROBOnsetDateFxMonthYear | varchar |  |  | SI | Dimension: DxPROBOnsetDateFxMonthYear<br/>
Source... |
| DxPROBOnsetDateFxYear | varchar |  |  | SI | Dimension: DxPROBOnsetDateFxYear<br/>
Source: PRO... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: PROBParRef.PA... |
| DxProblem | bigint |  |  | SI | Dimension: DxProblem
Expression: ##Class(web.PAPr... |
| DxSeverity | bigint |  |  | SI | Dimension: DxSeverity<br/>
Source: PROBSeverityDR... |
| RxIDViaPROBParRef | bigint |  |  | SI | Relationship: RxIDViaPROBParRef<br/>
Source: PROB... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*