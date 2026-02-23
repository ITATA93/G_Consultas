# SQLUser.OE_OrderItemChangeExec

**Schema:** SQLUser
**Columnas:** 57
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OICHEX_RowId | bigint | PK |  | NO | - |
| ChildQ35DR | - |  |  | SI | Child Reference: Ankle |
| OICHEX_ActDoseDrugDelRate | varchar |  |  | SI | Actual Dose Drug Delivery Rate   |
| OICHEX_ActDoseDrugDelRateCalcMeth | varchar |  |  | SI | Actual Dose Drug Delivery Calculation Method Unit ... |
| OICHEX_ActDoseDrugDelRateUom_DR | bigint |  | FK | SI | Des Ref CTUOM |
| OICHEX_ActDoseDrugFlowRate | varchar |  |  | SI | Actual Dose Drug Flow Rate     |
| OICHEX_ActDoseDrugFlowRateUnit | varchar |  |  | SI | Actual Dose Drug Flow Rate Unit     |
| OICHEX_ActDoseDrugFlowTime | varchar |  |  | SI | Actual Dose Drug Flow Time     |
| OICHEX_ActDoseDrugFlowTimeUnit | varchar |  |  | SI | Actual Dose Drug Flow Time Unit    |
| OICHEX_Action | varchar |  |  | SI | Action    |
| OICHEX_ActualDate | date |  |  | SI | Actual Date |
| OICHEX_ActualDose | double |  |  | SI | ActualDose |
| OICHEX_ActualDoseUom_DR | bigint |  | FK | SI | Des Ref CTUOM |
| OICHEX_ActualTime | time |  |  | SI | ActualTime |
| OICHEX_ActualUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| OICHEX_AdminStatusChReason_DR | bigint |  | FK | SI | Des Ref OECAdminStatusChReason |
| OICHEX_BagChanged | varchar |  |  | SI | Bag Changed |
| OICHEX_BolusAmt | double |  |  | SI | BolusAmt  |
| OICHEX_BolusUOM_DR | bigint |  | FK | SI | BolusUOM |
| OICHEX_ChosenAdminRoute_DR | bigint |  | FK | SI | Des Ref AdminRoute Chosen from PHCAdminRouteMultiR... |
| OICHEX_ChosenForm_DR | bigint |  | FK | SI | Des Ref PHCForm Chosen from Form |
| OICHEX_ChosenIVType | varchar |  |  | SI | Chosen IV Type |
| OICHEX_Comments | varchar |  |  | SI | - |
| OICHEX_DeferAdminReason | varchar |  |  | SI | Reason for Deferment |
| OICHEX_OrdExecVolRateChange_DR | varchar |  | FK | SI | Des Ref OEOrdExecVolRateChange  |
| OICHEX_OrdExec_DR | varchar |  | FK | SI | Des Ref OEOrdExec  |
| OICHEX_OrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem  |
| OICHEX_OrderAdminStatus_DR | bigint |  | FK | SI | Des Ref OECOrderAdminStatus   |
| OICHEX_OverseeUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| OICHEX_PlanDoseDrugDelRate | varchar |  |  | SI | Planned Dose Drug Delivery Rate   |
| OICHEX_PlanDoseDrugDelRateCalcMeth | varchar |  |  | SI | Planned Dose Drug Delivery Calculation Method Unit... |
| OICHEX_PlanDoseDrugDelRateUom_DR | bigint |  | FK | SI | Des Ref CTUOM |
| OICHEX_PlanDoseDrugFlowRate | varchar |  |  | SI | Planned Dose Drug Flow Rate     |
| OICHEX_PlanDoseDrugFlowRateUnit | varchar |  |  | SI | Planned Dose Drug Flow Rate Unit     |
| OICHEX_PlanDoseDrugFlowTime | varchar |  |  | SI | Planned Dose Drug Flow Time     |
| OICHEX_PlanDoseDrugFlowTimeUnit | varchar |  |  | SI | Planned Dose Drug Flow Time Unit    |
| OICHEX_PlannedDate | date |  |  | SI | Planned Date |
| OICHEX_PlannedDose | double |  |  | SI | PlannedDose |
| OICHEX_PlannedDoseUom_DR | bigint |  | FK | SI | Des Ref CTUOM |
| OICHEX_PlannedOver | varchar |  |  | SI | PlannedOver    |
| OICHEX_PlannedOverUnit | varchar |  |  | SI | PlannedOverUnit    |
| OICHEX_PlannedTime | time |  |  | SI | PlannedTime |
| OICHEX_PlannedUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| OICHEX_Reason_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason  |
| OICHEX_TotalVolInfused | double |  |  | SI | Total Volume Infused |
| OICHEX_UpdatedDate | date |  |  | SI | Updated Date |
| OICHEX_UpdatedTime | time |  |  | SI | UpdatedTime |
| OICHEX_UpdatedUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| OICHEX_VarianceReason_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason |
| Q34Q1 | - |  |  | SI | Movement |
| Q34Q2 | - |  |  | SI | Strength - Right |
| Q34Q3 | - |  |  | SI | Strength - Left |
| Q34Q4 | - |  |  | SI | AROM - Right |
| Q34Q5 | - |  |  | SI | AROM - Left |
| Q34Q6 | - |  |  | SI | PROM - Right |
| Q34Q7 | - |  |  | SI | PROM - Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*