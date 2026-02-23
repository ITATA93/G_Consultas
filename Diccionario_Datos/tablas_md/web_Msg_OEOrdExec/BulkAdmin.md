# web_Msg_OEOrdExec.BulkAdmin

**Schema:** web_Msg_OEOrdExec
**Columnas:** 47
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AdminVolumeOK | bit |  |  | SI | This property tracks whether the volume of the sel... |
| AdministrationLine | varchar |  |  | SI | Administration Line  |
| BarcodeIcon | varchar |  |  | SI | Barcode Scan Icon |
| BarcodeScanResult | varchar |  |  | SI | Barcode Scan Result as constructed by web.OEOrdExe... |
| BlockingCondition | varchar |  |  | SI | Property to display node blocking condition, if ap... |
| BulkAdminStatus | varchar |  |  | SI | Internal Description of Bulk Admin Status, referen... |
| CanBeDeferred | bit |  |  | SI | Boolean to keep track if defer action is allowed  |
| CanBeNotAdmined | bit |  |  | SI | Boolean to keep track if Mark as NOT administered ... |
| CanBeSkipped | bit |  |  | SI | Boolean to keep track if skip action is allowed |
| DispensedBatchInfo | varchar |  |  | SI | Dispensed Batch Information if any |
| ExternalBulkAdminStatus | varchar |  |  | SI | External Description of Bulk Admin Status, this de... |
| FirstExecNode | bit |  |  | SI | Indicates if this node will be the first execution... |
| GenericDesc | varchar |  |  | SI | Generic Description of the order item |
| ID | varchar |  |  | NO | - |
| ITM2NonMeteredDose | varchar |  |  | SI | Non Metered Dose |
| ITM2TimeCriticalWindow | varchar |  |  | SI | Critical Time Window as minutes |
| IVPushAdminVolume | double |  |  | SI | The administration volume for IVPush administratio... |
| IVType | varchar |  |  | SI | Property to display Order Item IVType (if not appl... |
| Icon | varchar |  |  | SI | Status icon to display in row |
| IconStyle | varchar |  |  | SI | Styling for icon |
| IsAdmixture | bit |  |  | SI | Whether the node is an admixture |
| IsOrderItemPRN | bit |  |  | SI | is Order Item  PRN Order |
| IsPRNWithoutFreq | bit |  |  | SI | if the PRN Order is prescribed without frequency |
| MarkAsText | varchar |  |  | SI | Mark as text to show what status will be applied u... |
| NeedsResolve | bit |  |  | SI | Whether the medication still needs resolve |
| NodeNotReadyReasons | varchar |  |  | SI | Reasons that the node is not ready to be administe... |
| OEOREDeferAdmin | varchar |  |  | SI | "Y" for Deferred; "N", Not Deferred (before Bulk A... |
| OEOREExStDate | date |  |  | SI | Planned Node Start Date |
| OEOREExStTime | time |  |  | SI | Planned Node Start Time |
| OEOREMinPhQtyOrd | varchar |  |  | SI | Minimum Quantity Ordered |
| OEOREOrderStatusID | varchar |  |  | SI | The original Node Status ID (before actioning from... |
| OEOREPhQtyOrd | varchar |  |  | SI | To Administer Quanitity  |
| OEORISttDat | date |  |  | SI | Order Start Date |
| OEORISttTim | time |  |  | SI | Order Start Time |
| OEORIUnitID | varchar |  |  | SI | Order Level Units of Measurement |
| OEOrdExecDR | varchar |  | FK | SI | Foreign Key to Node ID |
| PRNReason | varchar |  |  | SI | User Entered PRN Reason  |
| ReadOnly | bit |  |  | SI | - |
| SaveAsDeferred | varchar |  |  | SI | Property to indicate that the node will be saved a... |
| SaveAsNotAdmined | varchar |  |  | SI | Property to indicate that the node will be saved a... |
| SessionId | varchar |  |  | SI | - |
| StockItemAdminVolumeConfigured | bit |  |  | SI | This property tracks whether the selected stock it... |
| StockSupplyLocationID | varchar |  |  | SI | Stock Supply Location ID |
| VarianceReasonRequired | bit |  |  | SI | Boolean to indicate if the node needs a variance r... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*