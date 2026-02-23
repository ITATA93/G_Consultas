# TCBI_Cubes_MRMedReconciliation.Fact

**Schema:** TCBI_Cubes_MRMedReconciliation
**Columnas:** 43
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1301878156 | varchar |  |  | SI | Dimension: Dx1301878156<br/>
Source: MEDRECSnapsh... |
| Dx1552916911 | varchar |  |  | SI | Dimension: Dx1552916911<br/>
Source: MEDRECCreate... |
| Dx2020491592 | varchar |  |  | SI | Dimension: Dx2020491592<br/>
Source: MEDRECSnapsh... |
| Dx2344873809 | varchar |  |  | SI | Dimension: Dx2344873809<br/>
Source: MEDRECCreate... |
| Dx3443976464 | varchar |  |  | SI | Dimension: Dx3443976464<br/>
Source: MEDRECCreate... |
| Dx3650729986 | varchar |  |  | SI | Dimension: Dx3650729986<br/>
Source: MEDRECSnapsh... |
| Dx4217031777 | varchar |  |  | SI | Dimension: Dx4217031777<br/>
Source: MEDRECCreate... |
| Dx565119811 | varchar |  |  | SI | Dimension: Dx565119811<br/>
Source: MEDRECCreated... |
| Dx896555601 | varchar |  |  | SI | Dimension: Dx896555601<br/>
Source: MEDRECSnapsho... |
| Dx941073601 | varchar |  |  | SI | Dimension: Dx941073601<br/>
Source: MEDRECSnapsho... |
| DxCreatedDayOfWeek | bigint |  |  | SI | Dimension: DxCreatedDayOfWeek
Expression: $system... |
| DxCreatedHospital | bigint |  |  | SI | Dimension: DxCreatedHospital<br/>
Source: MEDRECC... |
| DxCreatedTimeRange | bigint |  |  | SI | Dimension: DxCreatedTimeRange
Expression: %source... |
| DxCreatedUser | bigint |  |  | SI | Dimension: DxCreatedUser<br/>
Source: MEDRECCreat... |
| DxEpisodeAdmToMedRecCreationTimeRange | bigint |  |  | SI | Dimension: DxEpisodeAdmToMedRecCreationTimeRange
... |
| DxEpisodeID | bigint |  |  | SI | Dimension: DxEpisodeID<br/>
Source: MEDRECParRef.... |
| DxErrorReason | bigint |  |  | SI | Dimension: DxErrorReason<br/>
Source: MEDRECError... |
| DxMEDRECCreatedDate | date |  |  | SI | Dimension: DxMEDRECCreatedDate<br/>
Source: MEDRE... |
| DxMEDRECCreatedDateFxYear | varchar |  |  | SI | Dimension: DxMEDRECCreatedDateFxYear<br/>
Source:... |
| DxMEDRECDate | date |  |  | SI | Dimension: DxMEDRECDate<br/>
Source: MEDRECDate |
| DxMEDRECDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxMEDRECDateFxDayMonthYear<br/>
Source... |
| DxMEDRECDateFxMonthNumber | varchar |  |  | SI | Dimension: DxMEDRECDateFxMonthNumber<br/>
Source:... |
| DxMEDRECDateFxMonthYear | varchar |  |  | SI | Dimension: DxMEDRECDateFxMonthYear<br/>
Source: M... |
| DxMEDRECDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxMEDRECDateFxQuarterNumber<br/>
Sourc... |
| DxMEDRECDateFxQuarterYear | varchar |  |  | SI | Dimension: DxMEDRECDateFxQuarterYear<br/>
Source:... |
| DxMEDRECDateFxYear | varchar |  |  | SI | Dimension: DxMEDRECDateFxYear<br/>
Source: MEDREC... |
| DxMEDRECSnapshotDate | date |  |  | SI | Dimension: DxMEDRECSnapshotDate<br/>
Source: MEDR... |
| DxMEDRECSnapshotDateFxYear | varchar |  |  | SI | Dimension: DxMEDRECSnapshotDateFxYear<br/>
Source... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: MEDRECParRef.... |
| DxSnapshotDayOfWeek | bigint |  |  | SI | Dimension: DxSnapshotDayOfWeek
Expression: $syste... |
| DxSnapshotHospital | bigint |  |  | SI | Dimension: DxSnapshotHospital<br/>
Source: MEDREC... |
| DxSnapshotTimeRange | bigint |  |  | SI | Dimension: DxSnapshotTimeRange
Expression: %sourc... |
| DxSnapshotUser | bigint |  |  | SI | Dimension: DxSnapshotUser<br/>
Source: MEDRECSnap... |
| DxStatus | bigint |  |  | SI | Dimension: DxStatus<br/>
Source: MEDRECStatus |
| DxType | bigint |  |  | SI | Dimension: DxType<br/>
Source: MEDRECType |
| DxUpdateDayOfWeek | bigint |  |  | SI | Dimension: DxUpdateDayOfWeek
Expression: $system.... |
| DxUpdateHospital | bigint |  |  | SI | Dimension: DxUpdateHospital<br/>
Source: MEDRECUp... |
| DxUpdateTimeRange | bigint |  |  | SI | Dimension: DxUpdateTimeRange
Expression: %source.... |
| DxUpdateUser | bigint |  |  | SI | Dimension: DxUpdateUser<br/>
Source: MEDRECUserDR... |
| Rx2699981574 | bigint |  |  | SI | Relationship: Rx2699981574<br/>
Source: MEDRECPar... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*