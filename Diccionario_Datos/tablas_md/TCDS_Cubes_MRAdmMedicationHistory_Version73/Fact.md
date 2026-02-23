# TCDS_Cubes_MRAdmMedicationHistory_Version73.Fact

**Schema:** TCDS_Cubes_MRAdmMedicationHistory_Version73
**Columnas:** 13
**Actualizado:** 2026-01-30 15:31:06

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxCreatedHospital | bigint |  |  | SI | Dimension: DxCreatedHospital<br/>
Source: MEDHIST... |
| DxCreatedUserCarProvType | bigint |  |  | SI | Dimension: DxCreatedUserCarProvType<br/>
Source: ... |
| DxDSSEpisodeID | bigint |  |  | SI | Dimension: DxDSSEpisodeID<br/>
Source: MEDHISTMRA... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: MEDHISTMRA... |
| DxNoMedHistory | bigint |  |  | SI | Dimension: DxNoMedHistory<br/>
Source: MEDHISTNoM... |
| DxPrimarySource | bigint |  |  | SI | Dimension: DxPrimarySource<br/>
Source: MEDHISTPr... |
| DxReasonForCorrection | bigint |  |  | SI | Dimension: DxReasonForCorrection<br/>
Source: MED... |
| DxStatus | bigint |  |  | SI | Dimension: DxStatus<br/>
Source: MEDHISTStatus |
| DxUpdateHospital | bigint |  |  | SI | Dimension: DxUpdateHospital<br/>
Source: MEDHISTU... |
| DxUpdateUserCarProvType | bigint |  |  | SI | Dimension: DxUpdateUserCarProvType<br/>
Source: M... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*