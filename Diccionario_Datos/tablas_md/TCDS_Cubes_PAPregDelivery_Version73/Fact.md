# TCDS_Cubes_PAPregDelivery_Version73.Fact

**Schema:** TCDS_Cubes_PAPregDelivery_Version73
**Columnas:** 42
**Actualizado:** 2026-01-30 15:31:47

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1001380864 | varchar |  |  | SI | Dimension: Dx1001380864<br/>
Source: DELDateOfInd... |
| Dx1090421044 | varchar |  |  | SI | Dimension: Dx1090421044<br/>
Source: DELDateOfInd... |
| Dx1214168933 | varchar |  |  | SI | Dimension: Dx1214168933<br/>
Source: DELLabourOns... |
| Dx1398619375 | varchar |  |  | SI | Dimension: Dx1398619375<br/>
Source: DELLabourOns... |
| Dx1504156440 | varchar |  |  | SI | Dimension: Dx1504156440<br/>
Source: DELLabourOns... |
| Dx2206923021 | varchar |  |  | SI | Dimension: Dx2206923021<br/>
Source: DELMembRuptu... |
| Dx2522192423 | varchar |  |  | SI | Dimension: Dx2522192423<br/>
Source: DELMembRuptu... |
| Dx2525107712 | varchar |  |  | SI | Dimension: Dx2525107712<br/>
Source: DELDateOfInd... |
| Dx2763480374 | varchar |  |  | SI | Dimension: Dx2763480374<br/>
Source: DELLabourOns... |
| Dx3611704915 | varchar |  |  | SI | Dimension: Dx3611704915<br/>
Source: DELDateOfInd... |
| Dx3982501137 | varchar |  |  | SI | Dimension: Dx3982501137<br/>
Source: DELDateOfInd... |
| Dx4023714549 | varchar |  |  | SI | Dimension: Dx4023714549<br/>
Source: DELLabourOns... |
| DxAnalgesia | varchar |  |  | SI | Dimension: DxAnalgesia
Expression: %cube.GetAnalg... |
| DxBabyDelivered | bigint |  |  | SI | Dimension: DxBabyDelivered
Expression: %expressio... |
| DxBloodLoss | bigint |  |  | SI | Dimension: DxBloodLoss<br/>
Source: DELBloodLoss |
| DxBloodTransfusion | bigint |  |  | SI | Dimension: DxBloodTransfusion<br/>
Source: DELBlo... |
| DxDELDateOfInduction | date |  |  | SI | Dimension: DxDELDateOfInduction<br/>
Source: DELD... |
| DxDELDateOfInductionFxYear | varchar |  |  | SI | Dimension: DxDELDateOfInductionFxYear<br/>
Source... |
| DxDELLabourOnsetDate | date |  |  | SI | Dimension: DxDELLabourOnsetDate<br/>
Source: DELL... |
| DxDELLabourOnsetDateFxYear | varchar |  |  | SI | Dimension: DxDELLabourOnsetDateFxYear<br/>
Source... |
| DxDELMembRuptureDate | date |  |  | SI | Dimension: DxDELMembRuptureDate<br/>
Source: DELM... |
| DxDELMembRuptureDateFxYear | varchar |  |  | SI | Dimension: DxDELMembRuptureDateFxYear<br/>
Source... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: DELParRef.... |
| DxDelivery | varchar |  |  | SI | Dimension: DxDelivery
Expression: %cube.GetDelive... |
| DxEpisiotomy | bigint |  |  | SI | Dimension: DxEpisiotomy<br/>
Source: DELEpisTypeD... |
| DxInductionIndicators | bigint |  |  | SI | Dimension: DxInductionIndicators
Expression: %exp... |
| DxInductionInds | bigint |  |  | SI | Dimension: DxInductionInds
Expression: "sourceInd... |
| DxInductionMethod | bigint |  |  | SI | Dimension: DxInductionMethod
Expression: %cube.Ge... |
| DxLabourMethod | bigint |  |  | SI | Dimension: DxLabourMethod<br/>
Source: DELLabourM... |
| DxLabourMethodType | bigint |  |  | SI | Dimension: DxLabourMethodType
Expression: %expres... |
| DxLacerations | varchar |  |  | SI | Dimension: DxLacerations
Expression: %cube.GetLac... |
| DxMethod | bigint |  |  | SI | Dimension: DxMethod
Expression: "sourceMethod" |
| DxMotherOutcome | bigint |  |  | SI | Dimension: DxMotherOutcome<br/>
Source: DELMother... |
| DxPerinealRepair | bigint |  |  | SI | Dimension: DxPerinealRepair<br/>
Source: DELPerin... |
| DxPlurality | bigint |  |  | SI | Dimension: DxPlurality<br/>
Source: DELPlurality.... |
| DxPuerperium | varchar |  |  | SI | Dimension: DxPuerperium
Expression: %cube.GetPuer... |
| DxStage1 | bigint |  |  | SI | Dimension: DxStage1<br/>
Source: DELStage1 |
| DxStage2 | bigint |  |  | SI | Dimension: DxStage2<br/>
Source: DELStage2 |
| DxSterilisation | bigint |  |  | SI | Dimension: DxSterilisation
Expression: %cube.Ster... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*