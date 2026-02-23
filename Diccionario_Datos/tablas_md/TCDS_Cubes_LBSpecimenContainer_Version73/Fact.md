# TCDS_Cubes_LBSpecimenContainer_Version73.Fact

**Schema:** TCDS_Cubes_LBSpecimenContainer_Version73
**Columnas:** 33
**Actualizado:** 2026-01-30 15:30:52

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1054869854 | bigint |  |  | SI | Dimension: Dx1054869854<br/>
Source: LBSPCInvalid... |
| Dx1522318459 | bigint |  |  | SI | Dimension: Dx1522318459
Expression: %source.LBSPC... |
| Dx1718909435 | bigint |  |  | SI | Dimension: Dx1718909435
Expression: $ztime(%sourc... |
| Dx191522918 | bigint |  |  | SI | Dimension: Dx191522918
Expression: $ztime(%source... |
| Dx2397359138 | bigint |  |  | SI | Dimension: Dx2397359138
Expression: %source.LBSPC... |
| Dx3032845712 | bigint |  |  | SI | Dimension: Dx3032845712<br/>
Source: LBSPCCollect... |
| Dx3237638165 | bigint |  |  | SI | Dimension: Dx3237638165<br/>
Source: LBSPCReferra... |
| Dx3268698118 | varchar |  |  | SI | Dimension: Dx3268698118<br/>
Source: LBSPCReceive... |
| Dx3471404815 | varchar |  |  | SI | Dimension: Dx3471404815<br/>
Source: LBSPCReceive... |
| Dx581833128 | varchar |  |  | SI | Dimension: Dx581833128<br/>
Source: LBSPCCollecti... |
| Dx937334489 | bigint |  |  | SI | Dimension: Dx937334489<br/>
Source: LBSPCLabSiteD... |
| Dx946952100 | varchar |  |  | SI | Dimension: Dx946952100<br/>
Source: LBSPCCollecti... |
| Dx986881274 | bigint |  |  | SI | Dimension: Dx986881274<br/>
Source: LBSPCInitiati... |
| DxAnatomicalSite | bigint |  |  | SI | Dimension: DxAnatomicalSite<br/>
Source: LBSPCAna... |
| DxAnatomicalSiteQualifier | bigint |  |  | SI | Dimension: DxAnatomicalSiteQualifier<br/>
Source:... |
| DxContainer | bigint |  |  | SI | Dimension: DxContainer<br/>
Source: LBSPCContaine... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBSPCEpi... |
| DxDSSLBTestSetID | varchar |  |  | SI | Dimension: DxDSSLBTestSetID
Expression: %expressi... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBSPCEpiso... |
| DxIDViaLBSPCEpisodeDR | bigint |  | FK | SI | Dimension: DxIDViaLBSPCEpisodeDR<br/>
Source: LBS... |
| DxLBSPCCollected | bigint |  |  | SI | Dimension: DxLBSPCCollected
Expression: %expressi... |
| DxLBSPCCollectionDate | date |  |  | SI | Dimension: DxLBSPCCollectionDate<br/>
Source: LBS... |
| DxLBSPCCollectionDateFxYear | varchar |  |  | SI | Dimension: DxLBSPCCollectionDateFxYear<br/>
Sourc... |
| DxLBSPCReceived | bigint |  |  | SI | Dimension: DxLBSPCReceived
Expression: %expressio... |
| DxLBSPCReceivedDate | date |  |  | SI | Dimension: DxLBSPCReceivedDate<br/>
Source: LBSPC... |
| DxLBSPCReceivedDateFxYear | varchar |  |  | SI | Dimension: DxLBSPCReceivedDateFxYear<br/>
Source:... |
| DxLesion | bigint |  |  | SI | Dimension: DxLesion<br/>
Source: LBSPCLesionDR.LB... |
| DxSpecimen | bigint |  |  | SI | Dimension: DxSpecimen<br/>
Source: LBSPCSpecimenD... |
| MxTotalCollected | double |  |  | SI | Measure: MxTotalCollected
Expression: %source.LBS... |
| MxTotalReceived | double |  |  | SI | Measure: MxTotalReceived
Expression: %source.LBSP... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*