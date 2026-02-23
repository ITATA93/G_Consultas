# TCDS_Cubes_PAQue1_Version73.Fact

**Schema:** TCDS_Cubes_PAQue1_Version73
**Columnas:** 28
**Actualizado:** 2026-01-30 15:31:54

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1607565367 | varchar |  |  | SI | Dimension: Dx1607565367<br/>
Source: QUE1TransDat... |
| Dx2988726433 | varchar |  |  | SI | Dimension: Dx2988726433<br/>
Source: QUE1TransDat... |
| Dx3006816868 | varchar |  |  | SI | Dimension: Dx3006816868<br/>
Source: QUE1TransDat... |
| Dx777768275 | varchar |  |  | SI | Dimension: Dx777768275<br/>
Source: QUE1TransDate |
| DxAcceptedToCollectedTime | bigint |  |  | SI | Dimension: DxAcceptedToCollectedTime
Expression: ... |
| DxAcceptedToPackedTime | bigint |  |  | SI | Dimension: DxAcceptedToPackedTime
Expression: ##c... |
| DxCareProvider | bigint |  |  | SI | Dimension: DxCareProvider<br/>
Source: QUE1CarePr... |
| DxDSSEpisodeID | bigint |  |  | SI | Dimension: DxDSSEpisodeID<br/>
Source: QUE1PAADMD... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: QUE1PAADMD... |
| DxOnQueueToPackedTime | bigint |  |  | SI | Dimension: DxOnQueueToPackedTime
Expression: ##cl... |
| DxOrderingLocation | bigint |  |  | SI | Dimension: DxOrderingLocation<br/>
Source: QUE1Or... |
| DxPackedToCollectedTime | bigint |  |  | SI | Dimension: DxPackedToCollectedTime
Expression: ##... |
| DxPharmacyPriority | bigint |  |  | SI | Dimension: DxPharmacyPriority<br/>
Source: QUE1Pr... |
| DxPharmacyStatus | varchar |  |  | SI | Dimension: DxPharmacyStatus
Expression: %expressi... |
| DxPharmacyStatusCode | varchar |  |  | SI | Dimension: DxPharmacyStatusCode
Expression: %expr... |
| DxPrescriptionType | bigint |  |  | SI | Dimension: DxPrescriptionType<br/>
Source: QUE1PA... |
| DxQUE1TransDate | date |  |  | SI | Dimension: DxQUE1TransDate<br/>
Source: QUE1Trans... |
| DxQUE1TransDateFxMonthYear | varchar |  |  | SI | Dimension: DxQUE1TransDateFxMonthYear<br/>
Source... |
| DxQUE1TransDateFxYear | varchar |  |  | SI | Dimension: DxQUE1TransDateFxYear<br/>
Source: QUE... |
| DxReceivingLocation | bigint |  |  | SI | Dimension: DxReceivingLocation<br/>
Source: QUE1D... |
| DxTransactionDayOfWeek | bigint |  |  | SI | Dimension: DxTransactionDayOfWeek
Expression: ##c... |
| DxTransactionTimeRange | bigint |  |  | SI | Dimension: DxTransactionTimeRange
Expression: %so... |
| MxItemCost | double |  |  | SI | Measure: MxItemCost
Expression: %cube.GetItemCost... |
| MxItems | double |  |  | SI | Measure: MxItems
Expression: %cube.GetOrderItem(%... |
| MxRepeatOrder | double |  |  | SI | Measure: MxRepeatOrder
Expression: %cube.GetRepea... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*