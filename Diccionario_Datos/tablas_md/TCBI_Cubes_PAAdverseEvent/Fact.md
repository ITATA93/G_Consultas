# TCBI_Cubes_PAAdverseEvent.Fact

**Schema:** TCBI_Cubes_PAAdverseEvent
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1012771450 | varchar |  |  | SI | Dimension: Dx1012771450<br/>
Source: ADEVDateRepo... |
| Dx1162457792 | varchar |  |  | SI | Dimension: Dx1162457792<br/>
Source: ADEVVacSched... |
| Dx1299936232 | varchar |  |  | SI | Dimension: Dx1299936232<br/>
Source: ADEVOnsetDat... |
| Dx1487824696 | date |  |  | SI | Dimension: Dx1487824696<br/>
Source: ADEVVacSched... |
| Dx1719389470 | varchar |  |  | SI | Dimension: Dx1719389470<br/>
Source: ADEVVacSched... |
| Dx2419077245 | varchar |  |  | SI | Dimension: Dx2419077245<br/>
Source: ADEVOnsetDat... |
| Dx2545278826 | varchar |  |  | SI | Dimension: Dx2545278826<br/>
Source: ADEVVacSched... |
| Dx2710737339 | varchar |  |  | SI | Dimension: Dx2710737339<br/>
Source: ADEVOnsetDat... |
| Dx3120645516 | varchar |  |  | SI | Dimension: Dx3120645516<br/>
Source: ADEVVacSched... |
| Dx3454502544 | varchar |  |  | SI | Dimension: Dx3454502544<br/>
Source: ADEVVacSched... |
| Dx3501475881 | varchar |  |  | SI | Dimension: Dx3501475881<br/>
Source: ADEVDateRepo... |
| Dx3773269079 | varchar |  |  | SI | Dimension: Dx3773269079<br/>
Source: ADEVDateRepo... |
| Dx554591427 | varchar |  |  | SI | Dimension: Dx554591427<br/>
Source: ADEVVacSchedD... |
| Dx643136596 | varchar |  |  | SI | Dimension: Dx643136596<br/>
Source: ADEVDateRepor... |
| Dx742966195 | varchar |  |  | SI | Dimension: Dx742966195<br/>
Source: ADEVDateRepor... |
| Dx941992165 | varchar |  |  | SI | Dimension: Dx941992165<br/>
Source: ADEVOnsetDate |
| DxADEVDateReported | date |  |  | SI | Dimension: DxADEVDateReported<br/>
Source: ADEVDa... |
| DxADEVDateReportedFxYear | varchar |  |  | SI | Dimension: DxADEVDateReportedFxYear<br/>
Source: ... |
| DxADEVOnsetDate | date |  |  | SI | Dimension: DxADEVOnsetDate<br/>
Source: ADEVOnset... |
| DxADEVOnsetDateFxMonthYear | varchar |  |  | SI | Dimension: DxADEVOnsetDateFxMonthYear<br/>
Source... |
| DxADEVOnsetDateFxYear | varchar |  |  | SI | Dimension: DxADEVOnsetDateFxYear<br/>
Source: ADE... |
| DxOrderCategory | bigint |  |  | SI | Dimension: DxOrderCategory<br/>
Source: ADEVOrdIt... |
| DxOrderDescription | bigint |  |  | SI | Dimension: DxOrderDescription<br/>
Source: ADEVOr... |
| DxOrderSubCategory | bigint |  |  | SI | Dimension: DxOrderSubCategory<br/>
Source: ADEVOr... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: ADEVParRef.%I... |
| DxType | bigint |  |  | SI | Dimension: DxType
Expression: %cube.GetAdverseEve... |
| RxIDViaADEVParRef | bigint |  |  | SI | Relationship: RxIDViaADEVParRef<br/>
Source: ADEV... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*