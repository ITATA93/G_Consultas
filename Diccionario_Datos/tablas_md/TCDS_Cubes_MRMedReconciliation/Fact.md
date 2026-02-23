# TCDS_Cubes_MRMedReconciliation.Fact

**Schema:** TCDS_Cubes_MRMedReconciliation
**Columnas:** 12
**Actualizado:** 2026-01-30 15:31:09

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxCreatedHospital | bigint |  |  | SI | Dimension: DxCreatedHospital<br/>
Source: MEDRECC... |
| DxCreatedUserCarProvType | bigint |  |  | SI | Dimension: DxCreatedUserCarProvType<br/>
Source: ... |
| DxDSSEpisodeID | bigint |  |  | SI | Dimension: DxDSSEpisodeID<br/>
Source: MEDRECParR... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: MEDRECParR... |
| DxErrorReason | bigint |  |  | SI | Dimension: DxErrorReason<br/>
Source: MEDRECError... |
| DxStatus | bigint |  |  | SI | Dimension: DxStatus<br/>
Source: MEDRECStatus |
| DxType | bigint |  |  | SI | Dimension: DxType<br/>
Source: MEDRECType |
| DxUpdateHospital | bigint |  |  | SI | Dimension: DxUpdateHospital<br/>
Source: MEDRECUp... |
| DxUpdateUserCarProvType | bigint |  |  | SI | Dimension: DxUpdateUserCarProvType<br/>
Source: M... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*