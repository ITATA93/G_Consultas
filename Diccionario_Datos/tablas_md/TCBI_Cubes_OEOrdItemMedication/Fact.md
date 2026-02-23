# TCBI_Cubes_OEOrdItemMedication.Fact

**Schema:** TCBI_Cubes_OEOrdItemMedication
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxDispenseType | bigint |  |  | SI | Dimension: DxDispenseType
Expression: %expression... |
| DxDoseQuantity | bigint |  |  | SI | Dimension: DxDoseQuantity<br/>
Source: OEORIDoseQ... |
| DxDrugControlledCategory | bigint |  |  | SI | Dimension: DxDrugControlledCategory<br/>
Source: ... |
| DxDurationType | bigint |  |  | SI | Dimension: DxDurationType
Expression: %expression... |
| DxDurationUnit | bigint |  |  | SI | Dimension: DxDurationUnit
Expression: %expression... |
| DxDurationValue | bigint |  |  | SI | Dimension: DxDurationValue<br/>
Source: OEORIOEOr... |
| DxEvent | bigint |  |  | SI | Dimension: DxEvent<br/>
Source: OEORIOEOrdItem2DR... |
| DxFormulary | bigint |  |  | SI | Dimension: DxFormulary
Expression: %expression.Fo... |
| DxFrequency | bigint |  |  | SI | Dimension: DxFrequency<br/>
Source: OEORIPHFreqDR... |
| DxGenericDrug | bigint |  |  | SI | Dimension: DxGenericDrug<br/>
Source: OEORIItmMas... |
| DxGenericDrugCode | bigint |  |  | SI | Dimension: DxGenericDrugCode<br/>
Source: OEORIIt... |
| DxPRNFlag | bigint |  |  | SI | Dimension: DxPRNFlag<br/>
Source: OEORIOEOrdItem2... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: OEORIOEORDPar... |
| DxPharmacyCategory | bigint |  |  | SI | Dimension: DxPharmacyCategory<br/>
Source: OEORII... |
| DxPharmacyItem | bigint |  |  | SI | Dimension: DxPharmacyItem<br/>
Source: OEORIItmMa... |
| DxPharmacyItemCode | bigint |  |  | SI | Dimension: DxPharmacyItemCode<br/>
Source: OEORII... |
| DxPharmacySubCategory | bigint |  |  | SI | Dimension: DxPharmacySubCategory<br/>
Source: OEO... |
| DxRoute | bigint |  |  | SI | Dimension: DxRoute<br/>
Source: OEORIAdminRouteDR... |
| DxScheduledDrugClass | bigint |  |  | SI | Dimension: DxScheduledDrugClass<br/>
Source: OEOR... |
| Rx818000209 | bigint |  |  | SI | Relationship: Rx818000209<br/>
Source: OEORIOEORD... |
| RxID | bigint |  |  | SI | Relationship: RxID<br/>
Source: %ID |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*