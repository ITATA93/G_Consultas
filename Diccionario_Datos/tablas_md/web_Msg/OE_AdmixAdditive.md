# web_Msg.OE_AdmixAdditive

**Schema:** web_Msg
**Columnas:** 51
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| ITM_AdditiveVolume | double |  |  | SI | Additive Volume (mL) |
| ITM_Additive_DR | varchar |  | FK | SI | Additive
Required by User.OEAdmixAdditive. |
| ITM_AdminDrugDeliveryPerUOM | varchar |  |  | SI | Administration Drug Delivery Rate Per UOM |
| ITM_AdminDrugDeliveryRate | double |  |  | SI | Administration Drug Delivery Rate |
| ITM_AdminDrugDeliveryUOM_DR | bigint |  | FK | SI | Administration Drug Delivery Rate UOM |
| ITM_Carrier | varchar |  |  | SI | Carrier |
| ITM_Childsub | double |  |  | SI | Childsub |
| ITM_ConcOverideReason_DR | bigint |  | FK | SI | Reason for Ordered Concentration Override |
| ITM_ConcentrationVariable | varchar |  |  | SI | Concentration Variable |
| ITM_DDRVariable | varchar |  |  | SI | DDR Variable |
| ITM_Date | date |  |  | SI | Date |
| ITM_Dose | double |  |  | SI | Dose |
| ITM_DoseUOM_DR | bigint |  | FK | SI | Dose UOM |
| ITM_DoseVariable | varchar |  |  | SI | Dose Variable |
| ITM_DrgHistDesc_DR | varchar |  | FK | SI | Des Ref PHCDrgHistDesc |
| ITM_DrugDeliveryPerUOM | varchar |  |  | SI | Drug Delivery Rate Per UOM |
| ITM_DrugDeliveryRate | double |  |  | SI | Drug Delivery Rate |
| ITM_DrugDeliveryUOM_DR | bigint |  | FK | SI | Drug Delivery Rate UOM |
| ITM_GenericHistDesc_DR | varchar |  | FK | SI | Des Ref PHCGenericHistDesc |
| ITM_IngrInstruction_DR | bigint |  | FK | SI | Ingredient Instructions |
| ITM_LoadingDoseVariable | varchar |  |  | SI | Loading Dose Variable |
| ITM_MainItem | varchar |  |  | SI | Main Item |
| ITM_ManfConcOverideReason_DR | bigint |  | FK | SI | Reason for Manufactured Concentration Override |
| ITM_ManufacturedVolume | double |  |  | SI | Manufactured Volume (mL) |
| ITM_MaxDrugDeliveryRate | double |  |  | SI | Max Drug Delivery Rate |
| ITM_MinDrugDeliveryRate | double |  |  | SI | Min Drug Delivery Rate |
| ITM_MsgParRef | varchar |  |  | SI | - |
| ITM_MsgUnconfirmedConcentrationChange | varchar |  |  | SI | - |
| ITM_MsgUnconfirmedDDRChange | varchar |  |  | SI | - |
| ITM_MsgUnconfirmedDoseChange | varchar |  |  | SI | - |
| ITM_MsgUnconfirmedLoadingDoseChange | varchar |  |  | SI | - |
| ITM_PCALoadingDose | double |  |  | SI | PCA Loading Dose |
| ITM_PCALoadingDoseUOM_DR | bigint |  | FK | SI | PCA Loading Dose UOM |
| ITM_ParRef | bigint |  |  | SI | OE_OrdAdmix Parent Reference
Required by User.OEA... |
| ITM_PerQuantity | double |  |  | SI | Quantity |
| ITM_PerUOM_DR | bigint |  | FK | SI | UOM |
| ITM_Percentage | double |  |  | SI | Percentage |
| ITM_Quantity | double |  |  | SI | Quantity |
| ITM_ReqPercentage | double |  |  | SI | Required Percentage |
| ITM_ResolvedAdditive_DR | varchar |  | FK | SI | Resolved Additive |
| ITM_RowId | varchar |  |  | SI | - |
| ITM_Significant | varchar |  |  | SI | Significant |
| ITM_Time | time |  |  | SI | Time |
| ITM_TotalBagVolume | double |  |  | SI | Total Bag Volume (mL) |
| ITM_UOM_DR | bigint |  | FK | SI | UOM |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*