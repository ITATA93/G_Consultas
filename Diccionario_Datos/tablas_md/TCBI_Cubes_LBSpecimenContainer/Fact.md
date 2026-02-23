# TCBI_Cubes_LBSpecimenContainer.Fact

**Schema:** TCBI_Cubes_LBSpecimenContainer
**Columnas:** 42
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1013401588 | varchar |  |  | SI | Dimension: Dx1013401588<br/>
Source: LBSPCInvalid... |
| Dx1054869854 | bigint |  |  | SI | Dimension: Dx1054869854<br/>
Source: LBSPCInvalid... |
| Dx1522318459 | bigint |  |  | SI | Dimension: Dx1522318459
Expression: %source.LBSPC... |
| Dx1564140054 | bigint |  |  | SI | Dimension: Dx1564140054<br/>
Source: LBSPCSourceM... |
| Dx1718909435 | bigint |  |  | SI | Dimension: Dx1718909435
Expression: $ztime(%sourc... |
| Dx191522918 | bigint |  |  | SI | Dimension: Dx191522918
Expression: $ztime(%source... |
| Dx2279356120 | bigint |  |  | SI | Dimension: Dx2279356120<br/>
Source: LBSPCCollect... |
| Dx2325748847 | bigint |  |  | SI | Dimension: Dx2325748847
Expression: $ztime(%sourc... |
| Dx2397359138 | bigint |  |  | SI | Dimension: Dx2397359138
Expression: %source.LBSPC... |
| Dx2423613062 | varchar |  |  | SI | Dimension: Dx2423613062<br/>
Source: LBSPCInvalid... |
| Dx3268698118 | varchar |  |  | SI | Dimension: Dx3268698118<br/>
Source: LBSPCReceive... |
| Dx3471404815 | varchar |  |  | SI | Dimension: Dx3471404815<br/>
Source: LBSPCReceive... |
| Dx3583630669 | bigint |  |  | SI | Dimension: Dx3583630669
Expression: %source.LBSPC... |
| Dx3629596709 | varchar |  |  | SI | Dimension: Dx3629596709<br/>
Source: LBSPCInvalid... |
| Dx581833128 | varchar |  |  | SI | Dimension: Dx581833128<br/>
Source: LBSPCCollecti... |
| Dx937334489 | bigint |  |  | SI | Dimension: Dx937334489<br/>
Source: LBSPCLabSiteD... |
| Dx946952100 | varchar |  |  | SI | Dimension: Dx946952100<br/>
Source: LBSPCCollecti... |
| DxAnatomicalSite | bigint |  |  | SI | Dimension: DxAnatomicalSite<br/>
Source: LBSPCAna... |
| DxCollectionCentre | bigint |  |  | SI | Dimension: DxCollectionCentre<br/>
Source: LBSPCC... |
| DxContainer | bigint |  |  | SI | Dimension: DxContainer<br/>
Source: LBSPCContaine... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBSPCEpiso... |
| DxIDViaLBSPCEpisodeDR | bigint |  | FK | SI | Dimension: DxIDViaLBSPCEpisodeDR<br/>
Source: LBS... |
| DxInitiation | bigint |  |  | SI | Dimension: DxInitiation<br/>
Source: LBSPCInitiat... |
| DxLBSPCCollectionDate | date |  |  | SI | Dimension: DxLBSPCCollectionDate<br/>
Source: LBS... |
| DxLBSPCCollectionDateFxYear | varchar |  |  | SI | Dimension: DxLBSPCCollectionDateFxYear<br/>
Sourc... |
| DxLBSPCInvalidSpecimenDate | date |  |  | SI | Dimension: DxLBSPCInvalidSpecimenDate<br/>
Source... |
| DxLBSPCReceivedDate | date |  |  | SI | Dimension: DxLBSPCReceivedDate<br/>
Source: LBSPC... |
| DxLBSPCReceivedDateFxYear | varchar |  |  | SI | Dimension: DxLBSPCReceivedDateFxYear<br/>
Source:... |
| DxLesion | bigint |  |  | SI | Dimension: DxLesion<br/>
Source: LBSPCLesionDR.LB... |
| DxSourceContainer | varchar |  |  | SI | Dimension: DxSourceContainer
Expression: %express... |
| DxSourceSpecimen | varchar |  |  | SI | Dimension: DxSourceSpecimen
Expression: %expressi... |
| DxSourceType | bigint |  |  | SI | Dimension: DxSourceType
Expression: %expression.S... |
| DxSpecimen | bigint |  |  | SI | Dimension: DxSpecimen<br/>
Source: LBSPCSpecimenD... |
| MxTotalAliquoted | double |  |  | SI | Measure: MxTotalAliquoted
Expression: (%source.LB... |
| MxTotalCollected | double |  |  | SI | Measure: MxTotalCollected
Expression: (%source.LB... |
| MxTotalConvertedFromMaterial | double |  |  | SI | Measure: MxTotalConvertedFromMaterial
Expression:... |
| MxTotalPooled | double |  |  | SI | Measure: MxTotalPooled
Expression: (%source.LBSPC... |
| MxTotalReceived | double |  |  | SI | Measure: MxTotalReceived
Expression: %source.LBSP... |
| RxIDViaLBSPCEpisodeDR | bigint |  | FK | SI | Relationship: RxIDViaLBSPCEpisodeDR<br/>
Source: ... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*