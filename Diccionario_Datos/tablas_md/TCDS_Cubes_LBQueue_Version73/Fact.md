# TCDS_Cubes_LBQueue_Version73.Fact

**Schema:** TCDS_Cubes_LBQueue_Version73
**Columnas:** 27
**Actualizado:** 2026-01-30 15:30:44

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx2553728747 | bigint |  |  | SI | Dimension: Dx2553728747
Expression: %source.LBQOu... |
| Dx3185330620 | bigint |  |  | SI | Dimension: Dx3185330620
Expression: %source.LBQIn... |
| Dx4291813178 | bigint |  |  | SI | Dimension: Dx4291813178
Expression: $ztime(%sourc... |
| Dx496739339 | bigint |  |  | SI | Dimension: Dx496739339
Expression: $ztime(%source... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBQTestS... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBQTestS... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: LBQTestS... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBQTestSet... |
| DxInUser | bigint |  |  | SI | Dimension: DxInUser<br/>
Source: LBQInUser.SSUSRN... |
| DxLBQInDate | date |  |  | SI | Dimension: DxLBQInDate<br/>
Source: LBQInDate |
| DxLBQInDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxLBQInDateFxDayMonthYear<br/>
Source:... |
| DxLBQInDateFxMonthNumber | varchar |  |  | SI | Dimension: DxLBQInDateFxMonthNumber<br/>
Source: ... |
| DxLBQInDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBQInDateFxMonthYear<br/>
Source: LB... |
| DxLBQInDateFxYear | varchar |  |  | SI | Dimension: DxLBQInDateFxYear<br/>
Source: LBQInDa... |
| DxLBQOutDate | date |  |  | SI | Dimension: DxLBQOutDate<br/>
Source: LBQOutDate |
| DxLBQOutDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxLBQOutDateFxDayMonthYear<br/>
Source... |
| DxLBQOutDateFxMonthNumber | varchar |  |  | SI | Dimension: DxLBQOutDateFxMonthNumber<br/>
Source:... |
| DxLBQOutDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBQOutDateFxMonthYear<br/>
Source: L... |
| DxLBQOutDateFxYear | varchar |  |  | SI | Dimension: DxLBQOutDateFxYear<br/>
Source: LBQOut... |
| DxOutUser | bigint |  |  | SI | Dimension: DxOutUser<br/>
Source: LBQOutUser.SSUS... |
| DxQType | bigint |  |  | SI | Dimension: DxQType
Expression: %expression.QType |
| DxQueue | bigint |  |  | SI | Dimension: DxQueue<br/>
Source: LBQQueueDR.LBCQDe... |
| MxNumberFinal | double |  |  | SI | Measure: MxNumberFinal
Expression: %source.LBQOut... |
| MxNumberPending | double |  |  | SI | Measure: MxNumberPending
Expression: %source.LBQO... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*