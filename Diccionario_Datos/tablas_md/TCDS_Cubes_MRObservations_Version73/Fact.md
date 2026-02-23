# TCDS_Cubes_MRObservations_Version73.Fact

**Schema:** TCDS_Cubes_MRObservations_Version73
**Columnas:** 22
**Actualizado:** 2026-01-30 15:31:13

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx2899221992 | date |  |  | SI | Dimension: Dx2899221992
Expression: %source.OBSDa... |
| DxDSSEffectiveDate | varchar |  |  | SI | Dimension: DxDSSEffectiveDate |
| DxDSSEpisodeID | bigint |  |  | SI | Dimension: DxDSSEpisodeID<br/>
Source: OBSParRef.... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: OBSParRef.... |
| DxEWSScore | bigint |  |  | SI | Dimension: DxEWSScore<br/>
Source: OBSEWSScore |
| DxOBSDate | date |  |  | SI | Dimension: DxOBSDate<br/>
Source: OBSDate |
| DxOBSDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxOBSDateFxDayMonthYear<br/>
Source: O... |
| DxOBSDateFxMonthNumber | varchar |  |  | SI | Dimension: DxOBSDateFxMonthNumber<br/>
Source: OB... |
| DxOBSDateFxMonthYear | varchar |  |  | SI | Dimension: DxOBSDateFxMonthYear<br/>
Source: OBSD... |
| DxOBSDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxOBSDateFxQuarterNumber<br/>
Source: ... |
| DxOBSDateFxQuarterYear | varchar |  |  | SI | Dimension: DxOBSDateFxQuarterYear<br/>
Source: OB... |
| DxOBSDateFxYear | varchar |  |  | SI | Dimension: DxOBSDateFxYear<br/>
Source: OBSDate |
| DxObsDoctorID | bigint |  |  | SI | Dimension: DxObsDoctorID<br/>
Source: OBSCTCPDR.C... |
| DxObsGroup | bigint |  |  | SI | Dimension: DxObsGroup
Expression: %expression.Get... |
| DxObservationCode | bigint |  |  | SI | Dimension: DxObservationCode<br/>
Source: OBSItem... |
| DxObservationDescription | bigint |  |  | SI | Dimension: DxObservationDescription<br/>
Source: ... |
| DxObservationUnitOfMeasure | bigint |  |  | SI | Dimension: DxObservationUnitOfMeasure<br/>
Source... |
| DxObservationValue | bigint |  |  | SI | Dimension: DxObservationValue<br/>
Source: OBSVal... |
| DxObservationValueNumber | bigint |  |  | SI | Dimension: DxObservationValueNumber
Expression: "... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*