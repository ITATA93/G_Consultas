# TCBI_Cubes_RTMasVol.Fact

**Schema:** TCBI_Cubes_RTMasVol
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1114666395 | varchar |  |  | SI | Dimension: Dx1114666395<br/>
Source: RTMAVRTMASPa... |
| Dx1194979737 | varchar |  |  | SI | Dimension: Dx1194979737<br/>
Source: RTMAVDateCre... |
| Dx1549813903 | date |  |  | SI | Dimension: Dx1549813903<br/>
Source: RTMAVRTMASPa... |
| Dx1811892518 | varchar |  |  | SI | Dimension: Dx1811892518<br/>
Source: RTMAVRTMASPa... |
| Dx2044745661 | varchar |  |  | SI | Dimension: Dx2044745661<br/>
Source: RTMAVRTMASPa... |
| Dx2266409845 | varchar |  |  | SI | Dimension: Dx2266409845<br/>
Source: RTMAVRTMASPa... |
| Dx2778894468 | varchar |  |  | SI | Dimension: Dx2778894468<br/>
Source: RTMAVDateCre... |
| Dx2882540490 | varchar |  |  | SI | Dimension: Dx2882540490<br/>
Source: RTMAVDateCre... |
| Dx3058772676 | varchar |  |  | SI | Dimension: Dx3058772676<br/>
Source: RTMAVRTMASPa... |
| Dx3705099425 | varchar |  |  | SI | Dimension: Dx3705099425<br/>
Source: RTMAVRTMASPa... |
| Dx4041976437 | varchar |  |  | SI | Dimension: Dx4041976437<br/>
Source: RTMAVDateCre... |
| Dx523086797 | varchar |  |  | SI | Dimension: Dx523086797<br/>
Source: RTMAVDateCrea... |
| DxCreatingLocation | bigint |  |  | SI | Dimension: DxCreatingLocation<br/>
Source: RTMAVR... |
| DxHomeLocation | bigint |  |  | SI | Dimension: DxHomeLocation<br/>
Source: RTMAVRTMAS... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: RTMAVRTMASParR... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: RTMAVRTMASPar... |
| DxRTMAVDateCreated | date |  |  | SI | Dimension: DxRTMAVDateCreated<br/>
Source: RTMAVD... |
| DxRTMAVDateCreatedFxYear | varchar |  |  | SI | Dimension: DxRTMAVDateCreatedFxYear<br/>
Source: ... |
| DxStatus | bigint |  |  | SI | Dimension: DxStatus<br/>
Source: RTMAVRTMASParRef... |
| DxType | bigint |  |  | SI | Dimension: DxType<br/>
Source: RTMAVRTMASParRef.R... |
| DxVolume | bigint |  |  | SI | Dimension: DxVolume<br/>
Source: RTMAVVolDesc |
| DxVolumeCreatingLocation | bigint |  |  | SI | Dimension: DxVolumeCreatingLocation<br/>
Source: ... |
| DxVolumeCurrentLocation | bigint |  |  | SI | Dimension: DxVolumeCurrentLocation<br/>
Source: R... |
| DxVolumeHomeLocation | bigint |  |  | SI | Dimension: DxVolumeHomeLocation<br/>
Source: RTMA... |
| DxVolumeStatus | bigint |  |  | SI | Dimension: DxVolumeStatus<br/>
Source: RTMAVMRSta... |
| DxVolumeType | bigint |  |  | SI | Dimension: DxVolumeType<br/>
Source: RTMAVMRTypeV... |
| Rx440985209 | bigint |  |  | SI | Relationship: Rx440985209<br/>
Source: RTMAVRTMAS... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*