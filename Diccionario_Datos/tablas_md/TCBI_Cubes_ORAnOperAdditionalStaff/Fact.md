# TCBI_Cubes_ORAnOperAdditionalStaff.Fact

**Schema:** TCBI_Cubes_ORAnOperAdditionalStaff
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
| Dx1148682386 | varchar |  |  | SI | Dimension: Dx1148682386<br/>
Source: OPASStartDat... |
| Dx1580041930 | varchar |  |  | SI | Dimension: Dx1580041930<br/>
Source: OPASStartDat... |
| Dx3283923750 | varchar |  |  | SI | Dimension: Dx3283923750<br/>
Source: OPASStartDat... |
| Dx750700343 | varchar |  |  | SI | Dimension: Dx750700343<br/>
Source: OPASEndDate |
| Dx794120565 | varchar |  |  | SI | Dimension: Dx794120565<br/>
Source: OPASStartDate |
| DxCareProvider | bigint |  |  | SI | Dimension: DxCareProvider<br/>
Source: OPASCarePr... |
| DxCareProviderRole | bigint |  |  | SI | Dimension: DxCareProviderRole<br/>
Source: OPASOp... |
| DxCreateHospital | bigint |  |  | SI | Dimension: DxCreateHospital<br/>
Source: OPASCPLo... |
| DxOPASEndDate | date |  |  | SI | Dimension: DxOPASEndDate<br/>
Source: OPASEndDate |
| DxOPASEndDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxOPASEndDateFxDayMonthYear<br/>
Sourc... |
| DxOPASEndDateFxMonthNumber | varchar |  |  | SI | Dimension: DxOPASEndDateFxMonthNumber<br/>
Source... |
| DxOPASEndDateFxMonthYear | varchar |  |  | SI | Dimension: DxOPASEndDateFxMonthYear<br/>
Source: ... |
| DxOPASEndDateFxQuarterYear | varchar |  |  | SI | Dimension: DxOPASEndDateFxQuarterYear<br/>
Source... |
| DxOPASEndDateFxYear | varchar |  |  | SI | Dimension: DxOPASEndDateFxYear<br/>
Source: OPASE... |
| DxOPASStartDate | date |  |  | SI | Dimension: DxOPASStartDate<br/>
Source: OPASStart... |
| DxOPASStartDateFxMonthYear | varchar |  |  | SI | Dimension: DxOPASStartDateFxMonthYear<br/>
Source... |
| DxOPASStartDateFxYear | varchar |  |  | SI | Dimension: DxOPASStartDateFxYear<br/>
Source: OPA... |
| DxOperation | bigint |  |  | SI | Dimension: DxOperation<br/>
Source: OPASOperation... |
| DxProcedure | bigint |  |  | SI | Dimension: DxProcedure<br/>
Source: OPASStatePPPD... |
| RxIDViaOPASParRef | bigint |  |  | SI | Relationship: RxIDViaOPASParRef<br/>
Source: OPAS... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*