# TCBI_Cubes_MRAdmMedicationHistory.Fact

**Schema:** TCBI_Cubes_MRAdmMedicationHistory
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1421000961 | varchar |  |  | SI | Dimension: Dx1421000961<br/>
Source: MEDHISTCreat... |
| Dx2036169267 | varchar |  |  | SI | Dimension: Dx2036169267<br/>
Source: MEDHISTCreat... |
| Dx2038974432 | varchar |  |  | SI | Dimension: Dx2038974432<br/>
Source: MEDHISTCreat... |
| Dx2333107990 | varchar |  |  | SI | Dimension: Dx2333107990<br/>
Source: MEDHISTUpdat... |
| Dx2511640672 | varchar |  |  | SI | Dimension: Dx2511640672<br/>
Source: MEDHISTCreat... |
| Dx2522391833 | varchar |  |  | SI | Dimension: Dx2522391833<br/>
Source: MEDHISTUpdat... |
| Dx3023545876 | varchar |  |  | SI | Dimension: Dx3023545876<br/>
Source: MEDHISTUpdat... |
| Dx3684592668 | varchar |  |  | SI | Dimension: Dx3684592668<br/>
Source: MEDHISTCreat... |
| Dx4062661699 | varchar |  |  | SI | Dimension: Dx4062661699<br/>
Source: MEDHISTUpdat... |
| Dx516861456 | varchar |  |  | SI | Dimension: Dx516861456<br/>
Source: MEDHISTUpdate... |
| DxCreatedDayOfWeek | bigint |  |  | SI | Dimension: DxCreatedDayOfWeek
Expression: $system... |
| DxCreatedHospital | bigint |  |  | SI | Dimension: DxCreatedHospital<br/>
Source: MEDHIST... |
| DxCreatedTimeRange | bigint |  |  | SI | Dimension: DxCreatedTimeRange
Expression: %source... |
| DxCreatedUser | bigint |  |  | SI | Dimension: DxCreatedUser<br/>
Source: MEDHISTCrea... |
| DxEpisodeAdmToMedHxCreationTimeRange | bigint |  |  | SI | Dimension: DxEpisodeAdmToMedHxCreationTimeRange
E... |
| DxEpisodeID | bigint |  |  | SI | Dimension: DxEpisodeID<br/>
Source: MEDHISTMRAdmD... |
| DxMEDHISTCreatedDate | date |  |  | SI | Dimension: DxMEDHISTCreatedDate<br/>
Source: MEDH... |
| DxMEDHISTCreatedDateFxYear | varchar |  |  | SI | Dimension: DxMEDHISTCreatedDateFxYear<br/>
Source... |
| DxMEDHISTUpdateDate | date |  |  | SI | Dimension: DxMEDHISTUpdateDate<br/>
Source: MEDHI... |
| DxMEDHISTUpdateDateFxYear | varchar |  |  | SI | Dimension: DxMEDHISTUpdateDateFxYear<br/>
Source:... |
| DxNoMedHistory | bigint |  |  | SI | Dimension: DxNoMedHistory<br/>
Source: MEDHISTNoM... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: MEDHISTMRAdmD... |
| DxPrimarySource | bigint |  |  | SI | Dimension: DxPrimarySource<br/>
Source: MEDHISTPr... |
| DxReasonForCorrection | bigint |  |  | SI | Dimension: DxReasonForCorrection<br/>
Source: MED... |
| DxStatus | bigint |  |  | SI | Dimension: DxStatus<br/>
Source: MEDHISTStatus |
| DxUpdateDayOfWeek | bigint |  |  | SI | Dimension: DxUpdateDayOfWeek
Expression: $system.... |
| DxUpdateHospital | bigint |  |  | SI | Dimension: DxUpdateHospital<br/>
Source: MEDHISTU... |
| DxUpdateTimeRange | bigint |  |  | SI | Dimension: DxUpdateTimeRange
Expression: %source.... |
| DxUpdateUser | bigint |  |  | SI | Dimension: DxUpdateUser<br/>
Source: MEDHISTUpdat... |
| Rx755534986 | bigint |  |  | SI | Relationship: Rx755534986<br/>
Source: MEDHISTMRA... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*