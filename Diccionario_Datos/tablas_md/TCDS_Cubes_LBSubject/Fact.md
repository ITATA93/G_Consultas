# TCDS_Cubes_LBSubject.Fact

**Schema:** TCDS_Cubes_LBSubject
**Columnas:** 21
**Actualizado:** 2026-01-30 15:30:53

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| DxBloodGroup | bigint |  |  | SI | Dimension: DxBloodGroup<br/>
Source: LBSUBBloodGr... |
| DxBloodGroupStatus | bigint |  |  | SI | Dimension: DxBloodGroupStatus
Expression: %expres... |
| DxCity | bigint |  |  | SI | Dimension: DxCity
Expression: %expression.GetSubj... |
| DxCountry | bigint |  |  | SI | Dimension: DxCountry
Expression: %expression.GetS... |
| DxCounty | bigint |  |  | SI | Dimension: DxCounty
Expression: %expression.GetSu... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: %ID |
| DxFacility | bigint |  |  | SI | Dimension: DxFacility<br/>
Source: LBSUBFacilityD... |
| DxFacilityType | bigint |  |  | SI | Dimension: DxFacilityType<br/>
Source: LBSUBFacil... |
| DxLBSUBDob | date |  |  | SI | Dimension: DxLBSUBDob<br/>
Source: LBSUBDob |
| DxLBSUBDobFxDayMonthYear | varchar |  |  | SI | Dimension: DxLBSUBDobFxDayMonthYear<br/>
Source: ... |
| DxLBSUBDobFxMonthYear | varchar |  |  | SI | Dimension: DxLBSUBDobFxMonthYear<br/>
Source: LBS... |
| DxLBSUBDobFxYear | varchar |  |  | SI | Dimension: DxLBSUBDobFxYear<br/>
Source: LBSUBDob |
| DxPostCode | bigint |  |  | SI | Dimension: DxPostCode
Expression: %expression.Get... |
| DxProvince | bigint |  |  | SI | Dimension: DxProvince
Expression: %expression.Get... |
| DxSex | bigint |  |  | SI | Dimension: DxSex<br/>
Source: LBSUBSexDR.CTSEXDes... |
| DxSpecies | bigint |  |  | SI | Dimension: DxSpecies<br/>
Source: LBSUBSpeciesDR.... |
| DxSpeciesBreed | bigint |  |  | SI | Dimension: DxSpeciesBreed<br/>
Source: LBSUBSpeci... |
| DxSubjectType | bigint |  |  | SI | Dimension: DxSubjectType<br/>
Source: LBSUBSubjec... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*