# TCBI_Cubes_RTReqVol.Fact

**Schema:** TCBI_Cubes_RTReqVol
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1258904297 | varchar |  |  | SI | Dimension: Dx1258904297<br/>
Source: RTREVRTREQPa... |
| Dx1280606229 | varchar |  |  | SI | Dimension: Dx1280606229<br/>
Source: RTREVMRRetur... |
| Dx1700834247 | varchar |  |  | SI | Dimension: Dx1700834247<br/>
Source: RTREVRTREQPa... |
| Dx170162925 | varchar |  |  | SI | Dimension: Dx170162925<br/>
Source: RTREVRTREQPar... |
| Dx2696766022 | varchar |  |  | SI | Dimension: Dx2696766022<br/>
Source: RTREVMRRetur... |
| Dx3129404111 | varchar |  |  | SI | Dimension: Dx3129404111<br/>
Source: RTREVRTREQPa... |
| Dx362155268 | varchar |  |  | SI | Dimension: Dx362155268<br/>
Source: RTREVMRReturn... |
| Dx3872233662 | varchar |  |  | SI | Dimension: Dx3872233662<br/>
Source: RTREVRTREQPa... |
| Dx4020279384 | varchar |  |  | SI | Dimension: Dx4020279384<br/>
Source: RTREVRTREQPa... |
| Dx4213705143 | varchar |  |  | SI | Dimension: Dx4213705143<br/>
Source: RTREVMRRetur... |
| Dx74195416 | date |  |  | SI | Dimension: Dx74195416<br/>
Source: RTREVRTREQParR... |
| Dx946559050 | varchar |  |  | SI | Dimension: Dx946559050<br/>
Source: RTREVMRReturn... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: RTREVRTMASDR.... |
| DxRTREVMRReturnDate | date |  |  | SI | Dimension: DxRTREVMRReturnDate<br/>
Source: RTREV... |
| DxRTREVMRReturnDateFxYear | varchar |  |  | SI | Dimension: DxRTREVMRReturnDateFxYear<br/>
Source:... |
| DxReasonForRequest | bigint |  |  | SI | Dimension: DxReasonForRequest<br/>
Source: RTREVR... |
| DxRequestStatus | bigint |  |  | SI | Dimension: DxRequestStatus
Expression: %cube.GetR... |
| DxRequestedByCareProvider | bigint |  |  | SI | Dimension: DxRequestedByCareProvider<br/>
Source:... |
| DxRequestedByLocation | bigint |  |  | SI | Dimension: DxRequestedByLocation<br/>
Source: RTR... |
| DxRequestedByUser | bigint |  |  | SI | Dimension: DxRequestedByUser<br/>
Source: RTREVRT... |
| DxVolumePriority | bigint |  |  | SI | Dimension: DxVolumePriority<br/>
Source: RTREVPri... |
| DxVolumeStatus | bigint |  |  | SI | Dimension: DxVolumeStatus<br/>
Source: RTREVStatu... |
| RxIDViaRTREVMasVolDR | bigint |  | FK | SI | Relationship: RxIDViaRTREVMasVolDR<br/>
Source: R... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*