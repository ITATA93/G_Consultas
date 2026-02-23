# web_Msg.OE_Admix

**Schema:** web_Msg
**Columnas:** 57
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AMIVType | varchar |  |  | SI | IV Type, only used if AMOEORIDR is blank |
| AM_AddedAdditiveFlg | varchar |  |  | SI | AMAddedAdditiveFlg |
| AM_AdditiveVolume | double |  |  | SI | Additive Volume (mL) |
| AM_AdministrationFlowRate | double |  |  | SI | Administration Flow Rate |
| AM_AdministrationFlowRatePerUOM | varchar |  |  | SI | Administration Flow Rate Per UOM |
| AM_AdministrationFlowRateUOM_DR | bigint |  | FK | SI | Administration Flow Rate UOM |
| AM_AdmixManufLock | bit |  |  | SI | Lock By Admixture Manufacture |
| AM_AdmixType | varchar |  |  | SI | Admixture Type
Required by User.OEAdmix. |
| AM_AllowToModify | varchar |  |  | SI | Allow to Modify Recipe |
| AM_BulkAdmixtureRecipe_DR | bigint |  | FK | SI | Des Ref Bulk Admixture Recipe |
| AM_BulkQuantity | double |  |  | SI | Bulk Quantity |
| AM_BulkRecLoc_DR | bigint |  | FK | SI | Bulk Receiving Location |
| AM_Date | date |  |  | SI | Date |
| AM_DefineTheFinalVolume | varchar |  |  | SI | Define the Final Volume |
| AM_DrgHistDesc_DR | varchar |  | FK | SI | Des Ref PHCDrgHistDesc |
| AM_FinalForm_DR | bigint |  | FK | SI | Final Form |
| AM_FlowRateVariable | varchar |  |  | SI | Flow Rate Variable |
| AM_GenericHistDesc_DR | varchar |  | FK | SI | Des Ref PHCGenericHistDesc |
| AM_IVMode | varchar |  |  | SI | IVMode |
| AM_IncludeAdditiveVolume | varchar |  |  | SI | Include Additive Volume |
| AM_IncludeOverfillVolume | varchar |  |  | SI | Include Overfill Volume |
| AM_LoadingVolumeVariable | varchar |  |  | SI | Loading Volume Variable |
| AM_MainItem | varchar |  |  | SI | Main Item |
| AM_ManufactureStatus | varchar |  |  | SI | AMManufactureStatus |
| AM_MaxFlowRate | double |  |  | SI | Max Flow Rate |
| AM_MinFlowRate | double |  |  | SI | Min Flow Rate |
| AM_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| AM_OrderedBagVolume | double |  |  | SI | Volume Per Bag (mL) from Order Entry |
| AM_OverfillVolume | double |  |  | SI | Overfill Volume (mL) |
| AM_PCALoadingVolume | double |  |  | SI | PCA Loading Volume |
| AM_PCALoadingVolumeUOM_DR | bigint |  | FK | SI | PCA Loading Volume UOM |
| AM_Quantity | double |  |  | SI | Quantity |
| AM_QuantityVariable | varchar |  |  | SI | Quantity Variable |
| AM_RemainInProgress | varchar |  |  | SI | Remain In progress when is quantity fulfilled |
| AM_ResolvedSolv_DR | varchar |  | FK | SI | Resolved Solvent |
| AM_RowId | varchar |  |  | SI | - |
| AM_SolventBagVolume | double |  |  | SI | Solvent Bag Volume (mL) |
| AM_SolventVolumeBeforeMixing | double |  |  | SI | Solvent Volume Before Mixing (mL) |
| AM_Solvent_DR | varchar |  | FK | SI | Solvent |
| AM_StartingSolventVolume | double |  |  | SI | Starting Solvent Volume (mL) |
| AM_SubtractAdditive | varchar |  |  | SI | Subtract Additive Volumes from Solvent |
| AM_Time | time |  |  | SI | Time |
| AM_TotalBagVolume | double |  |  | SI | Total Final Volume Per Bag (mL) |
| AM_TotalFlowRate | double |  |  | SI | Total Flow Rate |
| AM_TotalFlowRatePerUOM | varchar |  |  | SI | Total Flow Rate Per UOM |
| AM_TotalFlowRateUOM_DR | bigint |  | FK | SI | Total Flow Rate UOM |
| AM_TransactionNo | varchar |  |  | SI | AMTransactionNo |
| AM_UOM_DR | bigint |  | FK | SI | UOM |
| AM_VolumeCalculatorUsed | varchar |  |  | SI | Volume Calculator Used |
| AM_WithdrawVolume | double |  |  | SI | Withdraw Volume (mL) |
| AM_WithoutSolvent | varchar |  |  | SI | Admixture ordered without a solvent |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*